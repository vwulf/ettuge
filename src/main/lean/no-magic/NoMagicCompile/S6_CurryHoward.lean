import NoMagic

/-!
# Stage 6 — Curry–Howard: statements are types

`∀` is the dependent function type, `→` is the non-dependent one, and the
connectives are ordinary inductive types. A proof is a term of the
statement's type.
-/

open NoMagic

-- `∀ n, P n` and `(n : Nat) → P n` are the same type, by `rfl`.
example (P : Nat → Prop) : (∀ n, P n) = ((n : Nat) → P n) := rfl

-- The theorem *is* a function from numbers to proofs.
/-- info: two_mul_sumTo : ∀ (n : Nat), 2 * sumTo n = n * (n + 1) -/
#guard_msgs in #check (two_mul_sumTo : (n : Nat) → 2 * sumTo n = n * (n + 1))

/-- info: two_mul_sumTo 10 : 2 * sumTo 10 = 10 * (10 + 1) -/
#guard_msgs in #check two_mul_sumTo 10

-- Propositions live in `Prop = Sort 0`; data types in `Type = Sort 1`.
example : Prop = Sort 0 := rfl
example : Type = Sort 1 := rfl

-- The connectives are inductive types. `False` has no constructors,
-- so there is nothing to build a proof of it from.
/--
info: structure And (a b : Prop) : Prop
number of parameters: 2
fields:
  And.left : a
  And.right : b
constructor:
  And.intro {a b : Prop} (left : a) (right : b) : a ∧ b
-/
#guard_msgs in #print And

/--
info: inductive Or : Prop → Prop → Prop
number of parameters: 2
constructors:
Or.inl : ∀ {a b : Prop}, a → a ∨ b
Or.inr : ∀ {a b : Prop}, b → a ∨ b
-/
#guard_msgs in #print Or

/--
info: inductive False : Prop
number of parameters: 0
constructors:
-/
#guard_msgs in #print False

/--
info: inductive Exists.{u} : {α : Sort u} → (α → Prop) → Prop
number of parameters: 2
constructors:
Exists.intro : ∀ {α : Sort u} {p : α → Prop} (w : α), p w → Exists p
-/
#guard_msgs in #print Exists
