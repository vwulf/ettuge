# Agents and Repository Context


## AGENTS


### Agent: ellara-vocab-builder

# Agent: ellara-vocab-builder

## Purpose
Builds a native Kannada vocabulary dataset by scraping Honalu.net and Kannada Wiktionary, classifying word etymology (Dravidian vs Sanskrit), and storing results in Eke romanization.

## Pipeline

```
1. Scrape word list from Honalu.net
        ↓
2. Classify etymology (native Dravidian vs Sanskrit borrowing)
   Heuristics:
   - Sanskrit signals: aspirated consonants (kh/gh/th/dh/ph/bh), Sanskrit clusters (pr-/tr-/kr-), ಷ (Sha)
   - Dravidian signals: no aspirates, has ಳ/ಣ/ಡ/ಟ, Tamil cognate matches
        ↓
3. Transliterate to Eke romanization
   Rules: aspirates→plain, retroflexes uppercase (T/D/N/L), long vowels uppercase (A/I/U/E/O)
        ↓
4. Store as structured dataset (JSON or CSV)
   Schema: { word_kn, word_eke, etymology_class, source_url, confidence }
```

## Key Constraints
- Honalu.net may rate-limit — use delays between requests
- Prefer Wiktionary for etymology confirmation
- Flag uncertain classifications for human review
- Output must be compatible with `ellara-kannada-word-coiner` skill format

## Reference Files
- DNS Bhat word formation: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Eke rules: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`
- Analysis: `src/main/md/kannada/dnsbhat/dns-bhat-analysis.md`


### Agent: technical-term-coiner

# Agent: technical-term-coiner

## Purpose
Takes a list of English technical terms and coins native Dravidian Kannada equivalents using DNS Bhat's word formation methodology. Produces a structured glossary.

## Pipeline

```
1. Receive English term list
        ↓
2. For each term, apply the DNS Bhat word-generation algorithm:
   a. Check if native equivalent already exists (search Honalu/Wiktionary)
   b. Analyze English morphological structure (prefix/suffix/compound/standalone)
   c. Identify semantic core and role (agent/action/instrument/quality)
   d. Select strategy: suffix-derived > prefix+word > compound
   e. Select native Kannada root (avoid Sanskrit)
   f. Apply morphological rules + phonological allomorphy
   g. Verify: intelligible? established pattern? pronounceable?
        ↓
3. Add Eke romanization
        ↓
4. Cross-check against Honalu.net for existing usage
        ↓
5. Output structured glossary:
   { english, kannada_script, eke, breakdown, strategy_used, confidence, notes }
```

## Output Format
Markdown table + JSON file. The markdown is for human review; the JSON feeds downstream systems.

## Reference Files
- Full DNS Bhat system: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Skill to invoke: `.claude/skills/ellara-kannada-word-coiner/SKILL.md`
- Eke rules: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`


---

## REPOSITORY CONTEXT (CLAUDE.md files)


### Root CLAUDE.md

# CLAUDE.md — ettuge

This file provides guidance to Claude Code when working in this repository.

## Overview

Ettuge is a linguistic research project focused on native Kannada language preservation. It combines:
- Documentation of the **Eke** romanization system (designed by Vishwas, inspired by Hosabaraha and Harvard-Kyoto)
- Translation work using **DNS Bhat's native Kannada word formation methodology**
- YouTube transcript extraction and processing for linguistics research
- Functional programming examples in Haskell, Scala, and Kojo
- Personal reading catalog (Books)

**Repository:** https://github.com/vwulf/ettuge (public)

---

## Directory Structure

