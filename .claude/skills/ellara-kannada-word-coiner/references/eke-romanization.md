# Eke Romanization Reference

Eke (ಏಕೆ) is the romanization system for Kannada used in this project. It blends Informal Kannada (IK) with the Harvard-Kyoto (HK) protocol, adapted for native Kannada usage. It provides **two modes**:

- **Eke** — direct transliteration, preserving all formal distinctions (aspirates, legacy consonants), 41 symbols
- **Eke(ek)** — transliteration using *ellara kannaDa* (EK) simplifications: aspirates dropped, 31 symbols

**For word-coining work, use Eke(ek)** — we coin native EK words, which have no aspirates.

---

## Case Sensitivity

Uppercase = retroflex, special, or long:

| Uppercase | Meaning | Lowercase | Meaning |
|-----------|---------|-----------|---------|
| T | retroflex ಟ | t | dental ತ |
| D | retroflex ಡ | d | dental ದ |
| N | retroflex ಣ | n | dental ನ |
| L | retroflex ಳ | l | dental ಲ |
| S | palatal sibilant ಶ | s | alveolar ಸ |
| A | long ಆ | a | short ಅ |
| I | long ಈ | i | short ಇ |
| U | long ಊ | u | short ಉ |
| E | long ಏ | e | short ಎ |
| O | long ಓ | o | short ಒ |
| R | ಱ (archaic retroflex ṟ — preserved in Eke romanisation; in EK speech sounds like r) | r | ರ (common r — **always lowercase**) |
| Z | old ೞ (→ L in EK) | — | — |
| G | velar nasal ಙ | g | ಗ |
| Y | palatal nasal ಞ | y | ಯ |
| H | visarga ಃ | h | ಹ |
| X | ೠ / ೄ (vocalic ṝ, long — very rare) | x | ಋ / ೃ (vocalic ṛ, short) |

**Key distinction**: S = ಶ (palatal sibilant), NOT a generic "sh". s = ಸ (alveolar). These are different sounds.

---

## EK Consonants (Eke(ek) — 21 consonants)

Place of articulation × voicing, plus sonorants:

|           | voiceless | voiced | nasal   | pre-nasal (anusvAra) |
|-----------|-----------|--------|---------|----------------------|
| velar     | ka ಕ      | ga ಗ   |         | nka ಂಕ / nga ಂಗ      |
| palatal   | ca ಚ      | ja ಜ   |         | nca ಂಚ / nja ಂಜ      |
| retroflex | Ta ಟ      | Da ಡ   | Na ಣ    | nTa ಂಟ / nDa ಂಡ      |
| dental    | ta ತ      | da ದ   | na ನ    | nta ಂತ / nda ಂದ      |
| labial    | pa ಪ      | ba ಬ   | ma ಮ    | mpa ಂಪ / mba ಂಬ      |

Sonorants: ya ಯ, ra ರ, la ಲ, va ವ

Sibilants/fricatives: Sa ಶ, sa ಸ, ha ಹ, La ಳ

---

## Aspirates (Eke vs Eke(ek))

In full Eke, aspirates use digraphs. In Eke(ek), drop the `h`:

| Eke | Eke(ek) | Kannada |
|-----|---------|---------|
| kha | ka (→k) | ಖ |
| gha | ga (→g) | ಘ |
| cha | ca (→c) | ಛ |
| jha | ja (→j) | ಝ |
| Tha | Ta (→T) | ಠ |
| Dha | Da (→D) | ಢ |
| tha | ta (→t) | ಥ |
| dha | da (→d) | ಧ |
| pha | pa (→p) | ಫ |
| bha | ba (→b) | ಭ |
| Sha | Sa (→S) | ಷ → ಶ |

**Parenthetical notation**: When an aspirate is optional (allowed in EK but not required), show it in parentheses: `kaS(h)TagaLa`, `vid(h)i`.

---

## Vowels

| Kannada | EK equivalent | Eke | Note |
|---------|---------------|-----|------|
| ಅ | ಅ | a | short |
| ಆ | ಆ | A | long |
| ಇ | ಇ | i | short |
| ಈ | ಈ | I | long |
| ಉ | ಉ | u | short |
| ಊ | ಊ | U | long |
| ಎ | ಎ | e | short |
| ಏ | ಏ | E | long |
| ಒ | ಒ | o | short |
| ಓ | ಓ | O | long |
| ಐ | ಅಯ್ | ay | diphthong (EK: ay not ai) |
| ಔ | ಅವ್ | av | diphthong (EK: av not au) |
| ಋ / ೃ | — | x | vocalic ṛ (short), Sanskrit loanwords — e.g. ಸಂಸ್ಕೃತ→`samskxta`, ಸೃಷ್ಟಿ→`sxShTi` |
| ೠ / ೄ | — | X | vocalic ṝ (long) — extremely rare |
| ಃ | — | H | visarga, rare in EK |

