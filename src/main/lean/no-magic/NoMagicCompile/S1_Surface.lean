import NoMagic

/-!
# Stage 1 — Surface syntax

What a person writes and reads: `NoMagic.sumTo` and `NoMagic.two_mul_sumTo`
(see `NoMagic.SumFormula`). Notation (`*`, `+`, numerals) is on, implicit
arguments are hidden, and the proof is a tactic script.

The output under each command is Lean's own. The same outputs are pinned in
`NoMagicCompile.Checks`, so the project does not build if they ever change.
-/

open NoMagic

#check @sumTo
#check two_mul_sumTo
#check sumTo_eq