```
ettuge/
├── TRANSLATION_STATUS.md        # Detailed translation task status
├── TRANSLATION_SUMMARY.md       # Quick summary of active translation work
├── docs/                        # GitHub Pages output (Jekyll)
│   ├── dnsbhat/                 # Per-book HTML pages + PROJECT-RECAP.md
│   └── claude-project-instructions.md  # Combined skills for Claude.ai Projects
└── src/main/
    ├── claude/kannada/          # Claude AI session transcripts (session0-5.md)
    ├── md/
    │   ├── kannada/             # PRIMARY: Kannada linguistic work
    │   │   ├── Eke.md           # Main Eke specification (153KB)
    │   │   ├── Eke.kn.md        # Kannada translation (complete, DNS Bhat compliant)
    │   │   ├── Eke.eke.md       # Eke romanization of Eke.kn.md
    │   │   ├── brahmi-*.md      # Script history documentation
    │   │   ├── malatibhat_*.md  # Video references & analysis
    │   │   ├── dnsbhat/         # DNS Bhat word formation articles & prompts
    │   │   ├── transcripts/     # Raw YouTube transcripts (349+ files)
    │   │   ├── transcripts_cleaned/  # AI-cleaned transcripts (130+ files)
    │   │   └── sections/        # Extracted transcript sections
    │   ├── Books/               # Personal reading catalog
    │   │   ├── Books.md         # Index of influential books (by author, with summaries)
    │   │   ├── Books-Top.md     # Modern Library Top 100 novels list with summaries
    │   │   └── influential/     # Individual book files (Summary, Critical Takeaways, My Takeaways)
    │   ├── haskell/             # Haskell/FP documentation
    │   ├── kojo/                # Kojo programming articles
    │   ├── nihongo/             # Japanese language docs
    │   ├── physics/             # Unified field theory / Advaita philosophy (UniversalConsciousness.md)
    │   ├── pl/                  # Programming language theory
    │   └── self-reflection/     # Dated personal reflection documents (index.md + YYYY-MM-DD_topic.md)
    ├── haskell/                 # Haskell source files
    │   ├── euterpea/            # Music composition (rangapura.hs, twinkle.hs)
    │   └── quick/               # Quick Haskell project (Stack)
    ├── python/yt-transcript/    # YouTube transcript processing scripts
    ├── scala/                   # Scala scripts and Kojo files
    └── nu/                      # Nushell scripts
```

---

## Active Development

### Current Status (as of 2026-03-25, Phase 32)

All 33 DNS Bhat books have been catalogued; books 30–33 now have content files. Grammar section added with illustrated verb paradigm pages. CI chapter splitter generates paginated chapter pages for all books. Key milestones:

