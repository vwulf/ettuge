# MiniLean

A small type checker for a dependent type theory, written in Lean 4 after the
book [MiniLean4](https://learn.h5i.dev/). It proves the sum formula
2 · (1 + 2 + ⋯ + n) = n(n + 1) from an empty environment, with no axioms.

Companion to the articles
[MiniLean: The No Magic Proof in a Kernel You Can Read](../../md/pl/minilean.md) and
[No Magic](../../md/pl/lean-no-magic.md).

## Build

```sh
cd src/main/lean/minilean
nix develop      # or install elan yourself
lake build
```

`lake build` runs MiniLean's kernel on every declaration in `MiniLean/Prelude.lean`
and `MiniLean/Rejections.lean`. If MiniLean rejects a declaration that should be
accepted, or accepts one that should be rejected, the build fails.

## Layout

| File | Lines | Trusted? | Purpose |
| --- | --- | --- | --- |
| `MiniLean/Level.lean` | 110 | yes | universe levels, level equality |
| `MiniLean/Expr.lean` | 180 | yes | terms, substitution, abstraction, printing |
| `MiniLean/Env.lean` | 62 | yes | the environment of declarations |
| `MiniLean/Kernel.lean` | 385 | yes | `whnf` (β δ ι), `isDefEq`, `infer`, declarations, recursor generation |
| `MiniLean/Surface.lean` | 68 | no | name resolution |
| `MiniLean/Tactic.lean` | 240 | no | `intro`, `exact`, `refl`, `show`, `induction`, `rw` |
| `MiniLean/DSL.lean` | 289 | no | the `mini_…` commands |
| `MiniLean/Prelude.lean` | 169 | — | `Nat`, `Eq`, `add`, `mul`, `sumTo`, nine lemmas, the theorem |
| `MiniLean/Rejections.lean` | 83 | — | wrong declarations the kernel must refuse |

Only the first four files are trusted. Everything else produces terms that the
kernel checks.

## The DSL

```lean
mini_inductive Nat : Type where
  | zero : Nat
  | succ : Nat → Nat

mini_def add (m n : Nat) : Nat :=
  Nat.rec.{1} (λ (k : Nat) => Nat) m (λ (k ih : Nat) => succ ih) n

mini_theorem zero_add (n : Nat) : NatEq (add zero n) n := by
  induction n
  · refl
  · intro k ih
    show NatEq (succ (add zero k)) (succ k)
    rw [ih]
```

Commands: `mini_inductive`, `mini_def`, `mini_theorem`, `mini_open`, `#mini_check`,
`#mini_reduce`, `#mini_print`, `#mini_verdict`. The MiniLean environment lives in
a Lean environment extension and is not saved between files, so a development
lives in one file.
