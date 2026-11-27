import MiniLean.DSL

/-!
# The sum formula, from nothing

MiniLean starts with an empty environment. Every declaration below is checked
by MiniLean's kernel before it is added; if the kernel rejects one, this file
does not build.
-/

/-! ## Two inductive types

From these declarations the kernel generates `Nat.rec` (induction and
primitive recursion) and `Eq.rec` (transport: "replace equals by equals"). -/

mini_inductive Nat : Type where
  | zero : Nat
  | succ : Nat → Nat

mini_inductive Eq.{u} (α : Sort u) (a : α) : α → Prop where
  | refl : Eq.{u} α a a

mini_open Nat

#mini_print Nat.rec
#mini_print Eq.rec

/-! ## Definitions

`add` and `mul` recurse on their second argument, as Lean's do. `NatEq a b`
abbreviates `Eq.{1} Nat a b`; it is an ordinary definition, so the kernel
unfolds it whenever it needs to. -/

mini_def NatEq (a b : Nat) : Prop := Eq.{1} Nat a b

mini_def add (m n : Nat) : Nat :=
  Nat.rec.{1} (λ (k : Nat) => Nat) m (λ (k ih : Nat) => succ ih) n

mini_def mul (m n : Nat) : Nat :=
  Nat.rec.{1} (λ (k : Nat) => Nat) zero (λ (k ih : Nat) => add ih m) n

mini_def sumTo (n : Nat) : Nat :=
  Nat.rec.{1} (λ (k : Nat) => Nat) zero (λ (k ih : Nat) => add ih (succ k)) n

mini_def two : Nat := succ (succ zero)
mini_def three : Nat := succ two

#mini_reduce sumTo three
#mini_reduce mul two (sumTo three)

/-! ## The lemmas

Lean's library supplied `Nat.mul_add`, `Nat.add_mul` and `Nat.mul_comm`. Here
each is proved by induction, with the addition facts they rest on. -/

mini_theorem zero_add (n : Nat) : NatEq (add zero n) n := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add zero k)) (succ k)
    rw [ih]

mini_theorem succ_add (m n : Nat) : NatEq (add (succ m) n) (succ (add m n)) := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add (succ m) k)) (succ (succ (add m k)))
    rw [ih]

mini_theorem add_comm (m n : Nat) : NatEq (add m n) (add n m) := by
  induction n
  · show NatEq m (add zero m)
    rw [zero_add]
  · intro k ih
    show NatEq (succ (add m k)) (add (succ k) m)
    rw [succ_add, ih]

mini_theorem add_assoc (a b c : Nat) : NatEq (add (add a b) c) (add a (add b c)) := by
  induction c
  · refl
  · intro k ih
    show NatEq (succ (add (add a b) k)) (succ (add a (add b k)))
    rw [ih]

mini_theorem mul_add (a b c : Nat) : NatEq (mul a (add b c)) (add (mul a b) (mul a c)) := by
  induction c
  · refl
  · intro k ih
    show NatEq (add (mul a (add b k)) a) (add (mul a b) (add (mul a k) a))
    rw [ih, add_assoc]

mini_theorem zero_mul (n : Nat) : NatEq (mul zero n) zero := by
  induction n
  · refl
  · intro k ih
    show NatEq (add (mul zero k) zero) zero
    rw [ih]

mini_theorem succ_mul (m n : Nat) : NatEq (mul (succ m) n) (add (mul m n) n) := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add (mul (succ m) k) m)) (succ (add (add (mul m k) m) k))
    rw [ih, add_assoc, add_assoc, add_comm k m]

mini_theorem mul_comm (m n : Nat) : NatEq (mul m n) (mul n m) := by
  induction n
  · show NatEq zero (mul zero m)
    rw [zero_mul]
  · intro k ih
    show NatEq (add (mul m k) m) (mul (succ k) m)
    rw [succ_mul, ih]

mini_theorem add_mul (a b c : Nat) : NatEq (mul (add a b) c) (add (mul a c) (mul b c)) := by
  rw [mul_comm, mul_add, mul_comm c a, mul_comm c b]

/-! ## The theorem

The hand proof's chain, line for line. -/

mini_theorem two_mul_sumTo (n : Nat) : NatEq (mul two (sumTo n)) (mul n (succ n)) := by
  induction n
  · refl
  · intro k ih
    show NatEq (mul two (add (sumTo k) (succ k))) (mul (succ k) (succ (succ k)))
    rw [mul_add, ih, ← add_mul, mul_comm (add k two) (succ k)]

#mini_check two_mul_sumTo

/-! ## The kernel's verdicts on two small claims -/

mini_def twelve : Nat :=
  succ (succ (succ (succ (succ (succ (succ (succ (succ (succ (succ (succ zero)))))))))))

mini_def thirteen : Nat := succ twelve

#mini_verdict : NatEq (mul two (sumTo three)) twelve := Eq.refl.{1} Nat twelve
#mini_verdict : NatEq (mul two (sumTo three)) thirteen := Eq.refl.{1} Nat thirteen
