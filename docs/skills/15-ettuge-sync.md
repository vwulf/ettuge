# Ettuge Sync

Keeps all Claude context files current after a phase of work in the ettuge repository.
Files that matter to users who access the project from claude.ai (phone/web):

**Index (paste into claude.ai Project Instructions):**
- `docs/claude-project-instructions.md` — short index with per-skill fetch URLs (≤5k chars)

**Skills (fetched on demand — each under 25k chars):**
- `docs/skills/01-word-coiner.md` — ellara-kannada-word-coiner skill
- `docs/skills/02-morphology.md` — kannada-morphology skill
- `docs/skills/03-book-summarizer.md` — dns-bhat-book-summarizer skill
- `docs/skills/04-transcript-summarizer.md` — dns-bhat-transcript-summarizer skill
- `docs/skills/05-ocr-cleaner.md` — kannada-ocr-cleaner skill
- `docs/skills/06-agents-and-context.md` — agents + all CLAUDE.md repo context (~37k chars)

**Book primers (fetched on demand — each under 200k chars):**
- `docs/claude-book-primers-1.md` — books 01–25
- `docs/claude-book-primers-2.md` — books 27–33

Regeneration scripts live in `scripts/` alongside this file — run them with python3, don't rewrite them inline.

---

## Step 1 — Assess what changed

Ask the user (or infer from context): which of these changed in the latest phase?
- OCR cleanup / Nudi artefacts fixed
- New `*-kn.md` structured files created
- New or updated `*-claude-prompt.md` files
- CLAUDE.md learnings (new conventions, tools, workflow discoveries)
- New books added (new claude-prompt, README, or kn.md)
- Skill updates (SKILL.md files edited)

Then run the staleness check to find which book primers lag behind their kn.md:

```bash
cd /Users/vishwas/code/ettuge
for b in $(ls src/main/md/kannada/dnsbhat/ | grep '^[0-9]' | cut -d- -f1 | sort -n); do
  dir=$(ls -d src/main/md/kannada/dnsbhat/${b}-* 2>/dev/null | head -1)
  [ -z "$dir" ] && continue
  prompt=$(ls "$dir"/*-claude-prompt.md 2>/dev/null | head -1)
  kn=$(ls "$dir"/*-kn.md 2>/dev/null | head -1)
  [ -z "$prompt" ] || [ -z "$kn" ] && continue
  prompt_date=$(git log --format="%ci" -1 -- "$prompt")
  kn_date=$(git log --format="%ci" -1 -- "$kn")
  [[ "$kn_date" > "$prompt_date" ]] && echo "STALE: Book $b — kn.md newer than claude-prompt"
done
```

Also check recent git log to spot any other modified files not yet reflected in the docs:
```bash
git log --oneline -15
```

---

## Step 2 — Update CLAUDE.md files (if new learnings)

Edit only the CLAUDE.md files relevant to what changed. The three most likely to need updates:
- `CLAUDE.md` (root) — project overview, active development status, new phase milestones
- `.claude/CLAUDE.md` — automation context, skill table, OCR pipeline conventions
- `src/main/md/kannada/CLAUDE.md` — Eke rules, dnsbhat pipeline, book conventions

**Rules:**
- Preserve all existing content — append new sections or update specific items only
- For new phase milestones, update the "Current Status" section with a one-line summary
- For new conventions (quotes, anchors, markers), add to the relevant convention table
- For new skills, add a row to the skills table in `.claude/CLAUDE.md`

---

## Step 3 — Update stale claude-prompt.md files

For each book flagged as stale in Step 1, append a new numbered item to the end of its
`## INSTRUCTIONS FOR ANSWERING QUESTIONS` section. The item should document:

1. Which `*-kn.md` file now exists and what it contains (TOC, anchors, line count)
2. Citation quote convention: curly single quotes `'word'` (U+2018/U+2019) in kn.md and kn-eke.md
3. Whether the book uses *hosa baraha* (simplified spelling) or standard orthography
4. Any book-specific Phase fixes (e.g., page-split rejoined, 3-pass cleanup, vol1/vol2 split)
5. The `u^` marker if relevant (book 17 and Havyaka-related books)

Before writing, read the actual kn.md to confirm anchor names and structure — don't assume.

Example item format (adapt per book):
```
N. **Repository source (Phase 18):** A clean structured Kannada source file
`NN-slug-kn.md` is available with a ಪರಿವಿಡಿ TOC and `<a id="adhyAya-N">` chapter
anchors. The Eke file `NN-slug-kn-eke.md` mirrors the same structure. Citation
marks standardised to curly single quotes `'word'` (U+2018/U+2019). This book uses
*hosa baraha* spelling: ಭ→ಬ, ಧ→ದ, ಷ→ಸ in the source text.
```

