import sys; sys.path.insert(0,'/home/claude/tb'); from tool import assemble, add_terms
def Q(slug, meta, chapters):
    """chapters: list of (chapter_summary, 'sec1 | sec2 | ...', 'termsA ; termsB ; ...') — terms per section comma-separated.
    For a sectionless chapter give '' for sections and a single comma list for terms."""
    cs=[c[0] for c in chapters]
    ss=[[x.strip() for x in c[1].split(' | ')] if c[1] else [] for c in chapters]
    assemble(slug, meta, cs, ss)
    tt=[]
    for c in chapters:
        if c[1]: tt.append([[y.strip() for y in g.split(',') if y.strip()] for g in c[2].split(';')])
        else: tt.append([y.strip() for y in c[2].split(',') if y.strip()])
    add_terms(slug, tt)
def QL(slug, meta, chapters):
    """Light mode for very granular books: chapters = (summary, 'chapter terms comma list'); sections keep titles only."""
    import json, os
    st=json.load(open(f'/home/claude/tb/work/{slug}/structure.json'))
    assemble(slug, meta, [c[0] for c in chapters], [['' for _ in c['sections']] for c in st['chapters']])
    p=f'/home/claude/tb/work/{slug}/book.json'; bk=json.load(open(p))
    for c,(sm,tt) in zip(bk['chapters'],chapters): c['terms']=[x.strip() for x in tt.split(',') if x.strip()]
    json.dump(bk,open(p,'w'),indent=1,ensure_ascii=False)
    from tool import render; render(slug)
