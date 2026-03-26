"""
Regenerates docs/claude-book-primers-1.md and docs/claude-book-primers-2.md
from current claude-prompt.md files in the dnsbhat book directories.
Each book section ends with a compact Chapter Navigation block (where chapters exist).
Greedy-packs books into Part 1 up to 195k chars, remainder goes to Part 2.
Run from any directory: python3 regen_primers.py
"""
import os, re, glob

REPO = "/Users/vishwas/code/ettuge"
dnsbhat_base = f"{REPO}/src/main/md/kannada/dnsbhat"
out1 = f"{REPO}/docs/claude-book-primers-1.md"
out2 = f"{REPO}/docs/claude-book-primers-2.md"
GH_BASE = "https://vwulf.github.io/ettuge/kannaDa/dnsbhat"
LIMIT = 195_000

ANCHOR_RE = re.compile(r'<a id="(?:ch|adhyAya-)(\d+)">')

header_a = """# Ettuge DNS Bhat — Book Primers, Part 1

Detailed AI context primers for DNS Bhat books: thesis, key terms, chapter map, notable examples.
Each book ends with a **Chapter Navigation** block listing chapter titles and GitHub Pages fetch URLs.
For book catalogue and file structure, see `claude-project-instructions.md`.
For remaining book primers, see `claude-book-primers-2.md`.

---
"""

header_b = """# Ettuge DNS Bhat — Book Primers, Part 2

Detailed AI context primers for DNS Bhat books (continued).
Each book ends with a **Chapter Navigation** block listing chapter titles and GitHub Pages fetch URLs.
For book catalogue and file structure, see `claude-project-instructions.md`.
For earlier book primers, see `claude-book-primers-1.md`.

---
"""


def strip_fm(text):
    if text.startswith("---\n"):
        m = re.match(r"^---\n.*?\n---\n\n?", text, re.DOTALL)
        if m:
            return text[m.end():]
    return text


def extract_chapters(fp):
    """Return list of (ch_num, heading) from a full.md, using TOC fallback."""
    with open(fp, encoding="utf-8") as f:
        text = strip_fm(f.read())
    lines = text.split("\n")

    # Build TOC heading map: [Title](#adhyAya-N) or [Title](#chN)
    toc_re = re.compile(r"\[([^\]]+)\]\(#(?:adhyAya-|ch)(\d+)\)")
    toc_map = {}
    for line in lines:
        for m in toc_re.finditer(line):
            n = int(m.group(2))
            if n not in toc_map:
                toc_map[n] = m.group(1).strip()

    results = []
    for i, line in enumerate(lines):
        m = ANCHOR_RE.search(line)
        if not m:
            continue
        ch_num = int(m.group(1))

        # Look immediately after anchor for a heading line.
        # STOP if we hit another anchor (we've left the chapter heading zone).
        heading = ""
        for j in range(i + 1, min(i + 12, len(lines))):
            s = lines[j].strip()
            if not s:
                continue
            if s.startswith("<a "):
                break  # another anchor = end of chapter heading zone
            # Skip cross-link lines like [English →](...) [Eke →](...) [↑ ...]
            if re.match(r"\[(?:[A-Za-zಕ↑]|English|Eke|ಇಂ)", s) and "](http" not in s:
                continue
            heading = re.sub(r"^#+\s*", "", s)
            heading = re.sub(r"<[^>]+>", "", heading).strip()
            if heading:
                break

        # Fallback 1: TOC map
        if not heading and ch_num in toc_map:
            heading = toc_map[ch_num]

        # Fallback 2: generic label
        if not heading:
            heading = f"ಅಧ್ಯಾಯ {ch_num}"

        results.append((ch_num, heading))
    return results


def chapter_nav_block(slug):
    """
    Build a compact chapter navigation section for a book.
    Returns empty string if no chapters found.
    Groups by volume for multi-volume books.
    """
    bpath = os.path.join(dnsbhat_base, slug)

    # Find all kn/full.md files (book/kn/full.md and book/volN/kn/full.md)
    kn_fulls = sorted(
        glob.glob(os.path.join(bpath, "book", "*", "kn", "full.md")) +
        glob.glob(os.path.join(bpath, "book", "kn", "full.md"))
    )
    if not kn_fulls:
        return ""

    groups = []  # list of (label, sub_path, [(ch_num, heading)])
    for fp in kn_fulls:
        rel = fp[len(os.path.join(dnsbhat_base, slug)) + 1:]   # e.g. book/kn/full.md
        sub_path = "/".join(rel.split("/")[:-1])                 # e.g. book/kn
        chs = extract_chapters(fp)
        if not chs:
            continue
        # Label: "Vol N" for book/volN/kn, plain for book/kn
        parts = sub_path.split("/")
        if len(parts) == 3 and parts[1].startswith("vol"):
            label = parts[1].capitalize()
        else:
            label = None
        groups.append((label, sub_path, chs))

    if not groups:
        return ""

    lines = ["\n### Chapter Navigation\n"]
    for label, sub_path, chs in groups:
        if label:
            lines.append(f"**{label}:** ")
        else:
            lines.append("**Chapters:** ")
        links = []
        for ch_num, heading in chs:
            url = f"{GH_BASE}/{slug}/{sub_path}/ch{ch_num}"
            # Strip redundant chapter-number prefixes from heading:
            #   "ಅಧ್ಯಾಯ ೧ — ..." → "..."
            #   "ಭಾಗ ಒಂದು — ..." → "..."
            #   "1. ..." / "1 ..." → "..."
            short = heading
            short = re.sub(r"^(?:ಅಧ್ಯಾಯ|ಭಾಗ)\s+\S+\s*[—–-]\s*", "", short).strip()
            short = re.sub(r"^\d+[.\s]+", "", short).strip()
            if not short:
                short = heading
            links.append(f"[{ch_num}. {short}]({url})")
        lines.append("  \n".join(f"  {l}" for l in links) + "\n")

    return "\n".join(lines) + "\n"


# Build items list: (book_num, book_dir, full_block_text)
prompt_files = sorted(glob.glob(f"{dnsbhat_base}/*/claude-prompt.md"))

items = []
for f in prompt_files:
    prompt_text = open(f, encoding="utf-8").read()
    book_dir = os.path.basename(os.path.dirname(f))
    try:
        book_num = int(book_dir.split("-")[0])
    except ValueError:
        continue
    nav = chapter_nav_block(book_dir)
    items.append((book_num, book_dir, prompt_text, nav))

items.sort(key=lambda x: x[0])

part1, part2 = [], []
running = len(header_a)
for item in items:
    book_num, book_dir, prompt_text, nav = item
    block = f"---\n\n## Book {book_num:02d} — {book_dir}\n\n{prompt_text.strip()}\n{nav}\n"
    if running + len(block) < LIMIT:
        part1.append(block)
        running += len(block)
    else:
        part2.append(block)

combined1 = header_a + "\n".join(part1)
combined2 = header_b + "\n".join(part2)
open(out1, "w", encoding="utf-8").write(combined1)
open(out2, "w", encoding="utf-8").write(combined2)


def status(chars):
    return "✅ OK" if chars < 200000 else f"❌ TOO LARGE ({chars - 200000:,} over)"


p1_books = [item[0] for item in items[:len(part1)]]
p2_books = [item[0] for item in items[len(part1):]]
print(f"primers-1: {len(combined1):,} chars — {status(len(combined1))}  books: {p1_books}")
print(f"primers-2: {len(combined2):,} chars — {status(len(combined2))}  books: {p2_books}")