---

## Step 4a — Sync docs/ from src/

The `docs/dnsbhat/` directory is what GitHub Pages serves. All canonical edits go to
`src/main/md/kannada/dnsbhat/`. After any OCR cleanup, kn.md edits, or phase work,
run the sync script to push changes to docs/ while preserving Jekyll navigation front matter:

```bash
python3 /Users/vishwas/code/ettuge/.claude/skills/ettuge-sync/scripts/sync_docs.py
```

This preserves `title`, `parent`, `nav_order`, `layout` from the existing docs/ front matter
and replaces all content with the src/ version.

---

## Step 4b — Copy skills globally

```bash
cp -r /Users/vishwas/code/ettuge/.claude/skills /Users/vishwas/.claude/
cp -r /Users/vishwas/code/ettuge/.claude/agents /Users/vishwas/.claude/
cp -r /Users/vishwas/code/ettuge/.claude/commands /Users/vishwas/.claude/
```

This makes all skills available in every Claude Code session, not just in the ettuge directory.

---

## Step 5 — Regenerate docs files

```bash
python3 /Users/vishwas/code/ettuge/.claude/skills/ettuge-sync/scripts/regen_instructions.py
python3 /Users/vishwas/code/ettuge/.claude/skills/ettuge-sync/scripts/regen_primers.py
```

`regen_instructions.py` generates eight files:
- `docs/claude-project-instructions.md` — short index (~3k chars)
- `docs/skills/01-word-coiner.md` through `docs/skills/05-ocr-cleaner.md` — one skill each
- `docs/skills/06-agents-and-context.md` — agents + CLAUDE.mds (~37k chars)

`regen_primers.py` generates two files:
- `docs/claude-book-primers-1.md` — books 01–25 (≤200k chars)
- `docs/claude-book-primers-2.md` — books 27–33 (≤200k chars)

Verify all skill files are under 200,000 chars and primers are under 200,000 chars. If primers-1
overflows, the greedy split auto-adjusts — check which books moved to primers-2 and update
the headers in both files to reflect the new split.

---

## Step 6 — Commit and push

Stage all changed files and commit with a descriptive message:

```bash
cd /Users/vishwas/code/ettuge
git add CLAUDE.md .claude/CLAUDE.md src/main/md/kannada/CLAUDE.md
git add src/main/md/kannada/dnsbhat/**/*-claude-prompt.md
git add docs/claude-project-instructions.md docs/skills/
git add docs/claude-book-primers-1.md docs/claude-book-primers-2.md
git add .claude/skills/
git status  # confirm staged files look right before committing
git commit -m "docs(sync): update Claude context files — Phase N

- [bullet: what CLAUDE.md files changed and why]
- [bullet: which book primers updated and what was added]
- [bullet: regenerated docs/ files with new sizes]

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push origin master
```

---

## Step 7 — Report to user

Print a summary table so the user knows what changed:

| File | Action | Size |
|------|--------|------|
| `docs/claude-project-instructions.md` | regenerated | Xk chars |
| `docs/claude-book-primers-1.md` | regenerated | Xk chars |
| `docs/claude-book-primers-2.md` | regenerated | Xk chars |
| `NN-slug-claude-prompt.md` × N | updated (item N added) | — |
| `CLAUDE.md` × M | updated | — |

Also remind the user: to update their claude.ai Project Instructions, paste ONLY the new
index file (it now fits in one fetch — ~3k chars):
- `https://raw.githubusercontent.com/vwulf/ettuge/master/docs/claude-project-instructions.md`

The per-skill files and book primers are fetched on demand via the URLs listed in the index;
they do NOT need to be pasted into Project Instructions.

---

## Key Conventions (reference — do not change these without user confirmation)

| Convention | Value |
|------------|-------|
| Citation quotes in kn.md / kn-eke.md | Curly single quotes `'word'` U+2018 open, U+2019 close |
| Unrounded-u marker in kn-eke.md | `u^` = ಉ್ (Havyaka phoneme) — do not alter |
| Raw OCR archive | `*-book.md` — never edit |
| Structured source | `*-kn.md` — editable; has TOC + `<a id="adhyAya-N">` anchors |
| Chapter anchor format | `<a id="adhyAya-N">` at each chapter heading |
| Section anchor format | `<a id="sec-N-M">` at subsections (where completed) |
| Hosa baraha books | 03, 07, 17, 27, 28, 29 — aspirated letters suppressed |
| Standard orthography | Book 25 — aspirated letters written as-is |
| Claude.ai per-file char limit | 200,000 characters |
| Global skill path | `~/.claude/skills/`, `~/.claude/agents/`, `~/.claude/commands/` |
