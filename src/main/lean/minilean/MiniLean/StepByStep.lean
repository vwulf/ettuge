import MiniLean.Prelude
import MiniLean.Explain

/-!
# One proof, step by step

This page follows one declaration from the text you type to the kernel's
"accepted", one function at a time. The declaration is the first lemma of the
prelude:

```
mini_theorem zero_add (n : Nat) : NatEq (add zero n) n := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add zero k)) (succ k)
    rw [ih]
```

Each section names the function that does the step and shows its output. The
display commands (`#mini_syntax`, `#mini_raw`, `#mini_tactics`, …) are defined in
`MiniLean.Explain`: they run the same functions that `mini_theorem` runs, print
what each one produced, and add nothing to the environment.

| Step | Turns | into | Done by |
| --- | --- | --- | --- |
| 1 | text | Lean `Syntax` | Lean's parser, with the rules in `MiniLean.DSL` |
| 2 | `Syntax` | `Raw` | `toRaw`, `toBinders`, `Raw.binders` |
| 3 | `Raw` | `Expr` | `Raw.toExpr` |
| 4 | tactic syntax | `List Tac` | `toTacs`, plus one `intro` per binder |
| 5 | goal and `List Tac` | proof term | `prove`, `solve`, `runTac` |
| 6 | proof term | "accepted" | `addTheorem`: `infer`, `whnf`, `isDefEq` |
| 7 | accepted declaration | environment entry | `Env.add`, `commitEnv` |

Steps 1–5 are the front end, which nothing trusts. Step 6 is the kernel.
-/

/-!
## 1. Text to `Syntax`

MiniLean has no parser. `MiniLean.DSL` declares syntax categories
(`mini_term`, `mini_binder`, `mini_tactic`) and rules such as

```
syntax "∀ " mini_binder+ ", " mini_term : mini_term
syntax:10 mini_term:10 colGt mini_term:11 : mini_term   -- application
```

and Lean's own parser uses them. The result is a Lean `Syntax` tree, one node
per rule that matched. Here is the tree for the statement (the binder `(n : Nat)`
written as a `∀`, which is how step 2 will treat it):
-/

#mini_syntax ∀ (n : Nat), NatEq (add zero n) n

/-!
Application is a binary node (`mini_term___`), so `NatEq (add zero n) n` is
`(NatEq (add zero n)) n`. The parentheses are still there as a node of their own.

## 2. `Syntax` to `Raw`

`toRaw` (in `MiniLean.DSL`) walks the `Syntax` tree by pattern matching on
quotations, one case per rule:

```
| `(mini_term| $x:ident) => pure (.ident (nameOf x) none)
| `(mini_term| ($t)) => toRaw t
| `(mini_term| $f $a) => return .app (← toRaw f) (← toRaw a)
| `(mini_term| ∀ $bs*, $b) => return MiniLean.Raw.binders true (← toBinders bs) (← toRaw b)
```

`Raw` is MiniLean's own type, with five constructors. Parentheses are gone, and
names are still just strings. For `mini_theorem`, the binders before the colon
are wrapped around the statement by `Raw.binders true`, which gives the same tree
as writing the `∀`:
-/

#mini_raw ∀ (n : Nat), NatEq (add zero n) n

/-!
## 3. `Raw` to `Expr`: names

`Raw.toExpr` (in `MiniLean.Surface`) resolves every name. It looks first for a
binder it is under, then for a local of the current goal, then for a constant:

* `n` is the nearest enclosing binder, so it becomes `bvar 0`: a de Bruijn
  index counts binders outward, and the name is dropped;
* `zero` is not declared, but `mini_open Nat` lets it mean `Nat.zero`;
* `add` and `NatEq` are constants of the environment, with no universe arguments.

This is the term the kernel will see as the statement:
-/

#mini_db ∀ (n : Nat), NatEq (add zero n) n

/-!
Nothing has been checked yet: `Raw.toExpr` only fails on unknown names or a
wrong number of universe arguments. Whether the statement is well typed is the
kernel's question. Asked now, `infer` says it is a proposition:
-/

#mini_check ∀ (n : Nat), NatEq (add zero n) n

/-!
## 4. Tactic syntax to `List Tac`

`toTacs` turns each tactic into a constructor of `Tac` (in `MiniLean.Tactic`):
`intro k ih` becomes two `intro`s, and `·` becomes `focus` with the block's
tactics inside. `elabTheoremBy` then puts one `intro` per binder in front, so the
script that runs is the first line of the output below.

## 5. Tactics to a proof term

`prove` starts with one goal, `⊢ ∀ (n : Nat), NatEq (add zero n) n`, with no
locals. `solve` runs the tactics depth first: each tactic acts on the first open
goal, and the goals it creates are solved before the next one.

