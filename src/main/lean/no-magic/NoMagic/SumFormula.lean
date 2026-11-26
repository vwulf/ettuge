/-!
# The sum formula, core Lean only

Companion code for the article *No Magic* (`src/main/md/pl/lean-no-magic.md`).
Every proof here uses only core Lean 4 (no Mathlib), so each lemma it cites
is a short piece of library code you can read.
-/

namespace NoMagic

/-- `S(0) = 0`, `S(k+1) = S(k) + (k+1)`. -/
def sumTo : Nat → Nat
  | 0     => 0
  | k + 1 => sumTo k + (k + 1)

/-- `P(n): 2 · S(n) = n(n+1)`, by induction, following the hand proof step by step. -/
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

/-- Divide at the end: `S(n) = n(n+1)/2`. -/
theorem sumTo_eq (n : Nat) : sumTo n = n * (n + 1) / 2 := by
  rw [← two_mul_sumTo n, Nat.mul_div_cancel_left (sumTo n) (by decide : 0 < 2)]

/-- The same proof with no tactics: a direct application of `Nat.rec`. -/
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

/-! ## Checks the build enforces

These make `lake build` fail if a claim in the article stops being true. -/

-- The formula computes correctly.
#guard sumTo 100 = 5050

-- The article says the proofs use exactly one axiom, `propext`.
/-- info: 'NoMagic.sumTo_eq' depends on axioms: [propext] -/
#guard_msgs in #print axioms sumTo_eq

/-- info: 'NoMagic.two_mul_sumTo'' depends on axioms: [propext] -/
#guard_msgs in #print axioms two_mul_sumTo'

-- ...and that the definition and the base case use none.
/-- info: 'NoMagic.sumTo' does not depend on any axioms -/
#guard_msgs in #print axioms sumTo

end NoMagic
