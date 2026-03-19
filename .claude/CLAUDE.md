# ettuge — Claude Automation Context

This file documents the `.claude/` automation layer for the ettuge repository.

## Available Skills

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `ellara-kannada-word-coiner` | "native Kannada word for X", "DNS Bhat style", "no Sanskrit", "coin a word", "Ellara version of" | Coins native Dravidian words using DNS Bhat methodology |
| `kannada-morphology` | "Kannada suffix for", "conjugate this verb", "case form of", "dative of", "verbal noun chain" | Generates morphological forms using Bhat's grammar framework |
| `dns-bhat-book-summarizer` | "summarize book NN", "create English summary", "generate Eke", "create -en.md", "create -kn-eke.md", "create claude-prompt for book", "add paragraph breaks", "structure book NN" | Produces README.md + kn.md (paragraphs + anchors) + en.md + kn-eke.md for DNS Bhat books with OCR text (books 14–29) |
| `dns-bhat-transcript-summarizer` | "summarize transcript book NN", "summarize YouTube lectures", "create English summary from transcripts", "generate Eke for lectures", "books 01–13" | Produces en.md + kn-eke.md for YouTube-only DNS Bhat lecture series (books 01–13, no OCR text) from cleaned transcript .md files |
| `kannada-ocr-cleaner` | "OCR errors in Kannada", "garbled Kannada", "arka-ottu", "fix legacy font", "ರ್ wrong in OCR", "Nudi artefact", "running header in body", "page-break fragment", garbled Latin chars (É Å À ï õ) mixed with Kannada | Audits and fixes OCR artefacts from Nudi/Baraha/ISM legacy font encoding; handles arka-ottu reversals, anusvara garbling, embedded running headers, page-break fragments, oo-matra errors |

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

## DNS Bhat Book OCR Pipeline — Conventions

### File roles (do not conflate)
| File | Role | Editable? |
|------|------|-----------|
| `*-book.md` / `*-blog.md` | Raw OCR archive | NO — source of truth |
| `*-kn.md` | Structured Kannada source with TOC + anchors | YES |
| `*-kn-eke.md` | Eke romanisation of kn.md | YES (regenerate after kn.md changes) |
| `*-en.md` | English chapter summary | YES |
| `*-claude-prompt.md` | Condensed prompt context | YES |

### Citation quotes
DNS Bhat's typographic convention uses backtick as open-quote (`` `word' `` or ` ``word'' `). In kn.md and kn-eke.md, these are standardised to **curly single quotes** U+2018/U+2019: `'word'`. Never use backtick as open-quote — it creates Markdown code-span rendering bugs.

Close char varies by book (from original typography):
- Books 07 vol1+vol2, 25, 28: close was ASCII apostrophe U+0027 → normalised to U+2019
- Book 17: close was U+2019 → kept as U+2019

### Unrounded-u `u^`
In kn-eke.md files, `u^` marks ಉ್ (unrounded-u vowel) — a Havyaka phoneme. This marker is intentional and must NOT be treated as a citation mark or changed to `u'`.

### Nudi/WX encoding artefacts
Books typeset in legacy Nudi font have OCR'd as garbled Latin (É Å ÀÉ ÂÐ etc.). The fix pipeline:
1. Map each Latin glyph to its Nudi→Unicode equivalent using the Nudi codepoint chart
2. Check arka-ottu reversals: Nudi places the ರ್ virama *before* the base consonant; Unicode places it *after*. Pattern: `ರ್X` in Nudi OCR → `Xರ್` in Unicode.
3. Fix oo-matra (ೋ) which Nudi OCR renders as `oo` or `o ̄`
4. Remove per-page running headers (chapter titles repeated in body text)
5. Remove page-break fragments (isolated words/syllables at page boundaries)

### WX-encoded books (books 01–13 transcripts)
These were OCR'd via WX transliteration → Devanagari → Kannada pipeline. Key issue: column-break artifacts place each word/phrase on its own line with no blank line separator → renders as one flat paragraph in Markdown. Fix: detect short non-sentence-final lines and join with spaces. Requires PDF review.

### TOC structure
All kn.md files have a ಪರಿವಿಡಿ/ಒಳಪಿಡಿ table at the top linking to `<a id="adhyAya-N">` anchors. Deep section anchors (`sec-N-M`, `sub-N-M-K`) are pending for most books — see PROJECT-RECAP.md TBD list.

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
| `docs/dnsbhat/PROJECT-RECAP.md` | Full phased project history (Phases 1–17) — canonical record of all OCR cleanup decisions, quote conventions, Eke rules, and pending work |
| `docs/claude-project-instructions.md` | Combined skills + CLAUDE.md context for Claude.ai Projects (phone access) |
