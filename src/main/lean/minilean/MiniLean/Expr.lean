import MiniLean.Level

/-!
# Terms

Six kinds of term, plus free variables for the type checker's own use.

Bound variables are de Bruijn indices: `bvar 0` is the nearest enclosing
binder, `bvar 1` the next one out, and so on. Names on binders are kept only
for printing; they play no part in checking.

Free variables (`fvar`) are how the checker goes under a binder. To check the
body of `λ (x : A), b`, it invents a fresh `fvar`, records that it has type
`A`, and replaces `bvar 0` in `b` with it ("opening" the binder). Every term the
checker works on is therefore *locally closed*: it has no dangling `bvar`s.
That makes substitution simple, because a locally closed term never needs its
indices shifted. (This is the "locally nameless" representation.)
-/

namespace MiniLean

inductive Expr where
  | bvar (i : Nat)
  | fvar (id : Nat)
  | sort (l : Level)
  | const (n : Name) (ls : List Level)
  | app (f a : Expr)
  | lam (x : Name) (ty body : Expr)
  | pi (x : Name) (ty body : Expr)
  deriving Repr, Inhabited

namespace Expr

def prop : Expr := sort .zero
def type : Expr := sort (.succ .zero)

/-- Equality up to the names on binders (α-equivalence, which de Bruijn indices make syntactic). -/
partial def eqv : Expr → Expr → Bool
  | bvar i, bvar j => i == j
  | fvar i, fvar j => i == j
  | sort l, sort m => Level.isEquiv l m
  | const n ls, const m ms => n == m && ls.length == ms.length &&
      (ls.zip ms).all fun (a, b) => Level.isEquiv a b
  | app f a, app g b => eqv f g && eqv a b
  | lam _ t b, lam _ u c => eqv t u && eqv b c
  | pi _ t b, pi _ u c => eqv t u && eqv b c
  | _, _ => false

/-- Substitute the locally closed term `v` for `bvar d` (`d` binders deep), lowering the indices above it. -/
def instantiateAt (v : Expr) : Nat → Expr → Expr
  | d, bvar i => if i == d then v else if i > d then bvar (i - 1) else bvar i
  | d, app f a => app (instantiateAt v d f) (instantiateAt v d a)
  | d, lam x t b => lam x (instantiateAt v d t) (instantiateAt v (d + 1) b)
  | d, pi x t b => pi x (instantiateAt v d t) (instantiateAt v (d + 1) b)
  | _, e => e

/-- Open a binder's body: replace its bound variable with `v`. -/
def instantiate1 (body v : Expr) : Expr := instantiateAt v 0 body

/-- Turn the free variable `id` into `bvar d` (`d` binders deep): the inverse of opening. -/
def abstractAt (id : Nat) : Nat → Expr → Expr
  | d, fvar j => if j == id then bvar d else fvar j
  | d, app f a => app (abstractAt id d f) (abstractAt id d a)
  | d, lam x t b => lam x (abstractAt id d t) (abstractAt id (d + 1) b)
  | d, pi x t b => pi x (abstractAt id d t) (abstractAt id (d + 1) b)
  | _, e => e

def abstract1 (e : Expr) (id : Nat) : Expr := abstractAt id 0 e

/-- Replace universe parameters `ps` by levels `ls` everywhere. -/
def instantiateLevels (ps : List Name) (ls : List Level) : Expr → Expr
  | sort l => sort (l.instantiate ps ls)
  | const n ms => const n (ms.map (·.instantiate ps ls))
  | app f a => app (instantiateLevels ps ls f) (instantiateLevels ps ls a)
  | lam x t b => lam x (instantiateLevels ps ls t) (instantiateLevels ps ls b)
  | pi x t b => pi x (instantiateLevels ps ls t) (instantiateLevels ps ls b)
  | e => e

def hasLooseBVarAt : Nat → Expr → Bool
  | d, bvar i => i == d
  | d, app f a => hasLooseBVarAt d f || hasLooseBVarAt d a
  | d, lam _ t b => hasLooseBVarAt d t || hasLooseBVarAt (d + 1) b
  | d, pi _ t b => hasLooseBVarAt d t || hasLooseBVarAt (d + 1) b
  | _, _ => false

