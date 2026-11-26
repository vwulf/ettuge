import NoMagic

/-!
# Stage 1 — Surface syntax

What a person writes and reads: `NoMagic.sumTo` and `NoMagic.two_mul_sumTo`
(see `NoMagic/SumFormula.lean`). Notation (`*`, `+`, numerals) is on, implicit
arguments are hidden, and the proof is a tactic script.

Each `#guard_msgs` below pins Lean's actual output: `lake build` fails if a
future Lean version prints something different.
-/

open NoMagic

/-- info: sumTo : Nat → Nat -/
#guard_msgs in #check @sumTo

/-- info: NoMagic.two_mul_sumTo (n : Nat) : 2 * sumTo n = n * (n + 1) -/
#guard_msgs in #check two_mul_sumTo

/-- info: NoMagic.sumTo_eq (n : Nat) : sumTo n = n * (n + 1) / 2 -/
#guard_msgs in #check sumTo_eq
