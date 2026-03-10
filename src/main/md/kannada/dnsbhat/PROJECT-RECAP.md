# DNS Bhat Ettuge Project — Recap
*Last updated: 2026-03-10*

---

## What Is This Project?

The **ettuge DNS Bhat exercise** is a systematic effort to collect, digitise, structure, and make accessible the complete works of **Dr. D. N. Shankara Bhat** — Kannada's most important modern linguist.

The work lives at:
```
/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/
```

The project has three simultaneous goals:

1. **Text recovery** — Get readable Unicode text from all available sources (YouTube, website, PDF, DjVu, blog, OCR)
2. **Structured annotation** — Produce per-book files in a consistent format: `kn.md` (Kannada), `en.md` (English summary), `kn-eke.md` (Eke romanisation), `claude-prompt.md` (AI context primer)
3. **Ellara Kannada (Eke) romanisation** — Render Bhat's Kannada in his own *ellara kannaDa* system so that non-Kannada readers and AI models can engage with the phonological content directly

---

## About DNS Bhat

**Dr. D. N. Shankara Bhat** (Dayadhara Nagesha Shankara Bhat) was born in 1931 in the Havyaka Brahmin community of coastal Karnataka.

He held positions at Deccan College (Poona), Trivandrum, Manipur, Leeds, Stanford, Antwerp, the Max Planck Institute, and La Trobe. He won the **Pampa Award**, Karnataka's highest literary honour.

His work has two pillars:

| Pillar | Works | Audience |
|--------|-------|----------|
| **International typology** | *Pronouns* (Oxford, 2004), *Sound Change* (Motilal, 2001), *The Koraga Language* (1971), *An Outline Grammar of Havyaka* (1971), *Grammatical Relations* (journal) | Academic, English |
| **Kannada language reform** | *Sollarime* (7 vols), *Mahaprana Yake Beda*, *Baasheya Bagge*, *Hosapadagalannu Kattuva Bage*, *Nijakku Halegannada Vyakarana*, and 20+ more | General Kannada readers |

His central argument, developed over 50 years: **Kannada grammar must be built from Kannada's own structure, not borrowed from Sanskrit or English frameworks.**

---

## The Catalogue: 29 Known Works

The full registry is in [`BOOKS.md`](./BOOKS.md). Summary:

