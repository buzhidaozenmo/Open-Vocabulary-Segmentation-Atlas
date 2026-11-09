"""Check local HTML links and packaged research index after a strict build."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

ROOT = Path(__file__).resolve().parents[1] / '.codex_tmp/site'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get('id'):
            self.ids.add(data['id'])
        key = 'href' if tag == 'a' else 'src'
        if tag in ('a', 'script', 'img', 'link') and data.get(key):
            self.links.append(data[key])


errors = []
documents = {}
for path in ROOT.rglob('*.html'):
    parser = Links()
    parser.feed(path.read_text())
    documents[path.resolve()] = parser
for path in ROOT.rglob('*.html'):
    parser = documents[path.resolve()]
    for href in parser.links:
        url = urlsplit(href)
        if url.scheme or url.netloc or url.path.startswith('/'):
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{path.relative_to(ROOT)} -> {href}')
        elif url.fragment and target in documents and unquote(url.fragment) not in documents[target].ids:
            errors.append(f'{path.relative_to(ROOT)} -> missing anchor {href}')
records = json.loads((ROOT / 'assets/papers.json').read_text())
for record in records:
    if not (ROOT / record['url'] / 'index.html').exists():
        errors.append('Missing paper: ' + record['paper_id'])
methods = json.loads((ROOT / 'assets/methods.json').read_text())['methods']
ids = set()
for method in methods:
    if method['uid'] in ids:
        errors.append('Duplicate module: ' + method['uid'])
    ids.add(method['uid'])
    note = (ROOT / 'papers' / method['paper_id'] / 'index.html').resolve()
    if 'method-' + method['id'] not in documents[note].ids:
        errors.append('Missing module anchor: ' + method['uid'])
    if 'detail-' + method['paper_id'] + '-' + method['id'] not in documents[(ROOT / 'index.html').resolve()].ids:
        errors.append('Missing inline module: ' + method['uid'])
if errors:
    raise SystemExit('\n'.join(errors))
print(f'HTML links, {len(records)} papers and {len(methods)} module destinations verified.')
