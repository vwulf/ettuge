import NoMagic

/-!
# Stage 4 — Pattern matching becomes a recursor

`sumTo` was written with two equations. The kernel never sees that form.
Structural recursion is compiled to `Nat.brecOn` ("course-of-values"
recursion), and `Nat.brecOn` and `Nat.below` are themselves defined with
`Nat.rec`. The two equations come back as theorems Lean proves about the
compiled definition.
-/

open NoMagic

/-- info: def NoMagic.sumTo : Nat → Nat :=
fun x => Nat.brecOn x sumTo._f -/
#guard_msgs in #print sumTo

-- The body: a `match` whose recursive call `sumTo k` became `x.1`, a lookup
-- into the table of earlier values that `Nat.below` provides.
/--
info: @[reducible] def NoMagic.sumTo._f : (x : Nat) → Nat.below x → Nat :=
fun x f =>
  (match (motive := (x : Nat) → Nat.below x → Nat) x with
    | 0 => fun x => 0
    | k.succ => fun x => x.1 + (k + 1))
    f
-/
#guard_msgs in #print sumTo._f

-- `Nat.below` is a `Nat.rec`: at `n` it holds the values at every `m < n`.
/--
info: @[reducible] protected def Nat.below.{u} : {motive : Nat → Sort u} → Nat → Sort (max 1 u) :=
fun {motive} t => Nat.rec PUnit (fun n n_ih => motive n ×' n_ih) t
-/
#guard_msgs in #print Nat.below

-- The original equations, recovered as theorems.
/-- info: sumTo.eq_1 : sumTo 0 = 0 -/
#guard_msgs in #check @sumTo.eq_1

/-- info: sumTo.eq_2 : ∀ (k : Nat), sumTo k.succ = sumTo k + (k + 1) -/
#guard_msgs in #check @sumTo.eq_2
