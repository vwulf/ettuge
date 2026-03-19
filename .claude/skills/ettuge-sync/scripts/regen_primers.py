"""
Regenerates docs/claude-book-primers-1.md and docs/claude-book-primers-2.md
from current *-claude-prompt.md files in the dnsbhat book directories.
Greedy-packs books into Part 1 up to 195k chars, remainder goes to Part 2.
Run from any directory: python3 regen_primers.py
"""
import os, glob

REPO = "/Users/vishwas/code/ettuge"
dnsbhat_base = f"{REPO}/src/main/md/kannada/dnsbhat"
out1 = f"{REPO}/docs/claude-book-primers-1.md"
out2 = f"{REPO}/docs/claude-book-primers-2.md"
LIMIT = 195_000

header_a = """# Ettuge DNS Bhat — Book Primers, Part 1

Detailed AI context primers for DNS Bhat books: thesis, key terms, chapter map, notable examples.
For book catalogue and file structure, see `claude-project-instructions.md`.
For remaining book primers, see `claude-book-primers-2.md`.

---
"""

header_b = """# Ettuge DNS Bhat — Book Primers, Part 2

Detailed AI context primers for DNS Bhat books (continued).
For book catalogue and file structure, see `claude-project-instructions.md`.
For earlier book primers, see `claude-book-primers-1.md`.

---
"""

prompt_files = sorted(glob.glob(f"{dnsbhat_base}/*/*-claude-prompt.md"))

items = []
for f in prompt_files:
    text = open(f).read()
    book_dir = os.path.basename(os.path.dirname(f))
    book_num = int(book_dir.split('-')[0])
    items.append((book_num, book_dir, text))

part1, part2 = [], []
running = len(header_a)
for item in items:
    block = f"---\n\n## Book {item[0]:02d} — {item[1]}\n\n{item[2].strip()}\n\n"
    if running + len(block) < LIMIT:
        part1.append(block)
        running += len(block)
    else:
        part2.append(block)

combined1 = header_a + "\n".join(part1)
combined2 = header_b + "\n".join(part2)
open(out1, "w").write(combined1)
open(out2, "w").write(combined2)

def status(chars): return "✅ OK" if chars < 200000 else f"❌ TOO LARGE ({chars-200000:,} over)"
p1_books = [item[0] for item in items[:len(part1)]]
p2_books = [item[0] for item in items[len(part1):]]
print(f"primers-1: {len(combined1):,} chars — {status(len(combined1))}  books: {p1_books}")
print(f"primers-2: {len(combined2):,} chars — {status(len(combined2))}  books: {p2_books}")
