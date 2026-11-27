import MiniLean.Rejections

/-!
# Stage 9 — Checking the checker

The Lean proof of the sum formula was checked by Lean's kernel and by five
independent checkers. MiniLean is one more, written separately, and its
trusted part is small enough to read: about 745 lines in four modules.

| Module | Lines | What it trusts itself to do |
| --- | --- | --- |
| `MiniLean.Level` | 110 | compare universe levels |
| `MiniLean.Expr` | 180 | substitute and abstract variables |
| `MiniLean.Env` | 62 | store accepted declarations |
| `MiniLean.Kernel` | 393 | reduce, compare, infer types, check declarations, generate recursors |

The name resolution, the tactics and the DSL are not trusted. A bug there can
make a proof fail, but every term they produce is checked by the kernel.

A checker must also refuse. `MiniLean.Rejections` holds one wrong declaration
for each guard: a false equation, `Type : Type`, a non-positive inductive
type, a field in too large a universe, and data computed from a proof of a
disjunction. Each rejection is pinned, so the project builds only if all of
them are refused.

What the whole proof rests on:
-/

#mini_print Nat
#mini_print Eq

/-!
And nothing else: MiniLean has no axioms. Every lemma in `MiniLean.Prelude` was
proved by induction from the recursors these two declarations generated.
-/
