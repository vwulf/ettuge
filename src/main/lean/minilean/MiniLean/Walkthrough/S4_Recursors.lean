import MiniLean.Prelude

/-!
# Stage 4 — Recursion is already a recursor

In Lean, stage 4 showed `sumTo`'s pattern-matching definition compiled to
`Nat.brecOn`, which is built from `Nat.rec`. MiniLean has no pattern matching,
so there is nothing to compile: definitions are written with `Nat.rec` from the
start.
-/

#mini_print sumTo

/-!
`Nat.rec` itself was not written by anyone. When `mini_inductive Nat` was
declared, the kernel generated it (`MiniLean.Kernel`, function
`addInductive`), by the recipe in chapter 8 of the MiniLean4 book:

* one **motive**, a function from the type to a universe;
* one **minor premise** per constructor, taking the constructor's fields and
  an induction hypothesis for each field of type `Nat`;
* the **major premise**, the value being recursed on.
-/

#mini_print Nat.rec

/-!
How the recursor *computes* is the ι-rule (function `iota?`): on `Nat.succ x`,
it returns the `succ` minor premise applied to `x` and to the recursor applied
to `x`. The trace in stage 7 shows it running.
-/
