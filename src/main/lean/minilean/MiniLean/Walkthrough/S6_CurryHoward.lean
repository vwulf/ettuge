import MiniLean.Prelude

/-!
# Stage 6 — Curry–Howard

A statement is a type; a proof is a term of that type. MiniLean has a single
binder for both `∀` and `→`: the Π-type (`Expr.pi`). An arrow `A → B` is a Π
whose body does not use its variable.

Propositions are types in `Prop` (`Sort 0`). The kernel computes the universe
of a Π-type with `imax` (function `infer`): a `∀` over numbers whose body is a
proposition is again a proposition.
-/

#mini_check NatEq two two
#mini_check ∀ (n : Nat), NatEq n n
#mini_check Nat → Nat

/-! The theorem is a function from numbers to proofs. Applied to `three`, it gives a proof about `three`. -/

#mini_check two_mul_sumTo three

/-! The sorts themselves: `Prop : Type` and `Type : Sort 2`, never `Type : Type`. -/

#mini_check Prop
#mini_check Type
