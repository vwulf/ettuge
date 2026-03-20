"""
Syncs src/main/md/kannada/dnsbhat/ → docs/dnsbhat/
Preserves Jekyll navigation front matter (title, parent, nav_order, layout, grand_parent)
from the existing docs/ versions. All other content comes from src/ (canonical cleaned source).

Run from any directory: python3 sync_docs.py
"""
import os, re, shutil

REPO = "/Users/vishwas/code/ettuge"
src_base = f"{REPO}/src/main/md/kannada/dnsbhat"
docs_base = f"{REPO}/docs/dnsbhat"
JEKYLL_KEYS = {'title', 'parent', 'nav_order', 'layout', 'grand_parent'}

def parse_frontmatter(text):
    """Returns (fm_dict, body). fm_dict keys preserve insertion order."""
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}, text
    body = text[m.end():]
    fm = {}
    current_key = None
    for line in m.group(1).splitlines():
        if re.match(r'^[a-zA-Z_]', line) and ':' in line:
            k, _, v = line.partition(':')
            k, v = k.strip(), v.strip()
            if v:
                fm[k] = v
            else:
                fm[k] = []
            current_key = k
        elif line.strip().startswith('-') and current_key:
            val = line.strip().lstrip('- ').strip()
            if isinstance(fm[current_key], list):
                fm[current_key].append(val)
    return fm, body

def build_frontmatter(fm_dict):
    lines = ['---']
    for k, v in fm_dict.items():
        if isinstance(v, list):
            lines.append(f'{k}:')
            for item in v:
                lines.append(f'  - {item}')
        elif v:
            lines.append(f'{k}: {v}')
    lines.append('---')
    return '\n'.join(lines) + '\n'

synced = skipped = copied = 0

for book_dir in sorted(os.listdir(src_base)):
    src_book = os.path.join(src_base, book_dir)
    docs_book = os.path.join(docs_base, book_dir)
    if not os.path.isdir(src_book) or not os.path.isdir(docs_book):
        continue

    for fname in sorted(os.listdir(src_book)):
        if not fname.endswith('.md'):
            continue
        src_f = os.path.join(src_book, fname)
        docs_f = os.path.join(docs_book, fname)

        if not os.path.exists(docs_f):
            shutil.copy2(src_f, docs_f)
            print(f"  COPIED  {book_dir[:30]}/{fname}")
            copied += 1
            continue

        src_text = open(src_f).read()
        docs_text = open(docs_f).read()
        if src_text == docs_text:
            skipped += 1
            continue

        # Preserve Jekyll nav keys from docs/; all content from src/
        docs_fm, _ = parse_frontmatter(docs_text)
        src_fm, src_body = parse_frontmatter(src_text)
        merged_fm = dict(src_fm)
        merged_fm.update({k: v for k, v in docs_fm.items() if k in JEKYLL_KEYS})

        new_text = build_frontmatter(merged_fm) + src_body
        if new_text != docs_text:
            open(docs_f, 'w').write(new_text)
            print(f"  SYNCED  {book_dir[:30]}/{fname}")
            synced += 1
        else:
            skipped += 1

print(f"\nDone: {synced} synced, {copied} copied, {skipped} already current")
