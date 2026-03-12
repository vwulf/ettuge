#!/usr/bin/env python3
"""
format-transcripts.py

For each consolidated transcript .md file in dnsbhat/ (e.g. 01-idu-kannadade-vyakarana.md):
- Adds <a id="part-N"> anchors to each ## Part N heading
- Where a cleaned transcript exists in transcripts_cleaned/, replaces the raw
  single-line transcript block with the paragraphed cleaned version

Usage:
    python3 format-transcripts.py [--dry-run]
"""

import os
import re
import sys

DNSBHAT_DIR = os.path.join(
    os.path.dirname(__file__), "../md/kannada/dnsbhat"
)
CLEANED_DIR = os.path.join(
    os.path.dirname(__file__), "../md/kannada/transcripts_cleaned"
)

DRY_RUN = "--dry-run" in sys.argv


def load_cleaned(video_id: str):
    """Return the cleaned transcript body (after the === separator), or None."""
    path = os.path.join(CLEANED_DIR, f"{video_id}.txt")
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8").read()
    # Content follows the === separator line
    sep = "=" * 20
    idx = text.find(sep)
    if idx == -1:
        return text.strip()
    content = text[idx:].lstrip("=").strip()
    # Strip a second === block if present (some files have a double separator)
    if content.startswith("="):
        idx2 = content.find("\n")
        content = content[idx2:].strip()
    return content if content else None


def anchor_tag(part_num: int) -> str:
    return f'<a id="part-{part_num}"></a>\n\n'


def process_file(md_path: str):
    """
    Process one consolidated transcript .md file.
    Returns (parts_anchored, parts_replaced).
    """
    original = open(md_path, encoding="utf-8").read()
    lines = original.split("\n")
    output_lines = []
    i = 0
    parts_anchored = 0
    parts_replaced = 0

    while i < len(lines):
        line = lines[i]

        # Detect ## Part N heading (not already anchored above it)
        part_match = re.match(r'^## Part (\d+)\s*$', line)
        if part_match:
            part_num = int(part_match.group(1))

            # Inject anchor before the heading (only if not already present)
            prev_non_empty = next(
                (l for l in reversed(output_lines) if l.strip()), ""
            )
            if f'<a id="part-{part_num}">' not in prev_non_empty:
                output_lines.append(f'<a id="part-{part_num}"></a>')
                output_lines.append('')
                parts_anchored += 1

            output_lines.append(line)  # ## Part N
            i += 1

            # Collect the YouTube link line (immediately follows heading)
            yt_line = ""
            while i < len(lines) and lines[i].strip() == "":
                output_lines.append(lines[i])
                i += 1
            if i < len(lines) and "youtube.com/watch" in lines[i]:
                yt_line = lines[i]
                output_lines.append(yt_line)
                i += 1
            else:
                # No YouTube link — just continue
                continue

            # Extract video ID
            vid_match = re.search(r'youtube\.com/watch\?v=([\w-]+)', yt_line)
            if not vid_match:
                continue
            video_id = vid_match.group(1)

            # Collect existing transcript block (up to next --- or ## heading)
            raw_block_lines = []
            while i < len(lines):
                peek = lines[i]
                if re.match(r'^---\s*$', peek) or re.match(r'^## ', peek):
                    break
                raw_block_lines.append(peek)
                i += 1

            cleaned = load_cleaned(video_id)
            if cleaned:
                # Replace with cleaned paragraphed content
                output_lines.append("")
                output_lines.extend(cleaned.split("\n"))
                output_lines.append("")
                parts_replaced += 1
            else:
                # Keep original block as-is
                output_lines.extend(raw_block_lines)

            continue

        output_lines.append(line)
        i += 1

    result = "\n".join(output_lines)
    if result != original:
        if not DRY_RUN:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(result)

    return parts_anchored, parts_replaced


def main():
    if not os.path.isdir(DNSBHAT_DIR):
        print(f"ERROR: dnsbhat dir not found: {DNSBHAT_DIR}")
        sys.exit(1)
    if not os.path.isdir(CLEANED_DIR):
        print(f"ERROR: transcripts_cleaned dir not found: {CLEANED_DIR}")
        sys.exit(1)

    if DRY_RUN:
        print("DRY RUN — no files will be written\n")

    total_anchored = 0
    total_replaced = 0

    for book_dir in sorted(os.listdir(DNSBHAT_DIR)):
        full_dir = os.path.join(DNSBHAT_DIR, book_dir)
        if not os.path.isdir(full_dir):
            continue

        for fname in os.listdir(full_dir):
            # Match NN-slug.md (not -book, -kn, -en, -eke, -blog, -djvu, -website, etc.)
            if not re.match(r'^\d{2}-[^.]+\.md$', fname):
                continue

            md_path = os.path.join(full_dir, fname)
            anchored, replaced = process_file(md_path)
            if anchored or replaced:
                print(f"{fname}: {anchored} anchors added, {replaced} parts replaced with cleaned transcript")
                total_anchored += anchored
                total_replaced += replaced

    print(f"\nTotal: {total_anchored} anchors added, {total_replaced} parts replaced")
    if DRY_RUN:
        print("(DRY RUN — nothing written)")


if __name__ == "__main__":
    main()
