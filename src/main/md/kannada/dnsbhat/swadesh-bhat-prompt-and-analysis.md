# DNS Bhat-Style Word Coining: Prompt Design & Swadesh List Application

## Part 1: The Prompt — Summarized from "Kannadalle Hosapadagalannu Kattuva Bage"

### What the book teaches

DNS Bhat's "ಕನ್ನಡದಲ್ಲಿ ಹೊಸಪದಗಳನ್ನು ಕಟ್ಟುವ ಬಗೆ" (How to Build New Words in Kannada) is essentially a **native word-coining manual**. Its core argument: Kannada has rich, productive morphological machinery — suffixes, compounding rules, and Old Kannada roots — that can generate any word a modern speaker needs, yet writers default to Sanskrit borrowings out of habit and a misplaced inferiority complex toward their own language.

Bhat documents that **50%+ of general Kannada vocabulary and ~80% of scientific/technical terminology** are Sanskrit loanwords, most of which are unnecessary because native Kannada formations exist or can be trivially created.

### The word-formation toolkit Bhat prescribes

**Two methods:**

1. **Derivational (ಕಟ್ಟು ಪದ)** — Attach a native suffix to a root to change word class or meaning
2. **Compounding (ಜೋಡು ಪದ)** — Combine two words where the second is always a noun

**Native Kannada suffixes (the core toolkit):**

| Suffix | Attaches to | Creates | Example |
|--------|------------|---------|---------|
| **-ಗ / -ಇಗ** | Verb root | Agent noun (doer) | ನೋಡು → ನೋಡುಗ (watcher) |
| **-ಗಾರ** | Noun root | Professional/role noun | ಆಟ → ಆಟಗಾರ (player) |
| **-ಇಕೆ** | Verb root | Action/abstract noun | ಕೂಡಿಸು → ಕೂಡಿಕೆ (addition) |
| **-ಗೆ** | Verb root | Result/product noun | ತಿನ್ನು → ತಿನ್ನುಗೆ (food) |
| **-ತ** | Verb root | Patient/undergoer noun | ಕುತ್ತ → ಕುತ್ತ (sufferer) |
| **-ಕೆ** | Verb root | Agent or result | ಅಗೆ → ಅಗೆತ (digger) |
| **-ಕು** | Noun/Adj root | Adjective | (quality-forming, less common) |
| **-ಅಲು** | Noun root | Relational adjective | (expressing "relating to") |

**Compounding rules:**
- Second element = always a noun (provides the semantic head)
- First element = noun, verb (participial form), adjective, or numeral
- Meaning is compositional: first element modifies/specifies the second

**Prefix-like elements (not true prefixes — Kannada uses initial modifiers in compounds):**
- ಮುನ್ (front/before), ಹಿನ್ (back/after), ಕೆಳ (below), ಮೇಲ್ (above)
- These are separate words placed before nouns, not bound morphemes

**Old Kannada as a resource:**
- Archaic roots from Hale Kannada literature are fair game
- Use the ROOT, not the whole archaic word
- Combine with modern suffixes for contemporary intelligibility
- Must still be recognizable to educated modern speakers

**The 5-step methodology:**
1. Identify the concept needing a word
2. Find a native Kannada root (verb or noun) that captures the core meaning
3. Select the right suffix based on what type of word you need (agent, abstract, result, etc.)
4. Combine following Kannada sandhi/phonological rules
5. Test: Would a native speaker understand this without explanation?

**Quality criteria:**
- Semantically transparent (meaning is guessable from parts)
- Phonologically natural (follows existing Kannada sound patterns)
- Simpler than the Sanskrit alternative
- Consistent with patterns already established in the language

---

## Part 2: The Prompt Template for an LLM

Below is the system prompt that would be used to generate Bhat-style Kannada words at scale:

```
You are a Kannada lexicographer following DNS Bhat's principles for native
Kannada word formation, as described in "ಕನ್ನಡದಲ್ಲಿ ಹೊಸಪದಗಳನ್ನು ಕಟ್ಟುವ ಬಗೆ."

CORE PRINCIPLE: Every new Kannada word should be built from native Dravidian
roots and Kannada affixes. Sanskrit borrowings should be replaced wherever a
native formation is possible and intelligible.

TOOLKIT — Native suffixes:
  -ಗ/-ಇಗ  (verb → agent noun: one who does X)
  -ಗಾರ    (noun → professional/role: one associated with X)
  -ಇಕೆ    (verb → abstract/action noun: the act of X)
  -ಗೆ     (verb → result noun: the product/result of X)
  -ತ      (verb → patient noun: one who undergoes X)
  -ಕೆ     (verb → agent or result, for specific verb classes)

TOOLKIT — Compounding:
  [Modifier] + [Noun head]
  First element: noun, verb participle, adjective, or numeral
  Second element: always a noun

TOOLKIT — Prefix-like modifiers:
  ಮುನ್/ಮುಂದ (front/fore), ಹಿನ್/ಹಿಂದ (back/after),
  ಕೆಳ (below/under), ಮೇಲ್ (above/over),
  ಒಳ (inner), ಹೊರ (outer)

METHODOLOGY:
1. Analyze the concept: What is its core semantic content?
2. Find native root: Search existing Kannada verbs/nouns that capture this meaning.
   Prefer roots from spoken Kannada; Old Kannada roots are acceptable if
   the root is still recognizable.
3. Select affix: Match to desired word type (agent, abstract, result, etc.)
4. Combine: Follow Kannada sandhi rules. When in doubt, find an existing
   Kannada word with the same morphological shape and follow its pattern.
5. Verify: The word must be pronounceable, guessable in meaning, and follow
   established Kannada phonology.

OUTPUT FORMAT for each word:
  ಪದ (Word): [new Kannada word in Kannada script]
  ಒಡೆತ (Breakdown): [root] + [affix] or [word1] + [word2]
  ಹುರುಳು (Meaning): [definition in Kannada]
  English gloss: [English meaning]
  ಮಾದರಿ (Pattern precedent): [existing Kannada word showing same pattern]
  ಬದಲಿಸುವ ಪದ (Replaces): [Sanskrit/foreign word being replaced, if any]
  ಬಳಕೆ (Usage example): [one sentence using the word]

IMPORTANT RULES:
- NEVER use Sanskrit affixes (upa-, ati-, vi-, abhi-) when a native Kannada
  modifier exists
- Prefer transparent compounds over opaque derivations
- If multiple formations are possible, provide all with a recommendation
- Mark confidence level: ಕಟ್ಟುನಿಟ್ಟು (certain — follows established pattern)
  or ಹೊಸಹೊಲಬು (experimental — extends a pattern in a new direction)
```

---

## Part 3: Applying to the Swadesh List — Non-Native Entries

The Swadesh 207-word list is designed to contain basic vocabulary that tends to be **native** in most languages. For Kannada, the majority of Swadesh words are indeed native Dravidian. However, several entries have Sanskrit borrowings as their standard/common form in modern Kannada, even when native Dravidian alternatives exist (sometimes only in dialects or older literature).

Below I identify the Swadesh entries where the commonly listed Kannada form is non-native (Sanskrit or other borrowing), and then apply Bhat's methodology.

### Entries Where Standard Kannada Uses a Sanskrit Form