| # | Short Title | Language | Key Topic | Text Status |
|---|-------------|----------|-----------|-------------|
| 01 | Idu Kannadade Vyakarana | Kn | Native grammar framework | ✅ Transcript |
| 02 | Hosapadagalannu Kattuva Bage | Kn | Word formation | ✅ Transcript + 15 blog posts |
| 03 | Kannada Padagala Olarachane | Kn | Morphology | ✅ Transcript + **OCR** |
| 04 | Mathu Matthu Barahada Gondala | Kn | Speech vs. writing | ⚠️ Partial |
| 05 | Mathina Olaguttu | Kn | Deep structure of language | ✅ Transcript |
| 06 | Kalikenudi Matthu Nudikalike | Kn | Language acquisition | ❌ Corrupted |
| 07 | Kannadada Sollarime (7 vols) | Kn | Complete grammar | ⚠️ Partial + **OCR vol1+2** |
| 08 | Kannadakke Mahaprana Yake Beda | Kn | Script reform (aspirates) | ✅ **Full text** |
| 09 | Havyaka Kannada | Kn | Havyaka dialect (popular) | ⚠️ Corrupted |
| 10 | Kannada Nudiya Hinnadavali | Kn | History of Kannada | ⚠️ Corrupted |
| 11 | Kannada Barahada Padasamasye | Kn | Orthographic problems | ❌ Corrupted |
| 12 | Kannada Bhasheya Kalpita Charitre | Kn | Reconstructed history | ✅ Short excerpt |
| 13 | Dharege Doddavaru | Kn | Old Kannada literature | ❌ Corrupted |
| 14 | Nijakku Halegannada Vyakarana Entahadu | Kn | Old Kannada grammar | ✅ **Full text** + 7 blog posts |
| 15 | Inglish Kannada Padanerake | Kn | English→Kannada vocabulary | ⚠️ Sample only |
| 16 | Samskruta Padagalige Kannadade Padagalu | Kn | Sanskrit→Kannada terms | ❌ Not collected |
| 17 | Kannada Nudi Nadedu Banda Dari | Kn | Path of Kannada language | ✅ **OCR** |
| 18 | Kannada Nudiya Bagege Chintane | Kn | Reflections on Kannada | ✅ 13 blog posts |
| 19 | The Koraga Language | En | Koraga (endangered Dravidian) | ❌ PDF not extracted |
| 20 | An Outline Grammar of Havyaka | En | Havyaka grammar (academic) | ✅ **Full DjVu text** |
| 21 | Pronouns (Oxford) | En | Pronoun typology | ❌ PDF not extracted |
| 22 | Sound Change | En | Historical phonology theory | ❌ Not collected |
| 23 | A Grammar of Manipuri | En+Kn | Manipuri grammar | ❌ Not collected |
| 24 | Grammatical Relations | En | Syntax theory (journal) | ❌ Not collected |
| 25 | Kannada Vakyagala Olarachane | Kn | Sentence structure | ✅ **OCR** |
| 26 | Uli Marpadina Geregalu | Kn | Sound change laws | ❌ Cloudflare-blocked |
| 27 | Baasheya Bagge | Kn | Introduction to linguistics | ✅ **OCR** |
| 28 | Kannadakke Beku | Kn | Why Kannada needs its grammar | ✅ **OCR** |
| 29 | Kannada Vyakarana Yaake Beku | Kn | Why grammar matters | ✅ **OCR** |

---

## File Naming Convention

Each book folder follows this pattern:

```
{NN}-{slug}/
  {NN}-{slug}-book.md      # Raw extracted/OCR text
  {NN}-{slug}-kn.md        # Structured Kannada version with TOC + anchors
  {NN}-{slug}-kn-eke.md    # Eke romanisation companion
  {NN}-{slug}-en.md        # English chapter summaries
  {NN}-{slug}-claude-prompt.md  # AI context primer (key terms, thesis, chapter map)
  {NN}-{slug}-blog.md      # Blog posts (where applicable)
  {NN}-{slug}-djvu.md      # DjVu OCR text (where available)
  {NN}-{slug}-website.md   # Website/online content stub
  {NN}-{slug}-sample.md    # Sample pages
```

The **type suffix** taxonomy: `book` · `kn` · `kn-eke` · `en` · `claude-prompt` · `blog` · `djvu` · `website` · `sample`

---

## What Has Been Done (Chronological)

### Phase 1 — Discovery & Cataloguing

- **Crawled dnshankarabhat.net** via CDX Wayback API → found 91 unique archived pages
- **Identified 29 works** across Kannada popular books, English academic monographs, journal articles, and blog series
- Created `BOOKS.md` — comprehensive annotated catalogue of all 29 works, organised into thematic sections (Grammar, Dialect Studies, History, Vocabulary, Old Kannada, English Academic, Sound Change, Syntax)

### Phase 2 — Text Collection

**YouTube transcripts** extracted for books 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 12, 13:
- Best quality: 02 (519 lines), 03 (605 lines), 05 (539 lines)
- Corrupted: 06, 09, 10, 11, 13 (garbled or truncated)

**Internet Archive (archive.org)** extractions:
- Book 08: PDF + DjVu → 4,243-line `book.md` + 1,965-line `djvu.md` — ✅ full clean text
- Book 14: PDF + DjVu → 11,791-line `book.md` + 7,033-line `djvu.md` — ✅ full clean text
- Book 20: DjVu → full text of 1971 Havyaka grammar — ✅

