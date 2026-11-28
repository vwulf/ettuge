import Lean
import MiniLean.DSL

/-!
# Explain: one stage at a time

Display commands that run one stage of MiniLean's pipeline and print what that
stage produced. They call the same functions the `mini_…` commands call
(`toRaw`, `Raw.toExpr`, `runTac`, `whnf`, `isDefEq`, `infer`), print the
intermediate results, and add nothing to the environment.

* `#mini_raw t`: the `Raw` tree that the DSL builds from Lean's syntax.
* `#mini_db t`: the `Expr` after name resolution, bound variables as de Bruijn indices.
* `#mini_tactics (binders) : statement := by …`: run a script one tactic at a
  time, showing each goal, the goals the tactic leaves, and the piece of proof
  term it contributes, with holes `?1`, `?2`, … for the goals still open.
* `#mini_defeq a =?= b`: the steps `isDefEq` takes to decide `a ≡ b`.
* `#mini_infer n t`: the kernel's typing derivation for `t`, `n` levels deep.

`#mini_defeq` and `#mini_infer` retrace `isDefEq` and `infer` to print their
steps, calling the real functions for every result they report. Nothing here is
trusted or needed for checking: `Checks.lean` pins the output, so a change to
the kernel that these pages no longer describe makes the build fail.
-/

namespace MiniLean.Explain

open Lean Elab Command MiniLean.DSL
open MiniLean (Raw Expr Goal Tac M pp)

/-! ## Trees -/

/-- An indented tree: a label and children, one per line. -/
inductive Tree where
  | node (label : String) (kids : List Tree)

instance : Inhabited Tree := ⟨.node "" []⟩

partial def Tree.render (t : Tree) (ind : String := "") : List String :=
  match t with
  | .node l ks => (ind ++ l) :: ks.flatMap (·.render (ind ++ "  "))

def levels (ls : List MiniLean.Level) : String :=
  ".{" ++ ", ".intercalate (ls.map toString) ++ "}"

partial def rawTree : Raw → Tree
  | .ident n none => .node ("ident " ++ n) []
  | .ident n (some ls) => .node ("ident " ++ n ++ levels ls) []
  | .app f a => .node "app" [rawTree f, rawTree a]
  | .lam x t b => .node ("lam " ++ x) [rawTree t, rawTree b]
  | .pi x t b => .node ("pi " ++ x) [rawTree t, rawTree b]
  | .sort l => .node ("sort " ++ toString l) []

partial def exprTree : Expr → Tree
  | .bvar i => .node ("bvar " ++ toString i) []
  | .fvar i => .node ("fvar " ++ toString i) []
  | .sort l => .node ("sort " ++ toString l) []
  | .const n [] => .node ("const " ++ n) []
  | .const n ls => .node ("const " ++ n ++ levels ls) []
  | .app f a => .node "app" [exprTree f, exprTree a]
  | .lam x t b => .node ("lam " ++ x) [exprTree t, exprTree b]
  | .pi x t b => .node ("pi " ++ x) [exprTree t, exprTree b]

/-- A `Raw` term written back as source, for printing tactics. -/
partial def Raw.src : Raw → String
  | .ident n none => n
  | .ident n (some ls) => n ++ levels ls
  | .app f a => Raw.src f ++ " " ++ atom a
  | .lam x t b => "λ (" ++ x ++ " : " ++ Raw.src t ++ ") => " ++ Raw.src b
  | .pi "_" t b => atom t ++ " → " ++ Raw.src b
  | .pi x t b => "∀ (" ++ x ++ " : " ++ Raw.src t ++ "), " ++ Raw.src b
  | .sort l => "Sort " ++ toString l
where
  atom (r : Raw) : String := match r with
    | .app .. | .lam .. | .pi .. => "(" ++ Raw.src r ++ ")"
    | _ => Raw.src r

partial def Tac.src : Tac → String
  | .intro x => "intro " ++ x
  | .exact t => "exact " ++ Raw.src t
  | .refl => "refl"
  | .show_ t => "show " ++ Raw.src t
  | .induction x => "induction " ++ x
  | .rw rs => "rw [" ++ ", ".intercalate (rs.map fun (rev, r) => (if rev then "← " else "") ++ Raw.src r) ++ "]"
  | .focus ts => "· " ++ "; ".intercalate (ts.map Tac.src)

