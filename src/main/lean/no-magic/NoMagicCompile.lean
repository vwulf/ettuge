import NoMagicCompile.S1_Surface
import NoMagicCompile.S2_Notation
import NoMagicCompile.S3_Tactics
import NoMagicCompile.S4_Recursion
import NoMagicCompile.S5_Primitives
import NoMagicCompile.S6_CurryHoward
import NoMagicCompile.S7_Computation
import NoMagicCompile.S8_Kernel
import NoMagicCompile.S9_Checkers
import NoMagicCompile.Checks

/-!
# No Magic, compiled: one proof, from what you write to what the kernel checks

This is the literate companion to the article
[No Magic: Proving 1 + 2 + … + n = n(n+1)/2 from Paper to Lean's Kernel](https://vwulf.github.io/ettuge/FP/lean-no-magic).
The article explains each layer in prose. Here each layer is shown by Lean itself.

Every page below is an ordinary Lean file from the
[`no-magic`](https://github.com/vwulf/ettuge/tree/master/src/main/lean/no-magic) project.
The output under each command is Lean's own, produced when the page was built.
Every one is also pinned with `#guard_msgs` in `NoMagicCompile.Checks`, so the
project does not build if Lean ever prints something different. Hover over any
name to see its type.

1. **Surface syntax.** The theorem as a person writes it.
2. **Notation removed.** `2 * x` is a function call with instance arguments.
3. **Tactics become terms.** `rw` and `induction` are programs that build proof terms.
4. **Recursion becomes a recursor.** `sumTo` compiles to `Nat.brecOn`, which is built from `Nat.rec`.
5. **The primitives.** `Nat`, `Eq` and their recursors: induction and rewriting.
6. **Curry–Howard.** `∀` is a function type; the connectives are inductive types.
7. **Computation.** β, δ and ι reduction, and a false equation rejected.
8. **The kernel alone.** Declarations handed straight to the kernel: accepted and rejected.
9. **Checking the checker.** Independent kernels, and the full list of axioms.

The proofs themselves are in `NoMagic.SumFormula`.
-/
