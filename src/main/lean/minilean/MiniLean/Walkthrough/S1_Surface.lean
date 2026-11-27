import MiniLean.Prelude

/-!
# Stage 1 — What you write

In Lean, stage 1 was the theorem as a person writes it, with notation,
implicit arguments and a tactic script. In MiniLean there is only the DSL
(`MiniLean.DSL`): Lean's parser reads `mini_theorem …`, and the command hands
the result to MiniLean.

The theorem, as stated in `MiniLean.Prelude`:
-/

#mini_check two_mul_sumTo

/-!
There is no notation to hide anything: `mul two (sumTo n)` is exactly what the
kernel sees. `NatEq a b` is an ordinary definition, `Eq.{1} Nat a b`, and `two`
is `succ (succ zero)`.

The building blocks have the types you would expect:
-/

#mini_check add
#mini_check sumTo
#mini_check NatEq
