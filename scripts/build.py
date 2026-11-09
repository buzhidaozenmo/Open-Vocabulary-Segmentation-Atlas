#!/usr/bin/env python3
"""Validate source notes and generate a disposable MkDocs input tree."""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import yaml
from methods import generate_methods, note_modules, validate_methods

ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / '.codex_tmp/docs'
GROUPS = {
    '3d': '3D 点云', '2d': '2D 图像', 'video': '视频',
    'multiview': 'RGB-D / 多视角', '3dgs': 'NeRF / 3DGS',
    'rgbt': 'RGB-T / 多光谱', 'audio': '音视频',
    'remote': '遥感', 'medical': '医学影像',
}
LEVELS = {'detailed_sample': '样例笔记', 'index': '已建索引'}
README_START = '<!-- PAPERS:START -->'
README_END = '<!-- PAPERS:END -->'


def readme_catalogue(papers):
    """Render the GitHub-native catalogue from the same source as the website."""
    populated = [(key, label) for key, label in GROUPS.items()
                 if any(p['primary_direction'] == key for p in papers)]
    anchors = {'3d': 'papers-3d', '2d': 'papers-2d', 'video': 'papers-video',
               'multiview': 'papers-multiview', '3dgs': 'papers-3dgs',
               'rgbt': 'papers-rgbt', 'audio': 'papers-audio',
               'remote': 'papers-remote', 'medical': 'papers-medical'}
    n = len(papers)
    samples = sum(p['content_status'] == 'detailed_sample' for p in papers)
    chunks = [README_START, '\n## 论文目录\n',
              f'当前收录 **{n} 篇论文**，其中 **{samples} 篇样例笔记**。'
              '可以直接在 GitHub 阅读下方分类清单、打开原论文和官方代码，或进入仓库内的笔记。\n',
              ' | '.join(f'[{label}](#{anchors[key]})' for key, label in populated),
              '\n✅ 已查到实际官方实现；🟡 部分公开；❔ 尚未确认官方代码。代码状态不代表已完成运行或复现。'
              '预印本单独标注；“索引”表示尚未完成样例级整理。\n']
    def cell(value):
        return str(value).replace('|', '&#124;').replace('\n', ' ')
    for key, label in populated:
        group = sorted((p for p in papers if p['primary_direction'] == key),
                       key=lambda p: (-p['year'], p['short_name'].lower()))
        chunks += [f'<a id="{anchors[key]}"></a>\n\n### {label} · {len(group)} 篇\n',
                   '| 论文 | 发表 | 研究内容 | 官方代码与开放情况 | 笔记 |',
                   '| --- | --- | --- | --- | --- |']
        for p in group:
            title = f'**{cell(p["short_name"])}**<br>[{cell(p["title"])}]({p["paper_url"]})'
            venue = f'[{cell(p["venue"])} {p["year"]}]({p["publication_url"]})' if p['publication_url'] else f'arXiv {p["year"]}<br>**预印本**'
            if p['code_status'] == 'public':
                code = f'✅ [Code]({p["code_url"]})<br>{cell(p["code_details"])}'
            elif p['code_status'] == 'partial':
                code = f'🟡 [部分代码]({p["code_url"]})<br>{cell(p["code_details"])}'
            else:
                code = f'❔ {cell(p["code_details"])}'
            note_label = '样例笔记' if p['content_status'] == 'detailed_sample' else '索引'
            note = f'[{note_label}](docs/papers/{p["_file"]})'
            chunks.append('| ' + ' | '.join([title, venue, cell(p['summary']), code, note]) + ' |')
        chunks.append('')
    chunks += ['## 两条阅读主线\n',
               '- [开放词汇能力如何实现](https://buzhidaozenmo.github.io/Open-Vocabulary-Segmentation-Atlas/?track=vocabulary)：文本编码、视觉语言对齐、区域预测、视频和语言场。',
               '- [点云语义如何构建与优化](https://buzhidaozenmo.github.io/Open-Vocabulary-Segmentation-Atlas/?track=pointcloud)：投影、多视角融合、教师可靠性、蒸馏与几何区域处理。',
               '\n点击路线节点或连线筛选方法，展开查看具体操作、原图和证据。模块在上方各篇论文笔记的元数据维护。\n',
               '## 数据集与方法比较\n',
               '- [数据集与评测设置](docs/benchmarks.md)',
               '- [五篇样例的方法比较](docs/insights.md)',
               '- [研究地图与技术矩阵](https://buzhidaozenmo.github.io/Open-Vocabulary-Segmentation-Atlas/atlas/)',
               '\n最近核查：**' + max(str(p['checked_on']) for p in papers) + '**。'
               + ('已完成首期100篇收录，后续继续更新方法与来源核查。\n' if n >= 100 else '目标约100篇，后续按研究方向持续扩展。\n'),
               README_END]
    return '\n'.join(chunks)


