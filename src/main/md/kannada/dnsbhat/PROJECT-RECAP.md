# DNS Bhat Ettuge Project — Recap
*Last updated: 2026-03-21 (Phase 23)*

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

The full registry is in [`README.md`](./README.md). Summary:

| # | Short Title | Language | Key Topic | Text Status | Processed |
|---|-------------|----------|-----------|-------------|-----------|
| 01 | Idu Kannadade Vyakarana | Kn | Native grammar framework | ✅ Transcript | ❌ |
| 02 | Hosapadagalannu Kattuva Bage | Kn | Word formation | ✅ Transcript + 15 blog posts | ✅ full |
| 03 | Kannada Padagala Olarachane | Kn | Morphology | ✅ Transcript + OCR | ✅ full |
| 04 | Mathu Matthu Barahada Gondala | Kn | Speech vs. writing | ⚠️ Partial (25/44 parts) | ✅ full |
| 05 | Mathina Olaguttu | Kn | Deep structure of language | ✅ Transcript (27/37 parts) | ✅ full |
| 06 | Kalikenudi Matthu Nudikalike | Kn | Language acquisition | ❌ Corrupted | ❌ |
| 07 | Kannadada Sollarime (7 vols) | Kn | Complete grammar | ⚠️ Partial + OCR vol1+2 | ✅ full |
| 08 | Kannadakke Mahaprana Yake Beda | Kn | Script reform (aspirates) | ✅ Full text | ✅ full |
| 09 | Havyaka Kannada | Kn | Havyaka dialect (popular) | ⚠️ Partial (72/88 slots) | ✅ full |
| 10 | Kannada Nudiya Hinnadavali | Kn | History of Kannada | ⚠️ Corrupted | ❌ |
| 11 | Kannada Barahada Padasamasye | Kn | Orthographic problems | ❌ Corrupted | ❌ |
| 12 | Kannada Bhasheya Kalpita Charitre | Kn | Reconstructed history | ✅ Short excerpt | ❌ |
| 13 | Dharege Doddavaru | Kn | Old Kannada literature | ❌ Corrupted | ❌ |
| 14 | Nijakku Halegannada Vyakarana Entahadu | Kn | Old Kannada grammar | ✅ Full text + 7 blog posts | ✅ full |
| 15 | Inglish Kannada Padanerake | Kn | English→Kannada vocabulary | ⚠️ Sample only (53p) | ✅ full |
| 16 | Samskruta Padagalige Kannadade Padagalu | Kn | Sanskrit→Kannada terms | ❌ Not collected | ❌ |
| 17 | Kannada Nudi Nadedu Banda Dari | Kn | Path of Kannada language | ✅ OCR | ✅ full |
| 18 | Kannada Nudiya Bagege Chintane | Kn | Reflections on Kannada | ✅ 13 blog posts | ✅ full |
| 19 | The Koraga Language | En | Koraga (endangered Dravidian) | ❌ PDF not extracted | ❌ |
| 20 | An Outline Grammar of Havyaka | En | Havyaka grammar (academic) | ✅ Full DjVu text | ✅ en+prompt |
| 21 | Pronouns (Oxford) | En | Pronoun typology | ❌ PDF not extracted | ❌ |
| 22 | Sound Change | En | Historical phonology theory | ❌ Not collected | ❌ |
| 23 | A Grammar of Manipuri | En+Kn | Manipuri grammar | ❌ Not collected | ❌ |
| 24 | Grammatical Relations | En | Syntax theory (journal) | ❌ Not collected | ❌ |
| 25 | Kannada Vakyagala Olarachane | Kn | Sentence structure | ✅ OCR | ✅ full |
| 26 | Uli Marpadina Geregalu | Kn | Sound change laws | ❌ Cloudflare-blocked | ❌ |
| 27 | Baasheya Bagge | Kn | Introduction to linguistics | ✅ OCR | ✅ full |
| 28 | Kannadakke Beku | Kn | Why Kannada needs its grammar | ✅ OCR | ✅ full |
| 29 | Kannada Vyakarana Yaake Beku | Kn | Why grammar matters | ✅ OCR | ✅ full |

**"Processed" = full** means the book has all four key files: `en.md` + `kn-eke.md` + `claude-prompt.md` (+ `kn.md` where applicable). **"en+prompt"** means English and claude-prompt done but no kn-eke (English-language book).

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

**OCR run status** (all ✅ complete as of 2026-03-10):
| Book | Pages | Chunks | book.md |
|------|-------|--------|---------|
| 03 — Padagala Olarachane | 239 | 24 | ✅ |
| 07-vol1 — Sollarime vol.1 | 327 | 33 | ✅ |
| 07-vol2 — Sollarime vol.2 | 301 | 31 | ✅ |
| 17 — Nudi Nadedu Banda Dari | 405 | 41 | ✅ |
| 25 — Vakyagala Olarachane | 289 | 29 | ✅ |
| 27 — Baasheya Bagge | 208 | 21 | ✅ |
| 28 — Kannadakke Beku | 253 | 26 | ✅ |
| 29 — Kannada Vyakarana Yaake Beku | 260 | 26 | ✅ |

### Phase 5 — WX Decode Tool

Books 07, 17, 25, 28, 29 had OCR output in WX Kannada encoding (old Nudi/KGP font). Built `wx_decode.py` — a lookup-table decoder (based on aravindavk/ascii2unicode) that converts WX-encoded bytes to Unicode Kannada. Decoded ~1.9M Kannada Unicode chars across 6 files.

### Phase 6 — Bulk Processing of OCR Books (2026-03-11)

Created `en.md` + `kn-eke.md` + `claude-prompt.md` for all 5 remaining unprocessed OCR books using parallel background agents:

| Book | en.md | kn-eke.md | claude-prompt.md | Agents |
|------|-------|-----------|-----------------|--------|
| 03 — Padagala Olarachane | ✅ (prev.) | ✅ (prev.) | ✅ (prev.) | — |
| 07 — Kannadada Sollarime | ✅ 41KB | ✅ 9KB | ✅ 18KB | aed65cd |
| 17 — Nudi Nadedu Banda Dari | ✅ 35KB | ✅ 12KB | ✅ 20KB | ae26172 |
| 25 — Vakyagala Olarachane | ✅ 30KB | ✅ 19KB | ✅ 25KB | ae33f5d |
| 27 — Baasheya Bagge | ✅ (prev.) | ✅ (prev.) | ✅ (prev.) | — |
| 28 — Kannadakke Beku | ✅ 25KB | ✅ 14KB | ✅ 20KB | aaccf5f |
| 29 — Kannada Vyakarana Yaake Beku | ✅ 28KB | ✅ 12KB | ✅ 19KB | a0622eb |

**Format notes for claude-prompt.md:**
- Books 07, 17, 25 (technical linguistics): modelled on Book 03 template
- Books 27, 28, 29 (advocacy/popular): modelled on Book 08 template

### Phase 7 — Book 15 Hybrid Extraction & Processing (2026-03-12)

**Book 15** — *Inglish Kannada Padanerake* — first dictionary-format book processed:
- **Source:** 53-page sample PDF (`English-KannadaPadanerakeSample.pdf`) — pre-print prelims covering letter A (A→Az)
- **Challenge:** Old WX Nudi font encoding. English headwords extracted via raw pdfminer ASCII; Kannada equivalents decoded with `wx_decode.py` `convert_text()`. Result: 3,454-line `book.md` with 84,475 Kannada Unicode characters.
- `kn-eke.md` — Eke romanisation of preface, conventions, pattern tables, and ~100-entry A–Az transliteration sample
- `en.md` — English analysis with **10 word-formation pattern sections**: N+N compounding, verb-derived nouns (-ta/-ike/-uge/-me/-vu), agent nouns (-ga/-uga/-gAra), ಅರಿಮೆ domain names, ಮನೆ institutions, ಗಾಳಿ air-cluster, ಮಾಂಜುಗೆ therapy compounds, productive prefixes, and more
- `claude-prompt.md` — Rich AI primer: 6-step word-generation decision tree, 11 domain-specific head-noun cluster tables, 100 curated entries by domain, common mistakes table (Sanskrit vs native), philosophical frame

### Phase 8 — Cross-link Audit & Fixes; Book 15 kn-eke Restructure; Transcript Book Processing (2026-03-13)

**Cross-link audit** — systematic review of all processed books revealed inconsistent cross-linking in `en.md` files:

| Issue | Books affected | Fix applied |
|-------|---------------|-------------|
| `[ಕನ್ನಡ →]` links present but no `[Eke →]` links | 02, 08, 14 | Appended `\| [Eke →](kn-eke.md#anchor)` to every existing section link (43 + 33 + 61 links) |
| No cross-links at all (bulk-processed books) | 07, 17, 25, 27, 28, 29 | Inserted `[ಕನ್ನಡ →](book.md) \| [Eke →](kn-eke.md#anchor)` after each chapter heading (60 total links across 6 files) |
| Broken links to non-existent `kn.md` | 03 | Retargeted 9 links to `book.md` (bare) + added `[Eke →]` with correct kn-eke.md anchors; fixed footer reference |

All `en.md` files now follow the Book 14 template: every chapter/section heading has a `[ಕನ್ನಡ →] | [Eke →]` cross-link pair on the line immediately below.

**Book 15 kn-eke.md restructured** — original file mixed analytical pattern sections (N+N compounds, suffix tables, etc.) derived from `en.md` work with source-text romanisation. Restructured to be a proper romanisation of the source text:
- Removed: analytical kaTTaNe pattern tables (those belong in `en.md`)
- Retained: Eke romanisation of actual munnuDi (preface), irusarikegaLu (conventions), and all A–Az dictionary entries with usage examples
- Title updated to `ingliS-kannaDa padanerake — Eke mUla` to make the source-text nature explicit

**Transcript books 04, 05, 09 fully processed** — first systematic processing of YouTube-transcript-only books. Each had only a raw `.md` transcript and a website stub; now all three have a complete set of structured files:

