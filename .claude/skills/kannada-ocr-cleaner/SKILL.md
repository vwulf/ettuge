---
name: kannada-ocr-cleaner
description: >
  Audits and fixes OCR artefacts in Kannada text that was scanned from books
  typeset in legacy Kannada fonts (Nudi, Baraha, ISM, etc.). Use this skill
  whenever the user mentions garbled Kannada OCR text, legacy font artefacts,
  arka-ottu reversals, ಯ garbling, or asks to clean up a Kannada .md or .txt
  file produced by OCR. Also triggers for phrases like "OCR errors in Kannada",
  "fix 0iÉ", "arka-ottu problem", "ರ್ wrong in OCR", "legacy font garble",
  "ಣ್ರ should be ರ್ಣ", "ಥ್ರ should be ರ್ಥ", or any request to correct
  machine-scanned Kannada text. Invoke proactively whenever garbled Latin
  characters (É, Å, ï, õ, ÂÐ) appear mixed into Kannada Unicode text.
---

# Kannada OCR Cleaner

You help clean Kannada text that was OCR'd from books typeset in legacy
Kannada font encodings (Nudi, Baraha, ISM/CDAC, and similar pre-Unicode
systems). These fonts mapped Kannada glyphs to positions in a Latin codepage,
so OCR software read the glyph shapes and produced Latin characters instead of
the correct Kannada Unicode codepoints.

Two classes of error recur throughout this corpus:

1. **Vowel-sign + consonant garbling** — specific Kannada characters are
   consistently mis-encoded as sequences of Latin bytes.
2. **Arka-ottu reversal** — the RA-half-consonant (ರ್, written as a superscript
   above the following consonant) was read in the wrong order, producing
   consonant+್ರ instead of ರ್+consonant.

---

## Class 1 — Vowel-sign / consonant garbling

These are **always wrong** when they appear in Kannada Unicode text; replace
unconditionally.

### ಯ garbling (legacy: `0iÉ`)

The consonant ಯ and its associated vowel signs were encoded as the three-byte
Latin string `0iÉ` (U+0030 U+0069 U+00C9). The following vowel signs were also
mis-encoded:

| OCR output | Correct | Notes |
|------------|---------|-------|
| `0iÉ` + `ుೀ` | `ಯೇ` | long-e particle: ಯೇಕೆ, ಯೇನು |
| `0iÉ` + `ు` | `ಯೆ` | short-e: ಯೆಂಬ, ಯೆಂದು, ಯೆಂತ, ಯೆನ್ನ |
| `0iÉ` + `ు` before real ಯ | delete `0iÉు` | ordinals: ದ್ವಿತೀ**0iÉు**ಯ → ದ್ವಿತೀಯ |
| `0iÉ` alone | `ಯ` | before virama: ಗೆಯ್ಮ, ಆಯ್ಕ |

Apply in this order (most specific first):
```python
import re
text = re.sub(r'0iÉు(\s*)(?=ಯ)', r'\1', text)  # rule 1: ordinals
text = text.replace('0iÉుೀ', 'ಯೇ')             # rule 2: long-e
text = text.replace('0iÉు', 'ಯೆ')              # rule 3: short-e
text = text.replace('0iÉ', 'ಯ')               # rule 4: standalone
```

### Sanskrit tense-marker garbling (ಙ್)

The halanta form ಙ್ (used in Sanskrit verb forms ಲಙ್, ತಿಙ್, ಲುಙ್, ಲೃಙ್) was
garbled as `ಙõï` or the two-byte sequence `ÂÐ`:

```python
text = text.replace('ಙõï', 'ಙ್')
text = text.replace('ÂÐ', 'ಙ್')
```

### ಬಹು garbling (`ಬಹÅ`)

The word ಬಹು (bahu = "can", as in ಬಳಸಬಹುದು "can use") was garbled as `ಬಹÅ`:

```python
text = text.replace('ಬಹÅ', 'ಬಹು')
```

---

## Class 2 — Arka-ottu reversal