**Blog collection** via Wayback Machine CDX + fetch:
- Book 02: 15 blog posts (parts 4–18 of *ಇಂಗ್ಲಿಶ್ ಪದಗಳಿಗೆ ಸಾಟಿ...* series)
- Book 14: 7 blog posts (*ಶಬ್ದಮಣಿದರ್ಪಣದಲ್ಲಿ ತಳಮಟ್ಟದ ತಪ್ಪುಗಳು* series, May–June 2017)
- Book 18: 13 blog posts (parts 1–3, 10, 14, 18, 20, 23, 27–29, 33, 35 of *ನುಡಿಯರಿಮೆಯ ಇಣುಕುನೋಟ* series)

**Google Drive PDF downloads** (10 new PDFs, 2026-03-10):
- Books 03, 07(vol1+2), 17, 25 — confirmed in Drive
- Books 27, 28, 29 — **newly discovered books**, not previously in catalogue
- Book 15 — sample/prelims PDF (53 pages)
- Problem identified: all PDFs use old **WX Kannada font encoding** (non-Unicode, Ghostscript/PageMaker era) → pdfminer extracts garbled text like `¨sÁµÉAiÀÄ`

### Phase 3 — Structured Files (kn / en / kn-eke / claude-prompt)

**Book 08** — *Kannadakke Mahaprana Yake Beda* — first fully structured book:
- `kn.md` — 5-chapter structured Kannada text with TOC, `<a id>` anchors
- `kn-eke.md` — Eke romanisation (first kn-eke produced; served as format template)
- `en.md` — English chapter-by-chapter analysis
- `claude-prompt.md` — AI context primer with key terms table

**Book 14** — *Nijakku Halegannada Vyakarana Entahadu*:
- `kn.md` — 12-chapter structured Kannada text
- `kn-eke.md` — Eke romanisation (created by background agent `aa87faf`)
- `en.md` — English summary with blog series integration
- `claude-prompt.md` — AI primer
- `blog.md` — 7 Shabdamani blog posts

**Book 18** — *Kannada Nudiya Bagege Chintane*:
- `en.md` — English summaries of all 13 blog posts (29KB) — created by agent `a1f957e`
- `kn-eke.md` — Eke romanisation of all 13 posts (11KB)
- `claude-prompt.md` — AI primer with key terms table (7KB)

**Book 20** — *An Outline Grammar of Havyaka*:
- `en.md` — English chapter summaries (phonology, morphology, verb paradigms, case system)
- `claude-prompt.md` — 10 key grammatical features, 25 key terms

**Book 02** — *Kannadalle Hosapadagalannu Kattuva Bage* — most complex structured book:
- `kn.md` — 547 lines, 17 chapters, 37 sections, all with `<a id>` anchors
- `kn-eke.md` — 830 lines, 43KB — Eke romanisation of all 37 sections, complete with dual cross-links to kn.md and en.md
- `en.md` — English summary with cross-references
- `claude-prompt.md` — word-formation methodology primer
- `blog.md` — 15 blog posts (6,469 lines)

### Phase 4 — Sarvam Vision OCR Pipeline

**Problem:** 8 PDFs in Google Drive use old WX Kannada font encoding. `pdfminer` and `pdftotext` extract garbled bytes. Clean Kannada Unicode text is not recoverable by text extraction alone — OCR is needed.

**Solution:** Sarvam Vision API — a 3B multimodal VLM with 84.3% accuracy on olmOCR-Bench, trained on Indian languages including Kannada (`kn-IN`). Accepts PDF pages, outputs Markdown.

**Implementation:** `ettuge/src/main/python/sarvam-ocr/`

| File | Purpose |
|------|---------|
| `requirements.txt` | `sarvamai`, `pypdf` |
| `ocr.py` | Single-PDF OCR: splits into 10-page chunks (API limit), OCRs each chunk, concatenates |
| `ocr_dnsbhat.py` | Batch processor: all 8 WX-encoded books, prepends Kannada header to output |
| `README.md` | Setup, usage, API workflow documentation |

