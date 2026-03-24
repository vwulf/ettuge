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

## DNS Bhat's influence: *Ellara Kannada*

Dr. D.N. Shankara Bhat's *Ellara Kannada* reform argues that modern written Kannada should reflect how the language is actually spoken, not how Sanskrit grammar was once overlaid on it. Native Kannada has no *mahaprāṇa* (aspirated consonants) — `bh`, `dh`, `kh` etc. are borrowings from Sanskrit that do not appear in Dravidian root words. Eke(ek) — the coining mode — follows this: new native words avoid aspirates.

## *Hosabaraha* orthography

Hosabaraha (Vishwas's Kannada input system) uses a consistent phone-key mapping for Kannada characters. Eke extends this mapping into a romanisation that:
- Works with plain ASCII on any keyboard
- Is completely reversible — every roman string maps back to exactly one Kannada string
- Sorts correctly: uppercase before lowercase reflects the linguistic hierarchy (long before short, retroflex before dental)

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

**Anusvara as assimilation, never M.** In Kannada, anusvara ಂ before a plosive is phonologically the nasal of that plosive's place of articulation — `nk`, `ng`, `nc`, `nT`, `nt`, `mp`, `mb`. Writing `M` (as in IAST) is phonologically opaque and creates ambiguity with the labial nasal `m`.

**Diphthongs as sequences.** ಐ = ಅ + ಯ್ → `ay`; ಔ = ಅ + ವ್ → `av`. These reflect the actual phonological composition in Kannada, not the Sanskrit-influenced `ai`/`au`.

**`x` for vocalic ṛ.** Sanskrit-derived words have ಋ/ೃ (vocalic r, not a vowel+consonant sequence). `x` is a single ASCII character with no other use in Kannada phonology — unambiguous and typable.

---

Full specification: [Eke.md](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/Eke.md) (153KB, authoritative).
