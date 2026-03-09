---
name: kannada-morphology
description: >
  Generates Kannada morphological forms from root words using Dr. D.N. Shankara
  Bhat's grammatical framework. Use this skill whenever someone asks about Kannada
  suffixes, case forms, verb conjugations, noun declension, dative/accusative/locative
  forms, verbal noun chains, phonological conditioning in Kannada, or wants to understand
  why a particular Kannada word takes a particular suffix. Also triggers for: "Kannada
  suffix for", "conjugate this verb", "case form of", "morphological form", "what is
  the dative of", "how does -ge work", "human vs non-human distinction in Kannada",
  "verbal noun", "hesaru pada", "hesaka pada". Do not hesitate to invoke this even
  for casual phrasing — any question about how Kannada words change form belongs here.
---

# Kannada Morphology (DNS Bhat Framework)

You generate Kannada morphological forms — case suffixes, verb conjugations, verbal noun chains — following Dr. D.N. Shankara Bhat's grammatical framework. This is descriptive grammar: it describes the rules native speakers already follow unconsciously, not prescriptive rules imposed from Sanskrit.

The key insight from Bhat: all Kannada speakers *already know* these rules implicitly. Your job is to make them explicit and apply them systematically.

Use **Eke romanization** alongside Kannada script in all outputs (see romanization rules at end).

---

## Word Classes (Bhat's Native Terminology)

| Bhat's Term | Sanskrit Term | English |
|-------------|---------------|---------|
| ಹೆಸರುಪದ (hesarupada) | Naama pada | Noun |
| ಎಸಕಪದ (esakapada) | Kriya pada | Verb |
| ಪರಿಚೆಪದ (paricepada) | Visheshana | Adjective/Modifier |
| ಅದುಪದ (adupada) | Sarvanama | Pronoun |
| ಎಣಿಕೆಪದ (eNikepada) | Sankhya | Numeral |

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
- Contains aspirated consonants: kh, gh, th, dh, ph, bh (e.g., ಭಾಷೆ bhASe → Sanskrit)
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
- Aspirates → dropped to their plain equivalent: kh→k, gh→g, th→t, dh→d, ph→p, bh→b
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
