/-!
# Universe levels

`Sort u` is the type of types at level `u`: `Prop = Sort 0`, `Type = Sort 1`,
and so on. Levels are built from `0`, successor, `max`, `imax` and named
parameters (for universe-polymorphic declarations such as `Eq.{u}`).

`imax a b` is `0` when `b` is `0`, and `max a b` otherwise. It is the level of
a Π-type whose codomain is at level `b`: a function into `Prop` is a `Prop`,
whatever its domain.
-/

namespace MiniLean

abbrev Name := String

inductive Level where
  | zero
  | succ (l : Level)
  | max (a b : Level)
  | imax (a b : Level)
  | param (n : Name)
  deriving Repr, BEq, Inhabited

namespace Level

def ofNat : Nat → Level
  | 0 => zero
  | n + 1 => succ (ofNat n)

/-- The level's value once every parameter has been given a number. -/
def eval (σ : Name → Nat) : Level → Nat
  | zero => 0
  | succ l => eval σ l + 1
  | max a b => Nat.max (eval σ a) (eval σ b)
  | imax a b =>
    let vb := eval σ b
    if vb = 0 then 0 else Nat.max (eval σ a) vb
  | param n => σ n

def params : Level → List Name
  | zero => []
  | succ l => params l
  | max a b => params a ++ params b
  | imax a b => params a ++ params b
  | param n => [n]

/-- The largest number of `succ`s on any path: a bound on the constants in the level. -/
def depth : Level → Nat
  | zero => 0
  | succ l => depth l + 1
  | max a b => Nat.max (depth a) (depth b)
  | imax a b => Nat.max (depth a) (depth b)
  | param _ => 0

/-- Replace the parameters `ps` with the levels `ls`. -/
def instantiate (ps : List Name) (ls : List Level) : Level → Level
  | zero => zero
  | succ l => succ (instantiate ps ls l)
  | max a b => max (instantiate ps ls a) (instantiate ps ls b)
  | imax a b => imax (instantiate ps ls a) (instantiate ps ls b)
  | param n => ((ps.zip ls).lookup n).getD (param n)

/-- Every assignment of the values `0..k` to the parameters `ps`. -/
def assignments (ps : List Name) (k : Nat) : List (Name → Nat) :=
  ps.foldl (init := [fun _ => 0]) fun acc p =>
    acc.flatMap fun σ => (List.range (k + 1)).map fun v => fun q => if q == p then v else σ q

/--
Check a relation between two levels for every value of their parameters.

A level is a function of its parameters built from `+1`, `max` and `imax`. Once
every parameter is larger than the biggest constant in either level, both sides
change in lockstep, so trying every parameter value up to that bound (plus one)
decides the question.
-/
def forallValues (a b : Level) (r : Nat → Nat → Bool) : Bool :=
  let ps := (a.params ++ b.params).eraseDups
  let k := a.depth + b.depth + 1
  (assignments ps k).all fun σ => r (a.eval σ) (b.eval σ)

/-- Level equality: the same value for every value of the parameters. -/
def isEquiv (a b : Level) : Bool := forallValues a b (· == ·)

/-- `a ≤ b` for every value of the parameters. -/
def leq (a b : Level) : Bool := forallValues a b (· ≤ ·)

/-- Is the level `0` whatever the parameters are? -/
def isZero (a : Level) : Bool := isEquiv a zero

/-- Can the level ever be `0`? -/
def mayBeZero (a : Level) : Bool := !forallValues a zero (fun x _ => x != 0)

protected partial def toString : Level → String
  | zero => "0"
  | succ l =>
    let rec count : Level → Nat → (Level × Nat)
      | succ l, n => count l (n + 1)
      | l, n => (l, n)
    match count l 1 with
    | (zero, n) => toString n
    | (base, n) => s!"{Level.toString base}+{n}"
  | max a b => s!"max ({Level.toString a}) ({Level.toString b})"
  | imax a b => s!"imax ({Level.toString a}) ({Level.toString b})"
  | param n => n

instance : ToString Level := ⟨Level.toString⟩

end Level
end MiniLean