def synced_readme(papers):
    current = (ROOT / 'README.md').read_text(encoding='utf-8')
    if current.count(README_START) != 1 or current.count(README_END) != 1:
        raise ValueError('README requires exactly one catalogue marker pair')
    start, end = current.index(README_START), current.index(README_END) + len(README_END)
    return current[:start] + readme_catalogue(papers) + current[end:]


def read_papers():
    papers = []
    for path in sorted((ROOT / 'docs/papers').glob('*.md')):
        parts = path.read_text(encoding='utf-8').split('---', 2)
        if len(parts) != 3 or parts[0].strip():
            raise ValueError(f'{path.name}: missing YAML front matter')
        record = yaml.safe_load(parts[1])
        record['_body'] = parts[2].strip()
        record['_file'] = path.name
        papers.append(record)
    return papers


def validate(papers, taxonomy, relations):
    required = ['paper_id', 'title', 'short_name', 'year', 'venue',
                'publication_status', 'primary_direction', 'modalities',
                'task_setting', 'task_types', 'techniques', 'datasets',
                'paper_url', 'publication_url', 'code_status', 'code_url',
                'code_details', 'content_status', 'checked_on', 'sources']
    ids = [p['paper_id'] for p in papers]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate paper_id')
    for p in papers:
        label = p['paper_id']
        for key in required:
            if key not in p or p[key] is None:
                raise ValueError(f'{label}: missing {key}')
        if not re.fullmatch(r'[a-z][a-z0-9_-]*', label):
            raise ValueError(f'Invalid stable ID: {label}')
        if p['_file'] != label + '.md':
            raise ValueError(f'{label}: file name must equal paper_id')
        if p['primary_direction'] not in GROUPS:
            raise ValueError(f'{label}: unknown primary direction')
        if p['content_status'] not in LEVELS:
            raise ValueError(f'{label}: invalid content status')
        if p['publication_status'] not in ('published', 'preprint'):
            raise ValueError(f'{label}: invalid publication status')
        if p['publication_status'] == 'published' and not p['publication_url']:
            raise ValueError(f'{label}: published paper needs publication evidence')
        if p['code_status'] not in ('public', 'partial', 'unconfirmed', 'planned'):
            raise ValueError(f'{label}: invalid code status')
        if p['code_status'] in ('public', 'partial') and not p['code_url']:
            raise ValueError(f'{label}: implementation needs a URL')
        for key in ('paper_url', 'publication_url', 'code_url'):
            if p[key] and urlparse(p[key]).scheme != 'https':
                raise ValueError(f'{label}: {key} must be HTTPS')
        if any(t not in taxonomy['techniques'] for t in p['techniques']):
            raise ValueError(f'{label}: uncontrolled technique')
        if any(d not in taxonomy['datasets'] for d in p['datasets']):
            raise ValueError(f'{label}: uncontrolled dataset')
        if not p['sources'] or any(not s.get('url') or not s.get('locator') for s in p['sources']):
            raise ValueError(f'{label}: sources need URL and locator')
        if p['content_status'] == 'detailed_sample':
            for heading in ('## 任务', '## 方法', '## 实验', '## 局限', '## 证据'):
                if heading not in p['_body']:
                    raise ValueError(f'{label}: missing {heading}')
            if len(p['sources']) < 3:
                raise ValueError(f'{label}: detailed sample needs multiple evidence locators')
    validate_methods(papers, ROOT)
    for edge in relations:
        if edge['source'] not in ids or edge['target'] not in ids:
            raise ValueError('Broken relation reference')
        if edge['type'] not in ('explicit_basis', 'explicit_adaptation', 'comparison'):
            raise ValueError('Unsupported relation type')
        if not edge.get('evidence_url') or not edge.get('locator'):
            raise ValueError('Relation without evidence')
    print(f'Validated {len(papers)} papers; '
          f'{sum(p["content_status"] == "detailed_sample" for p in papers)} detailed samples; '
          f'{len(relations)} evidence-backed relations.')


