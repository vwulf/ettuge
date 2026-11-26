import NoMagic

/-!
# Stage 3 — Tactics become a term

A tactic proof is a program that builds a term. `show_term` prints the term a
tactic produced; `#print` shows the whole term stored for a theorem.
-/

open NoMagic

-- `rw [ih]` builds a call to `Eq.mpr` with a congruence proof made from `ih`.
/--
info: Try this:
  [apply] exact Eq.mpr (id (congrArg (fun _a => _a + 2 * (k + 1) = k * (k + 1) + 2 * (k + 1)) ih))
    (Eq.refl (k * (k + 1) + 2 * (k + 1)))
-/
#guard_msgs in
example (k : Nat) (ih : 2 * sumTo k = k * (k + 1)) :
    2 * sumTo k + 2 * (k + 1) = k * (k + 1) + 2 * (k + 1) := by
  show_term rw [ih]

-- `induction` builds an application of the recursor (`Nat.recAux` is `Nat.rec`
-- with `0` and `n + 1` in place of `Nat.zero` and `Nat.succ n`).
/--
info: Try this:
  [apply] exact Nat.recAux (Eq.refl (2 * sumTo 0)) (fun k ih => two_mul_sumTo (k + 1)) n
-/
#guard_msgs in
example (n : Nat) : 2 * sumTo n = n * (n + 1) := by
  show_term induction n with
  | zero => rfl
  | succ k ih => exact two_mul_sumTo (k + 1)

-- The article's term-mode proof, as stored after elaboration.
/--
info: theorem NoMagic.two_mul_sumTo' : ∀ (n : Nat), 2 * sumTo n = n * (n + 1) :=
fun n =>
  Nat.rec rfl
    (fun k ih =>
      have this :=
        Eq.trans (Nat.mul_add 2 (sumTo k) (k + 1))
          (Eq.trans (congrArg (fun x => x + 2 * (k + 1)) ih)
            (Eq.trans (Eq.symm (Nat.add_mul k 2 (k + 1))) (Nat.mul_comm (k + 2) (k + 1))));
      this)
    n
-/
#guard_msgs in
set_option pp.proofs true in
#print two_mul_sumTo'
