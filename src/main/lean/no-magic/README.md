# no-magic

Companion Lean code for the article
[No Magic: Proving 1 + 2 + … + n = n(n+1)/2 from Paper to Lean's Kernel](../../md/pl/lean-no-magic.md).

The library is core Lean 4 only (no Mathlib).

## Build

With Nix (flakes enabled):

```sh
cd src/main/lean/no-magic
nix develop      # puts elan on PATH
lake build       # elan fetches the Lean version in ./lean-toolchain on first use
```

Without Nix, install [elan](https://github.com/leanprover/elan) and run `lake build`.

## Layout

| File | Purpose |
| --- | --- |
| `lean-toolchain` | Pins the Lean version (read by elan) |
| `lakefile.toml` | Lake build config: one library, `NoMagic` |
| `NoMagic.lean` | Library root |
| `NoMagic/SumFormula.lean` | `sumTo`, the tactic proof, the `Nat.rec` term proof, `sumTo_eq` |
| `flake.nix` | Nix dev shell providing elan |

`lake build` also runs the checks at the end of `SumFormula.lean`. It fails if
`sumTo 100 ≠ 5050`, or if the proofs' axioms change from what the article says
(`#guard_msgs` on `#print axioms`).
