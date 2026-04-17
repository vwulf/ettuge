# ettuge Pre-Deploy Sanity Check

Run this before every `git push` on the ettuge repository.

## Step 1 — Run the script

```bash
cd /Users/vishwas/code/ettuge
python3 .claude/skills/ettuge-pre-deploy-check/scripts/sanity_check.py
```

Fix every ✗ error before proceeding. Review ⚠ warnings.

## Step 2 — Manual checks (read the diff)

Before committing, run `git diff --stat` and `git diff` and verify:

1. **Which _config.yml changed?**
   - Changes to `docs/_config.yml` → affects the live site ✓
   - Changes to root `_config.yml` → Jekyll IGNORES this file (builds from `docs/`) ✗
   - Rule: always edit `docs/_config.yml`, never the root one

2. **REFL_CATS / FP_ARTICLES changes?**
   - Every added entry must have a corresponding source file in `src/main/md/self-reflection/`
   - No duplicate nav_order values
   - Removed entries must not leave orphaned source files that CI would still copy

3. **New Reflection source files?**
   - Must have `<a id="ch1">` (and ch2, ch3…) anchors for chapterization to work
   - Must be listed in REFL_CATS in pages.yml

4. **pages.yml Python edits?**
   - Extract and `python3 -m py_compile` if you edited any Python block

## Step 3 — Confirm deploy target

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
