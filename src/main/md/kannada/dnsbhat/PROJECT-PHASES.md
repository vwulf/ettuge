---
title: "DNS Bhat — Phase History"
nav_exclude: true
---

# DNS Bhat Ettuge Project — Phase History
*Phases 35 → 1, newest first. Full project context: [PROJECT-RECAP.md](./PROJECT-RECAP.md)*

---

## ಪರಿವಿಡಿ — Phase Groups

| Group | Phases | Key Work |
|-------|--------|----------|
| [Group 1](ch1) | 35–28 | Search & Pagefind, CI Chapterization, Grammar Section, Sidebar Restructure |
| [Group 2](ch2) | 27–20 | Book 31 Decode, PDFs, Taxonomy Migration, Transcript Fixes |
| [Group 3](ch3) | 19–15 | Deep TOC, Markdown Structure, OCR & Eke Pipeline |
| [Group 4](ch4) | 14–8 | OCR Cleanup: Books 07–29, English Summaries |
| [Group 5](ch5) | 7–1 | Foundation, Initial Cataloguing, Early Pipeline |

---

<a id="ch1"></a>

## Phases 35–28 — Search & Pagefind, CI Chapterization, Grammar Section
*2026-03-24 to 2026-03-27*

---

### Phase 35 — Pagefind Search Integration + Mobile Fix (2026-03-27)

**Root cause: bracket filter syntax broken in Pagefind 1.4.0.** The `data-pagefind-filter="section[DNS Bhat]"` inline-bracket syntax silently returns an empty string for all pages — `pf.filters()` showed `{"section":{"":1039}}` (every page mapped to an empty section). Fix: switch to text-content syntax via a visually-hidden `<span data-pagefind-filter="section">DNS Bhat</span>` on each DNS Bhat page. After fix, `pf.filters()` correctly returns `{"section":{"DNS Bhat":800,"Eke":4,...}}`.

**PagefindUI abandoned; low-level `pagefind.js` API adopted.** `PagefindUI`'s `selected_filters` wrapper was unreliable even with the corrected index. Replaced with direct low-level calls: `pf.search(query, { filters: { section: ['DNS Bhat'] } })` returns exactly the 468 DNS Bhat pages. The `_pfSearch(query, filterSection, label)` function handles both global search (`filterSection = null`) and section-filtered search.

**Results panel rendered to the right of the sidebar.** Previous approach rendered results inside the sidebar column, cropping long excerpts. New approach: a `position:fixed` panel appended to `<body>`; `reposition()` dynamically sets `left = sidebar.getBoundingClientRect().right` on desktop. Panel shows up to 12 results with bold title, URL, and Pagefind excerpt.

**Mobile results panel full-width.** On mobile the sidebar is full-width (`r.right ≥ window.innerWidth − 10`), so the panel is positioned at `left:0, top:sidebar.bottom` instead — full viewport width below the sidebar header.

**Both search bars moved to sidebar top.** `nav_footer_custom.html` (formerly the search host) emptied to a comment. New `docs/_includes/components/sidebar.html` override injects a `.site-search` div between `.site-header` and `{% include_cached components/site_nav.html %}`. DNS Bhat search input is conditionally rendered only on `page.url contains '/kannaDa/dnsbhat/'` pages.

**Mobile search bar always visible.** Initial sidebar override used `d-md-block d-none` on the `.site-search` div — JTD's responsive utility sets `display:none !important` on mobile. Fixed by removing the class entirely; search inputs are now unconditionally visible on all screen sizes.

**Commits:** search filter fix → low-level API + results panel → sidebar search bars → mobile visibility fix (2026-03-27)

---

### Phase 34 — Eke Chapterization + PROJECT-RECAP Restructure (2026-03-26)

**Eke chapter pages for all books:** `book/eke/full.md` files now split into per-chapter pages by CI alongside the kn files. Book 27 eke (`book/eke/full.md`): 5 `<a id="chN">` aliases added before each `<a id="part-N">` anchor — CI now generates ch1–ch5 Eke pages. Books 03, 07 (vol1–vol4), 08, 14, 17, 25, 28, 29, 30 already had chapter anchors in their eke files.