**Key technical detail:** The Sarvam Document Intelligence API has a **10-page limit per job**. `ocr.py` uses `pypdf` to split each PDF into ≤10-page chunks, submits each as a separate job (create → upload → start → poll → download ZIP → extract .md), then concatenates.

**Iteration required to get API call right:**
1. `BadRequestError: PDF has 239 pages, maximum allowed is 10` — discovered 10-page limit; added `pypdf` chunking
2. `TypeError: wait_until_complete() got an unexpected keyword argument 'on_poll'` — inspected actual SDK source; API returns `DocDigitizationJobStatusResponse` with `.job_state` field (values: `"Completed"`, `"PartiallyCompleted"`, `"Failed"`), no callback parameter

**OCR run status** (as of 2026-03-10):
| Book | Pages | Chunks | Status |
|------|-------|--------|--------|
| 03 — Padagala Olarachane | 239 | 24 | ✅ `book.md` written |
| 07-vol1 — Sollarime vol.1 | 327 | 33 | ✅ `book.md` written |
| 07-vol2 — Sollarime vol.2 | 301 | 31 | ✅ `book.md` written |
| 17 — Nudi Nadedu Banda Dari | 405 | 41 | ✅ `book.md` written |
| 25 — Vakyagala Olarachane | 289 | 29 | ✅ `book.md` written |
| 27 — Baasheya Bagge | 208 | 21 | ✅ `book.md` written |
| 28 — Kannadakke Beku | 253 | 26 | ✅ `book.md` written |
| 29 — Kannada Vyakarana Yaake Beku | 260 | 26 | ✅ `book.md` written |

---

## Eke Romanisation System

**Ellara KannaDa (Eke)** is DNS Bhat's own romanisation of Kannada, designed to be learnable by any Indian and usable by non-Kannada readers. It is the romanisation used throughout the `-kn-eke.md` files.

### Core Rules

| Feature | Convention | Examples |
|---------|-----------|---------|
| Short vowels | lowercase | a i u e o |
| Long vowels | UPPERCASE | A I U E O |
| No aspirates | ಭ→b, ಧ→d, ಖ→k, ಥ→t, ಫ→p | bAsha, baddu |
| Retroflexes | UPPERCASE consonant | T D N L S |
| Anusvara assimilation | context-sensitive nasal | ಂಕ→nk, ಂಗ→ng, ಂತ→nt, ಂದ→nd, ಂಪ→mp, ಂಬ→mb |
| Velar nasal (ಙ) | ng | nADu→nADu |

### Key Terminology in Eke

| Kannada | Eke | English |
|---------|-----|---------|
| ಹೆಸರು ಪದ | hesaru pada | noun |
| ಎಸಕ ಪದ | esaka pada | verb |
| ಪರಿಚರಣ ಪದ | parichaRaNa pada | adjective |
| ಸೊಲ್ಲರಿಮೆ | sollarime | grammar |
| ನುಡಿಯರಿಮೆ | nuDiyarime | linguistics |
| ಉಲಿ | uLi | phoneme/sound |
| ಬರಿಗೆ | barige | letter/grapheme |
| ಮಾರ್ಪು | mArpu | suffix |
| ಒಟ್ಟು | oTTu | affix |
| ಮುನ್ನೊಟ್ಟು | munnoTTu | prefix |
| ಕೀಳರಿಮೆ | kILarime | inferiority complex |
| ಮೇಲರಿಮೆ | mElarime | superiority complex |
| ಎಲ್ಲರ ಕನ್ನಡ | ellara kannaDa | everyone's Kannada (Eke) |

---

## File Structure Summary

