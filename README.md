# ettuge

[ettuge](https://github.com/vwulf/ettuge/) is a personal knowledge garden sitting at the intersection of language, computation, and creativity. It collects explorations in Kannada linguistics, functional programming, visual art, and reflective reading — all held together by a curiosity about how structure gives rise to meaning.

All readable documents live under [`src/main/md`](https://github.com/vwulf/ettuge/blob/master/src/main/md). What follows is a guided tour through the most interesting stops.

---

## Language & Script

### [Eke — a romanization proposal for Kannada](https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/Eke.md)

Informal Kannada writing on the internet has drifted into a loose collection of ad-hoc conventions. *Eke* (ಏಕೆ) is a principled yet lightweight romanization scheme that bridges the gap between these informal habits and the more rigorous Harvard-Kyoto protocol. It is inspired by D. N. Shankara Bhat's *Ellara Kannada* movement, which advocates for a written form closer to how the language is actually spoken — dropping aspirated consonants that do not exist in natural speech and favoring native Dravidian roots over Sanskrit borrowings. Whether you type Kannada on a phone or a terminal, Eke offers a consistent, typable representation that stays faithful to the spoken word.

---

## Functional Programming

This repository doubles as a running notebook for functional programming ideas, worked out mostly in Haskell but drawing on Scala, lambda calculus, and category theory wherever they illuminate the concept best.

### [Forays into FP](https://github.com/vwulf/ettuge/blob/master/src/main/md/pl/FP.md)

Every programmer who has spent time in imperative languages and then stumbled into functional programming knows the disorientation: the vocabulary is familiar but the grammar is completely different. This piece traces one such journey — from C++ templates and Python comprehensions, through Scala at a startup, to the slowly-dawning realization that functional programming requires rethinking what "programming" means at all. It is a good place to start if you want context for the more technical pieces that follow.

### [Reading types in Haskell](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/reflection.md)

Types are Haskell's primary language for stating intentions. This is a hands-on session transcript that walks through how to *read* types interactively — using the GHC interpreter as a conversation partner — rather than just accepting what the compiler infers. Even Kannada characters (ಅ, ಆ, …) are fed to the type-checker, turning the exercise into a small celebration of Unicode and the universality of Haskell's type system.

### [Morphisms, diamonds and kannaDa](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/%E0%B2%95%E0%B2%B3%E0%B3%8D%E0%B2%B3.md)

A puzzle from a recreational mathematics book becomes the staging ground for an excursion into morphisms — the structure-preserving maps that category theory places at the centre of everything. The code is in Haskell; the puzzle is stated in the style of Scheherazade; and the Kannada title hints that the thief in the story is none other than the diamond itself. Language, mathematics, and storytelling braid together here more tightly than you might expect.

### [Monoids are everywhere](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/monoids-and-semigroups.md)

Addition of integers. Concatenation of strings. Merging of sets. These all look different on the surface, but each is an instance of the same algebraic pattern: a semigroup (an associative operation) and, if a neutral element exists, a monoid. This piece makes the case — with concrete numeric examples — that these abstractions are not academic overhead but practical design tools that let you write generic, composable code. Once you see monoids everywhere, you cannot unsee them.

### [A lazy take on (un)fold](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/qsortof.md)

Finding the *k* smallest elements of a list sounds like a job for sorting — but sorting does more work than necessary. This exploration starts with a one-liner in *Real World Haskell*, digs into the difference between `foldl`, `foldl'`, and `foldr`, and ends up with a lazy quicksort whose elegance lies in doing exactly as much work as the caller demands and no more. A good illustration of why laziness is not just a performance trick but a different way of thinking about computation.

### [rangapura vihAra](https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/hsom.md)

What happens when you use a functional programming DSL to compose music? This piece follows the Euterpea library (*Haskell School of Music*) from "Twinkle Twinkle Little Star" to an attempt at encoding a Carnatic fusion rendition of *Rangapura Vihara* — a bhairavi raga piece that straddles classical and contemporary sensibilities. Music theory and Haskell type theory turn out to share a surprising amount of vocabulary.

### [ॐλ](https://github.com/vwulf/ettuge/blob/master/src/main/md/pl/%E0%A5%90%CE%BB.md)

Lambda calculus is the bedrock beneath every functional language — a system so minimal (just abstraction and application) that it can express anything computable. This piece keeps returning to that bedrock: Y combinators, reduction strategies (WHNF, HNF, NF), the difference between eager and lazy evaluation, and the fixed points that turn self-referential expressions into recursion. The title pairs the Sanskrit *ॐ* (the primordial sound, implying wholeness) with *λ* (the symbol of abstraction), suggesting that in the lambda calculus, as in non-dual philosophy, all distinctions ultimately reduce to one.

---

## Visual Creativity

### [Kojo](https://github.com/vwulf/ettuge/blob/master/src/main/md/kojo/cloud_flowers_and.md)

Kojo is a Scala-based learning environment that descends from Logo — the turtle-graphics language that introduced a generation of children to programming through drawing. This section collects generated images: clouds and flowers, random polygons, ladder patterns, and a worm. The code is simple enough for a beginner and playful enough to remind experienced programmers why they fell in love with the craft. Kojo also serves as a gentle on-ramp to Scala's functional idioms in a visual context.

---

## Reflection

### [Self reflection](https://github.com/vwulf/ettuge/blob/master/src/main/md/self-reflection/index.md)

A large, sprawling personal notes file — links, snippets, ideas, and observations accumulated from 2021 to 2024 — has been distilled into topic-based files here. Subjects range across Kannada linguistics and Indian history, functional programming and machine learning, mathematics and algorithms, infrastructure and health. Think of it as a public externalisation of a working mind: not polished essays, but the connective tissue between reading, thinking, and building.

### [Books](https://github.com/vwulf/ettuge/blob/master/src/main/md/Books/Books.md)

A curated catalog of books that have genuinely changed how the author thinks — organized by author with inline summaries and links to individual files containing deeper analysis and personal takeaways. The list spans Western fiction (Camus, Hemingway, Fitzgerald), Kannada and Indian literature, classical Indian texts, D. N. Shankara Bhat's linguistics works, science, history, mathematics, and martial arts. It is as much a record of an intellectual biography as it is a reading list.

---

## Deep Dive

For a full map of the repository — its directory structure, active development threads, tooling, and the DNS Bhat methodology that underpins the Kannada translation work — see the [project guide](https://github.com/vwulf/ettuge/blob/master/CLAUDE.md).