---
title: Home
nav_order: 1
---

# ettuge

ettuge is a personal knowledge garden sitting at the intersection of language, computation, and reflective reading — all held together by a curiosity about how structure gives rise to meaning.

---

## ಕನ್ನಡ — Language & DNS Bhat

### [Eke — a romanisation for Kannada](kannaDa/eke/reference)

Informal Kannada writing on the internet has drifted into a loose collection of ad-hoc conventions. **Eke** (ಏಕೆ) is a principled yet lightweight romanisation scheme bridging the gap between these informal habits and the more rigorous Harvard-Kyoto protocol. It draws on D. N. Shankara Bhat's *Ellara Kannada* movement — which advocates for a written form closer to how the language is actually spoken, dropping aspirated consonants that do not exist in natural Kannada speech. Key conventions: long vowels uppercase (`A I U E O`), retroflexes uppercase (`T D N L S`), diphthongs as sequences (`ay` for ಐ, `av` for ಔ), anusvara always assimilated (never standalone `M`).

### [Dr. D. N. Shankara Bhat — digital archive](kannaDa/dnsbhat/)

Dr. D. N. Shankara Bhat (1931–) is the towering figure in modern Kannada linguistics — winner of the Pampa Award, holder of positions at Stanford, the Max Planck Institute, Oxford, and Deccan College, and the author of 33 known works spanning native Kannada grammar, script reform, historical phonology, word formation, and international typology. His central argument, developed over 50 years, is that Kannada grammar must be built from Kannada's own structure rather than borrowed Sanskrit or English frameworks.

This repository contains a systematic effort to collect, digitise, and make accessible his complete works: YouTube transcripts, blog posts recovered from dnshankarabhat.net via the Wayback Machine, full-text extractions from archive.org, and Sarvam Vision OCR runs on PDF books. Each processed book has companion files — structured Kannada text, Eke romanisation, English summary, and an AI context primer.

---

## [Functional Programming](FP/)

A running notebook for functional programming ideas, worked out mostly in Haskell but drawing on Scala, lambda calculus, and category theory wherever they illuminate the concept best. Visual programming with Kojo is folded in here too — simple generative code that reminds experienced programmers why they fell in love with the craft.

- **[ॐλ — Lambda Calculus](FP/om-lambda)** — Y combinators, fixed points, and the self-reference that turns pure substitution into recursion
- **[Monoids and Semigroups](FP/monoids-and-semigroups)** — Addition, string concatenation, set merging: the algebraic pattern that underlies composable code
- **[rangapura vihAra](FP/hsom)** — Using Euterpea (Haskell School of Music) to encode a Carnatic fusion rendition
- **[Lazy Min-K in Haskell](FP/qsortof)** — Finding the minimum k elements lazily using quickselect
- **[Reading Types in Haskell](FP/haskell-types)** — Using the GHC interpreter as a conversation partner; Kannada characters (ಅ, ಆ, …) fed to the type-checker
- **[ಕಳ್ಳ — Pumpkin Puzzle](FP/kumbaLakAyi-kaLLanalla)** — A simple iteration puzzle, solved in Haskell with Kannada script in the source
- **[Kojo — Clouds and Flowers](FP/cloud_flowers_and)** — Scala turtle graphics: clouds, flowers, random polygons, ladders

---

## Reflection & [Books](Books/Books)

- **Self-reflection** — Topic-based notes distilled from years of reading and thinking: Kannada linguistics, Indian history, machine learning, mathematics, algorithms, infrastructure, and health
- **Books** — A [curated catalog](Books/Books) of books that have genuinely changed how the author thinks, organised by author with inline summaries and individual analyses

---

*Source repository: [vwulf/ettuge](https://github.com/vwulf/ettuge)*
