---
name: vetted-kannaDa-dictionary
description: >
  Look up D. N. Shankara Bhat's settled native Kannada equivalents for English words
  before coining anything new. Draws on Book 31 (12,121-entry A-W dictionary, all
  letters except H J P S X Y Z) and Book 15 (letter-A sample only). Precedence rule:
  VETTED-15 > VETTED-31 > COINED. Trigger phrases: "what did Bhat use for X",
  "look up X in the dictionary", "vetted word for", "is there a settled Kannada word for",
  "Bhat's word for", "check the dictionary first", "ಬಟ್ ಅವರ ಪದ", "Book 31", "Book 15".
---

# Skill: vetted-kannaDa-dictionary

_Look up Bhat's settled native Kannada equivalents for English words before coining anything new_

---

# Vetted Kannada Dictionary

You look up **D. N. Shankara Bhat's own settled native Dravidian Kannada words** for English
concepts, drawn from his two dictionary books. These are *vetted* coinages — not generated fresh,
but established by Bhat himself through careful native-root selection. They take precedence over
any independently coined word.

The two source books:

- **Book 31** — *ಇಂಗ್ಲಿಶ್ ಪದಗಳಿಗೆ ಕನ್ನಡದ್ದೇ ಪದಗಳು* (2008/2011, 487 pp, solo).
  A–Z dictionary, 12,121 entries, written throughout in *hosa baraha* (no mahapranas). The earlier,
  curated work.
- **Book 15** — *ಇಂಗ್ಲಿಶ್-ಕನ್ನಡ ಪದನೆರಕೆ* (2015, 730 pp, collaborative: Bhat + Bharath Kumar +
  Vivek Shankar). Comprehensive A–Z successor, 5,000+ entries. Letter A sample only (53 pp) is
  currently extracted; full book not yet digitised.

---

## Precedence Rule

When a word appears in both books, **Book 15 takes precedence** (later, collaborative, more
comprehensive). When it appears in Book 31 only, use that. When it appears in neither, fall through
to fresh coining via the `ellara-kannada-word-coiner` skill.

```
VETTED-15  >  VETTED-31  >  COINED (ellara-kannada-word-coiner)
```

Always label the result with its source so the user knows what they are getting.

---

## Lookup Workflow

### Step 1 — Identify the first letter of the English headword

Map to the Book 31 chapter URL:

| Letter | Chapter | Letter | Chapter |
|--------|---------|--------|---------|
| A | ch1 | L | ch10 |
| B | ch2 | M | ch11 |
| C | ch3 | N | ch12 |
| D | ch4 | O | ch13 |
| E | ch5 | Q | ch14 |
| F | ch6 | R | ch15 |
| G | ch7 | T | ch16 |
| I | ch8 | U | ch17 |
| K | ch9 | V | ch18 |
| | | W | ch19 |

**Note:** Letters H, J, P, S, X, Y, Z are not present — Book 31 does not cover them.

**Base URL for Book 31 chapters:**
`https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu`

Full chapter URL example for letter C:
`https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch3`

Chapter index (browse all letters):
`https://vwulf.github.io/ettuge/kannaDa/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/book/kn/ch0`

### Step 2 — Fetch the chapter and search for the headword

Use `web_fetch` on the chapter URL. Search the result for the English headword (case-insensitive).
Entry format in Book 31:

```
**headword** — [PoS] ಕನ್ನಡ equivalent(s) (example sentence in Kannada)
```

Part-of-speech abbreviations in Book 31 entries:
- `ಕ್ರಿ` = verb (ಎಸಕಪದ / esakapada)
- `ನಾ` = noun (ಹೆಸರುಪದ / hesarupada)
- `ಗು` = adjective/qualifier (ಪರಿಚೆಪದ / paricepada)

When an entry gives multiple Kannada equivalents, the **first listed is Bhat's preferred form**.
Subsequent alternatives are acceptable but secondary.

### Step 3 — Check Book 15 for letter-A words

If the headword starts with **A**, also check Book 15's sample (letter A only is available).

Local file path:
`/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/15-ingliS-kannaDa-padanerake/book/kn/sample.md`

Book 15 entry format differs slightly — headword followed by Kannada equivalent(s), part-of-speech
abbreviations (ಹೆ = noun, ಎ = verb, ಪ = adjective), and usage notes. If Book 15 has the word,
its form takes precedence over Book 31.

### Step 4 — Apply Eke romanization

Book 31 entries do **not** include Eke romanization (the book predates the Eke system). Book 15
entries have Eke only for the 100 curated words in `claude-prompt.md`. For **all** lookups,
apply Eke romanization to the Kannada result yourself before returning it. Follow standard Eke rules:
long vowels uppercase (A/I/U/E/O), retroflexes uppercase (T/D/N/L), aspirates with h-marker,
anusvara always assimilated (never M).

### Step 5 — Fall through to fresh coining

If the word is not found in either book, invoke the `ellara-kannada-word-coiner` skill. Label
the result `COINED` and note it is not yet vetted by Bhat.

---

## Output Format

