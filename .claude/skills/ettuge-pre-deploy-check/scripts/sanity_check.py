#!/usr/bin/env python3
"""
ettuge pre-deploy sanity checker.
Run from the repo root: python3 .claude/skills/ettuge-pre-deploy-check/scripts/sanity_check.py
"""
import os, re, sys, ast

import subprocess
# Accept repo path as first arg, or detect via git, or fall back to cwd
if len(sys.argv) > 1:
    REPO = os.path.abspath(sys.argv[1])
else:
    try:
        REPO = subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        REPO = os.getcwd()
PAGES_YML  = os.path.join(REPO, '.github/workflows/pages.yml')
DOCS_CFG   = os.path.join(REPO, 'docs/_config.yml')
ROOT_CFG   = os.path.join(REPO, '_config.yml')
REFL_SRC   = os.path.join(REPO, 'src/main/md/self-reflection')
FP_SRC     = os.path.join(REPO, 'src/main/md')

errors   = []
warnings = []
passed   = []

def ok(msg):   passed.append(f"  ✓ {msg}")
def warn(msg): warnings.append(f"  ⚠ {msg}")
def fail(msg): errors.append(f"  ✗ {msg}")

# ── 1. Jekyll builds from docs/, not repo root ────────────────────────────────
with open(PAGES_YML) as f:
    yml = f.read()

if 'working-directory: docs' in yml:
    ok("Jekyll builds from docs/")
else:
    fail("pages.yml: missing 'working-directory: docs' — Jekyll may build from wrong directory")

# ── 2. docs/_config.yml is the real config ────────────────────────────────────
if not os.path.exists(DOCS_CFG):
    fail(f"docs/_config.yml not found — Jekyll has no config")
else:
    with open(DOCS_CFG) as f:
        doc_cfg = f.read()
    ok("docs/_config.yml exists")
    if 'search_enabled: true' in doc_cfg:
        fail("docs/_config.yml: search_enabled is true — will generate 35MB search-data.json")
    elif 'search_enabled: false' in doc_cfg:
        ok("docs/_config.yml: search_enabled is false")
    else:
        warn("docs/_config.yml: search_enabled not set (defaults to true)")

if os.path.exists(ROOT_CFG):
    with open(ROOT_CFG) as f:
        root_cfg = f.read()
    if 'search_enabled: true' in root_cfg:
        warn("root _config.yml has search_enabled:true — this file is UNUSED by Jekyll (builds from docs/) but may cause confusion")

# ── 3. Parse REFL_CATS from pages.yml ────────────────────────────────────────
refl_match = re.search(r'REFL_CATS\s*=\s*\[(.*?)\]', yml, re.DOTALL)
if not refl_match:
    fail("Could not find REFL_CATS in pages.yml")
    refl_cats = []
else:
    raw = '[' + refl_match.group(1) + ']'
    try:
        refl_cats = ast.literal_eval(raw)
        ok(f"REFL_CATS parsed: {len(refl_cats)} entries")
    except Exception as e:
        fail(f"REFL_CATS failed to parse: {e}")
        refl_cats = []

# ── 4. Every REFL_CATS file has a matching source file ───────────────────────
nav_orders = []
for fname, title, nav_order in refl_cats:
    # Source files are named 2026-02-25_{stem}.md
    stem = os.path.splitext(fname)[0]
    src = os.path.join(REFL_SRC, f'2026-02-25_{fname}')
    if not os.path.exists(src):
        # Try without date prefix (some files may not have it)
        src2 = os.path.join(REFL_SRC, fname)
        if os.path.exists(src2):
            ok(f"REFL '{title}': source found (no date prefix)")
        else:
            fail(f"REFL '{title}': source file not found — expected {src}")
    else:
        ok(f"REFL '{title}': source exists")

        # ── 5. Source file has at least <a id="ch1"> anchor ──────────────────
        with open(src) as f:
            content = f.read()
        if '<a id="ch1">' in content or '<a id="ch1"/>' in content:
            ok(f"REFL '{title}': has ch1 anchor")
        else:
            warn(f"REFL '{title}': no <a id=\"ch1\"> anchor — page won't be chapterized")

    # ── 6. No duplicate nav_order ─────────────────────────────────────────────
    if nav_order in nav_orders:
        fail(f"REFL_CATS: duplicate nav_order {nav_order} ('{title}')")
    else:
        nav_orders.append(nav_order)

# ── 7. Parse FP_ARTICLES similarly ───────────────────────────────────────────
fp_match = re.search(r'FP_ARTICLES\s*=\s*\[(.*?)\]', yml, re.DOTALL)
if fp_match:
    raw = '[' + fp_match.group(1) + ']'
    try:
        fp_articles = ast.literal_eval(raw)
        fp_nav = []
        for fname, title, nav_order in fp_articles:
            if nav_order in fp_nav:
                fail(f"FP_ARTICLES: duplicate nav_order {nav_order} ('{title}')")
            else:
                fp_nav.append(nav_order)
        ok(f"FP_ARTICLES parsed: {len(fp_articles)} entries, nav_orders unique")
    except Exception as e:
        warn(f"FP_ARTICLES could not be checked: {e}")

# ── 8. Python blocks in pages.yml are syntactically valid ────────────────────
import textwrap
py_blocks = re.findall(r"python3 - <<'PYEOF'\n(.*?)PYEOF", yml, re.DOTALL)
for i, block in enumerate(py_blocks):
    try:
        ast.parse(textwrap.dedent(block))
        ok(f"Python block {i+1}/{len(py_blocks)}: syntax valid")
    except SyntaxError as e:
        fail(f"Python block {i+1}/{len(py_blocks)}: syntax error — {e}")

# ── 9. instant.page loaded from CDN (not a blocking script) ──────────────────
head_custom = os.path.join(REPO, 'docs/_includes/head_custom.html')
if os.path.exists(head_custom):
    with open(head_custom) as f:
        hc = f.read()
    if 'type="module"' in hc:
        ok("head_custom.html: instant.page uses type=module (non-blocking)")
    elif '<script' in hc:
        warn("head_custom.html: <script> without type=module may block rendering")

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\nettuge pre-deploy sanity check")
print(f"{'='*50}")
for m in passed:   print(m)
for m in warnings: print(m)
for m in errors:   print(m)
print(f"{'='*50}")
print(f"  {len(passed)} passed  |  {len(warnings)} warnings  |  {len(errors)} errors")

if errors:
    print("\n  ❌ Fix errors before deploying.")
    sys.exit(1)
elif warnings:
    print("\n  ⚠  Warnings present — review before deploying.")
else:
    print("\n  ✅ All checks passed.")