def write(name, content):
    path = STAGE / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')


def link(p):
    return f'[{p["short_name"]}](papers/{p["_file"]})'


def generate(papers, taxonomy, relations):
    STAGE.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / 'docs', STAGE, dirs_exist_ok=True)
    ids = {p['paper_id']: p for p in papers}
    records = []
    code_names = {'public': '已公开实现', 'partial': '部分公开',
                  'unconfirmed': '尚未确认', 'planned': '计划公开'}
    for p in papers:
        meta = (
            f'<div class="paper-meta"><span>{html.escape(p["venue"])} · {p["year"]}</span>'
            f'<span>{LEVELS[p["content_status"]]}</span><span>{code_names[p["code_status"]]}</span></div>\n\n'
            f'**任务：** {" / ".join(p["task_types"])}　\n'
            f'**发表状态：** {"正式发表" if p["publication_status"] == "published" else "预印本；未确认正式录用"}　'
            f'**核查日期：** {p["checked_on"]}\n\n'
            f'[论文原文]({p["paper_url"]})'
            + (f' · [发表来源]({p["publication_url"]})' if p['publication_url'] else '')
            + (f' · [官方代码]({p["code_url"]})' if p['code_url'] else '')
            + '\n\n'
        )
        body = p['_body']
        head, _, rest = body.partition('\n')
        write('papers/' + p['_file'], head + '\n\n' + meta + note_modules(p) + rest)
        r = {k: v for k, v in p.items() if not k.startswith('_')}
        r['url'] = 'papers/' + p['paper_id'] + '/'
        r['direction_label'] = GROUPS[p['primary_direction']]
        r['technique_labels'] = [taxonomy['techniques'][t] for t in p['techniques']]
        r['content_label'] = LEVELS[p['content_status']]
        r['code_label'] = code_names[p['code_status']]
        records.append(r)
    write('assets/papers.json', json.dumps(records, ensure_ascii=False, indent=2))
    counts = Counter(p['primary_direction'] for p in papers)
    generate_methods(papers, GROUPS, write)
    filters = [('primary_direction', '方向'), ('year', '年份'), ('venue', '会议 / 期刊'),
               ('task_types', '任务'), ('techniques', '技术'), ('datasets', '数据集'),
               ('code_status', '开源状态'), ('publication_status', '发表状态'),
               ('content_status', '阅读深度')]
    fields = '\n'.join(f'<label>{label}<select data-filter="{key}"><option value="">全部</option></select></label>' for key, label in filters)
    table = '\n'.join(f'| {link(p)} | {p["year"]} · {p["venue"]} | {GROUPS[p["primary_direction"]]} | {LEVELS[p["content_status"]]} |' for p in papers)
    write('library.md', f'''
# 论文库

所有筛选条件取交集。关键词可搜索标题、方法摘要和技术标签；页面顶部搜索框可检索笔记全文。每篇论文仅按主要方向计数。

<div id="paper-browser" data-index="assets/papers.json">
<label class="search-label">搜索论文<input id="paper-query" type="search" placeholder="例如：几何、SAM3、蒸馏、SAS…" autocomplete="off"></label>
<div class="filter-grid">{fields}</div>
<div class="library-tools"><p id="paper-count" role="status" aria-live="polite">正在载入索引…</p><button id="reset-filters" type="button">重置筛选</button></div>
<div id="paper-results" class="paper-grid"></div>
</div>

<div id="paper-fallback" markdown>

## 完整索引

脚本未加载时可使用下表浏览全部论文。

| 论文 | 发表 | 主要方向 | 整理状态 |
| --- | --- | --- | --- |
{table}

</div>
''')
    year_lines = []
    for year in sorted({p['year'] for p in papers}, reverse=True):
        year_lines.append(f'## {year}\n\n' + '\n'.join(
            f'- **{GROUPS[p["primary_direction"]]}** · {link(p)} · {p["venue"]} · {p["summary"]}'
            for p in papers if p['year'] == year))
    direction_lines = '\n'.join(f'| {name} | {counts.get(key, 0)} |' for key, name in GROUPS.items())
    edges = '\n'.join(f'  {e["source"]}["{ids[e["source"]]["short_name"]}"] -->|{e["label"]}| {e["target"]}["{ids[e["target"]]["short_name"]}"]' for e in relations)
    evidence_lines = '\n'.join(f'- {link(ids[e["source"]])} → {link(ids[e["target"]])}：{e["label"]}。[证据：{e["locator"]}]({e["evidence_url"]})' for e in relations)
    write('atlas.md', f'''
# 研究方向与时间线

## 已覆盖与待扩展方向

| 主要方向 | 当前数量 |
| --- | ---: |
{direction_lines}

未覆盖方向将在后续批次补充，不用不相关论文填满数量。多视角和 3DGS 与 3D 有交叉，这里按主要问题归类，唯一论文只计一次。

## 有证据的方法关系

```mermaid
graph LR
{edges}
```

{evidence_lines}

时间先后、共同标签不代表继承关系。本图仅展示已核查的明确方法依据；后续关系需补充原文定位后加入。

## 按正式年份浏览

预印本使用当前预印本年份并明确标注，正式论文使用会议 / 期刊年份。

{chr(10).join(year_lines)}
''')
    used = [t for t in taxonomy['techniques'] if any(t in p['techniques'] for p in papers)]
    rows = '\n'.join('| ' + link(p) + ' | ' + ' | '.join('●' if t in p['techniques'] else '—' for t in used) + ' |' for p in papers)
    write('matrix.md', '# 论文 × 技术矩阵\n\n● 表示已在所读材料中识别该技术；— 表示本轮未标注，不能解释为论文必然没有使用。点击论文查看证据与阅读状态。\n\n'
          + '| 论文 | ' + ' | '.join(taxonomy['techniques'][t] for t in used) + ' |\n'
          + '| --- | ' + ' | '.join('---' for _ in used) + ' |\n' + rows)
    remaining = [p for p in papers if p['content_status'] == 'index']
    write('remaining.md', '# 其他论文笔记\n\n以下条目已完成研究关注点、操作证据、方法图与主要实验结果的定向整理，尚未完成样例级全文精读。\n\n'
          + '\n'.join(f'- {link(p)} · {p["venue"]} {p["year"]} · {p["summary"]}' for p in remaining))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='validate then strict build')
    parser.add_argument('--serve', action='store_true', help='validate, generate, serve on localhost')
    args = parser.parse_args()
    papers = read_papers()
    taxonomy = yaml.safe_load((ROOT / 'data/taxonomy.yaml').read_text())
    relations = yaml.safe_load((ROOT / 'data/paper_relations.yaml').read_text())
    validate(papers, taxonomy, relations)
    if (ROOT / 'README.md').read_text(encoding='utf-8') != synced_readme(papers):
        raise ValueError('README catalogue is stale; run python scripts/update_readme.py')
    generate(papers, taxonomy, relations)
    command = [sys.executable, '-m', 'mkdocs', 'serve', '-a', '127.0.0.1:8000'] if args.serve else [sys.executable, '-m', 'mkdocs', 'build', '--strict']
    subprocess.run(command, cwd=ROOT, check=True)
    if not args.serve:
        subprocess.run([sys.executable, str(ROOT / 'scripts/check_site.py')], cwd=ROOT, check=True)


if __name__ == '__main__':
    main()
