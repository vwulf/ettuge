/-!
# Stage 5 — The primitives

Everything above bottoms out in a few inductive declarations and the
recursors Lean generates from them. `Nat.rec` is induction; `Eq.rec` is
"replace equals by equals". Neither is an axiom.
-/

/--
info: inductive Nat : Type
number of parameters: 0
constructors:
Nat.zero : Nat
Nat.succ : Nat → Nat
-/
#guard_msgs in #print Nat

-- Read `motive` as a proposition about `n`: this is the principle of induction.
/-- info: @Nat.rec : {motive : Nat → Sort u_1} → motive Nat.zero → ((n : Nat) → motive n → motive n.succ) → (t : Nat) → motive t -/
#guard_msgs in #check @Nat.rec

/--
info: inductive Eq.{u_1} : {α : Sort u_1} → α → α → Prop
number of parameters: 2
constructors:
Eq.refl : ∀ {α : Sort u_1} (a : α), a = a
-/
#guard_msgs in #print Eq

/--
info: @Eq.rec : {α : Sort u_2} →
  {a : α} → {motive : (a_1 : α) → a = a_1 → Sort u_1} → motive a ⋯ → {a_1 : α} → (t : a = a_1) → motive a_1 t
-/
#guard_msgs in #check @Eq.rec
