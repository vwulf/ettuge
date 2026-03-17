---
name: kannada-ocr-cleaner
description: >
  Audits and fixes OCR artefacts in Kannada text that was scanned from books
  typeset in legacy Kannada fonts (Nudi, Baraha, ISM, etc.). Use this skill
  whenever the user mentions garbled Kannada OCR text, legacy font artefacts,
  arka-ottu reversals, ಯ garbling, orphaned word fragments, embedded running
  headers, or asks to clean up a Kannada .md or .txt file produced by OCR.
  Also triggers for phrases like "OCR errors in Kannada", "fix 0iÉ",
  "arka-ottu problem", "ರ್ wrong in OCR", "legacy font garble", "ಣ್ರ should
  be ರ್ಣ", "ಥ್ರ should be ರ್ಥ", "ಯುೀ should be ಯೇ", "page-break fragments",
  "words isolated before section headings", "chapter title appearing mid-text",
  "running header in body text", or any request to correct machine-scanned
  Kannada text. Invoke proactively whenever garbled Latin characters (É, Å, À,
  ï, õ, Ç, ÂÐ) appear mixed into Kannada Unicode text, when Kannada-script
  characters appear inside what should be English words in a bibliography, or
  when short isolated Kannada lines appear before section headings.
---

# Kannada OCR Cleaner

You help clean Kannada text that was OCR'd from books typeset in legacy
Kannada font encodings (Nudi, Baraha, ISM/CDAC, and similar pre-Unicode
systems). These fonts mapped Kannada glyphs to positions in a Latin codepage,
so OCR software read the glyph shapes and produced Latin characters instead of
the correct Kannada Unicode codepoints.

Four classes of error recur throughout this corpus:

1. **Vowel-sign + consonant garbling** — specific Kannada characters are
   consistently mis-encoded as sequences of Latin bytes.
2. **Arka-ottu reversal** — the RA-half-consonant (ರ್) was read in the wrong
   order, producing consonant+್ರ instead of ರ್+consonant.
3. **English text garbling** — books typeset entirely in the legacy font had
   their English passages (bibliography, titles) garbled into Kannada-like
   characters using the same encoding.
4. **OCR page-break structural artifacts** — paragraph-final words from the
   bottom of a page appear as isolated lines before the next section heading,
   and chapter-title running headers from print page-tops appear as standalone
   lines embedded mid-paragraph. These are structural, not character-level.

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

## Class 4 — OCR page-break structural artifacts

When OCR processes a multi-page book, two types of structural junk appear that
**no character-level replacement can fix** — they require line-level surgery.

### Type A: Orphaned fragments before section headings

The last few words of a print page appear as short isolated lines (each
preceded by a blank line) just before the next section heading:

```
ಹೇಳಿ ಕೊಡುವುದು ಹೇಗೆ ತಪ್ಪಾಗುತ್ತದೆಯೋ ಹಾಗೆಯೇ ಇದೂ ಕೂಡ.
                        ← paragraph ends here

ವ್ಯಾಕರಣವೆಂಬುದು         ← orphaned fragment (blank before and after)

ನುಡಿಯಿಂದ               ← orphaned fragment

ನುದಿಗೆ                 ← orphaned fragment

1.2  ವ್ಯಾಕರಣದ ಉದ್ದೇಶ    ← section heading (trigger)
```

**Fix**: join all orphaned fragments to the preceding paragraph, remove
the blank lines between them, and keep one blank before the section heading.

### Type B: Running chapter headers

The print book's page-top chapter-title header gets OCR'd into the text flow
as a standalone line, typically appearing between an orphaned fragment and the
next line of body text:

```
ಮಸೂರವನ್ನು                 ← orphaned fragment

ಮುನ್ನೋಟ                  ← chapter title from print page header (intruder)

ಸಂಬಂಧಿಸಿದಂತಹ ಚಟುವಟಿಕೆಗಳನ್ನು...  ← body text continues
```

**Fix**: join the fragment to the preceding paragraph, delete the running
header line and the blank lines surrounding it.

### The critical detection rule

A line is an **orphaned fragment** only if ALL of these hold:
- It contains Kannada text
- It is **preceded by a blank line** (this is the critical check — wrapped
  paragraph lines are *not* preceded by blanks, so they are not fragments)
- It is short (< 65 chars)
- It does not start a section heading (`N.N xxx`), chapter heading (`## …`),
  anchor (`<a id`), or nav link (`[…]`)