- **Phase 32 (2026-03-25):** Book 14 `raw.md` cleaned — 587 lines of Internet Archive HTML chrome (nav bars, SVG icons, banners) removed from top; content now starts cleanly at `# Full text of "..."`. Chapter splitter CI step added to `pages.yml`: walks all `docs/kannaDa/dnsbhat/*/book/*/full.md`, splits at `<a id="(?:ch|adhyAya-)(\d+)">` anchors, generates `ch0.md` (preamble + TOC + chapter nav) + `ch1.md`…`chN.md` per chapter. Sidebar CANDIDATES updated so `ch0.md` is the entry point (lightweight TOC index for slow connections). Chapter anchors added: Book 27 (5 `chN` aliases after `part-N`), Book 31 (19 `chN` before `## LETTER` headings A–W), Book 07 vol4 (`ch9` before `sec-9-1`, `ch10` before `sec-10-1`).
- **Phase 31 (2026-03-25):** PROJECT-RECAP.md TBD cleanup — 3 completed High-priority items removed (Deep TOC anchors Phase 19, Markdown headings Phase 18, word-per-line OCR artifact Phase 18); "Expand Eke home page description" done item removed.
- **Phase 30 (2026-03-25):** Books, FP/Haskell, and self-reflection sections published to GitHub Pages with full sidebar integration (L1 roots at nav_order 4/5/6).
- **Phase 29 (2026-03-25):** Grammar section added at `src/main/md/kannada/grammar/`. Three verb paradigm pairs: `iru-verb-paradigm.md` + `iru-illustrated.html`, `mADu-verb-paradigm.md` + `mADu-illustrated.html`, `illa-verb-paradigm.md` + `illa-illustrated.html`. Cross-navigation between all three illustrated pages (prev/next banners). Compound forms notes added (ಕೂಡಿಕೆ ರೂಪ: `mADihanu` = converb + emphatic `ಹನು`; `mADalAre` = purpose converb + defective aux `ಆರು`). Root redirect stubs at grammar folder index.
- **Phase 28 (2026-03-24):** ಕನ್nnaDa L1 sidebar root restructured: DNS Bhat/Eke/Grammar as L2; Books/Blog/YouTube/Stubs as L3 under DNS Bhat. Mixed-script `ಕನ್nnaDa` header text normalized (562 replacements). Eke motivation section rewritten: symbol complexity table (46 symbols vs Devanagari's 47), q/Q for vocalic ḷ/ḹ documented, `:` and `^` as dialect modifiers clarified. Script history Tamil-Brāhmī lineage clarified.
- **Phase 27 (2026-03-23):** Book 31 (*ಇಂಗ್ಲಿಶ್ ಪದಗಳಿಗೆ ಕನ್ನಡದ್ದೇ ಪದಗಳು*, 487pp Baraha A–Z dictionary) fully decoded. Cracked the three-range CID offset rule (≤96:+31, 97–114:+57, 115+:+61), resolved ±/¯/³ Baraha char ambiguities, and implemented `preprocess_baraha()` + `postprocess()` pipeline around wx_decode. Result: 12,121 entries, only 2 OCR-artifact garbled (down from 5,411 garbled + 495 partial). Batch decode script saved at `/tmp/decode_book31_batch.py`.
- **Phase 26 (2026-03-23):** Book 07 (*ಕನ್ನಡ ಬರಹದ ಸೊಲ್ಲರಿಮೆ*) Vols 3 and 4 fully processed. Generated from PDF via Baraha→Unicode OCR with Python cleanup script: vol3/kn/full.md (ch7–8, verbal arguments + alternations), vol3/eke/full.md, vol3/en/summary.md; vol4/kn/full.md (ch9–10, pronouns + demonstratives), vol4/eke/full.md, vol4/en/summary.md. Multi-volume index book/kn/full.md updated. All four syntax chapters now have full 3-file sets.
- **Phase 25 (2026-03-22):** Split Book 33 (*ಕನ್ನಡ ಸೊಲ್ಲರಿಮೆ*) out of Book 07's folder — the YouTube transcript was mis-shelved there. Added youtube/en/summary.md + claude-prompt.md for all 6 YouTube-only books (01, 06, 10, 11, 12, 13). All 33 books now have claude-prompt.md.
- **Phase 24 (2026-03-22):** Added books 30, 31, 32 from PDF extraction. Book 30 (382pp Nudi): full 4-file set (raw.md, full.md with 10-chapter TOC, en/summary.md, eke/full.md) via wx_decode.py. Book 31 (487pp Nudi, A–Z dictionary): book/kn/raw.md + book/en/summary.md; initial full.md had 5,411 garbled entries (now fixed in Phase 27). Book 32 (214pp clean English, John Benjamins): book/en/summary.md. claude-prompt.md created for all three. dnsbhat/README.md updated with collection stats (25→32 total books across sections A–L).
- **Phase 23 (2026-03-21):** Blog sidebar fallback fixed (Books 14, 18 now appear). Stubs sidebar category added — 16 YouTube placeholder files reclassified out of the YouTube sidebar. Books 02 and 03 YouTube transcripts enriched with link + 60-word excerpt cross-references to matching blog/book sections (Books 02: 10 Parts; Book 03: 33 of 55 Parts), using `#sec-N-M` anchors from Phase 19.
- **Phase 22 (2026-03-21):** YouTube transcript restructuring for all books 01–13: `## Part N` → `### Part N`, `<a id="part-N">` anchors, ~80-word paragraph breaks, garbage detection, ಪರಿವಿಡಿ TOC. Book 03 additionally restructured with 9-chapter grouping matching the book's chapter structure.
- **Phase 21 (2026-03-20):** GitHub Pages nested source-first sidebar (Books / Blog / YouTube / Stubs) generated via 6-pass Python script in CI. All 404s fixed after taxonomy migration.
- **Phase 20 (2026-03-20):** 4-level taxonomy migration — all 29 book dirs restructured to `book/kn/full.md`, `web/kn/raw.md`, `youtube/kn/full.md` etc. (129 git mv ops).
- **Phase 19 (2026-03-20):** Deep 3-level TOC with `<a id="sec-N-M">` and `<a id="sub-N-M-K">` anchors added to all books with kn.md (02, 03, 07-vol1, 07-vol2, 08, 14, 17, 25, 27, 28, 29). Section/subsection cross-links added: `[Eke →]` after every sec/sub anchor in kn.md; `[ಕನ್ನಡ →]` in kn-eke.md.
- **Phase 18 (2026-03-19):** Chapter/section headings converted to Markdown `##`/`###`/`####`. Book 28 deep TOC added. Book 03 subsection numbering corrected (1.6→1.5).
- **Earlier phases:** OCR cleanup (books 07, 08, 14, 17, 25, 27, 28, 29), Eke.md translation (complete), DNS Bhat book summarization pipeline established, transcript cleanup (349 videos).

Full history: `docs/dnsbhat/PROJECT-RECAP.md` (also served at https://vwulf.github.io/ettuge/dnsbhat/PROJECT-RECAP).

### DNS Bhat Methodology
All translation work must follow DNS Bhat's native Kannada word formation system:
- Reference: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Books: `src/main/md/kannada/dnsbhat/` — 32 book directories (01–32); see `dnsbhat/README.md` for the full annotated catalogue
- Analysis files: `dns-bhat-analysis.md`, `kannada-content-landscape.md`, `kannada-knowledge-gap-analysis.md`
- DNS Bhat prefers native (Dravidian) roots over Sanskrit. In Eke romanisation of his own books, aspirated forms ARE romanised as-is (bh, dh, kh etc.) because he uses Sanskrit loanwords — only *new coinages* avoid aspirates.

### DNS Bhat Book File Structure

Each book directory uses the Phase-20 4-level taxonomy (`source/lang/type.md`):
| Path pattern | Content |
|-------------|---------|
| `book/kn/raw.md` or `book/kn/full.md` | Structured Kannada source (do NOT use old `NN-slug-kn.md`) |
| `book/en/summary.md` | Chapter-wise English summary |
| `book/eke/full.md` | Eke romanisation |
| `web/kn/raw.md` | Blog/web Kannada source |
| `web/en/summary.md` | Blog English summary |
| `web/eke/full.md` | Blog Eke romanisation |
| `youtube/kn/full.md` | YouTube transcript (Kannada) |
| `youtube/en/summary.md` | YouTube English summary |
| `claude-prompt.md` | Condensed prompt context for Claude sessions |
| `README.md` | Book-level index (rendered on GitHub Pages as `index.md`) |

**Citation quote convention (Phase 17):** All DNS Bhat typographic `` `word` `` quotes are standardised to curly single quotes `'word'` (U+2018 open, U+2019 close) in kn.md and kn-eke.md files. Do not use backtick as open-quote.

**Unrounded-u marker:** `u^` in kn-eke.md represents ಉ್ (unrounded-u vowel, Havyaka feature). This is distinct from citation quotes and must not be changed.

---

## Languages & Tooling

### Python (YouTube transcript pipeline)
Location: `src/main/python/yt-transcript/`

```bash
# Setup
cd src/main/python/yt-transcript
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Workflow
python extract_transcripts.py         # Extract raw transcripts from YouTube
python extract_smart.py               # Smart extraction with language detection
python cleanup_with_claude.py         # Clean transcripts using Claude API
python cleanup_books.py               # Update books with cleaned transcripts
python extract_kannada_only.py        # Extract Kannada-only content
python transliterate_devanagari.py    # Convert Devanagari to Eke romanization
```

**Key dependency:** `youtube-transcript-api` — requires internet access; may encounter YouTube rate limiting.

### Haskell
Location: `src/main/haskell/`

```bash
# Quick project (Stack)
cd src/main/haskell/quick
stack build
stack test

# Euterpea music examples (requires Euterpea installed)
ghc src/main/haskell/euterpea/rangapura.hs
```

### Scala / Kojo
Location: `src/main/scala/` — standalone scripts and `.kojo` visualization files. No SBT project at root.

---

## Unicode Handling

This project deals extensively with Kannada Unicode (U+0C80–U+0CFF), Devanagari, and Japanese text:
- File names may contain Kannada script (e.g., `ಕಳ್ಳ.hs`, `ಕಳ್ಳ.md`)
- Transcript files contain raw Kannada, sometimes with OCR/ASR artifacts
- Transliteration maps Kannada → Eke romanization (aspirates simplified)

---

## Eke Romanization System

Eke (Ellara Kannada) is a romanization system documented in `Eke.md`. Two distinct rules apply depending on context:

**When romanizing existing Kannada text (books, OCR, transcripts):** Aspirates are **preserved**:
ಖ→kh, ಘ→gh, ಛ→ch, ಝ→jh, ಠ→Th, ಢ→Dh, ಥ→th, ಧ→dh, ಫ→ph, ಭ→bh

**When coining new native Kannada words (Ellara methodology):** Avoid aspirated consonants — native Dravidian speech has no mahapranas, so prefer k, g, c, j, T, D, t, d, p, b in new coinages.

**Always:**
- Retroflexes in UPPERCASE: ಟ→T, ಡ→D, ಣ→N, ಳ→L, ಶ/ಷ→S
- Long vowels in UPPERCASE: ಆ→A, ಈ→I, ಊ→U, ಏ→E, ಓ→O
- Vocalic ṛ (ಋ/ೃ): x (short), X (long rare) — e.g. ಸಂಸ್ಕೃತ → samskxta
- Anusvara ಂ: assimilated nasal — never standalone M. Before labials/sonorants→m; before velars/dentals/palatals/retroflexes→n
- N = exclusively ಣ; never write N for anusvara before stop consonants
- r = ರ always; R = rare archaic ಱ only

Full four-rule error table: `.claude/CLAUDE.md` → Eke Canonical Rules.

---

## Books

Personal reading catalog located in `src/main/md/Books/`:
- **`Books.md`** — Master index of influential books, organized by author with inline summaries. Categories include: Western Fiction, Kannada/Indian Literature, Indian Classical Texts, D. N. Shankara Bhat linguistics works, Science & Biology, History & Biography, Math & Computing, Martial Arts & Physical Practice, Economics & Ideas.
- **`Books-Top.md`** — Modern Library Top 100 novels list with summaries.
- **`influential/`** — Individual files for each book with: Summary, Critical Takeaways, and My Takeaways sections.

Two sections in `Books.md` are yet to be populated: "Read but Not That Influential" and "Want to Read".

---

## Physics

Located in `src/main/md/physics/`:
- **`UniversalConsciousness.md`** — Explores a unified field theory of universal consciousness with Advaitic (non-dual) philosophical foundations, blending quantum field theory with Vedanta concepts.

---

## Self-Reflection

Located in `src/main/md/self-reflection/`:
- **`index.md`** — Navigation index for all reflection documents.
- Dated files follow the `YYYY-MM-DD_topic.md` naming convention. Topics covered include: Kannada linguistics, Indian history/culture, functional programming (Scala/Haskell), machine learning/AI, mathematics, algorithms, data engineering, infrastructure/DevOps, health/fitness, and miscellaneous.

---

## GitHub Pages / Jekyll

The `docs/` directory is served at https://vwulf.github.io/ettuge/ via GitHub Pages with Jekyll.
- `docs/kannaDa/dnsbhat/` — per-book pages (generated from src/ into `docs/kannaDa/` by CI)
- `docs/kannaDa/eke/` — Eke romanisation reference pages (generated from `src/main/md/kannada/eke/`)
- `docs/dnsbhat/PROJECT-RECAP.md` — full phased project history (canonical; serves at /dnsbhat/PROJECT-RECAP)
- `docs/claude-project-instructions.md` — combined CLAUDE.md + skills for Claude.ai Projects (phone-accessible)
- `docs/_config.yml` — Jekyll config (theme: just-the-docs; title: ettuge — Kannada Linguistics)
- Do not commit generated HTML directly — Jekyll builds from `.md` source on push.
- **Sidebar structure (Phase 28):** `DNS Bhat` (L1 root, nav_order=2) → `Books`/`Blog`/`YouTube`/`Stubs` (L2) → `ಕನ್ನಡ`/`ಏಕೆ`/`English` (L3, grand_parent=DNS Bhat, body=sorted book table); `Eke` (L1 root, nav_order=3) → `Eke Reference`/`Motivation` (L2). Individual book pages and `ಕನ್ನಡ` wrapper nav_excluded. Icons: ಕ (Kannada), 🇮🇳 (Eke), 🇺🇸 (English).
- Old `/dnsbhat/` URLs redirect automatically via `redirect_from:` front matter in each file.

---

## Important Notes

1. **DNS Bhat is the reference standard** — when discussing Kannada vocabulary or creating translations, always prefer DNS Bhat's native (Dravidian-root) word choices over Sanskrit-derived terms.
2. **Transcripts have two versions** — `transcripts/` (raw, may be garbled) and `transcripts_cleaned/` (AI-processed). Always prefer cleaned versions for linguistic analysis.
3. **Rate limiting** — the Python YouTube scripts use proxy rotation and delays; do not bypass these.
4. **Session transcripts** in `src/main/claude/kannada/` document prior AI conversations — useful context for ongoing linguistic decisions.


### .claude/CLAUDE.md — Automation Context

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
| ರ vs ಱ | `vaRNa`, `sRiSTi` | `varNa`, `sxShTi` | Lowercase `r` = ರ always; `R` = exclusively rare ಱ |
| Vocalic ṛ ಋ/ೃ | `samskrita`, `sriSTi`, `kRi`→`kri` | `samskxta`, `sxShTi`, `kx` | `x` = ಋ/ೃ (short); `X` = ೠ/ೄ (long, rare) |

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
All kn.md files have a ಪರಿವಿಡಿ/ಒಳಪಿಡಿ table at the top linking to `<a id="adhyAya-N">` anchors. All books with kn.md (02, 03, 07-vol1, 07-vol2, 08, 14, 17, 25, 27, 28, 29) now have deep `<a id="sec-N-M">` and `<a id="sub-N-M-K">` anchors (Phase 19). The TOC in each book lists all levels (chapter → section → subsection).

### Chapter pages (Phase 32)
The CI step in `pages.yml` walks all `docs/kannaDa/dnsbhat/*/book/*/full.md` and generates paginated chapter pages at build time:
- `ch0.md` — preamble + ಪರಿವಿಡಿ TOC with `#chN` links rewritten to page-relative `chN` links + chapter quick-nav bar; front matter: `nav_exclude: true`
- `ch1.md`…`chN.md` — one per chapter anchor; nav banner with ← Contents / → Next
- Sidebar CANDIDATES: `book/kn/ch0.md` takes priority over `book/kn/full.md` so the lightweight index loads first on slow connections
- Books with ≥2 chapter anchors get split; single-chapter files are skipped
- Chapter anchor formats recognised: `<a id="chN">` and `<a id="adhyAya-N">`
- All books with `book/kn/full.md` (03, 07vol1–vol4, 08, 14, 17, 25, 27, 28, 29, 30, 31) now have chapter anchors

### Cross-link convention (Phase 19)
After every `<a id="sec-N-M">` or `<a id="sub-N-M-K">` anchor, insert a cross-link on its own line:
- In kn.md: `[Eke →](./SLUG-kn-eke#sec-N-M)` or `[Eke →](./SLUG-kn-eke#sub-N-M-K)`
- In kn-eke.md: `[ಕನ್ನಡ →](./SLUG-kn#sec-N-M)` or `[ಕನ್ನಡ →](./SLUG-kn#sub-N-M-K)`
- Chapter nav `[English →](./en#ch) | [Eke →](./kn-eke#adhyAya-N)` in kn.md; `[English →](...) | [ಕನ್ನಡ →](./kn#adhyAya-N)` in kn-eke.md
- Header block: `> [← ಸೂಚಿ](./README) | ಇಂಗ್ಲಿಶ್ ...: [en] | Eke: [kn-eke]` in kn.md; `> [← sUci](./README) | ingliS ...: [en] | kannaDa: [kn]` in kn-eke.md

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
| `docs/dnsbhat/PROJECT-RECAP.md` | Full phased project history (Phases 1–19) — canonical record of all OCR cleanup decisions, quote conventions, Eke rules, and pending work |
| `docs/claude-project-instructions.md` | Combined skills + CLAUDE.md context for Claude.ai Projects (phone access) |


### Kannada Directory CLAUDE.md

# Kannada Directory — CLAUDE.md

This directory contains the PRIMARY linguistic work for the ettuge project.

## Key Files
- `Eke.md` — Full Eke romanization specification (153KB) — do NOT edit casually
- `Eke.kn.md` — Complete Kannada translation of Eke.md (DNS Bhat compliant, complete)
- `Eke.eke.md` — Eke romanization of Eke.kn.md (complete)
- `brahmi-nabatian-phoenician-hieroglyphs-lineage.md` — Script history documentation
- `kannada-mnemonics-hieroglyph-hook.md` — Kannada mnemonic table
- `malatibhat_dns_bhat_chat.md` / `malatibhat_dns_bhat_videos.md` — Video references and analysis
- `malatibhat_dns_bhat_videos_links.txt` — Raw video link list

## Subdirectories

### `dnsbhat/` — DNS Bhat Book Collection (33 books, numbered 01–33)
Each book directory uses the Phase-20 4-level taxonomy (`source/lang/type.md`):
- `book/kn/raw.md` or `book/kn/full.md` — Structured Kannada source (do NOT use old `*-kn.md` names)
- `book/eke/full.md` — Eke romanisation (regenerate after kn changes)
- `book/en/summary.md` — Chapter-wise English summary
- `youtube/kn/full.md` — YouTube transcript (Kannada, with ಪರಿವಿಡಿ TOC and `<a id="part-N">` anchors)
- `claude-prompt.md` — Condensed prompt for Claude sessions
- `README.md` — Book index (serves as Jekyll page)

**Chapter pages (Phase 32):** CI generates `ch0.md` (index) + `ch1.md`…`chN.md` per chapter from `<a id="chN">` / `<a id="adhyAya-N">` anchors in `full.md`. Sidebar links to `ch0.md` as the entry point (lightweight for slow connections).

**Citation quotes:** Standardised to curly single quotes `'word'` (U+2018/U+2019) in kn.md and kn-eke.md. Never use backtick as open-quote.
**Unrounded-u:** `u^` in kn-eke.md = ಉ್ (Havyaka phoneme) — do not alter.
**Nudi OCR:** Books 14–29 were Nudi-encoded; OCR produces garbled Latin. See `.claude/CLAUDE.md` for fix pipeline.
**Project history:** `docs/dnsbhat/PROJECT-RECAP.md`

### `transcripts/` — Raw YouTube transcripts (349+ files, may have ASR artifacts)
### `transcripts_cleaned/` — AI-processed transcripts (130+ files)
### `sections/` — Extracted transcript sections

## Rules for This Directory
1. All new Kannada vocabulary must follow DNS Bhat's native (Dravidian-root) methodology. Reference: `dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
2. Avoid Sanskrit-derived terms when a native Kannada equivalent exists.
3. Eke romanization rules — TWO modes:
   - **Romanising existing Kannada text:** aspirates PRESERVED (ಭ→bh, ಧ→dh, ಖ→kh etc.); retroflexes UPPERCASE (T, D, N, L, S); long vowels UPPERCASE (A, I, U, E, O); vocalic ṛ → x; anusvara ಂ → assimilated nasal (never standalone M); N = exclusively ಣ; r = ರ always, R = rare archaic ಱ.
   - **New native word coining (Ellara):** avoid aspirated consonants — prefer k, g, c, j, T, D, t, d, p, b. All other rules same.
   - Full canonical error table: `.claude/CLAUDE.md` → "Eke Canonical Rules".
4. Always prefer `transcripts_cleaned/` over `transcripts/` for analysis.
5. Files may have Kannada-script names — handle Unicode carefully.

## Unicode
Kannada script range: U+0C80–U+0CFF. Filenames and content may contain Kannada Unicode characters.


### Books Directory CLAUDE.md

# Books Directory — CLAUDE.md

Personal reading catalog.

## Structure
- `Books.md` — Master index organized by author with inline summaries. Categories: Western Fiction, Kannada/Indian Literature, Indian Classical Texts, DNS Bhat linguistics, Science & Biology, History & Biography, Math & Computing, Martial Arts & Physical Practice, Economics & Ideas.
- `Books-Top.md` — Modern Library Top 100 novels list with summaries.
- `influential/` — One file per book with three required sections.

## File Convention for `influential/`
Each book file must contain exactly three sections:
1. **Summary** — concise overview
2. **Critical Takeaways** — objective analysis
3. **My Takeaways** — personal reflection

## TODO
- "Read but Not That Influential" section in `Books.md` is unpopulated
- "Want to Read" section in `Books.md` is unpopulated


### Self-Reflection CLAUDE.md

# Self-Reflection Directory — CLAUDE.md

This directory contains topic-based derivatives of `self.md` and `self-1.md`, personal notes files (Signal channel "self" export, 2021–2026) not stored in the repository. Each entry has been enriched with a 2–4 sentence prose description and a `[→ category]` routing hint.

---

## Structure

- **`README.md`** — Master navigation index listing all topic files with descriptions (displayed automatically on GitHub).
- **`project-recap.md`** — Project recap covering the four phases: cleanup → categorize → enrich+split → consolidate.
- **`YYYY-MM-DD_topic.md`** — Individual topic files, all derived from `self.md`/`self-1.md` on 2026-02-25.

### Current Topic Files

| File | Topic |
|------|-------|
| `2026-02-25_scala-functional-programming.md` | ZIO, Scala 3, Kyo, Haskell, functional effects, type theory |
| `2026-02-25_machine-learning-ai.md` | LLMs, RAG, fine-tuning, Indic LLMs, AI infrastructure |
| `2026-02-25_kannada-language-linguistics.md` | Kannada script, DNS Bhat grammar, Dravidian linguistics, Karnataka culture |
| `2026-02-25_indian-history-culture.md` | Harappan genetics, Indus script, ancient/medieval India, prehistory |
| `2026-02-25_infrastructure-devops.md` | Nix, AWS, Kubernetes, CI tools, EVs |
| `2026-02-25_algorithms-data-structures.md` | LeetCode (Scala), Knight's Tour, system design |
| `2026-02-25_health-fitness.md` | VO2 max, climbing, martial arts, nutrition, cold exposure |
| `2026-02-25_mathematics-science.md` | Riemann hypothesis, Langlands, category theory, biology, geology |
| `2026-02-25_data-engineering.md` | Spark, system design, Kannada data pipeline (alar.ink) |
| `2026-02-25_books-literature.md` | Books read, reading lists, literary essays, reviews |
| `2026-02-25_arts-music-film.md` | Music, cinema, documentaries, visual art, performance |
| `2026-02-25_travel-outdoors.md` | Hiking, adventure sports, Bay Area food, extreme sports |
| `2026-02-25_cricket-sports.md` | Match commentary, IPL analysis, player profiles, sports analytics |
| `2026-02-25_current-events-politics.md` | US/India politics, immigration, geopolitics, civil rights |
| `2026-02-25_career-personal.md` | Career, self-development, personal philosophy, PKM, AI tools |
| `2026-02-25_miscellaneous.md` | **Retired stub** — all content redistributed to the 16 files above |

---

## Rules for This Directory

1. **Enrichment format:** each entry = `**Bold heading**` → 2–4 sentence prose → `**[→ category; cross-link → other-category]**` → URL.
2. **Naming convention:** `YYYY-MM-DD_topic-slug.md` — date reflects when the file was derived.
3. **Cross-linking:** if a note fits multiple categories, it lives in the most specific file and cross-links to others using the `[→]` tag.
4. **`miscellaneous.md`** is retired — all residual entries have been moved to the 16 topic files.
5. **`README.md`** (the index) must be kept in sync whenever new topic files are added.

---

## Adding New Topic Files

When deriving new files from updated `self.md`/`self-1.md` content:
1. Use the date of derivation as the filename prefix (`YYYY-MM-DD`).
2. Add a frontmatter block with `title`, `created`, and `source`.
3. Group by primary subject domain.
4. Add a row to the table in `README.md` and this `CLAUDE.md` table above.


### Haskell Directory CLAUDE.md

# Haskell Directory — CLAUDE.md

Haskell source files for functional programming examples and music composition.

---

## Files

| File | Description |
|------|-------------|
| `accum.hs` | Accumulator examples |
| `cat.hs` | Categorical / functional composition examples |
| `reflection.hs` | Reflection utilities |
| `sqrt.hs` | Square root implementations |
| `ಕಳ್ಳ.hs` | Kannada-named Haskell file (Unicode filename — do not rename) |

## Subdirectories

- `euterpea/` — Music composition using the Euterpea library (`rangapura.hs`, `twinkle.hs`)
- `quick/` — Quick Haskell project managed with Stack

---

## Build & Run

### Quick project (Stack)
```bash
cd src/main/haskell/quick
stack build
stack test
```

### Euterpea music examples
Requires Euterpea installed separately:
```bash
ghc src/main/haskell/euterpea/rangapura.hs
```

### Standalone scripts
Files in the root `haskell/` directory are standalone — compile directly with `ghc`:
```bash
ghc src/main/haskell/sqrt.hs
```

---

## Notes
- There is no top-level Cabal or Stack project for standalone files — only `quick/` uses Stack
- Unicode filenames (Kannada script, e.g. `ಕಳ್ಳ.hs`) are intentional; do not rename or transliterate them
- See root `CLAUDE.md` for Unicode handling guidelines (U+0C80–U+0CFF range)


### Python Directory CLAUDE.md

# Python Directory — CLAUDE.md

YouTube transcript extraction and processing pipeline.

## Setup
```bash
cd src/main/python/yt-transcript
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Script Execution Order
1. `extract_transcripts.py` — raw extraction from YouTube
2. `extract_smart.py` — smart extraction with language detection
3. `cleanup_with_claude.py` — clean transcripts via Claude API
4. `cleanup_books.py` — update books catalog with cleaned transcripts
5. `extract_kannada_only.py` — filter Kannada-only content
6. `transliterate_devanagari.py` — convert Devanagari to Eke romanization

## Critical Notes
- DO NOT bypass proxy rotation or rate-limiting delays in scripts
- `youtube-transcript-api` requires internet access; expect YouTube rate limiting
- Outputs go to `src/main/md/kannada/transcripts/` (raw) and `transcripts_cleaned/` (processed)

