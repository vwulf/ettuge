# How a Theorem Prover Is Written: One MiniLean Proof, Step by Step

*Started Nov 28, 2026 · last updated Nov 28, 2026 · Vishwas*

> **Work in progress.** Every output on this page was produced by [MiniLean](minilean.md) and is pinned in its build: `MiniLean/Checks.lean` re-runs each command inside `#guard_msgs`, so the build fails if any of it changes. The same walk, as a literate Lean page with the source alongside, is **One proof, step by step** on the [No Magic, implemented](https://vwulf.github.io/ettuge/FP/minilean-literate/) site.

<!-- section-index:begin -->
## Contents {#contents}

- [Summary](#summary)
- [The pipeline](#pipeline)
- [1. Text to Syntax: the parser](#s1)
- [2. Syntax to Raw: the first tree of our own](#s2)
- [3. Raw to Expr: names become indices](#s3)
- [4. Tactic syntax to a list of tactics](#s4)
- [5. Tactics build the proof term](#s5)
  - [5.1 Goals and builders](#s5-1)
  - [5.2 The run, tactic by tactic](#s5-2)
  - [5.3 What each tactic did, in the code](#s5-3)
  - [5.4 The computation refl and show relied on](#s5-4)
- [6. The kernel checks the term](#s6)
  - [6.1 What addTheorem does](#s6-1)
  - [6.2 The derivation](#s6-2)
  - [6.3 Where computation happens](#s6-3)
- [7. Into the environment](#s7)
- [8. What it takes to write a prover](#s8)
- [References](#references)

*Every heading links to itself: hover (or tap the link icon) and copy the link to share a section.*
<!-- section-index:end -->

## Summary {#summary}

[No Magic](lean-no-magic.md) followed a theorem down through Lean's layers, and [MiniLean](minilean.md) rebuilt the bottom of that stack as a kernel small enough to read. This page goes one level more pedantic. It takes a single declaration and follows it through MiniLean's code, one function at a time, from the characters you type to the kernel's "accepted". At each step it shows the code that runs and the data that comes out.

The declaration is the first lemma of the prelude, 0 + n = n:

```lean
mini_theorem zero_add (n : Nat) : NatEq (add zero n) n := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add zero k)) (succ k)
    rw [ih]
```

It is small, but it uses every moving part: a binder, a definition that has to compute, induction, a definitional restatement and a rewrite.

The outputs come from display commands in [`MiniLean/Explain.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Explain.lean) (`#mini_syntax`, `#mini_raw`, `#mini_db`, `#mini_tactics`, `#mini_defeq`, `#mini_kernel`). Each one calls the same functions `mini_theorem` calls, prints what it got, and adds nothing to the environment.

## The pipeline {#pipeline}

| Step | From | To | Code | Trusted? |
| --- | --- | --- | --- | --- |
| 1 | text | Lean `Syntax` | Lean's parser, with MiniLean's rules in `DSL.lean` | no |
| 2 | `Syntax` | `Raw` | `toRaw`, `toBinders`, `Raw.binders` (`DSL.lean`, `Surface.lean`) | no |
| 3 | `Raw` | `Expr` | `Raw.toExpr` (`Surface.lean`) | no |
| 4 | tactic syntax | `List Tac` | `toTacs`, `elabTheoremBy` (`DSL.lean`) | no |
| 5 | goal + tactics | proof term | `prove`, `solve`, `runTac`, `rwOne` (`Tactic.lean`) | no |
| 6 | statement + proof | accepted or rejected | `addTheorem`, `infer`, `whnf`, `isDefEq` (`Kernel.lean`) | **yes** |
| 7 | accepted declaration | environment entry | `Env.add` (`Env.lean`), `commitEnv` (`DSL.lean`) | yes / no |

Steps 1–5 can be as clever or as buggy as you like: they only produce a term. Step 6 decides. That split is the whole design of an LCF-style prover, and the rest of this page is what fills each box.

[↑ Contents](#contents)

## 1. Text to Syntax: the parser {#s1}

MiniLean has no parser of its own. [`DSL.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/DSL.lean) declares syntax categories and rules, and Lean's parser applies them:

```lean
declare_syntax_cat mini_term
declare_syntax_cat mini_binder

syntax "(" ident+ " : " mini_term ")" : mini_binder
syntax ident : mini_term
syntax "(" mini_term ")" : mini_term
syntax:10 mini_term:10 colGt mini_term:11 : mini_term   -- application
syntax:5 mini_term:6 " → " mini_term:5 : mini_term
syntax "λ " mini_binder+ " => " mini_term : mini_term
syntax "∀ " mini_binder+ ", " mini_term : mini_term
```

The precedences do real work. Application is left-associative (`mini_term:10` on the left, `:11` on the right), binds tighter than `→`, and `colGt` stops an application from swallowing the next line. The output is a Lean `Syntax` tree with one node per rule that matched. For the statement, with the binder written as a `∀`:

```text
#mini_syntax ∀ (n : Nat), NatEq (add zero n) n

(MiniLean.DSL.«mini_term∀_,_»
 "∀"
 [(MiniLean.DSL.«mini_binder(_:_)» "(" [`n] ":" (MiniLean.DSL.mini_term_ `Nat) ")")]
 ","
 (MiniLean.DSL.mini_term___
  (MiniLean.DSL.mini_term___
   (MiniLean.DSL.mini_term_ `NatEq)
   (MiniLean.DSL.«mini_term(_)»
    "("
    (MiniLean.DSL.mini_term___
     (MiniLean.DSL.mini_term___ (MiniLean.DSL.mini_term_ `add) (MiniLean.DSL.mini_term_ `zero))
     (MiniLean.DSL.mini_term_ `n))
    ")"))
  (MiniLean.DSL.mini_term_ `n)))
```

`mini_term___` is the application rule: `NatEq (add zero n) n` is `(NatEq (add zero n)) n`. The parentheses, the `∀` and the comma are still in the tree as tokens. Nothing has been resolved or checked.

[↑ Contents](#contents)

## 2. Syntax to Raw: the first tree of our own {#s2}

`Syntax` is Lean's type. The first thing MiniLean does is translate it into its own, `Raw` ([`Surface.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Surface.lean)):

```lean
inductive Raw where
  | ident (n : Name) (ls : Option (List Level))
  | app (f a : Raw)
  | lam (x : Name) (ty body : Raw)
  | pi (x : Name) (ty body : Raw)
  | sort (l : Level)
```

`toRaw` walks the `Syntax` tree by matching on quotations, one case per rule:

```lean
partial def toRaw : TSyntax `mini_term → CommandElabM MiniLean.Raw
  | `(mini_term| $x:ident) => pure (.ident (nameOf x) none)
  | `(mini_term| ($t)) => toRaw t
  | `(mini_term| $f $a) => return .app (← toRaw f) (← toRaw a)
  | `(mini_term| $a → $b) => return .pi "_" (← toRaw a) (← toRaw b)
  | `(mini_term| ∀ $bs*, $b) => return MiniLean.Raw.binders true (← toBinders bs) (← toRaw b)
  …
```

Three things happen here. Parentheses disappear (`($t)` is just `t`). An arrow `A → B` becomes a `pi` whose variable is `"_"`, a name you cannot write, so it can never capture a variable. And `(x y : A)` binders are spread out one variable at a time by `toBinders` and wrapped around the body by `Raw.binders`:

```lean
def Raw.binders (isPi : Bool) (bs : List (Name × Raw)) (body : Raw) : Raw :=
  bs.foldr (fun (x, t) acc => if isPi then .pi x t acc else .lam x t acc) body
```

`mini_theorem zero_add (n : Nat) : …` uses the same function, so the binder before the colon gives exactly the tree that writing the `∀` gives:

```text
#mini_raw ∀ (n : Nat), NatEq (add zero n) n

pi n
  ident Nat
  app
    app
      ident NatEq
      app
        app
          ident add
          ident zero
        ident n
    ident n
```

Names are still strings. `zero` here could mean anything.

[↑ Contents](#contents)

## 3. Raw to Expr: names become indices {#s3}

The kernel's term type has no names that matter ([`Expr.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Expr.lean)):

```lean
inductive Expr where
  | bvar (i : Nat)                    -- bound variable: a de Bruijn index
  | fvar (id : Nat)                   -- free variable: a local the checker introduced
  | sort (l : Level)
  | const (n : Name) (ls : List Level)
  | app (f a : Expr)
  | lam (x : Name) (ty body : Expr)   -- the name is kept only for printing
  | pi (x : Name) (ty body : Expr)
```

`Raw.toExpr` decides what each name means. It looks in three places, in order:

```lean
def Raw.toExpr (sc : Scope) : List Name → Raw → Except String Expr
  | bound, .ident n ls =>
    match bound.idxOf? n with
    | some i => … .ok (.bvar i)                    -- 1. a binder we are under
    | none =>
      match sc.locals.find? (·.name == n) with
      | some l => .ok (.fvar l.id)                 -- 2. a local of the current goal
      | none =>
        match sc.resolveConst n with               -- 3. a constant, also via mini_open
        | none => .error s!"unknown identifier '{n}'"
        | some c => … .ok (.const c levels)
  | bound, .lam x t b => return .lam x (← t.toExpr sc bound) (← b.toExpr sc (x :: bound))
  | bound, .pi x t b => return .pi x (← t.toExpr sc bound) (← b.toExpr sc (x :: bound))
  …
```

`bound` is the list of binder names we are under, newest first, so a name's position in it is its de Bruijn index. Going under `pi n` pushes `n`; inside, `n` is at position 0. `zero` is not declared, but `mini_open Nat` lets `resolveConst` try `Nat.zero`, which is. The result:

```text
#mini_db ∀ (n : Nat), NatEq (add zero n) n

pi n
  const Nat
  app
    app
      const NatEq
      app
        app
          const add
          const Nat.zero
        bvar 0
    bvar 0
```

Both `n`s became `bvar 0`: "the nearest binder". With indices, two terms that differ only in their bound names are the same tree, so α-equivalence is plain equality (`Expr.eqv`).

Still nothing has been *checked*. `Raw.toExpr` only fails on an unknown name or a wrong number of universe arguments. Whether this is a well-typed statement is the kernel's business. Asked now, `infer` says it is a proposition:

```text
#mini_check ∀ (n : Nat), NatEq (add zero n) n

∀ (n : Nat), NatEq (add Nat.zero n) n : Prop
```

[↑ Contents](#contents)

## 4. Tactic syntax to a list of tactics {#s4}

Tactics get the same treatment as terms: Lean parses them with MiniLean's rules, and `toTacs` turns each into a constructor of MiniLean's own type ([`Tactic.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Tactic.lean)):

```lean
inductive Tac where
  | intro (x : Name)
  | exact (t : Raw)
  | refl
  | show_ (t : Raw)
  | induction (x : Name)
  | rw (rules : List (Bool × Raw))   -- `true` means right-to-left (`← h`)
  | focus (tacs : List Tac)
```

`intro k ih` becomes two `intro`s, and a `·` block becomes `focus` with its tactics inside. Terms inside tactics (`show`'s statement, `rw`'s rules) stay `Raw`: they can only be resolved once the goal's locals exist. Then `elabTheoremBy` adds one `intro` per binder before the colon, as Lean does, and calls the tactic engine:

```lean
let tacs := bs.map (fun (x, _) => MiniLean.Tac.intro x) ++ (← toTacSeq seq)
let proof ← ok stx (← runM (MiniLean.prove s.opens type tacs))
-- the tactics' proof term goes to the kernel like any other
let env ← ok stx (MiniLean.addTheorem s.env (nameOf n) [] type proof)
```

Those three lines are the architecture: build a term, then hand it to the kernel. The script that runs is

```text
intro n; induction n; · refl; · intro k; intro ih; show NatEq (succ (add zero k)) (succ k); rw [ih]
```

[↑ Contents](#contents)

## 5. Tactics build the proof term {#s5}

### 5.1 Goals and builders {#s5-1}

A goal is a list of locals and a statement:

```lean
structure Goal where
  locals : List Local     -- each: a fresh id, a name, a type
  target : Expr

abbrev Builder := List Expr → Expr
```

A tactic is a function from one goal to new goals plus a `Builder`: given proofs of the new goals, a proof of the old one. That is the entire interface, and `solve` is the loop that drives it, depth first:

```lean
partial def solve (opens : List Name) : List Tac → List Goal → M (List Expr × List Tac)
  | tacs, [] => return ([], tacs)
  | [], g :: _ => do throw s!"unsolved goal:\n{← g.fmt}"
  | t :: ts, g :: gs => do
    let (subgoals, build) ← runTac opens t g          -- this tactic on the first goal
    let (subproofs, ts') ← solve opens ts subgoals     -- the following tactics solve its goals
    let (restProofs, ts'') ← solve opens ts' gs        -- leftover tactics go to the other goals
    return (build subproofs :: restProofs, ts'')
```

The proof is never stored in pieces. Each `build` closure waits for its subgoals' proofs, and when the last goal is closed the closures fire from the leaves up and the whole term exists at once.

### 5.2 The run, tactic by tactic {#s5-2}

`#mini_tactics` runs the same loop and, at each step, prints the goal the tactic acted on (`on`), the goals it created (`new`), and its builder applied to placeholders `?k` for the new goals. Substituting each `?k` into the line that created it gives `?0`, the final term.

```text
#mini_tactics (n : Nat) : NatEq (add zero n) n := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add zero k)) (succ k)
    rw [ih]

tactics: intro n; induction n; · refl; · intro k; intro ih; show NatEq (succ (add zero k)) (succ k); rw [ih]

intro n
  on    ?0  ⊢ ∀ (n : Nat), NatEq (add Nat.zero n) n
  new   ?1  n : Nat ⊢ NatEq (add Nat.zero n) n
  ?0 := λ (n : Nat) => ?1
induction n
  on    ?1  n : Nat ⊢ NatEq (add Nat.zero n) n
  new   ?2  ⊢ NatEq (add Nat.zero Nat.zero) Nat.zero
  new   ?3  ⊢ ∀ (x : Nat), NatEq (add Nat.zero x) x → NatEq (add Nat.zero (Nat.succ x)) (Nat.succ x)
  ?1 := Nat.rec.{0} (λ (n : Nat) => NatEq (add Nat.zero n) n) ?2 ?3 n
· focus on ?2
  refl
    on    ?2  ⊢ NatEq (add Nat.zero Nat.zero) Nat.zero
    new   (none: ?2 is closed)
    ?2 := Eq.refl.{1} Nat (add Nat.zero Nat.zero)
· focus on ?3
  intro k
    on    ?3  ⊢ ∀ (x : Nat), NatEq (add Nat.zero x) x → NatEq (add Nat.zero (Nat.succ x)) (Nat.succ x)
    new   ?4  k : Nat ⊢ NatEq (add Nat.zero k) k → NatEq (add Nat.zero (Nat.succ k)) (Nat.succ k)
    ?3 := λ (k : Nat) => ?4
  intro ih
    on    ?4  k : Nat ⊢ NatEq (add Nat.zero k) k → NatEq (add Nat.zero (Nat.succ k)) (Nat.succ k)
    new   ?5  k : Nat, ih : NatEq (add Nat.zero k) k ⊢ NatEq (add Nat.zero (Nat.succ k)) (Nat.succ k)
    ?4 := λ (ih : NatEq (add Nat.zero k) k) => ?5
  show NatEq (succ (add zero k)) (succ k)
    on    ?5  k : Nat, ih : NatEq (add Nat.zero k) k ⊢ NatEq (add Nat.zero (Nat.succ k)) (Nat.succ k)
    new   ?6  k : Nat, ih : NatEq (add Nat.zero k) k ⊢ NatEq (Nat.succ (add Nat.zero k)) (Nat.succ k)
    ?5 := ?6
  rw [ih]
    on    ?6  k : Nat, ih : NatEq (add Nat.zero k) k ⊢ NatEq (Nat.succ (add Nat.zero k)) (Nat.succ k)
    rule      ih : NatEq (add Nat.zero k) k
    equation  add Nat.zero k = k, used left to right
    find      add Nat.zero k  (first match in the goal, outermost first)
    motive    λ (b : Nat) => NatEq (Nat.succ b) (Nat.succ k)  (the goal, with b for each match)
    new goal  NatEq (Nat.succ k) (Nat.succ k)  (the motive applied to k)
    new   (none: the new goal holds by refl, so ?6 is closed)
    ?6 := Eq.rec.{0, 1} Nat k (λ (b : Nat) => λ (h : Eq.{1} Nat k b) => NatEq (Nat.succ b) (Nat.succ k)) (Eq.refl.{1} Nat (Nat.succ k)) (add Nat.zero k) (Eq.rec.{0, 1} Nat (add Nat.zero k) (λ (b : Nat) => λ (h : Eq.{1} Nat (add Nat.zero k) b) => Eq.{1} Nat b (add Nat.zero k)) (Eq.refl.{1} Nat (add Nat.zero k)) k ih)

?0 := λ (n : Nat) => Nat.rec.{0} (λ (n1 : Nat) => NatEq (add Nat.zero n1) n1) (Eq.refl.{1} Nat (add Nat.zero Nat.zero)) (λ (k : Nat) => λ (ih : NatEq (add Nat.zero k) k) => Eq.rec.{0, 1} Nat k (λ (b : Nat) => λ (h : Eq.{1} Nat k b) => NatEq (Nat.succ b) (Nat.succ k)) (Eq.refl.{1} Nat (Nat.succ k)) (add Nat.zero k) (Eq.rec.{0, 1} Nat (add Nat.zero k) (λ (b : Nat) => λ (h : Eq.{1} Nat (add Nat.zero k) b) => Eq.{1} Nat b (add Nat.zero k)) (Eq.refl.{1} Nat (add Nat.zero k)) k ih)) n
```

Seven tactics, seven holes, one term. Reading `?0` against the run: `λ (n : Nat) =>` is `intro n`; `Nat.rec.{0} motive _ _ n` is `induction n`; the first `_` is `refl`'s `Eq.refl`; the second is `λ (k : Nat) => λ (ih : …) =>` from the two `intro`s, around `rw [ih]`'s two `Eq.rec`s. `show` left no trace.

### 5.3 What each tactic did, in the code {#s5-3}

**`intro n`** ([`runTac`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Tactic.lean)):

```lean
| .intro x =>
  let .pi _ d b ← whnf g.target | throw s!"intro: the goal is not a ∀ or →\n{← g.fmt}"
  let id ← fresh
  let g' : Goal := { locals := ⟨id, x, d⟩ :: g.locals, target := b.instantiate1 (.fvar id) }
  return ([g'], fun ps => .lam x d (ps[0]!.abstract1 id))
```

The goal must reduce (`whnf`) to a `∀`. A fresh free variable takes the place of `bvar 0` in the body (`instantiate1`, "opening" the binder). The builder does the reverse: it turns that free variable back into `bvar 0` in the body's proof (`abstract1`) and wraps it in a `λ`. This open–close pair is the "locally nameless" discipline: the checker only ever works on terms with no dangling indices, so substitution never has to shift them.

**`induction n`**:

```lean
let motive := Expr.lam x l.type (g.target.abstract1 l.id)
let recHead := Expr.mkAppN (.const (ind ++ ".rec") recLevels) (params.push motive)
-- the minor premises' types are the new goals
let mut t ← whnf (← infer recHead)
for _ in ctors do
  let .pi _ d b := t | throw "induction: unexpected recursor type"
  goals := goals ++ [{ locals := others, target := d.betaAll }]
  t := b.instantiate1 (.sort .zero)  -- minor premises are independent of each other
return (goals, fun ps => Expr.mkAppN recHead (ps.toArray.push (.fvar l.id)))
```

The motive is the goal with `n` abstracted: `λ (n : Nat) => NatEq (add zero n) n`. The tactic does not know what a base case or a step is. It applies `Nat.rec` to the motive, asks the kernel's `infer` for the type, and reads the next two `∀`s off it: those are the minor premises, and their types are the new goals. (`betaAll` only tidies them for display; the kernel never sees it.) The universe argument `0` is the motive's universe, from `ensureSort g.target`: we are proving a `Prop`. The same code would do induction on any inductive type without indices.

**`refl`**:

```lean
def tryRefl (g : Goal) : M (Option Expr) := inGoal g do
  let some (u, α, a, b) ← asEq? g.target | return none
  if ← isDefEq a b then return some (Expr.mkAppN (.const "Eq.refl" [u]) #[α, a]) else return none
```

`asEq?` puts the goal in weak head normal form, which unfolds `NatEq` (δ) to `Eq.{1} Nat (add zero zero) zero`. Then the kernel's own `isDefEq` decides whether the two sides compute to the same thing ([5.4](#s5-4)).

**`show`**: `isDefEq` between the new statement and the goal, and the builder `fun ps => ps[0]!` passes the proof through unchanged. A definitional restatement is free in the term.

**`rw [ih]`** (`rwOne`), condensed:

```lean
let (mvars, stmt) ← openRule (← infer h) []          -- leading ∀s become pattern variables
let some (u, α, l, r) ← asEq? stmt | throw …          -- the rule must be an equation
let some σ := findMatch mvars src g.target | throw …  -- first instance of the left side
let body := abstractTerm src 0 g.target               -- the goal with bvar 0 for each instance
let newTarget := body.instantiate1 dst
…
let symmH := eqRec l symmMotive (Eq.refl l) r hInst   -- flip h : l = r into r = l
let motive ← mkMotive r                               -- λ (b : α) (h : r = b), body[b]
pure fun ps => eqRec r motive ps[0]! l symmH          -- transport the new goal's proof back
```

A rewrite is a proof by `Eq.rec` with a motive the tactic invents. `findMatch` is plain one-way matching, outermost first; `abstractTerm` turns every occurrence of the match into a bound variable, which makes the goal a function of it. `Eq.rec` transports along an equation `a = b` from `motive a` to `motive b`. Here we have a proof for the *new* goal (with `k`) and need the old one (with `add zero k`), so we transport along `k = add zero k`: the flipped `ih`, which is itself an `Eq.rec`. If the new goal holds by `refl`, `rw` closes it, as Lean's does.

### 5.4 The computation refl and show relied on {#s5-4}

`refl` needed `add zero zero` to compute to `zero`. `whnfStep?` ([`Kernel.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Kernel.lean)) takes one head step at a time, and each step is one of three rules:

```lean
partial def whnfStep? (e : Expr) : M (Option (String × Expr)) := do
  match e.getAppFn with
  | .lam _ _ body => … return some ("β", Expr.mkAppN (body.instantiate1 args[0]) (args.extract 1 args.size))
  | .const n ls =>
    match (← getEnv).find? n with
    | some (.defn lps _ v) => return some (s!"δ {n}", Expr.mkAppN (v.instantiateLevels lps ls) e.getAppArgs)
    | some (.recursor _ _ ind np ni ctors _) => return (← iota? n ls ind np ni ctors e.getAppArgs).map (s!"ι {n}", ·)
    | _ => return none
  | _ => return none
```

```text
#mini_trace add zero zero

  add Nat.zero Nat.zero
⟶ δ add
  (λ (m : Nat) => λ (n : Nat) => Nat.rec.{1} (λ (k : Nat) => Nat) m (λ (k : Nat) => λ (ih : Nat) => Nat.succ ih) n) Nat.zero Nat.zero
⟶ β
  (λ (n : Nat) => Nat.rec.{1} (λ (k : Nat) => Nat) Nat.zero (λ (k : Nat) => λ (ih : Nat) => Nat.succ ih) n) Nat.zero
⟶ β
  Nat.rec.{1} (λ (k : Nat) => Nat) Nat.zero (λ (k : Nat) => λ (ih : Nat) => Nat.succ ih) Nat.zero
⟶ ι Nat.rec
  Nat.zero
```

δ unfolds `add`, two βs substitute its arguments, and ι runs `Nat.rec` on the constructor `Nat.zero`, which returns the base case. `iota?` finds the major premise among the recursor's arguments, puts it in weak head normal form, and, if it is a constructor, applies that constructor's minor premise to the fields and to the recursive calls on the recursive fields.

`show` needed its statement to be definitionally equal to the goal. `isDefEq` reduces both sides to weak head normal form; if they are still different, and both are stuck on the same head, it compares the arguments one by one:

```lean
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
  | _, _ => … -- same head (constant or free variable) and same number of arguments, then isDefEq on each
```

`#mini_defeq` retraces it (and checks that the real `isDefEq` agrees):

```text
#mini_defeq ∀ (k : Nat), NatEq (succ (add zero k)) (succ k) =?= ∀ (k : Nat), NatEq (add zero (succ k)) (succ k)

∀ (k : Nat), NatEq (Nat.succ (add Nat.zero k)) (Nat.succ k)  ≟  ∀ (k : Nat), NatEq (add Nat.zero (Nat.succ k)) (Nat.succ k)
  both binders: compare the types, then the bodies
  Nat  ≟  Nat
    identical ✓
  NatEq (Nat.succ (add Nat.zero k)) (Nat.succ k)  ≟  NatEq (add Nat.zero (Nat.succ k)) (Nat.succ k)
    whnf left   ⟶ Eq.{1} Nat (Nat.succ (add Nat.zero k)) (Nat.succ k)
    whnf right  ⟶ Eq.{1} Nat (add Nat.zero (Nat.succ k)) (Nat.succ k)
    stuck; same head Eq.{1}: compare the 3 arguments
    Nat  ≟  Nat
      identical ✓
    Nat.succ (add Nat.zero k)  ≟  add Nat.zero (Nat.succ k)
      whnf right  ⟶ Nat.succ (Nat.rec.{1} (λ (k : Nat) => Nat) Nat.zero (λ (k : Nat) => λ (ih : Nat) => Nat.succ ih) k)
      stuck; same head Nat.succ: compare the 1 arguments
      add Nat.zero k  ≟  Nat.rec.{1} (λ (k : Nat) => Nat) Nat.zero (λ (k : Nat) => λ (ih : Nat) => Nat.succ ih) k
        whnf left   ⟶ Nat.rec.{1} (λ (k : Nat) => Nat) Nat.zero (λ (k : Nat) => λ (ih : Nat) => Nat.succ ih) k
        identical ✓
    Nat.succ k  ≟  Nat.succ k
      identical ✓
```

On the right, `add zero (succ k)` takes one ι-step, because `Nat.rec` meets the constructor `succ`: the result is `succ (Nat.rec … k)`. That recursive call is stuck, because `k` is a variable. On the left, `add zero k` unfolds to exactly the same stuck term. This is why the script says `show` before `rw [ih]`: `rw` matches syntactically, and the goal contains `add zero k` only after `show` restates it.

[↑ Contents](#contents)

## 6. The kernel checks the term {#s6}

### 6.1 What addTheorem does {#s6-1}

The tactics are finished and the term exists. From here on nothing from steps 1–5 is believed:

```lean
def addTheorem (env : Env) (n : Name) (lps : List Name) (type proof : Expr) : Except String Env :=
  M.run env do
    checkFresh n
    checkLevelParams n lps [type, proof]
    let l ← ensureSort type
    unless l.isZero do throw s!"the statement of theorem '{n}' is not a proposition"
    check proof type
    return env.add n (.thm lps type proof)
```

`check proof type` is `infer proof`, then `isDefEq` with the statement. `infer` has one case per typing rule. The two that matter here:

```lean
| .app f a =>
  let tf ← whnf (← infer f)
  let .pi _ d b := tf | throw s!"'{← pp f}' is applied to an argument, but its type is not a function type…"
  let ta ← infer a
  unless ← isDefEq ta d do throw s!"argument has the wrong type…"
  return b.instantiate1 a
| .lam x t b =>
  discard <| ensureSort t
  withLocal x t fun v => do
    let tb ← infer (b.instantiate1 v)
    mkPi [v] tb
```

An application's head must have a function type, the argument's type must be definitionally equal to the domain, and the result is the codomain with the argument substituted. A `λ` is checked by opening its binder with a fresh local, inferring the body's type, and closing it back into a `∀`.

### 6.2 The derivation {#s6-2}

`#mini_kernel` replays `addTheorem` on the accepted theorem, using `infer`, `whnf` and `isDefEq` for every result it reports. Applications are shown as a head and its arguments; `infer` takes them one at a time, which is the same work. With depth 0, arguments are shown by their types, without their own derivations:

```text
#mini_kernel 0 zero_add

addTheorem zero_add
1. checkFresh: no earlier declaration is named zero_add
2. checkLevelParams: universe parameters [], none undeclared
3. ensureSort statement: ∀ (n : Nat), NatEq (add Nat.zero n) n : Sort imax (1) (0)
   level imax (1) (0) is 0, so the statement is a proposition ✓
4. check (proof) (statement): first infer the proof's type
   λ (n : Nat) =>   open n as a free variable, infer the body
     Nat.rec.{0} (λ (n : Nat) => NatEq (add Nat.zero n) n) (Eq.refl.{1} Nat (add Nat.zero Nat.zero)) (λ (k : Nat) => λ (ih : NatEq (add Nat.zero k) k) => Eq.rec.{0, 1} Nat k (λ (b : Nat) => λ (h : Eq.{1} Nat k b) => NatEq (Nat.succ b) (Nat.succ k)) (Eq.refl.{1} Nat (Nat.succ k)) (add Nat.zero k) (Eq.rec.{0, 1} Nat (add Nat.zero k) (λ (b : Nat) => λ (h : Eq.{1} Nat (add Nat.zero k) b) => Eq.{1} Nat b (add Nat.zero k)) (Eq.refl.{1} Nat (add Nat.zero k)) k ih)) n
       head  Nat.rec.{0} : ∀ (motive : Nat → Prop), motive Nat.zero → (∀ (x : Nat), motive x → motive (Nat.succ x)) → ∀ (t : Nat), motive t
       arg 1  λ (n : Nat) => NatEq (add Nat.zero n) n
         has type  Nat → Prop
         expected  Nat → Prop
         identical ✓
       arg 2  Eq.refl.{1} Nat (add Nat.zero Nat.zero)
         has type  Eq.{1} Nat (add Nat.zero Nat.zero) (add Nat.zero Nat.zero)
         expected  (λ (n : Nat) => NatEq (add Nat.zero n) n) Nat.zero
         definitionally equal ✓
       arg 3  λ (k : Nat) => λ (ih : NatEq (add Nat.zero k) k) => Eq.rec.{0, 1} Nat k (λ (b : Nat) => λ (h : Eq.{1} Nat k b) => NatEq (Nat.succ b) (Nat.succ k)) (Eq.refl.{1} Nat (Nat.succ k)) (add Nat.zero k) (Eq.rec.{0, 1} Nat (add Nat.zero k) (λ (b : Nat) => λ (h : Eq.{1} Nat (add Nat.zero k) b) => Eq.{1} Nat b (add Nat.zero k)) (Eq.refl.{1} Nat (add Nat.zero k)) k ih)
         has type  ∀ (k : Nat), ∀ (ih : NatEq (add Nat.zero k) k), (λ (b : Nat) => λ (h : Eq.{1} Nat k b) => NatEq (Nat.succ b) (Nat.succ k)) (add Nat.zero k) (Eq.rec.{0, 1} Nat (add Nat.zero k) (λ (b : Nat) => λ (h : Eq.{1} Nat (add Nat.zero k) b) => Eq.{1} Nat b (add Nat.zero k)) (Eq.refl.{1} Nat (add Nat.zero k)) k ih)
         expected  ∀ (x : Nat), (λ (n : Nat) => NatEq (add Nat.zero n) n) x → (λ (n : Nat) => NatEq (add Nat.zero n) n) (Nat.succ x)
         definitionally equal ✓
       arg 4  n
         has type  Nat
         expected  Nat
         identical ✓
       type  (λ (n : Nat) => NatEq (add Nat.zero n) n) n
     type  ∀ (n : Nat), (λ (n1 : Nat) => NatEq (add Nat.zero n1) n1) n
5. then isDefEq (inferred type) (statement)
   ∀ (n : Nat), (λ (n1 : Nat) => NatEq (add Nat.zero n1) n1) n  ≟  ∀ (n : Nat), NatEq (add Nat.zero n) n
     both binders: compare the types, then the bodies
     Nat  ≟  Nat
       identical ✓
     (λ (n : Nat) => NatEq (add Nat.zero n) n) n  ≟  NatEq (add Nat.zero n) n
       whnf left   ⟶ Eq.{1} Nat (add Nat.zero n) n
       whnf right  ⟶ Eq.{1} Nat (add Nat.zero n) n
       identical ✓
6. env.add zero_add (theorem: its proof is never unfolded)
```

Read it as the kernel consuming `Nat.rec`'s type one `∀` at a time. Argument 1 fixes the motive, and from then on every expected type mentions it: the base case must prove `motive Nat.zero`, the step must prove `∀ x, motive x → motive (succ x)`, and the whole application proves `motive n`. Step 3's universe is worth a look too: `∀ (n : Nat), P n` lives in `Sort (imax 1 0)`, and `imax u 0 = 0`. A `∀` into `Prop` is a proposition whatever it ranges over; that is the impredicativity of `Prop`.

### 6.3 Where computation happens {#s6-3}

Every "identical ✓" above was free. Every "definitionally equal ✓" is the kernel computing. The base case has type `Eq … (add zero zero) (add zero zero)` and must have type `motive Nat.zero`:

```text
#mini_defeq Eq.{1} Nat (add zero zero) (add zero zero) =?= (λ (n : Nat) => NatEq (add zero n) n) zero

Eq.{1} Nat (add Nat.zero Nat.zero) (add Nat.zero Nat.zero)  ≟  (λ (n : Nat) => NatEq (add Nat.zero n) n) Nat.zero
  whnf right  ⟶ Eq.{1} Nat (add Nat.zero Nat.zero) Nat.zero
  stuck; same head Eq.{1}: compare the 3 arguments
  Nat  ≟  Nat
    identical ✓
  add Nat.zero Nat.zero  ≟  add Nat.zero Nat.zero
    identical ✓
  add Nat.zero Nat.zero  ≟  Nat.zero
    whnf left   ⟶ Nat.zero
    identical ✓
```

β applies the motive, δ unfolds `NatEq`, and the last argument is the reduction of [5.4](#s5-4): `add zero zero` ⟶ `zero`. The tactic `refl` asked the same question of the same `isDefEq` while building the term. The kernel asks it again, because it does not take the tactic's word for anything.

The step case (argument 3) is the same kind of check, longer. After β-reducing the motives and unfolding `NatEq`, the hypotheses agree, and the conclusions are `Eq … (succ (add zero k)) (succ k)` against `Eq … (add zero (succ k)) (succ k)`: exactly the comparison `show` made in [5.4](#s5-4).

[↑ Contents](#contents)

## 7. Into the environment {#s7}

`addTheorem` returns a new environment with one more entry, `.thm [] type proof`. An environment is just an ordered array of declarations ([`Env.lean`](https://github.com/vwulf/ettuge/blob/master/src/main/lean/minilean/MiniLean/Env.lean)), and nothing joins it except through the kernel's `add…` functions.

The DSL then records the new entry in a Lean environment extension (`commitEnv`). That is how a later `mini_theorem`, or a later file importing the prelude, sees `zero_add`: the entry was checked when its own file was built. In `add_comm`, `rw [zero_add]` uses it as a constant with one pattern variable:

```text
  rw [zero_add]
    on    ?5  m : Nat ⊢ NatEq m (add Nat.zero m)
    rule      zero_add : ∀ (n : Nat), NatEq (add Nat.zero n) n
    equation  add Nat.zero ?n = ?n, used left to right
    pattern variables (the rule's ∀s): 1
    find      add Nat.zero m  (first match in the goal, outermost first)
```

A theorem is stored but never unfolded: `whnfStep?` unfolds only `.defn` entries. Its proof could be replaced by any other proof of the same statement without changing anything downstream. What was stored:

```text
#mini_print zero_add

theorem zero_add : ∀ (n : Nat), NatEq (add Nat.zero n) n :=
  λ (n : Nat) => Nat.rec.{0} (λ (n1 : Nat) => NatEq (add Nat.zero n1) n1) (Eq.refl.{1} Nat (add Nat.zero Nat.zero)) (λ (k : Nat) => λ (ih : NatEq (add Nat.zero k) k) => Eq.rec.{0, 1} Nat k (λ (b : Nat) => λ (h : Eq.{1} Nat k b) => NatEq (Nat.succ b) (Nat.succ k)) (Eq.refl.{1} Nat (Nat.succ k)) (add Nat.zero k) (Eq.rec.{0, 1} Nat (add Nat.zero k) (λ (b : Nat) => λ (h : Eq.{1} Nat (add Nat.zero k) b) => Eq.{1} Nat b (add Nat.zero k)) (Eq.refl.{1} Nat (add Nat.zero k)) k ih)) n
```

It is `?0` from [5.2](#s5-2), with the motive's bound variable renamed `n1` by the printer so that it does not shadow the outer `n`.

[↑ Contents](#contents)

## 8. What it takes to write a prover {#s8}

Followed from top to bottom, the steps are a list of design decisions, each small:

1. **Borrow a parser.** The syntax is a few dozen rules in a host language that already parses. Precedence and layout (`colGt`) are the only subtle parts.
2. **Translate into your own tree at once.** `Raw` has five constructors. Everything after this point is independent of the host's syntax.
3. **Resolve names into indices, and keep names only for printing.** De Bruijn indices make α-equivalence equality. Free variables with fresh ids give the "locally nameless" discipline: open a binder with a fresh variable, close it with `abstract1`, and substitution never needs to shift indices.
4. **Make a tactic a function from a goal to goals plus a builder.** Everything a tactic knows comes from the kernel's own functions (`whnf`, `infer`, `isDefEq`); `induction` even reads its new goals off the recursor's type. A tactic can be wrong, slow or incomplete, and it costs nothing in soundness.
5. **Compose the builders, not the proofs.** `solve` is a dozen lines, and the term appears whole when the last goal closes.
6. **Make the kernel small, and re-check everything.** One case per typing rule in `infer`, three reduction rules in `whnfStep?`, and a comparison in `isDefEq`. Computation enters the logic only through `isDefEq`, which is what lets `refl` prove `add zero zero = zero` and `show` restate a goal for free.
7. **Let only the kernel extend the environment.** Every later use of `zero_add` is a constant whose statement was checked once.

The trusted part is steps 6 and 7: about 745 lines (`Level.lean`, `Expr.lean`, `Env.lean`, `Kernel.lean`). Lean 4 has the same shape, at a much larger scale: its elaborator, unifier and tactic framework sit where steps 2–5 sit here, and its kernel in C++ (or one of the [independent checkers](lean-no-magic.md#s6)) where step 6 sits.

What MiniLean leaves out, and what Lean 4 adds on top of the same pipeline ([MiniLean §3](minilean.md#s3)): implicit arguments and unification in step 3, so `Eq.{1} Nat a b` can be written `a = b`; a pattern-matching compiler in front of step 2, so `add` can be defined by equations and compiled to `Nat.rec`; and many more tactics in step 5, each one still a builder of terms for the same kind of kernel.

[↑ Contents](#contents)

## References {#references}

- MiniLean source: [`src/main/lean/minilean`](https://github.com/vwulf/ettuge/tree/master/src/main/lean/minilean). This page's outputs: `MiniLean/StepByStep.lean`, using the display commands in `MiniLean/Explain.lean`.
- [MiniLean: The No Magic Proof in a Kernel You Can Read](minilean.md), the article this page goes underneath.
- [No Magic: Proving 1 + 2 + … + n = n(n+1)/2 from Paper to Lean's Kernel](lean-no-magic.md), the same journey in Lean 4.
- [MiniLean4](https://learn.h5i.dev/), the book MiniLean's structure follows.
- Arthur Charguéraud, "The Locally Nameless Representation", *Journal of Automated Reasoning* 49 (2012): the open/close discipline of step 3.
- Michael Gordon, Robin Milner and Christopher Wadsworth, *Edinburgh LCF*, LNCS 78 (1979): the origin of untrusted tactics feeding a small trusted checker.
