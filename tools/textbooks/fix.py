import json,re,sys
sys.path.insert(0,'/home/claude/tb'); from tool import build
def fix(slug, dropch=None, dropsec=r'^(\d+[A-Z]?\s*)?(Exercises|Further reading|Notes|Summary.*|Quiz|Test \d+|Review.*|How to solve.*|Conclusions?)$', last=None):
    build(slug)
    p=f'work/{slug}/structure.json'; st=json.load(open(p))
    if dropch: st['chapters']=[c for c in st['chapters'] if not re.search(dropch,c['title'])]
    for c in st['chapters']: c['sections']=[s for s in c['sections'] if not re.match(dropsec,s['title'],re.I)]
    if last: st['chapters'][-1]['end']=last; 
    for c in st['chapters']:
        for s in c['sections']: s['end']=min(s['end'],c['end'])
    json.dump(st,open(p,'w'),indent=1)
    for c in st['chapters']: print(c['start'],c['end'],c['title'],'|',len(c['sections']))