The arka-ottu is the half-form of ರ (RA) written as a superscript above its
following consonant. In correct Kannada, the cluster is **ರ್ + C** (ra +
virama + consonant). OCR of legacy fonts frequently reversed this, producing
**C + ್ರ** (consonant + virama + ra).

### The cardinal rule: only mid- and end-of-word

Initial consonant clusters beginning with ಕ್ರ, ಪ್ರ, ವ್ರ, ಶ್ರ, etc. are
**correct** — the arka-ottu never starts a word. These must NOT be changed:

| Leave alone | Why |
|-------------|-----|
| ಕ್ರಿಯಾ, ಪ್ರತ್ಯಯ | initial ಕ್ರ, ಪ್ರ |
| ಮಾತ್ರ, ಸೂತ್ರ | ತ್ರ is a legitimate medial cluster |
| ಸ್ವತಂತ್ರ, ಚಾರಿತ್ರಿಕ | same |
| ಸ್ತ್ರೀ | initial ಸ್ತ್ರ |

### Global-safe reversals

These C+್ರ combinations do **not** occur naturally in Kannada, so replacement
is always correct:

| OCR output | Correct | Frequency | Common words |
|------------|---------|-----------|--------------|
| `ಣ್ರ` | `ರ್ಣ` | high | ಪೂರ್ಣ, ಸಂಪೂರ್ಣ, ಅಪೂರ್ಣ, ವರ್ಣ |
| `ಥ್ರ` | `ರ್ಥ` | very high | ಅರ್ಥ (artha = meaning — extremely common) |
| `ಮ್ರ` | `ರ್ಮ` | high | ಕರ್ಮ, ಗುಣಧರ್ಮ, ಸಕರ್ಮಕ, ಅಕರ್ಮಕ |
| `ಯ್ರ` | `ರ್ಯ` | medium | ಕಾರ್ಯ, ಸೂರ್ಯ, ಆಶ್ಚರ್ಯ, ಸೌಜನ್ಯ |
| `ದೀಘ್ರ` | `ದೀರ್ಘ` | low | dīrgha = long vowel (linguistics term) |

```python
text = text.replace('ಣ್ರ', 'ರ್ಣ')
text = text.replace('ಥ್ರ', 'ರ್ಥ')
text = text.replace('ಮ್ರ', 'ರ್ಮ')
text = text.replace('ಯ್ರ', 'ರ್ಯ')
text = text.replace('ದೀಘ್ರ', 'ದೀರ್ಘ')
```

### Word-specific `ತ್ರ` and `ಧ್ರ` reversals

Because `ತ್ರ` also appears legitimately (ಮಾತ್ರ, ಸೂತ್ರ, ಸ್ವತಂತ್ರ), only fix
specific known-wrong words:

```python
# vartamAna (present tense) — very common in grammar books
text = text.replace('ವತ್ರಮಾ', 'ವರ್ತಮಾ')     # ವರ್ತಮಾನ

# kartari/karmaNi constructions
text = text.replace('ಕತ್ರರಿ', 'ಕರ್ತರಿ')
text = text.replace('ಕತ್ರೃ', 'ಕರ್ತೃ')        # kartR (agent noun)

# pUrti (completion), parivarta (change)
text = text.replace('ಪೂತ್ರಿ', 'ಪೂರ್ತಿ')
text = text.replace('ಪರಿವತ್ರ', 'ಪರಿವರ್ತ')

# nirdha- (determination, as in nirdharisu)
text = text.replace('ನಿಧ್ರ', 'ನಿರ್ಧ')

# aSOkavardhana (proper name in Sanskrit citation)
text = text.replace('ಅಶೋಕವಧ್ರ', 'ಅಶೋಕವರ್ಧ')
```

---

## Audit workflow

Before writing fix scripts, always audit the actual frequency and context of
each pattern so you understand what you're changing:

