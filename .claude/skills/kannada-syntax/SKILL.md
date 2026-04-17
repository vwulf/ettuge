---
name: kannada-syntax
description: >
  Answers questions about Kannada sentence structure and syntax using D. N.
  Shankara Bhat's framework from Books 25 and 07. Covers: SOV word order,
  clause combining (converbs, participial forms), relative clauses (pre-nominal
  participial), embedded clauses, sentence coordination, nominal and verbal
  phrase structure, case marking in sentences, and how Kannada syntax differs
  from both Sanskrit and English. Trigger phrases: "Kannada sentence structure",
  "Kannada word order", "SOV", "Kannada relative clause", "ಕನ್ನಡ ವಾಕ್ಯ",
  "clause combining Kannada", "Kannada converb", "embedded clause Kannada",
  "ಕನ್ನಡ ವಾಕ್ಯಗಳ ಒಳರಚನೆ", "how do you join sentences in Kannada".
---

# Kannada Syntax

You answer questions about Kannada sentence structure using D. N. Shankara
Bhat's framework from two primary sources.

---

## Source Material — Readiness Status

| Book | Title | Status | Content |
|------|-------|--------|---------|
| **Book 25** | *ಕನ್ನಡ ವಾಕ್ಯಗಳ ಒಳರಚನೆ* | ✅ Full text, chapter pages | Kannada sentence structure (primary source) |
| **Book 07** | *ಕನ್ನಡ ಬರಹದ ಸೊಲ್ಲರಿಮೆ* (4 vols) | ✅ Full text, chapter pages | Grammar of written Kannada — syntax in Vols 1–4 |

Book 25 is the dedicated syntax monograph. Book 07 treats syntax as part of a
full reference grammar of written Kannada.

**Note:** Book 25 english summary (`book/en/summary.md`) is only 290 lines —
a stub. For detailed syntax questions, fetch the Kannada chapter pages directly.

---

## Core Typological Properties of Kannada Syntax

### 1. SOV Word Order (Verb-Final)

Kannada is a **Subject-Object-Verb** language. The finite verb goes at the end:

> ರಾಮನು ಊಟ ಮಾಡಿದ.
> *rAmanu UTa mADida.*
> Rama food did. = "Rama ate food."

**Corollary:** All modifiers precede their heads:
- Adjectives before nouns: ಚಿಕ್ಕ ಹುಡುಗಿ (*cikka huDugi* / small girl) ✓
- \*ಹುಡುಗಿ ಚಿಕ್ಕ (*huDugi cikka*) ✗
- Relative clauses before the noun they modify (see below)
- Postpositions (not prepositions): ಮನೆಯಲ್ಲಿ (*maneyalli* / in-the-house) — suffix follows

### 2. Clause Combining via Converbs

Kannada joins clauses using **converb forms** — non-finite verb forms that express
a subordinate event with the same subject as the main clause:

**The co-reference constraint:** When two action clauses are joined via a converb,
both must have the **same subject**. Violation sounds ungrammatical:

> ರಾಜು ಮನೆಗೆ ಬಂದು ಊಟ ಮಾಡಿದ. ✓
> *rAju manege bandu UTa mADida.*
> Raju home came-CONV food ate. = "Raju came home and ate."
> (same subject: Raju did both actions)

> \*ರಾಜು ಮನೆಗೆ ಬಂದು ಜಾನಕಿ ಊಟ ಮಾಡಿದಳು. ✗
> (different subjects: Raju came, Janaki ate — ungrammatical with converb)

**Exception:** Converb joining a non-volitional (agentless) clause to an active clause
*can* have different participants:
> ರಾಜು ಮನೆಗೆ ಬಂದು ಜಾನಕಿಗೆ ತೊಂದರೆಯಾಯಿತು. ✓
> (Raju came home and [it] caused trouble for Janaki — one is action, one is event)

### 3. Pre-Nominal Relative Clauses

Unlike English (where relative clauses *follow* the noun: "the girl **who came**"),
Kannada uses a **participial form before the noun**:

> ಬಂದ ಹುಡುಗಿ / *banda huDugi* / "came-PART girl" = "the girl who came"
> ಓದುವ ಹುಡುಗ / *ODuva huDuga* / "reads-PART boy" = "the boy who reads"

The participial suffixes:
- **-da** (past participial): ಮಾಡಿದ (*mADida*) = "the one who did"
- **-uva** (present participial): ಮಾಡುವ (*mADuva*) = "the one who does"
- **-ada** (negative participial): ಮಾಡದ (*mADada*) = "the one who didn't do"

