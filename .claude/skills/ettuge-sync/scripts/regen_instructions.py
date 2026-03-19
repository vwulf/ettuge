"""
Regenerates docs/claude-project-instructions.md from current source files.
Combines: all skills + agents + all 7 CLAUDE.md files + dnsbhat catalogue README + all per-book READMEs.
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
dnsbhat_base = f"{REPO}/src/main/md/kannada/dnsbhat"
out_path = f"{REPO}/docs/claude-project-instructions.md"

skill_order = [
    "ellara-kannada-word-coiner",
    "kannada-morphology",
    "dns-bhat-book-summarizer",
    "dns-bhat-transcript-summarizer",
    "kannada-ocr-cleaner",
]

parts = []
parts.append("""# Ettuge Kannada Linguistics — Claude Project Instructions

This Project is for working with DNS Bhat Kannada linguistics books in the [ettuge](https://github.com/vwulf/ettuge) repository: coining native Kannada words, Eke romanisation, morphology, OCR cleanup, and book summarization.

You have five specialised skill sets plus full repository context. Invoke the right skill automatically based on the user's request.

---
""")

for skill in skill_order:
    skill_path = os.path.join(skills_dir, skill, "SKILL.md")
    if os.path.exists(skill_path):
        text = open(skill_path).read()
        text = re.sub(r'^---\n.*?---\n', '', text, flags=re.DOTALL)
        parts.append(f"---\n\n## SKILL: {skill}\n\n{text.strip()}\n\n")

parts.append("---\n\n## AGENTS\n\n")
for fname in sorted(os.listdir(agents_dir)):
    if fname.endswith(".md"):
        text = open(os.path.join(agents_dir, fname)).read()
        text = re.sub(r'^---\n.*?---\n', '', text, flags=re.DOTALL)
        parts.append(f"### Agent: {fname[:-3]}\n\n{text.strip()}\n\n")

parts.append("---\n\n## REPOSITORY CONTEXT (CLAUDE.md files)\n\n")
for path, label in claude_mds:
    if os.path.exists(path):
        text = open(path).read()
        parts.append(f"### {label}\n\n{text.strip()}\n\n")

parts.append("---\n\n## DNS BHAT BOOK CATALOGUE\n\n")
catalogue_path = os.path.join(dnsbhat_base, "README.md")
if os.path.exists(catalogue_path):
    parts.append(open(catalogue_path).read().strip() + "\n\n")

parts.append("---\n\n## PER-BOOK REFERENCE\n\nEach section below describes one DNS Bhat book: its theme, available files, and where to start.\n\n")
book_dirs = sorted([
    d for d in os.listdir(dnsbhat_base)
    if os.path.isdir(os.path.join(dnsbhat_base, d)) and d[0].isdigit()
])
for book_dir in book_dirs:
    readme_path = os.path.join(dnsbhat_base, book_dir, "README.md")
    if os.path.exists(readme_path):
        text = open(readme_path).read().strip()
        parts.append(f"### Book {book_dir}\n\n{text}\n\n")

combined = "\n".join(parts)
open(out_path, "w").write(combined)
chars = len(combined)
status = "✅ OK" if chars < 200000 else f"❌ TOO LARGE ({chars - 200000:,} over limit)"
print(f"claude-project-instructions.md: {chars:,} chars — {status}")
