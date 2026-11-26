import NoMagic

/-!
# Stage 4 — Pattern matching becomes a recursor

`sumTo` was written with two equations. The kernel never sees that form.
Structural recursion is compiled to `Nat.brecOn` ("course-of-values"
recursion):
-/

open NoMagic

#print sumTo

/-!
The body is a `match` in which the recursive call `sumTo k` has become `x.1`:
a lookup into a table of earlier values.
-/

#print sumTo._f

/-!
That table is `Nat.below`, and it is itself a `Nat.rec`: at `n` it holds the
values at every `m < n`.
-/

#print Nat.below

/-! The two original equations come back as theorems Lean proves about the compiled definition. -/

#check @sumTo.eq_1
#check @sumTo.eq_2