def hasLooseBVars : Nat → Expr → Bool
  | d, bvar i => i ≥ d
  | d, app f a => hasLooseBVars d f || hasLooseBVars d a
  | d, lam _ t b => hasLooseBVars d t || hasLooseBVars (d + 1) b
  | d, pi _ t b => hasLooseBVars d t || hasLooseBVars (d + 1) b
  | _, _ => false

def hasFVar (id : Nat) : Expr → Bool
  | fvar j => j == id
  | app f a => hasFVar id f || hasFVar id a
  | lam _ t b => hasFVar id t || hasFVar id b
  | pi _ t b => hasFVar id t || hasFVar id b
  | _ => false

def hasConst (n : Name) : Expr → Bool
  | const m _ => m == n
  | app f a => hasConst n f || hasConst n a
  | lam _ t b => hasConst n t || hasConst n b
  | pi _ t b => hasConst n t || hasConst n b
  | _ => false

def getAppFn : Expr → Expr
  | app f _ => getAppFn f
  | e => e

def getAppArgs (e : Expr) : Array Expr :=
  let rec go : Expr → List Expr → List Expr
    | app f a, acc => go f (a :: acc)
    | _, acc => acc
  (go e []).toArray

def mkAppN (f : Expr) (args : Array Expr) : Expr :=
  args.foldl app f

/-- β-reduce every redex `(λ x, b) a`, everywhere in the term. Used only to tidy goals for display. -/
partial def betaAll : Expr → Expr
  | app f a =>
    match betaAll f with
    | lam _ _ b => betaAll (b.instantiate1 (betaAll a))
    | f' => app f' (betaAll a)
  | lam x t b => lam x (betaAll t) (betaAll b)
  | pi x t b => pi x (betaAll t) (betaAll b)
  | e => e

/-! ## Printing -/

/-- Print a term. `fvars` names the free variables; `bound` names the binders we are under. -/
partial def fmt (fvars : Nat → String) (bound : List Name) : Expr → String
  | bvar i => bound[i]?.getD s!"#{i}"
  | fvar id => fvars id
  | sort l =>
    if Level.isEquiv l .zero then "Prop"
    else if Level.isEquiv l (.succ .zero) then "Type"
    else s!"Sort {l}"
  | const n [] => n
  | const n ls => n ++ ".{" ++ ", ".intercalate (ls.map toString) ++ "}"
  | e@(app ..) =>
    match succChain e 0 with
    | some (n, base) => s!"Nat.succ^{n} {atom base}"
    | none =>
      let f := e.getAppFn
      let args := e.getAppArgs
      " ".intercalate ((atom f) :: args.toList.map atom)
  | lam x t b =>
    let x := fresh x bound
    s!"λ ({x} : {fmt fvars bound t}) => {fmt fvars (x :: bound) b}"
  | pi x t b =>
    if hasLooseBVarAt 0 b then
      let x := fresh x bound
      s!"∀ ({x} : {fmt fvars bound t}), {fmt fvars (x :: bound) b}"
    else
      let dom := match t with
        | pi .. | lam .. => s!"({fmt fvars bound t})"
        | _ => fmt fvars bound t
      s!"{dom} → {fmt fvars ("_" :: bound) b}"
where
  /-- A name not already used by an enclosing binder (so printed terms are unambiguous). -/
  fresh (x : Name) (bound : List Name) : Name :=
    let x := if x == "_" then "x" else x
    if !bound.contains x then x
    else (List.range 100).map (fun i => x ++ toString (i + 1)) |>.find? (!bound.contains ·) |>.getD x
  /-- `Nat.succ (Nat.succ … base)` with at least three `succ`s, printed as `Nat.succ^n base`. -/
  succChain (e : Expr) (n : Nat) : Option (Nat × Expr) :=
    match e with
    | app (const "Nat.succ" []) a => succChain a (n + 1)
    | base => if n ≥ 3 then some (n, base) else none
  atom (e : Expr) : String :=
    match e with
    | app .. | lam .. | pi .. => s!"({fmt fvars bound e})"
    | sort l => if Level.isEquiv l .zero || Level.isEquiv l (.succ .zero) then fmt fvars bound e
                else s!"({fmt fvars bound e})"
    | _ => fmt fvars bound e

end Expr
end MiniLean
