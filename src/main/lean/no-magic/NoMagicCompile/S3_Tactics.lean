import NoMagic

/-!
# Stage 3 — Tactics become a term

A tactic proof is a program that builds a term. `show_term` prints the term a
tactic produced.

**`rw [ih]`** builds a call to `Eq.mpr` with a congruence proof made from `ih`.
-/

open NoMagic

example (k : Nat) (ih : 2 * sumTo k = k * (k + 1)) :
    2 * sumTo k + 2 * (k + 1) = k * (k + 1) + 2 * (k + 1) := by
  show_term rw [ih]

/-!
**`induction`** builds an application of the recursor. `Nat.recAux` is
`Nat.rec` with `0` and `n + 1` in place of `Nat.zero` and `Nat.succ n`.
-/

example (n : Nat) : 2 * sumTo n = n * (n + 1) := by
  show_term induction n with
  | zero => rfl
  | succ k ih => exact two_mul_sumTo (k + 1)

/-!
**The whole proof.** `#print` shows the article's term-mode proof as stored after
elaboration: one `Nat.rec`, and a chain of `Eq.trans` for the algebra.
-/

set_option pp.proofs true in
#print two_mul_sumTo'
