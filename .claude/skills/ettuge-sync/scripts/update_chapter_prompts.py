"""
Appends chapter-page navigation items to claude-prompt.md files for all
books that have been split into chapter pages by the CI build.

For each book with ≥2 chapter anchors:
  - Finds the last numbered item in ## INSTRUCTIONS FOR ANSWERING QUESTIONS
  - Appends a new item listing ch0 index URL + per-chapter fetch URLs
  - Skips books already updated (have GH Pages chapter URL in prompt)
  - Books with no INSTRUCTIONS section get one appended

Run from any directory: python3 update_chapter_prompts.py
"""
import os, re, glob

REPO = "/Users/vishwas/code/ettuge"
GH_BASE = "https://vwulf.github.io/ettuge/kannaDa/dnsbhat"
CHAPTER_RE = re.compile(r'<a id="(?:ch|adhyAya-)(\d+)">')
dnsbhat = f"{REPO}/src/main/md/kannada/dnsbhat"

CANDIDATES = [
    ('book/kn',      'book/kn/full.md'),
    ('book/vol1/kn', 'book/vol1/kn/full.md'),
    ('book/vol2/kn', 'book/vol2/kn/full.md'),
    ('book/vol3/kn', 'book/vol3/kn/full.md'),
    ('book/vol4/kn', 'book/vol4/kn/full.md'),
]


def strip_fm(text):
    if text.startswith('---\n'):
        m = re.match(r'^---\n.*?\n---\n\n?', text, re.DOTALL)
        if m:
            return text[m.end():]
    return text


def first_heading(text):
    m = re.search(r'^## (.+)$', text, re.MULTILINE)
    if m:
        h = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', m.group(1))
        h = re.sub(r'\*+([^*]+)\*+', r'\1', h).strip()
        h = re.sub(r'^[\d\u0CE6-\u0CEF]+[.\s]+', '', h).strip()
        return h
    return ''


def toc_title_map(body):
    result = {}
    for m in re.finditer(r'\[([^\]]+)\]\(#(?:adhyAya-|ch)(\d+)\)', body):
        n = int(m.group(2))
        if n not in result:
            t = m.group(1).strip()
            t = re.sub(r'^(?:ಅಧ್ಯಾಯ|Chapter)\s+\S+\s*[—\u2013-]\s*', '', t).strip()
            t = re.sub(r'^\d+[.\s]+', '', t).strip()
            if t:
                result[n] = t
    return result


def get_chapters(fp, sub_path, slug):
    body = strip_fm(open(fp, encoding='utf-8').read())
    positions = [(int(m.group(1)), m.start()) for m in CHAPTER_RE.finditer(body)]
    if len(positions) < 2:
        return []
    toc = toc_title_map(body)
    base_url = f"{GH_BASE}/{slug}/{sub_path}"
    result = []
    for i, (chnum, start) in enumerate(positions):
        end = positions[i+1][1] if i+1 < len(positions) else len(body)
        title = toc.get(chnum, '') or first_heading(body[start:end].strip())
        result.append((chnum, title, f"{base_url}/ch{chnum}"))
    return result


def last_item_num(prompt_text):
    """Highest numbered item in INSTRUCTIONS section."""
    in_section = False
    max_n = 0
    for line in prompt_text.split('\n'):
        if '## INSTRUCTIONS FOR ANSWERING QUESTIONS' in line:
            in_section = True
            continue
        if in_section and line.startswith('## '):
            break
        if in_section:
            m = re.match(r'^(\d+)\.\s', line)
            if m:
                max_n = max(max_n, int(m.group(1)))
    return max_n


def build_item(new_n, slug, all_vol_chapters):
    multi = len(all_vol_chapters) > 1
    lines = [
        f"\n{new_n}. **Chapter pages (Phase 33):** The Kannada source is split into"
        f" individual chapter pages on GitHub Pages. Fetch specific chapters"
        f" rather than loading the full book — chapters are lightweight and"
        f" avoid token exhaustion when answering focused questions:"
    ]
    for sub_path, chs in all_vol_chapters:
        if multi:
            vol = sub_path.split('/')[1].capitalize()
            lines.append(f"   - **{vol} index:** `{GH_BASE}/{slug}/{sub_path}/ch0`")
        else:
            lines.append(f"   - **Chapter index (ch0):** `{GH_BASE}/{slug}/{sub_path}/ch0`")
        for chnum, title, url in chs:
            title_part = f" — {title}" if title else ''
            lines.append(f"   - Ch {chnum}{title_part}: `{url}`")
    lines.append(
        "   \n   When a question targets a specific chapter, fetch only that URL."
        " Use `ch0` to browse the full chapter list first."
    )
    return '\n'.join(lines)


updated = []
skipped = []

for book_dir in sorted(os.listdir(dnsbhat)):
    bp = os.path.join(dnsbhat, book_dir)
    if not os.path.isdir(bp):
        continue
    prompt_path = os.path.join(bp, 'claude-prompt.md')
    if not os.path.exists(prompt_path):
        continue

    slug = book_dir
    all_vol_chapters = []
    for sub_path, rel in CANDIDATES:
        fp = os.path.join(bp, rel)
        if not os.path.exists(fp):
            continue
        chs = get_chapters(fp, sub_path, slug)
        if chs:
            all_vol_chapters.append((sub_path, chs))

    if not all_vol_chapters:
        continue

    prompt_text = open(prompt_path, encoding='utf-8').read()

    # Skip if GH Pages chapter URL already present for this book
    if f"{GH_BASE}/{slug}" in prompt_text and '/ch' in prompt_text:
        skipped.append(book_dir)
        continue

    # Determine item number
    has_instructions = '## INSTRUCTIONS FOR ANSWERING QUESTIONS' in prompt_text
    last_n = last_item_num(prompt_text) if has_instructions else 0
    new_n = last_n + 1

    item = build_item(new_n, slug, all_vol_chapters)

    if has_instructions:
        # Append before any trailing newlines at end of file
        new_text = prompt_text.rstrip() + '\n' + item + '\n'
    else:
        # Add a new INSTRUCTIONS section
        new_text = (prompt_text.rstrip() + '\n\n---\n\n'
                    '## INSTRUCTIONS FOR ANSWERING QUESTIONS\n' + item + '\n')

    open(prompt_path, 'w', encoding='utf-8').write(new_text)
    updated.append(book_dir)
    print(f"✅ Updated: {book_dir} (item {new_n})")

for b in skipped:
    print(f"⏭  Skipped: {b} (chapter URLs already present)")

print(f"\nDone: {len(updated)} updated, {len(skipped)} skipped.")
