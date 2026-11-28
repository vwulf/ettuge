# MiniLean: The No Magic Proof in a Kernel You Can Read

*Started Nov 26, 2026 · last updated Nov 26, 2026 · Vishwas*

> **Work in progress.** MiniLean now exists: [`src/main/lean/minilean`](https://github.com/vwulf/ettuge/tree/master/src/main/lean/minilean), about 1,400 lines of Lean 4. It builds with Lean 4.36.0, and the build checks every proof on this page with MiniLean's own kernel. Its companion, [No Magic, implemented](https://vwulf.github.io/ettuge/FP/minilean-literate/), walks the sum formula through MiniLean stage by stage, with the kernel's source alongside. [How a Theorem Prover Is Written](minilean-step-by-step.md) goes one level deeper: it follows one proof through MiniLean's code, function by function.

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
- [7. What the kernel refuses](#s7)
- [8. The companion, and what comes next](#s8)
- [References](#references)

*Every heading links to itself: hover (or tap the link icon) and copy the link to share a section.*
<!-- section-index:end -->

## Summary {#summary}

[No Magic](lean-no-magic.md) followed one theorem, 1 + 2 + ⋯ + n = n(n+1)/2, down from a hand proof to Lean's kernel. Its claim was that every layer is ordinary mathematics. Its [companion](https://vwulf.github.io/ettuge/FP/no-magic-literate/) let Lean show each layer. But the last layer, the kernel, was still Lean's own: a large C++ program you are asked to trust, or to replace with one of five independent checkers you are also asked to trust.

This page takes the next step. It builds a **MiniLean**: a type checker for a small dependent type theory, written in Lean 4, following Hideaki Takahashi's book [MiniLean4](https://learn.h5i.dev/). The book builds such a kernel in Rust in under three thousand lines, with no dependencies. MiniLean's trusted kernel is about 745 lines of Lean, small enough to read in an afternoon. It checks the *same* theorem, defined and proved from nothing.

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

MiniLean follows the structure of the MiniLean4 book. Each part below is one module of the implementation, with its size. The first four are the trusted kernel (about 745 lines). The rest is front end, which the kernel does not trust (about 650 lines).

1. **Universes** (book chapter 13; `Level.lean`, 110 lines). Levels built from `0`, successor, `max`, `imax` and parameters, so `Prop = Sort 0` and `Type = Sort 1`. The hierarchy is what blocks Hurkens' paradox (book Appendix C). Two levels are equal when they have the same value for every value of their parameters; trying values up to a bound set by the levels' constants decides it.
2. **Terms** (chapters 2 and 11; `Expr.lean`, 180 lines). Sorts, bound variables as de Bruijn indices, constants, application, λ and Π. To go under a binder, the checker replaces its bound variable with a fresh *free* variable, so every term it works on has no dangling indices and substitution never needs to shift them. (This "locally nameless" style is what Lean's kernel does too.)
3. **The environment** (`Env.lean`, 62 lines). An ordered list of definitions, theorems, inductive types, constructors and recursors. Nothing joins it except through the kernel's checks.
4. **The kernel** (chapters 3, 5, 7–9 and 12; `Kernel.lean`, 393 lines).
    - `whnf` reduces by β (apply a function), δ (unfold a definition) and ι (run a recursor on a constructor). `isDefEq` reduces both sides and compares.
    - `infer` computes a term's type, one case per typing rule.
    - `addInductive` checks an inductive declaration and *generates* its recursor and ι-rule by the book's fixed recipe. `Nat` and `Eq` are just two such declarations.
5. **Names** (`Surface.lean`, 68 lines). Resolves each name to a bound variable, a local or a constant.
6. **Tactics** (chapter 10; `Tactic.lean`, 240 lines). `intro`, `exact`, `refl`, `show`, `induction` and `rw`. Each turns a goal into new goals plus a way to build the old goal's proof from theirs. Tactics are outside the trusted part: the kernel checks the term they build.
7. **The DSL** (`DSL.lean`, 338 lines). Lean 4 commands that feed all of the above (section 6).

There is deliberately no elaborator, unifier, type-class search, pattern-match compiler or axiom. Section 6 explains how terms are written without them.

[↑ Contents](#contents)

## 3. MiniLean and Lean 4, side by side {#s3}

MiniLean against Lean 4.36, the version the No Magic project builds with. "Kernel" marks what the trusted checker itself must handle. "Front end" marks conveniences that run *before* the kernel and produce plain terms for it.

| Feature | Lean 4 | MiniLean | Where it lives |
| --- | --- | --- | --- |
| Term formers | sort, bound/free/meta variables, constant, application, λ, Π, `let`, literals, projection, metadata | sort, bound variable, free variable, constant, application, λ, Π | kernel |
| Variable representation | de Bruijn indices plus locally nameless free variables | the same: de Bruijn indices, plus free variables while checking | kernel |
| Universes | `Sort u` with `succ`, `max`, `imax`, universe polymorphism | the same levels; universe arguments are always written out | kernel |
| β, δ, ι reduction | yes | yes | kernel |
| ζ reduction (`let`) | yes | no `let` at all | kernel |
| η for functions | yes | no | kernel |
| η for structures | yes | no structures | kernel |
| Definitional proof irrelevance | yes | no; equal proofs are not identified | kernel |
| Number literals | built-in, with GMP arithmetic | none: `2` is `succ (succ zero)` | kernel |
| Inductive types | mutual, nested, indexed families | single inductive types, with parameters and indices; a recursive field must be exactly `I params idx` | kernel |
| Recursors | generated | generated by the book's recipe | kernel |
| Quotients | `Quot` built in | none | kernel |
| Axioms | `propext`, `Quot.sound`, `Classical.choice` | none | kernel |
| Structural recursion and `match` | compiled to recursors (`Nat.brecOn`, `Nat.below`) | none: recursors are written directly | front end |
| Notation (`*`, `+`, `=`, numerals) | user-extensible syntax | none: plain applications | front end |
| Implicit arguments and unification | yes | none: every argument explicit | front end |
| Type classes and instances | yes | none | front end |
| Tactics | hundreds, user-extensible | `intro`, `exact`, `refl`, `show`, `induction`, `rw` | front end |
| Surface language | Lean's parser and elaborator | a Lean 4 DSL (section 6) | front end |
| Implementation | C++ kernel, Lean front end | Lean 4, one Lake project: a 745-line kernel and a 650-line front end | both |
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
| 3. Tactics become terms | the same, on a smaller scale: six tactics, each a term builder you can read |
| 4. Recursion becomes a recursor | skipped: `add`, `mul` and `sumTo` are written with `Nat.rec` from the start |
| 5. The primitives | the same idea, now visible as code: the recursor generator *is* the recipe |
| 6. Curry–Howard | the same: `∀` is Π, and the theorem is a function from `n` to a proof |
| 7. Computation | β, δ and ι only; each `refl` that checks is a run of `whnf` |
| 8. The kernel alone | this is all of MiniLean: `check env decl` accepts the proof and rejects `2 · S(3) = 13` |
| 9. Checking the checker | MiniLean becomes one more checker, and a second implementation to compare against Lean |

So the MiniLean companion will be shorter in some places and deeper in others. Stages 2 and 4 vanish. Stages 5, 7 and 8 stop being outputs to look at and become functions to read.

[↑ Contents](#contents)

## 5. The sum formula, from nothing {#s5}

MiniLean starts with an empty environment. Everything the proof needs is declared and checked in order, in one file: [`MiniLean/Prelude.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Prelude.lean). Every snippet below is taken from it, and every output shown is pinned with `#guard_msgs`.

### 5.1 Definitions {#s5-1}

Two inductive types:

```lean
mini_inductive Nat : Type where
  | zero : Nat
  | succ : Nat → Nat

mini_inductive Eq.{u} (α : Sort u) (a : α) : α → Prop where
  | refl : Eq.{u} α a a
```

From these, MiniLean's kernel generates the recursors. They come out exactly as Lean's own:

```text
recursor Nat.rec.{w} : ∀ (motive : Nat → Sort w), motive Nat.zero →
  (∀ (x : Nat), motive x → motive (Nat.succ x)) → ∀ (t : Nat), motive t

recursor Eq.rec.{w, u} : ∀ (α : Sort u), ∀ (a : α), ∀ (motive : ∀ (x : α), Eq.{u} α a x → Sort w),
  motive a (Eq.refl.{u} α a) → ∀ (x : α), ∀ (t : Eq.{u} α a x), motive x t
```

Everything else is a *definition*: a term the kernel type-checks once and can then unfold (δ). With no implicit arguments, universe levels are written out (`Nat.rec.{1}` recurses into `Type`):

```lean
mini_def NatEq (a b : Nat) : Prop := Eq.{1} Nat a b

mini_def add (m n : Nat) : Nat :=
  Nat.rec.{1} (λ (k : Nat) => Nat) m (λ (k ih : Nat) => succ ih) n

mini_def mul (m n : Nat) : Nat :=
  Nat.rec.{1} (λ (k : Nat) => Nat) zero (λ (k ih : Nat) => add ih m) n

mini_def sumTo (n : Nat) : Nat :=
  Nat.rec.{1} (λ (k : Nat) => Nat) zero (λ (k ih : Nat) => add ih (succ k)) n

mini_def two : Nat := succ (succ zero)
```

`add` and `mul` recurse on their second argument, as Lean's do, so `add m zero` reduces to `m` and `mul m (succ n)` to `add (mul m n) m`. MiniLean computes with them: `#mini_reduce mul two (sumTo three)` prints `Nat.succ^12 Nat.zero`. (The printer abbreviates long `succ` chains; the term itself is twelve nested `succ`s.)

### 5.2 The lemmas {#s5-2}

Lean's library supplied `Nat.mul_add`, `Nat.add_mul` and `Nat.mul_comm`. In MiniLean each is proved by induction, with the addition facts it rests on:

| Lemma | Statement | Induction on | Uses |
| --- | --- | --- | --- |
| `zero_add` | 0 + n = n | n | — |
| `succ_add` | succ m + n = succ (m + n) | n | — |
| `add_comm` | m + n = n + m | n | `zero_add`, `succ_add` |
| `add_assoc` | (a + b) + c = a + (b + c) | c | — |
| `mul_add` | a · (b + c) = a · b + a · c | c | `add_assoc` |
| `zero_mul` | 0 · n = 0 | n | — |
| `succ_mul` | succ m · n = m · n + n | n | `add_assoc`, `add_comm` |
| `mul_comm` | m · n = n · m | n | `zero_mul`, `succ_mul` |
| `add_mul` | (a + b) · c = a · c + b · c | — | `mul_comm`, `mul_add` |

A typical one:

```lean
mini_theorem mul_add (a b c : Nat) : NatEq (mul a (add b c)) (add (mul a b) (mul a c)) := by
  induction c
  · refl
  · intro k ih
    show NatEq (add (mul a (add b k)) a) (add (mul a b) (add (mul a k) a))
    rw [ih, add_assoc]
```

The base case is `refl`: both sides compute to `mul a b`. In the step, `show` restates the goal in a form the kernel accepts by computation (it checks that the new statement is definitionally equal to the old), so that `rw` can find the subterms it needs.

### 5.3 The theorem {#s5-3}

```lean
mini_theorem two_mul_sumTo (n : Nat) : NatEq (mul two (sumTo n)) (mul n (succ n)) := by
  induction n
  · refl
  · intro k ih
    show NatEq (mul two (add (sumTo k) (succ k))) (mul (succ k) (succ (succ k)))
    rw [mul_add, ih, ← add_mul, mul_comm (add k two) (succ k)]
```

It is the hand proof's chain, line for line:

```text
mul two (sumTo (succ k))
  ≡ mul two (add (sumTo k) (succ k))            show: definition of sumTo
  = add (mul two (sumTo k)) (mul two (succ k))  mul_add
  = add (mul k (succ k)) (mul two (succ k))     ih
  = mul (add k two) (succ k)                    add_mul, read backwards
  = mul (succ k) (add k two)                    mul_comm
  ≡ mul (succ k) (succ (succ k))                refl: add k two computes to succ (succ k)
```

Lines marked ≡ cost nothing: the kernel checks them by computing. Lines marked = are rewrites. `rw` closes the goal by `refl` when the two sides become definitionally equal, as Lean's does.

**What the tactics build.** Tactics are untrusted: each script builds an ordinary proof term, and the kernel checks that term. For `zero_add` the term is:

```text
λ (n : Nat) => Nat.rec.{0} (λ (n1 : Nat) => NatEq (add Nat.zero n1) n1)
  (Eq.refl.{1} Nat (add Nat.zero Nat.zero))
  (λ (k : Nat) => λ (ih : NatEq (add Nat.zero k) k) =>
    Eq.rec.{0, 1} Nat k (λ (b : Nat) => λ (h : Eq.{1} Nat k b) => NatEq (Nat.succ b) (Nat.succ k))
      (Eq.refl.{1} Nat (Nat.succ k)) (add Nat.zero k)
      (Eq.rec.{0, 1} Nat (add Nat.zero k) (λ (b : Nat) => λ (h : Eq.{1} Nat (add Nat.zero k) b) => Eq.{1} Nat b (add Nat.zero k))
        (Eq.refl.{1} Nat (add Nat.zero k)) k ih))
  n
```

`induction` became `Nat.rec`. `rw [ih]` became an `Eq.rec` (transport), wrapped around a second `Eq.rec` that flips `ih` around. Nothing else is in it: no axiom, no lemma from anywhere else.

**The kernel's verdicts** on the claims that stage 8 of the companion tested on Lean:

```text
#mini_verdict : NatEq (mul two (sumTo three)) twelve := Eq.refl.{1} Nat twelve
  MiniLean's kernel accepts it

#mini_verdict : NatEq (mul two (sumTo three)) thirteen := Eq.refl.{1} Nat thirteen
  MiniLean's kernel rejects it: type mismatch.
    term: Eq.refl.{1} Nat thirteen
    has type: Eq.{1} Nat thirteen thirteen
    expected: NatEq (mul two (sumTo three)) thirteen
```

[↑ Contents](#contents)

## 6. The DSL {#s6}

MiniLean has no parser of its own. Lean 4's parser reads a small set of commands, and [`MiniLean/DSL.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/DSL.lean) turns them into MiniLean terms:

| Command | Does |
| --- | --- |
| `mini_inductive I.{u} (params) : type where \| c : type …` | declare an inductive type; the kernel checks it and generates `I.rec` |
| `mini_def f (binders) : type := term` | declare a definition |
| `mini_theorem t (binders) : statement := term` or `:= by …` | declare a theorem, by a term or a tactic script |
| `mini_open I` | let `I.c` be written `c` |
| `#mini_check`, `#mini_reduce`, `#mini_print` | show a type, a normal form, or a declaration |
| `#mini_verdict (binders) : statement := term` | report the kernel's verdict without failing the build |

The tactics are `intro`, `exact`, `refl`, `show`, `induction` and `rw`, with `·` to focus on a goal. They do no unification. `rw` finds the first instance of an equation's left-hand side by plain one-way matching, so occasionally it has to be told which instance to use: `mul_comm (add k two) (succ k)` in the theorem above.

If MiniLean's kernel rejects a declaration, the Lean build fails at that line. Lean 4 is only the editor and the build tool. The verdict is MiniLean's.

[↑ Contents](#contents)

## 7. What the kernel refuses {#s7}

A checker that accepts everything is useless. [`MiniLean/Rejections.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Rejections.lean) holds one wrong declaration for each thing the kernel guards against. Each rejection is pinned with `#guard_msgs`, so the project builds only if every one is refused.

| Declaration | Why it must fail | MiniLean says |
| --- | --- | --- |
| `bad (n) : Eq Nat (add n zero) (succ n) := Eq.refl Nat (succ n)` | a false equation | type mismatch: `Eq Nat (succ n) (succ n)` is not `Eq Nat (add n zero) (succ n)` |
| `typeInType : Type := Type` | `Type : Type` makes the logic inconsistent (Hurkens' paradox) | type mismatch: `Type` has type `Sort 2` |
| `Bad` with `mk : (Bad → Nat) → Bad` | a non-positive type allows non-termination, and so a proof of anything | strict positivity: `Bad` may only appear as a field's whole type |
| `Big : Type` with `mk : Type → Big` | storing a `Type` inside a `Type` breaks the universe hierarchy | a field lives in a universe larger than `Big`'s |
| `Or (a b : Prop)` with two constructors | a proof of `a ∨ b` must not be used to compute data | allowed, but `Or.rec` can only eliminate into `Prop` |

[↑ Contents](#contents)

## 8. The companion, and what comes next {#s8}

1. **The companion, [No Magic, implemented](https://vwulf.github.io/ettuge/FP/minilean-literate/)**, now exists. The first companion showed Lean's *output* at each stage; this one shows MiniLean doing each stage, with `#mini_trace` printing every β, δ and ι step, and the source of every kernel module on the same site.
2. **[How a Theorem Prover Is Written](minilean-step-by-step.md)** follows one proof, `zero_add`, through MiniLean's code one function at a time, from Lean's parser to the kernel's derivation, with the real output of each step.
3. **Later, perhaps:** translate Lean's own proof term into MiniLean and check it there. That would mean handling numerals, instances and `Nat.brecOn`, so it is a project of its own.

[↑ Contents](#contents)

## References {#references}

- Hideaki Takahashi, [MiniLean4](https://learn.h5i.dev/): a kernel for a small dependent type theory, built up chapter by chapter in Rust, with tactics and the leanmini script language
- [`src/main/lean/minilean`](https://github.com/vwulf/ettuge/tree/master/src/main/lean/minilean): this MiniLean, in Lean 4
- [No Magic: Proving 1 + 2 + … + n = n(n+1)/2 from Paper to Lean's Kernel](lean-no-magic.md)
- [No Magic, compiled](https://vwulf.github.io/ettuge/FP/no-magic-literate/): the companion, one stage per page, as literate Lean
- [Lean and AI Formalization](lean-ai-formalization.md), §1 (Lean's type theory) and §11 (kernel trust)
- [Calculus of constructions](https://en.wikipedia.org/wiki/Calculus_of_constructions), Wikipedia
