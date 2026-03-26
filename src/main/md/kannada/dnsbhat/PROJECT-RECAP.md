# DNS Bhat Ettuge Project — Recap
*Last updated: 2026-03-26 (Phase 34, reverse-chronological)*

---

## ಪರಿವಿಡಿ — Contents

| Section | |
|---------|--|
| [What Is This Project?](#ch1) | Overview, About DNS Bhat, Catalogue |
| [Phase History (newest first)](#ch2) | Links to [PROJECT-PHASES.md](./PROJECT-PHASES.md) |
| [Eke Romanisation System](#ch3) | Rules, consonants, vowels |
| [Current File Status](#ch4) | Per-book file inventory |
| [Pending Work](#ch5) | TBD items |
| [File Structure Summary](#ch6) | Directory layout |
| [Tools & Pipeline](#ch7) | OCR, WX decode, CI scripts |
| [Key Intellectual Themes](#ch8) | Research themes |

---

<a id="ch1"></a>

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

## The Catalogue: 33 Known Works

The full registry is in [`README.md`](./README.md). Summary:

| # | Short Title | Language | Key Topic | Text Status | Processed |
|---|-------------|----------|-----------|-------------|-----------|
| 01 | Idu Kannadade Vyakarana | Kn | Native grammar framework | ✅ Transcript | ✅ youtube+en |
| 02 | Hosapadagalannu Kattuva Bage | Kn | Word formation | ✅ Transcript + 15 blog posts | ✅ full |
| 03 | Kannada Padagala Olarachane | Kn | Morphology | ✅ Transcript + OCR | ✅ full |
| 04 | Mathu Matthu Barahada Gondala | Kn | Speech vs. writing | ⚠️ Partial (25/44 parts) | ✅ full |
| 05 | Mathina Olaguttu | Kn | Deep structure of language | ✅ Transcript (27/37 parts) | ✅ full |
| 06 | Kalikenudi Matthu Nudikalike | Kn | Language acquisition | ❌ Corrupted | ✅ youtube+en |
| 07 | Kannada Barahada Sollarime (7 vols) | Kn | Complete grammar of written Kn | ⚠️ OCR vol1–4; vols 5–7 missing | ✅ full |
| 08 | Kannadakke Mahaprana Yake Beda | Kn | Script reform (aspirates) | ✅ Full text | ✅ full |
| 09 | Havyaka Kannada | Kn | Havyaka dialect (popular) | ⚠️ Partial (72/88 slots) | ✅ full |
| 10 | Kannada Nudiya Hinnadavali | Kn | History of Kannada | ⚠️ Corrupted | ✅ youtube+en |
| 11 | Kannada Barahada Padasamasye | Kn | Orthographic problems | ❌ Corrupted | ✅ youtube+en |
| 12 | Kannada Bhasheya Kalpita Charitre | Kn | Reconstructed history | ✅ Short excerpt | ✅ youtube+en |
| 13 | Dharege Doddavaru | Kn | Old Kannada literature | ❌ Corrupted | ✅ youtube+en |
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
| 30 | Kannada Barahavanna Saripadisona | Kn | Practical script reform guide | ✅ Nudi OCR decoded | ✅ full |
| 31 | Ingliš Padagalige Kannadade Padagalu | Kn | English→native Kn dictionary (A–Z) | ✅ Baraha CID decoded (Phase 27) | ✅ raw+en |
| 32 | Prominence of Tense, Aspect and Mood | En | TAM typology (John Benjamins) | ✅ Clean English PDF | ✅ en+prompt |
| 33 | Kannada Sollarime | Kn | General Kn grammar (YouTube) | ✅ Transcript | ✅ youtube+en |

**"Processed" = full** means the book has all four key files: `en.md` + `kn-eke.md` + `claude-prompt.md` (+ `kn.md` where applicable). **"en+prompt"** = English summary + claude-prompt but no kn-eke. **"youtube+en"** = YouTube transcript + English summary. **"raw+en"** = decoded raw.md + English summary (no kn-eke yet).

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

<a id="ch2"></a>

## What Has Been Done

The full phase history (34 phases, ~60 KB) lives in **[PROJECT-PHASES.md](./PROJECT-PHASES.md)**, split by CI into browsable group pages:

| Group | Phases | Key Work |
|-------|--------|----------|
| [Group 1](PROJECT-PHASES/ch1) | 34–28 | CI chapterization, top-nav, GitHub Pages, Grammar section |
| [Group 2](PROJECT-PHASES/ch2) | 27–20 | Book 31 Baraha decode, Book 07 vols 3–4, taxonomy migration |
| [Group 3](PROJECT-PHASES/ch3) | 19–15 | Deep 3-level TOC, Markdown headings, OCR & Eke pipeline |
| [Group 4](PROJECT-PHASES/ch4) | 14–8  | OCR cleanup Books 07–29, English summaries, WX decode |
| [Group 5](PROJECT-PHASES/ch5) | 7–1   | Foundation, initial cataloguing, early pipeline |

<a id="ch3"></a>

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

<a id="ch4"></a>

## Current File Status (2026-03-23)

### ✅ Fully processed (en.md + kn-eke.md + claude-prompt.md)

| Book | Files present |
|------|--------------|
| 02 — Hosapadagalannu Kattuva Bage | book-website + blog + kn + kn-eke + en + claude-prompt |
| 03 — Padagala Olarachane | book + **kn** (OCR-cleaned, 11,437L) + kn-eke + en + claude-prompt |
| 04 — Mathu Matthu Barahada Gondala | transcript + website + kn-eke + en + claude-prompt |
| 05 — Mathina Olaguttu | transcript + website + kn-eke + en + claude-prompt |
| 07 — Kannada Barahada Sollarime | vol1-book + **vol1-kn** (20,475L) + vol2-book + **vol2-kn** (13,928L) + vol3/vol4 raw+full+eke+en + multi-vol index; citation quotes → curly ✅; Nudi-clean ✅ |
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
| 30 — Kannada Barahavanna Saripadisona | book/kn/raw.md + book/kn/full.md (10-ch TOC) + book/eke/full.md + book/en/summary.md + claude-prompt |

### ✅ Partially processed (raw decode done; kn-eke pending)

| Book | Files present | What's missing |
|------|--------------|---------------|
| 31 — Ingliš Padagalige Kannadade Padagalu | book/kn/raw.md + **book/kn/full.md** (12,121 entries, Baraha CID decoded Phase 27) + book/en/summary.md + claude-prompt | book/eke/full.md (Eke for a dictionary is less critical) |

### ✅ YouTube + English summary only

Books 01, 06, 10, 11, 12, 13, 33 — YouTube transcripts + youtube/en/summary.md + claude-prompt. No scanned book text available.

### ✅ English summary + claude-prompt only

| Book | Notes |
|------|-------|
| 32 — Prominence of Tense, Aspect and Mood | English monograph; book/en/summary.md + claude-prompt |

### ❌ PDFs exist in Google Drive but text not yet extracted

| Book | PDF | Pages | Notes |
|------|-----|-------|-------|
| 19 — The Koraga Language | `the-koraga-language.pdf` | 123 | English; Unicode-safe — needs pdftotext or OCR |
| 21 — Pronouns (Oxford) | `DNS-Bhat-Pronouns-Oxford.pdf` | ~296 | English; likely Unicode-safe |

### ❌ Not yet collected (website offline / blocked / unarchived)

Books 16, 22, 23, 24, 26 — website stubs only.

---

<a id="ch5"></a>

## Pending Work

### High priority

| Task | Books | What's needed |
|------|-------|---------------|
| Extract Book 19 PDF | 19 | The Koraga Language — pdftotext or Sarvam OCR; create en.md + claude-prompt.md |
| Extract Book 21 PDF | 21 | Pronouns (Oxford) — likely Unicode PDF; create en.md + claude-prompt.md |
| Sync docs/ after every phase (run sync_docs.py) | all | `docs/dnsbhat/` is served by GitHub Pages but edits go to `src/main/md/kannada/dnsbhat/`. After any OCR or kn.md changes, run `python3 .claude/skills/ettuge-sync/scripts/sync_docs.py` to sync src→docs preserving Jekyll nav front matter. Already handled by the `ettuge-sync` skill (Step 4a). |
| Fix OCR word-boundary splits | multiple | Words like `meccuge ay` should be `meccugAy` — OCR split at vowel boundaries. Audit all kn-eke.md files for space-separated suffix artifacts. |
| Verify cross-links kn → en → eke | all books with kn.md | Now that en.md files have detailed per-section anchors (Phase 16–17), the `[English →]` links in kn.md and the `[ಕನ್ನಡ →]` links in kn-eke.md need a full audit pass to ensure every anchor target resolves correctly. |
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
| Sollarime vol.5–7 | Vol.1–4 now processed (Phases 14 + 26); vols 5–7 not found in Google Drive — may be at dnshankarabhat.net (offline) |
| Book 31 eke/full.md | Eke romanisation of the A–Z dictionary entries not yet generated. Lower priority since the dictionary is English-headworded (Eke of Kannada definitions would be secondary use). |

### Low priority / stretch

| Task | Notes |
|------|-------|
| Retroflexion 1973 paper | Stanford Working Papers; should be in archive.org |
| Cambridge Dravidian Languages chapter | DNS Bhat contributed to Cambridge Language Surveys |

---

<a id="ch6"></a>

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

<a id="ch7"></a>

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

<a id="ch8"></a>

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
