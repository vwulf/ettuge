import MiniLean.Env

/-!
# The kernel

Everything in this file is trusted. It decides whether a declaration may join
the environment, and nothing else can add one.

* `whnf` reduces a term until its head can't be reduced: β (apply a λ),
  δ (unfold a definition) and ι (run a recursor on a constructor).
* `isDefEq` decides definitional equality: reduce both sides, then compare.
* `infer` computes a term's type, one case per typing rule, and fails on an
  ill-typed term.
* `addDefinition`, `addTheorem` and `addInductive` check a declaration and
  extend the environment.
-/

namespace MiniLean

/-- A free variable the checker has introduced, with its type. -/
structure Local where
  id : Nat
  name : Name
  type : Expr

structure Ctx where
  env : Env
  locals : List Local := []

/-- The kernel's monad: read the environment and locals, count fresh ids, fail with a message. -/
abbrev M := ReaderT Ctx (StateT Nat (Except String))

def M.run (env : Env) (x : M α) (locals : List Local := []) (nextId : Nat := 0) : Except String α :=
  (ReaderT.run x ({ env := env, locals := locals } : Ctx)).run' nextId

def getEnv : M Env := return (← read).env

def fresh : M Nat := modifyGet fun n => (n, n + 1)

/-- Run `k` with a new free variable `x : ty` in scope. -/
def withLocal (x : Name) (ty : Expr) (k : Expr → M α) : M α := do
  let id ← fresh
  withReader (fun c => { c with locals := ⟨id, x, ty⟩ :: c.locals }) (k (.fvar id))

def localName (id : Nat) : M String := do
  return ((← read).locals.find? (·.id == id)).map (·.name) |>.getD s!"?{id}"

/-- Print a term, naming free variables after the locals in scope. -/
def pp (e : Expr) : M String := do
  let ls := (← read).locals
  return e.fmt (fun id => (ls.find? (·.id == id)).map (·.name) |>.getD s!"?{id}") []

/-- Close the free variables `fvars` (outermost first) into Π- or λ-binders around `body`. -/
def mkBinders (isPi : Bool) (fvars : List Expr) (body : Expr) : M Expr := do
  let ls := (← read).locals
  fvars.foldrM (init := body) fun fv acc => do
    let .fvar id := fv | throw "mkBinders: not a free variable"
    let some l := ls.find? (·.id == id) | throw "mkBinders: unknown free variable"
    let b := acc.abstract1 id
    return if isPi then .pi l.name l.type b else .lam l.name l.type b

def mkPi := mkBinders true
def mkLam := mkBinders false

/-! ## Reduction -/

mutual

/-- Weak head normal form: reduce the head of `e` by β, δ and ι until none applies. -/
partial def whnf (e : Expr) : M Expr := do
  match e.getAppFn with
  | .lam _ _ body =>
    let args := e.getAppArgs
    if h : 0 < args.size then
      -- β: (λ x, b) a  ⟶  b[a/x]
      whnf (Expr.mkAppN (body.instantiate1 args[0]) (args.extract 1 args.size))
    else return e
  | .const n ls =>
    match (← getEnv).find? n with
    | some (.defn lps _ v) =>
      -- δ: unfold a definition
      whnf (Expr.mkAppN (v.instantiateLevels lps ls) e.getAppArgs)
    | some (.recursor _ _ ind np ni ctors _) =>
      match ← iota? n ls ind np ni ctors e.getAppArgs with
      | some e' => whnf e'
      | none => return e
    | _ => return e
  | _ => return e

