---
name: kannada-ocr-cleaner
description: >
  Audits and fixes OCR artefacts in Kannada text that was scanned from books
  typeset in legacy Kannada fonts (Nudi, Baraha, ISM, etc.). Use this skill
  whenever the user mentions garbled Kannada OCR text, legacy font artefacts,
  arka-ottu reversals, ಯ garbling, or asks to clean up a Kannada .md or .txt
  file produced by OCR. Also triggers for phrases like "OCR errors in Kannada",
  "fix 0iÉ", "arka-ottu problem", "ರ್ wrong in OCR", "legacy font garble",
  "ಣ್ರ should be ರ್ಣ", "ಥ್ರ should be ರ್ಥ", "ಯುೀ should be ಯೇ", or any
  request to correct machine-scanned Kannada text. Invoke proactively whenever
  garbled Latin characters (É, Å, À, ï, õ, Ç, ÂÐ) appear mixed into Kannada
  Unicode text, or when Kannada-script characters appear inside what should be
  English words in a bibliography.
---

# Kannada OCR Cleaner

You help clean Kannada text that was OCR'd from books typeset in legacy
Kannada font encodings (Nudi, Baraha, ISM/CDAC, and similar pre-Unicode
systems). These fonts mapped Kannada glyphs to positions in a Latin codepage,
so OCR software read the glyph shapes and produced Latin characters instead of
the correct Kannada Unicode codepoints.

Three classes of error recur throughout this corpus:

1. **Vowel-sign + consonant garbling** — specific Kannada characters are
   consistently mis-encoded as sequences of Latin bytes.
2. **Arka-ottu reversal** — the RA-half-consonant (ರ್) was read in the wrong
   order, producing consonant+್ರ instead of ರ್+consonant.
3. **English text garbling** — books typeset entirely in the legacy font had
   their English passages (bibliography, titles) garbled into Kannada-like
   characters using the same encoding.

---

## Class 1 — Vowel-sign / consonant garbling

These are **always wrong** when they appear in Kannada Unicode text; replace
unconditionally.

### ಯ garbling (legacy: `0iÉ`)

The consonant ಯ and its associated vowel signs were encoded as the three-byte
Latin string `0iÉ` (U+0030 U+0069 U+00C9). The vowel signs were also
mis-encoded — `ు` (U+0CC1) for short-e (ೆ) and `ುೀ` (U+0CC1+U+0CC0) for
long-e (ೇ):

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

### Residual long-e garble after correctly-recognised ಯ

When ಯ was OCR'd correctly but its long-e vowel sign (ೇ) was still garbled as
`ుೀ`, the result is `ಯುೀ`. This is a separate pattern from `0iÉ` and catches
a further 59 cases (interrogatives, emphatics, etc.):

```python
text = text.replace('\u0CAF\u0CC1\u0CC0', 'ಯೇ')   # ಯ + ు + ೀ → ಯೇ
```

Examples: `ಇದೆಯುೀ?` → `ಇದೆಯೇ?`, `ಹಾಗೆಯುೀ` → `ಹಾಗೆಯೇ`,
`ತಾವಾಗಿಯುೀ` → `ತಾವಾಗಿಯೇ`, `ಕನ್ನಡದಲ್ಲಿವೆಯುೀ?` → `ಕನ್ನಡದಲ್ಲಿವೆಯೇ?`

### Archaic diphthong / ಯ್ in letter-listing contexts (`0iÀiï`)

The sequence `0iÀiï` (U+0030 U+0069 U+00C0 U+0069 U+00EF) is the garbled form
of `ಯ್` (ya + virama) in contexts where the book lists archaic Kannada sound
combinations. Appears as `ಆ0iÀiï` = `ಆಯ್` and `ಅ0iÀiï` = `ಅಯ್`:

