import Lean
import NoMagic

/-!
# Stage 8 — The kernel, on its own

The elaborator, tactics and notation are all skipped here. A metaprogram
builds each `Declaration` by hand and calls the kernel's own entry point,
`Kernel.Environment.addDecl`, directly. It returns either a new environment
(accepted) or a kernel exception (rejected). Nothing is added to the real
environment: this only asks the kernel for its verdict.
-/

namespace NoMagicCompile

open Lean Meta NoMagic

/-- Ask the kernel to check `decl`, and report its verdict. -/
def kernelVerdict (decl : Declaration) : MetaM MessageData := do
  match (← getEnv).toKernelEnv.addDecl (← getOptions) decl with
  | .ok _    => return m!"kernel accepted"
  | .error e => return m!"kernel rejected: {e.toMessageData (← getOptions)}"

/-- `2 * sumTo k`, built as a raw expression. -/
def twoTimesSumTo (k : Nat) : MetaM Expr :=
  mkAppM ``HMul.hMul #[toExpr (2 : Nat), mkApp (mkConst ``NoMagic.sumTo) (toExpr k)]

/-!
**1. The article's proof, straight to the kernel.** Take the stored proof term of
`two_mul_sumTo'` and resubmit it under a new name.
-/

run_meta do
  let some ci := (← getEnv).find? ``NoMagic.two_mul_sumTo' | throwError "missing"
  let decl := .thmDecl {
    name := `NoMagicCompile.viaKernel, levelParams := []
    type := ci.type, value := ci.value! (allowOpaque := true) }
  logInfo m!"{ci.type}\n{← kernelVerdict decl}"

/-!
**2. A false claim.** `2 * sumTo 3 = 13`, "proved" by `Eq.refl _`. The kernel
computes the left side and refuses.
-/

run_meta do
  let lhs ← twoTimesSumTo 3
  let type ← mkEq lhs (toExpr (13 : Nat))
  let decl := .thmDecl { name := `NoMagicCompile.bogus, levelParams := [], type, value := ← mkEqRefl lhs }
  logInfo m!"{type}\n{← kernelVerdict decl}"

/-!
**3. The true claim.** `2 * sumTo 3 = 12`, with the same one-word proof, is accepted.
-/

run_meta do
  let lhs ← twoTimesSumTo 3
  let type ← mkEq lhs (toExpr (12 : Nat))
  let decl := .thmDecl { name := `NoMagicCompile.honest, levelParams := [], type, value := ← mkEqRefl lhs }
  logInfo m!"{type}\n{← kernelVerdict decl}"

end NoMagicCompile
