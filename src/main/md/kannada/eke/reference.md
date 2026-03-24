---
title: Eke Reference
nav_order: 1
---

# Eke — Ellara Kannada Romanisation

**Eke** (ಏಕೆ) is the romanisation system for Kannada used in the ettuge project. It adapts Harvard-Kyoto conventions for native Kannada phonology, with two operating modes:

| Mode | Use | Aspirates |
|------|-----|-----------|
| **Eke** | Romanising existing Kannada text | Preserved — `bh`, `dh`, `kh`, etc. |
| **Eke(ek)** | Coining new native (Dravidian) words | Dropped — native Kannada has no *mahaprāṇa* |

---

## Case Sensitivity

Uppercase letters mark retroflex consonants, long vowels, or special sounds:

| Symbol | Sound | Example |
|--------|-------|---------|
| `T` | retroflex ಟ (vs dental `t` = ತ) | `TamaaTe` ಟಮಾಟೆ |
| `D` | retroflex ಡ (vs dental `d` = ದ) | `Du` ಡು |
| `N` | retroflex ಣ (vs dental `n` = ನ) — **never anusvara** | `kaNNu` ಕಣ್ಣು |
| `L` | retroflex ಳ (vs dental `l` = ಲ) | `kaLLa` ಕಳ್ಳ |
| `S` | palatal sibilant ಶ/ಷ (vs alveolar `s` = ಸ) | `SabdA` ಶಬ್ದ |
| `A` | long ಆ (vs `a` = ಅ) | `mAtu` ಮಾತು |
| `I` | long ಈ (vs `i` = ಇ) | `nIru` ನೀರು |
| `U` | long ಊ (vs `u` = ಉ) | `hUvu` ಹೂವು |
| `E` | long ಏ (vs `e` = ಎ) | `Enu` ಏನು |
| `O` | long ಓ (vs `o` = ಒ) | `Odu` ಓದು |
| `H` | visarga ಃ (vs `h` = ಹ) | `namaH` ನಮಃ |
| `R` | archaic retroflex ಱ — rare | — |
| `G` | velar nasal ಙ — rare | — |
| `Y` | palatal nasal ಞ — rare | — |
| `x` | vocalic ṛ ಋ/ೃ (short) | `samskxta` ಸಂಸ್ಕೃತ |
| `X` | vocalic ṝ ೠ/ೄ (long) — extremely rare | — |

**Critical distinction:** `r` (lowercase) is always ರ. `R` (uppercase) is only archaic ಱ. Never use `R` for ರ.

---

## Vowels

| Kannada | Eke | Note |
|---------|-----|------|
| ಅ | `a` | short |
| ಆ | `A` | long |
| ಇ | `i` | short |
| ಈ | `I` | long |
| ಉ | `u` | short |
| ಊ | `U` | long |
| ಎ | `e` | short |
| ಏ | `E` | long |
| ಒ | `o` | short |
| ಓ | `O` | long |
| ಐ | `ay` | diphthong — ಅ + ಯ್; **not** `ai` |
| ಔ | `av` | diphthong — ಅ + ವ್; **not** `au` |
| ಋ / ೃ | `x` | vocalic ṛ — e.g. ಕೃಷ್ಣ → `kxSNa` |
| ಃ | `H` | visarga — uppercase |

### Diphthong note
In EK phonology, ಐ and ಔ are sequences, not single vowels:
- ಐ = ಅ + ಯ್ → `ay` (e.g. ಐದು → `aydu`)
- ಔ = ಅ + ವ್ → `av` (e.g. ಔಷಧ → `avSaDa`)

---

## Consonants

### Stops (ordered plosives)

| Place | Voiceless | Voiced | Nasal |
|-------|-----------|--------|-------|
| Velar | `k` ಕ, `kh` ಖ | `g` ಗ, `gh` ಘ | — |
| Palatal | `c` ಚ, `ch` ಛ | `j` ಜ, `jh` ಝ | — |
| Retroflex | `T` ಟ, `Th` ಠ | `D` ಡ, `Dh` ಢ | `N` ಣ |
| Dental | `t` ತ, `th` ಥ | `d` ದ, `dh` ಧ | `n` ನ |
| Labial | `p` ಪ, `ph` ಫ | `b` ಬ, `bh` ಭ | `m` ಮ |

