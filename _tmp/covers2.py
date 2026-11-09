import json, os, re, subprocess, time, urllib.request, urllib.parse, difflib
jobs = json.load(open('_tmp/jobs.json')); R = json.load(open('_tmp/redo.json'))
bad = set(int(x) for x in R['bad']); OUT = 'src/main/md/Books/covers'; res = {}
UA = {'User-Agent': 'ettuge-books-catalog/1.0'}
def n(s): return re.sub(r'[^a-z0-9]', '', s.lower())
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()
def thumb(src, dst): subprocess.run(['sips','-s','format','jpeg','-s','formatOptions','70','-Z','360',src,'--out',dst],check=True,capture_output=True)
def ok_title(main, t): return difflib.SequenceMatcher(None, n(main), n(re.split(r'[:(]', t)[0])).ratio() >= 0.8
for i in R['redo']:
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
            qs = f'intitle:{main}' + (f' inauthor:{sur}' if sur else '')
            g = json.loads(get('https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': qs, 'maxResults': 10})))
            for it in g.get('items', []):
                v = it['volumeInfo']; il = v.get('imageLinks', {})
                if not il or not ok_title(main, v.get('title', '')): continue
                if sur and not any(n(sur) in n(x) for x in v.get('authors', [])): continue
                u = (il.get('thumbnail') or il.get('smallThumbnail')).replace('http://', 'https://').replace('&edge=curl', '') + '&fife=w400'
                data = get(u)
                if len(data) > 5000: found = (f"GB_{it['id']}", data, 'GB ' + v['title']); break
        if found:
            fn, data, lab = found; tmp = f'/tmp/{fn}.jpg'; open(tmp, 'wb').write(data); thumb(tmp, f'{OUT}/{fn}.jpg'); res[i] = [fn, lab]
        else: res[i] = [None, 'nomatch2']
    except Exception as e: res[i] = [None, 'err ' + str(e)[:60]]
    print(i, res[i], flush=True); time.sleep(0.8)
json.dump(res, open('_tmp/covers_result2.json', 'w'), ensure_ascii=False)
print('DONE', sum(1 for v in res.values() if v[0]), len(res))