### 4. Verbal Noun Chains

Verbs become nouns, then take case suffixes to express purpose, means, location of activity:

```
ಓದು → ಓದುವ → ಓದುವುದು → ಓದುವುದಕ್ಕೆ
ODu  →  ODuva  →  ODuvudu  →  ODuvudakke
read   read-PART  reading(N)   for-reading
```

The verbal noun (**-uvudu** form) can appear in any nominal case slot:
- Nominative: ಓದುವುದು ಒಳ್ಳೆಯದು = "Reading is good"
- Dative: ಓದುವುದಕ್ಕೆ ಬಂದ = "came for reading"
- Locative: ಓದುವುದರಲ್ಲಿ ಖುಷಿ = "joy in reading"

### 5. Sentence-Final Particles and Mood

Kannada sentence type (declarative, interrogative, imperative) is marked
primarily by sentence-final forms:
- **Declarative:** verb takes indicative finite suffix
- **Yes/No question:** particle -ಆ (*-A*) or rising intonation
- **WH-question:** question word in situ (not moved to front)
- **Negative:** verb takes negative participial + auxiliary *illa* or negative
  finite suffix

---

## Sentence Types and Their Structures

### Simple Sentences
```
Subject(NOM) [Object(ACC)] Verb(finite)
ಅವನು ಊಟ ಮಾಡಿದ. = He ate (food).
avanu UTa mADida.
```

### Existential Sentences
```
Subject(NOM) Location(LOC) ಇದ್ದಾನೆ/ಇದ್ದಾಳೆ/ಇದೆ
ಮನೆಯಲ್ಲಿ ಮಕ್ಕಳಿದ್ದಾರೆ. = Children are in the house.
```

### Conditional Clauses
Formed with conditional verb form + main clause:
```
ಮಳೆ ಬಂದರೆ ನಾನು ಹೋಗಲ್ಲ. = If it rains, I won't go.
maLe bandare nAnu hOgalla.
```

### Causative Sentences
```
ಅಮ್ಮ ಮಗನಿಗೆ ಊಟ ಮಾಡಿಸಿದಳು. = Mother made the son eat.
```

---

## How Kannada Syntax Differs from Sanskrit

| Feature | Sanskrit | Kannada |
|---------|---------|---------|
| Word order | Relatively free (inflectional) | SOV strict (agglutinative) |
| Relative clause | Post-nominal (ya-relative) | Pre-nominal (participial) |
| Clause combining | Participial constructions (tvā, tuṃ, sati-saptami) | Converb constraint (same-subject required) |
| Negation | Sanskrit neg particles | Morphologically marked on verb |
| Question formation | Particle position varies | Particle sentence-final |

---

## Fetching Source Content

**Book 25** chapter pages:
Base URL: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/25-kannaDa-vAkyagaLa-oLaracane`

| Chapter | Title | URL suffix |
|---------|-------|-----------|
| ch0 | Chapter index | `/book/kn/ch0` |
| ch1 | ಮುನ್ನೋಟ (Overview) | `/book/kn/ch1` |
| ch2 | ಪದಗಳ ಇಟ್ಟಳ (Word structure) | `/book/kn/ch2` |
| ch3–ch11 | Sentence structure chapters | `/book/kn/ch3` through `/ch11` |

**Book 07** (full grammar of written Kannada):
Base URL: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/07-kannaDa-barahada-sollarime`
- Vol 1: word structure (`/book/vol1/kn/ch0` through `ch4`)
- Vol 2: word-form structure (`/book/vol2/kn/ch0` through `ch2`)
- Vol 3: sentence structure (`/book/vol3/kn/full`)
- Vol 4: pronouns and demonstratives (`/book/vol4/kn/full`)

---

## Answering Guidelines

1. **Primary source is Book 25** for dedicated syntax. Book 07 for grammar-in-context.
2. **Co-reference constraint on converbs** is the most important syntactic fact to
   get right — this distinguishes Kannada from both Sanskrit and English.
3. **Pre-nominal participials** are the key relative clause pattern — always lead
   with a concrete example.
4. **Verbal noun chains** (the *-uvudu* forms) are uniquely productive — show the
   full chain when explaining purpose/manner constructions.
5. For questions about morphology (suffixes, conjugation), refer to the
   `kannada-morphology` skill. This skill focuses on sentence-level patterns.
6. **English summary stub:** Book 25's en/summary.md is sparse. For detailed
   questions, fetch the Kannada chapter pages and read them directly.
