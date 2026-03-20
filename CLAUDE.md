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

### Current Status (as of 2026-03-20, Phase 19)

All 29 DNS Bhat books have been processed through multiple phases of OCR cleanup, Nudi→Unicode conversion, romanisation generation, and TOC restructuring. Key milestones:

- **Phase 19 (2026-03-20):** Deep 3-level TOC with `<a id="sec-N-M">` and `<a id="sub-N-M-K">` anchors added to all books with kn.md (02, 03, 07-vol1, 07-vol2, 08, 14, 17, 25, 27, 28, 29). Section/subsection cross-links added: `[Eke →]` after every sec/sub anchor in kn.md; `[ಕನ್ನಡ →]` in kn-eke.md. Index back-links `[← ಸೂಚಿ](./README)` added to all kn.md headers; `[← sUci]` to kn-eke.md. Chapter nav fragments fixed to `#adhyAya-N`. kn-eke.md self-referential header links corrected.
- **Phase 18 (2026-03-19):** Chapter/section headings converted to Markdown `##`/`###`/`####`. Book 28 deep TOC added, printed flat TOC removed, 5 heading-number OCR errors fixed. Book 03 subsection numbering corrected (1.6→1.5).
- **Phase 17 (2026-03-19):** Nudi/WX encoding cleanup for books 03, 07 (vol1+vol2), 08, 14, 17, 25, 27, 28, 29. TOC restructured with `<a id="adhyAya-N">` anchors (books 03, 27). Citation quote convention standardised to curly single quotes `'word'` (U+2018/U+2019) across books 07, 17, 25, 28. Unrounded-u marker unified to `u^` across all kn-eke files.
- **Phase 16 (2026-03-17):** Running headers removed, arka-ottu reversals fixed, fragment cleanup across 5 books.
- **Earlier phases:** Transcript cleanup (349 videos), Eke.md translation (complete), DNS Bhat book summarization pipeline established.

Full history: `docs/dnsbhat/PROJECT-RECAP.md` (also served at https://vwulf.github.io/ettuge/dnsbhat/PROJECT-RECAP).

### DNS Bhat Methodology
All translation work must follow DNS Bhat's native Kannada word formation system:
- Reference: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Books: `src/main/md/kannada/dnsbhat/` — 29 book directories (01–29); see `dnsbhat/README.md` for the full annotated catalogue
- Analysis files: `dns-bhat-analysis.md`, `kannada-content-landscape.md`, `kannada-knowledge-gap-analysis.md`
- DNS Bhat prefers native (Dravidian) roots over Sanskrit. In Eke romanisation of his own books, aspirated forms ARE romanised as-is (bh, dh, kh etc.) because he uses Sanskrit loanwords — only *new coinages* avoid aspirates.

### DNS Bhat Book File Structure

Each book directory contains:
| File pattern | Content |
|-------------|---------|
| `NN-slug-book.md` or `NN-slug.md` | Raw OCR archive — do NOT edit |
| `NN-slug-kn.md` | Structured Kannada source: paragraph breaks, TOC, `<a id="adhyAya-N">` anchors |
| `NN-slug-en.md` | Chapter-wise English summary with cross-links to kn.md anchors |
| `NN-slug-kn-eke.md` | Eke romanisation matching kn.md section structure |
| `NN-slug-claude-prompt.md` | Condensed prompt context for Claude sessions |
| `README.md` | Book-level index (rendered on GitHub) |

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
- `docs/dnsbhat/` — per-book `.html` pages (generated from kn.md, en.md, kn-eke.md sources in `src/`)
- `docs/dnsbhat/PROJECT-RECAP.md` — full phased project history
- `docs/claude-project-instructions.md` — combined CLAUDE.md + skills for Claude.ai Projects (phone-accessible)
- `_config.yml` — Jekyll config (theme: minima, plugins: jekyll-relative-links)
- Do not commit generated HTML directly — Jekyll builds from `.md` source on push.

---

## Important Notes

1. **DNS Bhat is the reference standard** — when discussing Kannada vocabulary or creating translations, always prefer DNS Bhat's native (Dravidian-root) word choices over Sanskrit-derived terms.
2. **Transcripts have two versions** — `transcripts/` (raw, may be garbled) and `transcripts_cleaned/` (AI-processed). Always prefer cleaned versions for linguistic analysis.
3. **Rate limiting** — the Python YouTube scripts use proxy rotation and delays; do not bypass these.
4. **Session transcripts** in `src/main/claude/kannada/` document prior AI conversations — useful context for ongoing linguistic decisions.