import json,re
DROP=r'^(Summary|Bibliographical Remarks|Conclusions?|Exercises|Concluding Remarks)$'
def tocbuild(slug,text,off,last,keep_unnumbered=()):
    rows=[]
    for l in text.split('\n'):
        l=l.strip(); m=re.match(r'^(\d+)(?:\.(\d+))?\s+(.*?)\s+(\d+)$',l)
        if m: rows.append((m.group(2) is not None, m.group(3), int(m.group(4))+off))
        else:
            m=re.match(r'^(.*?)\s+(\d+)$',l)
            if m and m.group(1) in keep_unnumbered: rows.append((False,m.group(1),int(m.group(2))+off))
    chs=[]
    for sec,t,p in rows:
        if not sec: chs.append({'title':t,'start':p,'sections':[]})
        else: chs[-1]['sections'].append({'title':t,'start':p})
    bounds=[c['start'] for c in chs]+[last+1]
    for i,c in enumerate(chs):
        c['end']=max(c['start'],bounds[i+1]-1); ss=c['sections']
        for j,s in enumerate(ss): s['end']=max(s['start'],(ss[j+1]['start']-1) if j+1<len(ss) else c['end'])
        c['sections']=[s for s in ss if not re.match(DROP,s['title'])]
    json.dump({'chapters':chs},open(f'work/{slug}/structure.json','w'),indent=1)
    for c in chs: print(c['start'],c['end'],c['title'],'|',len(c['sections']))
