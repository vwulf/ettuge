"""
Regenerates docs/claude-project-instructions.md (short index) and
docs/skills/01-*.md … docs/skills/06-*.md (per-skill + context files).

Split structure:
  01-word-coiner.md          ellara-kannada-word-coiner skill
  02-morphology.md           kannada-morphology skill
  03-book-summarizer.md      dns-bhat-book-summarizer skill
  04-transcript-summarizer.md dns-bhat-transcript-summarizer skill
  05-ocr-cleaner.md          kannada-ocr-cleaner skill
  06-agents-and-context.md   agents + all CLAUDE.md repo context

claude-project-instructions.md  short index with per-skill fetch URLs

Run from any directory: python3 regen_instructions.py
"""
import os, re

REPO = "/Users/vishwas/code/ettuge"
skills_dir = f"{REPO}/.claude/skills"
agents_dir = f"{REPO}/.claude/agents"
claude_mds = [
    (f"{REPO}/CLAUDE.md",                                              "Root CLAUDE.md"),
    (f"{REPO}/.claude/CLAUDE.md",                                      ".claude/CLAUDE.md — Automation Context"),
    (f"{REPO}/src/main/md/kannada/CLAUDE.md",                          "Kannada Directory CLAUDE.md"),
    (f"{REPO}/src/main/md/Books/CLAUDE.md",                            "Books Directory CLAUDE.md"),
    (f"{REPO}/src/main/md/self-reflection/CLAUDE.md",                  "Self-Reflection CLAUDE.md"),
    (f"{REPO}/src/main/haskell/CLAUDE.md",                             "Haskell Directory CLAUDE.md"),
    (f"{REPO}/src/main/python/CLAUDE.md",                              "Python Directory CLAUDE.md"),
]
out_dir   = f"{REPO}/docs"
skills_out = f"{REPO}/docs/skills"
index_path = f"{REPO}/docs/claude-project-instructions.md"
BASE_URL   = "https://raw.githubusercontent.com/vwulf/ettuge/master/docs"

skill_order = [
    ("ellara-kannada-word-coiner",      "01-word-coiner.md",           "Coin native Dravidian Kannada words using DNS Bhat's Ellara methodology"),
    ("kannada-morphology",              "02-morphology.md",            "Generate Kannada morphological forms: case, conjugation, suffixes"),
    ("dns-bhat-book-summarizer",        "03-book-summarizer.md",       "Summarize DNS Bhat books (OCR text): kn.md, en.md, kn-eke.md, claude-prompt"),
    ("dns-bhat-transcript-summarizer",  "04-transcript-summarizer.md", "Summarize DNS Bhat YouTube lecture series (books 01–13, transcript-only)"),
    ("kannada-ocr-cleaner",             "05-ocr-cleaner.md",           "Audit and fix OCR artefacts from Nudi/Baraha/ISM legacy font scans"),
]

os.makedirs(skills_out, exist_ok=True)

def strip_frontmatter(text):
    return re.sub(r'^---\n.*?---\n', '', text, flags=re.DOTALL)

# ── Write per-skill files ──────────────────────────────────────────────────────
print("Writing skill files:")
for skill_slug, filename, description in skill_order:
    skill_path = os.path.join(skills_dir, skill_slug, "SKILL.md")
    if not os.path.exists(skill_path):
        print(f"  MISSING: {skill_path}")
        continue
    text = strip_frontmatter(open(skill_path, encoding="utf-8").read())
    header = f"# Skill: {skill_slug}\n\n_{description}_\n\n---\n\n"
    content = header + text.strip() + "\n"
    out_path = os.path.join(skills_out, filename)
    open(out_path, "w", encoding="utf-8").write(content)
    chars = len(content)
    status = "✅" if chars < 200000 else "❌ TOO LARGE"
    print(f"  {filename}: {chars:,} chars {status}")

# ── Write agents + context file ────────────────────────────────────────────────
ctx_parts = ["# Agents and Repository Context\n\n"]

ctx_parts.append("## AGENTS\n\n")
for fname in sorted(os.listdir(agents_dir)):
    if fname.endswith(".md"):
        text = strip_frontmatter(open(os.path.join(agents_dir, fname), encoding="utf-8").read())
        ctx_parts.append(f"### Agent: {fname[:-3]}\n\n{text.strip()}\n\n")

ctx_parts.append("---\n\n## REPOSITORY CONTEXT (CLAUDE.md files)\n\n")
for path, label in claude_mds:
    if os.path.exists(path):
        text = open(path, encoding="utf-8").read()
        ctx_parts.append(f"### {label}\n\n{text.strip()}\n\n")

context_content = "\n".join(ctx_parts)
ctx_path = os.path.join(skills_out, "06-agents-and-context.md")
open(ctx_path, "w", encoding="utf-8").write(context_content)
chars = len(context_content)
status = "✅" if chars < 200000 else "❌ TOO LARGE"
print(f"  06-agents-and-context.md: {chars:,} chars {status}")

# ── Write index file ───────────────────────────────────────────────────────────
rows = []
for skill_slug, filename, description in skill_order:
    url = f"{BASE_URL}/skills/{filename}"
    rows.append(f"| `{skill_slug}` | {description} | [`fetch`]({url}) |")
ctx_url   = f"{BASE_URL}/skills/06-agents-and-context.md"
p1_url    = f"{BASE_URL}/claude-book-primers-1.md"
p2_url    = f"{BASE_URL}/claude-book-primers-2.md"

index_content = f"""# Ettuge Kannada Linguistics — Claude Project Instructions

This Project is for working with DNS Bhat Kannada linguistics books in the
[ettuge](https://github.com/vwulf/ettuge) repository: coining native Kannada
words, Eke romanisation, morphology, OCR cleanup, and book summarization.

**How to use:** Each skill is a separate file. When you need a skill, fetch
its URL below. The agents-and-context file has repository structure and all
CLAUDE.md files. Book primers have per-book reference data.

---

## Skills

| Skill | Purpose | File |
|-------|---------|------|
{chr(10).join(rows)}

---

## Agents and Repository Context

Agents, CLAUDE.md files, and repository conventions:
[`{BASE_URL}/skills/06-agents-and-context.md`]({ctx_url})

---

## Book Primers (per-book reference data)

| File | Books | URL |
|------|-------|-----|
| `claude-book-primers-1.md` | 01–25 | [`fetch`]({p1_url}) |
| `claude-book-primers-2.md` | 27–33 | [`fetch`]({p2_url}) |

---

## Quick Trigger Guide

| User says… | Fetch skill file |
|-----------|-----------------|
| "native Kannada word for X", "Ellara version of", "no Sanskrit", "coin a word" | `01-word-coiner.md` |
| "conjugate", "case form", "dative of", "suffix for", "morphological form" | `02-morphology.md` |
| "summarize book NN", "create English summary", "generate Eke", "create claude-prompt" | `03-book-summarizer.md` |
| "summarize transcript book NN", "YouTube lectures", books 01–13 | `04-transcript-summarizer.md` |
| "OCR errors", "garbled Kannada", "arka-ottu", "Nudi artefact", "fix legacy font" | `05-ocr-cleaner.md` |
"""

open(index_path, "w", encoding="utf-8").write(index_content)
chars = len(index_content)
status = "✅ OK" if chars < 200000 else f"❌ TOO LARGE"
print(f"\nclaude-project-instructions.md (index): {chars:,} chars — {status}")
