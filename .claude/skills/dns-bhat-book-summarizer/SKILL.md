---
name: dns-bhat-book-summarizer
description: >
  Generates chapter-wise English summaries with source pointers and Eke romanisation
  files for DNS Bhat Kannada linguistics books in the ettuge repository.
  Use this skill whenever the user asks to: summarize a DNS Bhat book, create an
  English summary for a book in the dnsbhat folder, generate Eke transliteration
  of Kannada content, add chapter pointers to an -en.md file, create a claude-prompt
  for a DNS Bhat book, cross-link Kannada and English versions of a book, or produce
  a *-kn-eke.md romanisation file. Triggers on phrases like "summarize book NN",
  "create English summary", "generate Eke", "add chapter pointers", "create prompt
  for book", or any reference to producing -en.md / -kn-eke.md files for the DNS Bhat collection.
---

# DNS Bhat Book Summarizer

You produce two kinds of output for DNS Bhat linguistics books in:
`/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/`

1. **`{NN}-{slug}-en.md`** — Chapter-wise English summary with cross-links to Kannada source and Eke romanisation
2. **`{NN}-{slug}-kn-eke.md`** — Eke romanisation of the Kannada content, structured with section anchors

These are companion files to the existing Kannada source (`-kn.md` or `-blog.md` or `-book.md`). They make the content accessible to non-Kannada-readers while preserving precise links back to the original.

---

## Step 1: Identify source material

Before writing anything, read the target book folder:

```
/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/{NN}-{slug}/
```