/--
ι: a recursor applied to a constructor. The recursor's arguments are, in order,
the parameters, the motive, one minor premise per constructor, the indices and
the major premise. If the major premise reduces to constructor `c` applied to
fields `f₁ … fₖ`, the result is `c`'s minor premise applied to the fields and
then to the recursive results ("induction hypotheses") for the fields whose
type is the inductive type itself.
-/
partial def iota? (recName : Name) (ls : List Level) (ind : Name) (np ni : Nat)
    (ctors : List Name) (args : Array Expr) : M (Option Expr) := do
  let nMinors := ctors.length
  let majorIdx := np + 1 + nMinors + ni
  if args.size ≤ majorIdx then return none
  let major ← whnf args[majorIdx]!
  let .const cn cls := major.getAppFn | return none
  let some (.ctor clps cty cind cidx _ nf) := (← getEnv).find? cn | return none
  if cind != ind then return none
  let margs := major.getAppArgs
  if margs.size != np + nf then return none
  let params := args.extract 0 np
  let motive := args[np]!
  let minors := args.extract (np + 1) (np + 1 + nMinors)
  let fields := margs.extract np margs.size
  -- Walk the constructor's type to find which fields are recursive.
  let mut t := cty.instantiateLevels clps cls
  for p in params do
    match t with
    | .pi _ _ b => t := b.instantiate1 p
    | _ => throw "iota: malformed constructor type"
  let mut ihs : Array Expr := #[]
  for f in fields do
    match t with
    | .pi _ d b =>
      if let .const dn _ := d.getAppFn then
        if dn == ind then
          let dargs := d.getAppArgs
          let idx := dargs.extract np dargs.size
          ihs := ihs.push <| Expr.mkAppN (.const recName ls) (params ++ #[motive] ++ minors ++ idx ++ #[f])
      t := b.instantiate1 f
    | _ => throw "iota: malformed constructor type"
  let rest := args.extract (majorIdx + 1) args.size
  return some <| Expr.mkAppN (Expr.mkAppN minors[cidx]! (fields ++ ihs)) rest

end

/-- Definitional equality: equal after reduction. -/
partial def isDefEq (a b : Expr) : M Bool := do
  if a.eqv b then return true
  let a ← whnf a
  let b ← whnf b
  if a.eqv b then return true
  match a, b with
  | .sort l, .sort m => return Level.isEquiv l m
  | .lam x t1 b1, .lam _ t2 b2 | .pi x t1 b1, .pi _ t2 b2 =>
    if !(← isDefEq t1 t2) then return false
    withLocal x t1 fun v => isDefEq (b1.instantiate1 v) (b2.instantiate1 v)
  | _, _ =>
    -- Both are stuck: compare heads, then arguments one by one.
    let fa := a.getAppFn
    let fb := b.getAppFn
    let xs := a.getAppArgs
    let ys := b.getAppArgs
    if xs.size != ys.size then return false
    let headsMatch := match fa, fb with
      | .fvar i, .fvar j => i == j
      | .const n ls, .const m ms => n == m && ls.length == ms.length &&
          (ls.zip ms).all fun (l, m) => Level.isEquiv l m
      | _, _ => false
    if !headsMatch then return false
    for (x, y) in xs.zip ys do
      if !(← isDefEq x y) then return false
    return true

/-! ## Type inference -/

mutual

/-- The type of `e`, or an error if `e` is ill-typed. -/
partial def infer (e : Expr) : M Expr := do
  match e with
  | .bvar i => throw s!"loose bound variable #{i}"
  | .fvar id =>
    match (← read).locals.find? (·.id == id) with
    | some l => return l.type
    | none => throw s!"unknown free variable ?{id}"
  | .sort l => return .sort (.succ l)
  | .const n ls =>
    let some ci := (← getEnv).find? n | throw s!"unknown constant '{n}'"
    if ls.length != ci.lps.length then
      throw s!"'{n}' takes {ci.lps.length} universe argument(s), given {ls.length}"
    return ci.type.instantiateLevels ci.lps ls
  | .app f a =>
    let tf ← whnf (← infer f)
    let .pi _ d b := tf
      | throw s!"'{← pp f}' is applied to an argument, but its type is not a function type:\n  {← pp tf}"
    let ta ← infer a
    unless ← isDefEq ta d do
      throw s!"argument has the wrong type.\n  argument: {← pp a}\n  has type: {← pp ta}\n  expected: {← pp d}"
    return b.instantiate1 a
  | .lam x t b =>
    discard <| ensureSort t
    withLocal x t fun v => do
      let tb ← infer (b.instantiate1 v)
      mkPi [v] tb
  | .pi x t b =>
    let l1 ← ensureSort t
    withLocal x t fun v => do
      let l2 ← ensureSort (b.instantiate1 v)
      return .sort (.imax l1 l2)

/-- Check that `t` is a type, and return its universe level. -/
partial def ensureSort (t : Expr) : M Level := do
  match ← whnf (← infer t) with
  | .sort l => return l
  | s => throw s!"expected a type, but '{← pp t}' has type {← pp s}"

end

/-- Check `e : expected`. -/
def check (e expected : Expr) : M Unit := do
  let t ← infer e
  unless ← isDefEq t expected do
    throw s!"type mismatch.\n  term: {← pp e}\n  has type: {← pp t}\n  expected: {← pp expected}"

/-! ## Declarations -/

partial def levelParamsOf : Expr → List Name
  | .sort l => l.params
  | .const _ ls => ls.flatMap (·.params)
  | .app f a => levelParamsOf f ++ levelParamsOf a
  | .lam _ t b | .pi _ t b => levelParamsOf t ++ levelParamsOf b
  | _ => []

def checkLevelParams (n : Name) (lps : List Name) (es : List Expr) : M Unit := do
  for e in es do
    for p in levelParamsOf e do
      unless lps.contains p do throw s!"'{n}' uses universe parameter '{p}', which it does not declare"

def checkFresh (n : Name) : M Unit := do
  if (← getEnv).contains n then throw s!"'{n}' is already declared"

/-- Check a definition and add it. Its value can be unfolded afterwards. -/
def addDefinition (env : Env) (n : Name) (lps : List Name) (type value : Expr) : Except String Env :=
  M.run env do
    checkFresh n
    checkLevelParams n lps [type, value]
    discard <| ensureSort type
    check value type
    return env.add n (.defn lps type value)

/-- Check a theorem and add it. Its statement must be a proposition; its proof is never unfolded. -/
def addTheorem (env : Env) (n : Name) (lps : List Name) (type proof : Expr) : Except String Env :=
  M.run env do
    checkFresh n
    checkLevelParams n lps [type, proof]
    let l ← ensureSort type
    unless l.isZero do throw s!"the statement of theorem '{n}' is not a proposition"
    check proof type
    return env.add n (.thm lps type proof)

/-- Open up to `n` (or all, if `none`) leading Π-binders of `t` as free variables. -/
partial def openPis (t : Expr) (n : Option Nat) (k : Array Expr → Expr → M α)
    (acc : Array Expr := #[]) : M α := do
  if n == some acc.size then return ← k acc t
  match ← whnf t with
  | .pi x d b => withLocal x d fun v => openPis (b.instantiate1 v) n k (acc.push v)
  | t' => if n.isNone then k acc t' else throw "expected more Π-binders"

/-- Run `k` with one new free variable per `(name, type)`; each type may use the earlier ones. -/
partial def withLocals (decls : List (Name × (Array Expr → M Expr))) (k : Array Expr → M α)
    (acc : Array Expr := #[]) : M α := do
  match decls with
  | [] => k acc
  | (x, mkTy) :: rest =>
    let ty ← mkTy acc
    withLocal x ty fun v => withLocals rest k (acc.push v)

/--
Check an inductive type and add it, with its constructors and its generated recursor.

* `type` is the type of the inductive itself, `Π params, Π indices, Sort s`.
* Each constructor's type is `Π params, Π fields, I params indices`.

The checks: every type is well formed; each constructor starts with the same
parameters and ends in the inductive type applied to them; a field may mention
the inductive type only as its whole type, `I params idx` (a simple form of
strict positivity); and, unless `I` is a proposition, every field lives in a
universe no larger than `I`'s.
-/
def addInductive (env : Env) (n : Name) (lps : List Name) (numParams : Nat) (type : Expr)
    (ctors : List (Name × Expr)) : Except String Env := M.run env do
  checkFresh n
  for (c, _) in ctors do checkFresh c
  checkLevelParams n lps (type :: ctors.map (·.2))
  discard <| ensureSort type
  let levels := lps.map Level.param
  let self := Expr.const n levels
  -- The universe of the inductive type, and how many indices it has.
  let (s, numIndices) ← openPis type none fun xs body => do
    let .sort s := body | throw s!"the type of '{n}' must end in a sort"
    if xs.size < numParams then throw s!"'{n}' has fewer than {numParams} parameters"
    return (s, xs.size - numParams)
  let isProp := s.isZero
  if !isProp && s.mayBeZero then
    throw s!"the universe of '{n}' must be Prop or never Prop"
  let ctorNames := ctors.map (·.1)
  let env1 := env.add n (.induct lps type numParams numIndices ctorNames)
  -- Check each constructor, recording its number of fields.
  let mut fieldCounts : Array Nat := #[]
  for (c, ct) in ctors do
    let nf ← withReader (fun ctx => { ctx with env := env1 }) do
      discard <| ensureSort ct
      openPis type (some numParams) fun ps _ => do
        -- the constructor must start with the same parameters
        let rest ← ps.foldlM (init := ct) fun t p => do
          match ← whnf t with
          | .pi _ d b =>
            let .fvar pid := p | throw "unreachable"
            let some pl := (← read).locals.find? (·.id == pid) | throw "unreachable"
            unless ← isDefEq d pl.type do
              throw s!"constructor '{c}' must start with the parameters of '{n}'"
            return b.instantiate1 p
          | _ => throw s!"constructor '{c}' must start with the parameters of '{n}'"
        let isSelfApp (e : Expr) : Bool :=
          e.getAppFn.eqv self && e.getAppArgs.size == numParams + numIndices &&
            (ps.zip (e.getAppArgs.extract 0 numParams)).all fun (p, a) => p.eqv a
        openPis rest none fun fields concl => do
          for f in fields do
            let .fvar fid := f | throw "unreachable"
            let some fl := (← read).locals.find? (·.id == fid) | throw "unreachable"
            let d := fl.type
            if d.hasConst n then
              unless isSelfApp d && (d.getAppArgs.extract numParams d.getAppArgs.size).all
                  (fun i => !i.hasConst n) do
                throw s!"constructor '{c}': '{n}' may only appear as a field's whole type, applied to its parameters (strict positivity)"
            else if !isProp then
              let fs ← ensureSort d
              unless Level.leq fs s do
                throw s!"constructor '{c}': a field lives in a universe larger than '{n}'s"
          unless isSelfApp concl &&
              (concl.getAppArgs.extract numParams concl.getAppArgs.size).all (fun i => !i.hasConst n) do
            throw s!"constructor '{c}' must end in '{n}' applied to its parameters"
          return fields.size
    fieldCounts := fieldCounts.push nf
  -- Add the constructors.
  let mut env2 := env1
  for ((c, ct), i) in ctors.zipIdx do
    env2 := env2.add c (.ctor lps ct n i numParams fieldCounts[i]!)
  -- Elimination: a proposition may only be eliminated into Prop, unless it has
  -- at most one constructor and that constructor has no fields (like Eq).
  let largeElim := !isProp || (ctors.length ≤ 1 && fieldCounts.all (· == 0))
  let u := if lps.contains "w" then "w'" else "w"
  let motiveSort : Level := if largeElim then .param u else .zero
  let recLps := if largeElim then u :: lps else lps
  let recName := n ++ ".rec"
  -- Generate the recursor's type.
  let recType ← withReader (fun ctx => { ctx with env := env2 }) do
    openPis type (some numParams) fun ps afterParams => do
      -- motive : Π indices, Π (t : I ps indices), Sort u
      let motiveType ← openPis afterParams none fun is _ =>
        withLocal "t" (Expr.mkAppN self (ps ++ is)) fun t => mkPi (is.toList ++ [t]) (.sort motiveSort)
      withLocal "motive" motiveType fun motive => do
        -- one minor premise per constructor
        let minorDecls ← ctors.mapM fun (c, ct) => do
          let mt ← do
            let rest ← ps.foldlM (init := ct) fun t p => do
              let .pi _ _ b ← whnf t | throw "unreachable"
              return b.instantiate1 p
            openPis rest none fun fields concl => do
              -- induction hypotheses for the recursive fields
              let mut ihDecls : List (Name × (Array Expr → M Expr)) := []
              for f in fields do
                let .fvar fid := f | throw "unreachable"
                let some fl := (← read).locals.find? (·.id == fid) | throw "unreachable"
                if fl.type.hasConst n then
                  let idx := fl.type.getAppArgs.extract numParams fl.type.getAppArgs.size
                  let ihType : Expr := Expr.mkAppN motive (idx.push f)
                  let mk : Array Expr → M Expr := fun _ => pure ihType
                  ihDecls := ihDecls ++ [("ih", mk)]
              withLocals ihDecls fun ihs => do
                let cidx := concl.getAppArgs.extract numParams concl.getAppArgs.size
                let target := Expr.mkAppN motive
                  (cidx.push (Expr.mkAppN (.const c levels) (ps ++ fields)))
                mkPi (fields.toList ++ ihs.toList) target
          pure ("minor_" ++ (c.splitOn ".").getLast!, fun (_ : Array Expr) => pure mt)
        withLocals minorDecls fun minors =>
          openPis afterParams none fun is _ =>
            withLocal "t" (Expr.mkAppN self (ps ++ is)) fun t =>
              mkPi (ps.toList ++ [motive] ++ minors.toList ++ is.toList ++ [t])
                (Expr.mkAppN motive (is.push t))
  let env3 := env2.add recName (.recursor recLps recType n numParams numIndices ctorNames largeElim)
  -- Self-check: the generated type must itself be well formed.
  withReader (fun ctx => { ctx with env := env3 }) (discard <| ensureSort recType)
  return env3

end MiniLean