```
dnsbhat/
├── BOOKS.md                          # Master catalogue — 29 books, annotated
├── PROJECT-RECAP.md                  # This file
├── dns-bhat-analysis.md              # Early analysis document
├── kannada-content-landscape.md      # Content survey
├── kannada-knowledge-gap-analysis.md # Gap analysis
├── swadesh-bhat-prompt-and-analysis.md
├── wiktionary-cost-analysis-kimi-k2.5.md
│
├── 01-idu-kannadade-vyakarana/
│   ├── 01-...-youtube.md             # Transcript
│   └── 01-...-website.md
├── 02-kannadadalle-hosapadagalannu-kattuva-bage/
│   ├── 02-...-blog.md                # 15 blog posts
│   ├── 02-...-kn.md                  # ★ Structured Kannada (547 lines)
│   ├── 02-...-kn-eke.md              # ★ Eke romanisation (830 lines, 43KB)
│   ├── 02-...-en.md                  # ★ English summaries
│   ├── 02-...-claude-prompt.md       # ★ AI primer
│   └── 02-...-website.md
├── 03-kannada-padagala-olarachane/
│   ├── 03-...-book.md                # ★ Sarvam OCR output (239 pages)
│   └── 03-...-website.md
├── 07-kannadada-sollarime/
│   ├── 07-...-vol1-book.md           # ★ Sarvam OCR (327 pages)
│   ├── 07-...-vol2-book.md           # ★ Sarvam OCR (301 pages)
│   └── 07-...-website.md
├── 08-kannadakke-mahaprana-yake-beda/
│   ├── 08-...-book.md                # Full text (archive.org)
│   ├── 08-...-djvu.md                # DjVu OCR
│   ├── 08-...-kn.md                  # ★ Structured Kannada
│   ├── 08-...-kn-eke.md              # ★ Eke romanisation (template book)
│   ├── 08-...-en.md                  # ★ English analysis
│   ├── 08-...-claude-prompt.md       # ★ AI primer
│   └── 08-...-website.md
├── 14-nijakku-halegannada-vyakarana-entahadu/
│   ├── nijakku-...-book.md           # Full text (archive.org)
│   ├── 14-...-djvu.md                # DjVu OCR
│   ├── 14-...-blog.md                # 7 blog posts
│   ├── 14-...-kn.md                  # ★ Structured Kannada
│   ├── 14-...-kn-eke.md              # ★ Eke romanisation
│   ├── 14-...-en.md                  # ★ English summary
│   ├── 14-...-claude-prompt.md       # ★ AI primer
│   └── 14-...-website.md
├── 17-kannada-nudi-nadedu-banda-dari/
│   ├── 17-...-book.md                # ★ Sarvam OCR (405 pages)
│   └── 17-...-website.md
├── 18-kannada-nudiya-bagege-chintane/
│   ├── 18-...-blog.md                # 13 blog posts
│   ├── 18-...-kn-eke.md              # ★ Eke romanisation
│   ├── 18-...-en.md                  # ★ English summaries (29KB)
│   ├── 18-...-claude-prompt.md       # ★ AI primer (7KB)
│   └── 18-...-website.md
├── 20-havyaka-outline-grammar/
│   ├── 20-...-djvu.md                # Full DjVu text
│   ├── 20-...-en.md                  # ★ English chapter summaries
│   ├── 20-...-claude-prompt.md       # ★ AI primer
│   └── 20-...-website.md
├── 25-kannada-vakyagala-olarachane/
│   ├── 25-...-book.md                # ★ Sarvam OCR (289 pages)
│   └── 25-...-website.md
├── 27-baasheya-bagge/
│   └── 27-...-book.md                # ★ Sarvam OCR (208 pages) — NEW BOOK
├── 28-kannadakke-beku/
│   └── 28-...-book.md                # ★ Sarvam OCR (253 pages) — NEW BOOK
├── 29-kannada-vyakarana-yaake-beku/
│   └── 29-...-book.md                # ★ Sarvam OCR (260 pages) — NEW BOOK
└── [... 11 more folders with website stubs or transcripts ...]
```

★ = created/significantly enriched in this project

---

## Pending Work

### High priority (next steps)

