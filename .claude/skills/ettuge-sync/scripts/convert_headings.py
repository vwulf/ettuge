#!/usr/bin/env python3
"""
Convert plain-text chapter and section headings to Markdown ##/###/#### in
DNS Bhat kn.md and kn-eke.md files.

Books and transformations:
  07-vol1, 07-vol2, 17 (kn + kn-eke): chapter N. Title → ## N. Title (join multi-line)
  25 (kn + kn-eke): ಅಧ್ಯಾಯ/adhyAya multi-line → ## combined title
  28, 29 (kn + kn-eke): chapter ## already done — skip
  All 07, 17, 25, 28, 29: N.M → ###, N.M.K → #### (body only, not pre-anchor TOC)

Run from any directory: python3 convert_headings.py
"""
import re, os, sys

REPO = "/Users/vishwas/code/ettuge"
BASE = f"{REPO}/src/main/md/kannada/dnsbhat"

FILES_07_17 = [
    f"{BASE}/07-kannaDa-barahada-sollarime/07-kannaDa-barahada-sollarime-vol1-kn.md",
    f"{BASE}/07-kannaDa-barahada-sollarime/07-kannaDa-barahada-sollarime-vol1-kn-eke.md",
    f"{BASE}/07-kannaDa-barahada-sollarime/07-kannaDa-barahada-sollarime-vol2-kn.md",
    f"{BASE}/07-kannaDa-barahada-sollarime/07-kannaDa-barahada-sollarime-vol2-kn-eke.md",
    f"{BASE}/17-kannaDa-nuDi-naDeDu-banda-dAri/17-kannaDa-nuDi-naDeDu-banda-dAri-kn.md",
    f"{BASE}/17-kannaDa-nuDi-naDeDu-banda-dAri/17-kannaDa-nuDi-naDeDu-banda-dAri-kn-eke.md",
]
FILES_25 = [
    f"{BASE}/25-kannaDa-vAkyagaLa-oLaracane/25-kannaDa-vAkyagaLa-oLaracane-kn.md",
    f"{BASE}/25-kannaDa-vAkyagaLa-oLaracane/25-kannaDa-vAkyagaLa-oLaracane-kn-eke.md",
]
FILES_28_29 = [
    f"{BASE}/28-kannaDakke-bEku/28-kannaDakke-bEku-kn.md",
    f"{BASE}/28-kannaDakke-bEku/28-kannaDakke-bEku-kn-eke.md",
    f"{BASE}/29-kannaDa-vyAkaraNa-yAke-bEku/29-kannaDa-vyAkaraNa-yAke-bEku-kn.md",
    f"{BASE}/29-kannaDa-vyAkaraNa-yAke-bEku/29-kannaDa-vyAkaraNa-yAke-bEku-kn-eke.md",
]

SEC3_PAT = re.compile(r'^(\d{1,2}\.\d{1,3}\.\d{1,3})\.?\s+(.*\S)')
SEC2_PAT = re.compile(r'^(\d{1,2}\.\d{1,3})\s+(.*\S)')
CHAP_PAT = re.compile(r'^(\d{1,2}\.)\s+(.*\S)')

def ensure_blank_before(out):
    """Ensure the last line in out is a blank line; add one if not."""
    if out and out[-1].strip():
        out.append('\n')

def convert_section_headings(lines, first_anchor):
    """Convert N.M → ### and N.M.K → #### for lines after first_anchor."""
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if i >= first_anchor and not line.startswith('#') and not line.startswith(' '):
            m3 = SEC3_PAT.match(stripped)
            if m3:
                ensure_blank_before(out)
                out.append(f"#### {m3.group(1)} {m3.group(2)}\n")
                out.append('\n')
                i += 1
                continue

            m2 = SEC2_PAT.match(stripped)
            if m2:
                ensure_blank_before(out)
                out.append(f"### {m2.group(1)} {m2.group(2)}\n")
                out.append('\n')
                i += 1
                continue

        out.append(line)
        i += 1
    return out


