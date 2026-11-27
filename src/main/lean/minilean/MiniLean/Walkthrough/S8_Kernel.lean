import MiniLean.Prelude

/-!
# Stage 8 — The kernel alone

In the Lean companion, stage 8 skipped Lean's elaborator and handed
declarations straight to Lean's kernel. MiniLean *is* such a kernel: every
`mini_def` and `mini_theorem` ends in `addDefinition` or `addTheorem`
(`MiniLean.Kernel`), which runs `infer` on the term and checks with `isDefEq`
that its type is the claimed statement.

`#mini_verdict` asks the same question without failing the build. Here are the
two claims from the Lean companion. `2 · sumTo 3 = 12`, proved by `Eq.refl`:
-/

#mini_verdict : NatEq (mul two (sumTo three)) twelve := Eq.refl.{1} Nat twelve

/-! The same one-word proof of `2 · sumTo 3 = 13`. The kernel computes both sides and refuses: -/

#mini_verdict : NatEq (mul two (sumTo three)) thirteen := Eq.refl.{1} Nat thirteen

/-!
A wrong *proof* of a true statement is refused too. `zero_add` does not prove
`succ_add`'s statement:
-/

#mini_verdict (m n : Nat) : NatEq (add (succ m) n) (succ (add m n)) := zero_add n

/-! And the theorem itself, applied to a number, checks as a proof about that number: -/

#mini_verdict : NatEq (mul two (sumTo three)) (mul three (succ three)) := two_mul_sumTo three
