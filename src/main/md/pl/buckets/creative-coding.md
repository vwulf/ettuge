# Creative Coding

Functional programming as an instrument: music as a literate DSL, and turtle graphics in Scala.

## Articles

- [rangapura vihAra](hsom.md) — from *Twinkle Twinkle* in Euterpea to a Carnatic kriti, via the Haskell School of Music.
- [Kojo — Clouds and Flowers](cloud_flowers_and.md) — generative drawings in Kojo, the Scala learning environment.

## Deep-dive gists

**Music as data, composition as combinators.** Hudak's *Haskell School of Music* represents sheet music as an algebraic data type, with `:+:` for sequential composition and `:=:` for parallel composition. Its later chapters connect musical structure to categorical ideas. Encoding a Carnatic kriti exposes what Western notation leaves out: gamakas, and the rāga's distinct ascending and descending scales (ārōhaṇa and avarōhaṇa). It forces a mapping layer between swaras and pitch classes.

**Learning by drawing.** Kojo uses turtle graphics in Scala to teach programming, mathematics and art together. The visual feedback loop makes recursion and composition tangible before any of the theory is named.

Sources: [Papers › Computing Education](../Books/Papers#computing-education).