```python
text = text.replace('0iÀiï', 'ಯ್')
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
text = text.replace('ವತ್ರಮಾ', 'ವರ್ತಮಾ')     # ವರ್ತಮಾನ (present tense)
text = text.replace('ಕತ್ರರಿ', 'ಕರ್ತರಿ')      # kartari construction
text = text.replace('ಕತ್ರೃ', 'ಕರ್ತೃ')        # kartR (agent noun)
text = text.replace('ಪೂತ್ರಿ', 'ಪೂರ್ತಿ')      # pUrti (completion)
text = text.replace('ಪರಿವತ್ರ', 'ಪರಿವರ್ತ')    # parivarta (change)
text = text.replace('ನಿಧ್ರ', 'ನಿರ್ಧ')        # nirdha- (determination)
text = text.replace('ಅಶೋಕವಧ್ರ', 'ಅಶೋಕವರ್ಧ')  # aSOkavardhana (proper name)
text = text.replace('ಕೃಷ್ಣಮೂತ್ರಿ', 'ಕೃಷ್ಣಮೂರ್ತಿ')  # Krishnamurti (scholar name)
```

---

## Class 3 — English text garbled through legacy font

Books typeset entirely in the legacy font had their English text (bibliography,
foreign book titles) encoded the same way. English words appear as garbled
Kannada-like characters. The font maps ASCII letters to these Kannada codepoints:

| Kannada char | Latin it represents |
|---|---|
| ಅ | C |
| ಆ | D |
| ಇ | E |
| ಐ | L |
| ಏ | K |
| ಎ | J |
| ಖ | R (capital) |
| ಖಿ | T (capital) |
| ಠಿ | p |
| ಚಿ | a |
| ಟಿ | n |
| ಟ | l |
| ಡಿ | r |
| ಜ | d |
| ಜಿ | f |
| ಣ | t |
| ಥಿ | y |

