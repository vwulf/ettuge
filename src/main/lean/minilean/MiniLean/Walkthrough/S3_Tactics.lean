import MiniLean.Prelude

/-!
# Stage 3 — Tactics become terms

As in Lean, a tactic script is a program that builds a proof term. In MiniLean
each tactic (`MiniLean.Tactic`, function `runTac`) turns one goal into new
goals plus a function that builds the old goal's proof from the new ones:

* `intro x` wraps the proof in `λ (x : A) => …`;
* `induction n` applies the recursor `Nat.rec` to a motive and one proof per constructor;
* `rw [h]` builds an `Eq.rec` (transport along `h`), flipping `h` with a second
  `Eq.rec` when it rewrites left to right;
* `refl` is `Eq.refl`; `show` changes nothing in the term.

A one-line theorem: `add n zero` computes to `n`, so `refl` proves it.
-/

mini_theorem add_zero' (n : Nat) : NatEq (add n zero) n := by
  refl

#mini_print add_zero'

/-!
The binder `(n : Nat)` became a `λ`, and `refl` became `Eq.refl`. The kernel
accepts the term because `add n zero` and `n` are definitionally equal.

A proof by induction and rewriting: every tactic is visible in the term.
-/

#mini_print zero_add
