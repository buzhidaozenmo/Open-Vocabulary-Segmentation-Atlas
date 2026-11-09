"""Build the problem-led method view from paper front matter (no second catalogue)."""
import html
import json
import re

TRACKS = {'vocabulary': '开放词汇能力如何实现', 'pointcloud': '点云语义如何构建与优化'}
PROBLEMS = {
    'alignment': '语言编码与视觉对齐', 'unseen': '未见类别与类别冲突',
    'projection': '像素—点对应与可见性', 'multiview': '多视角语义传递与融合',
    'reliability': '教师可靠性与语义冲突', 'distillation': '二维到三维特征蒸馏',
    'regions': '区域／超点聚合', 'geometry': '几何一致性与语义净化',
    'temporal': '跨帧语义与记忆', 'efficiency': '语言表示与查询效率',
}
ORIGINS = {'proposed': '本文提出', 'reused': '沿用已有方法',
           'modified': '在已有方法上修改', 'unverified': '来源未核实'}
AXES = ['语义来源', '相关操作', '输出表示', '预测／用途']
E = lambda v: html.escape(str(v), quote=True)


def validate_methods(papers, root):
    for p in papers:
        figures = {f['id']: f for f in p.get('figures', [])}
        if not p.get('methods'):
            raise ValueError(f'{p["paper_id"]}: missing research modules')
        seen = set()
        for f in figures.values():
            for key in ('asset', 'label', 'page', 'version', 'source_url', 'source_sha256', 'clip_pdf_points'):
                if not f.get(key):
                    raise ValueError(f'{p["paper_id"]}: figure needs {key}')
            if not re.fullmatch(r'[0-9a-f]{64}', f['source_sha256']):
                raise ValueError('Figure needs a real SHA256')
            if not (root / 'docs' / f['asset']).is_file():
                raise ValueError('Missing source figure ' + f['asset'])
        for m in p['methods']:
            for key in ('id', 'track', 'problems', 'title', 'question', 'operation', 'input', 'output',
                        'stage', 'supervision', 'origin', 'origin_note', 'evidence', 'figure', 'figure_guide', 'route'):
                if not m.get(key):
                    raise ValueError(f'{p["paper_id"]}/{m.get("id")}: missing {key}')
            if m['id'] in seen or m['track'] not in TRACKS or m['origin'] not in ORIGINS:
                raise ValueError('Invalid method identity or controlled label')
            seen.add(m['id'])
            if not re.fullmatch(r'[a-z][a-z0-9_-]*', m['id']):
                raise ValueError('Invalid module anchor')
            if any(x not in PROBLEMS for x in m['problems']) or len(m['route']) != 4:
                raise ValueError('Invalid problem or four-stage route')
            if m['figure'] not in figures or any(not s.get('url') or not s.get('locator') for s in m['evidence']):
                raise ValueError('Module without matching figure or evidence')
            if m['origin'] == 'reused' and not m.get('origin_refs'):
                raise ValueError('Reused module requires original reference')


def detail(p, m, prefix):
    f = next(f for f in p['figures'] if f['id'] == m['figure'])
    refs = ''.join(f'<li><a href="{E(s["url"])}">{E(s["locator"])}</a></li>' for s in m['evidence'])
    previous = ''.join(f'<li><a href="{E(s["url"])}">{E(s["locator"])}</a></li>' for s in m.get('origin_refs', []))
    img = prefix + f['asset']
    return f'''<div class="method-expanded">
<div class="method-explanation"><p class="fact-label">原文方法整理 · {E(p['module_checked_on'])}</p>
<h3>{E(m['title'])}</h3><p><strong>关注的问题</strong><br>{E(m['question'])}</p>
<p><strong>具体操作</strong><br>{E(m['operation'])}</p>
<dl><dt>输入</dt><dd>{E(m['input'])}</dd><dt>输出</dt><dd>{E(m['output'])}</dd>
<dt>使用环节</dt><dd>{E(m['stage'])}</dd><dt>必要监督</dt><dd>{E(m['supervision'])}</dd>
<dt>方法来源</dt><dd><span class="origin">{E(ORIGINS[m['origin']])}</span> {E(m['origin_note'])}</dd></dl>
<strong>原文证据</strong><ul>{refs}</ul>{'<strong>沿用／修改的来源</strong><ul>'+previous+'</ul>' if previous else ''}
</div><figure class="method-figure"><a class="figure-zoom" href="{E(img)}" aria-label="放大 {E(p['short_name'])} {E(f['label'])}">
<img src="{E(img)}" alt="{E(p['short_name'])} {E(f['label'])}：{E(m['title'])}" loading="lazy"></a>
<figcaption>{E(f['label'])} · PDF 第 {f['page']} 页 · {E(f['version'])}<br>
<a href="{E(f['source_url'])}#page={f['page']}">原图来源</a> · 点击原图放大</figcaption>
<p><strong>{'图中阅读路径' if m.get('depicted', True) else '图示范围与未绘出操作'}</strong><br>{E(m['figure_guide'])}</p>
</figure></div>'''


def note_modules(p):
    blocks = ['## 与研究关注点相关的方法\n\n', '<div class="note-methods">']
    for m in p['methods']:
        blocks.append(f'<details id="method-{E(m["id"])}"><summary>{E(m["title"])} · {E(TRACKS[m["track"]])}</summary>'
                      + detail(p, m, '../../') + '</details>')
    blocks.append('</div>\n\n')
    return '\n'.join(blocks)