- It is not itself a known running header title

Without the "preceded by blank" guard, normal wrapped paragraph lines like
`ಹೇಳಿ ಕೊಡುವುದು ಹೇಗೆ ತಪ್ಪಾಗುತ್ತದೆಯೋ ಹಾಗೆಯೇ ಇದೂ ಕೂಡ.` (which are short)
get misidentified as fragments.

### Chapter boundary lines — never delete, never use as target

When walking backward from a section heading to find the paragraph to append
fragments to, skip over these **chapter boundary** lines (they must be
preserved in the output):

- Lines starting with `## ` (chapter `##` headings)
- Lines starting with `<a id` (anchor tags)
- Lines starting with `[` and containing `→` or `->` (nav links)
- Blank lines

The fragment target is the last **body text** line before any boundary lines.
This handles the cross-chapter case where fragments appear between a `##`
chapter heading and the first subsection heading of that chapter.

### Running chapter headers to recognise (book 28)

Build a set of known running header titles specific to the book. For book 28
(*ಕನ್ನಡಕ್ಕೆ ಬೇಕು ಕನ್ನಡದ್ದೇ ವ್ಯಾಕರಣ*), these are the 12 chapter names:

```python
RUNNING_HEADERS = {
    'ಮುನ್ನೋಟ', 'ಸೇರಿಕೆಯ ನಿಯಮಗಳು', 'ಪದವಗ್ರಗಳು', 'ಪದಗಳ ಒಳರಚನೆ',
    'ಸಮಾಸಗಳು', 'ಲಿಂಗ ಮತ್ತು ವಚನಗಳು', 'ವಿಭಕ್ತಿಗಳು ಮತ್ತು ಕಾರಕಗಳು',
    'ವಿಭಕ್ತಿಗಳು', 'ವಿಭಕ್ತಿಪಲ್ಲಟ', 'ಸವ್ರನಾಮಗಳು ಮತ್ತು ಎಣಿಕೆಯ ಪದಗಳು',
    'ಕ್ರಿಯಾರೂಪಗಳು', 'ಮುಕ್ತಾಯ',
}
```

For each new book, grep for lines that match the chapter titles exactly to
build this set.

### Fix script pattern (three-pass)

The fix requires a three-pass approach because edits interact — the same
target line may receive fragments from multiple adjacent sections:

