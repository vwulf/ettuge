import json,os,shutil,collections
R=json.load(open('tools/textbooks/registry.json'))
D='src/main/md/deep-dives/textbooks'
for slug,work,cat,title,auth,blurb in R:
    if work: shutil.copy(f'/home/claude/tb/out/{work}.md', f'{D}/{slug}.md')
by=collections.OrderedDict()
order=['AI and Machine Learning','Computer Science','Mathematics','Linguistics and Languages','Physics and Engineering','Other']
for c in order: by[c]=[]
for slug,work,cat,title,auth,blurb in R: by[cat].append((title,auth,slug,blurb))
L=['# Textbooks\n','Books from the Drive *Books* folder, each broken down from the top: the book in a paragraph, then each chapter, then each section, and finally the pages in the PDF where that section sits. The summaries are in our own words; the books themselves stay in Drive, so the page links open only for the owner.\n',
   'Partial PDFs (samples, excerpts, unfinished drafts) are marked as such on their pages. Scanned books that need OCR come later.\n']
for c,items in by.items():
    if not items: continue
    L.append(f'## {c}\n')
    for title,auth,slug,blurb in sorted(items):
        L.append(f'- [{title}]({slug}) ({auth}): {blurb}')
    L.append('')
open(f'{D}/index.md','w').write('\n'.join(L))
print(len(R),'books')
