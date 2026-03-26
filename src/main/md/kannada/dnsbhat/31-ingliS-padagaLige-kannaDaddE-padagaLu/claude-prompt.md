# Claude Prompt — Book 31: ಇಂಗ್ಲಿಶ್ ಪದಗಳಿಗೆ ಕನ್ನಡದ್ದೇ ಪದಗಳು

**English title:** Kannada's Own Words for English Words
**Author:** D. N. Shankara Bhat (solo work)
**Published:** 2008 (1st ed.); 2011 (2nd ed.) · Bāshā Prakāshana, Billeshwara, Huncha, Tirthahalli
**Pages:** 487 · Language: Kannada (*hosa baraha* reformed script)

---

## THESIS

An A-to-Z dictionary that inverts the typical English–Kannada glossary: instead of explaining English words to Kannada speakers who don't know English, this book is for speakers who know English well and want to discover **what native Dravidian Kannada words** exist for common English vocabulary. The book argues that for almost every English concept, native Kannada equivalents already exist — speakers just don't know them because generations of writers have reached for Sanskrit instead.

This is an earlier, opinionated companion to Book 15 (*Inglish Kannada Padanerake*, 2015). Book 31 (solo, 487pp) is a curated selection; Book 15 (collaborative, 730pp) is the comprehensive A–Z successor.

---

## STRUCTURE

**Two-part book:**

1. **Preface / Introduction** (~120 pages): explains methodology and demonstrates native Kannada word-formation principles:
   - The *triśaṅku pada* problem (Sanskrit–Kannada hybrids)
   - Native suffix system: -gāra, -āḷi (agents); -ke/-ike, -ge/-ige, -ta, -vu/-pu/-hu, -me, -ha (actions/results)
   - Negation without Sanskrit prefix *a-* (use negating verbal form instead)
   - Compound formation and reduplication as native Dravidian strategies

2. **A–Z Dictionary** (~370 pages): English headwords with Kannada equivalents + example sentences
   - Format: `[English word]` / `[PoS: ಕ್ರಿ=verb, ನಾ=noun, ಗು=adj]` / `[Kannada equivalent(s)]` / `(example sentences)`

---

## KEY WORD-FORMATION EXAMPLES

| English concept | Native Kannada | Root |
|----------------|---------------|------|
| knowledge | ಅರಿವು, ಅರಿಮೆ, ಅರಿತ, ಅರಿಕೆ, ಅರಿಹ | ಅರಿ (to know) |
| science | ಅರಿಮೆ | ಅರಿ |
| patience | ತಾಳ್ಮೆ | ತಾಳ್ (to endure) |
| trust | ನಂಬಿಕೆ | ನಂಬ್ (to believe) |
| death | ಸಾವು | ಸಾ (to die) |
| dance | ಕುಣಿತ | ಕುಣಿ (to dance) |
| miscarriage | ಮಯ್ಯಿಳಿತ, ಬಸಿರಿಳಿತ | native compounds |
| zoo | ಉಸುರಿಮನೆ | ಉಸಿರು (breath/life) + ಮನೆ (house) |
| zoology | ಉಸಿರಿಯರಿಮೆ | ಉಸಿರಿ + ಅರಿಮೆ |

---

## REPOSITORY SOURCE

**Raw OCR text:** `book/kn/raw.md` — 2.8M chars; source from a Baraha-font PDF with CID-encoded glyphs.

**Decoded dictionary:** `book/kn/full.md` — **12,121 entries fully decoded to Unicode Kannada** (Phase 27, 2026-03-23). All `(cid:N)` glyph tokens resolved via three-range CID offset rule + Baraha cp1252 → wx_decode pipeline. Only 2 spurious OCR-artifact headwords remain garbled; all genuine dictionary entries are clean. Entry format: `**headword** — [PoS] Kannada equivalents (example sentences)`.

**English summary:** `book/en/summary.md` — methodology overview, word-formation tables, sample entries.

**Note:** No Eke file (dictionary length makes full romanisation impractical).

---

## CONNECTIONS TO OTHER BOOKS

- **Book 15** (*Inglish Kannada Padanerake*, 2015): the collaborative, comprehensive A–Z successor
- **Book 14** (*Nijakku Halegannada Vyākarana Entahadu*): grammar framework underlying the suffix system documented here
- **Book 30** (*Kannadavannu Saripaḍisōṇa*): the script reform companion — Book 31 is written throughout in Bhat's *hosa baraha* script
- **Book 08** (*Kannadakke Mahāprāṇa Yāke Bēḍa*): the *mahāprāṇa* argument — all headwords in this dictionary avoid aspirated consonants in their Kannada equivalents

---

## INSTRUCTIONS FOR ANSWERING QUESTIONS

1. **Book 31 is a dictionary** — when asked about a specific English word, look it up in `book/kn/full.md` (12,121 entries fully decoded to Unicode).
2. When asked about word-formation methodology, draw on the Preface/Introduction (~120 pages): native suffix system (-gAra, -ALi, -ke/-ike, -ge/-ige, -ta, -vu/-pu/-hu, -me, -ha), negation without *a-*, compound formation.
3. When asked about the difference between Books 31 and 15, note: Book 31 (2008, solo, 487pp) is the earlier curated selection; Book 15 (2015, collaborative, 730pp) is the comprehensive A–Z successor.
4. Entry format in the dictionary: `**headword** — [PoS] Kannada equivalents (example sentences)`.
5. **Chapter pages (Phase 32):** `book/kn/full.md` now has `<a id="chN">` anchors before each letter section (A=ch1 through W=ch19, 19 chapters total). CI generates `ch1.md`…`ch19.md` + `ch0.md` index. Access via chapter page links.
6. Always note that this book uses *hosa baraha* reformed orthography throughout: aspirated consonants in native Kannada equivalents are systematically avoided.

7. **Chapter pages (Phase 33):** The Kannada source is split into individual chapter pages on GitHub Pages. Fetch specific chapters rather than loading the full book — chapters are lightweight and avoid token exhaustion when answering focused questions:
   - **Chapter index (ch0):** `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch0`
   - Ch 1 — A: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch1`
   - Ch 2 — B: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch2`
   - Ch 3 — C: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch3`
   - Ch 4 — D: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch4`
   - Ch 5 — E: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch5`
   - Ch 6 — F: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch6`
   - Ch 7 — G: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch7`
   - Ch 8 — I: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch8`
   - Ch 9 — K: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch9`
   - Ch 10 — L: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch10`
   - Ch 11 — M: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch11`
   - Ch 12 — N: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch12`
   - Ch 13 — O: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch13`
   - Ch 14 — Q: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch14`
   - Ch 15 — R: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch15`
   - Ch 16 — T: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch16`
   - Ch 17 — U: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch17`
   - Ch 18 — V: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch18`
   - Ch 19 — W: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch19`
   
   When a question targets a specific chapter, fetch only that URL. Use `ch0` to browse the full chapter list first.
