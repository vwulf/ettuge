# Haskell Directory — CLAUDE.md

Haskell source files for functional programming examples and music composition.

---

## Files

| File | Description |
|------|-------------|
| `accum.hs` | Accumulator examples |
| `cat.hs` | Categorical / functional composition examples |
| `reflection.hs` | Reflection utilities |
| `sqrt.hs` | Square root implementations |
| `ಕಳ್ಳ.hs` | Kannada-named Haskell file (Unicode filename — do not rename) |

## Subdirectories

- `euterpea/` — Music composition using the Euterpea library (`rangapura.hs`, `twinkle.hs`)
- `quick/` — Quick Haskell project managed with Stack

---

## Build & Run

### Quick project (Stack)
```bash
cd src/main/haskell/quick
stack build
stack test
```

### Euterpea music examples
Requires Euterpea installed separately:
```bash
ghc src/main/haskell/euterpea/rangapura.hs
```

### Standalone scripts
Files in the root `haskell/` directory are standalone — compile directly with `ghc`:
```bash
ghc src/main/haskell/sqrt.hs
```

---

## Notes
- There is no top-level Cabal or Stack project for standalone files — only `quick/` uses Stack
- Unicode filenames (Kannada script, e.g. `ಕಳ್ಳ.hs`) are intentional; do not rename or transliterate them
- See root `CLAUDE.md` for Unicode handling guidelines (U+0C80–U+0CFF range)
