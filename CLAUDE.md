# CLAUDE.md — ettuge

This file provides guidance to Claude Code when working in this repository.

## Overview

Ettuge is a linguistic research project focused on native Kannada language preservation. It combines:
- Documentation of the **Eke** (Ellara Kannada) romanization system
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

### Current Status

All issues and PRs are currently closed. The Eke translation work is complete:
- **PR #6**: Initial Kannada translation of `Eke.md` (merged 2026-02-18)
- **PR #9**: DNS Bhat native terminology applied (merged 2026-02-18)
- **PR #12, #15**: Further Sanskrit → native Kannada replacements (merged 2026-02-18 and 2026-02-19)
- **PR #14**: Transliteration of `Eke.kn.md` → `Eke.eke.md` (merged 2026-02-19)
- **PR #16**: Euterpea encoding of Rangapura Vihara (merged 2026-02-19)
- **PR #17**: Brahmi lineage markdown cleanup (merged 2026-02-24)
- **PR #18**: Kannada mnemonic table added (merged 2026-02-24)
- **PR #19**: Fixed author attribution in `Books.md` (merged 2026-02-26)
- **PR #22**: Added auto-assign workflow for new issues (merged 2026-02-26)
- **PR #23, #24**: `UniversalConsciousness.md` added/updated in `physics/` (merged 2026-02-27)
- **Ongoing**: Processing YouTube transcripts (349+ videos, 130+ cleaned)
- **New content**: `physics/` and `self-reflection/` directories added

`Eke.kn.md` (Kannada translation) and `Eke.eke.md` (Eke romanization) are complete and DNS Bhat compliant.

### DNS Bhat Methodology
All translation work must follow DNS Bhat's native Kannada word formation system:
- Reference: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Books: `src/main/md/kannada/dnsbhat/` — 13 book directories (01–13):
  - 01-idu-kannadade-vyakarana
  - 02-kannadadalle-hosapadagalannu-kattuva-bage
  - 03-kannada-padagala-olarachane
  - 04-mathu-matthu-barahada-naduvina-gondala
  - 05-mathina-olaguttu
  - 06-kalikenudi-matthu-nudikalike
  - 07-kannadada-sollarime
  - 08-kannadakke-mahaprana-yake-beda
  - 09-havyaka-kannada
  - 10-kannada-nudiya-hinnadavali
  - 11-kannada-barahada-padasamasye
  - 12-kannada-bhasheya-kalpita-charitre
  - 13-dharege-doddavaru
- Analysis files:
  - `dns-bhat-analysis.md`
  - `kannada-content-landscape.md`
  - `kannada-knowledge-gap-analysis.md`
  - `swadesh-bhat-prompt-and-analysis.md`
  - `wiktionary-cost-analysis-kimi-k2.5.md`
- The Eke system removes aspirated consonants — prefer native Kannada (Dravidian) roots over Sanskrit-derived terms

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

Eke (Ellara Kannada) is a simplified romanization designed for native Kannada speakers:
- **Aspirates removed:** kh→k, gh→g, ch→c, jh→j, th→t, dh→d, ph→p, bh→b
- **Retroflexes preserved:** ಟ→T, ಡ→D, ಣ→N, ಳ→L
- **Velar nasals:** ಙ→G, ಞ→Y
- Full mappings documented in `Eke.md`

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

## Important Notes

1. **DNS Bhat is the reference standard** — when discussing Kannada vocabulary or creating translations, always prefer DNS Bhat's native (Dravidian-root) word choices over Sanskrit-derived terms.
2. **Transcripts have two versions** — `transcripts/` (raw, may be garbled) and `transcripts_cleaned/` (AI-processed). Always prefer cleaned versions for linguistic analysis.
3. **Rate limiting** — the Python YouTube scripts use proxy rotation and delays; do not bypass these.
4. **Session transcripts** in `src/main/claude/kannada/` document prior AI conversations — useful context for ongoing linguistic decisions.