**Book 07 `book/eke/full.md` updated:** Volume count corrected (2→4); ch7–8 links fixed to vol3, ch9–10 to vol4; ch10 (tOrUpada) added to TOC and content; stale "vols 3–4 not available" notice removed.

**PROJECT-RECAP restructured:** Phase history reversed to newest-first; ಪರಿವಿಡಿ TOC added; `<a id="chN">` anchors added at 8 major sections so CI generates chapter pages for the recap itself.

**src/ sync fix:** Phases 28–33 were accidentally added only to `docs/dnsbhat/PROJECT-RECAP.md` (old location); now correctly added to `src/main/md/kannada/dnsbhat/PROJECT-RECAP.md` so CI serves them at the live URL.

**Commit:** `f7dc3a5` — `feat(eke): chapterize book 27 eke + fix PROJECT-RECAP sync — Phase 34`

---

---

### Phase 33 — Chapter Page Title Fixes + Claude Prompt Chapter URLs (2026-03-26)

**Chapter title extraction fixed (5 commits to `pages.yml`):**

| Fix | Problem | Solution |
|-----|---------|----------|
| TOC-priority | `first_heading()` found section headings (`## ೧.೧ ...`) instead of chapter titles for books 03, 08, 14 | Added `toc_title_map()` parsing `[ಅಧ್ಯಾಯ N — Title](#adhyAya-N)` links; TOC title preferred over body heading |
| Number-prefix strip | `## 1. ಮುನ್ನೋಟ` rendered as "1. ಮುನ್ನೋಟ" | Added `re.sub(r'^[\d\u0CE6-\u0CEF]+[.\s]+', '', h)` to strip Arabic and Kannada numeral prefixes |
| Book 07 vol4 | No `## ` chapter headings for ch9/ch10 | Added `## ಅಧ್ಯಾಯ ೯ — ಆಡುಪದಗಳ ಬಳಕೆ` and `## ಅಧ್ಯಾಯ ೧೦ — ತೋರುಪದಗಳ ಬಳಕೆ` + TOC links |
| Book 27 ch4 | `ಭಾಗ ನಾಲ್ಕು` was plain text, not `## ` | Promoted to `## ಭಾಗ ನಾಲ್ಕು — ಕನ್ನಡ ಭಾಷೆಯ ಸ್ವರೂಪ`; other part headings given subtitles |
| Book 03 ch9 | `## ಅಧ್ಯಾಯ ಒಂಬತ್ತು` (generic); missing TOC entry | Updated to `## ಅಧ್ಯಾಯ ೯ — ಮುಕ್ತಾಯ`; added `[ಅಧ್ಯಾಯ 9 — ಮುಕ್ತಾಯ](#adhyAya-9)` to TOC |

**Verified live on GitHub Pages** — all 13 book/vol files now have correct chapter page titles:
- Book 03 ch1: "Ch 1 — ಪೀಠಿಕೆ" ✅
- Book 07 vol1 ch1: "Ch 1 — ಮುನ್ನೋಟ" ✅
- Book 08 ch1: "Ch 1 — ಮುನ್ನೋಟ" ✅
- Book 14 ch1: "Ch 1 — ಪೀಠಿಕೆ" ✅
- Book 27 ch1: "Ch 1 — ಭಾಗ ಒಂದು — ಭಾಷೆಯ ಸ್ವರೂಪ" ✅
- Book 31 ch1: "Ch 1 — A" ✅

**Claude prompt chapter URL updates:** `update_chapter_prompts.py` script written and run — appended Phase 33 item to 11 `claude-prompt.md` files with exact GitHub Pages fetch URLs per chapter:

| Book | Chapters | Item # |
|------|---------|--------|
| 03 | ch1–ch9 | 11 |
| 07 | ch1–ch4 (vol1), ch5–ch6 (vol2), ch7–ch8 (vol3), ch9–ch10 (vol4) | 12 |
| 08 | ch1–ch5 | 11 |
| 14 | ch1–ch12 | 11 |
| 17 | ch1–ch12 | 11 |
| 25 | ch1–ch11 | 11 |
| 27 | ch1–ch5 | 11 |
| 28 | ch1–ch12 | 11 |
| 29 | ch1–ch11 | 11 |
| 30 | ch1–ch10 (new INSTRUCTIONS section) | 1 |
| 31 | ch1–ch19 (A–W) | 7 |

