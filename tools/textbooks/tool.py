#!/usr/bin/env python3
"""Textbook breakdown helper.

  tool.py extract SLUG PDF        cache per-page text + outline into work/SLUG/
  tool.py outline SLUG [DEPTH]    print the PDF outline (title, pdf page)
  tool.py heads SLUG [A B]        print likely headings per page (for books w/o outline)
  tool.py pages SLUG A B [N]      print text of pages A..B (first N chars per page)
  tool.py digest SLUG             digest of each leaf in work/SLUG/structure.json
  tool.py render SLUG             write out/SLUG.md from work/SLUG/book.json
"""
import json, os, re, subprocess, sys, logging, warnings
logging.disable(logging.CRITICAL); warnings.filterwarnings('ignore')
W = '/home/claude/tb/work'; OUT = '/home/claude/tb/out'

def wd(slug):
    d = os.path.join(W, slug); os.makedirs(d, exist_ok=True); return d

def extract(slug, pdf):
    import pypdf
    d = wd(slug)
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    pages = txt.split('\f')[:n]
    json.dump(pages, open(os.path.join(d, 'pages.json'), 'w'))
    out = []
    try:
        r = pypdf.PdfReader(pdf)
        def walk(o, dep):
            for x in o:
                if isinstance(x, list): walk(x, dep + 1)
                else:
                    try: p = r.get_destination_page_number(x) + 1
                    except Exception: p = None
                    out.append([dep, x.title.strip(), p])
        walk(r.outline, 0)
    except Exception as e:
        print('outline error', e)
    json.dump(out, open(os.path.join(d, 'outline.json'), 'w'))
    empty = sum(1 for p in pages if len(p.strip()) < 40)
    print(f'{slug}: {n} pages, {len(out)} outline entries, {empty} near-empty pages')

def load(slug): return json.load(open(os.path.join(W, slug, 'pages.json')))

def outline(slug, depth=9):
    for d, t, p in json.load(open(os.path.join(W, slug, 'outline.json'))):
        if d <= depth: print('  ' * d + f'{t}  [{p}]')

HEAD = re.compile(r'^\s{0,12}((Chapter|CHAPTER|Part|PART|Lecture|Section|Appendix)\b.{0,70}|\d{1,2}(\.\d{1,2}){0,2}\.?\s+[A-Z][^.]{2,70}|[A-Z][A-Z ,:\-\'&]{6,60})\s*$')

def heads(slug, a=1, b=None):
    pages = load(slug); b = b or len(pages)
    for i in range(a - 1, b):
        lines = [l for l in pages[i].split('\n') if l.strip()]
        hs = [l.strip() for l in lines if HEAD.match(l) and len(l.strip()) > 3][:4]
        top = lines[0].strip()[:70] if lines else ''
        if hs: print(f'[{i+1}] top="{top}" | ' + ' || '.join(h[:70] for h in hs))

def pages_(slug, a, b, n=100000):
    pages = load(slug)
    for i in range(a - 1, min(b, len(pages))):
        t = re.sub(r'[ \t]+', ' ', pages[i]); t = re.sub(r'\n\s*\n+', '\n', t).strip()
        print(f'=== p{i+1} ===\n{t[:n]}')

def clean(t):
    t = re.sub(r'[ \t]+', ' ', t)
    t = re.sub(r'\n(?=[a-z,(])', ' ', t)
    return t

def digest(slug, maxc=420):
    pages = load(slug)
    st = json.load(open(os.path.join(W, slug, 'structure.json')))
    for c in st['chapters']:
        leaves = c.get('sections') or [c]
        print(f"# {c['title']} [{c['start']}-{c['end']}]")
        for s in leaves:
            t = clean('\n'.join(pages[s['start'] - 1:s['end']]))
            subs = re.findall(r'^\s*(\d+(?:\.\d+){1,3}\.?\s+[A-Z][^\n]{2,60})$', t, re.M)[:10]
            paras = [re.sub(r'\s+', ' ', p) for p in re.split(r'\n\s*\n', t) if len(p) > 200]
            body = ' '.join(paras)[:maxc] if paras else re.sub(r'\s+', ' ', t)[:maxc]
            print(f"## {s['title']} [{s['start']}-{s['end']}]\nSUBS: {'; '.join(x.strip() for x in subs)}\nTEXT: {body}\n")

