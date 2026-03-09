# /coin-word

Invoke the `ellara-kannada-word-coiner` skill to coin a native Dravidian Kannada word for a given English term.

## Usage

```
/coin-word <english-term>
/coin-word <english-term-1>, <english-term-2>, ...
```

## What it does

1. Reads the `ellara-kannada-word-coiner` skill
2. Applies DNS Bhat's 7-step word-generation algorithm
3. Returns: Kannada script + Eke romanization + morphological breakdown + pattern analogy

## Examples

```
/coin-word democracy
/coin-word software, algorithm, database
/coin-word artificial intelligence
```

## Notes

- Output always includes Eke romanization alongside Kannada script
- No Sanskrit borrowings — only native Dravidian roots
- Cites the morphological pattern used (e.g., "like ನುಡಿಯರಿಗ → linguist")
