import NoMagic

/-!
# Stage 7 — Computation inside the logic

The conversion rule: a proof of `A` is a proof of `B` when `A` and `B` reduce
to the same thing. Each `rfl` below is accepted only because both sides
reduce to one value.
-/

open NoMagic

/-- info: 10 -/
#guard_msgs in #reduce sumTo 4

/-- info: 12 -/
#guard_msgs in #reduce 2 * sumTo 3

-- β: apply a function to its argument.
example : (fun m : Nat => 2 * m) 5 = 10 := rfl

-- δ + ι: unfold `sumTo`, then run the recursor on `k + 1 = Nat.succ k`.
example (k : Nat) : sumTo (k + 1) = sumTo k + (k + 1) := rfl

-- ι directly on `Nat.rec`.
example (z : Nat) (s : Nat → Nat → Nat) (k : Nat) :
    Nat.rec (motive := fun _ => Nat) z s (k + 1)
      = s k (Nat.rec (motive := fun _ => Nat) z s k) := rfl

-- The base case of the article's proof.
example : 2 * sumTo 0 = 0 * (0 + 1) := rfl

-- A false equation is rejected: `sumTo 3` reduces to 6, not 7.
/--
error: Type mismatch
  Eq.refl 7
has type
  7 = 7
but is expected to have type
  sumTo 3 = 7
-/
#guard_msgs in
example : sumTo 3 = 7 := Eq.refl 7