/-! ## Syntax -/

syntax (name := miniRaw) "#mini_raw " mini_term : command
syntax (name := miniDb) "#mini_db " mini_term : command
syntax (name := miniTactics) "#mini_tactics " mini_binder* " : " mini_term " := " "by " miniTacticSeq : command
syntax (name := miniDefeq) "#mini_defeq " mini_term " =?= " mini_term : command
syntax (name := miniInfer) "#mini_infer " num ppSpace mini_term : command
syntax (name := miniKernel) "#mini_kernel " num ppSpace ident : command

@[command_elab miniRaw] def elabRaw : CommandElab := fun stx => do
  match stx with
  | `(#mini_raw $t) => logInfo ("\n".intercalate (rawTree (← toRaw t)).render)
  | _ => throwUnsupportedSyntax

@[command_elab miniDb] def elabDb : CommandElab := fun stx => do
  match stx with
  | `(#mini_db $t) => logInfo ("\n".intercalate (exprTree (← resolve stx (← toRaw t))).render)
  | _ => throwUnsupportedSyntax

/-! ## Tactics, one at a time -/

/-- A goal on one line: its locals, then `⊢` and the statement. -/
def goalLine (g : Goal) : M String := MiniLean.inGoal g do
  let mut ls : List String := []
  for l in g.locals.reverse do
    ls := ls ++ [s!"{l.name} : {← pp l.type}"]
  return ", ".intercalate ls ++ (if ls.isEmpty then "" else " ") ++ s!"⊢ {← pp g.target}"

/--
`MiniLean.solve`, with a record of each step. Each goal carries a label `?k`;
`next` is the next free label. Returns the proofs, the leftover tactics, the
next free label, and the record.
-/
partial def solveLog (opens : List MiniLean.Name) (ind : String) (next : Nat) :
    List Tac → List (Goal × Nat) → M (List Expr × List Tac × Nat × Array String)
  | tacs, [] => return ([], tacs, next, #[])
  | [], (g, _) :: _ => do throw s!"unsolved goal:\n{← g.fmt}"
  | t :: ts, (g, k) :: gs => do
    match t with
    | .focus inner =>
      let line := s!"{ind}· focus on ?{k}"
      let (ps, leftover, next, l1) ← solveLog opens (ind ++ "  ") next inner [(g, k)]
      unless leftover.isEmpty do throw "· : the goal was solved before the end of this block"
      let (rest, ts', next, l2) ← solveLog opens ind next ts gs
      return (ps[0]! :: rest, ts', next, #[line] ++ l1 ++ l2)
    | _ =>
      let (subgoals, build) ← MiniLean.runTac opens t g
      let labels := (List.range subgoals.length).map (next + ·)
      let holes := labels.map fun i => Expr.const s!"?{i}" []
      let piece ← MiniLean.inGoal g (pp (build holes))
      let mut lines := #[s!"{ind}{Tac.src t}", s!"{ind}  on    ?{k}  {← goalLine g}"]
      for (sg, i) in subgoals.zip labels do
        lines := lines.push s!"{ind}  new   ?{i}  {← goalLine sg}"
      if subgoals.isEmpty then lines := lines.push s!"{ind}  new   (none: ?{k} is closed)"
      lines := lines.push s!"{ind}  ?{k} := {piece}"
      let (subproofs, ts', next', l1) ← solveLog opens ind (next + subgoals.length) ts (subgoals.zip labels)
      let (restProofs, ts'', next'', l2) ← solveLog opens ind next' ts' gs
      return (build subproofs :: restProofs, ts'', next'', lines ++ l1 ++ l2)

@[command_elab miniTactics] def elabTactics : CommandElab := fun stx => do
  match stx with
  | `(#mini_tactics $bs* : $t := by $seq) =>
    let bs ← toBinders bs
    let type ← resolve stx (MiniLean.Raw.binders true bs (← toRaw t))
    -- as in `mini_theorem … := by`, the binders become `intro`s
    let tacs := bs.map (fun (x, _) => MiniLean.Tac.intro x) ++ (← toTacSeq seq)
    let s ← getState
    let out ← ok stx (← runM do
      let (ps, leftover, _, lines) ← solveLog s.opens "" 1 tacs [({ locals := [], target := type }, 0)]
      unless leftover.isEmpty do throw "all goals were solved before the end of the script"
      let header := s!"tactics: {"; ".intercalate (tacs.map Tac.src)}"
      return "\n".intercalate ([header, ""] ++ lines.toList ++ ["", s!"?0 := {← pp ps[0]!}"]))
    logInfo out
  | _ => throwUnsupportedSyntax

/-! ## Definitional equality, step by step -/

/-- `MiniLean.isDefEq`, retraced: the same steps, with a record of each. -/
partial def defeqLog (ind : String) (a b : Expr) : M (Bool × Array String) := do
  let mut lines := #[s!"{ind}{← pp a}  ≟  {← pp b}"]
  if a.eqv b then return (true, lines.push s!"{ind}  identical ✓")
  let a' ← MiniLean.whnf a
  let b' ← MiniLean.whnf b
  if !a'.eqv a then lines := lines.push s!"{ind}  whnf left   ⟶ {← pp a'}"
  if !b'.eqv b then lines := lines.push s!"{ind}  whnf right  ⟶ {← pp b'}"
  if a'.eqv b' then return (true, lines.push s!"{ind}  identical ✓")
  match a', b' with
  | .sort l, .sort m =>
    let r := MiniLean.Level.isEquiv l m
    return (r, lines.push s!"{ind}  universe levels {if r then "equal ✓" else "differ ✗"}")
  | .lam x t1 b1, .lam _ t2 b2 | .pi x t1 b1, .pi _ t2 b2 =>
    lines := lines.push s!"{ind}  both binders: compare the types, then the bodies"
    let (r1, l1) ← defeqLog (ind ++ "  ") t1 t2
    lines := lines ++ l1
    if !r1 then return (false, lines)
    MiniLean.withLocal x t1 fun v => do
      let (r2, l2) ← defeqLog (ind ++ "  ") (b1.instantiate1 v) (b2.instantiate1 v)
      return (r2, lines ++ l2)
  | _, _ =>
    let fa := a'.getAppFn
    let fb := b'.getAppFn
    let xs := a'.getAppArgs
    let ys := b'.getAppArgs
    let headsMatch := xs.size == ys.size && match fa, fb with
      | .fvar i, .fvar j => i == j
      | .const n ls, .const m ms => n == m && ls.length == ms.length &&
          (ls.zip ms).all fun (l, m) => MiniLean.Level.isEquiv l m
      | _, _ => false
    if !headsMatch then
      return (false, lines.push s!"{ind}  stuck, and the heads {← pp fa} and {← pp fb} differ ✗")
    lines := lines.push s!"{ind}  stuck; same head {← pp fa}: compare the {xs.size} arguments"
    for (x, y) in xs.zip ys do
      let (r, l) ← defeqLog (ind ++ "  ") x y
      lines := lines ++ l
      if !r then return (false, lines)
    return (true, lines)

@[command_elab miniDefeq] def elabDefeq : CommandElab := fun stx => do
  match stx with
  | `(#mini_defeq $a =?= $b) =>
    let a ← resolve stx (← toRaw a)
    let b ← resolve stx (← toRaw b)
    let out ← ok stx (← runM do
      discard <| MiniLean.infer a
      discard <| MiniLean.infer b
      let (r, lines) ← defeqLog "" a b
      -- the real `isDefEq` must agree with the record
      unless (← MiniLean.isDefEq a b) == r do throw "defeqLog disagrees with isDefEq"
      return "\n".intercalate lines.toList)
    logInfo out
  | _ => throwUnsupportedSyntax

/-! ## Type inference, step by step -/

/--
`MiniLean.infer`, retraced. An application `f a₁ … aₙ` is shown as its head
and arguments: `infer` handles it one argument at a time, so this is the same
work. `fuel` limits how deep the derivations of arguments are shown; below
that, an argument's type is reported without its derivation.
-/
partial def inferLog (fuel : Nat) (ind : String) (e : Expr) : M (Expr × Array String) := do
  match e with
  | .app .. =>
    let f := e.getAppFn
    let args := e.getAppArgs
    let tf ← MiniLean.infer f
    let mut lines := #[s!"{ind}{← pp e}", s!"{ind}  head  {← pp f} : {← pp tf}"]
    let mut t := tf
    for (a, i) in args.zipIdx do
      let t' ← MiniLean.whnf t
      let .pi _ d b := t' | throw "inferLog: not a function type"
      let (ta, la) ← if fuel > 0 && !(a matches .fvar _ | .const .. | .sort _)
        then inferLog (fuel - 1) (ind ++ "    ") a
        else return (← MiniLean.infer a, #[])
      lines := lines.push s!"{ind}  arg {i + 1}  {← pp a}"
      lines := lines ++ la
      lines := lines.push s!"{ind}    has type  {← pp ta}"
      lines := lines.push s!"{ind}    expected  {← pp d}"
      let same := ta.eqv d
      unless ← MiniLean.isDefEq ta d do throw "inferLog: argument has the wrong type"
      lines := lines.push s!"{ind}    {if same then "identical ✓" else "definitionally equal ✓"}"
      t := b.instantiate1 a
    lines := lines.push s!"{ind}  type  {← pp t}"
    return (t, lines)
  | .lam x ty b =>
    discard <| MiniLean.ensureSort ty
    MiniLean.withLocal x ty fun v => do
      let header := s!"{ind}λ ({x} : {← pp ty}) =>   open {x} as a free variable, infer the body"
      let (tb, lb) ← inferLog fuel (ind ++ "  ") (b.instantiate1 v)
      let res ← MiniLean.mkPi [v] tb
      return (res, #[header] ++ lb ++ #[s!"{ind}  type  {← pp res}"])
  | _ =>
    let t ← MiniLean.infer e
    return (t, #[s!"{ind}{← pp e} : {← pp t}"])

@[command_elab miniInfer] def elabInfer : CommandElab := fun stx => do
  match stx with
  | `(#mini_infer $n $t) =>
    let e ← resolve stx (← toRaw t)
    let out ← ok stx (← runM do
      let (ty, lines) ← inferLog n.getNat "" e
      -- the real `infer` must agree with the record
      unless ← MiniLean.isDefEq ty (← MiniLean.infer e) do throw "inferLog disagrees with infer"
      return "\n".intercalate lines.toList)
    logInfo out
  | _ => throwUnsupportedSyntax

/-- Replay `MiniLean.addTheorem`'s checks on an accepted theorem, with a record of each. -/
@[command_elab miniKernel] def elabKernel : CommandElab := fun stx => do
  match stx with
  | `(#mini_kernel $n $x) =>
    let name := nameOf x
    let some (.thm lps type proof) := (← getState).env.find? name
      | throwErrorAt x s!"'{name}' is not a theorem"
    let out ← ok stx (← runM do
      let mut lines := #[s!"addTheorem {name}"]
      lines := lines.push s!"1. checkFresh: no earlier declaration is named {name}"
      lines := lines.push s!"2. checkLevelParams: universe parameters {lps}, none undeclared"
      let l ← MiniLean.ensureSort type
      lines := lines.push s!"3. ensureSort statement: {← pp type} : Sort {l}"
      lines := lines.push s!"   level {l} is 0, so the statement is a proposition ✓"
      lines := lines.push "4. check proof statement: infer the proof's type"
      let (ty, lp) ← inferLog n.getNat "   " proof
      lines := lines ++ lp
      lines := lines.push "5. isDefEq (inferred type) (statement)"
      let (r, ld) ← defeqLog "   " ty type
      unless r && (← MiniLean.isDefEq ty type) do throw "the proof does not have the statement's type"
      lines := lines ++ ld
      lines := lines.push s!"6. env.add {name} (theorem: its proof is never unfolded)"
      return "\n".intercalate lines.toList)
    logInfo out
  | _ => throwUnsupportedSyntax

end MiniLean.Explain
