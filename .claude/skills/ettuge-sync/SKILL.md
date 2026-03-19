---
name: ettuge-sync
description: >
  Syncs all Claude context files in the ettuge Kannada linguistics repository after
  any phase of work. Use this skill whenever the user says: "sync Claude docs",
  "ettuge sync", "update project instructions", "update skills and claude.mds",
  "sync primers", "regenerate primers", "rebuild claude-project-instructions",
  "update Claude context", or any variation of "sync/update the ettuge docs/skills".
  Also invoke proactively at the end of any session where OCR cleanup, new kn.md
  files, new books, or CLAUDE.md learnings were added to the ettuge repository —
  even if the user hasn't explicitly asked to sync. The skill handles the full
  pipeline: assess staleness → update CLAUDE.md files → update stale book primers
  → copy skills globally → regenerate the three combined docs files → commit and push.
---

# Ettuge Sync

Keeps all Claude context files current after a phase of work in the ettuge repository.
Three outputs matter to users who access the project from claude.ai (phone/web):
- `docs/claude-project-instructions.md` — skills + CLAUDE.mds + per-book READMEs (≤200k chars)
- `docs/claude-book-primers-1.md` — deep book content, part 1 (≤200k chars)
- `docs/claude-book-primers-2.md` — deep book content, part 2 (≤200k chars)

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

## Step 4 — Copy skills globally

```bash
cp -r /Users/vishwas/code/ettuge/.claude/skills /Users/vishwas/.claude/
cp -r /Users/vishwas/code/ettuge/.claude/agents /Users/vishwas/.claude/
cp -r /Users/vishwas/code/ettuge/.claude/commands /Users/vishwas/.claude/
```

This makes all skills available in every Claude Code session, not just in the ettuge directory.

---

## Step 5 — Regenerate the three docs files

```bash
python3 /Users/vishwas/code/ettuge/.claude/skills/ettuge-sync/scripts/regen_instructions.py
python3 /Users/vishwas/code/ettuge/.claude/skills/ettuge-sync/scripts/regen_primers.py
```

Verify all three output files are under 200,000 chars (scripts print status). If primers-1
overflows, the greedy split auto-adjusts — check which books moved to primers-2 and update
the headers in both files to reflect the new split.

---

## Step 6 — Commit and push

Stage all changed files and commit with a descriptive message:

```bash
cd /Users/vishwas/code/ettuge
git add CLAUDE.md .claude/CLAUDE.md src/main/md/kannada/CLAUDE.md
git add src/main/md/kannada/dnsbhat/**/*-claude-prompt.md
git add docs/claude-project-instructions.md docs/claude-book-primers-1.md docs/claude-book-primers-2.md
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

Also remind the user: to update their claude.ai Projects, paste the new content from the
raw GitHub URLs:
- `https://raw.githubusercontent.com/vwulf/ettuge/master/docs/claude-project-instructions.md`
- `https://raw.githubusercontent.com/vwulf/ettuge/master/docs/claude-book-primers-1.md`
- `https://raw.githubusercontent.com/vwulf/ettuge/master/docs/claude-book-primers-2.md`

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
