# Skill: dns-bhat-book-summarizer

_Summarize DNS Bhat books (OCR text): kn.md, en.md, kn-eke.md, claude-prompt_

---

# DNS Bhat Book Summarizer

You produce three kinds of output for DNS Bhat linguistics books in:
`/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/`

1. **`{NN}-{slug}-kn.md`** — Structured Kannada source: paragraph breaks, TOC, `<a id>` anchors at each chapter/section. Created from the raw `-book.md` or `-blog.md` if not already present.
2. **`{NN}-{slug}-en.md`** — Chapter-wise English summary with cross-links to `-kn.md` anchors and Eke romanisation
3. **`{NN}-{slug}-kn-eke.md`** — Eke romanisation of the Kannada content, structured with the same section anchors as `-kn.md`

The `-kn.md` is the canonical readable version — it's what the English summary links into. The raw `-book.md` or `-blog.md` is the OCR archive and is not modified.

---

## Step 1: Identify source material

Before writing anything, read the target book folder:

```
/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/{NN}-{slug}/
```

Check which files exist:
- `README.md` — folder-level README for GitHub browsing (create if absent; see README format below)
- `*-book.md` — full book text (highest quality, use first)
- `*-blog.md` — blog posts (use if no book.md)
- `*-kn.md` — structured Kannada (use for chapter structure)
- `*-djvu.md` — DjVu OCR (fallback, may be noisy)
- `*-en.md` — existing English summary (update if present, don't overwrite good content)
- `*-kn-eke.md` — existing Eke file (update if present)
- `*-claude-prompt.md` — AI prompt (separate from what we produce here)

**README.md format** (create if absent):
```markdown
# [NN] — {Kannada title}
**{English title}**

> {One-sentence description of the book's argument and significance.}

**{✅ Fully processed / ⚠️ Partial / ❌ Not collected}** · {year} · {publisher} · {N} pages

---

## Files in This Folder

| File | Contents |
|------|----------|
| [`{NN}-{slug}-book.md`](./{NN}-{slug}-book.md) | Raw OCR text — ... |
| [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md) | Eke romanisation |
| [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md) | English summaries |
| [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md) | AI context primer |

---

## Where to Start

- **Don't read Kannada?** → [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md)
- **Want the phonetics?** → [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md)
- **AI context primer?** → [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md)
- **Full Kannada text?** → [`{NN}-{slug}-book.md`](./{NN}-{slug}-book.md)

---

[← Back to catalogue](../README.md)
```

Read the primary source file **and** `*-kn.md` if it exists (for chapter structure). For books with a `*-claude-prompt.md`, read it too — it has the chapter outline.

---

## Step 2: Produce the structured Kannada file (`*-kn.md`) — if absent

If no `-kn.md` exists, create one from the raw `-book.md` or `-blog.md`. The `-kn.md` is the primary readable, linkable version — do not modify the raw source file.

**Paragraph detection in `-book.md` OCR output:**
- Paragraphs typically begin with a 4-space indent
- Lines are hard-wrapped at ~65 chars — a paragraph is multiple consecutive lines followed by a blank line or the next indented line
- Chapter headings are usually short standalone lines (often numbered or in all-caps Kannada)
- Section subheadings may have a number prefix (e.g., `೧.`, `೨.`) or be formatted distinctively

**`-kn.md` structure:**
```markdown
# {Kannada title}

**ಲೇಖಕರು:** ಡಿ. ಎನ್. ಶಂಕರ ಬಟ್
**ಪ್ರಕಟಣೆ:** {year}, {publisher}

> ಮೂಲ ಪಠ್ಯ: [`{NN}-{slug}-book.md`](./{NN}-{slug}-book.md)
> ಇಂಗ್ಲಿಶ್ ವಿಶ್ಲೇಷಣೆ: [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md)

---

## ಒಳಪಿಡಿ

- [ಅಧ್ಯಾಯ ೧ — {title}](#ch1)
  - [೧.೧ {section}](#sec-1-1)

---

<a id="ch1"></a>

# ಅಧ್ಯಾಯ ೧ — {title}
[↑ ಒಳಪಿಡಿಗೆ ಹಿಂತಿರುಗಿ](#ಒಳಪಿಡಿ)

---

<a id="sec-1-1"></a>

## ೧.೧ {section title}

{paragraph text with blank lines between paragraphs}
```

See book 08's `-kn.md` as the reference implementation.

---

## Step 2b: Split large volumes into per-chapter page files

**Trigger:** Any volume whose `kn/full.md` exceeds ~6,000 lines (roughly one context window of Kannada text).

This is required for books like Book 07 (*Kannada Barahada Sollarime*) where individual volumes are 10,000–20,000 lines. Without splitting, a session cannot load a chapter into context. The pattern mirrors Book 31's per-letter split.

**Split script:**
```bash
python3 /Users/vishwas/code/ettuge/src/main/python/split_book_chapters.py \
    <path-to-vol-kn/full.md>
```

The script reads `<a id="adhyAya-N">` anchors as chapter boundaries and writes:
- `kn/ch0.md` — chapter index (full frontmatter + TOC + chapter link list)
- `kn/ch1.md`, `kn/ch2.md`, … — one file per chapter, with prev/next navigation links

**Rules:**
- Split only at `adhyAya-N` level. Section (`sec-N-N`) and subsection (`sub-N-N-N`) anchors stay inside their chapter file.
- Each chapter file opens with nav links: `[← ಅಧ್ಯಾಯ N-1](chN-1) | [ಒಳಪಿಡಿ](ch0) | [ಅಧ್ಯಾಯ N+1 →](chN+1)`
- `ch0.md` ends with `[← full.md (complete text)](full)` — the full file remains untouched as the authoritative source
- Volumes already under ~6,000 lines (e.g., Book 07 Vol 3 at 1,071 lines) do **not** need splitting

**GitHub Pages URLs for Book 07 (after push):**

Base: `https://vwulf.github.io/ettuge/kannaDa/dnsbhat/07-kannaDa-barahada-sollarime`

| Vol | Chapter | URL suffix |
|-----|---------|------------|
| Vol 1 | Index | `/book/vol1/kn/ch0` |
| Vol 1 | Ch 1 — ಮುನ್ನೋಟ | `/book/vol1/kn/ch1` |
| Vol 1 | Ch 2 — ಹೆಸರುಪದಗಳು | `/book/vol1/kn/ch2` |
| Vol 1 | Ch 3 — ಉಳಿದ ಪದಗಳು | `/book/vol1/kn/ch3` |
| Vol 1 | Ch 4 — ಪದರೂಪಗಳ ಇಟ್ಟಳ | `/book/vol1/kn/ch4` |
| Vol 2 | Index | `/book/vol2/kn/ch0` |
| Vol 2 | Ch 5 — ಎಸಕಪದಗಳ ಬಳಕೆ | `/book/vol2/kn/ch1` |
| Vol 2 | Ch 6 — ಹೆಸರುಪದಗಳ ಬಳಕೆ | `/book/vol2/kn/ch2` |
| Vol 3 | Full (no split needed) | `/book/vol3/kn/full` |
| Vol 4 | Full (no split needed) | `/book/vol4/kn/full` |

**When working with Book 07 in a session:**
1. Fetch `ch0` of the relevant volume to see the chapter map
2. Fetch only the specific chapter needed (`ch1`, `ch2`, etc.)
3. Never attempt to load `full.md` directly — it will overflow context

---

## Step 3: Produce the Eke romanisation file (`*-kn-eke.md`)

The Eke file has:
- Same chapter/section structure as the Kannada source
- Section anchors (`<a id="ch1"></a>`, `<a id="sec-1-1"></a>`) matching the Kannada file
- A table of contents (ಒಳಪಿಡಿ in Eke: `oLapiDi`) with links to anchors
- Cross-links at the top to `-kn.md` and `-en.md`
- Key passages transliterated; summaries in Eke for long sections

**Header format:**

```markdown
# {title in Eke}

**lEkhakaru:** Di. en. Sankara bhaT
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

Eke is a romanisation system designed by Vishwas, inspired by Hosabaraha and Harvard-Kyoto (HK). Use **Eke(ek)** mode (ellara kannaDa — simplified, no aspirates).

### Vowels
| Kannada | Eke | | Kannada | Eke |
|---------|-----|-|---------|-----|
| ಅ | a | | ಆ | A |
| ಇ | i | | ಈ | I |
| ಉ | u | | ಊ | U |
| ಎ | e | | ಏ | E |
| ಒ | o | | ಓ | O |
| ಐ | ay | | ಔ | av |
| ಋ / ೃ (vocalic r, short) | **x** | | ೠ / ೄ (vocalic r, long) | **X** |
| ಂ (anusvara) | nasal+C *(always assimilated — never M; see Anusvara section below)* | | ಃ visarga | H |

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
| ರ | r *(always lowercase — **R is exclusively ಱ, never ರ**)* | | ಲ | l |
| ಳ | **L** | | ವ | v |
| ಱ | **R** *(archaic retroflex ṟ — extremely rare in modern Kannada)* | | | |
| ಸ | s | | ಶ | **S** |
| ಹ | h | | ಷ | **S** (same as ಶ in EK) |

### Aspirates (mahapranas) — **preserved in Eke(ek)**
ಖ→kh, ಘ→gh, ಛ→ch, ಝ→jh, ಠ→Th, ಢ→Dh, ಥ→th, ಧ→dh, ಫ→ph, ಭ→bh

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
| Folder README | `README.md` |
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
