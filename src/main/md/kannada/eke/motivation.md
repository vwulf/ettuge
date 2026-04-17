---
title: Motivation
nav_order: 2
---

# Why Eke?

## The problem with Kannada romanisation

Kannada has no single accepted romanisation. Writers on the internet borrow whatever feels natural — some use IAST (`ā`, `ṭ`, `ḷ`), others use Hindi-inflected transliterations, and most use something ad hoc. The result: the same word appears dozens of ways, no scheme is searchable, and learners cannot reliably convert between script and roman.

Meanwhile, the two rigorous scholarly systems have real drawbacks:

- **IAST** — requires diacritic characters (ā, ī, ṭ, ḍ, ṇ, ḷ) that can't be typed on a standard keyboard and don't sort or search well in plain text
- **Harvard-Kyoto (HK)** — designed for Sanskrit, not Kannada; represents anusvara as standalone `M` (which is phonologically wrong for Kannada), conflates ಶ and ಷ, and has no natural way to represent Dravidian vowel distinctions

Despite these drawbacks, ASCII-based romanisation has a significant advantage that the native scripts don't: **cross-language readability across Dravidian languages.** A reader familiar with HK or Eke can follow Kannada, Tamil, Telugu, and Malayalam texts in romanisation with relatively little additional learning — the same consonant and vowel symbols appear in all four systems. Speakers of non-Dravidian languages who are comfortable with the English alphabet can also adjust to reading Dravidian languages in Eke far more quickly than they could learn a new script.

## DNS Bhat's influence: *Ellara Kannada*

Dr. D.N. Shankara Bhat's *Ellara Kannada* reform argues that modern written Kannada should reflect how the language is actually spoken, not how Sanskrit grammar was once overlaid on it. Native Kannada has no *mahaprāṇa* (aspirated consonants) — `bh`, `dh`, `kh` etc. are borrowings from Sanskrit that do not appear in Dravidian root words. Eke(ek) — the coining mode — follows this: new native words avoid aspirates.

## *Hosabaraha* orthography

