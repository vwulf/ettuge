import MiniLean.Surface

/-!
# Tactics

A tactic turns one goal into zero or more new goals, plus a way to build a
proof of the old goal from proofs of the new ones. Running a script fills in
the whole proof term, which is then handed to the kernel like any other term.
Tactics are *not* trusted: a buggy tactic can fail, or build a wrong term, but
the kernel will reject a wrong term.

The tactics are `intro`, `exact`, `refl`, `show`, `induction` and `rw`, plus
`·` to focus on one goal. `refl`, `rw` and `induction` rely on the prelude's
names: `Eq`, `Eq.refl`, `Eq.rec`, and `I.rec` for an inductive type `I`.
-/

namespace MiniLean

/-- A goal: the locals in scope (newest first) and the statement to prove. -/
structure Goal where
  locals : List Local
  target : Expr

inductive Tac where
  | intro (x : Name)
  | exact (t : Raw)
  | refl
  | show_ (t : Raw)
  | induction (x : Name)
  | rw (rules : List (Bool × Raw))   -- `true` means right-to-left (`← h`)
  | focus (tacs : List Tac)
  deriving Inhabited

/-- A proof builder: given proofs of the new goals, a proof of the old one. -/
abbrev Builder := List Expr → Expr

def inGoal (g : Goal) (x : M α) : M α := withReader (fun c => { c with locals := g.locals }) x

def Goal.fmt (g : Goal) : M String := inGoal g do
  let mut lines : List String := []
  for l in g.locals.reverse do
    lines := lines ++ [s!"{l.name} : {← pp l.type}"]
  return "\n".intercalate (lines ++ [s!"⊢ {← pp g.target}"])

def elabIn (g : Goal) (opens : List Name) (t : Raw) : M Expr := do
  let sc : Scope := { env := ← getEnv, locals := g.locals, opens }
  match t.toExpr sc [] with
  | .ok e => return e
  | .error msg => throw msg

/-- If `t` reduces to `Eq.{u} α a b`, return `(u, α, a, b)`. -/
def asEq? (t : Expr) : M (Option (Level × Expr × Expr × Expr)) := do
  let t ← whnf t
  match t.getAppFn, t.getAppArgs with
  | .const "Eq" [u], #[α, a, b] => return some (u, α, a, b)
  | _, _ => return none

def mkEq (u : Level) (α a b : Expr) : Expr := Expr.mkAppN (.const "Eq" [u]) #[α, a, b]

/-! ## Matching and abstraction, for `rw` -/

/-- One-way matching: find values for the pattern variables `mvars` that make `p` equal to `t`. -/
partial def matchPattern (mvars : List Nat) (p t : Expr) (σ : List (Nat × Expr)) :
    Option (List (Nat × Expr)) :=
  match p, t with
  | .fvar id, _ =>
    if mvars.contains id then
      if t.hasLooseBVars 0 then none
      else match σ.lookup id with
        | some v => if v.eqv t then some σ else none
        | none => some ((id, t) :: σ)
    else if let .fvar j := t then (if j == id then some σ else none) else none
  | .app f a, .app g b => matchPattern mvars f g σ >>= matchPattern mvars a b
  | .lam _ pt pb, .lam _ tt tb | .pi _ pt pb, .pi _ tt tb =>
    matchPattern mvars pt tt σ >>= matchPattern mvars pb tb
  | _, _ => if p.eqv t then some σ else none

/-- The first subterm of `t` (outermost first, left to right) that matches `p`. -/
partial def findMatch (mvars : List Nat) (p t : Expr) : Option (List (Nat × Expr)) :=
  (if t.hasLooseBVars 0 then none else matchPattern mvars p t []) <|>
  match t with
  | .app f a => findMatch mvars p f <|> findMatch mvars p a
  | .lam _ ty b | .pi _ ty b => findMatch mvars p ty <|> findMatch mvars p b
  | _ => none

partial def replaceFVars (σ : List (Nat × Expr)) : Expr → Expr
  | .fvar id => (σ.lookup id).getD (.fvar id)
  | .app f a => .app (replaceFVars σ f) (replaceFVars σ a)
  | .lam x t b => .lam x (replaceFVars σ t) (replaceFVars σ b)
  | .pi x t b => .pi x (replaceFVars σ t) (replaceFVars σ b)
  | e => e

