"""
Syncs src/main/md/kannada/{dnsbhat,eke}/ → docs/kannaDa/{dnsbhat,eke}/
Preserves Jekyll navigation front matter (title, parent, nav_order, layout, grand_parent)
from the existing docs/ versions. All other content comes from src/ (canonical cleaned source).

Phase B (2026-03-20): Now recursively walks src/ subdirectories (book/kn/, web/eke/, etc.)
and creates matching subdirectory structure in docs/. Orphaned flat docs/ files (old pre-migration
filenames) are deleted since redirect_from metadata in the new files handles old URL redirects.

Phase 27 (2026-03-23): Moved from docs/dnsbhat/ to docs/kannaDa/dnsbhat/; added docs/kannaDa/eke/.
Both sub-trees are synced under docs/kannaDa/.

Run from any directory: python3 sync_docs.py
"""
import os, re, shutil

REPO = "/Users/vishwas/code/ettuge"
JEKYLL_KEYS = {'title', 'parent', 'nav_order', 'layout', 'grand_parent'}

# Source → Docs path pairs to sync
SYNC_PAIRS = [
    (f"{REPO}/src/main/md/kannada/dnsbhat", f"{REPO}/docs/kannaDa/dnsbhat"),
    (f"{REPO}/src/main/md/kannada/eke",     f"{REPO}/docs/kannaDa/eke"),
]

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

total_synced = total_skipped = total_copied = total_deleted = 0

for src_base, docs_base in SYNC_PAIRS:
    if not os.path.isdir(src_base):
        print(f"  SKIP (src not found): {src_base}")
        continue

    os.makedirs(docs_base, exist_ok=True)
    synced = skipped = copied = deleted = 0

    # Step 1: Collect all src/ files (relative to src_base)
    src_rel_files = set()
    for root, dirs, files in os.walk(src_base):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fname in files:
            if fname.endswith('.md'):
                rel = os.path.relpath(os.path.join(root, fname), src_base)
                src_rel_files.add(rel)

    # Step 2: Delete orphaned flat docs/ files (old pre-migration filenames)
    # These are files at depth 1 (book_dir/filename.md) in docs/ that no longer
    # exist at that path in src/ (they've been moved to subdirectories).
    for book_dir in sorted(os.listdir(docs_base)):
        docs_book = os.path.join(docs_base, book_dir)
        if not os.path.isdir(docs_book):
            continue
        for fname in sorted(os.listdir(docs_book)):
            if not fname.endswith('.md'):
                continue
            docs_f = os.path.join(docs_book, fname)
            if os.path.isfile(docs_f):
                rel = os.path.join(book_dir, fname)
                if rel not in src_rel_files:
                    os.remove(docs_f)
                    print(f"  DELETED {rel}")
                    deleted += 1

    # Step 3: Sync all src/ files (recursively) to docs/
    for src_rel in sorted(src_rel_files):
        src_f = os.path.join(src_base, src_rel)
        docs_f = os.path.join(docs_base, src_rel)
        docs_dir = os.path.dirname(docs_f)

        # Create subdirectory in docs/ if needed
        os.makedirs(docs_dir, exist_ok=True)

        if not os.path.exists(docs_f):
            shutil.copy2(src_f, docs_f)
            print(f"  COPIED  {src_rel}")
            copied += 1
            continue

        src_text = open(src_f, encoding='utf-8').read()
        docs_text = open(docs_f, encoding='utf-8').read()
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
            open(docs_f, 'w', encoding='utf-8').write(new_text)
            print(f"  SYNCED  {src_rel}")
            synced += 1
        else:
            skipped += 1

    label = os.path.basename(src_base)
    print(f"\n[{label}] Done: {synced} synced, {copied} copied, {deleted} deleted, {skipped} already current")
    total_synced += synced; total_skipped += skipped
    total_copied += copied; total_deleted += deleted

print(f"\nTotal: {total_synced} synced, {total_copied} copied, {total_deleted} deleted, {total_skipped} already current")
