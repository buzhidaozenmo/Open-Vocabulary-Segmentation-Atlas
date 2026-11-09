/* Problem-led route view. Every paper contributes one unit across its visible modules. */
(() => {
  'use strict';
  const source = document.currentScript.src;
  const root = document.getElementById('method-browser');
  // Source figures remain ordinary links when scripts are unavailable.
  const dialog = document.createElement('dialog');
  dialog.className = 'figure-dialog';
  dialog.innerHTML = '<button type="button" aria-label="关闭原图">关闭 ×</button><img alt=""><p></p>';
  document.body.append(dialog);
  function revealHash() {
    let target;try{target=document.getElementById(decodeURIComponent(location.hash.slice(1)));}catch{}
    if(target?.tagName==='DETAILS')target.open=true;
  }
  revealHash();window.addEventListener('hashchange',revealHash);
  dialog.querySelector('button').onclick = () => dialog.close();
  dialog.addEventListener('click', e => { if (e.target === dialog) dialog.close(); });
  document.querySelectorAll('.figure-zoom').forEach(a => a.addEventListener('click', e => {
    e.preventDefault(); dialog.querySelector('img').src = a.href;
    dialog.querySelector('img').alt = a.querySelector('img').alt;
    dialog.querySelector('p').textContent = a.closest('figure').querySelector('figcaption').textContent;
    dialog.showModal();
  }));
  if (!root) return;
  const graph = document.getElementById('route-graph');
  const problem = document.getElementById('method-problem');
  const modality = document.getElementById('method-modality');
  const query = document.getElementById('method-query');
  const segment = document.getElementById('route-segment');
  const params = new URL(location.href).searchParams;
  let track = params.get('track') === 'pointcloud' ? 'pointcloud' : 'vocabulary';
  let selected = null, data, base = [], weights = new Map();
  const entries = new Map([...document.querySelectorAll('.method-entry')].map(el => [el.dataset.method, el]));
  for (const [el,key] of [[problem,'problem'],[modality,'modality']]) {
    if ([...el.options].some(o=>o.value===params.get(key))) el.value=params.get(key);
  }
  query.value = params.get('method_query') || '';
  function urlState() {
    const url = new URL(location.href);
    for(const [key,val] of Object.entries({track,problem:problem.value,modality:modality.value,method_query:query.value,route:selected?.key || ''})) {
      if(val) url.searchParams.set(key,val); else url.searchParams.delete(key);
    }
    history.replaceState(null,'',url);
  }
  const uniquePapers = records => new Set(records.map(m=>m.paper_id)).size;
  const matchSelection = (m,s) => !s || s.indices.every((col,i)=>m.route[col]===s.values[i]);
  function selectRoute(s) {
    selected = selected?.key === s?.key ? null : s;
    showRows(); urlState();
  }
  function showRows() {
    const filtered = base.filter(m=>matchSelection(m,selected));
    const visible = new Set(filtered.map(m=>m.uid));
    for(const [id,el] of entries) el.hidden=!visible.has(id);
    document.getElementById('method-count').textContent = `${uniquePapers(filtered)} 篇论文 · ${filtered.length} 个模块`;
    document.getElementById('method-empty').hidden=!!filtered.length;
    const state=document.getElementById('route-selection');
    state.replaceChildren();
    if(selected){
      const text=document.createElement('span');text.textContent=`已选择：${selected.values.join(' → ')}　`;
      const clear=document.createElement('button');clear.type='button';clear.textContent='取消路线选择';clear.onclick=()=>selectRoute(selected);
      state.append(text,clear);
    }
    graph.querySelectorAll('[data-route-key]').forEach(el=>{
      const spec=JSON.parse(el.dataset.routeSpec);
      const intersects=filtered.some(m=>matchSelection(m,spec));
      el.classList.toggle('route-dim',!!selected&&!intersects);
      el.setAttribute('aria-pressed',String(el.dataset.routeKey===selected?.key));
    });
  }
  function svgElement(name,attrs={}) {
    const el=document.createElementNS('http://www.w3.org/2000/svg',name);
    for(const [k,v] of Object.entries(attrs))el.setAttribute(k,String(v));
    return el;
  }
  function interactive(el,spec,title) {
    el.dataset.routeKey=spec.key;el.dataset.routeSpec=JSON.stringify(spec);
    el.setAttribute('role','button');el.setAttribute('tabindex','0');el.setAttribute('aria-label',title);
    const tip=svgElement('title');tip.textContent=title;el.append(tip);
    el.addEventListener('click',()=>selectRoute(spec));
    el.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();selectRoute(spec);}});
  }
  function draw() {
    graph.replaceChildren();
    if(!base.length)return;
    const mobile=matchMedia('(max-width:760px)').matches;
    const cols=mobile?[Number(segment.value),Number(segment.value)+1]:[0,1,2,3];
    const nodesByCol=cols.map(col=>{
      const groups=new Map();
      base.forEach(m=>{const v=m.route[col];if(!groups.has(v))groups.set(v,[]);groups.get(v).push(m);});
      return [...groups].map(([label,records])=>({label,records,col,weight:records.reduce((a,m)=>a+weights.get(m.uid),0)}));
    });
    const maxNodes=Math.max(...nodesByCol.map(a=>a.length));
    const height=Math.max(420,maxNodes*65+60), width=mobile?460:1200, nodeWidth=mobile?160:195;
    const total=uniquePapers(base), gap=12;
    const scale=(height-60-maxNodes*(34+gap))/total;
    const xStep=(width-nodeWidth)/(cols.length-1);
    const svg=svgElement('svg',{viewBox:`0 0 ${width} ${height}`,class:'route-svg','aria-label':'语义来源、相关操作、输出表示、预测用途的路线图'});
    const ribbons=svgElement('g'), boxes=svgElement('g');svg.append(ribbons,boxes);
    nodesByCol.forEach((nodes,i)=>{
      const used=nodes.reduce((sum,n)=>sum+34+n.weight*scale+gap,0)-gap;
      let y=48+(height-58-used)/2;
      const heading=svgElement('text',{x:i*xStep+nodeWidth/2,y:22,'text-anchor':'middle',class:'route-axis'});heading.textContent=data.axes[cols[i]];svg.append(heading);
      nodes.forEach(n=>{Object.assign(n,{x:i*xStep,y,h:34+n.weight*scale,offsetOut:17,offsetIn:17});y+=n.h+gap;});
    });
    const colors=['#358f89','#638fb0','#6b9d80','#9d9a60','#a98096','#8c88aa','#739caa','#b18b65'];
    const sources=[...new Set(base.map(m=>m.route[0]))];
    for(let i=0;i<cols.length-1;i++){
      const groups=new Map();
      base.forEach(m=>{const k=JSON.stringify([m.route[cols[i]],m.route[cols[i+1]],m.route[0]]);if(!groups.has(k))groups.set(k,[]);groups.get(k).push(m);});
      for(const [k,records] of groups){
        const [left,right]=JSON.parse(k),a=nodesByCol[i].find(n=>n.label===left),b=nodesByCol[i+1].find(n=>n.label===right);
        const value=records.reduce((sum,m)=>sum+weights.get(m.uid),0),h=value*scale;
        const x1=a.x+nodeWidth,x2=b.x,ym1=a.y+a.offsetOut,ym2=b.y+b.offsetIn,mid=(x1+x2)/2;
        a.offsetOut+=h;b.offsetIn+=h;
        const path=svgElement('path',{d:`M${x1},${ym1} C${mid},${ym1} ${mid},${ym2} ${x2},${ym2} L${x2},${ym2+h} C${mid},${ym2+h} ${mid},${ym1+h} ${x1},${ym1+h} Z`,fill:colors[sources.indexOf(records[0].route[0])%colors.length],class:'route-ribbon','data-weight':value,'data-transition':cols[i]});
        const pairs=new Map([[0,records[0].route[0]],[cols[i],left],[cols[i+1],right]]);
        const spec={indices:[...pairs.keys()],values:[...pairs.values()],key:JSON.stringify([...pairs].flat())};
        interactive(path,spec,`${left} → ${right}：${uniquePapers(records)} 篇论文，权重 ${value.toFixed(2)}。${[...new Set(records.map(m=>m.paper))].join('、')}`);ribbons.append(path);
      }
    }
    nodesByCol.forEach(nodes=>nodes.forEach(n=>{
      const g=svgElement('g',{class:'route-node'}),spec={indices:[n.col],values:[n.label],key:JSON.stringify([n.col,n.label])};
      const rect=svgElement('rect',{x:n.x,y:n.y,width:nodeWidth,height:n.h,rx:3});g.append(rect);
      const text=svgElement('text',{x:n.x+nodeWidth/2,y:n.y+n.h/2-3,'text-anchor':'middle'});
      const chunks=n.label.match(/.{1,12}/gu)||[];
      chunks.forEach((chunk,i)=>{const t=svgElement('tspan',{x:n.x+nodeWidth/2,dy:i?17:-(chunks.length-1)*8});t.textContent=chunk;text.append(t);});
      const count=svgElement('tspan',{x:n.x+nodeWidth/2,dy:18,class:'route-node-count'});count.textContent=`${uniquePapers(n.records)} 篇`;text.append(count);g.append(text);
      interactive(g,spec,`${n.label}：${uniquePapers(n.records)} 篇论文，权重 ${n.weight.toFixed(2)}。${[...new Set(n.records.map(m=>m.paper))].join('、')}`);boxes.append(g);
    }));
    graph.append(svg);
  }
  function refresh(preserve=false) {
    if(!preserve)selected=null;
    const terms=query.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    base=data.methods.filter(m=>m.track===track&&(!problem.value||m.problems.includes(problem.value))&&(!modality.value||m.modality===modality.value)&&terms.every(t=>(JSON.stringify(m)+data.origins[m.origin]).toLocaleLowerCase().includes(t)));
    const counts=new Map();base.forEach(m=>counts.set(m.paper_id,(counts.get(m.paper_id)||0)+1));
    weights=new Map(base.map(m=>[m.uid,1/counts.get(m.paper_id)]));
    document.querySelectorAll('[data-track]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.track===track)));
    document.getElementById('route-count').textContent=`${uniquePapers(base)} 篇论文`;
    draw();showRows();urlState();
  }
  fetch(new URL('methods.json',source)).then(r=>{if(!r.ok)throw Error('index');return r.json();}).then(index=>{
    data=index;
    if(params.has('route')) {
      try {const a=JSON.parse(params.get('route'));if(Array.isArray(a)&&a.length%2===0&&a.length<=8&&a.every((v,i)=>i%2?typeof v==='string':Number.isInteger(v)&&v>=0&&v<4))selected={indices:a.filter((v,i)=>i%2===0),values:a.filter((v,i)=>i%2===1),key:JSON.stringify(a)};}catch{}
    }
    document.querySelectorAll('[data-track]').forEach(b=>b.onclick=()=>{track=b.dataset.track;refresh();});
    problem.onchange=modality.onchange=()=>refresh();query.oninput=()=>refresh();segment.onchange=()=>{draw();showRows();};
    document.getElementById('method-reset').onclick=()=>{problem.value=modality.value=query.value='';refresh();};
    document.querySelectorAll('.open-method').forEach(b=>b.onclick=()=>{const row=document.getElementById(b.getAttribute('aria-controls')),open=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',String(open));b.querySelector('span').textContent=open?'−':'＋';row.hidden=!open;});
    matchMedia('(max-width:760px)').addEventListener('change',()=>{draw();showRows();});
    refresh(true);
  }).catch(()=>{document.getElementById('route-count').textContent='路线数据暂未载入；下方论文链接仍可阅读';});
})();
