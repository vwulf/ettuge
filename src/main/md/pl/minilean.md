# MiniLean: The No Magic Proof in a Kernel You Can Read

*Started Nov 26, 2026 · Vishwas*

> **Work in progress.** This page plans a MiniLean written in Lean 4 and the proof it will check. The implementation does not exist yet. Code here is *planned* DSL syntax, not code that has been compiled. The page will be updated as the implementation lands in `src/main/lean/minilean`.

<!-- section-index:begin -->
## Contents {#contents}

- [Summary](#summary)
- [1. Why a smaller Lean](#s1)
- [2. What MiniLean is](#s2)
- [3. MiniLean and Lean 4, side by side](#s3)
- [4. The No Magic stages, in MiniLean](#s4)
- [5. The sum formula, from nothing](#s5)
  - [5.1 Definitions](#s5-1)
  - [5.2 The lemmas](#s5-2)
  - [5.3 The theorem](#s5-3)
- [6. The DSL](#s6)
- [7. What comes next](#s7)
- [References](#references)

*Every heading links to itself: hover (or tap the link icon) and copy the link to share a section.*
<!-- section-index:end -->

## Summary {#summary}

[No Magic](lean-no-magic.md) followed one theorem, 1 + 2 + ⋯ + n = n(n+1)/2, down from a hand proof to Lean's kernel. Its claim was that every layer is ordinary mathematics. Its [companion](https://vwulf.github.io/ettuge/FP/no-magic-literate/) let Lean show each layer. But the last layer, the kernel, was still Lean's own: a large C++ program you are asked to trust, or to replace with one of five independent checkers you are also asked to trust.

This page takes the next step. It plans a **MiniLean**: a type checker for a small dependent type theory, written in Lean 4, following Hideaki Takahashi's book [MiniLean4](https://learn.h5i.dev/). The book builds such a kernel in Rust in under three thousand lines, with no dependencies. MiniLean will be small enough to read in an afternoon, and it will check the *same* theorem, defined and proved from nothing.

The comparison is the point. Section 3 lists, row by row, what Lean 4 has and MiniLean leaves out. Every row MiniLean leaves out is something that makes Lean pleasant to use. None of them is needed to check the proof.

[↑ Contents](#contents)

## 1. Why a smaller Lean {#s1}

"Trust the kernel" is only reassuring if the kernel is something you could, in principle, read. Lean's is small *for what it does*. It handles mutual and nested inductive types, quotients, efficient arithmetic on number literals, and a decade of engineering for speed. It is still not something most readers will audit.

MiniLean is built to be read. It keeps only what a proof checker needs, and it implements each piece in the simplest way that works. Speed doesn't matter here. It answers a concrete question: **what is the least machinery that can still check 2 · S(n) = n(n+1)?**

Writing it in Lean 4 rather than Rust has two benefits for this series:

- The same Lean project can hold the kernel, the proof it checks, and the tests, and `lake build` runs all three.
- Lean 4 can *also* check the sum formula. So each step can be shown twice, once by Lean and once by MiniLean, with the same expected answer.

[↑ Contents](#contents)

## 2. What MiniLean is {#s2}

MiniLean follows the structure of the MiniLean4 book. Each part below is one module of the planned implementation.

1. **Terms** (book chapters 2 and 11). Six kinds of expression: sorts `Sort u`, bound variables as de Bruijn indices, constants, application, λ-abstraction, and Π-types. Substitution is defined once, on de Bruijn indices, so variable capture cannot happen.
2. **Universes** (chapter 13). Levels built from `0`, successor, `max` and `imax`, so `Prop = Sort 0` and `Type = Sort 1`. The hierarchy is what blocks Hurkens' paradox (book Appendix C).
3. **Reduction** (chapter 12). Weak head normal form with three rules: β (apply a function), δ (unfold a definition) and ι (run a recursor on a constructor). Two terms are *definitionally equal* when their normal forms match.
4. **Type checking** (chapters 3 and 5). Two mutually recursive functions, `infer` and `check`, one case per typing rule. Their answer is the only verdict that counts.
5. **Inductive types** (chapters 7–9). An inductive declaration lists its constructors. MiniLean *generates* the recursor and its ι-rule from that list, by the fixed recipe in chapter 8. `Nat` and `Eq` are just two such declarations.
6. **Tactics** (chapter 10). `intro`, `apply`, `exact`, `induction` and `rw`. Each is a small program that fills a hole in a partial proof term. Tactics are outside the trusted part: the kernel checks the term they build.
7. **The environment**. An ordered list of declarations. Each is checked by the kernel before it is added, and nothing else can add one.

There is deliberately no parser, elaborator, unifier, type-class search, pattern-match compiler or axiom. Section 6 explains how terms are written without them.

[↑ Contents](#contents)

## 3. MiniLean and Lean 4, side by side {#s3}

The planned MiniLean against Lean 4.36, the version the No Magic project builds with. "Kernel" marks what the trusted checker itself must handle. "Front end" marks conveniences that run *before* the kernel and produce plain terms for it.

| Feature | Lean 4 | MiniLean (planned) | Where it lives |
| --- | --- | --- | --- |
| Term formers | sort, bound/free/meta variables, constant, application, λ, Π, `let`, literals, projection, metadata | sort, bound variable, constant, application, λ, Π | kernel |
| Variable representation | de Bruijn indices plus locally nameless free variables | de Bruijn indices only | kernel |
| Universes | `Sort u` with `succ`, `max`, `imax`, universe polymorphism | same levels; definitions take explicit level arguments | kernel |
| β, δ, ι reduction | yes | yes | kernel |
| ζ reduction (`let`) | yes | no `let` at all | kernel |
| η for functions | yes | no | kernel |
| η for structures | yes | no structures | kernel |
| Definitional proof irrelevance | yes | no; equal proofs are not identified | kernel |
| Number literals | built-in, with GMP arithmetic | none: `2` is `succ (succ zero)` | kernel |
| Inductive types | mutual, nested, indexed families | single inductive types, with parameters and indices (enough for `Nat` and `Eq`) | kernel |
| Recursors | generated | generated by the book's recipe | kernel |
| Quotients | `Quot` built in | none | kernel |
| Axioms | `propext`, `Quot.sound`, `Classical.choice` | none | kernel |
| Structural recursion and `match` | compiled to recursors (`Nat.brecOn`, `Nat.below`) | none: recursors are written directly | front end |
| Notation (`*`, `+`, `=`, numerals) | user-extensible syntax | none: plain applications | front end |
| Implicit arguments and unification | yes | none: every argument explicit | front end |
| Type classes and instances | yes | none | front end |
| Tactics | hundreds, user-extensible | `intro`, `apply`, `exact`, `induction`, `rw` | front end |
| Surface language | Lean's parser and elaborator | a Lean 4 DSL (section 6) | front end |
| Implementation | C++ kernel, Lean front end | Lean 4, one Lake project | both |
| Independent checkers | five, run by `lake check --paranoid` | none; MiniLean is itself a second checker for this one proof | both |
| Consistency | modelled in ZFC plus inaccessible cardinals (Carneiro) | consistency of the book's core system: book Appendix D | both |

Two things follow from this table.

**Everything in the "front end" rows is a convenience.** The No Magic companion showed Lean's front end turning `2 * sumTo n` into `HMul.hMul …` and a `match` into `Nat.brecOn`. MiniLean has no front end, so its terms are already in the form those stages produce. The proof is longer to write and identical in substance.

**MiniLean's proof uses no axioms.** Lean's proof reported one axiom, `propext`, which came in through the core library's proofs of `Nat.add_mul` and `Nat.mul_div_cancel_left`. MiniLean has no axioms to use. Every lemma below is proved by induction from the recursors, so the axiom list is provably empty.

[↑ Contents](#contents)

## 4. The No Magic stages, in MiniLean {#s4}

The companion walked through nine stages. Here is what each becomes when the checker is MiniLean.

| Stage (No Magic, compiled) | In MiniLean |
| --- | --- |
| 1. Surface syntax | DSL terms; no notation, so this stage and stage 2 coincide |
| 2. Notation removed | nothing to remove: `mul two (sumTo n)` is already plain |
| 3. Tactics become terms | the same, on a smaller scale: five tactics, each a term builder you can read |
| 4. Recursion becomes a recursor | skipped: `add`, `mul` and `sumTo` are written with `Nat.rec` from the start |
| 5. The primitives | the same idea, now visible as code: the recursor generator *is* the recipe |
| 6. Curry–Howard | the same: `∀` is Π, and the theorem is a function from `n` to a proof |
| 7. Computation | β, δ and ι only; each `refl` that checks is a run of `whnf` |
| 8. The kernel alone | this is all of MiniLean: `check env decl` accepts the proof and rejects `2 · S(3) = 13` |
| 9. Checking the checker | MiniLean becomes one more checker, and a second implementation to compare against Lean |

So the MiniLean companion will be shorter in some places and deeper in others. Stages 2 and 4 vanish. Stages 5, 7 and 8 stop being outputs to look at and become functions to read.

[↑ Contents](#contents)

## 5. The sum formula, from nothing {#s5}

MiniLean starts with an empty environment. Everything the proof needs is declared and checked in order.

### 5.1 Definitions {#s5-1}

Two inductive types:

```text
Nat : Type
  zero : Nat
  succ : Nat → Nat

Eq {α : Sort u} (a : α) : α → Prop
  refl : Eq a a
```

From these, MiniLean generates `Nat.rec` (induction and primitive recursion) and `Eq.rec` (transport, "replace equals by equals"). Everything else is a *definition*: a term the kernel type-checks once and can then unfold (δ).

```text
add m n   := Nat.rec m                (λ _ ih, succ ih)       n    -- m + succ n = succ (m + n)
mul m n   := Nat.rec zero             (λ _ ih, add ih m)      n    -- m · succ n = m · n + m
sumTo n   := Nat.rec zero             (λ k ih, add ih (succ k)) n  -- S(k+1) = S(k) + (k+1)
two       := succ (succ zero)
```

`add` and `mul` recurse on their second argument, as Lean's do. The familiar equations then hold *by computation*: `add m zero` reduces to `m`, and `mul m (succ n)` reduces to `add (mul m n) m`.

Three small facts about equality, each a few lines using `Eq.rec`:

```text
symm   : a = b → b = a
trans  : a = b → b = c → a = c
congr  : (f : α → β) → a = b → f a = f b
```

### 5.2 The lemmas {#s5-2}

Lean's library supplied `Nat.mul_add`, `Nat.add_mul` and `Nat.mul_comm`. In MiniLean we prove them, along with the addition facts they rest on. Each is one induction.

| Lemma | Statement | Induction on | Uses |
| --- | --- | --- | --- |
| `zero_add` | 0 + n = n | n | — |
| `succ_add` | succ m + n = succ (m + n) | n | — |
| `add_comm` | m + n = n + m | n | `zero_add`, `succ_add` |
| `add_assoc` | (a + b) + c = a + (b + c) | c | — |
| `mul_add` | a · (b + c) = a · b + a · c | c | `add_assoc` |
| `zero_mul` | 0 · n = 0 | n | `zero_add` |
| `succ_mul` | succ m · n = m · n + n | n | `add_assoc`, `add_comm` |
| `mul_comm` | m · n = n · m | n | `zero_mul`, `succ_mul` |
| `add_mul` | (a + b) · c = a · c + b · c | — | `mul_comm`, `mul_add` |

The last one needs no induction of its own: (a + b) · c = c · (a + b) = c · a + c · b = a · c + b · c.

### 5.3 The theorem {#s5-3}

```text
two_mul_sumTo : ∀ n, mul two (sumTo n) = mul n (succ n)
```

The proof is the hand proof again, by `Nat.rec`:

- **Base case, n = 0.** Both sides reduce to `zero`: `mul two zero` by ι, and `mul zero (succ zero)` reduces to `add zero zero` and then to `zero`. The proof is `refl`, accepted by conversion.
- **Step.** Assume `ih : mul two (sumTo k) = mul k (succ k)`. Then:

```text
mul two (sumTo (succ k))
  ≡ mul two (add (sumTo k) (succ k))            δ, ι: definition of sumTo
  = add (mul two (sumTo k)) (mul two (succ k))  mul_add
  = add (mul k (succ k)) (mul two (succ k))     ih, by congr
  = mul (add k two) (succ k)                    add_mul, read backwards
  ≡ mul (succ (succ k)) (succ k)                δ, ι: add k two reduces to succ (succ k)
  = mul (succ k) (succ (succ k))                mul_comm
```

The last line is the claim for `succ k`. Lines marked ≡ cost nothing: the kernel checks them by computing. Lines marked = are lemma applications chained with `trans`.

This is the same chain as No Magic section 1, line for line. The only differences are that `2` is spelled out, and that every lemma on the right was proved a few lines earlier rather than taken from a library.

[↑ Contents](#contents)

## 6. The DSL {#s6}

MiniLean has no parser of its own. Its terms are values of a Lean 4 data type, written with a small embedded language: a few Lean macros that turn readable syntax into MiniLean `Expr` values. Lean's parser handles the syntax. MiniLean sees only the resulting terms, so its trusted part stays the same size.

A planned sketch (not yet implemented, details will change):

```lean
mini_inductive Nat : Type where
  | zero : Nat
  | succ : Nat → Nat

mini_def add : Nat → Nat → Nat :=
  λ m n => Nat.rec (motive := λ _ => Nat) m (λ _ ih => succ ih) n

mini_theorem two_mul_sumTo : ∀ n : Nat, Eq (mul two (sumTo n)) (mul n (succ n)) := by
  induction n
  · refl
  · intro k ih
    -- unfold sumTo and the right-hand side by computation, so rw can match
    show Eq (mul two (add (sumTo k) (succ k))) (mul (succ k) (succ (succ k)))
    rw [mul_add, ih, ← add_mul, mul_comm]
```

Each `mini_…` command builds a MiniLean declaration, runs MiniLean's own `check` on it, and fails the Lean build if MiniLean rejects it. Lean 4 acts only as the editor and the build tool. The verdict is MiniLean's.

Choosing a DSL over a port of the book's script language (book Appendix E) keeps the project small. It also gives good error locations for free: a MiniLean rejection is reported on the line of the declaration that failed.

[↑ Contents](#contents)

## 7. What comes next {#s7}

1. **The implementation:** `src/main/lean/minilean/`, one module per part in section 2, and a `Prelude` with the definitions, lemmas and theorem from section 5. The build will pin the verdicts: MiniLean accepts `two_mul_sumTo`, rejects `2 · S(3) = 13`, and accepts `2 · S(3) = 12`, mirroring stage 8 of the companion.
2. **A second companion, "No Magic, implemented".** The first companion showed Lean's *output* at each stage. This one will show MiniLean's *code* for each stage: the substitution function behind β, the recursor generator behind induction, the five tactics as term builders, and `infer`/`check` as the kernel. Each will come with a trace of what it does to the sum formula. It will be published as literate Lean pages, like the first.
3. **Later, perhaps:** translate Lean's own proof term into MiniLean and check it there. That would mean handling numerals, instances and `Nat.brecOn`, so it is a project of its own.

[↑ Contents](#contents)

## References {#references}

- Hideaki Takahashi, [MiniLean4](https://learn.h5i.dev/): a kernel for a small dependent type theory, built up chapter by chapter in Rust, with tactics and the leanmini script language
- [No Magic: Proving 1 + 2 + … + n = n(n+1)/2 from Paper to Lean's Kernel](lean-no-magic.md)
- [No Magic, compiled](https://vwulf.github.io/ettuge/FP/no-magic-literate/): the companion, one stage per page, as literate Lean
- [Lean and AI Formalization](lean-ai-formalization.md), §1 (Lean's type theory) and §11 (kernel trust)
- [Calculus of constructions](https://en.wikipedia.org/wiki/Calculus_of_constructions), Wikipedia
