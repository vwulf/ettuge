# ಡಾ. ಡಿ. ಎನ್. ಶಂಕರ ಬಟ್ — ಹೊತ್ತಗೆಗಳ ಸೂಚಿ
# Dr. D. N. Shankara Bhat — Complete Book Catalog

**Last updated:** 2026-03-13 (cross-link audit complete; Book 15 kn-eke restructured)
**Scope:** All known DNS Bhat works, with emphasis on Kannada linguistics
**Sources:** dnshankarabhat.net (CDX sitemap — 91 unique pages found), archive.org, Google Drive, YouTube transcripts, Google Books

**Blog collection status:** Blog posts fetched from dnshankarabhat.net and saved as `*-blog.md` files:
- **Book 02** — 15 parts of *ಇಂಗ್ಲಿಶ್ ನುಡಿ* series (parts 4–18) ✅
- **Book 14** — 7 parts of *ಶಬ್ದಮಣಿದರ್ಪಣ* series ✅
- **Book 18** — 13 parts of *ನುಡಿಯರಿಮೆಯ ಇಣುಕುನೋಟ* series (parts 1–3, 10, 14, 18, 20, 23, 27, 28, 29, 33, 35) ✅

**Sarvam OCR status (2026-03-10):** 8 books OCR'd via Sarvam Vision API (`kn-IN`):
- **Book 03** ✅ Clean Unicode Kannada (12,264 lines, 957 KB, 292k Kannada chars)
- **Book 07 vol.1** ✅ WX-decoded (24,825 lines → 340k Kannada chars after decode)
- **Book 07 vol.2** ✅ WX-decoded (15,300 lines → 369k Kannada chars after decode)
- **Book 17** ✅ WX-decoded (22,230 lines → 287k Kannada chars after decode)
- **Book 25** ✅ WX-decoded (14,409 lines → 319k Kannada chars after decode)
- **Book 27** ✅ Clean Unicode Kannada (9,098 lines, 971 KB, 287k Kannada chars)
- **Book 28** ✅ WX-decoded (12,789 lines → 304k Kannada chars after decode)
- **Book 29** ✅ WX-decoded (10,039 lines → 304k Kannada chars after decode)

**WX→Unicode decode:** Books 07, 17, 25, 28, 29 used old Nudi/KGP font encoding. Decoded with `wx_decode.py` (Nudi→Unicode lookup table, based on aravindavk/ascii2unicode). Total: 1.9M Kannada Unicode chars decoded across 6 files.

**Book 15** — Sample PDF (53 pages, pre-print prelims; letter A only) — hybrid extracted (pdfminer ASCII + wx_decode) ✅ book.md, en.md, kn-eke.md, claude-prompt.md all created

**Cross-linking status (2026-03-13):** All processed books now have per-section `[ಕನ್ನಡ →] | [Eke →]` links in their `en.md` files. Books 02, 08, 14 had `[ಕನ್ನಡ →]` only — `[Eke →]` links added. Books 07, 17, 25, 27, 28, 29 had no links — both added. Book 03 had broken links to a non-existent `kn.md` — retargeted to `book.md` + `[Eke →]` added.

> For the full project arc — phases, pipeline, tools, pending work, and intellectual themes — see [PROJECT-RECAP.md](./PROJECT-RECAP.md).

---

## Quick Reference

| # | Short Title | Language | Year | Format Available | Text Available |
|---|-------------|----------|------|-----------------|----------------|
| 01 | Idu Kannadade Vyakarana | Kannada | 2021 | YouTube | ✅ Transcript |
| 02 | Kannadalle Hosapadagalannu Kattuva Bage | Kannada | — | YouTube + Blog | ✅ Transcript + 15 blog posts |
| 03 | Kannada Padagala Olarachane | Kannada | 2014 | YouTube + **PDF** | ✅ Transcript + ⚠️ PDF (WX font) |
| 04 | Mathu Matthu Barahada Naduvina Gondala | Kannada | — | YouTube | ⚠️ Partial |
| 05 | Mathina Olaguttu | Kannada | — | YouTube | ✅ Transcript |
| 06 | Kalikenudi Matthu Nudikalike | Kannada | — | YouTube | ❌ Corrupted |
| 07 | Kannadada Sollarime (7 vols) | Kannada | 2010–2019 | Website + YouTube + **PDF vol1+2** | ⚠️ PDF (WX font) |
| 08 | Kannadakke Mahaprana Yake Beda | Kannada | 2017 | PDF + DjVu | ✅ Full text |
| 09 | Havyaka Kannada (popular) | Kannada | — | YouTube | ⚠️ Partial |
| 10 | Kannada Nudiya Hinnadavali | Kannada | — | YouTube | ⚠️ Partial |
| 11 | Kannada Barahada Padasamasye | Kannada | — | YouTube | ❌ Corrupted |
| 12 | Kannada Bhasheya Kalpita Charitre | Kannada | — | YouTube | ✅ Transcript |
| 13 | Dharege Doddavaru | Kannada | — | YouTube | ❌ Corrupted |
| 14 | Nijakku Halegannada Vyakarana Entahadu | Kannada | 2005/2015 | PDF + DjVu + Blog | ✅ Full text + 7 blog posts |
| 15 | Inglish Kannada Padanerake | Kannada | 2015 | **PDF sample** (53p) | ✅ Hybrid extracted (A–Az, 84k chars) + en/kn-eke/claude-prompt |
| 16 | Samskruta Padagalige Kannadade Padagalu | Kannada | — | Website | ❌ Not collected |
| 17 | Kannada Nudi Nadedu Banda Dari | Kannada | 2014 | **PDF** | ⚠️ PDF (WX font, 405p) |
| 18 | Kannada Nudiya Bagege Chintane | Kannada | — | Website + Blog | ✅ 13 blog posts (Inukunota series) |
| 19 | The Koraga Language | English | 1971 | PDF | ❌ Not extracted |
| 20 | An Outline Grammar of Havyaka | English | 1971 | PDF + DjVu | ✅ Full text |
| 21 | Pronouns (Oxford) | English | 2004 | PDF | ❌ Not extracted |
| 22 | Sound Change | English | 2001 | Google Books | ❌ Not extracted |
| 23 | A Grammar of Manipuri | English/Kn | — | Website | ❌ Not collected |
| 24 | Grammatical Relations | English | — | Website | ❌ Not collected |
| 25 | Kannada Vakyagala Olarachane | Kannada | 2014 | **PDF** | ⚠️ PDF (WX font, 289p) |
| 26 | ಉಲಿ-ಮಾರ್ಪಾಡಿನ-ಗೆರೆಗಳು (Sound Change Laws) | Kannada | 2024 | Website | ❌ Cloudflare blocked |
| 27 | Baasheya Bagge *(ಭಾಷೆಯ ಬಗ್ಗೆ)* | Kannada | 1970/2010 | **PDF** (4th ed.) | ⚠️ PDF (WX font, 208p) — **NEW** |
| 28 | kannaDakke bEku kannaDaddE vyAkaraNa *(ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ)* | Kannada | 2000/2013 | **PDF** (7th ed.) | ⚠️ PDF (WX font, 253p) — **NEW** |
| 29 | Kannada Vyakarana Yaake Beku *(ಕನ್ನಡ ವ್ಯಾಕರಣ ಯಾಕೆ ಬೇಕು?)* | Kannada | 2009 | **PDF** | ⚠️ PDF (WX font, 260p) — **NEW** |