**Recognition cue**: a bibliography line containing Kannada-script characters
*inside* what should be an English title (e.g., `ಖಿhe ಆಡಿಚಿviಜiಚಿಟಿ` = "The
Dravidian"), or an author name containing an isolated Latin letter like `Ç`.

**Fix approach**: decode each garbled token using the table above, then replace
directly. For recurring proper names like Taraporewala, use a string replace:

```python
# Proper name with Ç artefact
text = text.replace('ತಾರಾಪೆÇರೆವಾಲಾ', 'ತಾರಾಪೋರ್ವಾಲಾ')

# Bibliography English titles (exact strings with OCR double-spaces)
text = text.replace('ಖಿhe  ಆಡಿಚಿviಜiಚಿಟಿ  ಐಚಿಟಿguಚಿge', 'The Dravidian Language')
text = text.replace('ಇಡಿgಚಿಣiviಣಥಿ',                     'Ergativity')
text = text.replace('Sಚಿಟಿsಞಡಿiಣ  sಥಿಟಿಣಚಿx',            'Sanskrit syntax')
text = text.replace('ಆeಟhi',                              'Delhi')
text = text.replace('ಅಚಿmbಡಿiಜge',                       'Cambridge')
text = text.replace('ಖeoಡಿಜeಡಿiಟಿg  ಡಿuಟes  iಟಿ',       'Reordering rules in')
text = text.replace('ಏಚಿಟಿಟಿಚಿಜಚಿ  ಠಿಡಿeಜಿixಚಿಣioಟಿ',    'Kannada prefixation')
text = text.replace('PIಐಅ  ಎouಡಿಟಿಚಿಟ  oಜಿ',            'PILC Journal of')
```

Note: OCR of these books typically inserts double spaces between words. Match
the exact spacing when writing replacement strings.

---

## Audit workflow

Before writing fix scripts, always audit the actual frequency and context of
each pattern so you understand what you're changing:

```python
import re

src = '/path/to/file-kn.md'
text = open(src, encoding='utf-8').read()
lines = text.split('\n')

# Frequency audit — Class 1 + 2 patterns
patterns = [
    '0iÉ',                          # ಯ garbling
    '\u0CAF\u0CC1\u0CC0',           # ಯ + residual long-e (ಯುೀ)
    '0iÀiï',                        # archaic ಯ್ diphthong
    'ಣ್ರ', 'ಥ್ರ', 'ಮ್ರ', 'ಯ್ರ',   # arka-ottu reversals
    'ಙõï', 'ÂÐ', 'ಬಹÅ', 'ದೀಘ್ರ',  # other Class 1
]
for p in patterns:
    n = text.count(p)
    if n:
        print(f'{n:4d}  {repr(p)}')

# Check for Class 3: Kannada chars inside English-dominant lines
for i, ln in enumerate(lines, 1):
    import unicodedata
    kn = sum(1 for c in ln if '\u0C80' <= c <= '\u0CFF')
    lat = sum(1 for c in ln if c.isascii() and c.isalpha())
    if 0 < kn < 8 and lat > 5:   # few Kannada chars, more Latin = garbled English
        print(f'  Possible Class 3 line {i}: {ln.strip()[:80]}')

# Context sampling
def show_context(pattern, n=5):
    for i, ln in enumerate(lines, 1):
        if pattern in ln:
            print(f'  line {i}: {ln.strip()[:90]}')
            n -= 1
            if not n:
                break
```

Key things to audit before applying global replacements:
- Are there any false positives? (e.g., does `ಮ್ರ` appear in words where it
  should NOT be ರ್ಮ?)
- Do line-split cases exist? (OCR sometimes breaks a word across lines; e.g.,
  `ಯೆಂಬು \nದ` should be `ಯೆಂಬುದ`)
- Does `ಯುೀ` appear after vowels other than ಯ? (In book 28 it did not — all
  59 were after ಯ — but audit for each new book.)

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

# ── Class 1: vowel-sign / consonant garbling ──
text = re.sub(r'0iÉు(\s*)(?=ಯ)', r'\1', text)
counts['0iÉు before ಯ (ordinals)'] = 0   # re.sub doesn't return count; check separately
rep('0iÉుೀ', 'ಯೇ')
rep('0iÉు',  'ಯೆ')
rep('0iÉ',   'ಯ')
rep('\u0CAF\u0CC1\u0CC0', 'ಯೇ', 'ಯುೀ→ಯೇ (residual long-e after ಯ)')
rep('0iÀiï', 'ಯ್', '0iÀiï→ಯ್ (archaic diphthong)')
rep('ಙõï', 'ಙ್')
rep('ÂÐ',  'ಙ್')
rep('ಬಹÅ', 'ಬಹು')

# ── Class 2: arka-ottu reversals ──
rep('ಣ್ರ', 'ರ್ಣ')
rep('ಥ್ರ', 'ರ್ಥ')
rep('ಮ್ರ', 'ರ್ಮ')
rep('ಯ್ರ', 'ರ್ಯ')
rep('ದೀಘ್ರ', 'ದೀರ್ಘ')
rep('ವತ್ರಮಾ', 'ವರ್ತಮಾ')
rep('ಕತ್ರರಿ', 'ಕರ್ತರಿ')
rep('ಕತ್ರೃ', 'ಕರ್ತೃ')
rep('ಪೂತ್ರಿ', 'ಪೂರ್ತಿ')
rep('ಪರಿವತ್ರ', 'ಪರಿವರ್ತ')
rep('ನಿಧ್ರ', 'ನಿರ್ಧ')
rep('ಅಶೋಕವಧ್ರ', 'ಅಶೋಕವರ್ಧ')
rep('ಕೃಷ್ಣಮೂತ್ರಿ', 'ಕೃಷ್ಣಮೂರ್ತಿ')

# ── Class 3: bibliography / English garbling (add as discovered) ──
rep('ತಾರಾಪೆÇರೆವಾಲಾ', 'ತಾರಾಪೋರ್ವಾಲಾ')
# ... add other bibliography entries

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

- **Initial `ಕ್ರ`, `ಪ್ರ`, `ಮಾತ್ರ`, `ಸೂತ್ರ`, `ಚಾರಿತ್ರ`**: these are correct.
- **Any `ತ್ರ` not in the word-specific list above**: audit before touching.
- **`ಯ` + `ు`** without the following `ೀ`: this is legitimate ಯು (ya+u),
  not a garble. Only the three-character sequence ಯ+ు+ೀ is wrong.
