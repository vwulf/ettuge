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

### Current Status (as of 2026-03-23, Phase 27)

All 33 DNS Bhat books have been catalogued; books 30–33 now have content files. Key milestones:

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