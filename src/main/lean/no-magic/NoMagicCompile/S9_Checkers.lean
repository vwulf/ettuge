import NoMagic

/-!
# Stage 9 — Checking the checker

Stage 8 used Lean's own kernel. Lean 4.36 also ships independent checkers
(`leanchecker-paranoid`, `lean4lean`, `nanoda`, `con-leche`, `con-ron`), run
from the command line rather than from a Lean file:

```sh
lake check              # export the build, replay it through the kernel in a sandbox
lake check --paranoid   # ...and through every bundled independent checker
```

`lake check` needs the `bwrap` sandbox, which exists on Linux only. On macOS it
can be run with `--inadvisably-no-sandbox`, which is reasonable only for code
you wrote yourself, like this project.

Every checker is also asked which axioms the proof rests on. This is the whole
list: one axiom, `propext`, which comes from the core library's proofs of
`Nat.add_mul` and `Nat.mul_div_cancel_left`. There is no `Classical.choice`.
-/

open NoMagic

#print axioms sumTo_eq
