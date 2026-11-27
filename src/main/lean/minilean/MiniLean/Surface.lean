import MiniLean.Kernel

/-!
# Surface terms and name resolution

The DSL's terms arrive here as `Raw`: a tree of names, applications and
binders. `Raw.toExpr` resolves each name to a bound variable, a local (in a
tactic goal), or a constant in the environment. This is the whole "front end":
no notation, no implicit arguments, no unification.

This file is not trusted. Whatever it produces, the kernel checks.
-/

namespace MiniLean

inductive Raw where
  | ident (n : Name) (ls : Option (List Level))
  | app (f a : Raw)
  | lam (x : Name) (ty body : Raw)
  | pi (x : Name) (ty body : Raw)
  | sort (l : Level)
  deriving Inhabited

/-- What a name can refer to: locals (newest first), namespaces opened with `mini_open`, and one
constant that is being declared and so is not in the environment yet. -/
structure Scope where
  env : Env
  locals : List Local := []
  opens : List Name := []
  pending : Option (Name × List Level) := none

def Scope.resolveConst (sc : Scope) (n : Name) : Option Name :=
  let isPending (c : Name) : Bool := match sc.pending with
    | some (p, _) => p == c
    | none => false
  ([n] ++ sc.opens.map (· ++ "." ++ n)).find? fun c => isPending c || sc.env.contains c

def Raw.toExpr (sc : Scope) : List Name → Raw → Except String Expr
  | bound, .ident n ls =>
    match bound.idxOf? n with
    | some i =>
      if ls.isSome then .error s!"'{n}' is a bound variable; it takes no universe arguments"
      else .ok (.bvar i)
    | none =>
      match sc.locals.find? (·.name == n) with
      | some l => .ok (.fvar l.id)
      | none =>
        match sc.resolveConst n with
        | none => .error s!"unknown identifier '{n}'"
        | some c =>
          let declared : Nat :=
            if let some (p, ps) := sc.pending then
              if p == c then ps.length else ((sc.env.find? c).map (·.lps.length)).getD 0
            else ((sc.env.find? c).map (·.lps.length)).getD 0
          let levels := ls.getD []
          if levels.length != declared then
            .error s!"'{c}' needs {declared} universe argument(s), written '{c}.{"{"}…}'; given {levels.length}"
          else .ok (.const c levels)
  | bound, .app f a => return .app (← f.toExpr sc bound) (← a.toExpr sc bound)
  | bound, .lam x t b => return .lam x (← t.toExpr sc bound) (← b.toExpr sc (x :: bound))
  | bound, .pi x t b => return .pi x (← t.toExpr sc bound) (← b.toExpr sc (x :: bound))
  | _, .sort l => return .sort l

/-- Wrap `body` in binders `(x : T)`, outermost first. -/
def Raw.binders (isPi : Bool) (bs : List (Name × Raw)) (body : Raw) : Raw :=
  bs.foldr (fun (x, t) acc => if isPi then .pi x t acc else .lam x t acc) body

end MiniLean