| # | English | Standard Kannada | Origin | Native Alternative (if known) |
|---|---------|-----------------|--------|-------------------------------|
| 1 | person/human | ಮನುಷ್ಯ (manushya) | Sanskrit (manuṣya) | ನರ (archaic Dravidian), ಆಳು (native) |
| 2 | animal | ಪ್ರಾಣಿ (praaNi) | Sanskrit (prāṇin) | — (no single-word native equivalent in common use) |
| 3 | skin | ಚರ್ಮ (charma) | Sanskrit (carman) | ತೊಗಲು (togalu, native Dravidian) |
| 4 | blood | ರಕ್ತ (rakta) | Sanskrit (rakta) | ನೆತ್ತರು (nettaru, native Dravidian) |
| 5 | heart (organ) | ಹೃದಯ (hRdaya) | Sanskrit (hṛdaya) | ಎದೆ (ede, native — means "chest" but also "heart") |
| 6 | liver | ಯಕೃತ್ (yakRt) | Sanskrit (yakṛt) | ಈರಲು (eeralu, native Dravidian) |
| 7 | sun | ಸೂರ್ಯ (suurya) | Sanskrit (sūrya) | ಬಿಸಿಲು (bisilu, "sunshine"), ತೇಜ (archaic) |
| 8 | moon | ಚಂದ್ರ (chandra) | Sanskrit (candra) | ತಿಂಗಳು (tingaLu, native Dravidian) |
| 9 | star | ನಕ್ಷತ್ರ (nakshatra) | Sanskrit (nakṣatra) | ಚುಕ್ಕಿ (chukki) / ತಾರೆ (taare, native Dravidian) |
| 10 | earth/ground | ಭೂಮಿ (bhuumi) | Sanskrit (bhūmi) | ನೆಲ (nela), ಮಣ್ಣು (maNNu) — both native |
| 11 | sea | ಸಮುದ್ರ (samudra) | Sanskrit (samudra) | ಕಡಲು (kadalu, native Dravidian) |
| 12 | night | ರಾತ್ರಿ (raatri) | Sanskrit (rātri) | ಇರುಳು (iruLu, native Dravidian) |
| 13 | seed | ಬೀಜ (biija) | Sanskrit (bīja) | ಬಿತ್ತ (bitta, native Dravidian) |
| 14 | tail | ಬಾಲ (baala) | Sanskrit (bāla) | ಬಾಲ may be acceptable; but ಕೊಡಿ (koDi) exists in some dialects |
| 15 | snake | ಸರ್ಪ (sarpa) | Sanskrit (sarpa) | ಹಾವು (haavu, native Dravidian — this IS commonly used) |
| 16 | worm | ಕ್ರಿಮಿ (krimi) | Sanskrit (kṛmi) | ಹುಳು (huLu, native Dravidian) |
| 17 | year | ವರ್ಷ (varsha) | Sanskrit (varṣa) | — (ಆಂಡು/ಆಡು exists in Old Kannada) |
| 18 | mountain | ಪರ್ವತ (parvata) | Sanskrit (parvata) | ಬೆಟ್ಟ (beTTa) / ಗುಡ್ಡ (guDDa) — both native |
| 19 | river | ನದಿ (nadi) | Sanskrit (nadī) | ಹೊಳೆ (hoLe, native Dravidian) |
| 20 | road/path | ಮಾರ್ಗ (maarga) | Sanskrit (mārga) | ದಾರಿ (daari) / ಹಾದಿ (haadi) — both native |
| 21 | dust | ಧೂಳು (dhuuLu) | Sanskrit (dhūli) | ಮಣ್ಣು (maNNu = earth/dust), ಪುಡಿ (puDi) |
| 22 | ice/snow | ಹಿಮ (hima) | Sanskrit (hima) | ಮಂಜುಗಡ್ಡೆ (manju + gaDDe, "fog-lump" — native compound) |
| 23 | sleep (n.) | ನಿದ್ರೆ/ನಿದ್ದೆ (nidre) | Sanskrit (nidrā) | ಎಚ್ಚರ is "wakefulness"; native verb ಮಲಗು exists but no common native noun |

**Note:** For several items (snake → ಹಾವು, mountain → ಬೆಟ್ಟ, river → ಹೊಳೆ, path → ದಾರಿ, star → ಚುಕ್ಕಿ), the native Dravidian form already exists in everyday spoken Kannada — it's primarily in formal/written registers that the Sanskrit form dominates. Bhat's reform is partly about legitimizing in writing what people already say.

---

## Part 4: Coining Bhat-Style Words for Entries Lacking Native Forms

For entries where no obvious native single-word equivalent exists, here is how Bhat's methodology applies:

### 1. "animal" — replacing ಪ್ರಾಣಿ (praaNi, Sanskrit)

**Analysis:** "animal" = a living creature that moves. The Sanskrit word comes from ಪ್ರಾಣ (breath/life). We need a native Kannada root capturing "living/breathing creature."

**Approach A — Derivational:**
- Root: ಉಸಿರು (usiru, "breath" — native Dravidian)
- Suffix: -ಇಗ (agent: one who does X)
- **Coined word: ಉಸಿರಿಗ** (usirига) — "one that breathes; a breathing creature"
- Pattern precedent: ನೋಡುಗ (one who watches)
- Confidence: ಹೊಸಹೊಲಬು (experimental — extends established pattern)

**Approach B — Compounding:**
- ಉಸಿರು (breath) + ಜೀವಿ → but ಜೀವಿ is Sanskrit
- Better: ಉಸಿರು (breath) + ಉಳ್ಳ (having) → ಉಸಿರುಳ್ಳದು — "that which has breath" (too long)
- Better: use verb ಅಲೆ (ale, "to wander/move") + -ಇಗ → **ಅಲೆಯಿಗ** — "one that moves about"