| Task | Books | What's needed |
|------|-------|---------------|
| Check OCR quality | 03, 07, 17, 25, 27, 28, 29 | Read first 50 lines of each `-book.md`; verify Kannada Unicode, not garbled |
| Create `kn.md` for OCR books | 03, 07, 17, 25, 27, 28, 29 | Structure chapters with TOC + `<a id>` anchors |
| Create `en.md` for OCR books | 03, 07, 17, 25, 27, 28, 29 | English chapter-by-chapter summaries |
| Create `claude-prompt.md` | 03, 07, 17, 25, 27, 28, 29 | Key terms, thesis, structure primers |
| Create `kn-eke.md` for OCR books | 03, 07 (vol1+2), 17, 25, 27, 28, 29 | Eke romanisation companions |
| Book 15 re-OCR | 15 | 53-page sample PDF — run Sarvam OCR |
| Book 19 extract | 19 | The Koraga Language PDF — Unicode-safe, run Sarvam OCR |
| Book 21 extract | 21 | DNS Bhat Pronouns (Oxford) PDF |

### Medium priority

| Task | Notes |
|------|-------|
| Collect missing blog posts | Books 02 (parts 1–3), 18 (many parts) — check more Wayback snapshots |
| Book 26 — Uli Marpadina Geregalu | Cloudflare-blocked; try different snapshots or direct Google Cache |
| Books 16, 22, 23, 24 | Not yet collected; website stubs only |
| Update BOOKS.md OCR status | Mark books 03, 07, 17, 25, 27, 28, 29 as ✅ once OCR quality verified |

### Low priority / stretch

| Task | Notes |
|------|-------|
| Sollarime vol.3–7 | Only vol.1+2 PDFs found; vols 3–7 may be at dnshankarabhat.net (offline) |
| Retroflexion 1973 paper | Stanford Working Papers; should be in archive.org |
| Cambridge Dravidian Languages chapter | DNS Bhat contributed to Cambridge Language Surveys |

---

## Tools & Pipeline

| Tool | Used for |
|------|---------|
| **Wayback CDX API** | Crawling dnshankarabhat.net (91 pages found) |
| **pdfminer** | PDF text extraction (failed for WX-encoded PDFs) |
| **DjVu text** | archive.org DjVu OCR (books 08, 14, 20) |
| **Sarvam Vision API** | OCR for WX-encoded PDFs (kn-IN, 10-page chunks) |
| **pypdf** | PDF splitting for chunked OCR |
| **sarvamai** (PyPI) | Python SDK for Sarvam API |
| **Claude agents** | Parallel book processing (kn-eke, en.md, claude-prompt) |
| **ettuge** | Scala/SBT project hosting all MD content |

OCR pipeline location: `ettuge/src/main/python/sarvam-ocr/`

---

## Key Intellectual Themes

### 1. Kannada-native grammar (anti-Sanskrit framework)
Bhat's life work: Kannada has its own grammatical logic. The three base categories are *hesaru pada* (noun), *esaka pada* (verb), *parichaRaNa pada* (adjective) — not Sanskrit's verb-root primacy. Books 01, 07, 08, 14, 28, 29.

### 2. Script reform (mahaprana / aspirated consonants)
Kannada phonology does not distinguish aspirated from unaspirated stops. The mahaprana letters (ಖ ಘ ಛ ಝ ಠ ಢ ಥ ಧ ಫ ಭ) are Sanskrit imports serving no phonological function. Book 08 makes this argument; books 28 and 29 are written in *hosa baraha* (simplified script without mahapranas).

### 3. Word formation without Sanskrit (native Dravidian roots)
Over 50% of standard Kannada vocabulary is Sanskrit-derived; 80% in scientific writing. Books 02 and 15 document systematic native Dravidian word-formation patterns using roots, affixes, and compounds.

### 4. Dialect documentation
Academic description of dialects as data: Havyaka (books 09, 20), Koraga (book 19), Belari (in book 19). These are not "corrupted" dialects but independent systems.

### 5. Sound change as the mechanism of language history
The theoretical underpinning of books 08, 14, 26: sound changes are regular, reconstructable, and explain the Sanskrit/Kannada relationship. Book 22 is the English theoretical monograph; Book 26 is the Kannada popularisation.