```python
import re

src = '/path/to/file-kn.md'
text = open(src, encoding='utf-8').read()
lines = text.split('\n')

# Frequency audit
patterns = ['0iÉ', 'ಣ್ರ', 'ಥ್ರ', 'ಮ್ರ', 'ಯ್ರ', 'ಙõï', 'ÂÐ', 'ಬಹÅ', 'ದೀಘ್ರ']
for p in patterns:
    n = text.count(p)
    if n:
        print(f'{n:4d}  {p}')

# Context sampling — see the 5 lines around first occurrence
def show_context(pattern, n=5):
    for i, ln in enumerate(lines, 1):
        if pattern in ln:
            print(f'  line {i}: {ln.strip()[:90]}')
            n -= 1
            if not n:
                break

show_context('ಮ್ರ')   # check: are all ಮ್ರ really karma-reversals?
```

Key things to audit before applying global replacements:
- Are there any false positives? (e.g., does `ಮ್ರ` appear in words where it
  should NOT be ರ್ಮ?)
- Do line-split cases exist? (OCR sometimes breaks a word across lines; e.g.,
  `ಯೆಂಬು \nದ` should be `ಯೆಂಬುದ`)
- Are there rare Latin artefacts not yet catalogued? (Grep for `[A-Za-z0-9Å-ÿ]`
  in otherwise Kannada lines)

---

## Fix script template

Always write a single script per cleanup pass, print a count summary, spot-
check a few lines, and write back in-place:

```python
#!/usr/bin/env python3
import re

SRC = '/path/to/file-kn.md'
text = open(SRC, encoding='utf-8').read()
counts = {}

def rep(old, new, label=None):
    global text
    n = text.count(old)
    text = text.replace(old, new)
    counts[label or f'{old}→{new}'] = n

# ── Class 1: vowel-sign garbling ──
text = re.sub(r'0iÉు(\s*)(?=ಯ)', r'\1', text); counts['0iÉు before ಯ (ordinals)'] = ...
rep('0iÉుೀ', 'ಯೇ')
rep('0iÉు',  'ಯೆ')
rep('0iÉ',   'ಯ')
rep('ಙõï', 'ಙ್')
rep('ÂÐ',  'ಙ್')
rep('ಬಹÅ', 'ಬಹು')

# ── Class 2: arka-ottu reversals ──
rep('ಣ್ರ', 'ರ್ಣ')
rep('ಥ್ರ', 'ರ್ಥ')
rep('ಮ್ರ', 'ರ್ಮ')
rep('ಯ್ರ', 'ರ್ಯ')
rep('ದೀಘ್ರ', 'ದೀರ್ಘ')

# ── Word-specific ──
rep('ವತ್ರಮಾ', 'ವರ್ತಮಾ')
rep('ಕತ್ರರಿ', 'ಕರ್ತರಿ')
# ... add others as discovered

# ── Report ──
total = sum(counts.values())
for label, n in counts.items():
    if n: print(f'  {n:4d}  {label}')
print(f'  ──── {total} total')

with open(SRC, 'w', encoding='utf-8') as f:
    f.write(text)
print(f'Written: {SRC}')
```

---

## After fixing kn.md — regenerate kn-eke.md

If the book has a `-kn-eke.md` Eke romanisation file, re-run the transliterator
after every batch of fixes:

```bash
python3 /tmp/kn_to_eke.py
```

Verify the ratio printed is ~1.00 (KN source tokens ≈ EKE output tokens).
Large deviations mean text was accidentally deleted or duplicated.

---

## What NOT to fix automatically

- **`Ç`** in proper names like *Taraporewala* (appears in Sanskrit grammar
  citations): leave for manual review — it's part of a transcribed title.
- **`0iÀiï`**: archaic Kannada letter listing (ೞ-related); leave as-is.
- **Initial `ಕ್ರ`, `ಪ್ರ`, `ಮಾತ್ರ`, `ಸೂತ್ರ`, `ಚಾರಿತ್ರ`**: these are correct.
- **Any `ತ್ರ` not in the word-specific list above**: audit before touching.