**Approach C — Old Kannada revival:**
- Old Kannada ಪುಲ್ (pul) appears in ಪುಲಿ (puli, "tiger") and related forms
- But too specific; doesn't generalize to "animal"

**Recommendation:** ಉಸಿರಿಗ or use existing dialectal/spoken ಜೀವ (which, while ultimately from Sanskrit *jīva*, is deeply naturalized in Kannada speech — Bhat acknowledges that long-naturalized borrowings with Kannada phonology are acceptable).

---

### 2. "year" — replacing ವರ್ಷ (varsha, Sanskrit)

**Analysis:** "year" = a full cycle of seasons. Old Kannada had ಆಂಡು (aaNDu), cognate with Tamil ஆண்டு (āṇṭu).

**Coined word: ಆಂಡು** (revival of Old Kannada form)
- This is a direct Dravidian cognate shared with Tamil
- Perfectly precedented — Bhat explicitly advocates reviving Old Kannada roots
- Pattern: Not derivation but **revival** of an existing Dravidian word
- Confidence: ಕಟ್ಟುನಿಟ್ಟು (certain — this word existed and its cognate thrives in Tamil)

---

### 3. "person/human" — replacing ಮನುಷ್ಯ (manushya, Sanskrit)

**Analysis:** "person" = a human being. Native Kannada has ಆಳು (aaLu, "person/servant" — but has acquired a subservient connotation). Old Kannada ನರ (nara) exists but may itself be from Sanskrit.

**Approach — Compounding:**
- Root: ಮಾತಿಗ (maatiga, from ಮಾತು "speech") — "one who speaks; a speaking being"
- Suffix: -ಗ (agent from verb ಮಾತನಾಡು "to speak")
- Pattern: ನೋಡುಗ (viewer), ಕೇಳುಗ (listener)
- **Coined word: ಮಾತಿಗ** — "the speaking one" (distinguishes humans from animals by speech)
- Confidence: ಹೊಸಹೊಲಬು

**Alternative:** Simply use ಜನ (jana) — while originally Sanskrit, it is so deeply naturalized (ಜನರು = people) that even purists accept it. Or ಗಂಡು/ಹೆಣ್ಣು for gendered forms.

---

### 4. "dust" — replacing ಧೂಳು (dhuuLu, Sanskrit dhūli)

**Analysis:** Fine dry particles of earth.

**Approach:** ಪುಡಿ (puDi, "powder/fine particles" — native Dravidian) already exists in spoken Kannada.
- Also: ಮಣ್ಣು (maNNu, "earth/dirt") covers some senses
- For airborne dust specifically: ತೂಳಿ (cognate exists in some Dravidian languages)
- **Recommendation: ಪುಡಿ** for "dust/powder" — already native and in use
- Confidence: ಕಟ್ಟುನಿಟ್ಟು (this is just legitimizing an existing native word)

---

### 5. "sleep" (noun) — replacing ನಿದ್ರೆ/ನಿದ್ದೆ (Sanskrit nidrā)

**Analysis:** The state of sleeping. The native verb ಮಲಗು (malagu, "to lie down/sleep") exists.

**Approach — Derivational:**
- Root: ಮಲಗು (to sleep/lie down)
- Suffix: -ಇಕೆ (action/abstract noun)
- **Coined word: ಮಲಗಿಕೆ** (malagike) — "the act/state of sleeping"
- Pattern precedent: ಮೆಚ್ಚಿಕೆ (the act of liking), ಕೂಡಿಕೆ (addition)
- Confidence: ಕಟ್ಟುನಿಟ್ಟು (exact pattern already established)

**Alternative:** ನಿದ್ದೆ is so deeply naturalized that some consider it native Kannada at this point (phonological adaptation is complete). Bhat might accept it.

---

### 6. "ice/snow" — replacing ಹಿಮ (Sanskrit hima)

**Analysis:** Frozen water. Kannada already has the compound ಮಂಜುಗಡ್ಡೆ (manju + gaDDe = "fog-lump").