| Book | Source Quality | en.md | kn-eke.md | claude-prompt.md |
|------|----------------|-------|-----------|-----------------|
| 04 — Mathu Matthu Barahada Gondala | ~25/44 parts (~57%) | ✅ 7 themes | ✅ key passages | ✅ AI primer |
| 05 — Mathina Olaguttu | ~27/37 parts (~73%) | ✅ 8 themes | ✅ key passages | ✅ AI primer |
| 09 — Havyaka Kannada | ~72/88 slots (~82%) | ✅ 5 themes | ✅ key passages | ✅ AI primer |

**Methodology for transcript books:** Unlike OCR books, transcript books have no continuous chapter text — only partial lecture recordings with gaps. The `en.md` files use a "Thematic Structure (Replacing Table of Contents)" format with coverage notes per section indicating which parts are readable vs. garbled. The `kn-eke.md` files extract and romanise the best available passages (rather than attempting whole-book coverage). The `claude-prompt.md` files follow the standard template adapted for transcript-quality sources, including explicit source limitation notes.

### Phase 9 — Eke Romanisation Bug-Fix Passes (2026-03-13)

Systematic correction of four romanisation errors propagated across all processed `kn-eke.md` files. Errors originated from LLM generation using HK-adjacent conventions instead of Eke rules.

| Pass | Error pattern | Correct Eke | Files | Instances |
|------|--------------|-------------|-------|-----------|
| 1 — Anusvara (M) | `M` used for anusvāra (HK style) | Assimilated nasal+C: `mb, mp, nk, ng, nc, nt, nd…` — **never standalone M** | 14 files | ~1,511 |
| 2 — N as anusvara | `N` (retroflex ಣ) used before stop consonants | `n` before stop consonants; N reserved exclusively for ಣ | 12 files | ~69 |
| 3 — R as ರ | `R` (exclusively ಱ) incorrectly used for common ರ | Lowercase `r` for all ರ; R kept exclusively for ಱ | 9 files | ~230 |
| 4 — Vocalic ṛ as ri/ru | `kRi/sri/kri/kru` used for ೃ/ಋ (vocalic ṛ) | Eke `x` (short ṛ = ಋ/ೃ); Eke `X` (long ṝ = ೠ/ೄ) | all files | ~400+ |

**Pass 4 specific word families fixed:**

| Wrong | Correct | Kannada | Count |
|-------|---------|---------|-------|
| `samskrita / samskruta / samskrta` | `samskxta` | ಸಂಸ್ಕೃತ | ~400 |
| `sriSTi` | `sxSTi` | ಸೃಷ್ಟಿ | ~30 |
| `driSTi` | `dxSTi` | ದೃಷ್ಟಿ | ~10 |
| `driSya` | `dxSya` | ದೃಶ್ಯ | 3 |
| `srijana` | `sxjana` | ಸೃಜನ | 1 |
| `mrita` | `mxta` | ಮೃತ | 1 |
| `tritIya` | `txtIya` | ತೃತೀಯ | 2 |

**Caution applied:** Words where original Kannada genuinely has ಕ್ರ + ಉ/ಇ (consonant r + vowel) were not changed. Examples: `krutaka` (ಕ್ರುತಕ), `krudanta`, `krullingagaLa`, `kriyA` (ಕ್ರಿಯಾ) — all verified to use consonant r, not ೃ sign.

**Skill files updated** — both `dns-bhat-book-summarizer/SKILL.md` and `dns-bhat-transcript-summarizer/SKILL.md` vowel/consonant tables corrected with all four rules. `ellara-kannada-word-coiner/SKILL.md` and `references/eke-romanization.md` also updated.

### Phase 10 — Book 08 varSa OCR Correction (2026-03-14)

Targeted fix for a systematic OCR misread in book 08 (*Kannadakke Mahaprana Yake Beda*). The word **ವರ್ಷ** ("year", Eke: `varSa`) was rendered in four wrong patterns by the OCR engine — corrected in both the Eke romanisation file and the structured Kannada file.

| Wrong form | Correct | Count |
|-----------|---------|-------|
| `varragaL*` / `varradoLage` | `varSagaL*` / `varSadoLage` | 6 |
| `varmagaL*` | `varSagaL*` | 3 |
| `varyagaL*` | `varSagaL*` | 2 |
| `varka` | `varSa` | 2 |

**Files fixed:** `08-kannaDakke-mahAprANa-yAke-bEDa-kn-eke.md` (13 instances) and `08-kannaDakke-mahAprANa-yAke-bEDa-kn.md` (matching Kannada script corrections: ವರ್ರ, ವರ್ಮ, ವರ್ಯ, ವರ್ಕ → ವರ್ಷ). No other books contained these patterns.

### Phase 11 — GitHub Pages / Jekyll Deployment (2026-03-14–15)

Set up a public-facing website at **https://vwulf.github.io/ettuge/** using Jekyll with the `just-the-docs` theme, served via GitHub Pages. The entire pipeline is in `.github/workflows/pages.yml` — no pre-generated files are checked in; everything is built fresh from `src/` on every push to `master`.

**Infrastructure built:**

| Component | Details |
|-----------|---------|
| `docs/_config.yml` | `theme: just-the-docs`, `color_scheme: light`, `search_enabled: true`, `nav_fold: true`, `defaults: layout: default` |
| `docs/Gemfile` | `gem "just-the-docs"` pinned for GitHub Actions |
| `.github/workflows/pages.yml` | Build + deploy pipeline: copy src/ → docs/dnsbhat/, generate nav, add front matter, Jekyll build, deploy |
| `.claude/launch.json` | Local preview server entry: `bundle exec jekyll serve --livereload --baseurl ""` |

**Bugs encountered and fixed:**

| Bug | Root cause | Fix |
|-----|-----------|-----|
| 404 on all pages | `configure-pages@v5` step had no `id:` → `base_path` was empty → Jekyll built without baseurl → all links used `/dnsbhat/...` instead of `/ettuge/dnsbhat/...` | Added `id: setup-pages` to the step |
| Content files (en/kn/eke) returned 404 | `-en.md`, `-kn.md`, `-kn-eke.md` lacked Jekyll front matter → Jekyll treated them as static assets, never built HTML | Workflow step prepends `---\nnav_exclude: true\n---` to every `.md` missing front matter |
| Sidebar flooded with transcripts, prompts, metadata | Empty `---\n---` front matter made all files sidebar-visible | Changed injected front matter to `nav_exclude: true` |
| Accidentally committed `docs/dnsbhat/` files | `.gitignore` pattern `docs/dnsbhat/*/` only excluded subdirs, not root-level loose files | `git rm --cached`; added `docs/dnsbhat/*.md` exception (`!docs/dnsbhat/index.md`) to `.gitignore` |

**Format-first sidebar redesign:**

The original sidebar showed books by number, and each book's entry pointed to the raw README metadata — noisy and not useful for readers. Replaced with a **format-oriented three-section sidebar** generated by a Python script in the workflow:

```
English Summaries        (nav_order: 10)
  └── Book 02 — Hosapadagalannu Kattuva Bage
  └── Book 03 — Padagala Olarachane
  └── ...  (en.md preferred; blog.md fallback; YouTube transcript last resort)

Kannada Text             (nav_order: 20)
  └── Book 02, 03, 07, 08, 14, ...  (kn.md or book.md)

Eke Transliteration      (nav_order: 30)
  └── Book 02, 03, 04, ...  (kn-eke.md)
```

The Python script (inline `python3 - <<'PYEOF'` in the workflow):
1. Creates three section index pages (`english-summaries.md`, `kannada-text.md`, `eke-transliteration.md`) with `has_children: true`
2. For each book directory, finds the best available file per format (en > blog > fallback)
3. Rewrites each content file's front matter with `parent: "English Summaries"` (or Kannada Text / Eke Transliteration) and `nav_order: {book_num}` — placing it in the correct sidebar section
4. Rewrites the book's main landing page body as a **clean summary**: Kannada title, English title, description blockquote, status, and a links table — no more raw README metadata or YouTube TOC at top level
5. Books with a dedicated `en.md` get `nav_exclude: true` on their landing page (the en.md IS the sidebar entry); transcript-only books get `parent: "English Summaries"` on their landing page (it IS the entry)

**Result:** All 29 books appear in the English Summaries section; 16 appear in Kannada Text; 14 appear in Eke Transliteration. Book landing pages are clean reader-facing pages, not developer metadata dumps.

### Phase 13 — Book 28 OCR Deep-Clean + kn.md + Anchors (2026-03-17)

Full multi-pass OCR cleanup of book 28 (*ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ*), creation of a clean `kn.md` (both books 28 and 29), anchor scaffolding, and cross-link updates. Also documented the full OCR-cleaning methodology in a new `kannada-ocr-cleaner` skill.

**OCR character-level fixes — book 28 (three-pass pipeline)**

The raw `-book.md` OCR text used the legacy Nudi/KGP font encoding (WX-decoded to Unicode by `wx_decode.py`, but with residual character-level errors). Three targeted fix scripts ran in sequence:

| Script | What it fixed | Instances |
|--------|--------------|-----------|
| `fix_arka_ottu.py` | arka-ottu reversals: `ಣ್ರ→ರ್ಣ`, `ಥ್ರ→ರ್ಥ`, `ಮ್ರ→ರ್ಮ`, `ಯ್ರ→ರ್ಯ`, `ದೀಘ್ರ→ದೀರ್ಘ`; word-specific `ತ್ರ/ಧ್ರ` cases; `ಙõï/ÂÐ→ಙ್`; `ಬಹÅ→ಬಹು` | ~500+ |
| `fix_residual_ocr.py` | Residual long-e `ಯುೀ→ಯೇ` (59×); archaic diphthong `0iÀiï→ಯ್` (2×); proper name `ತಾರಾಪೆÇರೆವಾಲಾ→ತಾರಾಪೋರ್ವಾಲಾ`; bibliography English garbling (`ಖಿhe → The`, `ಆeಟhi → Delhi`, etc.) | ~75 |
| `fix_page_fragments.py` | Structural: orphaned fragments before section headings (12 cases); standalone running chapter headers (8 cases — 4 with fragments, 4 without) | 96 lines deleted |

