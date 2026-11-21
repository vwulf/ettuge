#!/usr/bin/env python3
"""Add a linked index and stable, shareable section anchors to a long Markdown page.

Idempotent: re-running strips what a previous run added and regenerates it, so it
can be applied after every resync of a page exported from Claude Docs.

  python3 src/main/python/add_section_index.py src/main/md/pl/lean-ai-formalization.md

What it does
- Gives every ## and ### heading a stable kramdown id:
  "## 6. How much math ..."  -> {#s6}     (URL: .../lean-ai-formalization#s6)
  "### 11.1 The pipeline ..." -> {#s11-1}
  unnumbered headings ("Summary", "References") -> a slug ({#summary})
  Numbered ids stay stable when a heading is reworded, so shared links keep working.
- Inserts a "Contents" index (H2 entries with nested H3 entries) after the byline.
- Adds a small "↑ Contents" link before each H2 so readers can jump back.
"""
import re
import sys

BEGIN = "<!-- section-index:begin -->"
END = "<!-- section-index:end -->"
BACK = "[↑ Contents](#contents)"
HEAD = re.compile(r"^(#{2,3}) (.+?)(?: \{#[\w-]+\})?\s*$")


def slug(text):
    s = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")


def anchor(text):
    m = re.match(r"(\d+(?:\.\d+)*)\.?\s", text)
    return "s" + m.group(1).replace(".", "-") if m else slug(text)


def main(path):
    lines = open(path, encoding="utf-8").read().split("\n")

    # 1. strip anything a previous run added
    out, skipping = [], False
    for ln in lines:
        if ln.strip() == BEGIN:
            skipping = True
            continue
        if skipping:
            skipping = ln.strip() != END
            continue
        if ln.strip() == BACK:
            continue
        out.append(ln)
    lines = out
    # collapse runs of blank lines left behind by stripping
    lines = [ln for i, ln in enumerate(lines) if not (ln == "" and i and lines[i - 1] == "")]

    # 2. anchor headings, collect index entries
    entries, seen, in_code, first_h2 = [], set(), False, True
    out = []
    for ln in lines:
        if ln.startswith("```"):
            in_code = not in_code
        m = None if in_code else HEAD.match(ln)
        if not m:
            out.append(ln)
            continue
        level, text = len(m.group(1)), m.group(2).strip()
        aid = anchor(text)
        assert aid not in seen, f"duplicate anchor {aid!r} for heading {text!r}"
        seen.add(aid)
        entries.append((level, text, aid))
        if level == 2:
            if not first_h2:
                if out and out[-1] != "":
                    out.append("")
                out += [BACK, ""]
            first_h2 = False
        out.append(f"{m.group(1)} {text} {{#{aid}}}")
    lines = out

    # 3. build the index and insert it after the italic byline (or the title)
    idx = [BEGIN, "## Contents {#contents}", ""]
    for level, text, aid in entries:
        indent = "" if level == 2 else "  "
        label = text.replace("[", r"\[").replace("]", r"\]")
        idx.append(f"{indent}- [{label}](#{aid})")
    idx += ["", "*Every heading links to itself: hover (or tap the link icon) and copy the link "
            "to share a section, e.g. `#s6` for section 6.*", END]

    at = next(i for i, ln in enumerate(lines) if ln.startswith("# "))
    if at + 2 < len(lines) and lines[at + 1] == "" and lines[at + 2].startswith("*"):
        at += 2
    lines[at + 1:at + 1] = [""] + idx
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    open(path, "w", encoding="utf-8").write(text if text.endswith("\n") else text + "\n")
    print(f"{path}: {len(entries)} sections indexed")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
