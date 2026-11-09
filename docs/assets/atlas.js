/* Progressive enhancement: static Markdown index stays available on failure. */
(() => {
  const browser = document.getElementById('paper-browser');
  if (!browser) return;
  const script = [...document.scripts].find(s => /\/assets\/atlas\.js(?:\?|$)/.test(s.src));
  const indexUrl = new URL('papers.json', script.src);
  const baseUrl = new URL('../', indexUrl);
  const names = {
    public: '已公开实现', partial: '部分公开', planned: '计划公开', unconfirmed: '尚未确认',
    published: '正式发表', preprint: '预印本', detailed_sample: '样例笔记', index: '已建索引',
  };
  const query = document.getElementById('paper-query');
  const selects = [...browser.querySelectorAll('select[data-filter]')];
  const results = document.getElementById('paper-results');
  const count = document.getElementById('paper-count');
  const element = (tag, text, className) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  fetch(indexUrl).then(r => {
    if (!r.ok) throw new Error('index unavailable');
    return r.json();
  }).then(papers => {
    const labels = new Map(Object.entries(names));
    papers.forEach(p => {
      labels.set(p.primary_direction, p.direction_label);
      p.techniques.forEach((t, i) => labels.set(t, p.technique_labels[i]));
    });
    const params = new URLSearchParams(location.search);
    selects.forEach(select => {
      const key = select.dataset.filter;
      const options = [...new Set(papers.flatMap(p => [].concat(p[key])))];
      options.sort((a, b) => key === 'year' ? b - a : String(labels.get(a) || a).localeCompare(String(labels.get(b) || b), 'zh-CN'));
      options.forEach(value => {
        const opt = element('option', labels.get(value) || String(value));
        opt.value = value;
        select.append(opt);
      });
      if (options.some(v => String(v) === params.get(key))) select.value = params.get(key);
    });
    query.value = params.get('paper_query') || '';
    function render() {
      const term = query.value.trim().toLocaleLowerCase();
      const matched = papers.filter(p => {
        const searchable = [p.title, p.short_name, p.summary, p.direction_label,
          ...p.techniques, ...p.technique_labels, ...p.datasets, ...p.task_types].join(' ').toLocaleLowerCase();
        return (!term || searchable.includes(term)) && selects.every(s => !s.value || [].concat(p[s.dataset.filter]).map(String).includes(s.value));
      });
      results.replaceChildren();
      count.textContent = `${matched.length} / ${papers.length} 篇论文`;
      matched.forEach(p => {
        const card = element('article', undefined, 'paper-card');
        const heading = element('h3');
        const anchor = element('a', p.short_name);
        anchor.href = new URL(p.url, baseUrl);
        heading.append(anchor);
        const chips = element('div', undefined, 'paper-chips');
        [p.direction_label, `${p.venue} ${p.year}`, p.content_label].forEach(t => chips.append(element('span', t, 'paper-chip')));
        if (p.publication_status === 'preprint') chips.append(element('span', '预印本', 'paper-chip preprint'));
        card.append(heading, element('div', p.title, 'paper-title'), chips, element('p', p.summary),
          element('footer', `${p.code_label} · ${p.task_types.join(' / ')} · 核查 ${p.checked_on}`));
        results.append(card);
      });
      if (!matched.length) results.append(element('p', '暂无匹配论文。试着减少筛选条件或重置筛选。', 'paper-empty'));
      const state = new URLSearchParams();
      if (query.value.trim()) state.set('paper_query', query.value.trim());
      selects.forEach(s => { if (s.value) state.set(s.dataset.filter, s.value); });
      history.replaceState(null, '', location.pathname + (state.size ? '?' + state : '') + location.hash);
    }
    query.addEventListener('input', render);
    selects.forEach(s => s.addEventListener('change', render));
    document.getElementById('reset-filters').addEventListener('click', () => {
      query.value = ''; selects.forEach(s => { s.value = ''; }); render(); query.focus();
    });
    document.getElementById('paper-fallback').hidden = true;
    render();
  }).catch(() => {
    count.textContent = '交互筛选未加载，请使用下方完整索引。';
  });
})();