Hosabaraha (Vishwas's Kannada input system) uses a consistent phone-key mapping for Kannada characters. Its orthographic conventions are the same as Ellara Kannada — Hosabaraha *is* the Kannada-script counterpart of Eke(ek). Eke formalises this mapping as a romanisation that:
- Works with plain ASCII on any keyboard
- Is completely reversible — every roman string maps back to exactly one Kannada string

## Symbol complexity: Classical → Ellara → Eke

There are two ways to measure the burden of a script: the number of **distinct symbols** a learner must memorise, and the size of the **permuted symbol space** that must be recognised in context.

### Actual symbols (what you must learn)

| Component | Classical | Ellara Kannada | Eke |
|-----------|-----------|----------------|-----|
| Main consonants | 35 | 21 (mahāprāṇas and rare letters merged or dropped) | — |
| Ottakṣara (conjunct) consonants | 35 | 21 | — (sequences of letters) |
| Independent vowels | 16 | 10 | — |
| Vowel diacritics (mātrās) | 16 | 10 | — |
| Modifiers | 5 (virama ್, nuktā ಼, anusvara ಂ, visarga ಃ, jihvamūlīya ೱ) | 3 (virama, nuktā, anusvara; drops ಃ and ೱ) | — |
| **Total** | **~107** | **~65** | **31 / 41 / 46** |

Classical Kannada has 16 vowels (independent form / vowel diacritic):

| IAST | Independent | Diacritic | Retained in Ellara? |
|------|-------------|-----------|---------------------|
| a | ಅ | *(inherent)* | ✓ |
| ā | ಆ | ಾ | ✓ |
| i | ಇ | ಿ | ✓ |
| ī | ಈ | ೀ | ✓ |
| u | ಉ | ು | ✓ |
| ū | ಊ | ೂ | ✓ |
| **ṛ** | **ಋ** | **ೃ** | **✗** — Sanskrit-only vocalic syllabic |
| **ṝ** | **ೠ** | **ೄ** | **✗** — Sanskrit-only, long form |
| **ḷ** | **ಌ** | **ೢ** | **✗** — Sanskrit-only vocalic syllabic |
| **ḹ** | **ೡ** | **ೣ** | **✗** — Sanskrit-only, long form |
| e | ಎ | ೆ | ✓ |
| ē | ಏ | ೇ | ✓ |
| **ai** | **ಐ** | **ೈ** | **✗** — becomes vowel+glide sequence `ay` |
| o | ಒ | ೊ | ✓ |
| ō | ಓ | ೋ | ✓ |
| **au** | **ಔ** | **ೌ** | **✗** — becomes vowel+glide sequence `av` |

Ellara Kannada drops 6 of these — the four Sanskrit vocalic-syllabic sounds (ṛ ṝ ḷ ḹ) that do not occur in native Kannada speech, and the two diphthongs ai ಐ and au ಔ which become the vowel+glide sequences `ay` and `av`. This leaves 10 vowels: a ಅ, ā ಆ, i ಇ, ī ಈ, u ಉ, ū ಊ, e ಎ, ē ಏ, o ಒ, ō ಓ.

*Nuktā (಼)* is retained in both Classical and Ellara Kannada for representing sounds from contact languages — *fa*, *za*, *odd* (English), ḵ (Arabic/Urdu). It is also needed for dialect phonemes: Havyaka's unrounded-u vowel, Toda's retroflex laterals. In Eke, two additional modifier symbols handle these: `:` (nuktā diacritic, for sounds like Toda retroflex laterals) and `^` (rounding/unrounding marker, for Havyaka's unrounded-u: `u^`). These two bring the full dialect-inclusive count to **46**.

### Permuted symbol space (what you must recognise)

The ottakṣara system multiplies consonants combinatorially — any consonant can stack with any other. Combined with vowel forms, the recognisable glyph space is:

| Script system | Formula | Space |
|---------------|---------|-------|
| Classical Kannada | 35 × 35 × 21 (consonants × conjuncts × (16 diacritics + 5 modifiers)) | ≈ **25,725** |
| Ellara Kannada | 21 × 21 × 13 (21 consonants × conjuncts × (10 diacritics + 3 modifiers)) | ≈ **5,733** (-77%) |
| Eke | no conjuncts; 31 × 1 letter-forms | **31 / 41 / 46** |

**Ellara Kannada** achieves a 77% reduction with no loss of fidelity for spoken modern Kannada. Sanskrit and Vedic texts require the full classical set.

**Eke** eliminates the combinatorial explosion entirely: by using a plain alphabet, a consonant sequence is just letters side by side — no stacked glyph, no recognisable conjunct form. The three tiers of coverage:

| Coverage | Symbols |
|----------|---------|
| Eke(ek) — everyday spoken Kannada (Ellara Kannada equivalent) | **31** |
| Formal Kannada — including historical and rare sounds (full Ellara Kannada) | **41** |
| Extended — adds English *f*, *w*, *z* | **44** |
| Dialect-inclusive — adds `:` (nuktā) and `^` (rounding) for Havyaka, Toda | **46** |

Harvard-Kyoto follows the same alphabet-over-abugida philosophy; Eke makes small modifications to better reflect Kannada phonology.

## The two-mode design

A single romanisation can't serve both archivists and lexicographers. Eke has two modes:

| Mode | For | Aspirates | ಷ |
|------|-----|-----------|---|
| **Eke** | Romanising existing text | Preserved — `bh`, `Sh`, etc. | `Sh` (distinct from `S`=ಶ) |
| **Eke(ek)** | Coining new native words | Dropped | Merged with `S` |

This lets the same notation system serve both careful transcription of DNS Bhat's books (which contain Sanskrit loanwords) and the creation of new Dravidian-root vocabulary.

## Key design choices

**Case = contrast, not emphasis.** Uppercase always signals a phonological distinction:
- `T D N L` = retroflexes (vs `t d n l` = dentals)
- `S` = palatal ಶ (vs `s` = alveolar ಸ); `Sh` = retroflex ಷ
- `A I U E O` = long vowels (vs `a i u e o` = short)
- `H` = visarga ಃ (vs `h` = ಹ)

**`h` marks aspiration because mahāprāṇa = alphaprāṇa + half-h.** A mahāprāṇa consonant is phonologically identical to its alphaprāṇa counterpart followed by a halanta-ha — visible directly in Brāhmī (𑀔 = 𑀓◌𑁆𑀳, 𑀖 = 𑀕◌𑁆𑀳), Devanāgarī (ख = क्ह, घ = ग्ह), and Kannada script (ಖ = ಕ್ಹ, ಘ = ಗ್ಹ, ಭ = ಬ್ಹ). Using `h` as the aspiration marker — `kh`, `gh`, `bh`, `dh` etc. — reflects this phonological reality directly. The one exception is `Sh` (retroflex ಷ): `S` marks the retroflex sibilant, and `h` extends it to the aspirate in the same digraph pattern.

**Anusvara as assimilation, never M.** In Kannada, anusvara ಂ before a plosive is phonologically the nasal of that plosive's place of articulation — `nk`, `ng`, `nc`, `nT`, `nt`, `mp`, `mb`. Writing `M` (as in IAST) is phonologically opaque and creates ambiguity with the labial nasal `m`.

**Diphthongs as sequences.** ಐ = ಅ + ಯ್ → `ay`; ಔ = ಅ + ವ್ → `av`. These reflect the actual phonological composition in Kannada, not the Sanskrit-influenced `ai`/`au`.

This choice is not arbitrary — Kannada has a full productive series of vowel+glide sequences with both ಯ್ and ವ್, across all vowel lengths:

| With ಯ್ | With ವ್ |
|---------|---------|
| `ay` (ಅಯ್), `Ay` (ಆಯ್) | `av` (ಅವ್), `Av` (ಆವ್) |
| `iy` (ಇಯ್), `Iy` (ಈಯ್) | `iv` (ಇವ್), `Iv` (ಈವ್) |
| `uy` (ಉಯ್), `Uy` (ಊಯ್) | `uv` (ಉವ್), `Uv` (ಊವ್) |
| `ey` (ಎಯ್), `Ey` (ಏಯ್) | `ev` (ಎವ್), `Ev` (ಏವ್) |
| `oy` (ಒಯ್), `Oy` (ಓಯ್) | `ov` (ಒವ್), `Ov` (ಓವ್) |

Sanskrit treats ಐ and ಔ as atomic vowels requiring dedicated symbols (`ai`, `au`). Eke rejects this: since `iy`, `Iy`, `uy`, `Oy` and the rest are all written as plain vowel+glide sequences, `ay` is simply the `a`-row entry in the same regular pattern. Writing `ai`/`au` would be the *only* irregularity in the vowel table — a Sanskrit import with no phonological justification in Kannada.

**`x` / `q` for vocalic syllabics.** Sanskrit has four vocalic syllabic sounds that do not occur in native Kannada: vocalic ṛ (ಋ/ೃ), its long form ṝ (ೠ/ೄ), vocalic ḷ (ಌ/ೢ), and its long form ḹ (ೡ/ೣ). None of the four appear in Dravidian roots. Eke maps them to the two ASCII letters that have no other use in Kannada phonology:

| Symbol | Eke | Notes |
|--------|-----|-------|
| ಋ / ೃ | `x` | short vocalic ṛ — common in Sanskrit loanwords: `samskxta`, `kxShNa` |
| ೠ / ೄ | `X` | long vocalic ṝ — extremely rare |
| ಌ / ೢ | `q` | short vocalic ḷ — rare; Sanskrit only |
| ೡ / ೣ | `Q` | long vocalic ḹ — extremely rare |

*Fun fact:* the `x` choice echoes history — 𑀋 (U+1000B) is the Asokan Brahmi character for vocalic ṛ, and its visual shape is strikingly close to a lowercase `x`.

---

Full specification: [Eke.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/Eke.md) (153KB, authoritative).