```python
#!/usr/bin/env python3
import re

SRC = '/path/to/file-kn.md'
lines = open(SRC, encoding='utf-8').readlines()

BODY_START = 354   # line index where body text begins (after frontmatter/TOC)

sec_pat = re.compile(r'^\d+\.\d[\d.]*\s+[\u0C80-\u0CFF]')  # N.N KannadaText
kan_re  = re.compile(r'[\u0C80-\u0CFF]')

RUNNING_HEADERS = { ... }   # chapter titles for this book

def is_chapter_boundary(s):
    if not s: return True
    if s.startswith('## '): return True
    if s.startswith('<a id'): return True
    if s.startswith('[') and ('→' in s or '->' in s): return True
    return False

def is_fragment(lines, idx):
    if idx < BODY_START: return False
    s = lines[idx].strip()
    if not s: return False
    if not kan_re.search(s): return False
    if sec_pat.match(s): return False
    if s.startswith('##') or s.startswith('<') or s.startswith('['): return False
    if s in RUNNING_HEADERS: return False
    if any(c in s for c in ['+', '=', '→', '|']): return False
    if len(s) > 65: return False
    # CRITICAL: must be preceded by a blank line
    if idx > 0 and lines[idx - 1].strip() != '': return False
    return True


# ── Pass 1: collect all fixes ──────────────────────────────────────────────

fixes = []

for trigger_idx in range(BODY_START, len(lines)):
    s = lines[trigger_idx].strip()
    is_sec = bool(sec_pat.match(s))
    is_rh  = s in RUNNING_HEADERS
    if not is_sec and not is_rh: continue

    # Walk backward collecting orphaned fragments
    frags = []
    j = trigger_idx - 1
    while j >= BODY_START and lines[j].strip() == '': j -= 1
    while j >= BODY_START:
        if lines[j].strip() == '': j -= 1; continue
        if is_fragment(lines, j): frags.insert(0, j); j -= 1
        else: break

    if not frags:
        if is_rh:
            fixes.append({'type': 'delete_rh_only', 'trigger': trigger_idx})
        continue

    wall_idx = j  # last non-blank non-fragment line (may be a boundary line)
    target_idx = wall_idx
    while target_idx >= BODY_START and is_chapter_boundary(lines[target_idx].strip()):
        target_idx -= 1
    if target_idx < BODY_START or not lines[target_idx].strip(): continue

    fixes.append({
        'type': 'sec' if is_sec else 'rh',
        'trigger': trigger_idx, 'frags': frags,
        'wall': wall_idx, 'target': target_idx,
    })


# ── Pass 2: build to_delete / modify sets ─────────────────────────────────

to_delete = set()
modify    = {}

for fix in fixes:
    t = fix['type']

    if t == 'delete_rh_only':
        to_delete.add(fix['trigger'])
        k = fix['trigger'] - 1; removed = 0
        while k >= BODY_START and lines[k].strip() == '' and removed < 2:
            to_delete.add(k); k -= 1; removed += 1
        continue

    frags = fix['frags']; trigger = fix['trigger']
    wall  = fix['wall'];  target  = fix['target']

    # Append joined fragment text to target line
    frag_text = ' '.join(lines[f].strip() for f in frags)
    modify[target] = lines[target].rstrip() + ' ' + frag_text + '\n'

    for f in frags: to_delete.add(f)
    # Delete blank lines between fragments
    for k in range(frags[0], frags[-1] + 1):
        if lines[k].strip() == '': to_delete.add(k)
    # Delete blank lines between wall/target and first fragment (keep boundaries)
    start_del = wall + 1 if is_chapter_boundary(lines[wall].strip()) else target + 1
    for k in range(start_del, frags[0]):
        if lines[k].strip() == '': to_delete.add(k)
    # Delete blanks between last fragment and trigger
    blanks_after = [k for k in range(frags[-1] + 1, trigger) if lines[k].strip() == '']
    if t == 'sec':
        for b in blanks_after[:-1]: to_delete.add(b)  # keep one blank before heading
    else:  # running header: delete all + the trigger itself
        for b in blanks_after: to_delete.add(b)
        to_delete.add(trigger)


# ── Pass 3: build output ───────────────────────────────────────────────────

result = []
for i, line in enumerate(lines):
    if i in to_delete: continue
    result.append(modify[i] if i in modify else line)

with open(SRC, 'w', encoding='utf-8') as f:
    f.writelines(result)
```

### Audit before running

Before running the fix script, verify the patterns are what you expect:

```python
# Count section headings with preceding blank-line-separated short Kannada lines
import re
lines = open(SRC, encoding='utf-8').readlines()
sec_pat = re.compile(r'^\d+\.\d[\d.]*\s+[\u0C80-\u0CFF]')
for i, ln in enumerate(lines):
    if i < BODY_START: continue
    if sec_pat.match(ln.strip()):
        j = i - 1
        while j >= 0 and lines[j].strip() == '': j -= 1
        if j >= 0 and len(lines[j].strip()) < 65 and lines[j-1].strip() == '':
            print(f'L{i+1}: {ln.strip()[:60]}  ← possible fragment at L{j+1}')

# Verify running header occurrences
for rh in RUNNING_HEADERS:
    hits = [(i+1, ln.strip()) for i, ln in enumerate(lines) if ln.strip() == rh]
    if hits:
        print(f'{rh}: {len(hits)} hits at lines {[h[0] for h in hits]}')
```

Report produced by the script (book 28 example):
```
Section headings with fragments fixed: 12
Running headers with fragments fixed:  4
Running headers deleted (no frags):    4
Total lines deleted:  96
Total lines modified: 16
Output lines: 9517  (was 9613)
```

---

## What NOT to fix automatically

- **Initial `ಕ್ರ`, `ಪ್ರ`, `ಮಾತ್ರ`, `ಸೂತ್ರ`, `ಚಾರಿತ್ರ`**: these are correct.
- **Any `ತ್ರ` not in the word-specific list above**: audit before touching.
- **`ಯ` + `ు`** without the following `ೀ`: this is legitimate ಯು (ya+u),
  not a garble. Only the three-character sequence ಯ+ు+ೀ is wrong.
- **Wrapped paragraph lines**: short Kannada lines that are *not* preceded by
  a blank line. These are normal text wrapping, not orphaned fragments.
- **Table labels and diagram captions**: short Kannada words in phonetic charts,
  vowel triangles, or numbered example lists — check context before treating
  as fragments. The "preceded by blank" rule usually protects these.
