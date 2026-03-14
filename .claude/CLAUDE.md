# ettuge — Claude Automation Context

This file documents the `.claude/` automation layer for the ettuge repository.

## Available Skills

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `ellara-kannada-word-coiner` | "native Kannada word for X", "DNS Bhat style", "no Sanskrit", "coin a word", "Ellara version of" | Coins native Dravidian words using DNS Bhat methodology |
| `kannada-morphology` | "Kannada suffix for", "conjugate this verb", "case form of", "dative of", "verbal noun chain" | Generates morphological forms using Bhat's grammar framework |
| `dns-bhat-book-summarizer` | "summarize book NN", "create English summary", "generate Eke", "create -en.md", "create -kn-eke.md", "create claude-prompt for book", "add paragraph breaks", "structure book NN" | Produces README.md + kn.md (paragraphs + anchors) + en.md + kn-eke.md for DNS Bhat books with OCR text (books 14–29) |
| `dns-bhat-transcript-summarizer` | "summarize transcript book NN", "summarize YouTube lectures", "create English summary from transcripts", "generate Eke for lectures", "books 01–13" | Produces en.md + kn-eke.md for YouTube-only DNS Bhat lecture series (books 01–13, no OCR text) from cleaned transcript .md files |

## Available Agents

| Agent | File | Purpose |
|-------|------|---------|
| `ellara-vocab-builder` | `agents/ellara-vocab-builder.md` | Scrapes Honalu.net → classifies etymology → builds dataset |
| `technical-term-coiner` | `agents/technical-term-coiner.md` | Batch English→native Kannada glossary generation |

## Available Commands

| Command | Purpose |
|---------|---------|
| `/coin-word` | Quick word coining via ellara-kannada-word-coiner skill |

## Eke Romanisation — Canonical Rules (must not be violated)

Eke is the romanisation used in all `-kn-eke.md` files. Full spec: `src/main/md/kannada/Eke.md`. Quick reference: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`.

**Four rules that have historically caused systematic LLM errors:**

| Rule | Wrong form | Correct Eke | Notes |
|------|-----------|-------------|-------|
| Anusvara ಂ | `M` (HK) | Assimilated nasal+C: `nk ng nc nT nD nt nd mp mb ms my mv` | **Never standalone M** |
| N (retroflex ಣ) | `liNga`, `tuNDu` | `linga`, `tunDu` | N = exclusively ಣ; never anusvara before stop consonants |
| ರ vs ಱ | `vaRNa`, `sRiSTi` | `varNa`, `sxSTi` | Lowercase `r` = ರ always; `R` = exclusively rare ಱ |
| Vocalic ṛ ಋ/ೃ | `samskrita`, `sriSTi`, `kRi`→`kri` | `samskxta`, `sxSTi`, `kx` | `x` = ಋ/ೃ (short); `X` = ೠ/ೄ (long, rare) |

**Safe / do not change:** `kriyA`, `krutaka`, `krulling` — these use genuine consonant ರ + ಉ/ಇ, not vocalic ṛ.

---

## Key Reference Files in Repo

| File | Purpose |
|------|---------|
| `src/main/md/kannada/Eke.md` | Full Eke romanization spec (153KB) — do not edit casually |
| `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md` | Eke quick-reference (vowels, consonants, anusvara, aspirates) |
| `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md` | Complete DNS Bhat word formation reference |
| `src/main/md/kannada/dnsbhat/dns-bhat-analysis.md` | Analysis of 13 DNS Bhat transcript books + Book 14 summary |
| `src/main/md/kannada/dnsbhat/14-nijakku-halegannada-vyakarana-entahadu/` | Book 14: Old Kannada grammar vs Sanskrit — full text + English translation (added Mar 2026) |
| `src/main/md/kannada/dnsbhat/15-inglish-kannada-padanerake/15-inglish-kannada-padanerake-claude-prompt.md` | Book 15: English→Kannada dictionary patterns — 6-step decision tree, 11 domain cluster tables, 100 curated word pairs (added Mar 2026) |
| `src/main/claude/kannada/` | Prior AI session transcripts (session0–5.md) |