Check which files exist:
- `*-book.md` — full book text (highest quality, use first)
- `*-blog.md` — blog posts (use if no book.md)
- `*-kn.md` — structured Kannada (use for chapter structure)
- `*-djvu.md` — DjVu OCR (fallback, may be noisy)
- `*-en.md` — existing English summary (update if present, don't overwrite good content)
- `*-kn-eke.md` — existing Eke file (update if present)
- `*-claude-prompt.md` — AI prompt (separate from what we produce here)

Read the primary source file **and** `*-kn.md` if it exists (for chapter structure). For books with a `*-claude-prompt.md`, read it too — it has the chapter outline.

---

## Step 2: Produce the Eke romanisation file (`*-kn-eke.md`)

The Eke file has:
- Same chapter/section structure as the Kannada source
- Section anchors (`<a id="ch1"></a>`, `<a id="sec-1-1"></a>`) matching the Kannada file
- A table of contents (ಒಳಪಿಡಿ in Eke: `oLapiDi`) with links to anchors
- Cross-links at the top to `-kn.md` and `-en.md`
- Key passages transliterated; summaries in Eke for long sections

**Header format:**

```markdown
# {title in Eke}

**lEkhakaru:** Di. en. Sankara baT
**saraNi / Source:** {series if any}
**prakaTaNe / Published:** {year and publisher}

> mUla paThya (kannaDa lipi): [{NN}-{slug}-kn.md](./{NN}-{slug}-kn.md)
> ingliS viSlEShaNe: [{NN}-{slug}-en.md](./{NN}-{slug}-en.md)

---

## oLapiDi

- [adhyAya 1 — {chapter title in Eke}](#ch1)
  - [1.1 {section in Eke}](#sec-1-1)
```

**For each section:**

```markdown
<a id="ch1"></a>

# adhyAya 1 — {title in Eke}
[↑ oLapiDige hintirugi](#oLapiDi)

---

<a id="sec-1-1"></a>

## 1.1 {section title in Eke}

{Eke transliteration of first 3-5 sentences of the section, or a meaningful excerpt}
```

For long chapters, transliterate the opening passage (establishes voice and key terms) plus any key definitions or examples.

---

## Step 3: Produce the English summary file (`*-en.md`)

The English file has:
- A book overview paragraph (3–5 sentences)
- A table of contents with anchor links
- For each chapter/section: heading in English + Kannada title + cross-links + 3–6 bullet points
- A "Key Concepts" table (Kannada term → English meaning)
- A "Cross-references" section pointing to related DNS Bhat books

**Header format:**

```markdown
# {Full English Title}
## {Subtitle or Translation of Kannada Title}

**Author:** D. N. Shankara Bhat (ಡಿ. ಎನ್. ಶಂಕರ ಬಟ್)
**Published:** {year}, {publisher}
**Language:** Kannada
**Source quality:** {Full text / Blog posts (N parts) / Partial transcript}

---

## Book Overview

{3-5 sentence overview of the book's central argument and significance}

---

## Table of Contents

- [Chapter 1 — {English Title} ({Kannada Title})](#ch1)
  - [1.1 {Section English title}](#sec-1-1)
```

**For each section:**

```markdown
## Chapter 1 — {English Title}

*({Kannada title})*

### 1.1 {English section title}

[ಕನ್ನಡ →](./{NN}-{slug}-kn.md#sec-1-1) | [Eke →](./{NN}-{slug}-kn-eke.md#sec-1-1)

- Bullet 1: what this section establishes or argues
- Bullet 2: key evidence or examples used
- Bullet 3: connection to the book's central thesis
- Bullet 4 (if needed): objections considered or counter-arguments
```

**For blog-based books** (like Books 02 and 18), use the blog post title as the "chapter" and link to the blog file:

```markdown
### Part 4 — {English title of blog post}

[Blog (ಕನ್ನಡ) →](./{NN}-{slug}-blog.md#{anchor}) | [Eke →](./{NN}-{slug}-kn-eke.md#{anchor})
```

---

## Eke Romanisation Rules

Eke is DNS Bhat's romanisation system. Use **Eke(ek)** mode (ellara kannaDa — simplified, no aspirates).

### Vowels
| Kannada | Eke | | Kannada | Eke |
|---------|-----|-|---------|-----|
| ಅ | a | | ಆ | A |
| ಇ | i | | ಈ | I |
| ಉ | u | | ಊ | U |
| ಎ | e | | ಏ | E |
| ಒ | o | | ಓ | O |
| ಐ | ay | | ಔ | av |
| ಂ (anusvara) | M (or nasal+following C) | | ಃ visarga | H |

### Consonants — case rule: **uppercase = retroflex or special**
| Kannada | Eke | | Kannada | Eke |
|---------|-----|-|---------|-----|
| ಕ | k | | ಗ | g |
| ಚ | c | | ಜ | j |
| ಟ | **T** | | ಡ | **D** |
| ತ | t | | ದ | d |
| ಪ | p | | ಬ | b |
| ಮ | m | | ನ | n |
| ಣ | **N** | | ಯ | y |
| ರ | r | | ಲ | l |
| ಳ | **L** | | ವ | v |
| ಸ | s | | ಶ | **S** |
| ಹ | h | | ಷ | **S** (same as ಶ in EK) |

### Aspirates (mahapranas) — **drop in Eke(ek)**
ಖ→k, ಘ→g, ಛ→c, ಝ→j, ಠ→T, ಢ→D, ಥ→t, ಧ→d, ಫ→p, ಭ→b

### Anusvara before plosives — write as nasal+plosive
ಂಕ→nka, ಂಗ→nga, ಂಚ→nca, ಂಜ→nja, ಂಟ→nTa, ಂಡ→nDa, ಂತ→nta, ಂದ→nda, ಂಪ→mpa, ಂಬ→mba

### Inherent vowel
Every consonant has inherent `a`. Virama ್ suppresses it in clusters.
ಕ = ka, ಕ್ = k (in cluster), ಕ್ಕ = kka

### Common word examples
| Kannada | Eke |
|---------|-----|
| ಕನ್ನಡ | kannaDa |
| ನುಡಿ | nuDi |
| ಬರಹ | baraha |
| ಹೆಸರು | hesaru |
| ಎಸಕ | esaka |
| ಅರಿಮೆ | arime |
| ಮುನ್ನೋಟ | munnOTa |
| ಇಣುಕುನೋಟ | iNukunOTa |
| ಪದ | pada |
| ಸೊಲ್ಲರಿಮೆ | sollarime |
| ಮಾತು | mAtu |
| ಉಲಿ | uli |
| ಒಳರಚನೆ | oLaracane |
| ಹೊಸ | hosa |
| ಕಟ್ಟುವ | kaTTuva |
| ಮೇಲರಿಮೆ | mElarime |
| ಕೀಳರಿಮೆ | kILarime |

---

## Quality notes

**Source quality matters** — note it clearly in the English file header:
- `*-book.md` from archive.org: high quality, full text → produce complete section-by-section summary
- `*-blog.md` from Wayback Machine: good quality, part-by-part → produce per-post summary
- YouTube transcripts: variable quality, may be garbled → note limitations, summarize available content
- DjVu OCR: often has OCR errors — note this, cross-check with other sources

**For partial content** (missing blog parts, corrupted transcripts):
- Note what's missing in the overview
- Don't invent content — only summarize what's actually in the source files
- Use "⚠️ Parts X–Y not available" as section placeholders

---

## Cross-reference footer (always include in -en.md)

At the end of every English summary, add a cross-reference table:

```markdown
---

## Cross-References to Other DNS Bhat Works

| Related Book | Connection |
|---|---|
| [08 — Kannadakke Mahaprana Yake Beda](../08-kannadakke-mahaprana-yake-beda/) | {how it relates} |
| [14 — Nijakku Halegannada Vyakarana](../14-nijakku-halegannada-vyakarana-entahadu/) | {how it relates} |
```

See `references/book-cross-references.md` for the full thematic index to populate this table.

---

## File naming conventions

| File | Naming |
|------|--------|
| English summary | `{NN}-{slug}-en.md` |
| Eke romanisation | `{NN}-{slug}-kn-eke.md` |
| Kannada structured | `{NN}-{slug}-kn.md` |
| Blog content | `{NN}-{slug}-blog.md` |
| Book full text | `{NN}-{slug}-book.md` |
| AI prompt | `{NN}-{slug}-claude-prompt.md` |

Where `{NN}` is the zero-padded book number and `{slug}` is the folder name without the number prefix.

---

## Reference files

- `references/book-cross-references.md` — Thematic index for cross-linking between DNS Bhat works (read when populating the cross-reference footer)
