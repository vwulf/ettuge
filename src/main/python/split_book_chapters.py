#!/usr/bin/env python3
"""
split_book_chapters.py
======================
Split a DNS Bhat book's kn/full.md into per-chapter page files,
mirroring the pattern used for Book 31 (ch0.md index + ch1.md…chN.md).

Split boundary: lines containing  <a id="adhyAya-N">  (chapter-level anchors).
Section anchors (sec-*, sub-*) stay inside their chapter file.

Usage:
    python3 split_book_chapters.py <full_md_path> [<output_dir>]

Examples:
    # Vol 1 — writes ch0.md…ch4.md into vol1/kn/
    python3 split_book_chapters.py \\
        src/main/md/kannada/dnsbhat/07-.../book/vol1/kn/full.md

    # Vol 2 — same directory
    python3 split_book_chapters.py \\
        src/main/md/kannada/dnsbhat/07-.../book/vol2/kn/full.md

Output:
    <output_dir>/ch0.md   — chapter index (TOC extracted from full.md frontmatter)
    <output_dir>/ch1.md   — chapter 1 content
    <output_dir>/ch2.md   — chapter 2 content
    ...

The original full.md is NOT modified.
"""

import re
import sys
from pathlib import Path


# ── helpers ────────────────────────────────────────────────────────────────

ANCHOR_RE = re.compile(r'<a id="(adhyAya-\d+)"')


def find_chapter_boundaries(lines: list[str]) -> list[tuple[str, int]]:
    """Return [(anchor_id, line_index), ...] for every adhyAya anchor."""
    boundaries = []
    for i, line in enumerate(lines):
        m = ANCHOR_RE.search(line)
        if m:
            boundaries.append((m.group(1), i))
    return boundaries


def extract_frontmatter_and_toc(lines: list[str]) -> list[str]:
    """
    Return everything before the first <a id="adhyAya-"> anchor —
    the YAML front matter, title, metadata block, and ಒಳಪಿಡಿ / ಪರಿವಿಡಿ TOC.
    """
    for i, line in enumerate(lines):
        if ANCHOR_RE.search(line):
            return lines[:i]
    return lines  # no anchors found — return everything


def chapter_title_from_lines(lines: list[str]) -> str:
    """
    Find the first ## or # heading after an anchor tag.
    Used to label the ch0 index entry.
    """
    for line in lines[:20]:
        stripped = line.strip()
        if stripped.startswith('## ') or stripped.startswith('# '):
            # strip leading #s and whitespace
            return re.sub(r'^#+\s*', '', stripped)
    return '(no title)'


# ── main ───────────────────────────────────────────────────────────────────

def split(full_md: Path, out_dir: Path) -> None:
    lines = full_md.read_text(encoding='utf-8').splitlines(keepends=True)
    boundaries = find_chapter_boundaries(lines)

    if not boundaries:
        print(f'  ⚠  No adhyAya anchors found in {full_md}. Nothing to split.')
        return

    out_dir.mkdir(parents=True, exist_ok=True)

    # ── ch0: index ──────────────────────────────────────────────────────
    toc_lines = extract_frontmatter_and_toc(lines)

    # Derive the relative path from out_dir back up to full.md so links work
    # GitHub Pages serves ch1 alongside full from the same dir, so links are simple
    chapter_links = []
    for idx, (anchor_id, line_no) in enumerate(boundaries, start=1):
        ch_lines = lines[line_no: boundaries[idx][1] if idx < len(boundaries) else len(lines)]
        title = chapter_title_from_lines(ch_lines)
        n = anchor_id.split('-')[1]   # "adhyAya-5" → "5"
        chapter_links.append(f'- [ಅಧ್ಯಾಯ {n} — {title}](ch{idx})\n')

    ch0_content = (
        ''.join(toc_lines)
        + '\n---\n\n## ಅಧ್ಯಾಯಗಳ ಸೂಚಿ (Chapter Index)\n\n'
        + ''.join(chapter_links)
        + '\n[← full.md (complete text)](full)\n'
    )
    (out_dir / 'ch0.md').write_text(ch0_content, encoding='utf-8')
    print(f'  ✅ ch0.md  ({len(toc_lines) + len(chapter_links) + 4} lines)')

    # ── ch1…chN: one file per chapter ───────────────────────────────────
    for idx, (anchor_id, start_line) in enumerate(boundaries, start=1):
        end_line = boundaries[idx][1] if idx < len(boundaries) else len(lines)
        chapter_lines = lines[start_line:end_line]

        # Prepend navigation links
        n = anchor_id.split('-')[1]
        prev_link = f'[← ಅಧ್ಯಾಯ {int(n)-1}](ch{idx-1})' if idx > 1 else '[← ಒಳಪಿಡಿ](ch0)'
        next_link = f'[ಅಧ್ಯಾಯ {int(n)+1} →](ch{idx+1})' if idx < len(boundaries) else ''
        nav = f'{prev_link}  |  [ಒಳಪಿಡಿ](ch0)  {("| " + next_link) if next_link else ""}\n\n'

        content = nav + ''.join(chapter_lines)
        out_path = out_dir / f'ch{idx}.md'
        out_path.write_text(content, encoding='utf-8')
        print(f'  ✅ ch{idx}.md  anchor={anchor_id}  lines={end_line - start_line}')

    print(f'\n  Total: {len(boundaries)} chapter files + ch0 index → {out_dir}')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    full_md = Path(sys.argv[1]).resolve()
    if not full_md.exists():
        print(f'Error: {full_md} not found')
        sys.exit(1)

    out_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else full_md.parent

    print(f'\nSplitting: {full_md}')
    print(f'Output to: {out_dir}\n')
    split(full_md, out_dir)


if __name__ == '__main__':
    main()
