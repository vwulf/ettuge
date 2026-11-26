import Lean
import NoMagic
import NoMagicCompile.S8_Kernel

/-!
# Pinned outputs for the stage pages

Each stage page shows Lean's own output under each command. This module
re-runs every one of those commands inside `#guard_msgs`, with the expected
output written out, so `lake build` fails if a Lean upgrade changes anything
the pages show. It is left off the literate site (see `literate.toml`).
-/

open Lean Meta NoMagic NoMagicCompile

/-! ## Stage 1 -/

/-- info: sumTo : Nat → Nat -/
#guard_msgs in #check @sumTo

/-- info: NoMagic.two_mul_sumTo (n : Nat) : 2 * sumTo n = n * (n + 1) -/
#guard_msgs in #check two_mul_sumTo

/-- info: NoMagic.sumTo_eq (n : Nat) : sumTo n = n * (n + 1) / 2 -/
#guard_msgs in #check sumTo_eq

/-! ## Stage 2 -/

/-- info: NoMagic.two_mul_sumTo (n : Nat) : Eq (HMul.hMul 2 (sumTo n)) (HMul.hMul n (HAdd.hAdd n 1)) -/
#guard_msgs in
set_option pp.notation false in
#check two_mul_sumTo

/--
info: NoMagic.two_mul_sumTo (n : Nat) :
  @Eq Nat
    (@HMul.hMul Nat Nat Nat (@instHMul Nat instMulNat) (@OfNat.ofNat Nat (nat_lit 2) (instOfNatNat (nat_lit 2)))
      (sumTo n))
    (@HMul.hMul Nat Nat Nat (@instHMul Nat instMulNat) n
      (@HAdd.hAdd Nat Nat Nat (@instHAdd Nat instAddNat) n (@OfNat.ofNat Nat (nat_lit 1) (instOfNatNat (nat_lit 1)))))
-/
#guard_msgs in
set_option pp.notation false in
set_option pp.explicit true in
#check two_mul_sumTo

/-! ## Stage 3 -/

/--
info: Try this:
  [apply] exact Eq.mpr (id (congrArg (fun _a => _a + 2 * (k + 1) = k * (k + 1) + 2 * (k + 1)) ih))
    (Eq.refl (k * (k + 1) + 2 * (k + 1)))
-/
#guard_msgs in
example (k : Nat) (ih : 2 * sumTo k = k * (k + 1)) :
    2 * sumTo k + 2 * (k + 1) = k * (k + 1) + 2 * (k + 1) := by
  show_term rw [ih]

/--
info: Try this:
  [apply] exact Nat.recAux (Eq.refl (2 * sumTo 0)) (fun k ih => two_mul_sumTo (k + 1)) n
-/
#guard_msgs in
example (n : Nat) : 2 * sumTo n = n * (n + 1) := by
  show_term induction n with
  | zero => rfl
  | succ k ih => exact two_mul_sumTo (k + 1)

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

/-! ## Stage 4 -/

/-- info: def NoMagic.sumTo : Nat → Nat :=
fun x => Nat.brecOn x sumTo._f -/
#guard_msgs in #print sumTo

/--
info: @[reducible] def NoMagic.sumTo._f : (x : Nat) → Nat.below x → Nat :=
fun x f =>
  (match (motive := (x : Nat) → Nat.below x → Nat) x with
    | 0 => fun x => 0
    | k.succ => fun x => x.1 + (k + 1))
    f
-/
#guard_msgs in #print sumTo._f

/--
info: @[reducible] protected def Nat.below.{u} : {motive : Nat → Sort u} → Nat → Sort (max 1 u) :=
fun {motive} t => Nat.rec PUnit (fun n n_ih => motive n ×' n_ih) t
-/
#guard_msgs in #print Nat.below

/-- info: sumTo.eq_1 : sumTo 0 = 0 -/
#guard_msgs in #check @sumTo.eq_1

/-- info: sumTo.eq_2 : ∀ (k : Nat), sumTo k.succ = sumTo k + (k + 1) -/
#guard_msgs in #check @sumTo.eq_2

/-! ## Stage 5 -/

/--
info: inductive Nat : Type
number of parameters: 0
constructors:
Nat.zero : Nat
Nat.succ : Nat → Nat
-/
#guard_msgs in #print Nat

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

/-! ## Stage 6 -/

/-- info: two_mul_sumTo : ∀ (n : Nat), 2 * sumTo n = n * (n + 1) -/
#guard_msgs in #check (two_mul_sumTo : (n : Nat) → 2 * sumTo n = n * (n + 1))

/-- info: two_mul_sumTo 10 : 2 * sumTo 10 = 10 * (10 + 1) -/
#guard_msgs in #check two_mul_sumTo 10

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
info: inductive Exists.{u} : {α : Sort u} → (α → Prop) → Prop
number of parameters: 2
constructors:
Exists.intro : ∀ {α : Sort u} {p : α → Prop} (w : α), p w → Exists p
-/
#guard_msgs in #print Exists

/--
info: inductive False : Prop
number of parameters: 0
constructors:
-/
#guard_msgs in #print False

/-! ## Stage 7 -/

/-- info: 10 -/
#guard_msgs in #reduce sumTo 4

/-- info: 12 -/
#guard_msgs in #reduce 2 * sumTo 3

/-! ## Stage 8 -/

/--
info: ∀ (n : Nat), 2 * sumTo n = n * (n + 1)
kernel accepted
-/
#guard_msgs in
run_meta do
  let some ci := (← getEnv).find? ``NoMagic.two_mul_sumTo' | throwError "missing"
  let decl := .thmDecl {
    name := `NoMagicCompile.viaKernel, levelParams := []
    type := ci.type, value := ci.value! (allowOpaque := true) }
  logInfo m!"{ci.type}\n{← kernelVerdict decl}"

/--
info: 2 * sumTo 3 = 13
kernel rejected: (kernel) declaration type mismatch, 'NoMagicCompile.bogus' has type
  2 * sumTo 3 = 2 * sumTo 3
but it is expected to have type
  2 * sumTo 3 = 13
-/
#guard_msgs in
run_meta do
  let lhs ← twoTimesSumTo 3
  let type ← mkEq lhs (toExpr (13 : Nat))
  let decl := .thmDecl { name := `NoMagicCompile.bogus, levelParams := [], type, value := ← mkEqRefl lhs }
  logInfo m!"{type}\n{← kernelVerdict decl}"

/--
info: 2 * sumTo 3 = 12
kernel accepted
-/
#guard_msgs in
run_meta do
  let lhs ← twoTimesSumTo 3
  let type ← mkEq lhs (toExpr (12 : Nat))
  let decl := .thmDecl { name := `NoMagicCompile.honest, levelParams := [], type, value := ← mkEqRefl lhs }
  logInfo m!"{type}\n{← kernelVerdict decl}"

/-! ## Stage 9 -/

/-- info: 'NoMagic.sumTo_eq' depends on axioms: [propext] -/
#guard_msgs in #print axioms sumTo_eq