Purpose: Claude Chat skills can now fetch a specific chapter URL (e.g. `book/kn/ch3`) rather than loading the full 100k–300k character source, preventing token exhaustion when answering focused questions.

**Primers regenerated:** 194k + 129k chars (both within 200k limit) ✅

**Commits:** `69e5808`…`6ee4a69` — Phase 33 chapter title fixes and prompt updates

---

---

### Phase 32 — CI Chapter Splitter + Chapter Anchors (2026-03-25)

**Book 14 raw.md cleanup:** 587 lines of Internet Archive HTML chrome (nav bars, SVG icons, banners) removed from top of `book/kn/raw.md`; content now starts cleanly at `# Full text of "..."`.

**Chapter splitter added to CI (`pages.yml`):** Walks all `docs/kannaDa/dnsbhat/*/book/*/full.md`, splits at `<a id="(?:ch|adhyAya-)(\d+)">` anchors, generates:
- `ch0.md` — preamble + ಪರಿವಿಡಿ TOC with `#chN` links rewritten to page-relative `chN` + chapter quick-nav bar; `nav_exclude: true`
- `ch1.md`…`chN.md` — one per chapter anchor; nav banner `← Prev · Contents · Next →`

Sidebar CANDIDATES updated so `book/kn/ch0.md` takes priority over `book/kn/full.md` (lightweight index first on slow connections).

**Chapter anchors added** to three books that lacked them:
- **Book 27** — 5 `<a id="chN">` aliases added before each `#part-N` anchor
- **Book 31** — 19 `<a id="chN">` anchors added before each `## LETTER` heading (A=ch1, B=ch2, … W=ch19)
- **Book 07 vol4** — `ch9` before `sec-9-1`, `ch10` before `sec-10-1`

**Books with chapter pages generated (≥2 anchors):** 03, 07 (vol1–vol4), 08, 14, 17, 25, 27, 28, 29, 30, 31 — 13 full.md files, ~120 chapter pages total.

**Commit:** `e07a46d` — `feat(ci): add chapter splitter step to pages.yml — Phase 32`

---

---

### Phase 31 — PROJECT-RECAP Cleanup (2026-03-25)

Removed stale TBD items from PROJECT-RECAP.md:
- 3 completed High-priority items (Deep TOC anchors Phase 19, Markdown headings Phase 18, word-per-line OCR artifact Phase 18)
- "Expand Eke home page description" completed item removed

---

---

---

### Phase 29 — Grammar Section: Illustrated Verb Paradigms (2026-03-25)

New directory `src/main/md/kannada/grammar/` with three verb paradigm pairs:

| File | Content |
|------|---------|
| `iru-verb-paradigm.md` | 42 forms of ಇರು across tense/mood/person/number |
| `iru-illustrated.html` | Visual interactive paradigm table |
| `mADu-verb-paradigm.md` | 36 forms of ಮಾಡು |
| `mADu-illustrated.html` | Visual interactive paradigm table |
| `illa-verb-paradigm.md` | 5 forms of ಇಲ್ಲ (defective negative) |
| `illa-illustrated.html` | Visual interactive paradigm table |

Cross-navigation between all three illustrated pages (prev/next banners). Compound forms notes added: `mADihanu` (converb + emphatic ಹನು), `mADalAre` (purpose converb + defective aux ಆರು). Root redirect stubs at grammar folder index.

---

---

### Phase 28 — Sidebar Restructure + Eke Motivation Rewrite (2026-03-24)

**Sidebar restructure:** ಕನ್nnaDa L1 root reorganised — DNS Bhat / Eke / Grammar as L2 peers; Books / Blog / YouTube / Stubs as L3 under DNS Bhat. 562 occurrences of mixed-script `ಕನ್nnaDa` header text normalised.