---

## Section A — Kannada Language Reform & Grammar

### 01 — ಇದು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ
**Idu Kannadade Vyakarana** *(This Is Kannada's Own Grammar)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2021 (consolidation of 2010–2019 *Sollarime* volumes)
- **ವಿಶಯ / Topic:** A unified Kannada grammar described from Kannada's own structural logic — not Sanskrit or English
- **ಮೂಲ / Source:** YouTube transcript (Malati Bhat reading)
- **ಗುಣಮಟ್ಟ / Quality:** Good (49 lines — partial transcript)
- **ಕಡತ / Folder:** [01-idu-kannadade-vyakarana/](./01-idu-kannadade-vyakarana/)
- **ಸಂಬಂಧ / Relation:** Synthesizes all 7 volumes of *Kannada Barahada Sollarime* (→ 07)

**Key Thesis:** Existing Kannada grammars are not truly Kannada grammars — they impose Sanskrit frameworks on a language with fundamentally different structure. Bhat introduces native Kannada grammatical terminology: *hesaru pada* (noun), *esaka pada* (verb), *paricharana pada* (adjective).

---

### 02 — ಕನ್ನಡದಲ್ಲಿ ಹೊಸ ಪದಗಳನ್ನು ಕಟ್ಟುವ ಬಗೆ
**Kannadalle Hosapadagalannu Kattuva Bage** *(How to Form New Words in Kannada)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** Word-formation in Kannada using native Dravidian roots and affixes
- **ಮೂಲ / Source:** YouTube transcript + dnshankarabhat.net blog (Wayback Machine)
- **ಗುಣಮಟ್ಟ / Quality:** Good (519 lines transcript + **6,469 lines blog text**)
- **ಕಡತ / Folder:** [02-kannadadalle-hosapadagalannu-kattuva-bage/](./02-kannadadalle-hosapadagalannu-kattuva-bage/)

**Files in folder:**
| File | Contents |
|------|----------|
| `02-...-youtube.md` | YouTube transcript |
| `02-...-blog.md` | **15 blog posts** — *ಇಂಗ್ಲಿಶ್ ಪದಗಳಿಗೆ ಸಾಟಿಯಾಗಿ ಕನ್ನಡದಲ್ಲೇ ಹೊಸ ಪದಗಳನ್ನು ಕಟ್ಟುವ ಬಗೆ* series (parts 4–18) |

**Blog series coverage:** Parts 4–18 collected (parts 1–3 not found in Wayback Machine)
- Parts 4–5: ಎಸಕ ಪದಗಳಿಂದ / ಎಸಕವನ್ನು ಗುರುತಿಸುವ ಬಗೆ
- Parts 6–7: ಒಟ್ಟುಗಳಿಲ್ಲದೆ ಎಸಕಪದ / ಹೆಸರು ಪದ → ಬೇರೆ ಹೆಸರು ಪದ
- Parts 8–11: ಮುನ್ನೊಟ್ಟು series (*mun-*, *imba-*, *hotta-*, *allagaletya-* prefixes)
- Parts 12–13: ಅಲ್ಲಗಳೆಯುವ (negation word-formation)
- Parts 14–15: ಇಂಗ್ಲಿಶ್ ಜೋಡುಪದಗಳು (English compound words)
- Parts 16–18: ಇಂಗ್ಲಿಶ್ ಹೆಸರುಗಳು / ಎಸಕ ಪದ / ಪರಿಚೆ ಪದ equivalents

**Key Content:**
- Over 50% of Kannada vocabulary = Sanskrit loanwords; 80% in scientific writing
- Native Kannada suffixes: *-ga* (agent nouns), *-gara* (designation), *-ike* (nominalisation)
- Native prefixes: *mun-* (forward/before), *hin-* (behind/after), *hosa-* (new)
- Systematic documentation of productive Kannada word-formation patterns

---

### 03 — ಕನ್ನಡ ಪದಗಳ ಒಳರಚನೆ
**Kannada Padagala Olarachane** *(Internal Structure of Kannada Words)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** Morphology — how Kannada words are internally structured
- **ಮೂಲ / Source:** YouTube transcript
- **ಗುಣಮಟ್ಟ / Quality:** Good (605 lines)
- **ಕಡತ / Folder:** [03-kannada-padagala-olarachane/](./03-kannada-padagala-olarachane/)

**Key Content:**
- Kannada has three independent base categories: nouns, verbs, adjectives (unlike Sanskrit's verb-root primacy)
- Old Kannada roots can produce words as compact as Sanskrit compounds
- The "keelarimai" (inferiority complex) toward Kannada vs "meelarimai" (superiority) toward Sanskrit

---

### 04 — ಮಾತು ಮತ್ತು ಬರಹದ ನಡುವಿನ ಗೊಂದಲ
**Mathu Matthu Barahada Naduvina Gondala** *(The Confusion Between Speech and Writing)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2011
- **ಪ್ರಕಾಶಕರು / Publisher:** ಭಾಷಾ ಪ್ರಕಾಶನ (Bhasha Prakashana), Heggodu, Sagara
- **ಪುಟಗಳು / Pages:** 142
- **ವಿಶಯ / Topic:** The fundamental distinction between spoken language and written script
- **ಮೂಲ / Source:** YouTube transcript (44 parts)
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ Partial — ~25/44 parts cleaned (~57%); Parts 10, 15, 25, 33, 35 disabled; many garbled
- **ಕಡತ / Folder:** [04-mathu-matthu-barahada-naduvina-gondala/](./04-mathu-matthu-barahada-naduvina-gondala/)

**Files in folder:**
| File | Contents |
|------|----------|
| `04-...-transcript.md` | YouTube transcript (44 parts, ~519 lines — partial) |
| `04-...-website.md` | Author's website description (stub) |
| `04-...-en.md` | English thematic summary (7 themes) |
| `04-...-kn-eke.md` | Eke romanisation of key passages |
| `04-...-claude-prompt.md` | AI context primer |

**Key Thesis:** Language IS speech — writing is a secondary, artificial representation of speech (*krutaka rUpa*). Kannada has existed as spoken language for millennia; the script is a historical addition. Understanding this distinction is essential for both linguistics and script reform.

---

### 05 — ಮಾತಿನ ಒಳಗುಟ್ಟು
**Mathina Olaguttu** *(The Mystery/Complexity of Language)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2013 (2nd reprint)
- **ಪ್ರಕಾಶಕರು / Publisher:** ಭಾಷಾ ಪ್ರಕಾಶನ (Bhasha Prakashana), Heggodu, Sagara
- **ಪುಟಗಳು / Pages:** 130
- **ವಿಶಯ / Topic:** Popular introduction to general linguistics for Kannada readers
- **ಮೂಲ / Source:** YouTube transcript (37 parts)
- **ಗುಣಮಟ್ಟ / Quality:** ✅ Good — ~27/37 parts cleaned (~73%); Parts 4, 6, 12, 15, 22, 29, 30, 35 disabled or garbled
- **ಕಡತ / Folder:** [05-mathina-olaguttu/](./05-mathina-olaguttu/)

**Files in folder:**
| File | Contents |
|------|----------|
| `05-...-transcript.md` | YouTube transcript (37 parts, ~539 lines) |
| `05-...-website.md` | Author's website description (stub) |
| `05-...-en.md` | English thematic summary (8 themes) |
| `05-...-kn-eke.md` | Eke romanisation of key passages |
| `05-...-claude-prompt.md` | AI context primer |

**Key Thesis:** Kannada must be understood on its own terms — not through Sanskrit grammar or English grammatical categories. Covers phonology, word classes, dialect variation, neurolinguistics, and writing systems from a Kannada-first perspective.

---

### 06 — ಕಲಿಕೆನುಡಿ ಮತ್ತು ನುಡಿಕಲಿಕೆ
**Kalikenudi Matthu Nudikalike** *(Learning Language and Language Learning)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** Language acquisition — how children learn language vs. how adults learn second languages
- **ಮೂಲ / Source:** YouTube transcript
- **ಗುಣಮಟ್ಟ / Quality:** ❌ Heavily corrupted (197 lines — mostly garbled)
- **ಕಡತ / Folder:** [06-kalikenudi-matthu-nudikalike/](./06-kalikenudi-matthu-nudikalike/)

---

### 07 — ಕನ್ನಡ ಬರಹದ ಸೊಲ್ಲರಿಮೆ (೭ ಸಂಪುಟಗಳು)
**Kannada Barahada Sollarime** *(Grammar of Kannada Writing — 7 Volumes)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2010–2019 (Vols 1–7, published individually)
- **ವಿಶಯ / Topic:** A comprehensive 7-volume grammar of written Kannada from first principles
- **Website URLs:** Volumes 1, 2, and 7 linked on dnshankarabhat.net
- **ಮೂಲ / Source:** Website (offline) + YouTube transcripts
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ Partial/corrupted (227 lines; website offline)
- **ಕಡತ / Folder:** [07-kannadada-sollarime/](./07-kannadada-sollarime/)

**Volume Structure:**
- Vol. 1: Phonology — sounds and scripts (*Kannada Barahada Sollarime 1*)
- Vol. 2: Morphology — word forms (*Kannada Barahada Sollarime 2*)
- Vols. 3–6: Syntax — sentence structure
- Vol. 7: Summary and consolidation (*Kannada Barahada Sollarime 7*)

**Note:** The 2021 book *Idu Kannadade Vyakarana* (→ 01) consolidates all 7 volumes.

---

### 08 — ಕನ್ನಡಕ್ಕೆ ಮಹಾಪ್ರಾಣ ಯಾಕೆ ಬೇಡ?
**Kannadakke Mahaprana Yake Beda** *(Why Kannada Does Not Need Aspirated Consonants)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2017
- **ಪ್ರಕಾಶಕರು / Publisher:** Navakarnataka Prakashana, Bengaluru
- **ಸರಣಿ / Series:** ಅರಿಮೆಯ ಚುಟುಕು ಕಡತಗಳು – ೩
- **ಪುಟಗಳು / Pages:** 102
- **ಮೂಲ / Source:** [Internet Archive](https://archive.org/details/arn.kannadakkemahaap0000dnsh) — PDF + DjVu OCR
- **ಗುಣಮಟ್ಟ / Quality:** ✅ **Full text available** (4,243 lines book.md + 1,965 lines djvu.md)
- **ಕಡತ / Folder:** [08-kannadakke-mahaprana-yake-beda/](./08-kannadakke-mahaprana-yake-beda/)

**Files in folder:**
| File | Contents |
|------|----------|
| `08-...-book.md` | Full Kannada text (cleaned from archive.org HTML) |
| `08-...-kn.md` | Structured Kannada version with TOC |
| `08-...-en.md` | English analysis/summary |
| `08-...-djvu.md` | DjVu OCR text (raw, may have errors) |
| `08-...-claude-prompt.md` | Analysis prompt |

**Key Thesis:** Kannada does not phonologically distinguish aspirated stops (ಖ/ಘ/ಛ/ಝ...) from their unaspirated counterparts. The mahaprana characters were borrowed from Sanskrit and serve no functional purpose in Kannada. Eliminating them would make the script simpler and more accessible.

**Chapters:**
- 1. ಮುನ್ನೋಟ (Overview)
- 2. ಓದುವ ಹಾಗೆ ಬರೆಯುವುದು (Write as you speak)
- 3. ಮಾರ್ಬಡಿಸಿಕೊಂಡಿರುವ ಬೇರೆ ನುಡಿಗಳು (Other languages that reformed)
- 4. ಸರಿಪಡಿಕೆಯ ಎದುರಿಕೆಗಳು (Objections to reform)
- 5. ಮುಕ್ತಾಯ (Conclusion)

---

## Section B — Dialect Studies (Kannada)

### 09 — ಹವ್ಯಕ ಕನ್ನಡ
**Havyaka Kannada** *(The Havyaka Dialect of Kannada)*

- **ಭಾಷೆ / Language:** Kannada (popular version)
- **ಪ್ರಕಟಣೆ / Year:** 2017 (self-published)
- **ವಿಶಯ / Topic:** Popular Kannada account of the Havyaka dialect, its geography, history, and phonological/morphological features
- **ಮೂಲ / Source:** YouTube transcript (43 parts: P1–P6 preamble + Parts 1–37)
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ Partial — ~72/88 transcript slots cleaned (~82%); early parts (1–14) most affected; best content in Parts 11, 27–29
- **ಕಡತ / Folder:** [09-havyaka-kannada/](./09-havyaka-kannada/)
- **See also:** [20 — Havyaka Outline Grammar 1971](./20-havyaka-outline-grammar/) (academic English version)

**Files in folder:**
| File | Contents |
|------|----------|
| `09-...-transcript.md` | YouTube transcript (43 parts, ~387 lines) |
| `09-...-website.md` | Author's website description (stub) |
| `09-...-en.md` | English thematic summary (5 themes) |
| `09-...-kn-eke.md` | Eke romanisation of key passages |
| `09-...-claude-prompt.md` | AI context primer |

**Key Thesis:** Havyaka Kannada is a fully independent dialect that preserves Proto-Dravidian phonological and morphological features absent from written Kannada — making it an irreplaceable source for reconstructing Kannada's linguistic history. DNS Bhat was born into the Havyaka community.

---

## Section C — History of Kannada Language

### 10 — ಕನ್ನಡ ನುಡಿಯ ಹಿನ್ನಡವಳಿ
**Kannada Nudiya Hinnadavali** *(History of the Kannada Language)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** Historical development of Kannada — its Dravidian roots, Sanskrit influence, and evolution
- **ಮೂಲ / Source:** YouTube transcript
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ Heavily corrupted (131 lines)
- **ಕಡತ / Folder:** [10-kannada-nudiya-hinnadavali/](./10-kannada-nudiya-hinnadavali/)

---

### 11 — ಕನ್ನಡ ಬರಹದ ಪದಸಮಸ್ಯೆ
**Kannada Barahada Padasamasye** *(Problems in Kannada Writing)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** Orthographic problems in Kannada — the script vs. the language
- **ಮೂಲ / Source:** YouTube transcript
- **ಗುಣಮಟ್ಟ / Quality:** ❌ Heavily corrupted (253 lines)
- **ಕಡತ / Folder:** [11-kannada-barahada-padasamasye/](./11-kannada-barahada-padasamasye/)

---

### 12 — ಕನ್ನಡ ಭಾಷೆಯ ಕಲ್ಪಿತ ಚರಿತ್ರೆ
**Kannada Bhasheya Kalpita Charitre** *(Reconstructed/Imagined History of Kannada)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** A speculative/reconstructed history of Kannada and its speakers
- **ಮೂಲ / Source:** YouTube transcript
- **ಗುಣಮಟ್ಟ / Quality:** ✅ Good (29 lines — short excerpt)
- **ಕಡತ / Folder:** [12-kannada-bhasheya-kalpita-charitre/](./12-kannada-bhasheya-kalpita-charitre/)

---

### 17 — ಕನ್ನಡ ನುಡಿ ನಡೆದು ಬಂದ ದಾರಿ
**Kannada Nudi Nadedu Banda Dari** *(The Path Travelled by the Kannada Language)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** The historical journey of Kannada from Proto-Dravidian to the present
- **ಮೂಲ / Source:** dnshankarabhat.net (offline; not yet archived in Wayback Machine)
- **ಗುಣಮಟ್ಟ / Quality:** ❌ Not yet collected
- **ಕಡತ / Folder:** [17-kannada-nudi-nadedu-banda-dari/](./17-kannada-nudi-nadedu-banda-dari/)

---

### 18 — ಕನ್ನಡ ನುಡಿಯ ಬಗೆಗೆ ಚಿಂತನೆ
**Kannada Nudiya Bagege Chintane** *(Reflections on the Kannada Language)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** Reflections on Kannada's status, future, and the responsibilities of its speakers
- **ಮೂಲ / Source:** dnshankarabhat.net (Wayback Machine — blog posts)
- **ಗುಣಮಟ್ಟ / Quality:** ✅ **13 blog posts collected** (883 lines, 206,239 bytes)
- **ಕಡತ / Folder:** [18-kannada-nudiya-bagege-chintane/](./18-kannada-nudiya-bagege-chintane/)

**Files in folder:**
| File | Contents |
|------|----------|
| `18-...-blog.md` | **13 blog posts** — *ನುಡಿಯರಿಮೆಯ ಇಣುಕುನೋಟ* series (parts 1–3, 10, 14, 18, 20, 23, 27–29, 33, 35) |

**Blog series:** *ನುಡಿಯರಿಮೆಯ ಇಣುಕುನೋಟ* ("A Glimpse into Linguistics") — a multi-part series of popular Kannada linguistics articles
- **Part 1** — ಅರಿಮೆಯ ಪದಗಳಿಗೆ ಕನ್ನಡವೇ ಮೇಲು (Kannada terms are better for science concepts)
- **Parts 2–3** — Early series covering writing systems and language basics
- **Parts 10, 14** — Dravidian language family and historical phonology
- **Parts 18, 20** — Language and society; speech vs. writing distinctions
- **Parts 23, 27–29** — Kannada grammar from a native perspective
- **Parts 33, 35** — Advanced linguistics topics

**Missing parts:** 4–9, 11–13, 15–17, 19, 21–22, 24–26, 30–32, 34, 36+ (not archived in Wayback Machine or Cloudflare-blocked)

---

## Section D — Vocabulary and Word Formation

### 15 — ಇಂಗ್ಲಿಶ್ ಕನ್ನಡ ಪದನೆರಕೆ
**Inglish Kannada Padanerake** *(English-Kannada Word Correspondence)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2015
- **ಲೇಖಕರು / Authors:** D. N. Shankara Bhat, Y. Bharath Kumar, Vivek Shankar
- **ಪುಟಗಳು / Pages:** 730+ (full book); 53-page sample (pre-print prelims, letter A)
- **ವಿಶಯ / Topic:** English words and their native Kannada equivalents (without Sanskrit mediation)
- **ಮೂಲ / Source:** PDF sample (`English-KannadaPadanerakeSample.pdf`) — hybrid extraction (pdfminer + wx_decode)
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ **Sample only** — covers A–Az (84,475 Kannada chars, 3,454 lines); full 730-page book not yet obtained
- **ಕಡತ / Folder:** [15-inglish-kannada-padanerake/](./15-inglish-kannada-padanerake/)

**Files in folder:**
| File | Contents |
|------|----------|
| `15-...-book.md` | Hybrid-extracted text from 53-page sample (letter A only) |
| `15-...-kn-eke.md` | ★ Eke romanisation of source text — munnuDi (preface) + irusarikegaLu (conventions) + A–Az dictionary entries with usage |
| `15-...-en.md` | ★ English analysis — 10 word-formation patterns documented |
| `15-...-claude-prompt.md` | ★ AI primer — 6-step decision tree, 11 domain cluster tables, 100 curated entries |

**Part-of-speech abbreviations used:**
- **ಹೆ** = ಹೆಸರುಪದ (noun)
- **ಎ** = ಎಸಕಪದ (verb)
- **ಪ** = ಪರಿಚೆಪದ (adjective/qualifier)

**Key word-formation patterns documented (from A–Az sample):**
- N+N ಜೋಡುಪದ compounds (ಅಭ್ಯಾಸ+ಮನೆ → ಅಭ್ಯಾಸಮನೆ)
- Verb-derived nouns: *-ta, -ike, -uge, -me, -vu* suffixes
- Agent nouns: *-ga, -uga, -gAra*
- ಅರಿಮೆ discipline names (ಅಣ್ವರಿಮೆ = atomic science)
- ಮನೆ institution names (ಅಡಿಗೆಮನೆ = kitchen)
- ಗಾಳಿ air-cluster (ಅರ್ಭಟಗಾಳಿ = hurricane)

---

### 16 — ನುಡಿಯರಿಮೆಯ ಪದಗಳಿಗೆ ಕನ್ನಡದ್ದೇ ಪದಗಳು
**Samskruta Padagalige Kannadade Padagalu** *(Kannada Alternatives to Sanskrit/Linguistic Terms)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** Recently released (announced on website as of 2024)
- **ವಿಶಯ / Topic:** Native Kannada replacements for Sanskrit-derived linguistic terminology
- **ಮೂಲ / Source:** dnshankarabhat.net (offline)
- **ಗುಣಮಟ್ಟ / Quality:** ❌ Not yet collected
- **ಕಡತ / Folder:** [16-samskruta-padagalige-kannadade-padagalu/](./16-samskruta-padagalige-kannadade-padagalu/)

**Known Terminology (from cross-references in other works):**
| Sanskrit | Bhat's Kannada | English |
|---|---|---|
| ನಾಮಪದ | ಹೆಸರು ಪದ | Noun |
| ಕ್ರಿಯಾಪದ | ಎಸಕ ಪದ | Verb |
| ವಿಶೇಷಣ | ಪರಿಚರಣ ಪದ | Adjective |
| ವ್ಯಾಕರಣ | ಸೊಲ್ಲರಿಮೆ | Grammar |
| ಭಾಷಾಶಾಸ್ತ್ರ | ನುಡಿಯರಿಮೆ | Linguistics |
| ಧ್ವನಿ | ಉಲಿ | Phoneme/Sound |
| ಅಕ್ಷರ | ಬರಿಗೆ | Letter/Grapheme |
| ಪ್ರತ್ಯಯ | ಮಾರ್ಪು | Suffix |

---

## Section E — Old Kannada

### 13 — ಧಾರೆಗೆ ದೊಡ್ಡವರು
**Dharege Doddavaru** *(Great Ones of the Tradition)*

- **ಭಾಷೆ / Language:** Kannada
- **ವಿಶಯ / Topic:** Survey of historical Kannada grammar and literature
- **ಮೂಲ / Source:** YouTube transcript
- **ಗುಣಮಟ್ಟ / Quality:** ❌ Heavily corrupted (49 lines)
- **ಕಡತ / Folder:** [13-dharege-doddavaru/](./13-dharege-doddavaru/)

---

### 14 — ನಿಜಕ್ಕೂ ಹಳಗನ್ನಡ ವ್ಯಾಕರಣ ಎಂತಹದು?
**Nijakku Halegannada Vyakarana Entahadu** *(What Really Is the Grammar of Old Kannada?)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2005 (1st ed.), 2015 (2nd ed.)
- **ಪ್ರಕಾಶಕರು / Publisher:** Raveendra Pustakalaya, Sagar, Shimoga
- **ಪುಟಗಳು / Pages:** 224
- **ಬೆಲೆ / Price:** ₹200
- **ಮೂಲ / Source:** [Internet Archive](https://archive.org/details/arn.nijakkuhaleganna0000dnsh) — PDF + DjVu OCR + dnshankarabhat.net blog
- **ಗುಣಮಟ್ಟ / Quality:** ✅ **Full text available** (11,791 lines book.md + 7,033 lines djvu.md + **425 lines blog**)
- **ಕಡತ / Folder:** [14-nijakku-halegannada-vyakarana-entahadu/](./14-nijakku-halegannada-vyakarana-entahadu/)

**Files in folder:**
| File | Contents |
|------|----------|
| `nijakku-...-book.md` | Full Kannada text (from archive.org) |
| `14-...-kn.md` | Structured Kannada version |
| `14-...-en.md` | English analysis/summary |
| `14-...-djvu.md` | DjVu OCR text (new — March 2026) |
| `nijakku-...-claude-prompt.md` | Analysis prompt |
| `14-...-blog.md` | **7 blog posts** — *ಶಬ್ದಮಣಿದರ್ಪಣದಲ್ಲಿ ತಳಮಟ್ಟದ ತಪ್ಪುಗಳು* series (May–June 2017) |

**Blog series:** 7-part series *ಶಬ್ದಮಣಿದರ್ಪಣದಲ್ಲಿ ತಳಮಟ್ಟದ ತಪ್ಪುಗಳು* ("Fundamental Errors in Shabdamani Darpana")
- Bhat's critical analysis of Kesiraja's 13th-century Old Kannada grammar
- Argues that the medieval grammarians misapplied Sanskrit categories to Kannada data

**Key Thesis:** The traditional description of Old Kannada grammar is mistaken because it applies Sanskrit grammatical categories. Bhat argues Old Kannada was structurally Dravidian from the beginning — the grammatical categories that scholars mistook for Sanskrit-derived were actually native Kannada patterns being described in Sanskrit meta-language.

---

## Section F — English Academic Works

### 19 — The Koraga Language
**The Koraga Language**

- **Language:** English (academic)
- **Year:** 1971
- **Publisher:** Deccan College, Poona
- **Pages:** 123
- **Topic:** Linguistic description of the Koraga language (Dravidian) of South Kanara/Udupi districts
- **Source:** PDF in Google Drive (`DNS-Bhat/the-koraga-language.pdf`)
- **Quality:** ❌ PDF not yet extracted
- **Folder:** [19-the-koraga-language/](./19-the-koraga-language/)

**Significance:** Establishes Koraga as a **distinct Dravidian language** (not a Tulu dialect). Documents three dialects: Onti, Tappu, Mudu. Also describes the related language **Belari**.

---

### 20 — An Outline Grammar of Havyaka
**An Outline Grammar of Havyaka**

- **Language:** English (academic)
- **Year:** 1971
- **Publisher:** Deccan College, Poona
- **Series:** Linguistic Survey of India Series, No. 5
- **Pages:** ~151
- **Source:** Internet Archive (`unset0000unse_a3v7`) — PDF + DjVu OCR
- **Quality:** ✅ **Full DjVu text available** (`20-havyaka-outline-grammar-djvu.md`)
- **Folder:** [20-havyaka-outline-grammar/](./20-havyaka-outline-grammar/)

**Significance:** Academic linguistic description of the Havyaka dialect — phonology, morphology, syntax, texts. Companion to the popular Kannada version in folder 09.

---

### 21 — Pronouns (Oxford University Press)
**Pronouns**

- **Language:** English (academic)
- **Year:** 2004
- **Publisher:** Oxford University Press
- **Series:** Oxford Studies in Typology and Linguistic Theory
- **Pages:** ~296
- **Source:** PDF in Google Drive (`DNS-Bhat/DNS-Bhat-Pronouns-Oxford.pdf`)
- **Quality:** ❌ PDF not yet extracted
- **Folder:** [21-dns-bhat-pronouns/](./21-dns-bhat-pronouns/)

**Significance:** Major typological work examining pronoun systems across the world's languages. Based on Bhat's decades of fieldwork including Dravidian languages.

---

## Section G — Sound Change & Historical Phonology

### 22 — Sound Change
**Sound Change**

- **Language:** English (academic)
- **Year:** 2001 (revised from 1972 original)
- **Publisher:** Motilal Banarsidass, Delhi
- **Series:** MLBD Series in Linguistics, Vol. 14
- **ISBN:** 8120817664
- **Pages:** 167
- **Source:** Google Books preview; no archive.org copy yet found
- **Quality:** ❌ Not yet collected
- **Folder:** [22-sound-change/](./22-sound-change/)

**Why it matters:** This is the theoretical backbone for books 08, 14, 26. Bhat's *mahaprana* argument (book 08) is essentially applied sound change theory — aspirated stops merged into unaspirated in Kannada through regular sound change. Examples drawn from Dravidian, Indo-Aryan, and Tibeto-Burman.

**Contents:** Characteristics of sound change · Effects (assimilation, dissimilation) · Reconstruction (comparative method, internal reconstruction) · Exercises · Index

---

### 26 — ಉಲಿ ಮಾರ್ಪಾಡಿನ ಗೆರೆಗಳು
**Uli Marpadina Geregalu** *(Laws of Sound Change)*

- **Language:** Kannada
- **Year:** June 2024 *(one of Bhat's last publications)*
- **Source:** dnshankarabhat.net (Wayback snapshot exists but Cloudflare-blocked)
- **Quality:** ❌ Not yet collected (snapshot at 2024-06-21 blocked)
- **Folder:** [26-uli-marpadina-geregalu/](./26-uli-marpadina-geregalu/)

**Why it matters:** Bhat's Kannada-language popularization of sound change theory — the companion to the English *Sound Change* textbook. Published in 2024, one of his most recent writings.

---

## Section H — Syntax

### 25 — ಕನ್ನಡ ವಾಕ್ಯಗಳ ಒಳರಚನೆ
**Kannada Vakyagala Olarachane** *(Internal Structure of Kannada Sentences)*

- **Language:** Kannada
- **Year:** 2016 (original), 2019 (expanded: + ಅರ್ಥ ವ್ಯವಸ್ಥೆ)
- **Source:** dnshankarabhat.net (archived 2016, 2019 — not yet fetched)
- **Quality:** ❌ Not yet collected
- **Folder:** [25-kannada-vakyagala-olarachane/](./25-kannada-vakyagala-olarachane/)

**Why it matters:** Completes the grammar trilogy alongside word-structure (→ 03) and grammar (→ 01): phonology → morphology → **syntax**.

---

## Section I — Additional Academic Works

### 23 — A Grammar of Manipuri
**A Grammar of Manipuri** (+ Kannada version)

- **Language:** English (+ Kannada version exists)
- **Co-author:** M. S. Ningomba
- **Source:** dnshankarabhat.net (archived 2015, 2018)
- **Quality:** ❌ Not yet collected
- **Folder:** [23-manipuri-grammar/](./23-manipuri-grammar/)

---

### 24 — Grammatical Relations
**Grammatical Relations: The Evidence Against Their Necessity and Universality**

- **Language:** English
- **Published in:** *Theoretical Linguistics* (journal)
- **Source:** dnshankarabhat.net (archived 2016, 2018)
- **Quality:** ❌ Not yet collected
- **Folder:** [24-grammatical-relations/](./24-grammatical-relations/)

---

## Section K — Newly Discovered Books (Google Drive, 2026-03-10)

### 27 — ಭಾಷೆಯ ಬಗ್ಗೆ
**Baasheya Bagge** *(About Language / What Do You Know About Language?)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 1970 (1st edition); 1998 (2nd rev.); 2002 (3rd expanded); 2010 (4th edition)
- **ಪ್ರಕಾಶಕರು / Publisher:** Bhasha Prakashan, Heggodu, Sagara
- **ಪುಟಗಳು / Pages:** 208
- **ವಿಶಯ / Topic:** General introduction to linguistics — what language is, how it works, diversity of languages
- **ಮೂಲ / Source:** PDF in Google Drive (`baasheyaBagge.pdf`) — 4th edition
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ PDF extracted but old WX Kannada font — text garbled; awaiting OCR
- **ಕಡತ / Folder:** [27-baasheya-bagge/](./27-baasheya-bagge/)

**Full title:** *ಭಾಷೆಯ ಬಗ್ಗೆ ನೀವೇನು ಬಲ್ಲಿರಿ?* (Baasheya Bagege Niivenu Balliri?)
**Significance:** Bhat's popular introduction to linguistics for Kannada-speaking general audiences. One of his earliest and most reprinted works (4 editions over 40 years). Covers language universals, the Dravidian family, and Kannada's place among world languages.

---

### 28 — ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ
**kannaDakke bEku kannaDaddE vyAkaraNa** *(Kannada Needs Its Own Grammar)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2000 (1st edition); 2013 (7th edition)
- **ಪ್ರಕಾಶಕರು / Publisher:** © DNS Bhat (self-published)
- **ಪುಟಗಳು / Pages:** 253
- **ವಿಶಯ / Topic:** Advocacy for a Kannada-native grammar — critique of Sanskrit-based grammatical tradition
- **ಮೂಲ / Source:** PDF in Google Drive (`kannadakkeBeku.pdf`) — 7th edition
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ PDF extracted but old WX Kannada font — text garbled; awaiting OCR
- **ಕಡತ / Folder:** [28-kannadakke-beku/](./28-kannadakke-beku/)

**Full title:** *ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ* (kannaDakke bEku kannaDaddE vyAkaraNa)
**Significance:** Popular advocacy booklet that went to 7 editions — one of Bhat's most widely read works. Argues that Kannada needs its own grammar built from Kannada-internal structure (the position developed formally in the Sollarime series). Companion to Book 29.

---

### 29 — ಕನ್ನಡ ವ್ಯಾಕರಣ ಯಾಕೆ ಬೇಕು?
**Kannada Vyakarana Yaake Beku** *(Why Do We Need Kannada Grammar?)*

- **ಭಾಷೆ / Language:** Kannada
- **ಪ್ರಕಟಣೆ / Year:** 2009 (1st edition)
- **ಪ್ರಕಾಶಕರು / Publisher:** Bhasha Prakashan, Heggodu, Sagara
- **ಪುಟಗಳು / Pages:** 260
- **ವಿಶಯ / Topic:** Motivating case for studying Kannada grammar — who needs it, why, and how it should differ from Sanskrit grammar
- **ಮೂಲ / Source:** PDF in Google Drive (`kannadavyakaranayaakebeku.pdf`) — written in *hosa baraha* (new script)
- **ಗುಣಮಟ್ಟ / Quality:** ⚠️ PDF extracted but old WX Kannada font — text garbled; awaiting OCR
- **ಕಡತ / Folder:** [29-kannada-vyakarana-yaake-beku/](./29-kannada-vyakarana-yaake-beku/)

**Note:** This book is written in *hosa baraha* (Bhat's simplified Kannada orthography without mahapranas). PDF metadata confirms it.
**Significance:** Companion to Book 28. Where Book 28 argues *what kind* of grammar Kannada needs, Book 29 argues *why* grammar matters at all — aimed at skeptical general readers. Together they form the popular-level introduction to the Sollarime project.

---

## Section J — Other Known Works (Not Yet Collected)

These works are referenced in collected texts or found in the CDX sitemap but not yet fully collected:

| Title | Slug / Notes |
|-------|-------|
| *Kannada Barahavasthu Saripadisona* | `ಕನ್ನಡ-ಬರಹವನ್ನು-ಸರಿಪಡಿಸೋಣ` — "Let's fix Kannada spelling" — referenced in book 08; site archived 2015 |
| *Odu Hage Bareyuvudu* | `ಓದುವ-ಹಾಗೆಯೇ-ಬರೆಯುವುದು` — "Write as you read" — site archived 2021 |
| *Nudigala Naduvina Nantastike* | `ನುಡಿಗಳ-ನಡುವಿನ-ನಂಟಸ್ತಿಕೆ` — "Language Relationships" — site archived 2022 |
| *Dravida Nudigalu Aydalla* | `ದ್ರಾವಿಡ-ನುಡಿಗಳು-ಅಯ್ದಲ್ಲ` — "Dravidian Languages are Not Five" — site archived 2021 |
| *Kannada Nudi Estu Haleyadu* | `ಕನ್ನಡ-ನುಡಿ-ಎಶ್ಟು-ಹಳೆಯದು` — "How Old Is Kannada?" — site archived 2022 |
| *Shabdamani Darpanada Talamata* | 7-part series on the medieval Kannada grammar *Shabdamani Darpana* — site archived 2017 |
| *Ariimeya Padagalige Kannadave Ma-* | `ಅರಿಮೆಯ-ಪದಗಳಿಗೆ-ಕನ್ನಡವೇ-ಮ` — "Kannada for Scientific Terms" — site archived 2021 |
| *Ariimeya Barahagala Todakugalu* | `ಅರಿಮೆಯ-ಬರಹಗಳ-ತೊಡಕುಗಳು` — "Problems in Academic Writing" — site archived 2024 |
| *Baraha Kannada Mattu Adugannada* | `ಬರಹ-ಕನ್ನಡ-ಮತ್ತು-ಆಡುಗನ್ನಡ` — "Written Kannada vs Spoken Kannada" — site archived 2020 |
| *Retroflexion: An Areal Feature* (1973) | English academic paper (Stanford Working Papers on Language Universals No. 13) — in archive.org |
| Various articles in international journals | *Linguistics*, *Language*, *Journal of Linguistics* etc. |
| Contributions to *The Dravidian Languages* (Cambridge) | Cambridge Language Surveys chapter |

---

## Collection Statistics

| Category | Count | Full Text | Blog Content | PDF (WX) | Partial | Not Collected |
|----------|-------|-----------|--------------|----------|---------|---------------|
| Kannada popular books (collected) | 17 | 4 | 3 | 8 | 3 | 1 |
| Kannada popular books (not collected) | 1 | 0 | 0 | 0 | 0 | 1 |
| English academic monographs | 3 | 1 | 0 | 0 | 0 | 2 |
| **Newly discovered books (27–29)** | **3** | **0** | **0** | **3** | **0** | **0** |
| **Book 15 — hybrid extracted sample** | **1** | **0** | **0** | **0** | **1 (A only)** | **0** |
| **Total** | **25** | **5** | **3** | **11** | **4** | **4** |

> ℹ️ Book 15 counting: moved from "Partial" to its own row. 53-page sample (letter A) is hybrid-extracted and fully processed (en/kn-eke/claude-prompt). Full 730-page book not yet obtained.

> ⚠️ **WX font PDFs** — Books extracted from old Ghostscript/PageMaker PDFs have garbled text due to non-Unicode Kannada font encoding. A Unicode-aware OCR pass (e.g. Tesseract with Kannada model) is needed to recover clean text.

**Full text available (best quality):**
- 08 — Kannadakke Mahaprana Yake Beda (102 pp, 2017) — PDF + DjVu
- 14 — Nijakku Halegannada Vyakarana Entahadu (224 pp, 2005/2015) — PDF + DjVu + **7 blog posts**
- 20 — An Outline Grammar of Havyaka (151 pp, 1971) — DjVu

**Blog content collected (from dnshankarabhat.net via Wayback Machine):**
- 02 — Kannadalle Hosapadagalannu Kattuva Bage — 15 blog posts (6,469 lines, parts 4–18)
- 14 — Nijakku Halegannada Vyakarana Entahadu — 7 blog posts (425 lines, Shabdamani series)
- 18 — Kannada Nudiya Bagege Chintane — 13 blog posts (883 lines, Inukunota parts 1–3, 10, 14, 18, 20, 23, 27–29, 33, 35)

---

## Google Drive: DNS-Bhat Folder

Location: `My Drive/Books/DNS-Bhat/`

| File | Book # | Format |
|------|--------|--------|
| `08-kannadakke-mahaprana-yake-beda.pdf` | 08 | PDF (4.5 MB) |
| `08-kannadakke-mahaprana-yake-beda-djvu.txt` | 08 | DjVu OCR text |
| `14-nijakku-halegannada-vyakarana-entahadu.pdf` | 14 | PDF (16.8 MB) |
| `14-nijakku-halegannada-vyakarana-entahadu-djvu.txt` | 14 | DjVu OCR text |
| `09-havyaka-outline-grammar-1971.pdf` | 20 | PDF |
| `09-havyaka-outline-grammar-1971-djvu.txt` | 20 | DjVu OCR text |
| `the-koraga-language.pdf` | 19 | PDF |
| `DNS-Bhat-Pronouns-Oxford.pdf` | 21 | PDF |
| `KannadaPadagalaOlarachane.pdf` | 03 | PDF (239p, 2014) — ⚠️ WX font |
| `KannadaVakyagalaOlaracane.pdf` | 25 | PDF (289p, 2014) — ⚠️ WX font |
| `kannada-nudi-nadedu-banda-dari.pdf` | 17 | PDF (405p, 2014) — ⚠️ WX font |
| `sollarime-1.pdf` | 07 vol.1 | PDF (327p, 2010) — ⚠️ WX font |
| `sollarime-2.pdf` | 07 vol.2 | PDF (301p, 2014) — ⚠️ WX font |
| `sollarime_5_limited.pdf` | 07 vol.5 | PDF (30p sample, 2015) |
| `baasheyaBagge.pdf` | **27** | PDF (208p, 4th ed. 2010) — ⚠️ WX font |
| `kannadakkeBeku.pdf` | **28** | PDF (253p, 7th ed. 2013) — ⚠️ WX font |
| `kannadavyakaranayaakebeku.pdf` | **29** | PDF (260p, 2009) — ⚠️ WX font |
| `English-KannadaPadanerakeSample.pdf` | 15 | PDF sample/prelims (53p, 2015) |

---

## Thematic Index for Linguistics Exercise

### Theme 1: Script Reform (Kannada Writing System)
- **08** — Mahaprana Yake Beda (primary source — aspirated consonants)
- **07** — Kannadada Sollarime (comprehensive grammar/writing system)
- **11** — Kannada Barahada Padasamasye (orthographic problems)
- **04** — Mathu Matthu Barahada Gondala (speech vs. writing)

### Theme 2: Dravidian Grammar (Native Structure)
- **01** — Idu Kannadade Vyakarana (native grammar framework)
- **03** — Kannada Padagala Olarachane (word structure)
- **14** — Nijakku Halegannada Vyakarana (Old Kannada grammar)
- **21** — Pronouns/Oxford (typological framework)

### Theme 3: Word Formation (New Vocabulary)
- **02** — Hosapadagalannu Kattuva Bage (forming new words)
- **15** — Inglish Kannada Padanerake (English → Kannada)
- **16** — Samskruta Padagalige Kannadade Padagalu (Sanskrit → Kannada)

### Theme 4: History of Kannada
- **10** — Kannada Nudiya Hinnadavali (language history)
- **12** — Kalpita Charitre (reconstructed history)
- **17** — Nudi Nadedu Banda Dari (path of the language)
- **18** — Nudiya Bagege Chintane (reflections)

### Theme 6: Sound Change & Historical Phonology
- **22** — Sound Change (primary textbook, English)
- **26** — ಉಲಿ-ಮಾರ್ಪಾಡಿನ-ಗೆರೆಗಳು (Kannada, 2024)
- **08** — Mahaprana Yake Beda (applied: aspiration merger in Kannada)
- **14** — Nijakku Halegannada Vyakarana (historical: Old Kannada phonology)
- **19** — The Koraga Language (comparative Dravidian phonology)

### Theme 7: Endangered Dravidian Languages
- **09 / 20** — Havyaka (dialect documentation)
- **19** — Koraga Language (endangered language)
- **21** — Pronouns (typological context)

---

## About Dr. D. N. Shankara Bhat

D. N. Shankara Bhat is a towering figure in Indian linguistics, combining
rigorous academic work with passionate language advocacy for Kannada.

**Academic positions:** Deccan College (Poona), Trivandrum, Manipur, Leeds, Stanford, Antwerp, Max Planck Institute, La Trobe
**Degrees:** M.A. in Sanskrit, Ph.D. in Linguistics
**Awards:** Pampa Award (Karnataka's highest literary honour)
**Languages studied:** Kannada, Havyaka, Koraga, Belari, and many world languages (typological work)

**Two pillars of his work:**
1. **International typology** — How do the world's languages differ in grammar? (English academic works, Oxford)
2. **Kannada reform** — Applying typological insight to argue Kannada needs its own grammar, not a borrowed one (Kannada popular works)

**Website:** dnshankarabhat.net *(currently offline — was active until ~2025)*
