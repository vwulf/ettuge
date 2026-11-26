# no-magic

Companion Lean code for the article
[No Magic: Proving 1 + 2 + … + n = n(n+1)/2 from Paper to Lean's Kernel](../../md/pl/lean-no-magic.md).

Two libraries, core Lean 4 only (no Mathlib):

- **`NoMagic`**: the article's proofs.
- **`NoMagicCompile`**: the same proofs taken apart, one stage per file, from surface syntax down to the kernel. It's the companion to the article.

## Build

With Nix (flakes enabled):

```sh
cd src/main/lean/no-magic
nix develop      # puts elan on PATH
lake build       # elan fetches the Lean version in ./lean-toolchain on first use
```

Without Nix, install [elan](https://github.com/leanprover/elan) and run `lake build`.

## Literate pages

The same files render as a literate website: `/-! … -/` comments become prose,
code becomes highlighted code with hover types, and `#check`/`#print`/`#reduce`
output is shown inline. The site's deploy workflow publishes it at
<https://vwulf.github.io/ettuge/FP/no-magic-literate/>. To build it locally:

```sh
lake query :literateHtml   # prints the output directory
```

This uses [Verso](https://github.com/leanprover/verso), a documentation-only
dependency (pinned to the tag matching `lean-toolchain`). The proofs import
nothing from it. `literate.toml` sets the landing page, the page order and which
commands show their output. Verso is large, so the first build takes a while.

To replay everything through Lean's independent checkers as well:

```sh
lake check --paranoid                          # Linux (needs bwrap)
lake check --paranoid --inadvisably-no-sandbox # macOS; fine for code you wrote
```

Stage 8 imports `Lean` (for the metaprogram), so the export includes Lean's
own library and the paranoid check takes a while.

## Layout

| File | Purpose |
| --- | --- |
| `lean-toolchain` | Pins the Lean version (read by elan) |
| `lakefile.toml` | Lake build config: one library, `NoMagic` |
| `NoMagic.lean` | Library root |
| `NoMagic/SumFormula.lean` | `sumTo`, the tactic proof, the `Nat.rec` term proof, `sumTo_eq` |
| `flake.nix` | Nix dev shell providing elan |
| `literate.toml` | Verso literate-site settings: landing page, order, visible output |
| `NoMagicCompile.lean` | Root of the companion library |
| `NoMagicCompile/S1_Surface.lean` | What you write: notation, implicit arguments, tactics |
| `NoMagicCompile/S2_Notation.lean` | Notation removed: `HMul.hMul`, instances, `OfNat` numerals |
| `NoMagicCompile/S3_Tactics.lean` | Tactics become terms: `show_term`, `#print` |
| `NoMagicCompile/S4_Recursion.lean` | Pattern matching becomes `Nat.brecOn` / `Nat.below` / `Nat.rec` |
| `NoMagicCompile/S5_Primitives.lean` | `Nat`, `Eq` and their recursors (induction, rewriting) |
| `NoMagicCompile/S6_CurryHoward.lean` | `∀` is `Π`; the connectives are inductive types |
| `NoMagicCompile/S7_Computation.lean` | β, δ, ι reduction; `rfl` and a rejected false equation |
| `NoMagicCompile/S8_Kernel.lean` | Declarations handed straight to the kernel: accepted and rejected |
| `NoMagicCompile/S9_Checkers.lean` | Independent checkers (`lake check --paranoid`) and the axiom list |
| `NoMagicCompile/Checks.lean` | Every shown output, pinned with `#guard_msgs` (left off the literate site) |

The stage files are written for reading: plain commands, with Lean's output shown
beneath each one on the literate pages. `NoMagicCompile/Checks.lean` re-runs every
one of those commands inside `#guard_msgs` with the expected output written out,
so `lake build` fails if a Lean upgrade changes anything the pages show.

`lake build` also runs the checks at the end of `SumFormula.lean`. It fails if
`sumTo 100 ≠ 5050`, or if the proofs' axioms change from what the article says
(`#guard_msgs` on `#print axioms`).