def pr(a, b):
    return f'PDF pp. {a}–{b}' if b > a else f'PDF p. {a}'

def render(slug):
    bk = json.load(open(os.path.join(W, slug, 'book.json')))
    url = bk['url']
    L = [f'<a id="ch1"></a>\n# {bk["title"]}\n', f'> {bk["byline"]} · [the PDF in Drive]({url})\n']
    if bk.get('note'): L.append(bk['note'] + '\n')
    L.append(f'## The book in one paragraph\n\n{bk["summary"]}\n')
    chs = bk['chapters']
    if len(chs) > 1:
        L.append('**Contents**\n')
        for i, c in enumerate(chs, 1):
            L.append(f'{i}. [{c["title"]}](ch{i}): {c["summary"].split(". ")[0].rstrip(".")}.')
        L.append('')
    if bk.get('tail'):
        L.append('Also in this PDF:\n')
        for t, s in bk['tail']: L.append(f'- **{t}**: {s}')
        L.append('')
    for i, c in enumerate(chs, 1):
        L.append('\n---\n' if i == 1 else f'\n---\n\n<a id="ch{i}"></a>')
        L.append(f'## {c["title"]}\n\n*{pr(c["start"], c["end"])}*\n\n{c["summary"]}\n')
        for s in c.get('sections', []):
            L.append(f'**{s["title"]}**  \n{s["summary"]}  \n→ {pr(s["start"], s["end"])} in [the PDF]({url})\n')
        if not c.get('sections'):
            L.append(f'→ {pr(c["start"], c["end"])} in [the PDF]({url})\n')
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, slug + '.md'), 'w').write('\n'.join(L) + '\n')
    print('wrote', os.path.join(OUT, slug + '.md'), sum(len(x.split()) for x in L), 'words')

def build(slug, skip=()):
    """structure.json from outline: depth0 = chapters, depth1 = sections."""
    ol = [x for x in json.load(open(os.path.join(W, slug, 'outline.json'))) if x[2] and x[0] <= 1 and x[1] not in skip]
    n = len(load(slug))
    chs = []
    for i, (d, t, p) in enumerate(ol):
        nxt = next((q for dd, tt, q in ol[i + 1:] if dd <= d), n + 1)
        end = max(p, nxt - 1) if nxt > p else p
        if d == 0: chs.append({'title': t, 'start': p, 'end': end, 'sections': []})
        elif chs: chs[-1]['sections'].append({'title': t, 'start': p, 'end': end})
    json.dump({'chapters': chs}, open(os.path.join(W, slug, 'structure.json'), 'w'), indent=1)
    print(len(chs), 'chapters', sum(len(c['sections']) for c in chs), 'sections')

def assemble(slug, meta, ch_summ, sec_summ):
    """book.json = structure + summaries. ch_summ: list; sec_summ: list of lists."""
    st = json.load(open(os.path.join(W, slug, 'structure.json')))
    ids = json.load(open('/home/claude/tb/ids.json'))
    for c, cs, ss in zip(st['chapters'], ch_summ, sec_summ):
        c['summary'] = cs
        assert len(ss) == len(c['sections']), (c['title'], len(ss), len(c['sections']))
        for s, x in zip(c['sections'], ss): s['summary'] = x
    assert len(ch_summ) == len(st['chapters']), (len(ch_summ), len(st['chapters']))
    bk = dict(meta, chapters=st['chapters'], url=f"https://drive.google.com/file/d/{ids[slug]}/view")
    json.dump(bk, open(os.path.join(W, slug, 'book.json'), 'w'), indent=1)
    render(slug)

if __name__ == '__main__':
    a = sys.argv[1:]
    {'extract': lambda: extract(a[1], a[2]), 'outline': lambda: outline(a[1], int(a[2]) if len(a) > 2 else 9),
     'heads': lambda: heads(a[1], *(int(x) for x in a[2:4])), 'pages': lambda: pages_(a[1], int(a[2]), int(a[3]), *(int(x) for x in a[4:5])),
     'digest': lambda: digest(a[1]), 'render': lambda: render(a[1]), 'build': lambda: build(a[1], tuple(a[2:]))}[a[0]]()