**Approach — Compounding:**
- ಮಂಜು (manju, "fog/mist/cold" — native Dravidian)
- ಗಡ್ಡೆ (gaDDe, "lump/tuber" — native Dravidian)
- **ಮಂಜುಗಡ್ಡೆ** is already the native compound and widely used
- For "snow" specifically: ಮಂಜು alone can work (as in Tamil மஞ்சு)
- For "ice": ಮಂಜುಗಡ್ಡೆ or shortened ಮಂಗಡ್ಡೆ
- Confidence: ಕಟ್ಟುನಿಟ್ಟು (compound already in use)

---

## Part 5: Summary — The Swadesh Verdict

Of the standard 207 Swadesh words, **roughly 180-185 already have native Dravidian forms** in common Kannada use. This is expected — the Swadesh list targets core vocabulary that resists borrowing.

The ~20-25 entries that use Sanskrit forms in standard written Kannada fall into three categories:

### Category A: Native form exists but is stigmatized in formal writing (~12 entries)
These need NO coining — just legitimization. Bhat's reform here is cultural, not linguistic.

| Written (Sanskrit) | Spoken (Native) | Status |
|-------------------|-----------------|--------|
| ರಕ್ತ (blood) | ನೆತ್ತರು | Just use the native form in writing |
| ಚರ್ಮ (skin) | ತೊಗಲು | Just use the native form |
| ಸೂರ್ಯ (sun) | — (see below) | Compound needed |
| ಚಂದ್ರ (moon) | ತಿಂಗಳು | Just use the native form |
| ನಕ್ಷತ್ರ (star) | ಚುಕ್ಕಿ / ತಾರೆ | Just use the native form |
| ಭೂಮಿ (earth) | ನೆಲ / ಮಣ್ಣು | Just use the native form |
| ಸಮುದ್ರ (sea) | ಕಡಲು | Just use the native form |
| ರಾತ್ರಿ (night) | ಇರುಳು | Just use the native form |
| ಬೀಜ (seed) | ಬಿತ್ತ | Just use the native form |
| ಪರ್ವತ (mountain) | ಬೆಟ್ಟ / ಗುಡ್ಡ | Just use the native form |
| ನದಿ (river) | ಹೊಳೆ | Just use the native form |
| ಮಾರ್ಗ (road) | ದಾರಿ / ಹಾದಿ | Just use the native form |

### Category B: Old Kannada form can be revived (~5 entries)

| Sanskrit | Revival | Source |
|----------|---------|--------|
| ವರ್ಷ (year) | ಆಂಡು | Old Kannada, cognate with Tamil ஆண்டு |
| ಹೃದಯ (heart) | ಎದೆ (already means "chest/heart") | Expand semantic range |
| ಯಕೃತ್ (liver) | ಈರಲು | Dravidian, still in some dialects |
| ಧೂಳು (dust) | ಪುಡಿ | Already in spoken use |
| ಸೂರ್ಯ (sun) | ಬಿಸಿಲ್ಗೂಡು? or revive Old Kannada ಪೊಳ್ತು (poLtu, "time/sun") | Needs community consensus |

### Category C: Genuine coining needed (~3-5 entries)

| Concept | Challenge | Bhat-style approach |
|---------|-----------|-------------------|
| animal (ಪ್ರಾಣಿ) | No single native word | ಉಸಿರಿಗ (breathing-one) or accept naturalized ಜೀವ |
| person (ಮನುಷ್ಯ) | Native ಆಳು has connotation shift | ಮಾತಿಗ (speaking-one) or accept naturalized ಜನ |
| sleep (n.) (ನಿದ್ರೆ) | No native noun form in common use | ಮಲಗಿಕೆ (from ಮಲಗು + -ಇಕೆ) |

---

## Part 6: What This Tells Us About the Larger Wiktionary Project

The Swadesh list exercise reveals that **the biggest win in a Bhat-style Kannada Wiktionary isn't coining new words — it's legitimizing existing native words** that speakers already use but that formal/literary Kannada suppresses in favor of Sanskrit equivalents.

For the full Wiktionary project:
- **~60-70% of effort** would be documenting native words that already exist in speech but lack formal dictionary recognition
- **~20-25% of effort** would be reviving Old Kannada roots with modern suffixes
- **~10-15% of effort** would be genuine new coinages for modern/technical concepts

This is actually good news for cost estimation — the "legitimization" entries are simpler (less creative generation, more documentation) and could use cheaper models or even template-based generation.
