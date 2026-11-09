"""Update only the marked GitHub catalogue; preserve the rest of README."""
from build import ROOT, read_papers, synced_readme

if __name__ == '__main__':
    papers = read_papers()
    (ROOT / 'README.md').write_text(synced_readme(papers), encoding='utf-8')
    print(f'Updated GitHub README catalogue: {len(papers)} papers.')
