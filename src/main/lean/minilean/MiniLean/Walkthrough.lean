import MiniLean.Walkthrough.S1_Surface
import MiniLean.Walkthrough.S2_Names
import MiniLean.Walkthrough.S3_Tactics
import MiniLean.Walkthrough.S4_Recursors
import MiniLean.Walkthrough.S5_Primitives
import MiniLean.Walkthrough.S6_CurryHoward
import MiniLean.Walkthrough.S7_Computation
import MiniLean.Walkthrough.S8_Kernel
import MiniLean.Walkthrough.S9_Checkers

/-!
# No Magic, implemented

The companion [No Magic, compiled](https://vwulf.github.io/ettuge/FP/no-magic-literate/)
took the sum formula apart in Lean, stage by stage, and showed Lean's *output*
at each stage. This one walks the same stages through
[MiniLean](https://vwulf.github.io/ettuge/FP/minilean), a small type checker
written in Lean 4, and shows the *code* that does each step.

Every page is an ordinary Lean file. The output under each command is
MiniLean's own, produced when the page was built, and pinned in the project's
checks.

| Stage | Here | Code that does it |
| --- | --- | --- |
| 1. What you write | the DSL | `MiniLean.DSL` |
| 2. Names, not notation | name resolution, de Bruijn indices | `MiniLean.Surface`, `MiniLean.Expr` |
| 3. Tactics become terms | `intro`, `induction`, `rw` as term builders | `MiniLean.Tactic` |
| 4. Recursion is already a recursor | the generated `Nat.rec` | `addInductive`, `iota?` |
| 5. The primitives | `Nat`, `Eq`, their recursors | `MiniLean.Env` |
| 6. Curry–Howard | Π-types and `Prop` | `infer` |
| 7. Computation | each β, δ, ι step, traced | `whnfStep?`, `whnf`, `isDefEq` |
| 8. The kernel alone | accept and reject | `addTheorem`, `infer`, `isDefEq` |
| 9. Checking the checker | the trusted 745 lines, and what they refuse | `MiniLean.Rejections` |

The source of every module is part of this site: follow the links in the
navigation, or hover over any name in the code.
-/
