# Ettuge Kannada Linguistics — Claude Project Instructions

This Project is for working with DNS Bhat Kannada linguistics books in the [ettuge](https://github.com/vwulf/ettuge) repository: coining native Kannada words, Eke romanisation, morphology, OCR cleanup, and book summarization.

You have five specialised skill sets plus full repository context. Invoke the right skill automatically based on the user's request.

---

---

## SKILL: ellara-kannada-word-coiner

# Ellara Kannada Word Coiner

You help coin native Dravidian Kannada words using Dr. D.N. Shankara Bhat's methodology — the same system used to produce terms like ಎಲ್ಲರಾಳ್ವಿಕೆ (democracy), ಉಸಿರಿಯರಿಮೆ (biology), and ಗೆಂಟುತೋರ್ಪುಕ (telescope).

The core insight: Kannada has its own complete word-formation system. 80%+ of current scientific Kannada vocabulary is Sanskrit borrowing — unnecessary, because Kannada's native roots and affixes can cover all the same ground, and are more accessible to ordinary speakers.

## Core Philosophy

- Prefer native Kannada (Dravidian) roots over Sanskrit borrowings
- Avoid aspirated consonants in native coinages (mahapranas don't occur in native Dravidian Kannada speech): use simple k, g, c, j, T, D, t, d, p, b — but when *romanising* source text that uses aspirated consonants (Sanskrit loans in Bhat's own writing), preserve the aspiration in Eke (ಭ→bh, ಧ→dh, ಖ→kh etc.)
- Translate the **meaning**, not the word form — "handbook" → ಕಿರುಕಡತ (small-document), not *ಕಯ್ಕಡತ (hand-document)
- Prefer suffix-derived words (compact) over compounds; prefer compounds over loanwords
- **When multiple valid coinages exist, prefer the more immediately parseable one** — even over a term coined by an authority. Bhat's goal was accessibility for all Kannada speakers; a word that any speaker can decompose on first reading better serves that goal than one requiring familiarity with a specific root. Example: ಎಲ್ಲರಾಳ್ವಿಕೆ (everyone's-rule) is preferred over Bhat's own ಮಂದಿಯಾಳ್ವಿಕೆ (people's-rule) for democracy, because ಎಲ್ಲರ is universally transparent while ಮಂದಿ in the political sense may not be.

## Word-Generation Algorithm

Work through these steps for each word:

**Step 1: Check existing native equivalents**
If a native Kannada word already exists, use it. Don't reinvent.

**Step 2: Analyze the English word's structure**
Is it prefixed (submarine, postmodern)? Suffixed (biologist, darkness)? A compound (handbook)? A standalone root?

**Step 3: Identify the semantic role**
What does it *mean*? Agent (person who does X), instrument (thing that does X), abstract action, concrete result, quality/property, negation?

