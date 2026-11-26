# No Magic: Proving 1 + 2 + … + n = n(n+1)/2 from Paper to Lean's Kernel

*Started Nov 22, 2026 · last updated Nov 26, 2026 · Vishwas*

> **Work in progress.** The Lean code below builds with Lean 4.36.0 (core Lean only, no Mathlib), checked Nov 26, 2026. It lives in the repo as a Lake project, [`src/main/lean/no-magic`](https://github.com/vwulf/ettuge/tree/master/src/main/lean/no-magic), whose build also checks the `#print axioms` results quoted below. Still to do: check the inaccessible-cardinals claim in [6.1](#s6-1) against Carneiro's thesis.

<!-- section-index:begin -->
## Contents {#contents}

- [Summary](#summary)
- [1. The proof by hand](#s1)
- [2. The same proof in Lean](#s2)
- [3. What the Lean program turns into](#s3)
- [4. Why a type is a statement and a term is a proof](#s4)
- [5. How the kernel checks the proof](#s5)
- [6. Who checks the checker](#s6)
  - [6.1 Sidebar: why Lean is not ZFC, and where the extra cardinals come from](#s6-1)
- [7. No magic](#s7)
- [References](#references)

*Every heading links to itself: hover (or tap the link icon) and copy the link to share a section.*
<!-- section-index:end -->

## Summary {#summary}

When Lean says "proved", it means one thing: a small, fixed program checked that a term has a certain type. Every layer under that check is ordinary mathematics, the same kind you would use on paper. This article follows one small theorem all the way down to show it.

The theorem is the one Gauss is said to have used as a schoolboy:

```text
1 + 2 + ⋯ + n = n(n+1) / 2
```

We take it through six stages:

1. Prove it by hand, by induction.
2. Write a Lean program that follows the hand proof step by step.
3. See what Lean turns that program into: a single term, built from a few primitive constructions.
4. See why a term's type is a logical statement, and why a well-typed term is a proof (Curry–Howard).
5. See how Lean's kernel checks the term, by running a type-checking algorithm.
6. Ask who checks the kernel, and find that the answer ends in set theory, which is to say in mathematics.

This matters more in 2026 than it used to. AI systems now write Lean proofs at scale. Agents produced a roughly 13-million-line formalization of Fermat's Last Theorem in September 2026, and a claimed Riemann hypothesis result arrived with a Lean proof on November 20 (see [Lean and AI Formalization](lean-ai-formalization.md)). Nobody reads 13 million lines. What makes such a proof worth anything is the type checker described below, and that checker contains nothing mysterious.

[↑ Contents](#contents)

## 1. The proof by hand {#s1}

The hand proof is two short checks: the formula holds at 0, and if it holds at k it holds at k + 1.

**Define the sum by recursion.** Writing "1 + 2 + ⋯ + n" leans on the dots. A precise definition says how to build the sum one step at a time:

```text
S(0)   = 0
S(k+1) = S(k) + (k+1)
```

**State the claim without division.** On the natural numbers, division truncates (7 / 2 = 3), so it is cleaner to prove the doubled form and divide at the end:

```text
P(n):   2 · S(n) = n(n+1)
```

**Base case, n = 0.** The left side is 2 · S(0) = 2 · 0 = 0. The right side is 0 · 1 = 0. They agree.

**Inductive step.** Assume P(k), that is, 2 · S(k) = k(k + 1). This assumption is the *induction hypothesis*. Then:

```text
2 · S(k+1) = 2 · (S(k) + (k+1))     definition of S
           = 2 · S(k) + 2(k+1)       distributivity
           = k(k+1) + 2(k+1)         induction hypothesis
           = (k+2)(k+1)              distributivity, backwards
           = (k+1)(k+2)              commutativity
```

The last line is P(k + 1), because (k + 1) + 1 = k + 2.

**Conclude.** By the principle of induction, P(n) holds for every natural number n. Since 2 · S(n) = n(n + 1), the number n(n + 1) is even, and dividing by 2 gives S(n) = n(n + 1) / 2 exactly.

**What the hand proof quietly relied on.** Five things, none of them written down:

- a definition of the natural numbers (start at 0, take successors);
- the recursive definition of S;
- the principle of induction itself;
- the laws of + and × (distributivity, commutativity);
- the meaning of "=", including that you may replace equals by equals.

On paper, a reader takes these on trust. Lean makes each one an explicit object, and that is the whole difference.

[↑ Contents](#contents)

## 2. The same proof in Lean {#s2}

The Lean version below is the hand proof line for line, using only core Lean (no Mathlib), so every lemma it cites is a few lines of library code you can read.

```lean
-- S(0) = 0,  S(k+1) = S(k) + (k+1)
def sumTo : Nat → Nat
  | 0     => 0
  | k + 1 => sumTo k + (k + 1)

-- P(n): 2 · S(n) = n(n+1)
theorem two_mul_sumTo (n : Nat) : 2 * sumTo n = n * (n + 1) := by
  induction n with
  | zero => rfl
  | succ k ih =>
    calc 2 * sumTo (k + 1)
        = 2 * (sumTo k + (k + 1))   := rfl
      _ = 2 * sumTo k + 2 * (k + 1) := Nat.mul_add 2 (sumTo k) (k + 1)
      _ = k * (k + 1) + 2 * (k + 1) := by rw [ih]
      _ = (k + 2) * (k + 1)         := (Nat.add_mul k 2 (k + 1)).symm
      _ = (k + 1) * (k + 2)         := Nat.mul_comm (k + 2) (k + 1)

-- Divide at the end: S(n) = n(n+1)/2
theorem sumTo_eq (n : Nat) : sumTo n = n * (n + 1) / 2 := by
  rw [← two_mul_sumTo n, Nat.mul_div_cancel_left (sumTo n) (by decide : 0 < 2)]

#eval sumTo 100          -- 5050
#print axioms sumTo_eq   -- 'sumTo_eq' depends on axioms: [propext]
```

Each piece maps to one move on paper:

| Hand proof | Lean |
| --- | --- |
| Define S by recursion | `def sumTo` with two pattern-matching cases |
| Claim P(n) for all n | `theorem two_mul_sumTo (n : Nat) : …` |
| "By induction on n" | `induction n with` |
| Base case: both sides are 0 | `zero => rfl` ("both sides compute to the same value") |
| Assume P(k) | `succ k ih` names the hypothesis `ih` |
| Unfold the definition of S | first `calc` step, `rfl` |
| Distributivity | `Nat.mul_add`, `Nat.add_mul` |
| Use the induction hypothesis | `rw [ih]` rewrites `2 * sumTo k` to `k * (k + 1)` |
| Commutativity | `Nat.mul_comm` |
| Divide by 2 | `Nat.mul_div_cancel_left` |

Two details are worth noticing.

**`rfl` does real work.** In the base case, `rfl` claims that `2 * sumTo 0` and `0 * (0 + 1)` are the same. Lean accepts this by *computing* both sides to `0`. The same is true of the first `calc` step, where `sumTo (k + 1)` computes to `sumTo k + (k + 1)` by the definition. Computation is part of the logic, and [section 5](#s5) explains how.

**The goal for k + 1 is `(k + 1) * (k + 1 + 1)`, and the `calc` ends in `(k + 1) * (k + 2)`.** Lean accepts the match because `k + 1 + 1` and `k + 2` compute to the same number. Again, no step is waved through; the computation is checked.

**One axiom, and where it comes from.** `#print axioms` reports exactly one axiom, `propext` (two propositions that imply each other are equal). It does not come from the induction. `sumTo`, the `rfl` base case, `Nat.mul_add` and `Nat.mul_comm` use no axioms at all. It comes in through the core library's own proofs of `Nat.add_mul` and `Nat.mul_div_cancel_left`. There is no `Classical.choice`, so the proof is constructive.

**Why not Mathlib?** With Mathlib, the last four `calc` steps collapse into `rw [Nat.mul_add, ih]; ring`. That is shorter, but `ring` hides the algebra, and here the algebra is the point.

[↑ Contents](#contents)

## 3. What the Lean program turns into {#s3}

The tactic script is not the proof. It is a program that *builds* the proof: one term in a small core language, which is then handed to the kernel. The part of Lean that does this building is called the **elaborator**.

**Notation is unfolded.** `2 * sumTo n` is shorthand. After elaboration it is a function applied to arguments, with every hidden argument filled in:

```lean
@HMul.hMul Nat Nat Nat instHMul (@OfNat.ofNat Nat 2 _) (sumTo n)
```

The elaborator finds the missing pieces (which multiplication, which `2`) by unification and type-class search. These are search procedures, and they may be clever or buggy. That is safe, because their output is checked later.

**Numbers are an inductive type.** Core Lean declares the natural numbers in two lines:

```lean
inductive Nat where
  | zero : Nat
  | succ (n : Nat) : Nat
```

From this declaration Lean generates, by a fixed recipe, a **recursor**:

```lean
Nat.rec : {motive : Nat → Sort u} →
  motive Nat.zero →                              -- a value at 0
  ((n : Nat) → motive n → motive (Nat.succ n)) →  -- a way to step n ↦ n+1
  (t : Nat) → motive t                           -- gives a value at every t
```

Read `motive` as a proposition about n, and this is exactly the principle of induction. Read it as a data type, and it is primitive recursion. Same object, two readings. Induction is not an extra axiom in Lean; it comes from what it means for `Nat` to be *generated* by `zero` and `succ`. ([MiniLean4](https://learn.h5i.dev/), chapters 7–8, builds this recipe in Rust.)

**Definitions compile down to recursors.** The kernel knows only recursors. Pattern matching and recursion are translated into them before checking ([Lean and AI Formalization §1](lean-ai-formalization.md#s1)). So `sumTo` becomes a `Nat.rec` application (via a helper, `Nat.brecOn`, itself defined with `Nat.rec`).

**Equality is an inductive type too.**

```lean
inductive Eq : α → α → Prop where
  | refl (a : α) : Eq a a
```

There is only one way to build a proof of `a = b`: `Eq.refl a`, which needs `a` and `b` to be the same. `rfl` is that constructor. "Replace equals by equals", which `rw` does, is `Eq`'s recursor. `calc` chains steps with `Eq.trans`, a two-line theorem proved from the recursor.

**The whole proof as one term.** Without tactics, the induction proof is a direct application of `Nat.rec`:

```lean
theorem two_mul_sumTo' (n : Nat) : 2 * sumTo n = n * (n + 1) :=
  Nat.rec (motive := fun m => 2 * sumTo m = m * (m + 1))
    -- base case: both sides compute to 0
    (rfl : 2 * sumTo 0 = 0 * (0 + 1))
    -- step: from ih : P k, build P (k+1)
    (fun k ih =>
      show 2 * (sumTo k + (k + 1)) = (k + 1) * (k + 2) from
        (Nat.mul_add 2 (sumTo k) (k + 1)).trans
          ((congrArg (· + 2 * (k + 1)) ih).trans
            ((Nat.add_mul k 2 (k + 1)).symm.trans
              (Nat.mul_comm (k + 2) (k + 1)))))
    n
```

Read it inside out and it is the hand proof. `Nat.rec` is induction. `rfl` is the base case. `fun k ih => …` is "assume P(k)". Each `.trans` is one `=` in the chain. `congrArg` is "apply the same operation to both sides". `#print two_mul_sumTo` shows the term the tactic version actually produced; it is longer, but it has the same shape.

**From source text to verdict.** Only the last step is trusted:

```text
  Source text        theorem two_mul_sumTo … := by induction n with …
       │
┌ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐
  UNTRUSTED · builds the term
│      ▼                                                               │
  Parser             turns characters into syntax trees
│      ▼                                                               │
  Elaborator         unfolds notation, fills implicit arguments,
│                    resolves type classes, runs tactics               │
                     (induction, rw, calc), compiles recursion
│                    to recursors                                      │
└ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘
       ▼
  Core term          Nat.rec (motive := …) rfl (fun k ih => …) n
       │
┌──────│───────────────────────────────────────────────────────────────┐
│ TRUSTED · checks the term                                            │
│      ▼                                                               │
│ Kernel             infers the term's type with a few typing rules;   │
│                    reduces both types (β, δ, ι) and compares them    │
└──────┬──────────────────────────────┬────────────────────────────────┘
       │ types match                  │ types differ
       ▼                              ▼
  Accepted: the theorem is proved    Rejected: an error; nothing is added
```

Everything in the untrusted zone can be replaced, rewritten, or written by an AI. None of it can make a false proof pass, because its only output is a term that the kernel checks.

[↑ Contents](#contents)

## 4. Why a type is a statement and a term is a proof {#s4}

In Lean, a proposition is a type, and a proof of it is any term of that type. This is the **Curry–Howard correspondence**. The type of `two_mul_sumTo` is literally the statement ∀ n, 2 · S(n) = n(n + 1), and the term from [section 3](#s3) is an inhabitant of it.

The correspondence is not a metaphor. Each logical connective *is* a type former, and the rules for using it are the rules for using that type:

| Logic | Lean type | A proof is… |
| --- | --- | --- |
| A implies B | `A → B` (function type) | a function turning proofs of A into proofs of B |
| for all x : X, P x | `(x : X) → P x` (dependent function, Π) | a function taking any x to a proof of P x |
| A and B | `And A B` (a structure) | a pair: a proof of A and a proof of B |
| A or B | `Or A B` (inductive, two constructors) | a proof of A or a proof of B, tagged with which |
| there exists x, P x | `Exists P` (inductive) | a witness x and a proof of P x |
| false | `False` (inductive, no constructors) | impossible to build: there is nothing to build it with |
| not A | `A → False` | a function that would turn any proof of A into the impossible |
| a equals b | `Eq a b` (inductive family) | `Eq.refl`, only when a and b compute to the same thing |
| induction on ℕ | `Nat.rec` | (a primitive, generated from `Nat`) |

**One construction does most of the work.** The dependent function type Π covers both ∀ and → (an implication is a ∀ whose bound variable is never used). In the original Calculus of Constructions, Π is the *only* way to form propositions, and it is enough to define all the other connectives ([Wikipedia: Calculus of constructions](https://en.wikipedia.org/wiki/Calculus_of_constructions)). Lean uses a variant with inductive types added, the Calculus of Inductive Constructions, so `And`, `Or`, `Exists` and `Eq` are ordinary inductive declarations rather than encodings.

**Where first-order logic fits.** Our theorem is a sentence of first-order arithmetic: it quantifies only over numbers. In first-order Peano arithmetic, induction has to be an *axiom schema*, one axiom for each formula. Lean's logic is higher order. `Nat.rec` quantifies over the `motive`, which is any predicate at all, so a single theorem replaces the whole schema. First-order logic is a fragment of what Lean can say, and our proof lives inside that fragment.

**Two further properties of Lean's logic matter here.**

- **It is constructive at the core.** A proof of "A or B" must say which. Classical reasoning, such as the law of excluded middle, comes from three named axioms: `propext`, `Quot.sound` and `Classical.choice` ([Lean and AI Formalization §1](lean-ai-formalization.md#s1)). `#print axioms` tells you which of them a proof used. Ours uses only `propext`, and only through two library lemmas ([section 2](#s2)).
- **Types are stratified.** `Prop` is `Sort 0`, `Type` is `Sort 1`, and so on up. The hierarchy is there for consistency. If `Type` were allowed to contain itself, you could build a term of type `False` (Hurkens' paradox; [MiniLean4](https://learn.h5i.dev/), Appendix C), and every statement would be provable.

So "is this proof valid?" becomes "does this term have this type?" That question can be answered mechanically, and [section 5](#s5) shows how.

[↑ Contents](#contents)

## 5. How the kernel checks the proof {#s5}

The kernel does not search for a proof. It is given a finished term and a claimed type, and it runs a deterministic algorithm to check that they match. If they do, the proof is valid. If not, Lean reports an error.

**The rules.** The kernel works with judgments of the form Γ ⊢ t : T, read "in context Γ, the term t has type T". A handful of rules generate all valid judgments. Three carry almost all the weight:

```text
    Γ, x : A ⊢ b : B                 Γ ⊢ f : Πx:A. B    Γ ⊢ a : A           Γ ⊢ t : A    A ≡ B
 ─────────────────────── (λ)        ───────────────────────────── (app)    ───────────────── (conv)
  Γ ⊢ (λx. b) : Πx:A. B                   Γ ⊢ f a : B[a/x]                     Γ ⊢ t : B
```

In logical terms, the first rule says that to prove ∀ x, B, you prove B for an arbitrary x. The second says that from ∀ x, B and a particular a, you get B for that a. The third, the **conversion rule**, says that a proof of A is also a proof of B whenever A and B compute to the same thing. That third rule is where `rfl` gets its power.

**Definitional equality.** The relation A ≡ B is checked by reducing both sides with a few rewriting steps until they match:

| Reduction | What it does | Example in our proof |
| --- | --- | --- |
| β (beta) | apply a function to its argument | `(fun m => 2 * sumTo m = …) 0` becomes `2 * sumTo 0 = …` |
| δ (delta) | unfold a definition by name | `sumTo` unfolds to its `Nat.rec` term |
| ι (iota) | run a recursor on a constructor | `Nat.rec z s (succ k)` becomes `s k (Nat.rec z s k)` |
| ζ (zeta) | substitute a `let` | (not used here) |
| η (eta) | `fun x => f x` equals `f` | (not used here) |

Lean's kernel adds two practical extras: number literals are computed with fast big-integer arithmetic instead of unary `succ` chains, and any two proofs of the same proposition count as equal (definitional proof irrelevance).

**Checking `two_mul_sumTo'` by hand.** Here is what the kernel does with the term from [section 3](#s3):

1. **Look up `Nat.rec`.** Its type is the induction principle. Plugging in the motive m ↦ (2 · sumTo m = m(m + 1)) fixes what the two cases must prove (rule app, plus β).
2. **Check the base case.** It needs `rfl : 2 * sumTo 0 = 0 * (0 + 1)`. `rfl` has type `x = x`. The kernel reduces `2 * sumTo 0`: δ unfolds `sumTo`, ι picks the `zero` case, and the literal arithmetic gives `0`. The right side `0 * (0 + 1)` also gives `0`. The two sides match, so the conversion rule accepts it.
3. **Check the step.** It needs a function of type (k : Nat) → P k → P (k + 1). By rule λ it checks the body with `k` and `ih` in the context. The body's stated type uses `sumTo k + (k + 1)`; the kernel confirms by δ and ι that this is what `sumTo (k + 1)` means. Each `.trans` link is then checked by rule app: the right side of one equation must be definitionally equal to the left side of the next.
4. **Check the result.** `Nat.rec … n` has type `motive n`, which β-reduces to `2 * sumTo n = n * (n + 1)`, the type the theorem claims. Accepted.

No step needs insight. Each is a lookup, a substitution, or a reduction followed by a syntactic comparison. That is why a kernel can be small. The MiniLean4 book builds one for this type theory, with its tactics and parser, in under three thousand lines of Rust with no dependencies ([MiniLean4](https://learn.h5i.dev/)). Its core idea: tactics only produce terms for the kernel to check, so a bug outside the kernel can stop a proof but should not let a false theorem through.

**One honest wrinkle.** In theory, Lean's definitional equality is not fully decidable. Proof irrelevance interacts with certain inductive types in a way that can make the check fail to terminate or behave non-transitively (Abel and Coquand). In practice this almost never arises ([Lean and AI Formalization §1](lean-ai-formalization.md#s1)). When it does, the kernel rejects or times out. It does not accept a false proof.

[↑ Contents](#contents)

## 6. Who checks the checker {#s6}

Trust in Lean narrows to two questions. Is the logic consistent? Is the kernel a correct implementation of it? Since October 2026 both have machine-checked answers, and both answers end in set theory.

**Question 1: is the logic consistent?** Consistency means no closed term has type `False`. Gödel's second incompleteness theorem says a system strong enough for arithmetic cannot prove its own consistency. So this cannot be settled inside Lean alone. It has to be settled in a stronger system. Mario Carneiro's model of Lean's type theory does this in set theory: every type becomes a set, every term an element, and `False` becomes the empty set. If set theory (ZFC plus one inaccessible cardinal per universe level; see [6.1](#s6-1)) is consistent, so is Lean. This is the same footing as ordinary paper mathematics, which also rests on set theory. For a small kernel, MiniLean4 proves the simpler version directly: its Appendix D shows that no closed term inhabits "for all P, P" ([MiniLean4](https://learn.h5i.dev/)).

**Question 2: is the kernel a correct implementation?** This is the question that failed in 2026. The logic was sound; the C++ code was not.

| Date (2026) | Event |
| --- | --- |
| Oct 15 | Lean v4.35.0 ships with verified kernels |
| Aug 21 | Lean v4.33.1 ships the fixes |
| Jul 30 – Aug 20 | OpenAI runs security-focused AI over the kernel; several more implementation bugs are found and fixed |
| Jul 28 | Kiran Gopinathan reduces the exploit to a small proof of `False` (issue #14576): nested inductive types lost phantom type parameters. A fix follows within an hour |
| Jul 25 | Ramana Kumar publishes an AI-assisted "disproof" of the Collatz conjecture that Lean accepts; he then finds Lean would accept `False` itself |

Source: [Lean and AI Formalization §11](lean-ai-formalization.md#s11). The episode shows the system working as designed. The bug was in roughly the one place a bug could matter, it was found by people using AI, and it was fixed in days.

**The answer: several independent kernels, one of them proved correct.** Lean now ships with more than one checker, so a proof is only as weak as a bug that all of them share:

| Kernel | Written in | Assurance |
| --- | --- | --- |
| con-leche | Lean | Proved consistent: every environment it accepts has a model in set theory (Carneiro's model). Implemented and proved by Claude under Joachim Breitner's supervision |
| con-ron | Rust | A translation of con-leche, proved via Aeneas to refine its algorithm |
| lean4lean | Lean | Follows the C++ kernel closely; verification expected within months |
| nanoda | Rust | Independent implementation, not verified |
| Official (`leanchecker`) | C++ | Tested; built with a hardened allocator |

Source: [Lean and AI Formalization §11](lean-ai-formalization.md#s11). `lake check --paranoid` runs them all. con-leche checks all of Mathlib in about 100 seconds on eight threads.

**Isn't Lean checking Lean circular?** Partly, and the circle is small and can be inspected. con-leche's correctness proof is a Lean proof, so it was itself checked by a kernel. What that proof shows is a mathematical statement: "whatever this checker accepts has a set-theoretic model". The remaining trust is narrow and spelled out:

- the consistency of the set theory behind the model;
- the kernel that checked con-leche's proof;
- the compilers and runtimes (including the big-number library) used to build each checker. Running con-leche on the Lean toolchain and con-ron on the Rust toolchain makes a shared compiler bug unlikely.

**Two gaps no kernel closes.** A kernel checks the term it is given against the statement it is given. Metaprograms can, in principle, make what you read in the editor differ from what the kernel checked. Comparator closes that gap: it re-checks the exported declarations, in a sandbox, against a held-out copy of the statement ([Lean and AI Formalization §11.1](lean-ai-formalization.md#s11-1)). The last gap is **statement fidelity**: does `2 * sumTo n = n * (n + 1)` really say what you meant? Only a human can judge that. For our theorem it takes one glance at the three-line definition of `sumTo`. For a research theorem it can take serious expert reading.

**The trust stack.** Every layer of trust ends in mathematics:

```text
┌──────────────────────────────────────────────────────────────────────┐
│ Your statement: 2 * sumTo n = n * (n + 1)                            │
│ Checked by a person reading it: does it say what you meant?          │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼ rests on
┌──────────────────────────────────────────────────────────────────────┐
│ Elaborator, tactics, AI provers                                      │
│ Untrusted. Comparator re-checks the exported result against a        │
│ held-out statement                                                   │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Kernel implementations                                               │
│ Five independent checkers; con-leche is proved to accept only what   │
│ has a model                                                          │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ Type theory (Lean's Calculus of Inductive Constructions)             │
│ Consistent because it has a model in set theory (Carneiro)           │
└──────────────────────────────────┬───────────────────────────────────┘
                                   ▼
╔══════════════════════════════════════════════════════════════════════╗
║ Set theory (ZFC plus inaccessible cardinals)                         ║
║ The same foundation paper mathematics rests on                       ║
╚══════════════════════════════════════════════════════════════════════╝

Gödel: no system proves its own consistency, so each layer leans on the one below it.
```

Only the top layer needs human judgment. Each layer below it is a mathematical claim, and each claim is checked by the layer beneath.

### 6.1 Sidebar: why Lean is not ZFC, and where the extra cardinals come from {#s6-1}

ZFC is first-order logic plus axioms about one kind of object, the set. Lean is a type theory, and its design choices differ from ZFC's on purpose:

- **Types, not untyped sets.** In ZFC, "3 ∈ π" is a legitimate (meaningless) question. In Lean it does not type-check.
- **Proofs are objects.** A ZFC proof is a derivation outside the theory. A Lean proof is a term inside it, which a kernel can check.
- **Computation is built in.** `rfl` proves `2 * sumTo 0 = 0` by computing. ZFC has no notion of computation.
- **Induction is generated.** Declaring `Nat` produces `Nat.rec`. In ZFC, ℕ is a particular set and induction is a theorem about it.

**The universes.** Lean has a tower of types of types: `Prop`, `Type 0`, `Type 1`, …, with each `Type u` living in `Type (u+1)`. To model `Type u` as a set, you need a set closed under everything you can build inside it: function spaces, power sets, and unions of families indexed by its members. Such a set is a **Grothendieck universe**.

A Grothendieck universe exists exactly when there is a **strongly inaccessible cardinal** κ. Such a cardinal is uncountable, *regular* (not a union of fewer than κ smaller sets) and a *strong limit* (if λ < κ then 2^λ < κ). The sets of rank below κ then form a model of all of ZFC. That is exactly why ZFC cannot prove such a κ exists: it would prove its own consistency, which Gödel's second theorem forbids. So the existence of inaccessibles has to be added as an axiom.

**The model.** In Mario Carneiro's model (his 2019 thesis, *The Type Theory of Lean*), `Prop` becomes the two truth values, and each `Type u` becomes the universe at the (u+1)-th inaccessible. Any single proof uses only finitely many universe levels, so Lean's consistency follows from ZFC plus "there are n inaccessible cardinals", for each finite n. This is a strictly stronger assumption than ZFC alone. Mathematicians have used it since Grothendieck brought universes into algebraic geometry in the 1960s. Elementary results like our sum formula do not need it. *(To verify against the thesis before this page leaves WIP.)*

[↑ Contents](#contents)

## 7. No magic {#s7}

Followed all the way down, "Lean proved 1 + 2 + ⋯ + n = n(n + 1)/2" unpacks into a chain of ordinary mathematical facts:

1. The theorem is a **type**, built from Π, `Eq` and `Nat`.
2. The proof is a **term**, built from `Nat.rec` (induction), `Eq.refl` (equality) and a few lemmas that are themselves terms of the same kind.
3. Each of those primitives is **generated by a fixed recipe** from two short inductive declarations. Induction comes from what `Nat` is; it is not assumed separately.
4. The kernel **checks** the term with a handful of typing rules and reductions. It is a small, deterministic algorithm, simple enough to write in a few thousand lines.
5. The kernel's **correctness** is a theorem: con-leche accepts only what has a model in set theory, and that proof was itself machine-checked.
6. The **logic's consistency** rests on set theory, the same foundation that paper mathematics uses.

Every layer is math, described in a way a machine can check. The tactics, the elaborator, the editor and the AI that may have written the proof all sit *outside* this chain. They can make finding a proof easier or harder, but they cannot make a false proof pass. What is left to trust is set theory, a small amount of code checked several independent ways, and your own reading of the statement. That is less than a paper proof asks you to trust.

[↑ Contents](#contents)

## References {#references}

- [Lean (proof assistant)](https://en.wikipedia.org/wiki/Lean_(proof_assistant)), Wikipedia, especially the Artificial intelligence section
- [Calculus of constructions](https://en.wikipedia.org/wiki/Calculus_of_constructions), Wikipedia, General traits
- [Lean and AI Formalization](lean-ai-formalization.md), §1 (foundations) and §11 (kernel trust)
- [MiniLean4](https://learn.h5i.dev/), Hideaki Takahashi: a Lean-style kernel in Rust, built up chapter by chapter
- [Functional Programming in Lean](../Deep-Dives/textbooks/functional-programming-in-lean), textbook breakdown; chapter 3 (propositions and proofs) and chapter 9 (tactics and induction) are the natural next reading
- Mario Carneiro, *The Type Theory of Lean* (MS thesis, Carnegie Mellon, 2019)
