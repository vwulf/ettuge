import MiniLean.Prelude

/-!
# Stage 2 — Names, not notation

In Lean, stage 2 removed notation and revealed the implicit arguments and
instances the elaborator had filled in. MiniLean has none of these, so the
corresponding step is smaller: **name resolution** (`MiniLean.Surface`).

Each name becomes one of three things:
* a **bound variable**, written as a de Bruijn index: `bvar 0` is the nearest
  enclosing binder, `bvar 1` the next one out;
* a **local** in a tactic goal (a free variable);
* a **constant** in the environment. `mini_open Nat` lets `Nat.succ` be
  written `succ`.

`#mini_expr` shows the term exactly as the kernel stores it, as values of the
Lean type `MiniLean.Expr`. The binder names are kept only for printing.
-/

#mini_expr λ (x : Nat) => succ x

/-! With two binders, the inner one is `bvar 0` and the outer one `bvar 1`: -/

#mini_expr λ (m n : Nat) => add n m

/-!
Universe arguments are never inferred. `Nat.rec` takes one (the universe of
its motive), and it must be written: `Nat.rec.{1}` recurses into `Type`,
`Nat.rec.{0}` into `Prop`.
-/

#mini_check Nat.rec.{1}