def process_07_17(path):
    """Books 07/17: convert chapter N. Title (multi-line join) + section headings."""
    with open(path) as f:
        lines = f.readlines()

    first_anchor = next((i for i, l in enumerate(lines) if '<a id="adhyAya-' in l), -1)
    if first_anchor < 0:
        print(f"  SKIP (no anchors): {os.path.basename(path)}")
        return

    out = []
    i = 0
    post_anchor = False  # True right after seeing an adhyAya anchor

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Detect any adhyAya anchor
        if '<a id="adhyAya-' in line:
            post_anchor = True
            out.append(line)
            i += 1
            continue

        if post_anchor:
            # Skip blank lines and the link line (starts with '[')
            if stripped == '' or stripped.startswith('['):
                out.append(line)
                i += 1
                continue

            # Expect chapter title: "N. Title text"
            m = CHAP_PAT.match(stripped)
            if m:
                prefix = m.group(1)   # e.g., "1." or "10."
                title = m.group(2)    # e.g., "ಮುನ್ನೋಟ"

                # Look-ahead: immediate next line is continuation if non-blank
                # and doesn't start with digit+dot (section heading)
                continuation = []
                j = i + 1
                while j < len(lines):
                    nxt = lines[j].strip()
                    if not nxt:
                        break  # blank → end of title
                    if re.match(r'^\d{1,2}\.', nxt):
                        break  # section number → end of title
                    if nxt.startswith('['):
                        break  # link line → weird but stop
                    continuation.append(nxt)
                    j += 1

                parts = [title] + continuation
                combined = ' '.join(parts)
                heading = f"## {prefix} {combined}\n"

                ensure_blank_before(out)
                out.append(heading)
                out.append('\n')

                # Advance past continuation lines we consumed
                i = j
                post_anchor = False
                continue
            else:
                post_anchor = False
                # Fall through to normal output

        out.append(line)
        i += 1

    # Now apply section heading conversion to result
    out = convert_section_headings(out, first_anchor)

    with open(path, 'w') as f:
        f.writelines(out)
    print(f"  DONE 07/17: {os.path.basename(path)}")


def process_25(path):
    """Book 25: convert ಅಧ್ಯಾಯ/adhyAya multi-line chapter titles + section headings."""
    with open(path) as f:
        lines = f.readlines()

    first_anchor = next((i for i, l in enumerate(lines) if '<a id="adhyAya-' in l), -1)
    if first_anchor < 0:
        print(f"  SKIP (no anchors): {os.path.basename(path)}")
        return

    # Detect whether this is kn.md (Kannada) or kn-eke.md (Eke romanisation)
    is_eke = path.endswith('-kn-eke.md')
    chap_trigger = re.compile(r'^adhyAya ' if is_eke else r'^ಅಧ್ಯಾಯ ')

    out = []
    i = 0
    post_anchor = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if '<a id="adhyAya-' in line:
            post_anchor = True
            out.append(line)
            i += 1
            continue

        if post_anchor:
            # Skip link line (starts with '[')
            if stripped.startswith('['):
                out.append(line)
                i += 1
                continue

            # Book 25: no blank lines between anchor, link, and title
            # Look for the adhyAya/ಅಧ್ಯಾಯ trigger line
            if chap_trigger.match(stripped):
                # Collect all consecutive non-blank lines until a section heading
                title_parts = [stripped]
                j = i + 1
                while j < len(lines):
                    nxt = lines[j].strip()
                    if not nxt:
                        break  # blank → end of title block
                    if re.match(r'^\d{1,2}\.\d', nxt):
                        break  # section heading → end of title
                    title_parts.append(nxt)
                    j += 1

                # Build: "## adhyAya X — title rest"
                first_line = title_parts[0]
                rest = ' '.join(title_parts[1:])
                if rest:
                    heading = f"## {first_line} — {rest}\n"
                else:
                    heading = f"## {first_line}\n"

                ensure_blank_before(out)
                out.append(heading)
                out.append('\n')

                i = j
                post_anchor = False
                continue
            else:
                post_anchor = False

        out.append(line)
        i += 1

    # Section heading conversion
    out = convert_section_headings(out, first_anchor)

    with open(path, 'w') as f:
        f.writelines(out)
    print(f"  DONE 25: {os.path.basename(path)}")


def process_28_29(path):
    """Books 28/29: section headings only (chapter ## already done)."""
    with open(path) as f:
        lines = f.readlines()

    first_anchor = next((i for i, l in enumerate(lines) if '<a id="adhyAya-' in l), -1)
    if first_anchor < 0:
        print(f"  SKIP (no anchors): {os.path.basename(path)}")
        return

    out = convert_section_headings(lines, first_anchor)

    with open(path, 'w') as f:
        f.writelines(out)
    print(f"  DONE 28/29: {os.path.basename(path)}")


if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("DRY RUN — no files will be modified")

    print("\nProcessing books 07 and 17...")
    for p in FILES_07_17:
        if not os.path.exists(p):
            print(f"  NOT FOUND: {p}")
            continue
        if dry_run:
            print(f"  WOULD process: {os.path.basename(p)}")
        else:
            process_07_17(p)

    print("\nProcessing book 25...")
    for p in FILES_25:
        if not os.path.exists(p):
            print(f"  NOT FOUND: {p}")
            continue
        if dry_run:
            print(f"  WOULD process: {os.path.basename(p)}")
        else:
            process_25(p)

    print("\nProcessing books 28 and 29...")
    for p in FILES_28_29:
        if not os.path.exists(p):
            print(f"  NOT FOUND: {p}")
            continue
        if dry_run:
            print(f"  WOULD process: {os.path.basename(p)}")
        else:
            process_28_29(p)

    print("\nDone.")
