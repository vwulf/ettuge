import Lean
import MiniLean.Tactic

/-!
# The DSL

Lean 4 commands for writing MiniLean declarations:

* `mini_inductive I.{u…} (params…) : type where | c : type …`
* `mini_def f.{u…} (binders…) : type := term`
* `mini_theorem t (binders…) : statement := term` (or `:= by tactics`)
* `mini_open I`: let `I.c` be written `c`
* `#mini_check term`, `#mini_reduce term`, `#mini_print name`
* `#mini_verdict (binders…) : statement := term`: report MiniLean's verdict
  without failing the build

Lean's parser reads the syntax, and this file turns it into `MiniLean.Raw`.
Everything after that is MiniLean's own: `Raw.toExpr` resolves names, the
tactics build a term, and the kernel decides. If the kernel rejects a
declaration, the Lean build fails at that line.

The MiniLean environment lives in a Lean environment extension. It is not
saved between files, so a development that uses these commands lives in a
single file.
-/

namespace MiniLean.DSL

open Lean Elab Command

structure State where
  env : MiniLean.Env := {}
  opens : List MiniLean.Name := []
  deriving Inhabited

initialize stateExt : EnvExtension State ← registerEnvExtension (pure {})

def getState : CommandElabM State := return stateExt.getState (← Lean.getEnv)
def setState (s : State) : CommandElabM Unit := modifyEnv (stateExt.setState · s)

/-! ## Syntax -/

declare_syntax_cat mini_level
syntax num : mini_level
syntax ident : mini_level

declare_syntax_cat mini_term
declare_syntax_cat mini_binder

syntax "(" ident+ " : " mini_term ")" : mini_binder

syntax ident : mini_term
syntax ident noWs ".{" mini_level,* "}" : mini_term
syntax "(" mini_term ")" : mini_term
syntax "Prop" : mini_term
syntax "Type" : mini_term
syntax "Sort " mini_level : mini_term
syntax:10 mini_term:10 colGt mini_term:11 : mini_term
syntax:5 mini_term:6 " → " mini_term:5 : mini_term
syntax "λ " mini_binder+ " => " mini_term : mini_term
syntax "∀ " mini_binder+ ", " mini_term : mini_term

declare_syntax_cat mini_tactic (behavior := both)
declare_syntax_cat mini_rw_rule
syntax mini_term : mini_rw_rule
syntax "← " mini_term : mini_rw_rule

syntax miniTacticSeq := sepByIndentSemicolon(mini_tactic)

syntax "intro" (ppSpace colGt ident)+ : mini_tactic
syntax "exact " mini_term : mini_tactic
syntax &"refl" : mini_tactic
syntax "show " mini_term : mini_tactic
syntax "induction " ident : mini_tactic
syntax "rw " "[" mini_rw_rule,* "]" : mini_tactic
syntax "· " miniTacticSeq : mini_tactic

syntax (name := miniInductive) "mini_inductive " ident (".{" ident,* "}")? mini_binder* " : " mini_term
  " where" ("| " ident " : " mini_term)* : command
syntax (name := miniDef) "mini_def " ident (".{" ident,* "}")? mini_binder* " : " mini_term
  " := " mini_term : command
syntax (name := miniTheoremBy) "mini_theorem " ident mini_binder* " : " mini_term
  " := " "by " miniTacticSeq : command
syntax (name := miniTheorem) "mini_theorem " ident mini_binder* " : " mini_term
  " := " mini_term : command
syntax (name := miniOpen) "mini_open " ident : command
syntax (name := miniCheck) "#mini_check " mini_term : command
syntax (name := miniReduce) "#mini_reduce " mini_term : command
syntax (name := miniPrint) "#mini_print " ident : command
syntax (name := miniVerdict) "#mini_verdict " mini_binder* " : " mini_term " := " mini_term : command

/-! ## From syntax to `Raw` -/