**OCR structural artifacts (new class discovered)**

The most interesting class of errors was purely structural, not character-level: page-break artifacts where the last words of a print page ended up as isolated blank-line-separated lines just before the next subsection heading. Example before fix:
```
ಹೇಳಿ ಕೊಡುವುದು ಹೇಗೆ ತಪ್ಪಾಗುತ್ತದೆಯೋ ಹಾಗೆಯೇ ಇದೂ ಕೂಡ.

ವ್ಯಾಕರಣವೆಂಬುದು

ನುಡಿಯಿಂದ

ನುದಿಗೆ

1.2  ವ್ಯಾಕರಣದ ಉದ್ದೇಶ
```
After fix: `ಹೇಳಿ ಕೊಡುವುದು ಹೇಗೆ ತಪ್ಪಾಗುತ್ತದೆಯೋ ಹಾಗೆಯೇ ಇದೂ ಕೂಡ. ವ್ಯಾಕರಣವೆಂಬುದು ನುಡಿಯಿಂದ ನುದಿಗೆ`

Running chapter headers (chapter titles printed at the top of each print page, OCR'd into the body) were deleted — the 12 chapter names (`ಮುನ್ನೋಟ`, `ಸೇರಿಕೆಯ ನಿಯಮಗಳು`, …, `ಮುಕ್ತಾಯ`) were built into a `RUNNING_HEADERS` set and matched exactly. The key detection rule: a line is an orphaned fragment *only if preceded by a blank line* — this guards against misidentifying normal wrapped paragraph lines (which are not preceded by blanks).

Total effect: 9,613 → 9,517 lines (96 lines removed, 16 modified).

**kn.md creation (books 28 + 29)**

New `kn.md` files created from the cleaned OCR for both books, with:
- Jekyll front matter (nav_order, title, parent, redirect_from)
- `<a id="adhyAya-N"></a>` anchors before each `## N. ChapterTitle` heading
- 12 chapter anchors for book 28 (`adhyAya-1` through `adhyAya-12`)
- 11 chapter anchors for book 29 (`adhyAya-1` through `adhyAya-11`)
- Cross-navigation links: `[English →](en#chapter-N--...) | [Eke →](kn-eke#anchor)` before each chapter heading

**en.md anchors + cross-links (books 28 + 29)**

Both `-en.md` files updated with:
- 13 `<a id="chapter-N--...">` anchors in book 28 (chapters 1–12 + key-terms-glossary)
- 12 `<a id="chapter-N--...">` anchors in book 29 (chapters 1–11 + key-terms-glossary)
- All `[ಕನ್ನಡ →]` links updated from bare `-book` targets to `-kn#adhyAya-N` fragment URLs

**kannada-ocr-cleaner skill created**

New Claude skill at `.claude/skills/kannada-ocr-cleaner/SKILL.md` documenting all four classes of error and the methodology:
- Class 1: Vowel-sign/consonant garbling (ಯ, ಯೇ, ಯ್, ಙ್, ಬಹು patterns)
- Class 2: Arka-ottu reversal (global-safe + word-specific replacements)
- Class 3: English text garbled through legacy font (bibliography, titles)
- Class 4: OCR page-break structural artifacts (orphaned fragments + running headers) — added in this phase, with the full three-pass fix script pattern

### Phase 12 — mahAprana (Aspirate) Eke Correction (2026-03-16)

Corrected a systematic error in the Eke romanisation rule for aspirated consonants. All `kn-eke.md` files had been generated with the wrong rule "drop aspirates" (ಭ→b, ಧ→d, ಖ→k, ಥ→t, ಫ→p, ಭ→b). The correct rule is "preserve aspirates with h marker" (ಭ→bh, ಧ→dh, ಖ→kh, ಥ→th, ಫ→ph).

The guiding principle: Eke romanises what is *written* in the source. If the source uses ಭ (aspirated labial), the romanisation must write `bh`, not `b` — to faithfully represent what DNS Bhat wrote. (Separately, the word-coining philosophy of *ellara kannaDa* avoids mahapranas in *new* coinages, since they don't occur in native Dravidian speech — but that's a word-formation rule, not a transcription rule.)

**Specific fixes applied (Python `re.sub` + `replace`):**

| Wrong Eke | Correct Eke | Source consonant | Instances |
|-----------|-------------|-----------------|-----------|
| `bAShe` | `bhAShe` | ಭ (ಭಾಷೆ) | ~18 files |
| `bAga` | `bhAga` | ಭ (ಭಾಗ) | multiple |
| `sankara baT` | `sankara bhaT` | ಭ (ಭಟ್) | all files |
| `adyAya` | `adhyAya` | ಧ (ಅಧ್ಯಾಯ) | multiple |
| `sambanda` | `sambandha` | ಧ | multiple |
| `\badika` | `adhika` | ಧ | multiple |
| `\bmukya` | `mukhya` | ಖ (ಮುಖ್ಯ) | multiple |
| `leKana` | `lEkhana` | ಖ (ಲೇಖನ) | multiple |
| `lEkakaru` | `lEkhakaru` | ಖ (ಲೇಖಕರು) | multiple |
| `\barta` | `artha` | ಥ (ಅರ್ಥ) | multiple |
| `\bpATa` | `pATha` | ಠ (ಪಾಠ) | multiple |
| `bAgya` | `bhAgya` | ಭ (ಭಾಗ್ಯ) | 1 |
| `dIrga` | `dIrgha` | ಘ (ದೀರ್ಘ) | 2 |

**Commit:** `907ac31` "eke: fix all mahAprANa (aspirate) romanization" — 22 files, 398 insertions/deletions

**Skill files and PROJECT-RECAP** also updated in this phase to reflect the corrected rule.

### Phase 14 — Bulk OCR Cleanup: Books 03, 07, 17, 25, 27 (2026-03-17)

Character-level and structural cleanup of the five remaining uncleaned OCR books, producing `-kn.md` files for each and regenerating all six `-kn-eke.md` files. All books now have 0 residual Kannada characters in their Eke output.

**Two OCR error classes, two fix scripts:**

| Book(s) | OCR source | Error type | Fix script |
|---------|-----------|-----------|-----------|
| 03, 27 | Sarvam Vision OCR | Structural artifacts only (page numbers, `---` separators, running headers) | `fix_books_sarvam.py` |
| 07, 17, 25 | Sarvam OCR + WX-decode | Character-level garbling + structural artifacts | `fix_books_wx.py` |

**WX character-level errors fixed (books 07, 17, 25):**

| Error class | Pattern | Scope |
|------------|---------|-------|
| Arka-ottu reversal | `ಣ್ರ→ರ್ಣ`, `ಥ್ರ→ರ್ಥ`, `ಮ್ರ→ರ್ಮ`, `ಯ್ರ→ರ್ಯ`, `ಧ್ರ→ರ್ಧ` | All 3 books |
| Ç-fix (garbled aa-mathrā U+00C7) | `\u0CC6\u00C7\u0CBF` → `\u0CCB` (oo-sign); `\u0CC6\u00C7` → `\u0CCA` (o-sign) | All 3 books |
| Ya-garble | `0iÉ` (U+0030+U+0069+U+00C9) → `ಯ`; 159 occurrences | Book 17 only |
| Word-specific | `ನಿದ್ರಿಷ್ಟ→ನಿರ್ದಿಷ್ಟ`, `ನಿದ್ರೇಶ→ನಿರ್ದೇಶ`, `¦ÃpPÉ→ಪೀಠಿಕೆ`, `ದೀಘ್ರ→ದೀರ್ಘ` | Book 25 only |

**Key decisions on safe vs. unsafe replacements:**
- `ದ್ರ→ರ್ದ` blanket fix is **UNSAFE** — legitimate in `ಕೇಂದ್ರ`, `ದ್ರಾವಿಡ`, `ಚಂದ್ರ` etc.; targeted word-level fixes only
- `ನ್ರ` in `ಏನ್ರಿ` is legitimate colloquial Kannada — not an arka-ottu error
- `ಧ್ರ` in books 03/27 (Sarvam OCR) is legitimate (`ಆಂಧ್ರ`, `ಉತ್ತರಧ್ರುವ`) — Sarvam OCR was correct

**Multi-pass dependency fix:** The `ಸಾಮಥ್ಯ್ರ` problem: `ಯ್ರ→ರ್ಯ` creates `ಥ್ರ` *after* `ಥ್ರ→ರ್ಥ` has already run. Solved by `apply_char_fixes()` iterating up to `max_passes=3` until text is stable. A single pass was insufficient for this class of chained reversal.

**Critical structural insight:** Char fixes must be applied to the **entire file** (including TOC, acknowledgements, index sections before the first `<a id="adhyAya-N">` anchor), not only the body. An earlier version that split header/body first and fixed only the body left hundreds of errors in front matter and prefatory sections.

**Results — book.md → kn.md line counts:**

| Book | book.md | kn.md | Lines removed | Notes |
|------|---------|-------|---------------|-------|
| 03 — Padagala Olarachane | 12,319 | 11,437 | 882 | Sarvam OCR; 653 structural lines deleted |
| 07 vol1 — Sollarime | 24,861 | 20,475 | 4,386 | WX; Ç-fix |
| 07 vol2 — Sollarime | 15,324 | 13,928 | 1,396 | WX; Ç-fix |
| 17 — Nudi Nadedu Banda Dari | 22,312 | 16,883 | 5,429 | WX; ya-fix + Ç-fix + 1,539 zero-Kannada lines removed |
| 25 — Vakyagala Olarachane | 14,485 | 11,676 | 2,809 | WX; word-level fixes + zero-Kannada lines removed |
| 27 — Baasheya Bagge | 9,138 | 8,245 | 893 | Sarvam OCR; 545 structural lines deleted |

**kn-eke.md generation (generic `gen_kn_eke.py`):**

A single generic transliterator replaced the book-28-specific `kn_to_eke.py`. Key fix over earlier stubs: `<td>` and `<th>` table cell content is now transliterated (matched by regex `>[^<]*<` inside HTML lines) rather than passed through verbatim. This eliminated 7,201 residual Kannada chars in book 03's previous stub (book 03 is table-heavy). All 6 books now output 0 residual Kannada characters.

**Commit:** `d8e037a` "Phase 14: OCR cleanup + kn.md + kn-eke.md for books 03, 07, 17, 25, 27" — 12 files (6 new kn.md + 6 kn-eke.md regenerated)

### Phase 15 — Holistic kn-eke.md Audit + Nav Fix + Stale-Eke Regeneration (2026-03-17)

**Motivation:** After Phase 14, a cross-book audit revealed two systemic issues that had been fixed one book at a time in prior commits, and two that hadn't been fixed at all.

**Issue 1 — Nav link hygiene (fixed holistically in commit `4964158`)**

All `kn-eke.md` files had inconsistent nav-link labels. Patterns found and corrected:

| Old pattern | Correct | Books affected |
|-------------|---------|----------------|
| `[ಕನ್ನಡ →]` (hybrid Eke in Kannada label) | `[ಕನ್ನಡ →]` | 02, 07, 14, 18, 27, 29 |
| `[ingliS →]` (Eke romanisation of "English") | `[English →]` | 02, 14 |
| `[English →] \| [Eke →](kn-eke#...)` (self-referential) | `[ಕನ್ನಡ →](kn#adhyAya-N) \| [English →](en#...)` | 03, 17, 25, 28 |

Total: 12 files, 18,746 insertions across the single holistic commit.

**Issue 2 — Book 07 OCR page headers/footers (fixed in commit `98c2c7e`)**

After Phase 14 cleaned `vol1-kn.md` and `vol2-kn.md`, the corresponding `kn-eke.md` files were still stale — generated from the uncleaned source. Transliterated page headers remained:

| File | Lines before | Lines after | Pattern removed |
|------|-------------|-------------|-----------------|
| `vol1-kn.md` | 20,475 | 20,185 | `N / kannaDa barahada sollarime`, garbled M¼À |
| `vol2-kn.md` | 13,928 | 13,333 | copyright line, `N / kannaDa barahada sollarime`, chapter headers |

**Issue 3 — Book 07 kn-eke.md files stale after OCR cleanup (fixed in this phase)**

The `vol1-kn-eke.md` (20,473 lines) and `vol2-kn-eke.md` (13,929 lines) were regenerated from the Phase 14 uncleaned kn.md — before the header/footer removal. After removing those artifacts from kn.md, the kn-eke.md files still contained their transliterated equivalents:

- `4 / kannaDa barahada sollarime` — page headers from left-page running headers
- Copyright line in Eke form
- Section separators from chapter titles printed at top of print pages

Fix: Regenerate both from the cleaned kn.md using `gen_kn_eke.py`.

**Issue 4 — Book 02 kn-eke.md was hand-authored summaries, not verbatim Eke (fixed in this phase)**

The earliest `kn-eke.md` in the collection (book 02, *Kannadalle Hosapadagalannu Kattuva Bage*) was written manually as a companion document with explanatory Eke text — not a verbatim transliteration of `kn.md`. At sections like `sec-4-4`, the kn-eke.md had analytical explanation ("esaka padakkE -ka oTTannu sErisi upakaraNavannu hesarisuvA...") while kn.md had verbatim Kannada word lists and body text. The file was 835 lines vs kn.md's 553 lines (52% larger — expanded by hand-authored explanations).

Fix: Regenerate from `kn.md` using `gen_kn_eke.py`, replacing hand-authored content with verbatim Eke.

**Regenerations in this phase (all via `gen_kn_eke.py`, 0 residual Kannada chars):**

| File | Old lines | New lines | Source | Reduction |
|------|-----------|-----------|--------|-----------|
| `02-...-kn-eke.md` | 835 (hand-authored) | 491 (verbatim) | `02-...-kn.md` (553L) | −344 (removed summaries) |
| `07-...-vol1-kn-eke.md` | 20,473 (stale) | 20,183 (clean) | `07-...-vol1-kn.md` (20,185L) | −290 (removed page headers) |
| `07-...-vol2-kn-eke.md` | 13,929 (stale) | 13,331 (clean) | `07-...-vol2-kn.md` (13,333L) | −598 (removed page headers/footers) |

**Known residual:** `07-...-vol1-kn.md` line 11206 has `(4) M¼À:` — a garbled WX-encoded list entry (1 occurrence). Requires original PDF to determine correct Kannada. All other character-level cleanup is complete.

**Commit:** `fix(02,07): regenerate kn-eke.md verbatim — drop hand-authored summaries and stale page headers`

---

### Phase 16 — Cross-Link Audit + Nav Transformation Fix (2026-03-17)

**Motivation:** After adding cross-links to kn.md files in prior phases, two systemic issues remained:
1. `kn.md` cross-links used wrong label (`[ingliS →]` — Eke romanisation of "English" — instead of `[English →]`)
2. `gen_kn_eke.py` passed `[English →] | [Eke →]` nav lines through verbatim, so regenerated `kn-eke.md` files had self-referential `[Eke →]` links pointing at themselves
3. `02-kn.md` had zero cross-links (the user reported `#ch2` had no navigation to English or Eke)

**Audit of all kn.md files for cross-links:**

| Book | [English →] links | [ingliS →] links | Status |
|------|-------------------|------------------|--------|
| 02 | 0 | 0 | ❌ Missing — added 60 |
| 03 | 9 (1/chapter) | 0 | ✅ |
| 07 vol1 | 4 (1/chapter) | 0 | ✅ |
| 07 vol2 | 2 (1/chapter) | 0 | ✅ |
| 08 | 38 (1/section) | 0 | ✅ |
| 14 | 0 | 82 | ❌ Wrong label — renamed to [English →] |
| 17 | 12 | 0 | ✅ |
| 25 | 11 | 0 | ✅ |
| 27 | 5 | 0 | ✅ |
| 28 | 12 (1/chapter) | 0 | ✅ |
| 29 | 11 (1/chapter) | 0 | ✅ |

**Fix 1 — Book 14 kn.md: rename `[ingliS →]` → `[English →]`** (82 occurrences; kn-eke.md already correct, not regenerated)

**Fix 2 — `gen_kn_eke.py`: proper nav-link transformation**

Previously: `[English →](en) | [Eke →](kn-eke)` was passed through verbatim into kn-eke.md — creating self-referential Eke links.

Now: when generating kn-eke.md, these lines are transformed to the correct perspective:
```
[English →](./book-en#en-anchor) | [Eke →](./book-kn-eke#sec-id)
  ↓  (in kn-eke.md)
[ಕನ್ನಡ →](./book-kn#sec-id) | [English →](./book-en#en-anchor)
```
The kn URL is derived by stripping `-eke` from the Eke filename in the `[Eke →]` link.

**Fix 3 — Book 02 kn.md: 60 cross-links added** (every chapter + section anchor)

Anchor-to-English-anchor mapping (30 unique chapters/sections):
- ch1, sec-1-[1-3] → `part-1--philosophy-and-core-principles`
- ch2, sec-2-[1-3] → `part-2--framework-overview`
- ch3, sec-3-[1-2] → `part-3--adjective-to-noun--ತನ`
- ch4, sec-4-[1-6] → `parts-45--verb-to-noun`
- ch6, sec-6-1 → `part-6--zero-derivation`
- ch7, sec-7-[1-3] → `part-7--noun-to-noun`
- ch8-ch11, ch13-ch14, ch18-ch19, ch29-36, ch37-52 (and their sections) → most specific en.md anchor

**Regenerations:**

| File | Old lines | New lines | Change |
|------|-----------|-----------|--------|
| `02-...-kn-eke.md` | 491 (no nav) | 611 (with nav) | +60 nav links; correct `[ಕನ್ನಡ →]` format |
| `07-...-vol1-kn-eke.md` | 20,183 | 20,183 | Nav fixed: `[English →]\|[Eke →]` → `[ಕನ್ನಡ →]\|[English →]` |
| `07-...-vol2-kn-eke.md` | 13,331 | 13,331 | Same nav fix |

**Verbatim content audit (all kn-eke.md files):** All 11 books confirmed verbatim — non-empty line counts match kn.md exactly.

**Commit:** `fix(02,14): add kn.md cross-links, fix ingliS→English, fix kn-eke nav transformation`

---

### Phase 17 — Nudi Encoding Cleanup, u' → u^, TOC Restructure, Citation Quote Convention (2026-03-18–19)

Multi-part phase completing Nudi/WX glyph-map artifact cleanup, fixing the unrounded-u Eke marker, restructuring TOCs, removing residual OCR structural artifacts, and establishing a canonical citation-quote convention for the published site.

**Sub-phase A — Nudi character-level cleanup (books 17 and 14)**

Books 17 and 14 were typeset in Nudi legacy font. WX-decoding produced Kannada Unicode text but left unmapped Latin glyph-map residuals that required cross-referencing the original PDF.

*Book 17 — symbols resolved:*

| Symbol | U+ | → | Replacement | Count | Context |
|--------|----|---|-------------|-------|---------|
| `ù` | 00F9 | → | ಱ (archaic RA, U+0CB1) | 85 | vowel-displacement pattern |
| `Â` | 00C2 | → | `ᵒ` (modifier letter small o, U+1D52) | 24 | Havyaka suffix marker |
| `ï` | 00EF | → | ್ (virama, U+0CCD) | 7 | unrounded-u context |
| `û` | 00FB | → | ಼ (nukta, U+0CBC) | 3 | — |
| `Ð` | 00D0 | → | direct reconstructions | 2 | two Tamil loanwords: ಞೆಙ್ಙೋಳ್, ಞಙ್ಙು |
| `Œ` | 0152 | → | char + ಼ (nukta) | 21 | lowered vowels (ಅ಼, ಎ಼, ಒ಼) — pattern A prefix and B infix |

Additional compound OCR garbles fixed: `ಯುೀ → ಯೇ` (75×), `ೊೀ → ೋ` (37×), `ೂೀ → ೋ` (3×), `ದುು → ದು` (1×).

New Eke rules for book 17's archaic symbols: ಱ → `R/Ra`, ೞ → `Z/Za`, ಙ → `G/Ga`, ಞ → `Y/Ya` (halant/full akshara); ಼ (nukta) → `:` suffix (e.g. ಅ಼ → `a:`); `ᵒ` → pass through as-is; `ಉ್` (unrounded u) → `u^`.

*Book 14 — symbols resolved:*

| Symbol | U+ | Replacement | Count | Context |
|--------|----|-------------|-------|---------|
| `«` | 00AB | `<` | 16 | etymological source arrow (§4.6) |
| `»` | 00BB | `>` (4×) / `,` (7×) | 11 | word-change notation / clause joins |
| `¢` | 00A2 | vowel extender | 1 | `ಮಧ್ಯದಲ್ಲೆ ¢ → ಮಧ್ಯದಲ್ಲೇ` |
| `£` | 00A3 | `,` | 1 | clause join (§12.2) |
| `©` | 00A9 | deleted | 1 | page-break artifact block (§9.1 running header) |
| `(ಆಕ)` | — | `(೮ಕ)` | 1 | OCR misread of Kannada digit ೮ |

**Sub-phase B — Eke u' → u^ fix (2026-03-18)**

All 8 existing kn-eke.md files (03, 07-vol1, 07-vol2, 14, 17, 25, 27, 28) regenerated with `u^` (caret) for the unrounded-u vowel `ಉ್`, replacing the earlier `u'` (apostrophe). Reason: apostrophe caused rendering ambiguity in citation-quote contexts and Markdown processors. Book 27 and 29 re-regenerated again after the fragment cleanup below. Commit: `9a9b8fe`.

**Sub-phase C — OCR structural artifact removal**

| Commit | Books | What was removed |
|--------|-------|-----------------|
| `dc21662` | 27, 28, 29 | Per-page running chapter headers embedded in body text |
| `66a7c62` | 27 | Page-break orphaned fragments before section headings |
| `61d2f36` | 29 | Page-split sentence fragment rejoined to its paragraph |
| `5412429` | 08 | Page-break orphaned fragment lines (3 instances) |
| `6b072f1` | 03 | Stray `ಚ` page-break fragment isolated before a section heading |
| `949ed17` | 25 | Entire OCR'd anukaraNike (preface) block removed from body (202 lines) — preface had been OCR'd twice, appearing a second time mid-body |

**Sub-phase D — TOC restructure (all kn.md files)**

All books with kn.md now have a clean ಒಳಪಿಡಿ/ಪರಿವಿಡಿ section with `<a id>` anchors and section-link tables. Books 03 and 27 received new full TOCs in this phase; other books were already clean.

| Book | TOC header | Anchor scheme | Count |
|------|-----------|--------------|-------|
| 03 | `## ಒಳಪಿಡಿ` | `sec-N-M`, `sec-N-M-P` | 100 sections, 3 levels |
| 07 | `## ಒಳಪಿಡಿ` | `adhyAya-N` | 4 (vol1) + 2 (vol2) |
| 08 | `## ಒಳಪಿಡಿ` | mixed | 38 |
| 14 | `## ಒಳಪಿಡಿ` | mixed | 164 |
| 17 | `## ಪರಿವಿಡಿ` | `adhyAya-N` | 12 |
| 25 | `## ಪರಿವಿಡಿ` | `adhyAya-N` | 11 |
| 27 | `## ಒಳಪಿಡಿ` | `part-N`, `sec-N-M`, `sub-N-M-K` | 221 (5+32+184) |
| 28 | `## ಪರಿವಿಡಿ` | `adhyAya-N` | 12 |
| 29 | `## ಪರಿವಿಡಿ` | `adhyAya-N` | 11 |

Commits: `20bb002` (book 03 — new full 3-level TOC), `ad6be57` (book 27 — new 3-tier TOC with 221 anchors).

**Sub-phase E — Citation quote convention (books 07, 17, 25, 28)**

DNS Bhat's books were typeset with backtick (U+0060) as typographic open-quote and apostrophe (U+0027 or U+2019) as close. Backtick triggers Markdown code-span rendering on the published site.

**Decision:** Replace with curly single quotes `'word'` (U+2018 open / U+2019 close) — the convention already used natively in books 03 and 27 (Sarvam OCR output). The vowel-modification marker `u^` (unrounded-u in Eke) is explicitly **not** a citation quote and is left unchanged.

Close-char per book: U+0027 (ASCII apostrophe) for books 07, 25, 28; U+2019 (right single quotation mark) for book 17.

Implementation: retrieved `HEAD^:{path}` via git to get pre-intermediate-commit state, then applied a DOTALL regex (`\`CONTENT'` → `'CONTENT'`, max 300-char span to handle page-break-split citations) with a double-backtick pass first (`\`\`CONTENT''` → `'CONTENT'` for direct speech). Orphaned opens/closes handled case-by-case.

| Book (file pair) | Quotes converted | Notable edge cases |
|-----------------|-----------------|-------------------|
| 07 vol1 kn + eke | ~400 | OCR fix `ನವi್ಮಲ್ಲಿ → ನಮ್ಮಲ್ಲಿ` (+ Eke `navaimalli → nammalli`); double-citation-mark display `(``'')` → `('')`; 1 orphaned-open vocab gloss |
| 07 vol2 kn + eke | ~300 | 1 orphaned open (parallel entry); 1 nested outer backtick; 2 isolated OCR fragment orphans (backtick removed); 1 orphaned close |
| 17 kn + eke | 15 | 4 list-gloss items with OCR-dropped close; 1 bibliography backtick before garbled English title (backtick removed) |
| 25 kn + eke | 4 | 4 double-backtick direct-speech citations; 0 residual backticks after regex |
| 28 kn + eke | ~30 | 3 translation glosses with OCR-dropped close; 1 number-structure example |

Commits: `500a296` (intermediate `^..^` convention — superseded), `971e918` (final curly single quotes — 10 files across 5 books).

**All Nudi Latin artifacts (0x80–0xFF) now cleared** across all kn.md files except `©` (genuine copyright symbol, preserved in books 03 and 27).

---

### Phase 18 — docs/ sync + Noto Sans Kannada + ettuge-sync skill (2026-03-20)

**Root cause fixed:** All 57 `docs/dnsbhat/` files were stale — Phase 17 OCR cleanup and kn.md changes went to `src/` but were never copied to `docs/` (the GitHub Pages source). This caused garbled rendering of books 25, 15, and all other Phase 17-touched books.

**Changes:**
- `docs/dnsbhat/` — synced 57 files from `src/main/md/kannada/dnsbhat/` preserving Jekyll nav front matter (`title`, `parent`, `nav_order`) in each file
- `docs/_sass/custom/custom.scss` — added Noto Sans Kannada via Google Fonts for correct nukta (U+0CBC ಼) rendering; previously Georgia/system fonts silently dropped nukta-modified clusters
- `.claude/skills/ettuge-sync/` — new skill (`ettuge-sync`) automates the full post-phase sync pipeline: staleness detection → CLAUDE.md updates → claude-prompt updates → docs/ sync → global skill copy → regenerate combined docs files → commit and push
- `.claude/skills/ettuge-sync/scripts/sync_docs.py` — standalone script for src→docs sync (Step 4a of ettuge-sync skill)

---

### Phase 19 — Deep 3-Level TOC + Section Anchors (2026-03-20)

**Scope:** All 11 books with kn.md (02, 03, 07-vol1, 07-vol2, 08, 14, 17, 25, 27, 28, 29).

**Changes:**
- Added `<a id="sec-N-M">` anchors at all section headings and `<a id="sub-N-M-K">` at all subsection headings in every kn.md
- ಪರಿವಿಡಿ TOC in each kn.md extended to list all three levels (chapter → section → subsection)
- Cross-links inserted after every sec/sub anchor: `[Eke →](./SLUG-kn-eke#sec-N-M)` in kn.md; `[ಕನ್nnaDa →](./SLUG-kn#sec-N-M)` in kn-eke.md
- Chapter nav fragments corrected to `#adhyAya-N` throughout
- Index back-links added to all kn.md headers: `[← ಸೂಚಿ](./README)` and `[← sUci](./README)` in kn-eke.md
- kn-eke.md self-referential header links corrected (were pointing to wrong file)

---

### Phase 20 — 4-Level Taxonomy Migration (2026-03-20)

**Scope:** All 29 book directories in `src/main/md/kannada/dnsbhat/`.

**Motivation:** The old flat layout (`NN-slug-kn.md`, `NN-slug-en.md`, etc.) mixed all content types in one directory. The new 4-level taxonomy separates by source (book/web/youtube), language (kn/eke/en), and type (full/summary/raw).

**New structure:**
```
NN-slug/
├── README.md              # Book index landing page
├── claude-prompt.md       # AI context primer
├── book/
│   ├── kn/full.md         # Scanned book — structured Kannada (was NN-slug-kn.md)
│   ├── kn/raw.md          # Raw OCR archive (was NN-slug-book.md)
│   ├── eke/full.md        # Eke romanisation (was NN-slug-kn-eke.md)
│   └── en/summary.md      # English chapter summary (was NN-slug-en.md)
├── web/
│   ├── kn/raw.md          # DNS Bhat blog posts (was NN-slug-blog.md)
│   └── en/summary.md      # Blog-based English summary
└── youtube/
    ├── kn/full.md         # Assembled transcript Kannada (was NN-slug.md — nav metadata carrier)
    ├── eke/full.md        # Eke romanisation of transcript
    └── en/summary.md      # YouTube-based English summary
```

**Migration:** 129 `git mv` operations via script. All cross-links in kn.md and kn-eke.md files updated to new relative paths (depth 3: `../eke/full`, `../../README`; depth 4: `../../../README`).

**sync_docs.py rewrite:** `ettuge-sync/scripts/sync_docs.py` rewritten to recursively walk src/ subdirectories and create matching structure in docs/; orphaned flat docs/ files deleted.

---

### Phase 21 — GitHub Pages Nested Sidebar + Bug Fixes (2026-03-20)

**Motivation:** After the taxonomy migration, the GitHub Pages site was broken: 404s throughout, no books showing in sidebar (the old pages.yml Python script used flat paths that no longer existed), and `.md`-suffix links causing 404s.

**Sidebar redesign:** Replaced the flat 3-section sidebar (English Summaries / Kannada Text / Eke Transliteration) with a source-first 3-level hierarchy:
```
▶ Books
    ▶ English        — book/en/summary.md entries
    ▶ Kannada Text   — book/kn/full.md entries
    ▶ Eke Transliteration — book/eke/full.md entries
▶ Blog
    ▶ Kannada Text   — web/kn/full.md entries
    …
▶ YouTube
    ▶ English        — youtube/en/summary.md entries
    ▶ Kannada Text   — youtube/kn/full.md entries
    …
```
Each content file gets `parent: "Kannada Text"` + `grand_parent: "Books"` (etc.) using just-the-docs 3-level nesting. Sections only created when content exists.

**pages.yml Python script** completely rewritten in 6-pass architecture:
1. Gather book metadata from `youtube/kn/full.md` + find content files via CANDIDATES dict
2. Create source section pages (`book.md`, `web.md`, `youtube.md`)
3. Create language sub-section pages (`book-en.md`, `book-kn.md`, etc.)
4. Write `parent`/`grand_parent` front matter to all content files
5. Write book landing pages as `index.md` (so `/NN-slug/` directory URL resolves)
6. Mark all other `.md` files `nav_exclude: true`

**Bug fixes:**
- `docs/_config.yml`: removed `jekyll-relative-links` plugin (frozen Gemfile.lock); removed orphaned `collections:` + `just_the_docs: collections:` blocks (were rendering a floating "DNS Bhat" label in sidebar)
- `docs/Gemfile`: removed `jekyll-relative-links` gem
- Books 14, 27, 28, 29 `youtube/kn/full.md`: fixed broken cross-links `../en/summary` → `../../book/en/summary` and `../eke/full` → `../../book/eke/full` (youtube/ has no en/eke content for these books)
- Book landing pages now written as `index.md` so directory URLs like `/dnsbhat/28-kannaDakke-bEku/` resolve correctly

---

### Phase 22 — YouTube Transcript Restructuring: Paragraph Breaks + Chapter TOC (2026-03-21)

**Scope:** Books 01–13 (YouTube-only lecture series — no scanned book text).

**Motivation:** All `youtube/kn/full.md` files for books 01–13 contained raw ASR transcripts as flat single-paragraph blobs under `## Part N` headers, with no visual separation between parts, no anchor links, and no chapter grouping. The files were unreadable as reference material.

**Changes (script: `/tmp/structure_v2.py`):**
- `## Part N` headers demoted to `### Part N` (to nest under chapter `##` headings)
- `<a id="part-N">` anchor inserted before every Part
- ASR transcript blobs split into ~80-word paragraphs for readability
- Lines with < 40% Kannada characters replaced with `> *[ಈ ಭಾಗದ ಭಾಷಾಂತರ ಲಭ್ಯವಿಲ್ಲ — transcript not available for this part]*`
- `[Watch on YouTube](URL)` link inserted into each Part from the Table of Contents
- ಪರಿವಿಡಿ TOC added at the top of each file linking to `#part-N` anchors
- **Book 03** additionally restructured with 9-chapter grouping (`## ಅಧ್ಯಾಯ N` headings with `<a id="adhyAya-N">` anchors) per the book's chapter structure

**Books processed:**
- Flat (no chapters): 01, 06, 07, 08, 10, 11, 12, 13
- Chapter-mapped: 03 (9 chapters, Parts 1–55)
- Earlier partial restructuring (separate commits): 02, 04, 05, 09

**Commits:** `304fc93`, `ad1b267`, `0c9f7b9`

---

### Phase 23 — Blog Sidebar Fix + Stubs Category + YouTube Transcript Cross-References (2026-03-21)

**Motivation:** Three separate improvements triggered by an audit of which YouTube transcripts could be enriched using existing high-quality sources (book/kn/full.md or web/kn/raw.md).

#### 23a — Blog sidebar fallback fix

`CANDIDATES[('web', 'kn')]` in `pages.yml` was `['web/kn/full.md']` only. Books 14 and 18, which have `web/kn/raw.md` but no `full.md`, were missing from the Blog Kannada sidebar. Added `'web/kn/raw.md'` as a fallback candidate.

**Commit:** `7678364`

#### 23b — Stubs sidebar category

16 of 29 books have `youtube/kn/full.md` files that are placeholder stubs (no `## Part` or `### Part` headers — just a description or link list). These were cluttering the YouTube sidebar.

Added a **Stubs** top-level sidebar section (`nav_order: 40`) with automatic reclassification: the `is_youtube_stub()` helper in `pages.yml` detects stub files and moves them from `('youtube', 'kn')` to `('stub', 'kn')` in Pass 1, dropping their associated YouTube `en`/`eke` entries. A dedicated `Stubs` section renders them separately.

**Commit:** `33d0247`

#### 23c — YouTube transcript cross-references (Books 02 and 03)

**Observation:** Books 02 and 03 have both a YouTube transcript file and a high-quality Kannada source (web blog for Book 02, scanned book for Book 03). Keyword-overlap analysis (TF-IDF-style, 5+ char Kannada words, overlap score ratio) identified which YouTube Parts correspond to which source sections.

**Approach chosen:** Rather than copying full source text inline (which duplicates content and inflates the YouTube file), each matched Part gets a **link + 60-word excerpt** pointing to the canonical source section:

```markdown
*ಈ ಭಾಗ ಪುಸ್ತಕದ [೧.೫: ಪದದೊಟ್ಟುಗಳು ಮತ್ತು ಪದರಪದೊಟ್ಟುಗಳು](../../book/kn/full#sec-1-5) ಅನ್ನು ಆಧರಿಸಿದೆ.*

> ನುಡಿಗಳಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ ಎರಡು ಬಗೆಯ ಒಟ್ಟುಗಳು ಬಳಕೆಯಲ್ಲಿರುತ್ತವೆ:…
```

Links use the `#sec-N-M` / `#sub-N-M-K` anchors added in Phase 19.

**Results:**
- Book 02: 10 Parts (24, 26–30, 39–42) linked to `web/kn/raw.md` blog sections (ಭಾಗ 4–10)
- Book 03: 33 of 55 Parts linked to `book/kn/full.md` sections using precise `sec-N-M` anchors; 22 Parts retained ASR (ambiguous overlap, ratio < 1.4×)

**File sizes after:** Book 02 youtube/kn/full.md: 1,342 lines; Book 03: 1,424 lines (vs 4K–6K if full text had been copied inline).

**Scripts:** `/tmp/link_substitute_02.py`, `/tmp/link_substitute_03.py`

**Commits:** `cb466d7` (reverted), `d5d82cf` (reverted), `4678d9f` (final link+excerpt approach)

---

## Eke Romanisation System

**Ellara KannaDa (Eke)** is a romanisation of Kannada devised by Vishwas — inspired by HK protocol and DNS Bhat's ideas, designed to be learnable by any Indian and usable by non-Kannada readers. It is the romanisation used throughout the `-kn-eke.md` files.

### Core Rules

| Feature | Convention | Examples |
|---------|-----------|---------|
| Short vowels | lowercase | a i u e o |
| Long vowels | UPPERCASE | A I U E O |
| Aspirates preserved | ಭ→bh, ಧ→dh, ಖ→kh, ಥ→th, ಫ→ph | bhAShe, adhyayana |
| Retroflexes | UPPERCASE consonant | T D N L (ಟ ಡ ಣ ಳ) |
| ಶ | S | viSwAsa |
| ಷ | Sh | santOSha |
| ಹ | h | hesaru |
| Anusvara assimilation | context-sensitive nasal — **never M** | ಂಕ→nk, ಂಗ→ng, ಂತ→nt, ಂದ→nd, ಂಪ→mp, ಂಬ→mb |
| N | **exclusively ಣ** (retroflex nasal) — never anusvara | kaNNu, maNNu |
| r vs R | lowercase `r` = ರ; uppercase `R` = ಱ (archaic, rare) | `hesaru`, `nuDi` — never `hesaRu` |
| ಋ / ೃ | `x` (short vocalic ṛ) | `samskxta`, `sxSTi`, `dxSTi` |
| ೠ / ೄ | `X` (long vocalic ṝ, extremely rare) | — |

### Key Terminology in Eke

| Kannada | Eke | English |
|---------|-----|---------|
| ಹೆಸರು ಪದ | hesaru pada | noun |
| ಎಸಕ ಪದ | esaka pada | verb |
| ಪರಿಚೆ ಪದ | parice pada | adjective/qualifier |
| ಸೊಲ್ಲರಿಮೆ | sollarime | grammar |
| ನುಡಿಯರಿಮೆ | nuDiyarime | linguistics |
| ಉಲಿ | uLi | phoneme/sound |
| ಬರಿಗೆ | barige | letter/grapheme |
| ಒಟ್ಟು | oTTu | affix |
| ಮುನ್ನೊಟ್ಟು | munnoTTu | prefix |
| ಜೋಡುಪದ | jODupada | compound word |
| ಕೀಳರಿಮೆ | kILarime | inferiority complex |
| ಮೇಲರಿಮೆ | mElarime | superiority complex |
| ಎಲ್ಲರ ಕನ್ನಡ | ellara kannaDa | everyone's Kannada (Eke) |
| ಹೊಸ ಬರಹ | hosa baraha | new orthography (no mahapranas) |
| ಸೇರಿಕೆ | serike | sandhi |
| ವಿಭಕ್ತಿಪಲ್ಲಟ | vibaktipaLLaTa | case alternation |

---

## Current File Status (2026-03-20)

### ✅ Fully processed (en.md + kn-eke.md + claude-prompt.md)

| Book | Files present |
|------|--------------|
| 02 — Hosapadagalannu Kattuva Bage | book-website + blog + kn + kn-eke + en + claude-prompt |
| 03 — Padagala Olarachane | book + **kn** (OCR-cleaned, 11,437L) + kn-eke + en + claude-prompt |
| 04 — Mathu Matthu Barahada Gondala | transcript + website + kn-eke + en + claude-prompt |
| 05 — Mathina Olaguttu | transcript + website + kn-eke + en + claude-prompt |
| 07 — Kannadada Sollarime | vol1-book + **vol1-kn** (20,475L) + vol2-book + **vol2-kn** (13,928L) + kn-eke + en + claude-prompt; citation quotes → curly ✅; Nudi-clean ✅ |
| 08 — Mahaprana Yake Beda | book + djvu + kn + kn-eke + en + claude-prompt |
| 09 — Havyaka Kannada | transcript + website + kn-eke + en + claude-prompt |
| 14 — Nijakku Halegannada | book + djvu + blog + kn + kn-eke + en + claude-prompt; Nudi-clean ✅ |
| 15 — Inglish Kannada Padanerake | book (53p sample) + kn-eke + en + claude-prompt |
| 17 — Nudi Nadedu Banda Dari | book + **kn** (OCR-cleaned, 16,883L) + kn-eke + en + claude-prompt; Nudi-clean ✅; citation quotes → curly ✅ |
| 18 — Nudiya Bagege Chintane | blog + kn-eke + en + claude-prompt |
| 20 — Havyaka Outline Grammar | djvu + en + claude-prompt |
| 25 — Vakyagala Olarachane | book + **kn** (OCR-cleaned, 11,676L) + kn-eke + en + claude-prompt; citation quotes → curly ✅; anukaraNike removed from body ✅ |
| 27 — Baasheya Bagge | book + **kn** (OCR-cleaned, 8,245L) + kn-eke + en + claude-prompt |
| 28 — Kannadakke Beku | book + **kn** (OCR-cleaned, 9,517L) + kn-eke + en (13 anchors) + claude-prompt; citation quotes → curly ✅ |
| 29 — Kannada Vyakarana Yaake Beku | book + **kn** (OCR-cleaned, 11 ch. anchors) + kn-eke + en (12 anchors) + claude-prompt |

### ❌ Not yet processed — no PDF source available

Books 01, 06, 10, 11, 12, 13 — YouTube transcripts only, too corrupted/short for full processing.

### ❌ PDFs exist in Google Drive but text not yet extracted

| Book | PDF | Pages | Notes |
|------|-----|-------|-------|
| 19 — The Koraga Language | `the-koraga-language.pdf` | 123 | English; Unicode-safe — needs pdftotext or OCR |
| 21 — Pronouns (Oxford) | `DNS-Bhat-Pronouns-Oxford.pdf` | ~296 | English; likely Unicode-safe |

### ❌ Not yet collected (website offline / blocked / unarchived)

Books 16, 22, 23, 24, 26 — website stubs only.

---

## Pending Work

### High priority

| Task | Books | What's needed |
|------|-------|---------------|
| Extract Book 19 PDF | 19 | The Koraga Language — pdftotext or Sarvam OCR; create en.md + claude-prompt.md |
| Extract Book 21 PDF | 21 | Pronouns (Oxford) — likely Unicode PDF; create en.md + claude-prompt.md |
| Sync docs/ after every phase (run sync_docs.py) | all | `docs/dnsbhat/` is served by GitHub Pages but edits go to `src/main/md/kannada/dnsbhat/`. After any OCR or kn.md changes, run `python3 .claude/skills/ettuge-sync/scripts/sync_docs.py` to sync src→docs preserving Jekyll nav front matter. Already handled by the `ettuge-sync` skill (Step 4a). |
| Fix OCR word-boundary splits | multiple | Words like `meccuge ay` should be `meccugAy` — OCR split at vowel boundaries. Audit all kn-eke.md files for space-separated suffix artifacts. |
| Verify cross-links kn → en → eke | all books with kn.md | Now that en.md files have detailed per-section anchors (Phase 16–17), the `[English →]` links in kn.md and the `[ಕನ್nnaDa →]` links in kn-eke.md need a full audit pass to ensure every anchor target resolves correctly. |
| Update Skills and CLAUDE.md files | — | `.claude/skills/kannada-ocr-cleaner/SKILL.md`, `dns-bhat-book-summarizer/SKILL.md`, `dns-bhat-transcript-summarizer/SKILL.md`, and relevant `CLAUDE.md` files need updating with Phase 17 learnings: nukta symbol (U+0CBC ಼) + Eke `:` suffix rule, archaic RA (ಱ→R), ೞ→Z, ಙ→G, ಞ→Y, Havyaka suffix `ᵒ`, unrounded-u `u^`, curly quote convention, Nudi Latin artifact table. |
| Expand ettuge home page Eke description | site | [https://vwulf.github.io/ettuge/](https://vwulf.github.io/ettuge/) home page needs a richer Eke description: cover extensions for Havyaka phonemes (ಱ `R`, `ᵒ` suffix, unrounded-u `u^`), lowered vowels (nukta + `:` suffix), archaic stops (ೞ `Z`), and the overall design philosophy (no aspirate loss in *transcription*, aspirate loss only in *word coining*). |
| Deep TOC: chapter.section.subsection anchors | 07, 08, 14, 17, 25, 27, 28, 29, 03 | Current kn.md files only have top-level `adhyAya-N` anchors. The OCR'd book TOCs contain full `N.M` and `N.M.K` section hierarchies (e.g. [book 28](https://vwulf.github.io/ettuge/dnsbhat/28-kannaDakke-bEku/28-kannaDakke-bEku-kn.html)). Each book's OCR TOC needs to be read, the `N.M` / `N.M.K` section headings identified in the body, `<a id="sec-N-M">` / `<a id="sub-N-M-K">` anchors inserted, and the ಒಳಪಿಡಿ/ಪರಿವಿಡಿ block rebuilt with full three-level link tables. Book 03 already has this (Phase 17); all others need the same treatment. |
| Chapter + section headings not marked as Markdown headings | 17, 25, 28, 29 and others | Chapter titles (e.g. `ಅಧ್ಯಾಯ ಒಂಬತ್ತು`) and numbered section headings (e.g. `9.1 ಪೀಠಿಕೆ`) are plain text in the OCR output — not `##`/`###` Markdown headings. This makes entire chapters render as one flat unbroken text block ([example: book 25 adhyAya-9](https://vwulf.github.io/ettuge/dnsbhat/25-kannaDa-vAkyagaLa-oLaracane/25-kannaDa-vAkyagaLa-oLaracane-kn.html#adhyAya-9)). Each kn.md needs a pass that: (a) converts `ಅಧ್ಯಾಯ N` header lines to `## N. ಶೀರ್ಷಿಕೆ`, (b) converts `N.M ...` body lines that are section headings to `### N.M ...`, (c) adds blank lines between paragraphs. Requires PDF cross-reference to identify heading vs. body lines. |
| Split-sentence / word-per-line OCR artifact | 17 and others | In some sections the OCR placed each line of a narrowly-typeset (2-column) page as its own separate line with no blank lines between them. Markdown collapses these into one long run-together paragraph. Example from [book 17](https://vwulf.github.io/ettuge/dnsbhat/17-kannaDa-nuDi-naDeDu-banda-dAri/17-kannaDa-nuDi-naDeDu-banda-dAri-kn.html): `ಕನ್ನಡದಲ್ಲಿ` / `ಇಂತಹ` / `ಸಂದರ್ಬಗಳಲ್ಲಿ` / `ಕನ್ನಡ ವಿದ್ವಾಂಸರು` / `ಸಂಸ್ಕ್ರುತದ ಮೊರೆಹೊಗುತ್ತಾರೆ.` should be one sentence. Fix strategy: detect runs of short (< ~60 char) non-blank lines that don't end in sentence-final punctuation (`। . ? !`), join them. Requires PDF review to calibrate thresholds per book. |
| Book 15 dictionary entry boundaries | 15 | The [book 15 book.md page](https://vwulf.github.io/ettuge/dnsbhat/15-ingliS-kannaDa-padanerake/15-ingliS-kannaDa-padanerake-book.html) renders dictionary headwords and their Kannada equivalents running together — each dictionary entry should be on its own visually distinct line/block, but the WX-decoded OCR has no blank lines between entries. Fix: identify entry boundaries (English headword lines) and insert blank lines before each. |

### Medium priority

| Task | Notes |
|------|-------|
| Collect missing blog posts | Books 02 (parts 1–3), 18 (many parts) — check more Wayback snapshots |
| Book 26 — Uli Marpadina Geregalu | Cloudflare-blocked; try different snapshots or direct Google Cache |
| Books 16, 22, 23, 24 | Not yet collected; website stubs only |
| Sollarime vol.3–7 | Only vol.1+2 PDFs found; vols 3–7 may be at dnshankarabhat.net (offline) |

### Low priority / stretch

| Task | Notes |
|------|-------|
| Retroflexion 1973 paper | Stanford Working Papers; should be in archive.org |
| Cambridge Dravidian Languages chapter | DNS Bhat contributed to Cambridge Language Surveys |

---

## File Structure Summary

```
dnsbhat/
├── README.md                         # Master catalogue — 29 books, annotated
├── PROJECT-RECAP.md                  # This file
├── dns-bhat-analysis.md              # Early analysis document
├── kannada-content-landscape.md      # Content survey
├── kannada-knowledge-gap-analysis.md # Gap analysis
├── swadesh-bhat-prompt-and-analysis.md
├── wiktionary-cost-analysis-kimi-k2.5.md
│
├── 02-kannaDadalle-hosapadagaLannu-kaTTuva-bage/
│   ├── 02-...-blog.md                # 15 blog posts
│   ├── 02-...-kn.md                  # ★ Structured Kannada (547 lines)
│   ├── 02-...-kn-eke.md              # ★ Eke romanisation (830 lines, 43KB)
│   ├── 02-...-en.md                  # ★ English summaries
│   └── 02-...-claude-prompt.md       # ★ AI primer
├── 03-kannaDa-padagaLa-oLaracane/
│   ├── 03-...-book.md                # ★ Sarvam OCR output (239 pages)
│   ├── 03-...-kn.md                  # ★ OCR-cleaned Kannada (11,437L; structural artifact removal)
│   ├── 03-...-kn-eke.md              # ★ Eke romanisation (0 residual Kannada chars)
│   ├── 03-...-en.md                  # ★ English summaries
│   └── 03-...-claude-prompt.md       # ★ AI primer
├── 04-mAtu-mattu-barahada-naDuvina-gondala/
│   ├── 04-....md                     # YouTube transcript (~519 lines, 25/44 parts)
│   ├── 04-...-website.md             # Author's website stub
│   ├── 04-...-kn-eke.md              # ★ Eke romanisation of key passages
│   ├── 04-...-en.md                  # ★ English thematic summary (7 themes)
│   └── 04-...-claude-prompt.md       # ★ AI primer
├── 05-mAtina-oLaguTTu/
│   ├── 05-....md                     # YouTube transcript (~539 lines, 27/37 parts)
│   ├── 05-...-website.md             # Author's website stub
│   ├── 05-...-kn-eke.md              # ★ Eke romanisation of key passages
│   ├── 05-...-en.md                  # ★ English thematic summary (8 themes)
│   └── 05-...-claude-prompt.md       # ★ AI primer
├── 09-havyaka-kannaDa/
│   ├── 09-....md                     # YouTube transcript (~387 lines, 72/88 slots)
│   ├── 09-...-website.md             # Author's website stub
│   ├── 09-...-kn-eke.md              # ★ Eke romanisation of key passages
│   ├── 09-...-en.md                  # ★ English thematic summary (5 themes)
│   └── 09-...-claude-prompt.md       # ★ AI primer
├── 07-kannaDa-barahada-sollarime/
│   ├── 07-...-vol1-book.md           # ★ Sarvam OCR (327 pages)
│   ├── 07-...-vol1-kn.md             # ★ OCR-cleaned Kannada vol1 (20,475L; Ç-fix + arka-ottu)
│   ├── 07-...-vol2-book.md           # ★ Sarvam OCR (301 pages)
│   ├── 07-...-vol2-kn.md             # ★ OCR-cleaned Kannada vol2 (13,928L; Ç-fix + arka-ottu)
│   ├── 07-...-kn-eke.md              # ★ Eke romanisation (9KB)
│   ├── 07-...-en.md                  # ★ English summaries (41KB)
│   └── 07-...-claude-prompt.md       # ★ AI primer (18KB)
├── 08-kannaDakke-mahAprANa-yAke-bEDa/
│   ├── 08-...-book.md                # Full text (archive.org)
│   ├── 08-...-djvu.md                # DjVu OCR
│   ├── 08-...-kn.md                  # ★ Structured Kannada
│   ├── 08-...-kn-eke.md              # ★ Eke romanisation (template book)
│   ├── 08-...-en.md                  # ★ English analysis
│   └── 08-...-claude-prompt.md       # ★ AI primer
├── 14-nijakkU-haLegannaDa-vyAkaraNa-entahadu/
│   ├── nijakku-...-book.md           # Full text (archive.org)
│   ├── 14-...-djvu.md                # DjVu OCR
│   ├── 14-...-blog.md                # 7 blog posts
│   ├── 14-...-kn.md                  # ★ Structured Kannada
│   ├── 14-...-kn-eke.md              # ★ Eke romanisation
│   ├── 14-...-en.md                  # ★ English summary
│   └── 14-...-claude-prompt.md       # ★ AI primer
├── 15-ingliS-kannaDa-padanerake/
│   ├── 15-...-book.md                # ★ Hybrid extraction (53p sample, A–Az)
│   ├── 15-...-kn-eke.md              # ★ Eke romanisation of source text (munnuDi + conventions + A–Az entries)
│   ├── 15-...-en.md                  # ★ English analysis (10 word-formation patterns)
│   └── 15-...-claude-prompt.md       # ★ AI primer (decision tree, cluster tables, 100 entries)
├── 17-kannaDa-nuDi-naDeDu-banda-dAri/
│   ├── 17-...-book.md                # ★ Sarvam OCR (405 pages)
│   ├── 17-...-kn.md                  # ★ OCR-cleaned Kannada (16,883L; ya-fix + Ç-fix + 1,539 zero-KN lines removed)
│   ├── 17-...-kn-eke.md              # ★ Eke romanisation (12KB)
│   ├── 17-...-en.md                  # ★ English summaries (35KB)
│   └── 17-...-claude-prompt.md       # ★ AI primer (20KB)
├── 18-kannaDa-nuDiya-bagege-cintane/
│   ├── 18-...-blog.md                # 13 blog posts
│   ├── 18-...-kn-eke.md              # ★ Eke romanisation
│   ├── 18-...-en.md                  # ★ English summaries (29KB)
│   └── 18-...-claude-prompt.md       # ★ AI primer (7KB)
├── 20-havyaka-outline-grammar/
│   ├── 20-...-djvu.md                # Full DjVu text
│   ├── 20-...-en.md                  # ★ English chapter summaries
│   └── 20-...-claude-prompt.md       # ★ AI primer
├── 25-kannaDa-vAkyagaLa-oLaracane/
│   ├── 25-...-book.md                # ★ Sarvam OCR (289 pages)
│   ├── 25-...-kn.md                  # ★ OCR-cleaned Kannada (11,676L; word-level fixes + zero-KN lines)
│   ├── 25-...-kn-eke.md              # ★ Eke romanisation (19KB)
│   ├── 25-...-en.md                  # ★ English summaries (30KB)
│   └── 25-...-claude-prompt.md       # ★ AI primer (25KB)
├── 27-bhASheya-bagge/
│   ├── 27-...-book.md                # ★ Sarvam OCR (208 pages)
│   ├── 27-...-kn.md                  # ★ OCR-cleaned Kannada (8,245L; structural artifact removal)
│   ├── 27-...-kn-eke.md              # ★ Eke romanisation
│   ├── 27-...-en.md                  # ★ English summaries
│   └── 27-...-claude-prompt.md       # ★ AI primer
├── 28-kannaDakke-bEku/
│   ├── 28-...-book.md                # ★ Sarvam OCR (253 pages, raw WX-decoded)
│   ├── 28-...-kn.md                  # ★ OCR-cleaned Kannada (9,517L; 3-pass OCR fixes + structural artifact removal)
│   ├── 28-...-kn-eke.md              # ★ Eke romanisation (regenerated from kn.md)
│   ├── 28-...-en.md                  # ★ English summaries (25KB; 13 chapter anchors added)
│   └── 28-...-claude-prompt.md       # ★ AI primer (20KB)
├── 29-kannaDa-vyAkaraNa-yAke-bEku/
│   ├── 29-...-book.md                # ★ Sarvam OCR (260 pages, raw WX-decoded)
│   ├── 29-...-kn.md                  # ★ OCR-cleaned Kannada (11 chapter anchors)
│   ├── 29-...-kn-eke.md              # ★ Eke romanisation (12KB)
│   ├── 29-...-en.md                  # ★ English summaries (28KB; 12 chapter anchors added)
│   └── 29-...-claude-prompt.md       # ★ AI primer (19KB)
└── [... 11 more folders with website stubs or transcripts ...]
```

★ = created/significantly enriched in this project

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
| **wx_decode.py** | WX→Unicode lookup-table decoder (books 07, 17, 25, 28, 29) |
| **Claude agents** | Parallel book processing (kn-eke, en.md, claude-prompt) |
| **Jekyll / just-the-docs** | Static site generator; format-first sidebar via Python script in CI |
| **GitHub Actions** | Build + deploy pipeline (`.github/workflows/pages.yml`) |
| **ettuge** | Scala/SBT project hosting all MD content; public site at https://vwulf.github.io/ettuge/ |

OCR pipeline location: `ettuge/src/main/python/sarvam-ocr/`

---

## Key Intellectual Themes

### 1. Kannada-native grammar (anti-Sanskrit framework)
Bhat's life work: Kannada has its own grammatical logic. The three base categories are *hesaru pada* (noun), *esaka pada* (verb), *parice pada* (adjective) — not Sanskrit's verb-root primacy. Books 01, 03, 07, 08, 14, 25, 28, 29.

### 2. Script reform (mahaprana / aspirated consonants)
Kannada phonology does not distinguish aspirated from unaspirated stops. The mahaprana letters (ಖ ಘ ಛ ಝ ಠ ಢ ಥ ಧ ಫ ಭ) are Sanskrit imports serving no phonological function. Book 08 makes this argument; books 07, 17, 29 are written in *hosa baraha* (simplified script without mahapranas).

### 3. Word formation without Sanskrit (native Dravidian roots)
Over 50% of standard Kannada vocabulary is Sanskrit-derived; 80% in scientific writing. Books 02 and 15 document systematic native Dravidian word-formation patterns using roots, affixes, and compounds.

### 4. Dialect documentation
Academic description of dialects as data: Havyaka (books 09, 20), Koraga (book 19), Belari (in book 19). These are not "corrupted" dialects but independent systems.

### 5. Sound change as the mechanism of language history
The theoretical underpinning of books 08, 14, 17, 26: sound changes are regular, reconstructable, and explain the Sanskrit/Kannada relationship. Book 22 is the English theoretical monograph; Book 26 is the Kannada popularisation. Book 17 applies historical phonology to trace Kannada from Proto-Dravidian.

### 6. Applied linguistics (why grammar matters)
Books 27, 28, 29 form Bhat's popular advocacy trilogy: *Baasheya Bagge* (intro to linguistics), *Kannadakke Beku* (why Kannada needs its own grammar), *Kannada Vyakarana Yaake Beku* (who needs grammar and why). Together they make the case that correct grammatical description has practical consequences for education, translation, and language planning.