def generate_methods(papers, groups, write):
    rows, records = [], []
    for p in papers:
        for m in p['methods']:
            uid = p['paper_id'] + ':' + m['id']
            records.append({**m, 'uid': uid, 'paper_id': p['paper_id'], 'paper': p['short_name'],
                            'modality': p['primary_direction'], 'modality_label': groups[p['primary_direction']]})
            rows.append(f'''<tbody class="method-entry" data-method="{E(uid)}">
<tr><td data-label="论文／模态"><a href="papers/{p['paper_id']}/#method-{E(m['id'])}"><strong>{E(p['short_name'])}</strong></a><small>{E(groups[p['primary_direction']])} · {p['year']}</small></td>
<td data-label="关注的问题">{E(m['question'])}<small>{' · '.join(E(PROBLEMS[x]) for x in m['problems'])}</small></td>
<td data-label="相关模块及具体操作"><strong>{E(m['title'])}</strong><p>{E(m['operation'])}</p><span class="origin">{E(ORIGINS[m['origin']])}</span></td>
<td data-label="输入输出与使用环节"><span>{E(m['input'])}</span><span class="io-arrow">↓</span><span>{E(m['output'])}</span><small>{E(m['stage'])}</small></td>
<td data-label="图解"><button type="button" class="open-method" aria-expanded="false" aria-controls="detail-{p['paper_id']}-{m['id']}">方法与原图 <span aria-hidden="true">＋</span></button></td></tr>
<tr class="method-detail" id="detail-{p['paper_id']}-{m['id']}" hidden><td colspan="5">{detail(p,m,'')}</td></tr></tbody>''')
    write('assets/methods.json', json.dumps(dict(tracks=TRACKS, problems=PROBLEMS, origins=ORIGINS, axes=AXES, methods=records), ensure_ascii=False, indent=2))
    problems = ''.join(f'<option value="{k}">{E(v)}</option>' for k,v in PROBLEMS.items())
    mods = ''.join(f'<option value="{k}">{E(v)}</option>' for k,v in groups.items() if any(p['primary_direction']==k for p in papers))
    tracks = ''.join(f'<button type="button" data-track="{k}" aria-pressed="false"><strong>{E(v)}</strong><span>{"文本如何进入像素、区域、视频与语言场" if k=="vocabulary" else "多视角传递、可靠性、蒸馏与几何区域处理"}</span></button>' for k,v in TRACKS.items())
    write('index.md', f'''---
hide:
  - toc
  - navigation
---
# 开放词汇分割 · 方法路线

从研究问题出发，比较论文中实际使用的操作。模块包含新设计与沿用方法；每项说明均可展开查看原图、输入输出和原文证据。

<div id="method-browser">
<div class="track-tabs" aria-label="阅读主线">{tracks}</div>
<div class="method-filters"><label>研究问题<select id="method-problem"><option value="">全部问题</option>{problems}</select></label>
<label>来源模态<select id="method-modality"><option value="">全部模态</option>{mods}</select></label>
<label class="method-search">关键词<input id="method-query" type="search" placeholder="例如：多视角、CLIP、超点、沿用、SAM3" autocomplete="off"></label>
<button id="method-reset" type="button">重置</button></div>
<section class="route-section" aria-labelledby="route-title"><div class="section-heading"><h2 id="route-title">研究路线</h2><span id="route-count" role="status" aria-live="polite"></span></div>
<p class="route-help">点击节点或连线，查看对应方法；再次点击取消。路线表示模块的处理路径，不表示论文之间的继承关系。</p>
<label class="route-mobile-control">查看相邻阶段<select id="route-segment"><option value="0">语义来源 → 相关操作</option><option value="1">相关操作 → 输出表示</option><option value="2">输出表示 → 预测／用途</option></select></label>
<div id="route-graph" aria-label="交互方法路线图"></div>
<div id="route-selection" role="status" aria-live="polite"></div>
<p class="route-caption">连线按论文等量加权：同篇论文在当前主线中的多个模块共同贡献 1；带宽仅表示当前记录的分布。颜色区分语义来源。<a href="assets/methods.json">下载路线与模块数据</a></p></section>
<div class="section-heading"><h2 id="comparison">相关方法比较</h2><span id="method-count" role="status" aria-live="polite"></span></div>
<p id="method-empty" hidden>没有匹配的方法，请调整研究问题、模态或关键词。</p>
<div class="method-table-wrap"><table class="method-table"><thead><tr><th>论文／模态</th><th>关注的问题</th><th>相关模块及具体操作</th><th>输入输出与使用环节</th><th>图解</th></tr></thead>{''.join(rows)}</table></div>
</div>
<noscript>交互路线图需要 JavaScript。可直接阅读上表，或进入各篇论文查看完整模块与配图。</noscript>

<p class="scope-note">当前：{len(papers)} 篇论文的 {len(records)} 项定向模块整理，保留 {sum(p['content_status']=='detailed_sample' for p in papers)} 篇样例笔记；未独立复现实验。NeRF／3DGS 按模块内容归类。<a href="library/">按年份、会议与模态浏览论文库</a> · <a href="about/">整理与图示规范</a></p>
''')
