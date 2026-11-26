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

-- 1. The stored proof term of `two_mul_sumTo'`, resubmitted under a new name.
/--
info: ∀ (n : Nat), 2 * sumTo n = n * (n + 1)
kernel accepted
-/
#guard_msgs in
run_meta do
  let some ci := (← getEnv).find? ``NoMagic.two_mul_sumTo' | throwError "missing"
  let decl := .thmDecl {
    name := `NoMagicCompile.viaKernel, levelParams := []
    type := ci.type, value := ci.value! (allowOpaque := true) }
  logInfo m!"{ci.type}\n{← kernelVerdict decl}"

-- 2. A false claim, `2 * sumTo 3 = 13`, "proved" by `Eq.refl _`.
/--
info: 2 * sumTo 3 = 13
kernel rejected: (kernel) declaration type mismatch, 'NoMagicCompile.bogus' has type
  2 * sumTo 3 = 2 * sumTo 3
but it is expected to have type
  2 * sumTo 3 = 13
-/
#guard_msgs in
run_meta do
  let lhs ← twoTimesSumTo 3
  let type ← mkEq lhs (toExpr (13 : Nat))
  let decl := .thmDecl { name := `NoMagicCompile.bogus, levelParams := [], type, value := ← mkEqRefl lhs }
  logInfo m!"{type}\n{← kernelVerdict decl}"

-- 3. The true claim `2 * sumTo 3 = 12`, with the same one-word proof.
/--
info: 2 * sumTo 3 = 12
kernel accepted
-/
#guard_msgs in
run_meta do
  let lhs ← twoTimesSumTo 3
  let type ← mkEq lhs (toExpr (12 : Nat))
  let decl := .thmDecl { name := `NoMagicCompile.honest, levelParams := [], type, value := ← mkEqRefl lhs }
  logInfo m!"{type}\n{← kernelVerdict decl}"

end NoMagicCompile