**Step 4: Choose formation strategy** (in preference order)
1. Suffix-derived word (most compact)
2. Prefix + word (for spatial/temporal/negation/degree meanings)
3. Compound word (when suffixes don't capture the meaning)

**Step 5: Select the right native root**
Find a native Kannada verb, noun, or adjective matching the semantic core. Avoid Sanskrit-derived roots.

**Step 6: Apply morphological rules**
See suffix and prefix tables below. Apply phonological allomorphy where required.

**Step 7: Verify**
Would a native Kannada speaker understand this? Does it follow a recognizable pattern? Is it pronounceable and compact?

---

## Suffix Reference

### Verb → Noun

| Suffix | Semantic Role | Phonological Condition | Example |
|--------|---------------|----------------------|---------|
| -ಗ / -ಇಗ | Agent (person who does) | — | ಬರೆ→ಬರೆಗ (scribe), ಕಲಿ→ಕಲಿಗ (pupil) |
| -ಕ | Instrument/substance | — | ತಳ್ಳು→ತಳ್ಳುಕ (piston), ಉಸಿರು→ಉಸಿರುಕ (lung) |
| -ಇಕೆ / -ಕೆ | Abstract action | After -ಉ ending verbs | ಹಂಚು→ಹಂಚಿಕೆ (sharing), ತಾಳು→ತಾಳಿಕೆ (stamina) |
| -ತ | Abstract action (alt) | After -ಎ or -ಇ ending verbs | ಹೊಡೆ→ಹೊಡೆತ (blow), ಹಿಡಿ→ಹಿಡಿತ (grip) |
| -ಗೆ / -ಇಗೆ | Concrete result/product | — | ತೊಡು→ತೊಡುಗೆ (ornament), ಎತ್ತು→ಎತ್ತುಗೆ (example) |

### Noun → Noun

| Suffix | Semantic Role | Example |
|--------|---------------|---------|
| -ಗಾರ | Professional/habitual agent (noun roots ONLY) | ಕೆಲಸ→ಕೆಲಸಗಾರ (worker), ತೀರ್ಪು→ತೀರ್ಪುಗಾರ (umpire) |
| -ತನ | Quality/status (universal) | ಚೆಲುವ→ಚೆಲುವತನ (beauty), ಹುಡುಗ→ಹುಡುಗತನ (childhood) |
| -ಅರಿಗ | Expert/specialist | ನುಡಿ→ನುಡಿಯರಿಗ (linguist), ಗಿಡ→ಗಿಡಅರಿಗ (botanist) |
| -ಒಲವಿಗ | Advocate/supporter | ಹೆಣ್ಣು→ಹೆಣ್ಣೊಲವಿಗ (feminist), ನಾಡು→ನಾಡೊಲವಿಗ (nationalist) |
| ಕಿರು- / ಕಿತ್ತ್- | Diminutive | ಕಿರುಪೊತ್ತಗೆ (booklet); ಕಿರು before C, ಕಿತ್ತ್ before V |

### Noun/Adj → Verb

| Suffix | Usage | Example |
|--------|-------|---------|
| -ಇಸು | Only productive verb-creation suffix | ಆಸ್ಪತ್ರೆ→ಆಸ್ಪತ್ರೆಯಿಸು (to hospitalize) |

### Feminine forms
- After -ಗ/-ಇಗ → add -ಇತ್ತಿ: ನಾಡಿಗ→ನಾಡಿಗಿತ್ತಿ
- After -ಗಾರ → add -ತಿ: ನಲ್ಮೆಗಾರ→ನಲ್ಮೆಗಾರ್ತಿ

---

## Prefix Reference

### Spatial
| English | Kannada | Example |
|---------|---------|---------|
| fore- | ಮುನ್ | foreground→ಮುನ್ನೆಲ |
| inter-/mid- | ಒಡ/ನಡು | international→ಒಡನಾಡಿನ |
| out-/ex- (outside) | ಹೊರ | export→ಹೊರಸಾಗಣೆ |
| over-/super- (above) | ಮೇಲ್ | overcoat→ಮೇಲುಡುಪು |
| sub-/under- (below) | ಒಳ/ಕೆಳ | submarine→ಒಳನೀರಿಗೆ |
| tele- (far) | ಗೆಂಟು | telephone→ಗೆಂಟುಲಿಕ |

### Temporal
| English | Kannada | Allomorphy |
|---------|---------|------------|
| re- (again) | ಮರು/ಮಾರ್ | ಮರು before C, ಮಾರ್ before V |
| pre-/fore- | ಮುನ್ | — |
| post- | ಬಳಿ | — |
| neo- | ಹೊಸ | — |
| paleo- | ಹಳೆ | — |

### Degree/Quantity
| English | Kannada | Example |
|---------|---------|---------|
| arch-/super-/ultra- | ಎಕ್ಕ | superman→ಎಕ್ಕಮನುಶ್ಯ |
| multi-/poly- | ಹಲ | multilingual→ಹಲನುಡಿಯ |
| semi- | ಅರೆ | semicircle→ಅರೆವಟ್ಟ |
| co-/fellow | ಒಡ/ಕೂಡು | co-author→ಒಡಬರೆಗ |
| self-/auto- | ತನ್ನ | autobiography→ತನ್ನಬದುಕುಬರಹ |

### Numeral prefixes (Old Kannada roots)
| Number | Root | Allomorphy |
|--------|------|------------|
| mono/uni | ಒರ್/ಓರ್ | ಒರ್ before C, ಓರ್ before V |
| bi/di | ಇರ್/ಈರ್ | ಇರ್ before C, ಈರ್ before V |
| tri | ಮುರ್/ಮೂರ್ | ಮುರ್ before C, ಮೂರ್ before V |
| quad | ನಾಲ್ | — |
| penta | ಅಯ್ | — |
| many | ಹಲ | — |
| all | ಎಲ್ಲ | — |

### Negation
| English | Kannada | Distinction |
|---------|---------|-------------|
| un-/lacking | ಇಲ್ಲದ | absence of a quality |
| non-/not being | ಅಲ್ಲದ | being something other than |
| anti- | ಎದುರಿ | against |

---

## Neo-Classical Root Mappings

For technical vocabulary from Greek/Latin:

| Root | Kannada | Root | Kannada |
|------|---------|------|---------|
| bio- | ಉಸಿರಿ | hydro- | ನೀರ್ |
| electro- | ಮಿನ್ | tele- | ಗೆಂಟು |
| geo- | ಮಣ್/ನೆಲ | thermo- | ಬಿಸಿ |
| photo- | ಬೆಳಕು | psycho- | ಮನ |
| astro- | ಬಾನ್ | — | — |

| Suffix | Kannada | Example |
|--------|---------|---------|
| -logy | ಅರಿಮೆ | biology→ಉಸಿರಿಯರಿಮೆ |
| -scope | ತೋರ್ಪುಕ | telescope→ಗೆಂಟುತೋರ್ಪುಕ |
| -meter | ಅಳಕ | thermometer→ಬಿಸಿಯಳಕ |
| -cracy | ಆಳ್ವಿಕೆ | democracy→ಮಂದಿಯಾಳ್ವಿಕೆ |
| -naut | ಹಾಯ್ಗ | astronaut→ಬಾನಹಾಯ್ಗ |
| -graph | ಬರಹ | photograph→ಬೆಳಕುಬರಹ |

---

## Eke Romanization

All output must include Eke transliteration alongside Kannada script. For full mappings see `references/eke-romanization.md`. Critical rules:

**Aspirates preserved** (Eke romanises what is written in the source — if ಭ is used, write `bh`; if ಖ is used, write `kh` etc.):
ಖ→kh, ಘ→gh, ಛ→ch, ಝ→jh, ಠ→Th, ಢ→Dh, ಥ→th, ಧ→dh, ಫ→ph, ಭ→bh

**Retroflexes — UPPERCASE** (important phonemic distinctions):
ಟ→T, ಡ→D, ಣ→N, ಳ→L, ಶ/ಷ→S

**Long vowels — UPPERCASE:**
ಆ→A, ಈ→I, ಊ→U, ಏ→E, ಓ→O

**Vocalic ṛ** (Sanskrit loanwords with ೃ/ಋ sign):
ಋ / ೃ → **x** (short), ೠ / ೄ → **X** (long, very rare)
Examples: ಸಂಸ್ಕೃತ → `samskxta`, ಸೃಷ್ಟಿ → `sxSTi`, ಕೃಷಿ → `kxSi`

**Velar nasals:**
ಙ→G, ಞ→Y

**Anusvara ಂ — always assimilated, never written as M:**
Before labials + sonorants/sibilants (b, p, m, v, y, l, S, s, h, L): → **m** | Before velars, palatals, retroflexes, dentals, r (k, g, c, j, T, D, t, d, n, r): → **n**
Examples: ಕಂಬ → `kamba`, ಕಂಕಣ → `kankaNa`, ಸಂಸ್ಕೃತ → `samskxta`

**N is exclusively ಣ** — never use N as anusvara before stop consonants:
`linga` not `liNga`, `tunDu` not `tuNDu`

**r vs R:**
- Lowercase `r` = ರ (always) — e.g., `hesaru`, `nuDi`
- Uppercase `R` = ಱ (archaic retroflex, extremely rare in modern Kannada)

---

## Output Format

For each coined word, provide:

```
**English**: <word>
**Kannada**: <ಕನ್ನಡ ಲಿಪಿ>
**Eke**: <romanization>
**Breakdown**: <root1> (<meaning>) + <root2> (<meaning>) + <suffix> (<role>)
**Pattern**: Like <existing-word> (<analogous-formation>)
```

When coining multiple words in a batch, use a table:

| English | Kannada | Eke | Breakdown |
|---------|---------|-----|-----------|
| biology | ಉಸಿರಿಯರಿಮೆ | usiriyarime | ಉಸಿರಿ(bio) + ಅರಿಮೆ(-logy) |

Always explain the morphological logic. The user is trying to understand the system, not just get outputs.

---

## Example Coined Words

| English | Kannada | Eke | Notes |
|---------|---------|-----|-------|
| submarine | ಒಳನೀರಿಗೆ | oLanIrige | ಒಳ(sub/under) + ನೀರು(water) + -ಇಗೆ(vessel) |
| telescope | ಗೆಂಟುತೋರ್ಪುಕ | genTutOrpuka | ಗೆಂಟು(tele) + ತೋರ್(show) + -ಪುಕ(scope) |
| biology | ಉಸಿರಿಯರಿಮೆ | usiriyarime | ಉಸಿರಿ(bio/life) + ಅರಿಮೆ(study-of) |
| democracy | ಎಲ್ಲರಾಳ್ವಿಕೆ | ellarALvike | ಎಲ್ಲರ(everyone's) + ಆಳ್ವಿಕೆ(rule) — DNS Bhat coined ಮಂದಿಯಾಳ್ವಿಕೆ but ಎಲ್ಲರ is more immediately transparent |
| multilingual | ಹಲನುಡಿಯ | halanuDiya | ಹಲ(multi) + ನುಡಿ(language) + -ಯ(adj) |
| astronaut | ಬಾನಹಾಯ್ಗ | bAnahAyga | ಬಾನ್(sky) + ಹಾಯ್ಗ(navigator) |
| myth | ಕಟ್ಟುಕತೆ | kaTTukate | ಕಟ್ಟು(construct) + ಕತೆ(story) |
| linguist | ನುಡಿಯರಿಗ | nuDiyariga | ನುಡಿ(language) + ಅರಿಗ(expert) |
| isomorphic | ಸಮರೂಪ | samarUpa | (already native — ಸಮ is not Sanskrit-exclusive here) |
| feminist | ಹೆಣ್ಣೊಲವಿಗ | heNNolaviga | ಹೆಣ್ಣು(woman) + ಒಲವಿಗ(advocate) |
| handbook | ಕಿರುಕಡತ | kirukaData | ಕಿರು(small) + ಕಡತ(document) — NOT ಕಯ್ಕಡತ |

---

## Reference Files

- `references/eke-romanization.md` — Full Eke romanization table (read if asked about specific sounds or edge cases)
- Full DNS Bhat word-formation system is documented in the ettuge repo at:
  `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
  Read this when you encounter formation patterns not covered above.


---

## SKILL: kannada-morphology

# Kannada Morphology (DNS Bhat Framework)

You generate Kannada morphological forms — case suffixes, verb conjugations, verbal noun chains — following Dr. D.N. Shankara Bhat's grammatical framework. This is descriptive grammar: it describes the rules native speakers already follow unconsciously, not prescriptive rules imposed from Sanskrit.

The key insight from Bhat: all Kannada speakers *already know* these rules implicitly. Your job is to make them explicit and apply them systematically.

Use **Eke romanization** alongside Kannada script in all outputs (see romanization rules at end).

---

## Word Classes (Bhat's Native Terminology)

| Bhat's Term | Sanskrit Term | English |
|-------------|---------------|---------|
| ಹೆಸರುಪದ (hesarupada) | Naama pada (nAmapada) | Noun |
| ಎಸಕಪದ (esakapada) | Kriya pada (kriyApada) | Verb |
| ಪರಿಚೆಪದ (paricepada) | Visheshana (viShESaNa) ) | Adjective/Modifier |
| ಆಡುಪದ (ADupada) | Sarvanama (sarvanAma)| Pronoun |
| ಎಣಿಕೆಪದ (eNikepada) | Sankhya (sankhya) | Numeral |

---

## Case System (ವಿಭಕ್ತಿ / Vibhakti)

### The Critical Rational / Non-Rational Split

Kannada divides nouns into **rational** (ಉತ್ತಮ ಪ್ರಾಣಿ — higher beings) and **non-rational** (ಕ್ರಿಮಿ/ಜಡ — lower beings / inert) classes. This distinction controls suffix selection throughout the case system.

**This is NOT Sanskrit's three-gender system (masculine/feminine/neuter).** Book 14 (*Nijakku Halegannada Vyakarana Entahadu?*) documents how ancient Kannada grammarians like Keshiraja wrongly imposed Sanskrit's three-gender framework on Kannada — a fundamental error that persists in modern grammar textbooks. Old Kannada and modern Kannada both use a binary rational/non-rational split, not Sanskrit's tripartite gender.

- Rational: people, deities, respected beings (controls -anu/-aLu/-aru agreement)
- Non-rational: animals, objects, abstract concepts, plants (controls -itu/-avu agreement)

### Dative Case (-ge / "to", "for")

This is Bhat's key example of implicit native speaker knowledge — all Kannada speakers know these rules but cannot typically state them explicitly.

**Rule: Three allomorphs — conditioned by stem-final phonology AND human/non-human**

| Condition | Suffix | Example |
|-----------|--------|---------|
| Vowel-final stems (most) | -ge | ರಾಮ+ಗೆ = ರಾಮನಿಗೆ (to Rama), ಹುಡುಗ+ಗೆ = ಹುಡುಗನಿಗೆ |
| Consonant-final, non-human | -ge (with linking) | ಮರ+ಗೆ = ಮರಕ್ಕೆ (to the tree) |
| Consonant-final, certain human nouns | -ige | ನಾಯಿ+ಗೆ = ನಾಯಿಗೆ |
| Words ending in retroflex/special | -kke | ಅವ+ಗೆ = ಅವನಿಗೆ, ಇದ+ಗೆ = ಇದಕ್ಕೆ |

**Key dative allomorphs:**
- **-ge** (ಗೆ): vowel-final human nouns, e.g. ರಾಮನಿಗೆ, ಅಮ್ಮನಿಗೆ
- **-ige** (ಇಗೆ): some consonant-final nouns, e.g. ನಾಯಿಗೆ
- **-kke** (ಕ್ಕೆ): pronouns and demonstratives, e.g. ಅವನಿಗೆ, ಇದಕ್ಕೆ, ಅವಳಿಗೆ

### Other Cases

| Case | English Equivalent | Suffix(es) | Example |
|------|--------------------|------------|---------|
| Nominative | Subject | — (bare stem + ನು for human) | ರಾಮನು (Rama-NOM) |
| Accusative | Object | -ನ್ನು / -ಅನ್ನು | ರಾಮನನ್ನು (Rama-ACC) |
| Instrumental | by/with | -ಇಂದ | ರಾಮನಿಂದ (by Rama) |
| Locative | in/on/at | -ಅಲ್ಲಿ | ಮನೆಯಲ್ಲಿ (in the house) |
| Ablative | from | -ಇಂದ | ಊರಿಂದ (from the village) |
| Genitive | of/possessive | -ಅ / -ದ | ರಾಮನ (of Rama), ಮನೆಯ (of the house) |
| Vocative | address | -ಏ / -ಅ | ರಾಮ! / ಅಮ್ಮಾ! |

---

## Verbal Noun Chains (ಎಸಕನಾಮ / Esakanama)

One of the most productive patterns in Kannada: verbs become nouns, then take case suffixes.

**4-step chain:**

```
Verb root → Verbal noun → Case-marked verbal noun
ಮಾಡು → ಮಾಡುವುದು → ಮಾಡುವುದಕ್ಕೆ (for/to doing)
mADu → mADuvudu → mADuvudakke
```

**Formation rules:**

| Step | Operation | Example |
|------|-----------|---------|
| 1. Root | Bare verb | ಮಾಡು (mADu) — to do |
| 2. + -vu | Infinitive marker | ಮಾಡುವ (mADuva) |
| 3. + -du | Verbal noun | ಮಾಡುವುದು (mADuvudu) — doing/the act of doing |
| 4. + case suffix | Case-marked noun | ಮಾಡುವುದಕ್ಕೆ (mADuvudakke) — for doing |

**Examples of full chains:**

| Verb | Verbal Noun | Dative ("for X-ing") | Locative ("in X-ing") |
|------|-------------|----------------------|----------------------|
| ಓದು (read) | ಓದುವುದು | ಓದುವುದಕ್ಕೆ | ಓದುವುದರಲ್ಲಿ |
| ಬರೆ (write) | ಬರೆಯುವುದು | ಬರೆಯುವುದಕ್ಕೆ | ಬರೆಯುವುದರಲ್ಲಿ |
| ತಿನ್ನು (eat) | ತಿನ್ನುವುದು | ತಿನ್ನುವುದಕ್ಕೆ | ತಿನ್ನುವುದರಲ್ಲಿ |
| ನೋಡು (see) | ನೋಡುವುದು | ನೋಡುವುದಕ್ಕೆ | ನೋಡುವುದರಲ್ಲಿ |

---

## Verb Conjugation

### Tense-Aspect-Mood System

Kannada verbs mark tense (past/non-past) and agreement with subject (person-number-gender — PNG).

**Past tense (himbottina hesaka):** stem + past marker + PNG

| Person | Singular | Plural |
|--------|----------|--------|
| 1st | ಮಾಡಿದೆ (mADide) | ಮಾಡಿದೆವು (mADidevu) |
| 2nd | ಮಾಡಿದೆ (mADide) | ಮಾಡಿದಿರಿ (mADidiri) |
| 3rd masc | ಮಾಡಿದನು (mADidanu) | ಮಾಡಿದರು (mADidaru) |
| 3rd fem | ಮಾಡಿದಳು (mADidaLu) | ಮಾಡಿದರು (mADidaru) |
| 3rd neut | ಮಾಡಿತು (mADitu) | ಮಾಡಿದವು (mADidavu) |

**Present/Future (mubottina hesaka):** stem + -utt- + PNG

| Person | Singular | Plural |
|--------|----------|--------|
| 1st | ಮಾಡುತ್ತೇನೆ (mADuttEne) | ಮಾಡುತ್ತೇವೆ (mADuttEve) |
| 2nd | ಮಾಡುತ್ತೀಯ (mADuttIya) | ಮಾಡುತ್ತೀರಿ (mADuttIri) |
| 3rd masc | ಮಾಡುತ್ತಾನೆ (mADuttAne) | ಮಾಡುತ್ತಾರೆ (mADuttAre) |
| 3rd fem | ಮಾಡುತ್ತಾಳೆ (mADuttALe) | ಮಾಡುತ್ತಾರೆ (mADuttAre) |
| 3rd neut | ಮಾಡುತ್ತದೆ (mADuttade) | ಮಾಡುತ್ತವೆ (mADuttave) |

### Participial Forms (for adjectives from verbs)

| Form | Suffix | Example | Meaning |
|------|--------|---------|---------|
| Past participial | -da | ಮಾಡಿದ (mADida) | done, the one who did |
| Present participial | -uva | ಮಾಡುವ (mADuva) | doing, the one who does |
| Negative participial | -ada | ಮಾಡದ (mADada) | not done, undone |

---

## Etymology Classification Heuristics

When asked whether a word is native Dravidian or Sanskrit-borrowed:

**Sanskrit borrowing signals:**
- Contains aspirated consonants: kh, gh, th, dh, ph, bh (e.g., ಭಾಷೆ bhAShe → Sanskrit)
- Repeated consonant clusters from Sanskrit: pr-, tr-, kr-, sth-, etc.
- Retroflex ಷ (Sha) — rare in native Dravidian
- Ends in -a with Sanskrit declension feel

**Native Dravidian signals:**
- Simple consonant clusters or none
- No aspirates
- Contains retroflex L (ಳ), N (ಣ), D (ಡ), T (ಟ) — these are distinctly Dravidian
- Short, monosyllabic or disyllabic roots
- Found in Tamil/Telugu cognates with regular sound correspondences

**Dravidian ↔ Tamil sound correspondences (Bhat's comparative method):**
- Kannada k (before front vowels) ↔ Tamil c: ಕೆರಿ/cheri (tank), ಕೆನೆ/chene
- Kannada l ↔ Tamil l/zh in some environments
- These correspondences confirm native Dravidian origin

---

## Key Source: Book 14

*Nijakku Halegannada Vyakarana Entahadu?* (D.N. Shankara Bhat, 2005) is the most important theoretical source for this skill. It systematically demonstrates — chapter by chapter across phonology, morphology, and syntax — why Sanskrit grammatical categories do not apply to Kannada, and what Kannada's actual Dravidian grammatical principles are.

Key findings relevant to this skill:
- **Gender:** Kannada has rational/non-rational (2-way), not masculine/feminine/neuter (3-way)
- **Case:** Old Kannada does not have Sanskrit's 8-case system; suffixes function differently
- **Compounds:** Sanskrit's tatpurusha/bahuvrihi/dvandva taxonomy doesn't map onto Kannada compounds
- **Verb forms:** Old Kannada tense/aspect differs fundamentally from Sanskrit's lakara system
- **Technical terms:** Sanskrit terms like *lopa*, *agama*, *adesa*, *karaka* misrepresent Kannada morphology

Full text: `src/main/md/kannada/dnsbhat/14-nijakku-halegannada-vyakarana-entahadu/`

---

## Eke Romanization Quick Reference

- Long vowels → uppercase: a/A, i/I, u/U, e/E, o/O
- Retroflexes → uppercase: T, D, N, L
- Aspirates → preserved with h marker: kh, gh, th, dh, ph, bh (e.g., ಭಾಷೆ → bhAShe, ಅರ್ಥ → artha, ಧರ್ಮ → dharma)
- sh/Sh → S

---

## Output Format

When generating morphological forms:

1. **State the stem/root** in Kannada and Eke
2. **Identify conditioning factors** (human/non-human, vowel/consonant final, tense, person-number-gender)
3. **Show the suffix selected and why**
4. **Give the complete form** in Kannada script + Eke
5. **For paradigms**, use tables

**Example:**
> "Dative of ಮರ (tree, non-human, consonant-final)"
> Conditioning: non-human, consonant-final → suffix -kke
> Form: ಮರಕ್ಕೆ / marakke — "to the tree"

When asked about a paradigm, give the full set of forms, not just one.


---

## SKILL: dns-bhat-book-summarizer

# DNS Bhat Book Summarizer

You produce three kinds of output for DNS Bhat linguistics books in:
`/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/`

1. **`{NN}-{slug}-kn.md`** — Structured Kannada source: paragraph breaks, TOC, `<a id>` anchors at each chapter/section. Created from the raw `-book.md` or `-blog.md` if not already present.
2. **`{NN}-{slug}-en.md`** — Chapter-wise English summary with cross-links to `-kn.md` anchors and Eke romanisation
3. **`{NN}-{slug}-kn-eke.md`** — Eke romanisation of the Kannada content, structured with the same section anchors as `-kn.md`

The `-kn.md` is the canonical readable version — it's what the English summary links into. The raw `-book.md` or `-blog.md` is the OCR archive and is not modified.

---

## Step 1: Identify source material

Before writing anything, read the target book folder:

```
/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/{NN}-{slug}/
```

Check which files exist:
- `README.md` — folder-level README for GitHub browsing (create if absent; see README format below)
- `*-book.md` — full book text (highest quality, use first)
- `*-blog.md` — blog posts (use if no book.md)
- `*-kn.md` — structured Kannada (use for chapter structure)
- `*-djvu.md` — DjVu OCR (fallback, may be noisy)
- `*-en.md` — existing English summary (update if present, don't overwrite good content)
- `*-kn-eke.md` — existing Eke file (update if present)
- `*-claude-prompt.md` — AI prompt (separate from what we produce here)

**README.md format** (create if absent):
```markdown
# [NN] — {Kannada title}
**{English title}**

> {One-sentence description of the book's argument and significance.}

**{✅ Fully processed / ⚠️ Partial / ❌ Not collected}** · {year} · {publisher} · {N} pages

---

## Files in This Folder

| File | Contents |
|------|----------|
| [`{NN}-{slug}-book.md`](./{NN}-{slug}-book.md) | Raw OCR text — ... |
| [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md) | Eke romanisation |
| [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md) | English summaries |
| [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md) | AI context primer |

---

## Where to Start

- **Don't read Kannada?** → [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md)
- **Want the phonetics?** → [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md)
- **AI context primer?** → [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md)
- **Full Kannada text?** → [`{NN}-{slug}-book.md`](./{NN}-{slug}-book.md)

---

[← Back to catalogue](../README.md)
```

Read the primary source file **and** `*-kn.md` if it exists (for chapter structure). For books with a `*-claude-prompt.md`, read it too — it has the chapter outline.

---

## Step 2: Produce the structured Kannada file (`*-kn.md`) — if absent

If no `-kn.md` exists, create one from the raw `-book.md` or `-blog.md`. The `-kn.md` is the primary readable, linkable version — do not modify the raw source file.

**Paragraph detection in `-book.md` OCR output:**
- Paragraphs typically begin with a 4-space indent
- Lines are hard-wrapped at ~65 chars — a paragraph is multiple consecutive lines followed by a blank line or the next indented line
- Chapter headings are usually short standalone lines (often numbered or in all-caps Kannada)
- Section subheadings may have a number prefix (e.g., `೧.`, `೨.`) or be formatted distinctively

**`-kn.md` structure:**
```markdown
# {Kannada title}

**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಬಟ್
**ಪ್ರಕಟಣೆ:** {year}, {publisher}

> ಮೂಲ ಪಠ್ಯ: [`{NN}-{slug}-book.md`](./{NN}-{slug}-book.md)
> ಇಂಗ್ಲಿಶ್ ವಿಶ್ಲೇಷಣೆ: [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md)

---

## ಒಳಪಿಡಿ

- [ಅಧ್ಯಾಯ ೧ — {title}](#ch1)
  - [೧.೧ {section}](#sec-1-1)

---

<a id="ch1"></a>

# ಅಧ್ಯಾಯ ೧ — {title}
[↑ ಒಳಪಿಡಿಗೆ ಹಿಂತಿರುಗಿ](#ಒಳಪಿಡಿ)

---

<a id="sec-1-1"></a>

## ೧.೧ {section title}

{paragraph text with blank lines between paragraphs}
```

See book 08's `-kn.md` as the reference implementation.

---

## Step 3: Produce the Eke romanisation file (`*-kn-eke.md`)

The Eke file has:
- Same chapter/section structure as the Kannada source
- Section anchors (`<a id="ch1"></a>`, `<a id="sec-1-1"></a>`) matching the Kannada file
- A table of contents (ಒಳಪಿಡಿ in Eke: `oLapiDi`) with links to anchors
- Cross-links at the top to `-kn.md` and `-en.md`
- Key passages transliterated; summaries in Eke for long sections

**Header format:**

```markdown
# {title in Eke}

**lEkhakaru:** Di. en. Sankara bhaT
**saraNi / Source:** {series if any}
**prakaTaNe / Published:** {year and publisher}

> mUla paThya (kannaDa lipi): [{NN}-{slug}-kn.md](./{NN}-{slug}-kn.md)
> ingliS viSlEShaNe: [{NN}-{slug}-en.md](./{NN}-{slug}-en.md)

---

## oLapiDi

- [adhyAya 1 — {chapter title in Eke}](#ch1)
  - [1.1 {section in Eke}](#sec-1-1)
```

**For each section:**

```markdown
<a id="ch1"></a>

# adhyAya 1 — {title in Eke}
[↑ oLapiDige hintirugi](#oLapiDi)

---

<a id="sec-1-1"></a>

## 1.1 {section title in Eke}

{Eke transliteration of first 3-5 sentences of the section, or a meaningful excerpt}
```

For long chapters, transliterate the opening passage (establishes voice and key terms) plus any key definitions or examples.

---

## Step 3: Produce the English summary file (`*-en.md`)

The English file has:
- A book overview paragraph (3–5 sentences)
- A table of contents with anchor links
- For each chapter/section: heading in English + Kannada title + cross-links + 3–6 bullet points
- A "Key Concepts" table (Kannada term → English meaning)
- A "Cross-references" section pointing to related DNS Bhat books

**Header format:**

```markdown
# {Full English Title}
## {Subtitle or Translation of Kannada Title}

**Author:** D. N. Shankara Bhat (ಡಿ. ಎನ್. ಶಂಕರ ಬಟ್)
**Published:** {year}, {publisher}
**Language:** Kannada
**Source quality:** {Full text / Blog posts (N parts) / Partial transcript}

---

## Book Overview

{3-5 sentence overview of the book's central argument and significance}

---

## Table of Contents

- [Chapter 1 — {English Title} ({Kannada Title})](#ch1)
  - [1.1 {Section English title}](#sec-1-1)
```

**For each section:**

```markdown
## Chapter 1 — {English Title}

*({Kannada title})*

### 1.1 {English section title}

[ಕನ್ನಡ →](./{NN}-{slug}-kn.md#sec-1-1) | [Eke →](./{NN}-{slug}-kn-eke.md#sec-1-1)

- Bullet 1: what this section establishes or argues
- Bullet 2: key evidence or examples used
- Bullet 3: connection to the book's central thesis
- Bullet 4 (if needed): objections considered or counter-arguments
```

**For blog-based books** (like Books 02 and 18), use the blog post title as the "chapter" and link to the blog file:

```markdown
### Part 4 — {English title of blog post}

[Blog (ಕನ್ನಡ) →](./{NN}-{slug}-blog.md#{anchor}) | [Eke →](./{NN}-{slug}-kn-eke.md#{anchor})
```

---

## Eke Romanisation Rules

Eke is a romanisation system designed by Vishwas, inspired by Hosabaraha and Harvard-Kyoto (HK). Use **Eke(ek)** mode (ellara kannaDa — simplified, no aspirates).

### Vowels
| Kannada | Eke | | Kannada | Eke |
|---------|-----|-|---------|-----|
| ಅ | a | | ಆ | A |
| ಇ | i | | ಈ | I |
| ಉ | u | | ಊ | U |
| ಎ | e | | ಏ | E |
| ಒ | o | | ಓ | O |
| ಐ | ay | | ಔ | av |
| ಋ / ೃ (vocalic r, short) | **x** | | ೠ / ೄ (vocalic r, long) | **X** |
| ಂ (anusvara) | nasal+C *(always assimilated — never M; see Anusvara section below)* | | ಃ visarga | H |

### Consonants — case rule: **uppercase = retroflex or special**
| Kannada | Eke | | Kannada | Eke |
|---------|-----|-|---------|-----|
| ಕ | k | | ಗ | g |
| ಚ | c | | ಜ | j |
| ಟ | **T** | | ಡ | **D** |
| ತ | t | | ದ | d |
| ಪ | p | | ಬ | b |
| ಮ | m | | ನ | n |
| ಣ | **N** | | ಯ | y |
| ರ | r *(always lowercase — **R is exclusively ಱ, never ರ**)* | | ಲ | l |
| ಳ | **L** | | ವ | v |
| ಱ | **R** *(archaic retroflex ṟ — extremely rare in modern Kannada)* | | | |
| ಸ | s | | ಶ | **S** |
| ಹ | h | | ಷ | **S** (same as ಶ in EK) |

### Aspirates (mahapranas) — **preserved in Eke(ek)**
ಖ→kh, ಘ→gh, ಛ→ch, ಝ→jh, ಠ→Th, ಢ→Dh, ಥ→th, ಧ→dh, ಫ→ph, ಭ→bh

### Anusvara before plosives — write as nasal+plosive
ಂಕ→nka, ಂಗ→nga, ಂಚ→nca, ಂಜ→nja, ಂಟ→nTa, ಂಡ→nDa, ಂತ→nta, ಂದ→nda, ಂಪ→mpa, ಂಬ→mba

### Inherent vowel
Every consonant has inherent `a`. Virama ್ suppresses it in clusters.
ಕ = ka, ಕ್ = k (in cluster), ಕ್ಕ = kka

### Common word examples
| Kannada | Eke |
|---------|-----|
| ಕನ್ನಡ | kannaDa |
| ನುಡಿ | nuDi |
| ಬರಹ | baraha |
| ಹೆಸರು | hesaru |
| ಎಸಕ | esaka |
| ಅರಿಮೆ | arime |
| ಮುನ್ನೋಟ | munnOTa |
| ಇಣುಕುನೋಟ | iNukunOTa |
| ಪದ | pada |
| ಸೊಲ್ಲರಿಮೆ | sollarime |
| ಮಾತು | mAtu |
| ಉಲಿ | uli |
| ಒಳರಚನೆ | oLaracane |
| ಹೊಸ | hosa |
| ಕಟ್ಟುವ | kaTTuva |
| ಮೇಲರಿಮೆ | mElarime |
| ಕೀಳರಿಮೆ | kILarime |

---

## Quality notes

**Source quality matters** — note it clearly in the English file header:
- `*-book.md` from archive.org: high quality, full text → produce complete section-by-section summary
- `*-blog.md` from Wayback Machine: good quality, part-by-part → produce per-post summary
- YouTube transcripts: variable quality, may be garbled → note limitations, summarize available content
- DjVu OCR: often has OCR errors — note this, cross-check with other sources

**For partial content** (missing blog parts, corrupted transcripts):
- Note what's missing in the overview
- Don't invent content — only summarize what's actually in the source files
- Use "⚠️ Parts X–Y not available" as section placeholders

---

## Cross-reference footer (always include in -en.md)

At the end of every English summary, add a cross-reference table:

```markdown
---

## Cross-References to Other DNS Bhat Works

| Related Book | Connection |
|---|---|
| [08 — Kannadakke Mahaprana Yake Beda](../08-kannadakke-mahaprana-yake-beda/) | {how it relates} |
| [14 — Nijakku Halegannada Vyakarana](../14-nijakku-halegannada-vyakarana-entahadu/) | {how it relates} |
```

See `references/book-cross-references.md` for the full thematic index to populate this table.

---

## File naming conventions

| File | Naming |
|------|--------|
| Folder README | `README.md` |
| English summary | `{NN}-{slug}-en.md` |
| Eke romanisation | `{NN}-{slug}-kn-eke.md` |
| Kannada structured | `{NN}-{slug}-kn.md` |
| Blog content | `{NN}-{slug}-blog.md` |
| Book full text | `{NN}-{slug}-book.md` |
| AI prompt | `{NN}-{slug}-claude-prompt.md` |

Where `{NN}` is the zero-padded book number and `{slug}` is the folder name without the number prefix.

---

## Reference files

- `references/book-cross-references.md` — Thematic index for cross-linking between DNS Bhat works (read when populating the cross-reference footer)


---

## SKILL: dns-bhat-transcript-summarizer

# DNS Bhat Transcript Summarizer

You produce two kinds of output for DNS Bhat YouTube lecture series in:
`/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/`

1. **`{NN}-{slug}-en.md`** — Thematic English summary grouping YouTube parts, with cross-links to `#part-N` anchors in the transcript file
2. **`{NN}-{slug}-kn-eke.md`** — Eke romanisation of key passages from cleaned transcript parts, matching the thematic groupings

The primary source is the **consolidated transcript `.md` file** (e.g., `09-havyaka-kannada.md`) — NOT a `-book.md`. This file was processed by `format-transcripts.py` and already has `<a id="part-N"></a>` anchors before each `## Part N` heading.

There is **no `-kn.md` step** for transcript books — the transcript file itself serves that role directly.

---

## Step 1: Identify source material and assess quality

Read the target book folder:

```
/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/{NN}-{slug}/
```

The primary source file is `{NN}-{slug}.md` (same name as the folder, no suffix). Check what exists:

- `{NN}-{slug}.md` — consolidated transcript file with `## Part N` sections and `<a id="part-N">` anchors **(required — this is the source)**
- `README.md` — folder-level README (create if absent; see format below)
- `*-website.md` — Wayback Machine snapshot of dnshankarabhat.net for this book. **Always read this.** Some contain the official book description in Kannada or English (a gold-standard overview); others are mostly navigation chrome. If it contains a book blurb/description, use it verbatim for the overview and link to the archive URL.
- `*-blog.md` — DNS Bhat's blog posts (e.g., Book 02). If present, this is full Kannada text that can supplement or replace garbled transcript sections.
- `*-en.md` — existing English summary (update if present, don't overwrite good content)
- `*-kn-eke.md` — existing Eke file (update if present)
- `*-claude-prompt.md` — AI context primer (read if present for background)

**Assessing `-website.md` content quality:**
- If it contains a `### Description` or `### ವಿವರಗಳು` section with multiple sentences about the book → **substantive** — use the description in the overview
- If it's mostly navigation links (`ಬ್ಲಾಗ್`, `ಕನ್ನಡ ಹೊತ್ತಗೆಗಳು`, contact links) with no prose → **nav-only** — note the archive URL but skip the content
- Always include the archive URL as a "Further reading" link at the bottom of `-en.md`

**README.md format** (create if absent):

```markdown
# [NN] — {Kannada title}
**{English title}**

> {One-sentence description of the lecture series' argument and significance.}

**{✅ Fully processed / ⚠️ Partial / ❌ Not processed}** · {N} parts · YouTube lecture series

---

## Files in This Folder

| File | Contents |
|------|----------|
| [`{NN}-{slug}.md`](./{NN}-{slug}.md) | Consolidated YouTube transcripts — {N} parts |
| [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md) | Eke romanisation of key passages |
| [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md) | English summaries by theme |
| [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md) | AI context primer |

---

## Where to Start

- **Don't read Kannada?** → [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md)
- **Want the phonetics?** → [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md)
- **AI context primer?** → [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md)
- **Full transcripts?** → [`{NN}-{slug}.md`](./{NN}-{slug}.md)

---

[← Back to catalogue](../README.md)
```

---

## Step 2: Read and assess transcript quality

Read the consolidated transcript file. For each `## Part N` section, assess:

**Quality tiers:**
- **Good (🟢)** — Cleaned Kannada paragraphs from `transcripts_cleaned/`. Readable linguistic content. Summarise in detail.
- **Garbled (🟡)** — Uncleaned single-line block. May contain useful Kannada words mixed with Hindi/English fragments from faulty auto-captions. Note what's discernible, skip what isn't.
- **Disabled/Missing (🔴)** — `ERROR: Transcripts are disabled` or `ERROR: Could not retrieve`. Skip entirely; note the gap.
- **Prelim (🔵)** — Parts labelled P1–P6 in some books (e.g., 09) are introductory/preamble — often lower quality readings or context-setting.

**Spotting garbled content:** Look for repeated "foreign" tokens, Hindi words (ek, do, teen, aur, kya, etc.), or fragmented Kannada without grammatical structure. If > 50% of a part is noise, mark as 🟡 partial.

**Spotting good content:** Grammatically complete Kannada sentences about linguistics — verb conjugation, phonology, dialectology, word formation, etc.

---

## Step 3: Group parts into themes

Transcript parts run sequentially within a single sustained lecture series. Identify **thematic blocks** — adjacent parts covering the same topic. The `-en.md` is organised around these themes, not individual parts.

**How to identify themes:**
- Look at the opening sentences of each good part for the topic shift
- Each "chapter" in the English summary = 3–8 consecutive parts on the same theme
- Use the book's `-claude-prompt.md` (if present) for the chapter outline — it often lists the original book's structure
- For books without an outline, infer from the Kannada content

**Naming themes:** Derive English theme titles from the Kannada linguistic content. DNS Bhat's lectures typically follow his book structure.

---

## Step 4: Produce the English summary file (`*-en.md`)

**Header format:**

```markdown
# {Full English Title}
## {Subtitle or Translation of Kannada Title}

**Author:** D. N. Shankara Bhat (ಡಿ. ಎನ್. ಶಂಕರ ಬಟ್)
**Format:** YouTube lecture series — {N} parts
**Read by:** {reader, if known — e.g., Malati Bhat}
**Language:** Kannada
**Source quality:** {e.g., "72/88 parts cleaned (82%)" or "Partial — 22/43 cleaned"}
**Transcript file:** [`{NN}-{slug}.md`](./{NN}-{slug}.md)

---

## Overview

{3–5 sentences: what this lecture series covers, DNS Bhat's central argument, why it matters.}

---

## Table of Contents

- [Theme 1 — {English title}](#theme-1)
- [Theme 2 — {English title}](#theme-2)
```

**For each thematic group:**

```markdown
<a id="theme-1"></a>

## Theme 1 — {English Title}

*Parts {N}–{M} of the transcript*

[📼 Parts {N}–{M} →](./{NN}-{slug}.md#part-{N})

- Bullet: what this section establishes or argues
- Bullet: key evidence or examples given (cite Kannada terms in Eke)
- Bullet: connection to the overall thesis
- Bullet (if needed): counter-arguments considered

> **Coverage note:** Parts {X}, {Y} unavailable (transcripts disabled). Parts {Z}–{W} garbled (auto-caption noise).
```

**For individual standalone parts** (if a single part is a complete unit):

```markdown
### Part {N} — {English title of this part's content}

[📼 Part {N} →](./{NN}-{slug}.md#part-{N})

- {Summary bullet}
```

**Source quality field options:**
- `Full text (book OCR)` — NOT used here (that's the other skill)
- `YouTube transcripts — {N}/{total} parts cleaned ({pct}%)`
- `YouTube transcripts — partial ({N} parts unavailable)`

---

## Step 5: Produce the Eke romanisation file (`*-kn-eke.md`)

Romanise **key passages** from the **good (🟢) parts only**. For garbled/disabled parts, note the gap.

**Header format:**

```markdown
# {title in Eke}

**lEkhakaru:** Di. en. Sankara bhaT
**mULa:** YouTube udangaLu — {N} bagagaLu
**odidaravaru:** {reader in Eke, if known}

> mUla paThya (kannaDa lipi): [{NN}-{slug}.md](./{NN}-{slug}.md)
> ingliS viSlEShaNe: [{NN}-{slug}-en.md](./{NN}-{slug}-en.md)

---

## oLapiDi

- [viShaya 1 — {theme 1 in Eke}](#theme-1)
- [viShaya 2 — {theme 2 in Eke}](#theme-2)
```

**For each thematic group:**

```markdown
<a id="theme-1"></a>

## viShaya 1 — {title in Eke}

*bagagaLu {N}–{M}*

[📼 bagagaLu {N}–{M} →](./{NN}-{slug}.md#part-{N})

{Eke transliteration of 3–5 key sentences from the best part in this group.
Pick sentences that capture the core idea — a definition, a key example, or a thesis statement.}

> *(bagagaLu {X}, {Y} dorakalavillDa / kannaDavagalilla)*
```

---

## Eke Romanisation Rules

Eke is a romanisation system designed by Vishwas, inspired by Hosabaraha and Harvard-Kyoto (HK). Use **Eke(ek)** mode (ellara kannaDa — simplified, no aspirates).

### Vowels
| Kannada | Eke | | Kannada | Eke |
|---------|-----|-|---------|-----|
| ಅ | a | | ಆ | A |
| ಇ | i | | ಈ | I |
| ಉ | u | | ಊ | U |
| ಎ | e | | ಏ | E |
| ಒ | o | | ಓ | O |
| ಐ | ay | | ಔ | av |
| ಋ / ೃ (vocalic r, short) | **x** | | ೠ / ೄ (vocalic r, long) | **X** |
| ಂ (anusvara) | nasal+C *(always assimilated — never M; see Anusvara section below)* | | ಃ visarga | H |

### Consonants — case rule: **uppercase = retroflex or special**
| Kannada | Eke | | Kannada | Eke |
|---------|-----|-|---------|-----|
| ಕ | k | | ಗ | g |
| ಚ | c | | ಜ | j |
| ಟ | **T** | | ಡ | **D** |
| ತ | t | | ದ | d |
| ಪ | p | | ಬ | b |
| ಮ | m | | ನ | n |
| ಣ | **N** | | ಯ | y |
| ರ | r *(always lowercase — **R is exclusively ಱ, never ರ**)* | | ಲ | l |
| ಳ | **L** | | ವ | v |
| ಱ | **R** *(archaic retroflex ṟ — extremely rare in modern Kannada)* | | | |
| ಸ | s | | ಶ | **S** |
| ಹ | h | | ಷ | **S** (same as ಶ in EK) |

### Aspirates (mahapranas) — **preserved in Eke(ek)**
ಖ→kh, ಘ→gh, ಛ→ch, ಝ→jh, ಠ→Th, ಢ→Dh, ಥ→th, ಧ→dh, ಫ→ph, ಭ→bh

### Anusvara before plosives — write as nasal+plosive
ಂಕ→nka, ಂಗ→nga, ಂಚ→nca, ಂಜ→nja, ಂಟ→nTa, ಂಡ→nDa, ಂತ→nta, ಂದ→nda, ಂಪ→mpa, ಂಬ→mba

### Inherent vowel
Every consonant has inherent `a`. Virama ್ suppresses it in clusters.
ಕ = ka, ಕ್ = k (in cluster), ಕ್ಕ = kka

### Common word examples
| Kannada | Eke |
|---------|-----|
| ಕನ್ನಡ | kannaDa |
| ನುಡಿ | nuDi |
| ಬರಹ | baraha |
| ಮಾತು | mAtu |
| ಉಲಿ | uli |
| ಭಾಷೆ | bhAShe |
| ವ್ಯಾಕರಣ | vyAkaraNa |
| ಪದ | pada |
| ಅರ್ಥ | artha |
| ಸ್ವರ | svara |
| ವ್ಯಂಜನ | vyanjana |
| ಕ್ರಿಯಾಪದ | kriyApada |
| ನಾಮಪದ | nAmapada |
| ಉಚ್ಚಾರಣೆ | uccAraNe |
| ಅಕ್ಷರ | akSara |
| ಸೊಲ್ಲರಿಮೆ | sollarime |
| ಒಳರಚನೆ | oLaracane |
| ಹವ್ಯಕ | havyaka |
| ಉಪಭಾಷೆ | upabhAShe |
| ಮಾತಿನ | mAtina |

---

## Quality notes

**Be honest about coverage.** Always state the cleaned-part count in the header.

- **🟢 Cleaned parts:** Full thematic summary with Eke romanisation of key passages
- **🟡 Garbled parts:** Note as "⚠️ Parts X–Y partially available (auto-caption noise)" — extract whatever Kannada words are legible; skip the noise
- **🔴 Disabled parts:** Note as "❌ Part X unavailable (transcripts disabled)"

**Don't invent content.** If a section's transcripts are missing or garbled, say so explicitly. Use the structure from the book's `-claude-prompt.md` or from adjacent good parts to infer what topics were likely covered — mark inferences clearly as `*(likely topic — transcript unavailable)*`.

**Prelim parts (P1–P6):** Some books (e.g., 09) have prefix parts read by Malati Bhat or others. Treat these as an introduction section. They often introduce DNS Bhat and give context.

---

## Cross-reference and external links footer (always include in -en.md)

```markdown
---

## Cross-References to Other DNS Bhat Works

| Related Book | Connection |
|---|---|
| [08 — Kannadakke Mahaprana Yake Beda](../08-kannadakke-mahaprana-yake-beda/) | {how it relates} |
| [05 — Mathina Olaguttu](../05-mathina-olaguttu/) | {how it relates} |

---

## External Links

- **Author's website (archived):** {archive URL from *-website.md}
- **YouTube playlist:** {link from transcript file's Table of Contents, if available}
```

See `references/book-cross-references.md` for the full thematic index.

---

## File naming conventions

| File | Naming |
|------|--------|
| Folder README | `README.md` |
| Transcript source | `{NN}-{slug}.md` |
| English summary | `{NN}-{slug}-en.md` |
| Eke romanisation | `{NN}-{slug}-kn-eke.md` |
| AI prompt | `{NN}-{slug}-claude-prompt.md` |

Where `{NN}` is the zero-padded book number and `{slug}` is the folder name without the number prefix.

---

## Reference files

- `references/book-cross-references.md` — Thematic index for cross-linking between DNS Bhat works
- `transcripts_cleaned/` — Pre-processed transcript `.txt` files (source for cleaned parts)
- `format-transcripts.py` — Script that substituted cleaned transcripts into the `.md` files


---

## SKILL: kannada-ocr-cleaner

# Kannada OCR Cleaner

You help clean Kannada text that was OCR'd from books typeset in legacy
Kannada font encodings (Nudi, Baraha, ISM/CDAC, and similar pre-Unicode
systems). These fonts mapped Kannada glyphs to positions in a Latin codepage,
so OCR software read the glyph shapes and produced Latin characters instead of
the correct Kannada Unicode codepoints.

Four classes of error recur throughout this corpus:

1. **Vowel-sign + consonant garbling** — specific Kannada characters are
   consistently mis-encoded as sequences of Latin bytes.
2. **Arka-ottu reversal** — the RA-half-consonant (ರ್) was read in the wrong
   order, producing consonant+್ರ instead of ರ್+consonant.
3. **English text garbling** — books typeset entirely in the legacy font had
   their English passages (bibliography, titles) garbled into Kannada-like
   characters using the same encoding.
4. **OCR page-break structural artifacts** — paragraph-final words from the
   bottom of a page appear as isolated lines before the next section heading,
   and chapter-title running headers from print page-tops appear as standalone
   lines embedded mid-paragraph. These are structural, not character-level.

---

## Class 1 — Vowel-sign / consonant garbling

These are **always wrong** when they appear in Kannada Unicode text; replace
unconditionally.

### ಯ garbling (legacy: `0iÉ`)

The consonant ಯ and its associated vowel signs were encoded as the three-byte
Latin string `0iÉ` (U+0030 U+0069 U+00C9). The vowel signs were also
mis-encoded — `ు` (U+0CC1) for short-e (ೆ) and `ುೀ` (U+0CC1+U+0CC0) for
long-e (ೇ):

| OCR output | Correct | Notes |
|------------|---------|-------|
| `0iÉ` + `ుೀ` | `ಯೇ` | long-e particle: ಯೇಕೆ, ಯೇನು |
| `0iÉ` + `ు` | `ಯೆ` | short-e: ಯೆಂಬ, ಯೆಂದು, ಯೆಂತ, ಯೆನ್ನ |
| `0iÉ` + `ు` before real ಯ | delete `0iÉు` | ordinals: ದ್ವಿತೀ**0iÉు**ಯ → ದ್ವಿತೀಯ |
| `0iÉ` alone | `ಯ` | before virama: ಗೆಯ್ಮ, ಆಯ್ಕ |

Apply in this order (most specific first):
```python
import re
text = re.sub(r'0iÉు(\s*)(?=ಯ)', r'\1', text)  # rule 1: ordinals
text = text.replace('0iÉుೀ', 'ಯೇ')             # rule 2: long-e
text = text.replace('0iÉు', 'ಯೆ')              # rule 3: short-e
text = text.replace('0iÉ', 'ಯ')               # rule 4: standalone
```

### Residual long-e garble after correctly-recognised ಯ

When ಯ was OCR'd correctly but its long-e vowel sign (ೇ) was still garbled as
`ుೀ`, the result is `ಯುೀ`. This is a separate pattern from `0iÉ` and catches
a further 59 cases (interrogatives, emphatics, etc.):

```python
text = text.replace('\u0CAF\u0CC1\u0CC0', 'ಯೇ')   # ಯ + ు + ೀ → ಯೇ
```

Examples: `ಇದೆಯುೀ?` → `ಇದೆಯೇ?`, `ಹಾಗೆಯುೀ` → `ಹಾಗೆಯೇ`,
`ತಾವಾಗಿಯುೀ` → `ತಾವಾಗಿಯೇ`, `ಕನ್ನಡದಲ್ಲಿವೆಯುೀ?` → `ಕನ್ನಡದಲ್ಲಿವೆಯೇ?`

### Archaic diphthong / ಯ್ in letter-listing contexts (`0iÀiï`)

The sequence `0iÀiï` (U+0030 U+0069 U+00C0 U+0069 U+00EF) is the garbled form
of `ಯ್` (ya + virama) in contexts where the book lists archaic Kannada sound
combinations. Appears as `ಆ0iÀiï` = `ಆಯ್` and `ಅ0iÀiï` = `ಅಯ್`:

```python
text = text.replace('0iÀiï', 'ಯ್')
```

### Sanskrit tense-marker garbling (ಙ್)

The halanta form ಙ್ (used in Sanskrit verb forms ಲಙ್, ತಿಙ್, ಲುಙ್, ಲೃಙ್) was
garbled as `ಙõï` or the two-byte sequence `ÂÐ`:

```python
text = text.replace('ಙõï', 'ಙ್')
text = text.replace('ÂÐ', 'ಙ್')
```

### ಬಹು garbling (`ಬಹÅ`)

The word ಬಹು (bahu = "can", as in ಬಳಸಬಹುದು "can use") was garbled as `ಬಹÅ`:

```python
text = text.replace('ಬಹÅ', 'ಬಹು')
```

---

## Class 2 — Arka-ottu reversal

The arka-ottu is the half-form of ರ (RA) written as a superscript above its
following consonant. In correct Kannada, the cluster is **ರ್ + C** (ra +
virama + consonant). OCR of legacy fonts frequently reversed this, producing
**C + ್ರ** (consonant + virama + ra).

### The cardinal rule: only mid- and end-of-word

Initial consonant clusters beginning with ಕ್ರ, ಪ್ರ, ವ್ರ, ಶ್ರ, etc. are
**correct** — the arka-ottu never starts a word. These must NOT be changed:

| Leave alone | Why |
|-------------|-----|
| ಕ್ರಿಯಾ, ಪ್ರತ್ಯಯ | initial ಕ್ರ, ಪ್ರ |
| ಮಾತ್ರ, ಸೂತ್ರ | ತ್ರ is a legitimate medial cluster |
| ಸ್ವತಂತ್ರ, ಚಾರಿತ್ರಿಕ | same |
| ಸ್ತ್ರೀ | initial ಸ್ತ್ರ |

### Global-safe reversals

These C+್ರ combinations do **not** occur naturally in Kannada, so replacement
is always correct:

| OCR output | Correct | Frequency | Common words |
|------------|---------|-----------|--------------|
| `ಣ್ರ` | `ರ್ಣ` | high | ಪೂರ್ಣ, ಸಂಪೂರ್ಣ, ಅಪೂರ್ಣ, ವರ್ಣ |
| `ಥ್ರ` | `ರ್ಥ` | very high | ಅರ್ಥ (artha = meaning — extremely common) |
| `ಮ್ರ` | `ರ್ಮ` | high | ಕರ್ಮ, ಗುಣಧರ್ಮ, ಸಕರ್ಮಕ, ಅಕರ್ಮಕ |
| `ಯ್ರ` | `ರ್ಯ` | medium | ಕಾರ್ಯ, ಸೂರ್ಯ, ಆಶ್ಚರ್ಯ, ಸೌಜನ್ಯ |
| `ದೀಘ್ರ` | `ದೀರ್ಘ` | low | dīrgha = long vowel (linguistics term) |

```python
text = text.replace('ಣ್ರ', 'ರ್ಣ')
text = text.replace('ಥ್ರ', 'ರ್ಥ')
text = text.replace('ಮ್ರ', 'ರ್ಮ')
text = text.replace('ಯ್ರ', 'ರ್ಯ')
text = text.replace('ದೀಘ್ರ', 'ದೀರ್ಘ')
```

### Word-specific `ತ್ರ` and `ಧ್ರ` reversals

Because `ತ್ರ` also appears legitimately (ಮಾತ್ರ, ಸೂತ್ರ, ಸ್ವತಂತ್ರ), only fix
specific known-wrong words:

```python
text = text.replace('ವತ್ರಮಾ', 'ವರ್ತಮಾ')     # ವರ್ತಮಾನ (present tense)
text = text.replace('ಕತ್ರರಿ', 'ಕರ್ತರಿ')      # kartari construction
text = text.replace('ಕತ್ರೃ', 'ಕರ್ತೃ')        # kartR (agent noun)
text = text.replace('ಪೂತ್ರಿ', 'ಪೂರ್ತಿ')      # pUrti (completion)
text = text.replace('ಪರಿವತ್ರ', 'ಪರಿವರ್ತ')    # parivarta (change)
text = text.replace('ನಿಧ್ರ', 'ನಿರ್ಧ')        # nirdha- (determination)
text = text.replace('ಅಶೋಕವಧ್ರ', 'ಅಶೋಕವರ್ಧ')  # aSOkavardhana (proper name)
text = text.replace('ಕೃಷ್ಣಮೂತ್ರಿ', 'ಕೃಷ್ಣಮೂರ್ತಿ')  # Krishnamurti (scholar name)
```

---

## Class 3 — English text garbled through legacy font

Books typeset entirely in the legacy font had their English text (bibliography,
foreign book titles) encoded the same way. English words appear as garbled
Kannada-like characters. The font maps ASCII letters to these Kannada codepoints:

| Kannada char | Latin it represents |
|---|---|
| ಅ | C |
| ಆ | D |
| ಇ | E |
| ಐ | L |
| ಏ | K |
| ಎ | J |
| ಖ | R (capital) |
| ಖಿ | T (capital) |
| ಠಿ | p |
| ಚಿ | a |
| ಟಿ | n |
| ಟ | l |
| ಡಿ | r |
| ಜ | d |
| ಜಿ | f |
| ಣ | t |
| ಥಿ | y |

**Recognition cue**: a bibliography line containing Kannada-script characters
*inside* what should be an English title (e.g., `ಖಿhe ಆಡಿಚಿviಜiಚಿಟಿ` = "The
Dravidian"), or an author name containing an isolated Latin letter like `Ç`.

**Fix approach**: decode each garbled token using the table above, then replace
directly. For recurring proper names like Taraporewala, use a string replace:

```python
# Proper name with Ç artefact
text = text.replace('ತಾರಾಪೆÇರೆವಾಲಾ', 'ತಾರಾಪೋರ್ವಾಲಾ')

# Bibliography English titles (exact strings with OCR double-spaces)
text = text.replace('ಖಿhe  ಆಡಿಚಿviಜiಚಿಟಿ  ಐಚಿಟಿguಚಿge', 'The Dravidian Language')
text = text.replace('ಇಡಿgಚಿಣiviಣಥಿ',                     'Ergativity')
text = text.replace('Sಚಿಟಿsಞಡಿiಣ  sಥಿಟಿಣಚಿx',            'Sanskrit syntax')
text = text.replace('ಆeಟhi',                              'Delhi')
text = text.replace('ಅಚಿmbಡಿiಜge',                       'Cambridge')
text = text.replace('ಖeoಡಿಜeಡಿiಟಿg  ಡಿuಟes  iಟಿ',       'Reordering rules in')
text = text.replace('ಏಚಿಟಿಟಿಚಿಜಚಿ  ಠಿಡಿeಜಿixಚಿಣioಟಿ',    'Kannada prefixation')
text = text.replace('PIಐಅ  ಎouಡಿಟಿಚಿಟ  oಜಿ',            'PILC Journal of')
```

Note: OCR of these books typically inserts double spaces between words. Match
the exact spacing when writing replacement strings.

---

## Audit workflow

Before writing fix scripts, always audit the actual frequency and context of
each pattern so you understand what you're changing:

```python
import re

src = '/path/to/file-kn.md'
text = open(src, encoding='utf-8').read()
lines = text.split('\n')

# Frequency audit — Class 1 + 2 patterns
patterns = [
    '0iÉ',                          # ಯ garbling
    '\u0CAF\u0CC1\u0CC0',           # ಯ + residual long-e (ಯುೀ)
    '0iÀiï',                        # archaic ಯ್ diphthong
    'ಣ್ರ', 'ಥ್ರ', 'ಮ್ರ', 'ಯ್ರ',   # arka-ottu reversals
    'ಙõï', 'ÂÐ', 'ಬಹÅ', 'ದೀಘ್ರ',  # other Class 1
]
for p in patterns:
    n = text.count(p)
    if n:
        print(f'{n:4d}  {repr(p)}')

# Check for Class 3: Kannada chars inside English-dominant lines
for i, ln in enumerate(lines, 1):
    import unicodedata
    kn = sum(1 for c in ln if '\u0C80' <= c <= '\u0CFF')
    lat = sum(1 for c in ln if c.isascii() and c.isalpha())
    if 0 < kn < 8 and lat > 5:   # few Kannada chars, more Latin = garbled English
        print(f'  Possible Class 3 line {i}: {ln.strip()[:80]}')

# Context sampling
def show_context(pattern, n=5):
    for i, ln in enumerate(lines, 1):
        if pattern in ln:
            print(f'  line {i}: {ln.strip()[:90]}')
            n -= 1
            if not n:
                break
```

Key things to audit before applying global replacements:
- Are there any false positives? (e.g., does `ಮ್ರ` appear in words where it
  should NOT be ರ್ಮ?)
- Do line-split cases exist? (OCR sometimes breaks a word across lines; e.g.,
  `ಯೆಂಬು \nದ` should be `ಯೆಂಬುದ`)
- Does `ಯುೀ` appear after vowels other than ಯ? (In book 28 it did not — all
  59 were after ಯ — but audit for each new book.)

---

## Fix script template

Always write a single script per cleanup pass, print a count summary, spot-
check a few lines, and write back in-place:

```python
#!/usr/bin/env python3
import re

SRC = '/path/to/file-kn.md'
text = open(SRC, encoding='utf-8').read()
counts = {}

def rep(old, new, label=None):
    global text
    n = text.count(old)
    text = text.replace(old, new)
    counts[label or f'{old}→{new}'] = n

# ── Class 1: vowel-sign / consonant garbling ──
text = re.sub(r'0iÉు(\s*)(?=ಯ)', r'\1', text)
counts['0iÉు before ಯ (ordinals)'] = 0   # re.sub doesn't return count; check separately
rep('0iÉుೀ', 'ಯೇ')
rep('0iÉు',  'ಯೆ')
rep('0iÉ',   'ಯ')
rep('\u0CAF\u0CC1\u0CC0', 'ಯೇ', 'ಯುೀ→ಯೇ (residual long-e after ಯ)')
rep('0iÀiï', 'ಯ್', '0iÀiï→ಯ್ (archaic diphthong)')
rep('ಙõï', 'ಙ್')
rep('ÂÐ',  'ಙ್')
rep('ಬಹÅ', 'ಬಹು')

# ── Class 2: arka-ottu reversals ──
rep('ಣ್ರ', 'ರ್ಣ')
rep('ಥ್ರ', 'ರ್ಥ')
rep('ಮ್ರ', 'ರ್ಮ')
rep('ಯ್ರ', 'ರ್ಯ')
rep('ದೀಘ್ರ', 'ದೀರ್ಘ')
rep('ವತ್ರಮಾ', 'ವರ್ತಮಾ')
rep('ಕತ್ರರಿ', 'ಕರ್ತರಿ')
rep('ಕತ್ರೃ', 'ಕರ್ತೃ')
rep('ಪೂತ್ರಿ', 'ಪೂರ್ತಿ')
rep('ಪರಿವತ್ರ', 'ಪರಿವರ್ತ')
rep('ನಿಧ್ರ', 'ನಿರ್ಧ')
rep('ಅಶೋಕವಧ್ರ', 'ಅಶೋಕವರ್ಧ')
rep('ಕೃಷ್ಣಮೂತ್ರಿ', 'ಕೃಷ್ಣಮೂರ್ತಿ')

# ── Class 3: bibliography / English garbling (add as discovered) ──
rep('ತಾರಾಪೆÇರೆವಾಲಾ', 'ತಾರಾಪೋರ್ವಾಲಾ')
# ... add other bibliography entries

# ── Report ──
total = sum(counts.values())
for label, n in counts.items():
    if n: print(f'  {n:4d}  {label}')
print(f'  ──── {total} total')

with open(SRC, 'w', encoding='utf-8') as f:
    f.write(text)
print(f'Written: {SRC}')
```

---

## After fixing kn.md — regenerate kn-eke.md

If the book has a `-kn-eke.md` Eke romanisation file, re-run the transliterator
after every batch of fixes:

```bash
python3 /tmp/kn_to_eke.py
```

Verify the ratio printed is ~1.00 (KN source tokens ≈ EKE output tokens).
Large deviations mean text was accidentally deleted or duplicated.

---

## Class 4 — OCR page-break structural artifacts

When OCR processes a multi-page book, two types of structural junk appear that
**no character-level replacement can fix** — they require line-level surgery.

### Type A: Orphaned fragments before section headings

The last few words of a print page appear as short isolated lines (each
preceded by a blank line) just before the next section heading:

```
ಹೇಳಿ ಕೊಡುವುದು ಹೇಗೆ ತಪ್ಪಾಗುತ್ತದೆಯೋ ಹಾಗೆಯೇ ಇದೂ ಕೂಡ.
                        ← paragraph ends here

ವ್ಯಾಕರಣವೆಂಬುದು         ← orphaned fragment (blank before and after)

ನುಡಿಯಿಂದ               ← orphaned fragment

ನುದಿಗೆ                 ← orphaned fragment

1.2  ವ್ಯಾಕರಣದ ಉದ್ದೇಶ    ← section heading (trigger)
```

**Fix**: join all orphaned fragments to the preceding paragraph, remove
the blank lines between them, and keep one blank before the section heading.

### Type B: Running chapter headers

The print book's page-top chapter-title header gets OCR'd into the text flow
as a standalone line, typically appearing between an orphaned fragment and the
next line of body text:

```
ಮಸೂರವನ್ನು                 ← orphaned fragment

ಮುನ್ನೋಟ                  ← chapter title from print page header (intruder)

ಸಂಬಂಧಿಸಿದಂತಹ ಚಟುವಟಿಕೆಗಳನ್ನು...  ← body text continues
```

**Fix**: join the fragment to the preceding paragraph, delete the running
header line and the blank lines surrounding it.

### The critical detection rule

A line is an **orphaned fragment** only if ALL of these hold:
- It contains Kannada text
- It is **preceded by a blank line** (this is the critical check — wrapped
  paragraph lines are *not* preceded by blanks, so they are not fragments)
- It is short (< 65 chars)
- It does not start a section heading (`N.N xxx`), chapter heading (`## …`),
  anchor (`<a id`), or nav link (`[…]`)
- It is not itself a known running header title

Without the "preceded by blank" guard, normal wrapped paragraph lines like
`ಹೇಳಿ ಕೊಡುವುದು ಹೇಗೆ ತಪ್ಪಾಗುತ್ತದೆಯೋ ಹಾಗೆಯೇ ಇದೂ ಕೂಡ.` (which are short)
get misidentified as fragments.

### Chapter boundary lines — never delete, never use as target

When walking backward from a section heading to find the paragraph to append
fragments to, skip over these **chapter boundary** lines (they must be
preserved in the output):

- Lines starting with `## ` (chapter `##` headings)
- Lines starting with `<a id` (anchor tags)
- Lines starting with `[` and containing `→` or `->` (nav links)
- Blank lines

The fragment target is the last **body text** line before any boundary lines.
This handles the cross-chapter case where fragments appear between a `##`
chapter heading and the first subsection heading of that chapter.

### Running chapter headers to recognise (book 28)

Build a set of known running header titles specific to the book. For book 28
(*ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ*), these are the 12 chapter names:

```python
RUNNING_HEADERS = {
    'ಮುನ್ನೋಟ', 'ಸೇರಿಕೆಯ ನಿಯಮಗಳು', 'ಪದವಗ್ರಗಳು', 'ಪದಗಳ ಒಳರಚನೆ',
    'ಸಮಾಸಗಳು', 'ಲಿಂಗ ಮತ್ತು ವಚನಗಳು', 'ವಿಭಕ್ತಿಗಳು ಮತ್ತು ಕಾರಕಗಳು',
    'ವಿಭಕ್ತಿಗಳು', 'ವಿಭಕ್ತಿಪಲ್ಲಟ', 'ಸವ್ರನಾಮಗಳು ಮತ್ತು ಎಣಿಕೆಯ ಪದಗಳು',
    'ಕ್ರಿಯಾರೂಪಗಳು', 'ಮುಕ್ತಾಯ',
}
```

For each new book, grep for lines that match the chapter titles exactly to
build this set.

### Fix script pattern (three-pass)

The fix requires a three-pass approach because edits interact — the same
target line may receive fragments from multiple adjacent sections:

```python
#!/usr/bin/env python3
import re

SRC = '/path/to/file-kn.md'
lines = open(SRC, encoding='utf-8').readlines()

BODY_START = 354   # line index where body text begins (after frontmatter/TOC)

sec_pat = re.compile(r'^\d+\.\d[\d.]*\s+[\u0C80-\u0CFF]')  # N.N KannadaText
kan_re  = re.compile(r'[\u0C80-\u0CFF]')

RUNNING_HEADERS = { ... }   # chapter titles for this book

def is_chapter_boundary(s):
    if not s: return True
    if s.startswith('## '): return True
    if s.startswith('<a id'): return True
    if s.startswith('[') and ('→' in s or '->' in s): return True
    return False

def is_fragment(lines, idx):
    if idx < BODY_START: return False
    s = lines[idx].strip()
    if not s: return False
    if not kan_re.search(s): return False
    if sec_pat.match(s): return False
    if s.startswith('##') or s.startswith('<') or s.startswith('['): return False
    if s in RUNNING_HEADERS: return False
    if any(c in s for c in ['+', '=', '→', '|']): return False
    if len(s) > 65: return False
    # CRITICAL: must be preceded by a blank line
    if idx > 0 and lines[idx - 1].strip() != '': return False
    return True


# ── Pass 1: collect all fixes ──────────────────────────────────────────────

fixes = []

for trigger_idx in range(BODY_START, len(lines)):
    s = lines[trigger_idx].strip()
    is_sec = bool(sec_pat.match(s))
    is_rh  = s in RUNNING_HEADERS
    if not is_sec and not is_rh: continue

    # Walk backward collecting orphaned fragments
    frags = []
    j = trigger_idx - 1
    while j >= BODY_START and lines[j].strip() == '': j -= 1
    while j >= BODY_START:
        if lines[j].strip() == '': j -= 1; continue
        if is_fragment(lines, j): frags.insert(0, j); j -= 1
        else: break

    if not frags:
        if is_rh:
            fixes.append({'type': 'delete_rh_only', 'trigger': trigger_idx})
        continue

    wall_idx = j  # last non-blank non-fragment line (may be a boundary line)
    target_idx = wall_idx
    while target_idx >= BODY_START and is_chapter_boundary(lines[target_idx].strip()):
        target_idx -= 1
    if target_idx < BODY_START or not lines[target_idx].strip(): continue

    fixes.append({
        'type': 'sec' if is_sec else 'rh',
        'trigger': trigger_idx, 'frags': frags,
        'wall': wall_idx, 'target': target_idx,
    })


# ── Pass 2: build to_delete / modify sets ─────────────────────────────────

to_delete = set()
modify    = {}

for fix in fixes:
    t = fix['type']

    if t == 'delete_rh_only':
        to_delete.add(fix['trigger'])
        k = fix['trigger'] - 1; removed = 0
        while k >= BODY_START and lines[k].strip() == '' and removed < 2:
            to_delete.add(k); k -= 1; removed += 1
        continue

    frags = fix['frags']; trigger = fix['trigger']
    wall  = fix['wall'];  target  = fix['target']

    # Append joined fragment text to target line
    frag_text = ' '.join(lines[f].strip() for f in frags)
    modify[target] = lines[target].rstrip() + ' ' + frag_text + '\n'

    for f in frags: to_delete.add(f)
    # Delete blank lines between fragments
    for k in range(frags[0], frags[-1] + 1):
        if lines[k].strip() == '': to_delete.add(k)
    # Delete blank lines between wall/target and first fragment (keep boundaries)
    start_del = wall + 1 if is_chapter_boundary(lines[wall].strip()) else target + 1
    for k in range(start_del, frags[0]):
        if lines[k].strip() == '': to_delete.add(k)
    # Delete blanks between last fragment and trigger
    blanks_after = [k for k in range(frags[-1] + 1, trigger) if lines[k].strip() == '']
    if t == 'sec':
        for b in blanks_after[:-1]: to_delete.add(b)  # keep one blank before heading
    else:  # running header: delete all + the trigger itself
        for b in blanks_after: to_delete.add(b)
        to_delete.add(trigger)


# ── Pass 3: build output ───────────────────────────────────────────────────

result = []
for i, line in enumerate(lines):
    if i in to_delete: continue
    result.append(modify[i] if i in modify else line)

with open(SRC, 'w', encoding='utf-8') as f:
    f.writelines(result)
```

### Audit before running

Before running the fix script, verify the patterns are what you expect:

```python
# Count section headings with preceding blank-line-separated short Kannada lines
import re
lines = open(SRC, encoding='utf-8').readlines()
sec_pat = re.compile(r'^\d+\.\d[\d.]*\s+[\u0C80-\u0CFF]')
for i, ln in enumerate(lines):
    if i < BODY_START: continue
    if sec_pat.match(ln.strip()):
        j = i - 1
        while j >= 0 and lines[j].strip() == '': j -= 1
        if j >= 0 and len(lines[j].strip()) < 65 and lines[j-1].strip() == '':
            print(f'L{i+1}: {ln.strip()[:60]}  ← possible fragment at L{j+1}')

# Verify running header occurrences
for rh in RUNNING_HEADERS:
    hits = [(i+1, ln.strip()) for i, ln in enumerate(lines) if ln.strip() == rh]
    if hits:
        print(f'{rh}: {len(hits)} hits at lines {[h[0] for h in hits]}')
```

Report produced by the script (book 28 example):
```
Section headings with fragments fixed: 12
Running headers with fragments fixed:  4
Running headers deleted (no frags):    4
Total lines deleted:  96
Total lines modified: 16
Output lines: 9517  (was 9613)
```

---

## What NOT to fix automatically

- **Initial `ಕ್ರ`, `ಪ್ರ`, `ಮಾತ್ರ`, `ಸೂತ್ರ`, `ಚಾರಿತ್ರ`**: these are correct.
- **Any `ತ್ರ` not in the word-specific list above**: audit before touching.
- **`ಯ` + `ు`** without the following `ೀ`: this is legitimate ಯು (ya+u),
  not a garble. Only the three-character sequence ಯ+ు+ೀ is wrong.
- **Wrapped paragraph lines**: short Kannada lines that are *not* preceded by
  a blank line. These are normal text wrapping, not orphaned fragments.
- **Table labels and diagram captions**: short Kannada words in phonetic charts,
  vowel triangles, or numbered example lists — check context before treating
  as fragments. The "preceded by blank" rule usually protects these.


---

## AGENTS


### Agent: ellara-vocab-builder

# Agent: ellara-vocab-builder

## Purpose
Builds a native Kannada vocabulary dataset by scraping Honalu.net and Kannada Wiktionary, classifying word etymology (Dravidian vs Sanskrit), and storing results in Eke romanization.

## Pipeline

```
1. Scrape word list from Honalu.net
        ↓
2. Classify etymology (native Dravidian vs Sanskrit borrowing)
   Heuristics:
   - Sanskrit signals: aspirated consonants (kh/gh/th/dh/ph/bh), Sanskrit clusters (pr-/tr-/kr-), ಷ (Sha)
   - Dravidian signals: no aspirates, has ಳ/ಣ/ಡ/ಟ, Tamil cognate matches
        ↓
3. Transliterate to Eke romanization
   Rules: aspirates→plain, retroflexes uppercase (T/D/N/L), long vowels uppercase (A/I/U/E/O)
        ↓
4. Store as structured dataset (JSON or CSV)
   Schema: { word_kn, word_eke, etymology_class, source_url, confidence }
```

## Key Constraints
- Honalu.net may rate-limit — use delays between requests
- Prefer Wiktionary for etymology confirmation
- Flag uncertain classifications for human review
- Output must be compatible with `ellara-kannada-word-coiner` skill format

## Reference Files
- DNS Bhat word formation: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Eke rules: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`
- Analysis: `src/main/md/kannada/dnsbhat/dns-bhat-analysis.md`


### Agent: technical-term-coiner

# Agent: technical-term-coiner

## Purpose
Takes a list of English technical terms and coins native Dravidian Kannada equivalents using DNS Bhat's word formation methodology. Produces a structured glossary.

## Pipeline

```
1. Receive English term list
        ↓
2. For each term, apply the DNS Bhat word-generation algorithm:
   a. Check if native equivalent already exists (search Honalu/Wiktionary)
   b. Analyze English morphological structure (prefix/suffix/compound/standalone)
   c. Identify semantic core and role (agent/action/instrument/quality)
   d. Select strategy: suffix-derived > prefix+word > compound
   e. Select native Kannada root (avoid Sanskrit)
   f. Apply morphological rules + phonological allomorphy
   g. Verify: intelligible? established pattern? pronounceable?
        ↓
3. Add Eke romanization
        ↓
4. Cross-check against Honalu.net for existing usage
        ↓
5. Output structured glossary:
   { english, kannada_script, eke, breakdown, strategy_used, confidence, notes }
```

## Output Format
Markdown table + JSON file. The markdown is for human review; the JSON feeds downstream systems.

## Reference Files
- Full DNS Bhat system: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Skill to invoke: `.claude/skills/ellara-kannada-word-coiner/SKILL.md`
- Eke rules: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`


---

## REPOSITORY CONTEXT (CLAUDE.md files)


### Root CLAUDE.md

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

### Current Status (as of 2026-03-19, Phase 17)

All 29 DNS Bhat books have been processed through multiple phases of OCR cleanup, Nudi→Unicode conversion, romanisation generation, and TOC restructuring. Key milestones:

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


### .claude/CLAUDE.md — Automation Context

# ettuge — Claude Automation Context

This file documents the `.claude/` automation layer for the ettuge repository.

## Available Skills

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `ellara-kannada-word-coiner` | "native Kannada word for X", "DNS Bhat style", "no Sanskrit", "coin a word", "Ellara version of" | Coins native Dravidian words using DNS Bhat methodology |
| `kannada-morphology` | "Kannada suffix for", "conjugate this verb", "case form of", "dative of", "verbal noun chain" | Generates morphological forms using Bhat's grammar framework |
| `dns-bhat-book-summarizer` | "summarize book NN", "create English summary", "generate Eke", "create -en.md", "create -kn-eke.md", "create claude-prompt for book", "add paragraph breaks", "structure book NN" | Produces README.md + kn.md (paragraphs + anchors) + en.md + kn-eke.md for DNS Bhat books with OCR text (books 14–29) |
| `dns-bhat-transcript-summarizer` | "summarize transcript book NN", "summarize YouTube lectures", "create English summary from transcripts", "generate Eke for lectures", "books 01–13" | Produces en.md + kn-eke.md for YouTube-only DNS Bhat lecture series (books 01–13, no OCR text) from cleaned transcript .md files |
| `kannada-ocr-cleaner` | "OCR errors in Kannada", "garbled Kannada", "arka-ottu", "fix legacy font", "ರ್ wrong in OCR", "Nudi artefact", "running header in body", "page-break fragment", garbled Latin chars (É Å À ï õ) mixed with Kannada | Audits and fixes OCR artefacts from Nudi/Baraha/ISM legacy font encoding; handles arka-ottu reversals, anusvara garbling, embedded running headers, page-break fragments, oo-matra errors |

## Available Agents

| Agent | File | Purpose |
|-------|------|---------|
| `ellara-vocab-builder` | `agents/ellara-vocab-builder.md` | Scrapes Honalu.net → classifies etymology → builds dataset |
| `technical-term-coiner` | `agents/technical-term-coiner.md` | Batch English→native Kannada glossary generation |

## Available Commands

| Command | Purpose |
|---------|---------|
| `/coin-word` | Quick word coining via ellara-kannada-word-coiner skill |

## Eke Romanisation — Canonical Rules (must not be violated)

Eke is the romanisation used in all `-kn-eke.md` files. Full spec: `src/main/md/kannada/Eke.md`. Quick reference: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`.

**Four rules that have historically caused systematic LLM errors:**

| Rule | Wrong form | Correct Eke | Notes |
|------|-----------|-------------|-------|
| Anusvara ಂ | `M` (HK) | Assimilated nasal+C: `nk ng nc nT nD nt nd mp mb ms my mv` | **Never standalone M** |
| N (retroflex ಣ) | `liNga`, `tuNDu` | `linga`, `tunDu` | N = exclusively ಣ; never anusvara before stop consonants |
| ರ vs ಱ | `vaRNa`, `sRiSTi` | `varNa`, `sxSTi` | Lowercase `r` = ರ always; `R` = exclusively rare ಱ |
| Vocalic ṛ ಋ/ೃ | `samskrita`, `sriSTi`, `kRi`→`kri` | `samskxta`, `sxSTi`, `kx` | `x` = ಋ/ೃ (short); `X` = ೠ/ೄ (long, rare) |

**Safe / do not change:** `kriyA`, `krutaka`, `krulling` — these use genuine consonant ರ + ಉ/ಇ, not vocalic ṛ.

---

## DNS Bhat Book OCR Pipeline — Conventions

### File roles (do not conflate)
| File | Role | Editable? |
|------|------|-----------|
| `*-book.md` / `*-blog.md` | Raw OCR archive | NO — source of truth |
| `*-kn.md` | Structured Kannada source with TOC + anchors | YES |
| `*-kn-eke.md` | Eke romanisation of kn.md | YES (regenerate after kn.md changes) |
| `*-en.md` | English chapter summary | YES |
| `*-claude-prompt.md` | Condensed prompt context | YES |

### Citation quotes
DNS Bhat's typographic convention uses backtick as open-quote (`` `word' `` or ` ``word'' `). In kn.md and kn-eke.md, these are standardised to **curly single quotes** U+2018/U+2019: `'word'`. Never use backtick as open-quote — it creates Markdown code-span rendering bugs.

Close char varies by book (from original typography):
- Books 07 vol1+vol2, 25, 28: close was ASCII apostrophe U+0027 → normalised to U+2019
- Book 17: close was U+2019 → kept as U+2019

### Unrounded-u `u^`
In kn-eke.md files, `u^` marks ಉ್ (unrounded-u vowel) — a Havyaka phoneme. This marker is intentional and must NOT be treated as a citation mark or changed to `u'`.

### Nudi/WX encoding artefacts
Books typeset in legacy Nudi font have OCR'd as garbled Latin (É Å ÀÉ ÂÐ etc.). The fix pipeline:
1. Map each Latin glyph to its Nudi→Unicode equivalent using the Nudi codepoint chart
2. Check arka-ottu reversals: Nudi places the ರ್ virama *before* the base consonant; Unicode places it *after*. Pattern: `ರ್X` in Nudi OCR → `Xರ್` in Unicode.
3. Fix oo-matra (ೋ) which Nudi OCR renders as `oo` or `o ̄`
4. Remove per-page running headers (chapter titles repeated in body text)
5. Remove page-break fragments (isolated words/syllables at page boundaries)

### WX-encoded books (books 01–13 transcripts)
These were OCR'd via WX transliteration → Devanagari → Kannada pipeline. Key issue: column-break artifacts place each word/phrase on its own line with no blank line separator → renders as one flat paragraph in Markdown. Fix: detect short non-sentence-final lines and join with spaces. Requires PDF review.

### TOC structure
All kn.md files have a ಪರಿವಿಡಿ/ಒಳಪಿಡಿ table at the top linking to `<a id="adhyAya-N">` anchors. Deep section anchors (`sec-N-M`, `sub-N-M-K`) are pending for most books — see PROJECT-RECAP.md TBD list.

---

## Key Reference Files in Repo

| File | Purpose |
|------|---------|
| `src/main/md/kannada/Eke.md` | Full Eke romanization spec (153KB) — do not edit casually |
| `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md` | Eke quick-reference (vowels, consonants, anusvara, aspirates) |
| `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md` | Complete DNS Bhat word formation reference |
| `src/main/md/kannada/dnsbhat/dns-bhat-analysis.md` | Analysis of 13 DNS Bhat transcript books + Book 14 summary |
| `src/main/md/kannada/dnsbhat/14-nijakku-halegannada-vyakarana-entahadu/` | Book 14: Old Kannada grammar vs Sanskrit — full text + English translation (added Mar 2026) |
| `src/main/md/kannada/dnsbhat/15-inglish-kannada-padanerake/15-inglish-kannada-padanerake-claude-prompt.md` | Book 15: English→Kannada dictionary patterns — 6-step decision tree, 11 domain cluster tables, 100 curated word pairs (added Mar 2026) |
| `src/main/claude/kannada/` | Prior AI session transcripts (session0–5.md) |
| `docs/dnsbhat/PROJECT-RECAP.md` | Full phased project history (Phases 1–17) — canonical record of all OCR cleanup decisions, quote conventions, Eke rules, and pending work |
| `docs/claude-project-instructions.md` | Combined skills + CLAUDE.md context for Claude.ai Projects (phone access) |


### Kannada Directory CLAUDE.md

# Kannada Directory — CLAUDE.md

This directory contains the PRIMARY linguistic work for the ettuge project.

## Key Files
- `Eke.md` — Full Eke romanization specification (153KB) — do NOT edit casually
- `Eke.kn.md` — Complete Kannada translation of Eke.md (DNS Bhat compliant, complete)
- `Eke.eke.md` — Eke romanization of Eke.kn.md (complete)
- `brahmi-nabatian-phoenician-hieroglyphs-lineage.md` — Script history documentation
- `kannada-mnemonics-hieroglyph-hook.md` — Kannada mnemonic table
- `malatibhat_dns_bhat_chat.md` / `malatibhat_dns_bhat_videos.md` — Video references and analysis
- `malatibhat_dns_bhat_videos_links.txt` — Raw video link list

## Subdirectories

### `dnsbhat/` — DNS Bhat Book Collection (29 books, numbered 01–29)
Each book directory follows this file structure:
- `*-book.md` / `*-blog.md` — Raw OCR archive (do NOT edit)
- `*-kn.md` — Structured Kannada source: paragraph breaks, ಪರಿವಿಡಿ TOC, `<a id="adhyAya-N">` anchors
- `*-kn-eke.md` — Eke romanisation (regenerate after kn.md changes)
- `*-en.md` — Chapter-wise English summary with kn.md cross-links
- `*-claude-prompt.md` — Condensed prompt for Claude sessions
- `README.md` — Book index

**Citation quotes:** Standardised to curly single quotes `'word'` (U+2018/U+2019) in kn.md and kn-eke.md. Never use backtick as open-quote.
**Unrounded-u:** `u^` in kn-eke.md = ಉ್ (Havyaka phoneme) — do not alter.
**Nudi OCR:** Books 14–29 were Nudi-encoded; OCR produces garbled Latin. See `.claude/CLAUDE.md` for fix pipeline.
**Project history:** `docs/dnsbhat/PROJECT-RECAP.md`

### `transcripts/` — Raw YouTube transcripts (349+ files, may have ASR artifacts)
### `transcripts_cleaned/` — AI-processed transcripts (130+ files)
### `sections/` — Extracted transcript sections

## Rules for This Directory
1. All new Kannada vocabulary must follow DNS Bhat's native (Dravidian-root) methodology. Reference: `dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
2. Avoid Sanskrit-derived terms when a native Kannada equivalent exists.
3. Eke romanization rules — TWO modes:
   - **Romanising existing Kannada text:** aspirates PRESERVED (ಭ→bh, ಧ→dh, ಖ→kh etc.); retroflexes UPPERCASE (T, D, N, L, S); long vowels UPPERCASE (A, I, U, E, O); vocalic ṛ → x; anusvara ಂ → assimilated nasal (never standalone M); N = exclusively ಣ; r = ರ always, R = rare archaic ಱ.
   - **New native word coining (Ellara):** avoid aspirated consonants — prefer k, g, c, j, T, D, t, d, p, b. All other rules same.
   - Full canonical error table: `.claude/CLAUDE.md` → "Eke Canonical Rules".
4. Always prefer `transcripts_cleaned/` over `transcripts/` for analysis.
5. Files may have Kannada-script names — handle Unicode carefully.

## Unicode
Kannada script range: U+0C80–U+0CFF. Filenames and content may contain Kannada Unicode characters.


### Books Directory CLAUDE.md

# Books Directory — CLAUDE.md

Personal reading catalog.

## Structure
- `Books.md` — Master index organized by author with inline summaries. Categories: Western Fiction, Kannada/Indian Literature, Indian Classical Texts, DNS Bhat linguistics, Science & Biology, History & Biography, Math & Computing, Martial Arts & Physical Practice, Economics & Ideas.
- `Books-Top.md` — Modern Library Top 100 novels list with summaries.
- `influential/` — One file per book with three required sections.

## File Convention for `influential/`
Each book file must contain exactly three sections:
1. **Summary** — concise overview
2. **Critical Takeaways** — objective analysis
3. **My Takeaways** — personal reflection

## TODO
- "Read but Not That Influential" section in `Books.md` is unpopulated
- "Want to Read" section in `Books.md` is unpopulated


### Self-Reflection CLAUDE.md

# Self-Reflection Directory — CLAUDE.md

This directory contains topic-based derivatives of `self.md` and `self-1.md`, personal notes files (Signal channel "self" export, 2021–2026) not stored in the repository. Each entry has been enriched with a 2–4 sentence prose description and a `[→ category]` routing hint.

---

## Structure

- **`README.md`** — Master navigation index listing all topic files with descriptions (displayed automatically on GitHub).
- **`project-recap.md`** — Project recap covering the four phases: cleanup → categorize → enrich+split → consolidate.
- **`YYYY-MM-DD_topic.md`** — Individual topic files, all derived from `self.md`/`self-1.md` on 2026-02-25.

### Current Topic Files

| File | Topic |
|------|-------|
| `2026-02-25_scala-functional-programming.md` | ZIO, Scala 3, Kyo, Haskell, functional effects, type theory |
| `2026-02-25_machine-learning-ai.md` | LLMs, RAG, fine-tuning, Indic LLMs, AI infrastructure |
| `2026-02-25_kannada-language-linguistics.md` | Kannada script, DNS Bhat grammar, Dravidian linguistics, Karnataka culture |
| `2026-02-25_indian-history-culture.md` | Harappan genetics, Indus script, ancient/medieval India, prehistory |
| `2026-02-25_infrastructure-devops.md` | Nix, AWS, Kubernetes, CI tools, EVs |
| `2026-02-25_algorithms-data-structures.md` | LeetCode (Scala), Knight's Tour, system design |
| `2026-02-25_health-fitness.md` | VO2 max, climbing, martial arts, nutrition, cold exposure |
| `2026-02-25_mathematics-science.md` | Riemann hypothesis, Langlands, category theory, biology, geology |
| `2026-02-25_data-engineering.md` | Spark, system design, Kannada data pipeline (alar.ink) |
| `2026-02-25_books-literature.md` | Books read, reading lists, literary essays, reviews |
| `2026-02-25_arts-music-film.md` | Music, cinema, documentaries, visual art, performance |
| `2026-02-25_travel-outdoors.md` | Hiking, adventure sports, Bay Area food, extreme sports |
| `2026-02-25_cricket-sports.md` | Match commentary, IPL analysis, player profiles, sports analytics |
| `2026-02-25_current-events-politics.md` | US/India politics, immigration, geopolitics, civil rights |
| `2026-02-25_career-personal.md` | Career, self-development, personal philosophy, PKM, AI tools |
| `2026-02-25_miscellaneous.md` | **Retired stub** — all content redistributed to the 16 files above |

---

## Rules for This Directory

1. **Enrichment format:** each entry = `**Bold heading**` → 2–4 sentence prose → `**[→ category; cross-link → other-category]**` → URL.
2. **Naming convention:** `YYYY-MM-DD_topic-slug.md` — date reflects when the file was derived.
3. **Cross-linking:** if a note fits multiple categories, it lives in the most specific file and cross-links to others using the `[→]` tag.
4. **`miscellaneous.md`** is retired — all residual entries have been moved to the 16 topic files.
5. **`README.md`** (the index) must be kept in sync whenever new topic files are added.

---

## Adding New Topic Files

When deriving new files from updated `self.md`/`self-1.md` content:
1. Use the date of derivation as the filename prefix (`YYYY-MM-DD`).
2. Add a frontmatter block with `title`, `created`, and `source`.
3. Group by primary subject domain.
4. Add a row to the table in `README.md` and this `CLAUDE.md` table above.


### Haskell Directory CLAUDE.md

# Haskell Directory — CLAUDE.md

Haskell source files for functional programming examples and music composition.

---

## Files

| File | Description |
|------|-------------|
| `accum.hs` | Accumulator examples |
| `cat.hs` | Categorical / functional composition examples |
| `reflection.hs` | Reflection utilities |
| `sqrt.hs` | Square root implementations |
| `ಕಳ್ಳ.hs` | Kannada-named Haskell file (Unicode filename — do not rename) |

## Subdirectories

- `euterpea/` — Music composition using the Euterpea library (`rangapura.hs`, `twinkle.hs`)
- `quick/` — Quick Haskell project managed with Stack

---

## Build & Run

### Quick project (Stack)
```bash
cd src/main/haskell/quick
stack build
stack test
```

### Euterpea music examples
Requires Euterpea installed separately:
```bash
ghc src/main/haskell/euterpea/rangapura.hs
```

### Standalone scripts
Files in the root `haskell/` directory are standalone — compile directly with `ghc`:
```bash
ghc src/main/haskell/sqrt.hs
```

---

## Notes
- There is no top-level Cabal or Stack project for standalone files — only `quick/` uses Stack
- Unicode filenames (Kannada script, e.g. `ಕಳ್ಳ.hs`) are intentional; do not rename or transliterate them
- See root `CLAUDE.md` for Unicode handling guidelines (U+0C80–U+0CFF range)


### Python Directory CLAUDE.md

# Python Directory — CLAUDE.md

YouTube transcript extraction and processing pipeline.

## Setup
```bash
cd src/main/python/yt-transcript
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Script Execution Order
1. `extract_transcripts.py` — raw extraction from YouTube
2. `extract_smart.py` — smart extraction with language detection
3. `cleanup_with_claude.py` — clean transcripts via Claude API
4. `cleanup_books.py` — update books catalog with cleaned transcripts
5. `extract_kannada_only.py` — filter Kannada-only content
6. `transliterate_devanagari.py` — convert Devanagari to Eke romanization

## Critical Notes
- DO NOT bypass proxy rotation or rate-limiting delays in scripts
- `youtube-transcript-api` requires internet access; expect YouTube rate limiting
- Outputs go to `src/main/md/kannada/transcripts/` (raw) and `transcripts_cleaned/` (processed)

