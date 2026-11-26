import NoMagic

/-!
# Stage 6 — Curry–Howard: statements are types

`∀` is the dependent function type. `∀ n, P n` and `(n : Nat) → P n` are the
same type, so `rfl` proves they are equal.
-/

open NoMagic

example (P : Nat → Prop) : (∀ n, P n) = ((n : Nat) → P n) := rfl

/-! The theorem *is* a function from numbers to proofs. Applying it to `10` gives a proof about `10`. -/

#check (two_mul_sumTo : (n : Nat) → 2 * sumTo n = n * (n + 1))
#check two_mul_sumTo 10

/-! Propositions live in `Prop = Sort 0`; data types live in `Type = Sort 1`. -/

example : Prop = Sort 0 := rfl
example : Type = Sort 1 := rfl

/-!
**The connectives are inductive types.** A proof of `A ∧ B` is a pair; a proof
of `A ∨ B` says which side holds; a proof of `∃ x, P x` carries a witness.
-/

#print And
#print Or
#print Exists

/-! `False` has no constructors, so there is nothing to build a proof of it from. -/

#print False
