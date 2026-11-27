import MiniLean.Prelude

/-!
# Stage 7 — Computation inside the logic

The kernel's `whnf` takes one step at a time (`MiniLean.Kernel`, function
`whnfStep?`), and each step is one of three rules:

* **δ**: replace a defined constant by its value;
* **β**: apply a `λ` to an argument;
* **ι**: run a recursor on a constructor.

`#mini_trace` prints every head step. Here is `2 + 2`: unfold `add` (δ),
substitute the arguments (β, β), then `Nat.rec` meets `succ (succ zero)` (ι).
It stops when the head is a constructor, `Nat.succ`.
-/

#mini_trace add two two

/-! `sumTo three` takes the same route, through `sumTo`, `Nat.rec` and then `add`. -/

#mini_trace sumTo three

/-! Reducing everywhere, not just at the head, gives the numbers. -/

#mini_reduce add two two
#mini_reduce mul two (sumTo three)

/-!
This is what makes `refl` work. `NatEq (add two two) (succ three)` is proved by
`Eq.refl`: the kernel reduces both sides to the same normal form
(`isDefEq`).
-/

mini_theorem two_add_two : NatEq (add two two) (succ three) := Eq.refl.{1} Nat (succ three)