`runTac` is the whole of a tactic's meaning. It returns the new goals, and a
*builder*: a function from proofs of the new goals to a proof of the old one.
Below, each step shows the goal it acted on (`on`), the goals it created (`new`),
and its builder applied to placeholders `?k` for the new goals. Substituting each
`?k` into the line that created it gives the final term, `?0`.
-/

#mini_tactics (n : Nat) : NatEq (add zero n) n := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add zero k)) (succ k)
    rw [ih]

/-!
What each tactic did:

* `intro n`: the goal reduces to a `∀` (`whnf`), so a fresh free variable `n`
  joins the locals and the target is the `∀`'s body with `n` for `bvar 0`
  (`instantiate1`). The builder wraps the body's proof in `λ (n : Nat) => …`,
  turning the free variable back into `bvar 0` (`abstract1`).
* `induction n`: the motive is the goal with `n` abstracted,
  `λ (n : Nat) => NatEq (add zero n) n`. The new goals are the types of
  `Nat.rec`'s minor premises for that motive, β-reduced for display: the base
  case and the step. The builder is `Nat.rec.{0} motive ?2 ?3 n`; the level `0`
  is the motive's universe, `Prop`.
* `refl`: the goal unfolds to `Eq.{1} Nat (add zero zero) zero`, and `isDefEq`
  finds both sides equal (below). The proof is `Eq.refl.{1} Nat (add zero zero)`.
* `show`: checks that the new statement is definitionally equal to the goal, and
  contributes nothing to the term (`?5 := ?6`).
* `rw [ih]`: `ih`'s type unfolds to `Eq.{1} Nat (add zero k) k`. The rewrite
  finds `add zero k` in the goal, makes the goal into a function of it (the
  *motive*), and transports along the equation with `Eq.rec`. Rewriting left to
  right needs the equation the other way round, so `ih` is first flipped by a
  second `Eq.rec`. The new goal `NatEq (succ k) (succ k)` holds by `refl`.

### What `refl` and `show` relied on

`refl` needed `add zero zero` to compute to `zero`. `whnf` takes one head step at
a time: unfold `add` (δ), substitute its two arguments (β, β), then `Nat.rec` on
the constructor `Nat.zero` returns the base case (ι):
-/

#mini_trace add zero zero

/-!
`show` needed its statement to be definitionally equal to the goal. `isDefEq`
reduces both sides to weak head normal form, then compares heads and arguments.
On the right, `add zero (succ k)` computes to `succ (Nat.rec … k)`, because
`Nat.rec` can take one ι-step on `succ k`. On the left, `add zero k` unfolds to
the same stuck `Nat.rec … k`, which cannot reduce further because `k` is a
variable:
-/

#mini_defeq ∀ (k : Nat), NatEq (succ (add zero k)) (succ k) =?= ∀ (k : Nat), NatEq (add zero (succ k)) (succ k)

/-!
This is why the script says `show` before `rw [ih]`: `rw` matches syntactically,
and `add zero k` appears in the goal only after `show` restates it.

## 6. The proof term to the kernel

`elabTheoremBy` hands the finished term to `addTheorem`, exactly as if it had
been written by hand. The tactics' work is not trusted: the kernel checks the
term from scratch. `#mini_kernel` replays the checks `addTheorem` makes, with
the derivation `infer` builds for the proof (arguments shown by their types):
-/

#mini_kernel 0 zero_add

/-!
Three things to see in it:

* **Applications are checked argument by argument.** `infer` puts the head's
  type into weak head normal form, which must be a `∀ (x : D), B`; the
  argument's type must be definitionally equal to `D`; then the result type is
  `B` with the argument for `x`. `Nat.rec`'s type is consumed one `∀` at a time.
* **"Definitionally equal" is where computation happens.** The base case has
  type `Eq … (add zero zero) (add zero zero)` but is expected to have type
  `motive Nat.zero`. These are different terms, and `isDefEq` makes them meet:
-/

#mini_defeq Eq.{1} Nat (add zero zero) (add zero zero) =?= (λ (n : Nat) => NatEq (add zero n) n) zero

/-!
* **The statement's level decides "theorem".** `∀ (n : Nat), P n` lives in
  `Sort (imax 1 0)`, and `imax u 0 = 0`: a `∀` into `Prop` is a proposition,
  whatever it ranges over. That is the impredicativity of `Prop`.

## 7. Into the environment

`addTheorem` returns a new environment with one more entry, a `thm`. The DSL
records it in a Lean environment extension (`commitEnv`), so later declarations,
and later files, can use `zero_add` as a constant. Used as a rewrite rule, its
`∀` becomes a pattern variable, which matching fills in:
-/

#mini_tactics (m : Nat) : NatEq m (add zero m) := by
  rw [zero_add]

/-!
A theorem's proof is stored but never unfolded: `whnfStep?` only unfolds
`defn`s. What was stored:
-/

#mini_print zero_add