**Eke motivation section rewritten:** Symbol complexity table added (46 Eke symbols vs Devanagari's 47); `q/Q` for vocalic ḷ/ḹ documented; `:` and `^` as dialect modifiers clarified (`:` = geminate, `^` = unrounded-u in Havyaka). Script history Tamil-Brāhmī lineage clarified.

---

---


<a id="ch2"></a>

## Phases 27–20 — Book 31 Decode, PDFs, Taxonomy Migration, Transcript Fixes
*2026-03-20 to 2026-03-23*

---

### Phase 27 — Book 31 Full CID Decode: Baraha Dictionary (2026-03-23)

**Book 31** — *ಇಂಗ್ಲಿಶ್ ಪದಗಳಿಗೆ ಕನ್ನಡದ್ದೇ ಪದಗಳು* (487pp, A–Z dictionary) — all 12,121 English headwords fully decoded. The initial Phase 24 `full.md` had 5,411 garbled + 495 partial entries because the source PDF used an embedded Baraha font with CID-encoded glyphs.

**The CID decode problem:** `pdfplumber` could not map glyph IDs to Unicode — it emitted `(cid:N)` tokens instead of characters. Standard Nudi/WX pipelines didn't apply here because the font's codepoint mapping was Baraha cp1252, not WX.

**Three key discoveries:**

| Discovery | Detail |
|-----------|--------|
| Three-range CID offset rule | CIDs 1–96: offset +31 (ASCII); CIDs 97–114: offset +57 (0xA0–0xAB Baraha high zone); CIDs 115+: offset +61 (0xB2–0xFF Baraha extended). Boundary at 114 (not 113 as initially assumed). |
| CID 114 → `«` = ವಿ | With offset +57: byte 171 = 0xAB = `«` → maps to ವಿ in wx_decode MAPPING. Critical for locative/instrumental forms. Proved by `abet` → ಕಳವಿನಲ್ಲಿ. |
| `±` (0xB1) as ಲ, not ಶ | In this PDF font, CID 116 decodes to `±` but is used as ಲ base (3,196 of 3,207 occurrences). Only 12 are genuine ಶ (patterns `±À` = ಶ, `±É` = ಶೆ). Fix: `re.sub(r'±(?![ÀÉ])', '®', text)`. |
| `³` (0xB3) = ಲ್ಲಿ trigger | CID 116 produces `³`; `³è` sequences encode the locative suffix. Fix: replace `³→°` before wx_decode → VATTAKSHARA rearrangement produces ಲ + ್ + ಲ + ಿ = ಲ್ಲಿ. Affects 580 locative forms. |

**Additional preprocess fixes:**
- `¯À` → `®` (standalone ಲ; the `¯ + À` pair was not in MAPPING)
- `¯` before non-combo chars → `®` (handles all unmapped `¯` uses)
- `\xad` (soft hyphen) → `©` (ಬಿ single-glyph form)

**Result:** 12,121 entries decoded; **2 remaining garbled** (OCR-artifact headwords: `wAr)` and `XYZ` — spurious, not real dictionary entries). All genuine dictionary entries are fully readable Kannada.

**Batch script:** `/tmp/decode_book31_batch.py` — full decode pipeline with three-range CID rule, preprocess substitutions, wx_decode.convert_chunk(), postprocess cleanup, entry parser, and full.md generator.

**Commit:** `4751e65` — `feat(book31): fully decode Baraha CID dictionary — Phase 27`

---

---

### Phase 26 — Sollarime Vol.3 + Vol.4 from PDF (2026-03-23)

**Book 07** — *ಕನ್ನಡ ಬರಹದ ಸೊಲ್ಲರಿಮೆ* vols 3 and 4 (syntax volumes) extracted from PDF and processed.

**Source:** Google Drive PDFs — vol3 (241pp), vol4 (274pp). Both use Baraha/WX encoding; decoded via `wx_decode.py` pipeline.

**Vol3 — ವಾಕ್ಯರಚನೆ ಭಾಗ ೧ (Chapters 7–8):**
- Chapter 7: ಎಸಕಪದದ ಪಾಂಗುಗಳು (Verbal Arguments) — verb valency, transitivity, argument frames
- Chapter 8: ಪಾಂಗಿಟ್ಟಳದಲ್ಲಿ ಮಾರ್ಪಾಡುಗಳು (Argument Frame Alternations) — passivisation, causativisation

**Vol4 — ವಾಕ್ಯರಚನೆ ಭಾಗ ೨ (Chapters 9–10):**
- Chapter 9: ಆಡುಪದಗಳು (Personal Pronouns) — person/number/gender in Kannada pronoun system
- Chapter 10: ತೋರುಪದಗಳು (Demonstratives) — proximal/distal deixis, anaphora

**Files produced per volume:**
- `book/volN/kn/raw.md` — extracted OCR source
- `book/volN/kn/full.md` — structured Kannada with TOC and `<a id="adhyAya-N">` anchors
- `book/volN/eke/full.md` — Eke romanisation
- `book/volN/en/summary.md` — English chapter summary

**Multi-volume index** `book/kn/full.md` updated: vol3 and vol4 entries added; vol1/vol2 entries corrected; vols 5–7 marked as pending.

**Commits:** (see git log)

---

---

### Phase 25 — YouTube Summaries for Books 01–13 + Book 33 Split (2026-03-22)

**Motivation:** Two tasks: (1) provide English overviews for the 6 YouTube-only books that lacked any English entry; (2) correctly separate the two distinct *sollarime* works that had been conflated in Book 07's folder.

#### 25a — YouTube English summaries for books 01, 06, 10, 11, 12, 13

Six books had YouTube transcripts (or stubs) but no English summary. Created `youtube/en/summary.md` + updated `claude-prompt.md` for each:

| Book | Title | Quality | Notes |
|------|-------|---------|-------|
| 01 | idu kannaDaddE vyAkaraNa | ✅ Excellent | Malati Bhat reading; 3 parts; full 19-chapter TOC read aloud in Part 1 |
| 06 | kalikenuDi mattu nuDikalike | ⚠️ Garbled | Live-lecture ASR; keyword signals only |
| 10 | kannaDa nuDiya hinnaDavaLi | ⚠️ Garbled | Live-lecture ASR; content drawn from website description |
| 11 | kannaDa barahada padasamasye | ⚠️ Garbled | 25-part lecture; may be earlier monograph later condensed into Book 30 |
| 12 | kannaDa bhASheya kalpita caritre | ✅ Good | Malati Bhat reading; 2 parts; comparative method section well-preserved |
| 13 | dArege doDDavaru | 🎓 Symposium | Third-person references to Bhat; panels praising his work — felicitation proceedings, not Bhat reading his own book |

All 6 books now have `youtube/en/summary.md` with explicit quality assessment and part-level availability table. `claude-prompt.md` updated to include the new English file.

**Commits:** (see git log)

#### 25b — Book 33 split from Book 07 (ಕನ್ನಡ ಸೊಲ್ಲರಿಮೆ vs ಕನ್ನಡ ಬರಹದ ಸೊಲ್ಲರಿಮೆ)

**Discovery:** The `youtube/kn/full.md` inside Book 07's folder was titled *KANNADA SOLLARIME* (no "baraha") — a different, shorter work than Book 07's *KANNADA BARAHADA SOLLARIME* (7-volume grammar of *written* Kannada). The Book 07 README had carried a `⚠️ YouTube note` since Phase 22 flagging the mismatch.

**Action:**
- `git mv` Book 07's `youtube/kn/full.md` → new folder `33-kannaDa-sollarime/youtube/kn/full.md`
- `nav_order` updated 107→133; `redirect_from: /dnsbhat/07-kannadada-sollarime/07-kannadada-sollarime` preserved for URL continuity
- New Book 33 folder: `README.md`, `claude-prompt.md`, `youtube/en/summary.md` created
- Book 07 `README.md` updated: YouTube row removed, clean cross-reference link to Book 33 added
- `dnsbhat/README.md`: Book 33 entry added (Section M — YouTube-Only Book Split from Book 07), collection stats updated 32→33

**Identity note:** *ಕನ್ನಡ ಸೊಲ್ಲರಿಮೆ* (no "baraha") may be an earlier or more general grammar covering both spoken and written Kannada — the omission of "baraha" (writing) distinguishes it from Book 07 (*ಕನ್ನಡ ಬರಹದ ಸೊಲ್ಲರಿಮೆ*, 7-volume grammar of written Kannada). The precise relationship cannot be determined without a PDF.

**Stats after Phase 25:** All 33 DNS Bhat books catalogued; all 33 have `claude-prompt.md`.

**Commits:** (see git log)

---

---

### Phase 24 — Books 30–32 Added from PDF Extraction (2026-03-22)

**Motivation:** Three additional DNS Bhat works identified from Google Drive PDFs not previously catalogued.

#### Book 30 — ಕನ್ನಡ ಬರಹವನ್ನು ಸರಿಪಡಿಸೋಣ (382 pages, Nudi encoding)

Full 4-file set produced via `wx_decode.py` (Nudi→Unicode lookup, same pipeline as Books 07/17/25/28/29):
- `book/kn/raw.md` — decoded Kannada source (Nudi WX → Unicode)
- `book/kn/full.md` — structured Kannada with 10-chapter TOC and `<a id="adhyAya-N">` anchors
- `book/en/summary.md` — English chapter-by-chapter summary with cross-links
- `book/eke/full.md` — Eke romanisation matching full.md structure
- `claude-prompt.md` — AI context primer

**Subject:** Practical guide to correcting Kannada script usage — aspirate simplification, anusvara normalisation, vowel-length marking. Arguments for *hosa baraha* (simplified writing) applied to print.

#### Book 31 — ಇಂಗ್ಲಿಶ್ ಪದಗಳಿಗೆ ಕನ್ನಡದ್ದೇ ಪದಗಳು (487 pages, Nudi encoding, A–Z dictionary)

Partial processing — Nudi WX decode successful but English headword reconstruction partially garbled:
- `book/kn/raw.md` — decoded Kannada source
- `book/en/summary.md` — English summary (headwords + overview; garbling noted)
- `claude-prompt.md`

**Subject:** Comprehensive dictionary of native Kannada equivalents for English words (A–Z), structured as a lexical resource. Companion to Book 15 (*ingliS-kannaDa padanerake*).

#### Book 32 — The Prominence of Tense, Aspect and Mood (214 pages, clean English, John Benjamins)

Clean English PDF — pdfplumber extraction; no Nudi decoding required:
- `book/en/summary.md` — chapter summary
- `claude-prompt.md`

**Subject:** Cross-linguistic typological monograph (English) on the TAM hierarchy across world languages. Bhat's contribution to general linguistic theory; Kannada-informed but not Kannada-specific.

**Stats after Phase 24:** 32 books catalogued (sections A–L); all 32 have `claude-prompt.md`.

**Commit:** (see git log)

---

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

---


<a id="ch3"></a>

## Phases 19–15 — Deep TOC, Markdown Structure, OCR & Eke Pipeline
*2026-03-19 to 2026-03-20*

---

### Phase 19 — Deep 3-Level TOC + Section Anchors (2026-03-20)

**Scope:** All 11 books with kn.md (02, 03, 07-vol1, 07-vol2, 08, 14, 17, 25, 27, 28, 29).

**Changes:**
- Added `<a id="sec-N-M">` anchors at all section headings and `<a id="sub-N-M-K">` at all subsection headings in every kn.md
- ಪರಿವಿಡಿ TOC in each kn.md extended to list all three levels (chapter → section → subsection)
- Cross-links inserted after every sec/sub anchor: `[Eke →](./SLUG-kn-eke#sec-N-M)` in kn.md; `[ಕನ್ನಡ →](./SLUG-kn#sec-N-M)` in kn-eke.md
- Chapter nav fragments corrected to `#adhyAya-N` throughout
- Index back-links added to all kn.md headers: `[← ಸೂಚಿ](./README)` and `[← sUci](./README)` in kn-eke.md
- kn-eke.md self-referential header links corrected (were pointing to wrong file)

---

---

### Phase 18 — docs/ sync + Noto Sans Kannada + ettuge-sync skill (2026-03-20)

**Root cause fixed:** All 57 `docs/dnsbhat/` files were stale — Phase 17 OCR cleanup and kn.md changes went to `src/` but were never copied to `docs/` (the GitHub Pages source). This caused garbled rendering of books 25, 15, and all other Phase 17-touched books.

**Changes:**
- `docs/dnsbhat/` — synced 57 files from `src/main/md/kannada/dnsbhat/` preserving Jekyll nav front matter (`title`, `parent`, `nav_order`) in each file
- `docs/_sass/custom/custom.scss` — added Noto Sans Kannada via Google Fonts for correct nukta (U+0CBC ಼) rendering; previously Georgia/system fonts silently dropped nukta-modified clusters
- `.claude/skills/ettuge-sync/` — new skill (`ettuge-sync`) automates the full post-phase sync pipeline: staleness detection → CLAUDE.md updates → claude-prompt updates → docs/ sync → global skill copy → regenerate combined docs files → commit and push
- `.claude/skills/ettuge-sync/scripts/sync_docs.py` — standalone script for src→docs sync (Step 4a of ettuge-sync skill)

---

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

---

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

---


<a id="ch4"></a>

## Phases 14–8 — OCR Cleanup: Books 07–29, English Summaries
*2026-03 (earlier)*

---

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

---

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

---

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

---

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

---

### Phase 10 — Book 08 varSa OCR Correction (2026-03-14)

Targeted fix for a systematic OCR misread in book 08 (*Kannadakke Mahaprana Yake Beda*). The word **ವರ್ಷ** ("year", Eke: `varSa`) was rendered in four wrong patterns by the OCR engine — corrected in both the Eke romanisation file and the structured Kannada file.

| Wrong form | Correct | Count |
|-----------|---------|-------|
| `varragaL*` / `varradoLage` | `varSagaL*` / `varSadoLage` | 6 |
| `varmagaL*` | `varSagaL*` | 3 |
| `varyagaL*` | `varSagaL*` | 2 |
| `varka` | `varSa` | 2 |

**Files fixed:** `08-kannaDakke-mahAprANa-yAke-bEDa-kn-eke.md` (13 instances) and `08-kannaDakke-mahAprANa-yAke-bEDa-kn.md` (matching Kannada script corrections: ವರ್ರ, ವರ್ಮ, ವರ್ಯ, ವರ್ಕ → ವರ್ಷ). No other books contained these patterns.

---

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

---

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

---


<a id="ch5"></a>

## Phases 7–1 — Foundation, Initial Cataloguing, Early Pipeline
*2026-03 (initial)*

---

### Phase 7 — Book 15 Hybrid Extraction & Processing (2026-03-12)

**Book 15** — *Inglish Kannada Padanerake* — first dictionary-format book processed:
- **Source:** 53-page sample PDF (`English-KannadaPadanerakeSample.pdf`) — pre-print prelims covering letter A (A→Az)
- **Challenge:** Old WX Nudi font encoding. English headwords extracted via raw pdfminer ASCII; Kannada equivalents decoded with `wx_decode.py` `convert_text()`. Result: 3,454-line `book.md` with 84,475 Kannada Unicode characters.
- `kn-eke.md` — Eke romanisation of preface, conventions, pattern tables, and ~100-entry A–Az transliteration sample
- `en.md` — English analysis with **10 word-formation pattern sections**: N+N compounding, verb-derived nouns (-ta/-ike/-uge/-me/-vu), agent nouns (-ga/-uga/-gAra), ಅರಿಮೆ domain names, ಮನೆ institutions, ಗಾಳಿ air-cluster, ಮಾಂಜುಗೆ therapy compounds, productive prefixes, and more
- `claude-prompt.md` — Rich AI primer: 6-step word-generation decision tree, 11 domain-specific head-noun cluster tables, 100 curated entries by domain, common mistakes table (Sanskrit vs native), philosophical frame

---

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

---

### Phase 5 — WX Decode Tool

Books 07, 17, 25, 28, 29 had OCR output in WX Kannada encoding (old Nudi/KGP font). Built `wx_decode.py` — a lookup-table decoder (based on aravindavk/ascii2unicode) that converts WX-encoded bytes to Unicode Kannada. Decoded ~1.9M Kannada Unicode chars across 6 files.

---

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

---

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

---

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

---

### Phase 1 — Discovery & Cataloguing

- **Crawled dnshankarabhat.net** via CDX Wayback API → found 91 unique archived pages
- **Identified 29 works** across Kannada popular books, English academic monographs, journal articles, and blog series
- Created `BOOKS.md` — comprehensive annotated catalogue of all 29 works, organised into thematic sections (Grammar, Dialect Studies, History, Vocabulary, Old Kannada, English Academic, Sound Change, Syntax)

---

