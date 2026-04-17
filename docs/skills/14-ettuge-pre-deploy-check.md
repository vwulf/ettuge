# ettuge Pre-Deploy Sanity Check

Run this before every `git push` on the ettuge repository.

## Step 1 — Config and CI checks

```bash
cd /Users/vishwas/code/ettuge
python3 .claude/skills/ettuge-pre-deploy-check/scripts/sanity_check.py
```

Fix every ✗ error before proceeding. Review ⚠ warnings.

## Step 2 — Cross-link check (NEW — catches 404s)

```bash
python3 .claude/skills/ettuge-pre-deploy-check/scripts/check_links.py
```

This scans all ~13,000 internal markdown links in `src/main/md/` and reports:
- **✗ ERRORS** — genuinely broken links; fix before pushing
- **⚠ WARNINGS** — stale pre-Phase-20 flat names (work via redirect_from, low priority)
- **✅ OK** — nothing to do

**Run this whenever you:**
- Add, rename, or restructure any book file or directory
- Edit cross-references in `en/summary.md`, `claude-prompt.md`, or `full.md` files
- Generate new chapter pages (ch0.md, ch1.md etc.)
- Fix any link — the fix itself might introduce a new break

## Step 3 — Manual diff review

Before committing, run `git diff --stat` and `git diff` and verify:

1. **Which _config.yml changed?**
   - Changes to `docs/_config.yml` → affects the live site ✓
   - Changes to root `_config.yml` → Jekyll IGNORES this file (builds from `docs/`) ✗

2. **REFL_CATS / FP_ARTICLES changes?**
   - Every added entry must have a corresponding source file in `src/main/md/self-reflection/`
   - No duplicate nav_order values

3. **New Reflection source files?**
   - Must have `<a id="ch1">` anchors for chapterization to work
   - Must be listed in REFL_CATS in pages.yml

4. **pages.yml Python edits?**
   - Extract and `python3 -m py_compile` if you edited any Python block

## Step 4 — Confirm deploy target

```bash
grep -n 'working-directory' /Users/vishwas/code/ettuge/.github/workflows/pages.yml
```

Should show `working-directory: docs` for the Jekyll build step.

## What each check catches

| Check | Past failure it prevents |
|-------|--------------------------|
| `docs/_config.yml` is the real config | Edited root `_config.yml` — search bar kept showing |
| `search_enabled: false` | 35MB search-data.json causing 10-second page loads |
| REFL_CATS source files exist | Deploying a broken sidebar link that 404s |
| No duplicate nav_order | Silent sidebar ordering bugs |
| `<a id="ch1">` anchors present | Chapterization silently skipped |
| Python syntax valid | CI fails at runtime, no pages regenerated |
| instant.page uses `type=module` | Blocking script in `<head>` slows every page |
| Cross-link check | Navigation links 404ing after book restructuring |

## Link Checker Details

The `check_links.py` script handles ~13,000 links across 33 books and resolves:
- **Book-number fuzzy matching**: `../08-.../ ` matches any dir starting with `08-`
- **Phase-20 taxonomy**: links from `youtube/en/` need 3 `../` levels to reach sibling books
- **Pre-Phase-20 flat names**: classified as WARN (not ERROR) since they work via redirect_from
- **Permanent stubs**: Books-Top, Schwa etc. are classified as SKIP (known missing)
- **Archive junk**: Internet Archive image URLs from OCR are skipped
- **Local Google Drive PDFs**: skipped (personal files, expected missing in CI)