In Eke(ek) (new word coining), aspirate digraphs drop the `h`:
`kh→k`, `gh→g`, `ch→c`, `jh→j`, `Th→T`, `Dh→D`, `th→t`, `dh→d`, `ph→p`, `bh→b`

### Sonorants and Sibilants

| Symbol | Sound |
|--------|-------|
| `y` | ಯ |
| `r` | ರ (always lowercase — the common r) |
| `l` | ಲ |
| `v` | ವ |
| `S` | ಶ / ಷ (palatal sibilant — **not** generic "sh") |
| `s` | ಸ (alveolar) |
| `h` | ಹ |
| `L` | ಳ (retroflex lateral) |

---

## Anusvara — Nasal Assimilation

The anusvara ಂ is **never** written as standalone `M`. It always assimilates to the following consonant:

| Following consonant | Prefix |
|---------------------|--------|
| ಕ `k`, ಗ `g` | `n` → `nk`, `ng` |
| ಚ `c`, ಜ `j` | `n` → `nc`, `nj` |
| ಟ `T`, ಡ `D` | `n` → `nT`, `nD` |
| ತ `t`, ದ `d` | `n` → `nt`, `nd` |
| ಪ `p`, ಬ `b` | `m` → `mp`, `mb` |
| `y`, `l`, `S`, `s`, `h`, `L` | `m` |
| `r`, `v` | `n` |

**Examples:** ಕಂಬ → `kamba`; ಕಂಠ → `kanTha`; ಸಂಸ್ಕೃತ → `samskxta`; ಬಂಧ → `bandha`

**Critical disambiguation:** `N` (uppercase) = exclusively retroflex ಣ.
- Write `linga` (ಲಿಂಗ), NOT `liNga` — that would mean ಲಿಣಗ
- Write `tunDu` (ತುಂಡು), NOT `tuNDu` — that would mean ತುಣ್ಡು

---

## Inherent Vowel and Conjuncts

- Every Kannada consonant has an inherent `a`: ಕ = `ka`, ನ = `na`, etc.
- The virama ್ suppresses it in consonant clusters: ಕ್ನ = `kna`
- Word-final consonants lose the inherent `a` in spoken EK: ಕನ್ನಡ = `kannaDa` (not `kannaDaa`)

---

## Quick Examples

| Kannada | Eke | Notes |
|---------|-----|-------|
| ಕನ್ನಡ | `kannaDa` | D = retroflex ಡ |
| ಮಾತು | `mAtu` | A = long ಆ |
| ಸೂರ್ಯ | `sUrya` | U = long ಊ, r = ರ |
| ಸಂಸ್ಕೃತ | `samskxta` | m = assimilated anusvara; x = vocalic ṛ |
| ಎಲ್ಲರ ಕನ್ನಡ | `ellara kannaDa` | (Ellara Kannada — everyone's Kannada) |
| ಭಾಷೆ | `bhASe` | bh = aspirate ಭ, S = ಶ, e = short |
| ಐದು | `aydu` | ay = diphthong ಐ |
| ಔಷಧ | `avSaDa` | av = diphthong ಔ |

---

## Two-Mode Summary

| Feature | Eke (romanising text) | Eke(ek) (coining words) |
|---------|----------------------|------------------------|
| Aspirates | Preserved: `bh`, `dh`, `kh` | Dropped: `b`, `d`, `k` |
| Retroflexes | Uppercase: T D N L S | Same |
| Long vowels | Uppercase: A I U E O | Same |
| Diphthongs | `ay`, `av` | Same |
| Anusvara | Assimilated nasal | Same |
| Vocalic ṛ | `x` | Same |

Full specification: [Eke.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/Eke.md) (153KB, authoritative).
