# Algorithms, Functionally

Designing algorithms and data structures without mutation: laziness, persistence, and deriving programs by equational reasoning.

## Articles

- [Lazy Min-K in Haskell](qsortof.md) — the k smallest elements from a lazily unfolded quicksort, with laziness doing the pruning.
- [ಕಳ್ಳ — Pumpkin Puzzle](kumbaLakAyi-kaLLanalla.md) — a Scheherazade jeweller puzzle solved by iteration.

## Deep-dive gists

**Imperative textbooks, functional gap.** CLRS is the standard reference, but its pseudo-code assumes mutable arrays and in-place updates. Bird and Gibbons' *Algorithm Design with Haskell* covers the same strategies (divide and conquer, greedy, dynamic programming, exhaustive search) by deriving efficient programs from specifications through equational reasoning. It fills the gap the Forays essay identifies. Okasaki covers persistent *data structures*, and Bird and Gibbons cover *algorithms*.

**From recursion to recursion schemes.** Naive recursion, then tail recursion, then folds and unfolds, then recursion schemes: catamorphisms, anamorphisms and hylomorphisms (Meijer, Fokkinga and Paterson's *Bananas, Lenses, Envelopes and Barbed Wire*). Hinze, Wu and Gibbons' *Conjugate Hylomorphisms* unifies the whole zoo as hylomorphisms parametrized by an adjunction. It is still the open frontier on this site.

**Persistent structures in practice.** Scala's immutable collections rest on Bagwell's Hash Array Mapped Tries and Relaxed Radix Balanced trees, which give near-constant-time persistent maps and vectors with cheap concatenation. One gap surfaced in the Lean survey: amortized purely functional structures in Okasaki's style are still unformalized in Lean, because amortization arguments are hard to state in a proof assistant.

Sources: [Technical › Functional Programming](../Books/Technical#functional-programming), [Technical › Algorithms and Data Structures](../Books/Technical#algorithms-and-data-structures), [Papers › Algorithms and Data Structures](../Books/Papers#algorithms-and-data-structures).
