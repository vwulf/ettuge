import MiniLean.Prelude

/-!
# Stage 5 — The primitives

Everything the proof uses comes from two inductive declarations in
`MiniLean.Prelude`. Here they are as the environment stores them
(`MiniLean.Env`): the types, their constructors, and the generated recursors.
-/

#mini_print Nat
#mini_print Nat.zero
#mini_print Nat.succ

/-! `Eq` has two parameters (`α` and `a`), one index, and a single constructor. -/

#mini_print Eq
#mini_print Eq.refl

/-!
Its recursor is transport: from a proof of `motive a (refl)` and a proof `t`
that `a = x`, get `motive x t`. This is "replace equals by equals", and it is
all that `rw` uses.
-/

#mini_print Eq.rec