Single lookup:

```
**English:** <word>
**Source:** VETTED — Book 15 / VETTED — Book 31 / COINED (not yet vetted)
**Kannada:** <ಕನ್ನಡ ಲಿಪಿ>
**Eke:** <romanization>
**PoS:** noun / verb / adjective
**Breakdown:** <root analysis — include when the structure is non-obvious>
**Example:** <example sentence from the dictionary entry, if present>
```

Batch lookup — use a table:

| English | Kannada | Eke | PoS | Source |
|---------|---------|-----|-----|--------|
| arson | ಕಿಚ್ಚಿಡುಗೆ | kiccIDuge | noun | VETTED-15 |
| autonomy | ತನ್ನಾಳ್ಕೆ | tannALke | noun | VETTED-15 |
| algorithm | ಎಸಗುಬಗೆ | esagubge | noun | VETTED-15 |
| zoo | ಉಸುರಿಮನೆ | usurumane | noun | VETTED-31 |

---

## Key Word-Formation Patterns in the Dictionaries

These patterns recur throughout both books. Knowing them helps interpret entries and extend
the vocabulary into uncovered domains:

| Pattern | Formula | Examples from books |
|---------|---------|-------------------|
| Semantic N+N compound | [modifier] + [head] | ಗಾಳಿತೇರು (aircraft), ಗಾಳಿರೇವು (airport), ಕೊಲ್ಲುಮನೆ (abattoir) |
| Discipline name | [domain] + ಅರಿಮೆ | ಲೆಕ್ಕದರಿಮೆ (arithmetic), ಪಳಮೆಯರಿಮೆ (archaeology) |
| Action noun (-ta) | verb + -ತ | ತೊರೆತ (abandonment), ಕುಣಿತ (dance) |
| Action noun (-ike) | verb + -ಇಕೆ | ಹಂಚಿಕೆ (distribution), ನಂಬಿಕೆ (trust) |
| Action noun (-uge) | verb + -ಉಗೆ | ಕಿಚ್ಚಿಡುಗೆ (arson), ತೊಡುಗೆ (ornament) |
| Process noun (-ANike) | verb + -ಆಣಿಕೆ | ನೀಗಾಣಿಕೆ (abolition) |
| Agent noun (-ga/-uga) | verb + -ಗ / -ಉಗ | ಹಾರಿಸುಗ (abductor), ಪೂಣಿಗ (archer) |
| Agent noun (-gAra) | noun + -ಗಾರ | ತೀರ್ಪುಗಾರ (arbitrator), ಆಡಳಿತಗಾರ (administrator) |
| Institution | [activity] + ಮನೆ | ಕೊಲ್ಲುಮನೆ (abattoir), ಉಸುರಿಮನೆ (zoo) |
| Self/auto- | ತನ್ನ- prefix | ತನ್ನಾಳ್ಕೆ (autonomy), ತನ್ನಾಳ್ವಿಕೆ (self-rule) |
| Air/sky cluster | ಗಾಳಿ- prefix | ಗಾಳಿಚೀಲ (airbag), ಗಾಳಿತಡೆ (airlock) |
| Medical treatment | [agent] + ಮಾಂಜುಗೆ | ಬೇನೆಮಾಂಜುಗೆ (allopathy), ಕಂಪುಮಾಂಜುಗೆ (aromatherapy) |
| Ancient/paleo- | ಪಳ- prefix | ಪಳಮೆಯರಿಮೆ (archaeology) |
| Foreign/outer | ಹೊರ- prefix | ಹೊರನಾಡಿಗ (alien/foreigner) |

---

## Important Notes on Both Books

**Script:** Both books use Bhat's *hosa baraha* reformed orthography. Native Kannada equivalents
**never use mahapranas (aspirated consonants)** — this is a built-in quality signal. If you see
ಥ, ಭ, ಫ, ಧ etc. in a Kannada entry, it is a Sanskrit loanword being glossed, not a native coinage.

**Multiple equivalents:** When 2–3 options are listed, the first is Bhat's preferred form.
Others are acceptable alternatives with slightly different register or nuance.

**Example sentences:** Book 31 entries include short Kannada example sentences demonstrating
usage. Include these in output when present — they often disambiguate between multiple equivalents.

**Coverage gaps in Book 31:** Letters H, J, P, S, X, Y, Z have no chapter pages. For English
words starting with these letters, skip directly to the `ellara-kannada-word-coiner` fallback.

**Book 15 letter-A coverage:** The 53-page sample covers A through approximately "Az". It is
a pre-print proof, so some entries may differ slightly from the published 2015 edition.

---

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| `ellara-kannada-word-coiner` | Downstream fallback — invoke when no vetted entry found |
| `kannada-morphology` | Apply after lookup to inflect the found word (case, tense, agreement) |
| `dns-bhat-book-summarizer` | Used to process raw Book 15/31 source files into structured form |

**Always run this skill first** when asked to find or coin a Kannada word for an English concept.
Vetted > coined. A word Bhat himself settled is stronger evidence than any fresh derivation.
