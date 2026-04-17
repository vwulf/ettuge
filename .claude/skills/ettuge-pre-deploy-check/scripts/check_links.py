#!/usr/bin/env python3
"""
ettuge cross-link checker — checks all internal markdown links in src/main/md/
for broken targets (files that don't exist on disk).

Run:
  python3 .claude/skills/ettuge-pre-deploy-check/scripts/check_links.py [repo-root]

Categories:
  SKIP   — archive.org image junk, data: URIs, Google Drive local paths,
            PROJECT-PHASES/RECAP placeholders, kojo image files
  WARN   — pre-Phase-20 flat-file names (NN-slug-kn, NN-slug-en etc.)
            that work via Jekyll redirect_from — stale but low priority
  ERROR  — genuine broken links; exit code 1 if any present
"""
import re, os, sys, subprocess
from pathlib import Path
from collections import defaultdict

# ── Repo root detection ───────────────────────────────────────────────────────
if len(sys.argv) > 1:
    REPO = Path(sys.argv[1]).resolve()
else:
    try:
        REPO = Path(subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.DEVNULL
        ).decode().strip())
    except Exception:
        REPO = Path.cwd()

SRC = REPO / 'src' / 'main' / 'md'
LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]{1,300})\)')

# ── Patterns to always skip ───────────────────────────────────────────────────
ARCHIVE_JUNK_RE = re.compile(
    r'Full%20text|archive\.org|0\.gif\?kind=|'
    r'widgetOL|americana\.jpg|internetarcade|clevelandart|etree\.jpg|librivox|'
    r'consolelivingroom|metropolitanmuseum|tv\.jpg|911\.jpg'
)
# Pre-Phase-20 flat filenames like ./NN-slug-kn, ./NN-slug-en, ./NN-slug-blog etc.
OLD_FLAT_RE = re.compile(
    r'\.?/?\d{2}-[a-zA-Z].*-(?:kn|en|eke|blog|djvu|website|claude-prompt|kn-eke)$'
)
# Template/documentation placeholders in PROJECT-PHASES.md etc.
PLACEHOLDER_RE = re.compile(
    r'^(?:ch[0-9]+|en|kn-eke|kn|URL|book\.md|'
    r'\./SLUG-[a-z-]+|'
    r'\./book-(?:en|kn)|'
    r'[a-z-]+#\.\.\.|'
    r'kn#adhyAya-N|'
    r'kn-eke\.md#anchor)$'
)
# Kojo image refs (embedded in link syntax with title strings)
KOJO_IMAGE_RE = re.compile(r'\.(png|jpg|gif|svg|webp)(\s+"[^"]*")?$', re.IGNORECASE)


def classify(src_path: Path, href: str) -> str:
    """Return 'skip', 'warn', or 'error'."""
    if (href.startswith('http') or href.startswith('#') or
            href.startswith('mailto:') or href.startswith('data:') or
            len(href) > 300):
        return 'skip'
    if ARCHIVE_JUNK_RE.search(href):
        return 'skip'
    if 'Library/CloudStorage' in href or 'GoogleDrive' in href:
        return 'skip'   # local personal PDF files — expected missing
    if PLACEHOLDER_RE.match(href.split('#')[0].strip()):
        return 'skip'
    if 'PROJECT-PHASES' in str(src_path) or 'PROJECT-RECAP' in str(src_path):
        return 'skip'
    if KOJO_IMAGE_RE.search(href):
        return 'skip'   # kojo/ image refs not tracked in git
    # Known permanent structural stubs — referenced but never created
    KNOWN_MISSING = {'Books-Top', 'Books-Top.md', 'Schwa', 'Schwa.md'}
    if href.split('#')[0].strip().split('/')[-1] in KNOWN_MISSING:
        return 'skip'
    if OLD_FLAT_RE.search(href.split('#')[0].strip()):
        return 'warn'   # pre-Phase-20 flat name
    return 'error'


# ── Book-dir-aware resolver ───────────────────────────────────────────────────
# Build a lookup of NN → actual dir name for all book dirs
_DNSBHAT_DIR = SRC / 'kannada' / 'dnsbhat'
BOOK_DIRS: dict[str, Path] = {}   # "08" → Path("08-kannaDakke-...")
if _DNSBHAT_DIR.exists():
    for d in _DNSBHAT_DIR.iterdir():
        if d.is_dir() and re.match(r'^\d{2}-', d.name):
            num = d.name[:2]
            BOOK_DIRS[num] = d


def target_exists(src_path: Path, href: str) -> bool:
    target = href.split('#')[0].strip()
    if not target:
        return True  # anchor-only link

    resolved = (src_path.parent / target).resolve()

    # Direct checks
    if (resolved.exists() or
            resolved.with_suffix('.md').exists() or
            (resolved / 'README.md').exists() or
            (resolved / 'index.md').exists() or
            (resolved / 'full.md').exists() or
            (resolved / 'book').exists() or
            (resolved / 'youtube').exists()):
        return True

    # Book-number fuzzy match: ../NN-anything/ → check if NN dir exists under dnsbhat
    # Handles case-mismatch slugs where the dir DOES exist under a different casing
    m = re.search(r'(?:^|/)(\d{2})-[a-zA-Z]', target)
    if m:
        num = m.group(1)
        if num in BOOK_DIRS:
            return True   # a book with that number exists

    return False


# ── Scan all .md files ────────────────────────────────────────────────────────
errors_by_file   = defaultdict(list)
warnings_by_file = defaultdict(list)
ok_count = 0
skipped = 0

for md_file in sorted(SRC.rglob('*.md')):
    try:
        text = md_file.read_text(encoding='utf-8', errors='replace')
    except Exception:
        continue
    for m in LINK_RE.finditer(text):
        href = m.group(2)
        level = classify(md_file, href)
        if level == 'skip':
            skipped += 1
            continue
        if target_exists(md_file, href):
            ok_count += 1
            continue
        rel = str(md_file.relative_to(REPO))
        if level == 'warn':
            warnings_by_file[rel].append(href)
        else:
            errors_by_file[rel].append(href)

# ── Report ────────────────────────────────────────────────────────────────────
total_errors   = sum(len(v) for v in errors_by_file.values())
total_warnings = sum(len(v) for v in warnings_by_file.values())

print(f"\nettuge cross-link check  ({SRC})")
print('=' * 60)

if errors_by_file:
    print(f"\n✗ ERRORS ({total_errors} broken links in {len(errors_by_file)} files)\n")
    for f in sorted(errors_by_file):
        print(f"  {f}")
        for href in errors_by_file[f]:
            print(f"    → {href}")

if warnings_by_file:
    print(f"\n⚠  WARNINGS ({total_warnings} stale links in {len(warnings_by_file)} files)")
    print("   (pre-Phase-20 flat names — work via redirect_from, low priority)\n")
    for f in sorted(warnings_by_file):
        print(f"  {f}")
        for href in warnings_by_file[f]:
            print(f"    → {href}")

print('=' * 60)
print(f"  {ok_count} OK  |  {total_warnings} warnings  |  {total_errors} errors")

if total_errors:
    print("\n  ❌ Fix errors before deploying.")
    sys.exit(1)
elif total_warnings:
    print("\n  ⚠  Warnings present — low priority (stale pre-Phase-20 links).")
else:
    print("\n  ✅ All links OK.")
