# Run on the Mac from repo root: makes cover thumbnails (own photos or Open Library stock covers)
import json, os, re, subprocess, time, urllib.request, urllib.parse, difflib
jobs = json.load(open('_tmp/jobs.json'))
PROC = os.path.expanduser('~/Downloads/books-pics/processed')
OUT = 'src/main/md/Books/covers'
res = {}
def n(s): return re.sub(r'[^a-z0-9]', '', s.lower())
def thumb(src, dst):
    subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '70', '-Z', '360', src, '--out', dst],
                   check=True, capture_output=True)
for i, q, a, own in jobs:
    try:
        if own:
            src = [f for f in os.listdir(PROC) if f.startswith(own + ' ') or f.startswith(own + '.')][0]
            thumb(os.path.join(PROC, src), f'{OUT}/{own}.jpg'); res[i] = [own, 'own']; continue
        main = re.split(r'[:(]', q)[0].strip()
        params = {'title': main, 'limit': 8, 'fields': 'title,author_name,cover_i'}
        if a: params['author'] = a.split()[-1]
        url = 'https://openlibrary.org/search.json?' + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={'User-Agent': 'ettuge-books-catalog/1.0'})
        docs = json.load(urllib.request.urlopen(req, timeout=20)).get('docs', [])
        pick = None
        for d in docs:
            if not d.get('cover_i'): continue
            r = difflib.SequenceMatcher(None, n(main), n(re.split(r'[:(]', d['title'])[0])).ratio()
            if r < (0.85 if a else 0.95): continue
            if a and not any(n(a.split()[-1]) in n(x) for x in d.get('author_name', [])): continue
            pick = d; break
        if not pick: res[i] = [None, 'nomatch']; time.sleep(0.6); continue
        cid = pick['cover_i']; tmp = f'/tmp/ol_{cid}.jpg'
        req = urllib.request.Request(f'https://covers.openlibrary.org/b/id/{cid}-L.jpg?default=false', headers={'User-Agent': 'ettuge-books-catalog/1.0'})
        open(tmp, 'wb').write(urllib.request.urlopen(req, timeout=30).read())
        if os.path.getsize(tmp) < 2000: res[i] = [None, 'tiny']; continue
        thumb(tmp, f'{OUT}/OL_{cid}.jpg'); res[i] = [f'OL_{cid}', pick['title'] + ' / ' + ', '.join(pick.get('author_name', [])[:2])]
        time.sleep(0.6)
    except Exception as e:
        res[i] = [None, 'err ' + str(e)[:80]]
    print(i, res[i], flush=True)
json.dump(res, open('_tmp/covers_result.json', 'w'), ensure_ascii=False, indent=0)
print('DONE', sum(1 for v in res.values() if v[0]), 'of', len(jobs))