/-- Replace every occurrence of the (locally closed) term `s` in `t` by `bvar d`, `d` binders deep. -/
partial def abstractTerm (s : Expr) (d : Nat) (t : Expr) : Expr :=
  if !t.hasLooseBVars 0 && t.eqv s then .bvar d
  else match t with
    | .app f a => .app (abstractTerm s d f) (abstractTerm s d a)
    | .lam x ty b => .lam x (abstractTerm s d ty) (abstractTerm s (d + 1) b)
    | .pi x ty b => .pi x (abstractTerm s d ty) (abstractTerm s (d + 1) b)
    | e => e

/-! ## The tactics -/

/-- Close the goal by `refl` if it is an equation whose sides are definitionally equal. -/
def tryRefl (g : Goal) : M (Option Expr) := inGoal g do
  let some (u, α, a, b) ← asEq? g.target | return none
  if ← isDefEq a b then return some (Expr.mkAppN (.const "Eq.refl" [u]) #[α, a]) else return none

/-- Rewrite with one equation. Returns the new goal, or none if `refl` closed it. -/
partial def rwOne (opens : List Name) (g : Goal) (rev : Bool) (rule : Raw) : M (Option Goal × Builder) := inGoal g do
  let h ← elabIn g opens rule
  -- Leading ∀s of the rule's statement become pattern variables.
  let rec openRule (t : Expr) (mvs : List Nat) : M (List Nat × Expr) := do
    match ← whnf t with
    | .pi _ _ b => let id ← fresh; openRule (b.instantiate1 (.fvar id)) (mvs ++ [id])
    | t' => return (mvs, t')
  let (mvars, stmt) ← openRule (← infer h) []
  let some (u, α, l, r) ← asEq? stmt | throw s!"rw: '{← pp h}' is not an equation"
  let (src, dst) := if rev then (r, l) else (l, r)
  let some σ := findMatch mvars src g.target
    | throw s!"rw: did not find an instance of\n  {← pp src}\nin the goal\n  {← pp g.target}"
  for m in mvars do
    if (σ.lookup m).isNone then throw "rw: could not determine all the arguments of the rule"
  let inst := replaceFVars σ
  let hInst := Expr.mkAppN h (mvars.map (fun m => (σ.lookup m).get!)).toArray
  let (α, l, r, src, dst) := (inst α, inst l, inst r, inst src, inst dst)
  -- motive body: the goal with each occurrence of `src` replaced by a bound variable
  let body := abstractTerm src 0 g.target
  let newTarget := body.instantiate1 dst
  -- λ (b : α) (_ : Eq α a b), body[b]
  let mkMotive (a : Expr) : M Expr :=
    withLocal "b" α fun b => withLocal "h" (mkEq u α a b) fun hb => mkLam [b, hb] (body.instantiate1 b)
  let eqRec (a motive minor b proof : Expr) : Expr :=
    Expr.mkAppN (.const "Eq.rec" [.zero, u]) #[α, a, motive, minor, b, proof]
  let builder : Builder ← if rev then do
      -- h : l = r, goal mentions r; new goal mentions l. Transport along h: motive l → motive r.
      let motive ← mkMotive l
      pure fun ps => eqRec l motive ps[0]! r hInst
    else do
      -- h : l = r, goal mentions l; new goal mentions r. Transport along (symm h): motive r → motive l.
      let symmMotive ← withLocal "b" α fun b => withLocal "h" (mkEq u α l b) fun hb =>
        mkLam [b, hb] (mkEq u α b l)
      let symmH := eqRec l symmMotive (Expr.mkAppN (.const "Eq.refl" [u]) #[α, l]) r hInst
      let motive ← mkMotive r
      pure fun ps => eqRec r motive ps[0]! l symmH
  let g' : Goal := { g with target := newTarget }
  match ← tryRefl g' with
  | some p => return (none, fun _ => builder [p])
  | none => return (some g', builder)

mutual

/-- Run one tactic on one goal. -/
partial def runTac (opens : List Name) (t : Tac) (g : Goal) : M (List Goal × Builder) := inGoal g do
  match t with
  | .intro x =>
    let .pi _ d b ← whnf g.target | throw s!"intro: the goal is not a ∀ or →\n{← g.fmt}"
    let id ← fresh
    let g' : Goal := { locals := ⟨id, x, d⟩ :: g.locals, target := b.instantiate1 (.fvar id) }
    return ([g'], fun ps => .lam x d (ps[0]!.abstract1 id))
  | .exact raw =>
    let e ← elabIn g opens raw
    check e g.target
    return ([], fun _ => e)
  | .refl =>
    match ← tryRefl g with
    | some p => return ([], fun _ => p)
    | none => throw s!"refl: the two sides are not definitionally equal\n{← g.fmt}"
  | .show_ raw =>
    let t ← elabIn g opens raw
    unless ← isDefEq t g.target do
      throw s!"show: '{← pp t}' is not definitionally equal to the goal\n{← g.fmt}"
    return ([{ g with target := t }], fun ps => ps[0]!)
  | .induction x =>
    let some l := g.locals.find? (·.name == x) | throw s!"induction: no local named '{x}'"
    for other in g.locals do
      if other.id != l.id && other.type.hasFVar l.id then
        throw s!"induction: '{other.name}' depends on '{x}' (not supported)"
    let ty ← whnf l.type
    let .const ind ls := ty.getAppFn | throw s!"induction: '{x}' does not have an inductive type"
    let some (.induct _ _ np ni _) := (← getEnv).find? ind
      | throw s!"induction: '{x}' does not have an inductive type"
    if ni != 0 then throw "induction: inductive families with indices are not supported"
    let some (.recursor _ _ _ _ _ ctors largeElim) := (← getEnv).find? (ind ++ ".rec")
      | throw s!"induction: no recursor for '{ind}'"
    let lvl ← ensureSort g.target
    if !largeElim && !lvl.isZero then throw s!"induction: '{ind}' can only be eliminated into Prop"
    let recLevels := if largeElim then lvl :: ls else ls
    let params := ty.getAppArgs
    let motive := Expr.lam x l.type (g.target.abstract1 l.id)
    let recHead := Expr.mkAppN (.const (ind ++ ".rec") recLevels) (params.push motive)
    -- the minor premises' types are the new goals
    let mut t ← whnf (← infer recHead)
    let mut goals : List Goal := []
    let others := g.locals.filter (·.id != l.id)
    for _ in ctors do
      let .pi _ d b := t | throw "induction: unexpected recursor type"
      goals := goals ++ [{ locals := others, target := d.betaAll }]
      t := b.instantiate1 (.sort .zero)  -- minor premises are independent of each other
    return (goals, fun ps => Expr.mkAppN recHead (ps.toArray.push (.fvar l.id)))
  | .rw rules =>
    match rules with
    | [] => return ([g], fun ps => ps[0]!)
    | (rev, r) :: rest =>
      let (g'?, b1) ← rwOne opens g rev r
      match g'? with
      | none =>
        if rest.isEmpty then return ([], b1)
        else throw "rw: the goal was closed by refl before the remaining rules"
      | some g' =>
        let (gs, b2) ← runTac opens (.rw rest) g'
        return (gs, fun ps => b1 [b2 ps])
  | .focus tacs =>
    let (ps, leftover) ← solve opens tacs [g]
    unless leftover.isEmpty do throw "· : the goal was solved before the end of this block"
    return ([], fun _ => ps[0]!)

/--
Run a script against a list of goals, depth first: each tactic acts on the
first open goal, and the goals it creates are solved before the next one.
Returns the proofs and any tactics left over.
-/
partial def solve (opens : List Name) : List Tac → List Goal → M (List Expr × List Tac)
  | tacs, [] => return ([], tacs)
  | [], g :: _ => do throw s!"unsolved goal:\n{← g.fmt}"
  | t :: ts, g :: gs => do
    let (subgoals, build) ← runTac opens t g
    let (subproofs, ts') ← solve opens ts subgoals
    let (restProofs, ts'') ← solve opens ts' gs
    return (build subproofs :: restProofs, ts'')

end

/-- Prove `target` with a tactic script, returning the proof term. -/
def prove (opens : List Name) (target : Expr) (tacs : List Tac) : M Expr := do
  let (ps, leftover) ← solve opens tacs [{ locals := [], target }]
  unless leftover.isEmpty do throw "all goals were solved before the end of the script"
  return ps[0]!

end MiniLean