---

## Diphthongs

In EK, the formal diphthong vowels ಐ and ಔ are written as sequences:
- ಐ → ಅಯ್ → **ay**
- ಔ → ಅವ್ → **av**

Other vowel+glide combinations: iy, Iy, uy, Uy, ey, Ey, oy, Oy (with ಯ್); iv, Iv, uv, Uv, ev, Ev, ov, Ov (with ವ್).

---

## Nasal Assimilation (anusvAra Rules)

The anusvAra ಂ before a plosive is written as the nasal+plosive combination:

**Before ordered plosives** (Rule 3):
| anusvAra + | Eke(ek) | Kannada |
|------------|---------|---------|
| ಕ | nka | ಂಕ |
| ಗ | nga | ಂಗ |
| ಚ | nca | ಂಚ |
| ಜ | nja | ಂಜ |
| ಟ | nTa | ಂಟ |
| ಡ | nDa | ಂಡ |
| ತ | nta | ಂತ |
| ದ | nda | ಂದ |
| ಪ | mpa | ಂಪ |
| ಬ | mba | ಂಬ |

**Before sonorants/sibilants** (Rule 3b) — use m or n by phonological approximation:

| after anusvAra | prefix |
|----------------|--------|
| y, l, S, s, h, L | **m** |
| r, v, R, Z | **n** |

Examples: ಂಶ = mSa, ಂಸ = msa, ಂರ = nra, ಂವ = nva

> **Critical disambiguation**: `N` (uppercase) is **exclusively** retroflex ಣ. Never write N as anusvara before stop consonants — `linga` not `liNga`, `tunDu` not `tuNDu`. The anusvara before g/k/d/t/b/p/c/j always uses lowercase `n` or `m`.

---

## Six Transliteration Rules Summary

1. **Aspirates (Eke(ek))**: Drop `h` in aspirate digraphs: kh→k, gh→g, ch→c, jh→j, Th→T, Dh→D, th→t, dh→d, ph→p, bh→b, Sh→S
2. **Old Kannada letters**: ಱ → `R` in Eke romanisation (preserved to mark the archaic retroflex ṟ; in EK speech it sounds like r); ೞ (Za) → `L`
3. **Nasal assimilation — never M**: anusvAra ಂ always written as the assimilated nasal+C pair. Before labials (b,p,m,v,h,y) → **m**; before all others → **n**. Examples: `kamba`, `kankaNa`, `samskxta`. N (uppercase) is exclusively ಣ (retroflex nasal) — never use N as anusvara.
4. **Case sensitivity**: Uppercase = retroflex or special; S = ಶ/ಷ (not sh); long vowels uppercase (A, I, U, E, O); x = ಋ/ೃ (vocalic ṛ short), X = ೠ/ೄ (vocalic ṝ long)
5. **Inherent vowel**: Every consonant has inherent `a`; suppressed by virama ್ in clusters
6. **Parenthetical optional aspirate**: `kaS(h)TagaLa` — `h` in parens = can be dropped in Eke(ek)

---

## Examples — Coined Words

| Kannada | Eke(ek) | Meaning |
|---------|---------|---------|
| ಕನ್ನಡ | kannaDa | Kannada |
| ಎಲ್ಲರಾಳ್ವಿಕೆ | ellarALvike | democracy (rule of all) |
| ಉಸಿರಿಯರಿಮೆ | usiriyarime | biology (study of life) |
| ಗೆಂಟುತೋರ್ಪುಕ | genTutOrpuka | telescope (far-shower) |
| ಬಿಸಿಯಳಕ | bisiyaLaka | thermometer (heat-measurer) |
| ಬಾನಹಾಯ್ಗ | bAnahAyga | astronaut (sky-navigator) |
| ಬೆಳಕುಬರಹ | beLakubaraha | photograph (light-writing) |
| ತಿಳಿಯರಿಮೆ | tiLiyarime | algorithm (clarity-knowledge) |
| ಕಣಜ | kaNaja | database (storehouse) |
| ಹೆಜ್ಜೆಗಾರ | hejjegAra | programmer (step-maker) |

Note: `genTutOrpuka` — the capital T is retroflex ಟ, capital O is long ಓ; `bAnahAyga` — capital A is long ಆ.
