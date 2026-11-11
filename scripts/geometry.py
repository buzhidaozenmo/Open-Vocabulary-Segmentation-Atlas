"""Geometry topic generated from the same per-paper method metadata."""
import html

FAMILIES = {
    'pretrained': '三维预训练表征', 'coordinates': '坐标与空间邻域',
    'superpoints': '超点与区域结构', 'visibility': '投影深度与可见性',
    'affinity': '几何亲和与关系图', 'canonical': '规范空间与形状',
    'reconstruction': '多视图几何估计',
}
AXES = ['几何信号来源', '如何使用几何', '改变的表示／关系', '参与的任务环节']
E = lambda v: html.escape(str(v), quote=True)


def validate_geometry(m):
    g = m.get('geometry')
    if not g:
        return
    for k in ('families', 'signal', 'mechanism', 'changes', 'stage', 'semantic_role', 'route', 'evidence'):
        if not g.get(k):
            raise ValueError(f'Geometry module {m["id"]} requires {k}')
    if any(f not in FAMILIES for f in g['families']) or len(g['route']) != 4:
        raise ValueError('Invalid geometry taxonomy or route')
    if any(not x.get('url') or not x.get('locator') for x in g['evidence']):
        raise ValueError('Geometry operation needs source evidence')


def geometry_facts(m):
    g = m.get('geometry')
    if not g:
        return ''
    refs = '；'.join(f'<a href="{E(s["url"])}">{E(s["locator"])}</a>' for s in g['evidence'])
    return (f'<div class="geometry-facts"><p><strong>几何信号：</strong>{E(g["signal"])}</p>'
            f'<p><strong>几何具体怎么用：</strong>{E(g["mechanism"])}</p>'
            f'<p><strong>改变什么：</strong>{E(g["changes"])}　<strong>环节：</strong>{E(g["stage"])}</p>'
            f'<p><strong>与类别语义的关系：</strong>{E(g["semantic_role"])}</p>'
            f'<p class="geometry-evidence"><strong>几何依据：</strong>{refs}</p></div>')


def generate_geometry(papers, groups, write, detail):
    selected = [(p, m) for p in papers for m in p['methods'] if m.get('geometry')]
    rows = []
    for p, m in selected:
        g = m['geometry'];uid = p['paper_id'] + ':' + m['id']
        rows.append(f'''<tbody class="method-entry" data-method="{E(uid)}">
<tr><td data-label="论文／方法"><a href="../papers/{p['paper_id']}/#method-{m['id']}"><strong>{E(p['short_name'])}</strong></a><small>{E(p['venue'])} · {p['year']}</small><strong>{E(m['title'])}</strong></td>
<td data-label="几何信号">{E(g['signal'])}<small>{' · '.join(E(FAMILIES[f]) for f in g['families'])}</small></td>
<td data-label="具体操作"><p>{E(g['mechanism'])}</p><small>改变：{E(g['changes'])}</small></td>
<td data-label="参与位置与作用"><strong>{E(g['stage'])}</strong><p>{E(g['semantic_role'])}</p></td>
<td data-label="原图与证据"><button type="button" class="open-method" aria-expanded="false" aria-controls="detail-{p['paper_id']}-{m['id']}">图解与结果 <span aria-hidden="true">＋</span></button></td></tr>
<tr class="method-detail" id="detail-{p['paper_id']}-{m['id']}" hidden><td colspan="5">{detail(p,m,'../')}</td></tr></tbody>''')
    families = ''.join(f'<option value="{k}">{E(v)}</option>' for k,v in FAMILIES.items())
    mods = ''.join(f'<option value="{k}">{E(v)}</option>' for k,v in groups.items() if any(p['primary_direction']==k for p,m in selected))
    count = len({p['paper_id'] for p,m in selected})
    write('geometry.md', f'''---
hide:
  - toc
  - navigation
---
# 3D 几何如何被利用

比较几何在原论文中实际改变了什么：点特征、邻接关系、可靠性权重、区域划分，还是训练约束。这里同时收录几何表征基础工作与使用几何处理语义的应用工作。

Sonata、PTv3 等本身不提供文本类别接口；它们输出的三维表征如何被其他方法使用，需要查看对应应用论文。正式发表信息、原图、主要结果和来源均随条目保留。

<div id="method-browser" data-topic="geometry">
<div class="method-filters"><label>几何来源<select id="geometry-source"><option value="">全部来源</option>{families}</select></label>
<label>来源模态<select id="method-modality"><option value="">全部模态</option>{mods}</select></label>
<label class="method-search">关键词<input id="method-query" type="search" placeholder="Sonata、法向、超点、亲和、深度…" autocomplete="off"></label>
<button id="method-reset" type="button">重置</button></div>
<select id="method-problem" hidden><option value="">全部问题</option></select><input id="route-level" type="hidden" value="precise">
<section class="route-section"><div class="section-heading"><h2>几何作用路线</h2><span id="route-count" role="status" aria-live="polite"></span></div>
<p class="route-help">点击节点或连线，查看具体方法。连线表示处理路径；论文之间的沿用关系另见<a href="../atlas/">有原文依据的关系图</a>。</p>
<label class="route-mobile-control">查看相邻阶段<select id="route-segment"><option value="0">几何来源 → 使用方式</option><option value="1">使用方式 → 改变的表示</option><option value="2">改变的表示 → 参与环节</option></select></label>
<div id="route-graph" aria-label="三维几何作用路线图"></div><div id="route-selection" role="status" aria-live="polite"></div>
<p class="route-caption">每篇论文的可见模块共同贡献 1；带宽表示收录分布，不表示性能优劣。</p></section>
<div class="section-heading"><h2>几何操作比较</h2><span id="method-count" role="status" aria-live="polite"></span></div>
<p id="method-empty" hidden>没有匹配的几何操作，请调整筛选或关键词。</p>
<div class="method-table-wrap"><table class="method-table"><thead><tr><th>论文／方法</th><th>几何信号</th><th>具体操作</th><th>参与位置与作用</th><th>原图与证据</th></tr></thead>{''.join(rows)}</table></div></div>

<noscript>可直接阅读上表并进入论文笔记查看原图与证据。</noscript>

当前覆盖 {count} 篇论文、{len(selected)} 个几何相关模块。全部内容由论文元数据生成。<a href="../">返回全部方法</a> · <a href="../atlas/">查看有证据的论文关系</a>
''')
