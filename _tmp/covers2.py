import json, os, re, subprocess, time, urllib.request, urllib.parse, difflib
jobs = json.load(open('_tmp/jobs.json')); R = json.load(open('_tmp/redo.json'))
bad = set(int(x) for x in R['bad']); OUT = 'src/main/md/Books/covers'
prev = json.load(open('/tmp/prev2.json')) if os.path.exists('/tmp/prev2.json') else {}
res = {int(k): v for k, v in prev.items() if v[0]}
UA = {'User-Agent': 'ettuge-books-catalog/1.0 (https://github.com/vwulf/ettuge; personal reading list)'}
def n(s): return re.sub(r'[^a-z0-9]', '', s.lower())
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()
def thumb(src, dst): subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','70','-Z','360',src,'--out',dst],check=True,capture_output=True)
def ok_title(main, t): return difflib.SequenceMatcher(None, n(main), n(re.split(r'[:(]', t)[0])).ratio() >= 0.8
for i in R['redo']:
    if i in res: continue
    _, q, a, own = jobs[i]; main = re.split(r'[:(]', q)[0].strip(); sur = a.split()[-1] if a else ''
    try:
        found = None
        if sur:
            d = json.loads(get('https://openlibrary.org/search.json?' + urllib.parse.urlencode({'q': f'{main} {a}', 'limit': 25, 'fields': 'title,author_name,cover_i'})))
            for doc in d.get('docs', []):
                if doc.get('cover_i') and doc['cover_i'] not in bad and ok_title(main, doc['title']) and any(n(sur) in n(x) for x in doc.get('author_name', [])):
                    data = get(f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-L.jpg?default=false")
                    if len(data) > 5000: found = (f"OL_{doc['cover_i']}", data, 'OL ' + doc['title']); break
        if not found:
            w = json.loads(get('https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode({'action':'query','list':'search','srsearch':f'{main} {sur}'.strip(),'srlimit':4,'format':'json'})))
            for hit in w['query']['search']:
                pt = re.sub(r'\s*\(.*?\)$', '', hit['title'])
                if difflib.SequenceMatcher(None, n(main), n(pt)).ratio() < 0.85: continue
                p = json.loads(get('https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode({'action':'query','titles':hit['title'],'prop':'pageimages','piprop':'thumbnail','pithumbsize':400,'format':'json'})))
                pg = list(p['query']['pages'].values())[0]; th = pg.get('thumbnail', {}).get('source')
                if not th or th.lower().endswith('.svg.png'): continue
                data = get(th)
                if len(data) > 5000: found = ('WP_' + re.sub(r'[^A-Za-z0-9]+', '_', hit['title'])[:50], data, 'WP ' + hit['title']); break
        if found:
            fn, data, lab = found; tmp = f'/tmp/{fn}.jpg'; open(tmp, 'wb').write(data); thumb(tmp, f'{OUT}/{fn}.jpg'); res[i] = [fn, lab]
        else: res[i] = [None, 'nomatch2']
    except Exception as e: res[i] = [None, 'err ' + str(e)[:60]]
    print(i, res[i], flush=True); time.sleep(2.5)
json.dump(res, open('_tmp/covers_result2.json', 'w'), ensure_ascii=False)
print('DONE', sum(1 for v in res.values() if v[0]), len(res))
