import MiniLean.Prelude

/-!
# What the kernel refuses

A checker that accepts everything is useless. Each declaration below is wrong
in a different way, and MiniLean must reject it. `#guard_msgs` pins the exact
rejection, so this file builds only if every one is refused. It uses the
prelude's `Nat`, `Eq` and `add`.
-/

/-! A false equation, "proved" by computation: `n + 0` reduces to `n`, not `n + 1`.
With a proof term the kernel itself refuses it. -/
/--
error: type mismatch.
  term: λ (n : Nat) => Eq.refl.{1} Nat (Nat.succ n)
  has type: ∀ (n : Nat), Eq.{1} Nat (Nat.succ n) (Nat.succ n)
  expected: ∀ (n : Nat), Eq.{1} Nat (add n Nat.zero) (Nat.succ n)
-/
#guard_msgs in
mini_theorem bad (n : Nat) : Eq.{1} Nat (add n zero) (succ n) := Eq.refl.{1} Nat (succ n)

/-! With a tactic, the tactic gives up first. Tactics are untrusted, so this is only a
courtesy: had it built a wrong term anyway, the kernel would refuse it as above. -/
/--
error: refl: the two sides are not definitionally equal
n : Nat
⊢ Eq.{1} Nat (add n Nat.zero) (Nat.succ n)
-/
#guard_msgs in
mini_theorem bad' (n : Nat) : Eq.{1} Nat (add n zero) (succ n) := by
  refl

/-! `Type` does not have type `Type`. If it did, Hurkens' paradox would prove anything. -/
/--
error: type mismatch.
  term: Type
  has type: Sort 2
  expected: Type
-/
#guard_msgs in
mini_def typeInType : Type := Type

/-! A type built from functions out of itself is not strictly positive: it would allow a
non-terminating term, and so a proof of anything. -/
/-- error: constructor 'Bad.mk': 'Bad' may only appear as a field's whole type, applied to its parameters (strict positivity) -/
#guard_msgs in
mini_inductive Bad : Type where
  | mk : (Bad → Nat) → Bad

/-! A type in `Type` cannot store a whole `Type`: that would break the universe hierarchy. -/
/-- error: constructor 'Big.mk': a field lives in a universe larger than 'Big's -/
#guard_msgs in
mini_inductive Big : Type where
  | mk : Type → Big

/-! A proposition with two constructors may only be eliminated into `Prop`: its recursor has
no universe parameter, and its motive returns `Prop`. -/
mini_inductive Or (a b : Prop) : Prop where
  | inl : a → Or a b
  | inr : b → Or a b

/--
info: recursor Or.rec : ∀ (a : Prop), ∀ (b : Prop), ∀ (motive : Or a b → Prop), (∀ (x : a), motive (Or.inl a b x)) → (∀ (x : b), motive (Or.inr a b x)) → ∀ (t : Or a b), motive t
-/
#guard_msgs in
#mini_print Or.rec

/-! A misspelt name is a front-end error: the kernel never sees the term. -/
/-- error: unknown identifier 'sucd' -/
#guard_msgs in
mini_def oops : Nat := sucd zero