def nameOf (x : TSyntax `ident) : MiniLean.Name := x.getId.toString

def elabLevel : TSyntax `mini_level → CommandElabM MiniLean.Level
  | `(mini_level| $n:num) => pure (MiniLean.Level.ofNat n.getNat)
  | `(mini_level| $x:ident) => pure (.param (nameOf x))
  | stx => throwErrorAt stx "unsupported universe level"

mutual

partial def toRaw : TSyntax `mini_term → CommandElabM MiniLean.Raw
  | `(mini_term| $x:ident) => pure (.ident (nameOf x) none)
  | `(mini_term| $x:ident.{$ls,*}) => do
    return .ident (nameOf x) (some (← ls.getElems.toList.mapM elabLevel))
  | `(mini_term| ($t)) => toRaw t
  | `(mini_term| Prop) => pure (.sort .zero)
  | `(mini_term| Type) => pure (.sort (.succ .zero))
  | `(mini_term| Sort $l) => return .sort (← elabLevel l)
  | `(mini_term| $f $a) => return .app (← toRaw f) (← toRaw a)
  | `(mini_term| $a → $b) => return .pi "_" (← toRaw a) (← toRaw b)  -- "_" cannot be written, so it never captures a name
  | `(mini_term| λ $bs* => $b) => return MiniLean.Raw.binders false (← toBinders bs) (← toRaw b)
  | `(mini_term| ∀ $bs*, $b) => return MiniLean.Raw.binders true (← toBinders bs) (← toRaw b)
  | stx => throwErrorAt stx "unsupported MiniLean term"

partial def toBinders (bs : Array (TSyntax `mini_binder)) :
    CommandElabM (List (MiniLean.Name × MiniLean.Raw)) := do
  let mut out := []
  for b in bs do
    match b with
    | `(mini_binder| ($xs:ident* : $t)) =>
      let t ← toRaw t
      for x in xs do out := out ++ [(nameOf x, t)]
    | _ => throwErrorAt b "unsupported binder"
  return out

end

mutual

partial def toTacs (stx : TSyntax `mini_tactic) : CommandElabM (List MiniLean.Tac) := do
  match stx with
  | `(mini_tactic| intro $xs*) => return xs.toList.map fun x => .intro (nameOf x)
  | `(mini_tactic| exact $t) => return [.exact (← toRaw t)]
  | `(mini_tactic| refl) => return [.refl]
  | `(mini_tactic| show $t) => return [.show_ (← toRaw t)]
  | `(mini_tactic| induction $x) => return [.induction (nameOf x)]
  | `(mini_tactic| rw [$rs,*]) =>
    let rules ← rs.getElems.toList.mapM fun (r : TSyntax `mini_rw_rule) => do
      match r with
      | `(mini_rw_rule| ← $t) => return (true, ← toRaw t)
      | `(mini_rw_rule| $t:mini_term) => return (false, ← toRaw t)
      | _ => throwErrorAt r "unsupported rewrite rule"
    return [.rw rules]
  | `(mini_tactic| · $seq) => return [.focus (← toTacSeq seq)]
  | _ => throwErrorAt stx "unsupported MiniLean tactic"

partial def toTacSeq (seq : TSyntax ``miniTacticSeq) : CommandElabM (List MiniLean.Tac) := do
  let tacs := seq.raw[0]!.getSepArgs
  tacs.toList.flatMapM fun t => toTacs ⟨t⟩

end

/-! ## Running the kernel -/

def runM (x : MiniLean.M α) : CommandElabM (Except String α) := do
  return MiniLean.M.run (← getState).env x

def ok (stx : Syntax) : Except String α → CommandElabM α
  | .ok a => pure a
  | .error msg => throwErrorAt stx msg

def resolve (stx : Syntax) (r : MiniLean.Raw)
    (pending : Option (MiniLean.Name × List MiniLean.Level) := none) : CommandElabM MiniLean.Expr := do
  let s ← getState
  ok stx (r.toExpr { env := s.env, opens := s.opens, pending } [])

def toLps (us : Option (Array (TSyntax `ident))) : List MiniLean.Name :=
  (us.getD #[]).toList.map nameOf

/-! ## Commands -/

@[command_elab miniInductive] def elabInductive : CommandElab := fun stx => do
  match stx with
  | `(mini_inductive $n $[.{$us,*}]? $bs* : $t where $[| $cs:ident : $cts]*) =>
    let name := nameOf n
    let lps := toLps (us.map (·.getElems))
    let params ← toBinders bs
    let pending := some (name, lps.map MiniLean.Level.param)
    let type ← resolve stx (MiniLean.Raw.binders true params (← toRaw t)) pending
    let mut ctors := #[]
    for (c, ct) in cs.zip cts do
      let ty ← resolve c (MiniLean.Raw.binders true params (← toRaw ct)) pending
      ctors := ctors.push (name ++ "." ++ nameOf ⟨c⟩, ty)
    let s ← getState
    let env ← ok stx (MiniLean.addInductive s.env name lps params.length type ctors.toList)
    setState { s with env }
  | _ => throwUnsupportedSyntax

@[command_elab miniDef] def elabDef : CommandElab := fun stx => do
  match stx with
  | `(mini_def $n $[.{$us,*}]? $bs* : $t := $v) =>
    let bs ← toBinders bs
    let type ← resolve stx (MiniLean.Raw.binders true bs (← toRaw t))
    let value ← resolve stx (MiniLean.Raw.binders false bs (← toRaw v))
    let s ← getState
    let env ← ok stx (MiniLean.addDefinition s.env (nameOf n) (toLps (us.map (·.getElems))) type value)
    setState { s with env }
  | _ => throwUnsupportedSyntax

@[command_elab miniTheorem] def elabTheorem : CommandElab := fun stx => do
  match stx with
  | `(mini_theorem $n $bs* : $t := $p) =>
    let bs ← toBinders bs
    let type ← resolve stx (MiniLean.Raw.binders true bs (← toRaw t))
    let proof ← resolve stx (MiniLean.Raw.binders false bs (← toRaw p))
    let s ← getState
    let env ← ok stx (MiniLean.addTheorem s.env (nameOf n) [] type proof)
    setState { s with env }
  | _ => throwUnsupportedSyntax

@[command_elab miniTheoremBy] def elabTheoremBy : CommandElab := fun stx => do
  match stx with
  | `(mini_theorem $n $bs* : $t := by $seq) =>
    let bs ← toBinders bs
    let type ← resolve stx (MiniLean.Raw.binders true bs (← toRaw t))
    -- the binders before the colon are introduced automatically, as in Lean
    let tacs := bs.map (fun (x, _) => MiniLean.Tac.intro x) ++ (← toTacSeq seq)
    let s ← getState
    let proof ← ok stx (← runM (MiniLean.prove s.opens type tacs))
    -- the tactics' proof term goes to the kernel like any other
    let env ← ok stx (MiniLean.addTheorem s.env (nameOf n) [] type proof)
    setState { s with env }
  | _ => throwUnsupportedSyntax

@[command_elab miniOpen] def elabOpen : CommandElab := fun stx => do
  match stx with
  | `(mini_open $n) =>
    let s ← getState
    setState { s with opens := s.opens ++ [nameOf n] }
  | _ => throwUnsupportedSyntax

@[command_elab miniCheck] def elabCheck : CommandElab := fun stx => do
  match stx with
  | `(#mini_check $t) =>
    let e ← resolve stx (← toRaw t)
    let msg ← ok stx (← runM do return s!"{← MiniLean.pp e} : {← MiniLean.pp (← MiniLean.infer e)}")
    logInfo msg
  | _ => throwUnsupportedSyntax

/-- Full normal form: reduce the head, then everything under it. -/
partial def nf (e : MiniLean.Expr) : MiniLean.M MiniLean.Expr := do
  let e ← MiniLean.whnf e
  match e with
  | .lam x t b => MiniLean.withLocal x t fun v => do MiniLean.mkLam [v] (← nf (b.instantiate1 v))
  | .pi x t b => do
    let t ← nf t
    MiniLean.withLocal x t fun v => do MiniLean.mkPi [v] (← nf (b.instantiate1 v))
  | _ => return MiniLean.Expr.mkAppN e.getAppFn (← e.getAppArgs.mapM nf)

@[command_elab miniReduce] def elabReduce : CommandElab := fun stx => do
  match stx with
  | `(#mini_reduce $t) =>
    let e ← resolve stx (← toRaw t)
    let msg ← ok stx (← runM do
      discard <| MiniLean.infer e
      MiniLean.pp (← nf e))
    logInfo msg
  | _ => throwUnsupportedSyntax

@[command_elab miniPrint] def elabPrint : CommandElab := fun stx => do
  match stx with
  | `(#mini_print $n) =>
    let s ← getState
    let some c := s.env.find? (nameOf n) | throwErrorAt n s!"unknown MiniLean constant '{nameOf n}'"
    let msg ← ok stx (← runM do
      let header := s!"{c.kind} {nameOf n}" ++
        (if c.lps.isEmpty then "" else ".{" ++ ", ".intercalate c.lps ++ "}")
      let ty := s!"{header} : {← MiniLean.pp c.type}"
      match c with
      | .defn _ _ v | .thm _ _ v => return s!"{ty} :=\n  {← MiniLean.pp v}"
      | _ => return ty)
    logInfo msg
  | _ => throwUnsupportedSyntax

@[command_elab miniVerdict] def elabVerdict : CommandElab := fun stx => do
  match stx with
  | `(#mini_verdict $bs* : $t := $p) =>
    let bs ← toBinders bs
    let type ← resolve stx (MiniLean.Raw.binders true bs (← toRaw t))
    let proof ← resolve stx (MiniLean.Raw.binders false bs (← toRaw p))
    let s ← getState
    match MiniLean.addTheorem s.env "_verdict" [] type proof with
    | .ok _ => logInfo "MiniLean's kernel accepts it"
    | .error msg => logInfo s!"MiniLean's kernel rejects it: {msg}"
  | _ => throwUnsupportedSyntax

end MiniLean.DSL
