---
name: dns-bhat-transcript-summarizer
description: >
  Generates thematic English summaries with part-level source pointers and Eke
  romanisation files for DNS Bhat YouTube lecture series in the ettuge repository.
  Use this skill when the user asks to summarize a YouTube-only DNS Bhat book
  (books 01–13 in the dnsbhat folder), create an English summary from transcripts,
  produce Eke romanisation of transcript content, or generate -en.md / -kn-eke.md
  for a book that has no -book.md. Triggers on phrases like "summarize book NN
  from transcripts", "create English summary for lecture series", "generate Eke
  for transcripts", or any reference to the transcript-based books (01–13).
  Distinct from dns-bhat-book-summarizer which handles books with OCR text.
---

# DNS Bhat Transcript Summarizer

You produce two kinds of output for DNS Bhat YouTube lecture series in:
`/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/`

1. **`{NN}-{slug}-en.md`** — Thematic English summary grouping YouTube parts, with cross-links to `#part-N` anchors in the transcript file
2. **`{NN}-{slug}-kn-eke.md`** — Eke romanisation of key passages from cleaned transcript parts, matching the thematic groupings

The primary source is the **consolidated transcript `.md` file** (e.g., `09-havyaka-kannada.md`) — NOT a `-book.md`. This file was processed by `format-transcripts.py` and already has `<a id="part-N"></a>` anchors before each `## Part N` heading.

There is **no `-kn.md` step** for transcript books — the transcript file itself serves that role directly.

---

## Step 1: Identify source material and assess quality

Read the target book folder:

```
/Users/vishwas/code/ettuge/src/main/md/kannada/dnsbhat/{NN}-{slug}/
```

The primary source file is `{NN}-{slug}.md` (same name as the folder, no suffix). Check what exists:

- `{NN}-{slug}.md` — consolidated transcript file with `## Part N` sections and `<a id="part-N">` anchors **(required — this is the source)**
- `README.md` — folder-level README (create if absent; see format below)
- `*-website.md` — Wayback Machine snapshot of dnshankarabhat.net for this book. **Always read this.** Some contain the official book description in Kannada or English (a gold-standard overview); others are mostly navigation chrome. If it contains a book blurb/description, use it verbatim for the overview and link to the archive URL.
- `*-blog.md` — DNS Bhat's blog posts (e.g., Book 02). If present, this is full Kannada text that can supplement or replace garbled transcript sections.
- `*-en.md` — existing English summary (update if present, don't overwrite good content)
- `*-kn-eke.md` — existing Eke file (update if present)
- `*-claude-prompt.md` — AI context primer (read if present for background)

**Assessing `-website.md` content quality:**
- If it contains a `### Description` or `### ವಿವರಗಳು` section with multiple sentences about the book → **substantive** — use the description in the overview
- If it's mostly navigation links (`ಬ್ಲಾಗ್`, `ಕನ್ನಡ ಹೊತ್ತಗೆಗಳು`, contact links) with no prose → **nav-only** — note the archive URL but skip the content
- Always include the archive URL as a "Further reading" link at the bottom of `-en.md`

**README.md format** (create if absent):

```markdown
# [NN] — {Kannada title}
**{English title}**

> {One-sentence description of the lecture series' argument and significance.}

**{✅ Fully processed / ⚠️ Partial / ❌ Not processed}** · {N} parts · YouTube lecture series

---

## Files in This Folder

| File | Contents |
|------|----------|
| [`{NN}-{slug}.md`](./{NN}-{slug}.md) | Consolidated YouTube transcripts — {N} parts |
| [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md) | Eke romanisation of key passages |
| [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md) | English summaries by theme |
| [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md) | AI context primer |

---

## Where to Start

- **Don't read Kannada?** → [`{NN}-{slug}-en.md`](./{NN}-{slug}-en.md)
- **Want the phonetics?** → [`{NN}-{slug}-kn-eke.md`](./{NN}-{slug}-kn-eke.md)
- **AI context primer?** → [`{NN}-{slug}-claude-prompt.md`](./{NN}-{slug}-claude-prompt.md)
- **Full transcripts?** → [`{NN}-{slug}.md`](./{NN}-{slug}.md)

---

[← Back to catalogue](../README.md)
```

---

## Step 2: Read and assess transcript quality

Read the consolidated transcript file. For each `## Part N` section, assess:

**Quality tiers:**
- **Good (🟢)** — Cleaned Kannada paragraphs from `transcripts_cleaned/`. Readable linguistic content. Summarise in detail.
- **Garbled (🟡)** — Uncleaned single-line block. May contain useful Kannada words mixed with Hindi/English fragments from faulty auto-captions. Note what's discernible, skip what isn't.
- **Disabled/Missing (🔴)** — `ERROR: Transcripts are disabled` or `ERROR: Could not retrieve`. Skip entirely; note the gap.
- **Prelim (🔵)** — Parts labelled P1–P6 in some books (e.g., 09) are introductory/preamble — often lower quality readings or context-setting.

**Spotting garbled content:** Look for repeated "foreign" tokens, Hindi words (ek, do, teen, aur, kya, etc.), or fragmented Kannada without grammatical structure. If > 50% of a part is noise, mark as 🟡 partial.

**Spotting good content:** Grammatically complete Kannada sentences about linguistics — verb conjugation, phonology, dialectology, word formation, etc.

---

## Step 3: Group parts into themes

Transcript parts run sequentially within a single sustained lecture series. Identify **thematic blocks** — adjacent parts covering the same topic. The `-en.md` is organised around these themes, not individual parts.

**How to identify themes:**
- Look at the opening sentences of each good part for the topic shift
- Each "chapter" in the English summary = 3–8 consecutive parts on the same theme
- Use the book's `-claude-prompt.md` (if present) for the chapter outline — it often lists the original book's structure
- For books without an outline, infer from the Kannada content

**Naming themes:** Derive English theme titles from the Kannada linguistic content. DNS Bhat's lectures typically follow his book structure.

---

## Step 4: Produce the English summary file (`*-en.md`)

**Header format:**

```markdown
# {Full English Title}
## {Subtitle or Translation of Kannada Title}

**Author:** D. N. Shankara Bhat (ಡಿ. ಎನ್. ಶಂಕರ ಬಟ್)
**Format:** YouTube lecture series — {N} parts
**Read by:** {reader, if known — e.g., Malati Bhat}
**Language:** Kannada
**Source quality:** {e.g., "72/88 parts cleaned (82%)" or "Partial — 22/43 cleaned"}
**Transcript file:** [`{NN}-{slug}.md`](./{NN}-{slug}.md)

---

## Overview

{3–5 sentences: what this lecture series covers, DNS Bhat's central argument, why it matters.}

---

## Table of Contents

- [Theme 1 — {English title}](#theme-1)
- [Theme 2 — {English title}](#theme-2)
```

**For each thematic group:**

```markdown
<a id="theme-1"></a>

## Theme 1 — {English Title}

*Parts {N}–{M} of the transcript*

[📼 Parts {N}–{M} →](./{NN}-{slug}.md#part-{N})

- Bullet: what this section establishes or argues
- Bullet: key evidence or examples given (cite Kannada terms in Eke)
- Bullet: connection to the overall thesis
- Bullet (if needed): counter-arguments considered

> **Coverage note:** Parts {X}, {Y} unavailable (transcripts disabled). Parts {Z}–{W} garbled (auto-caption noise).
```

**For individual standalone parts** (if a single part is a complete unit):

```markdown
### Part {N} — {English title of this part's content}

[📼 Part {N} →](./{NN}-{slug}.md#part-{N})

- {Summary bullet}
```

**Source quality field options:**
- `Full text (book OCR)` — NOT used here (that's the other skill)
- `YouTube transcripts — {N}/{total} parts cleaned ({pct}%)`
- `YouTube transcripts — partial ({N} parts unavailable)`

---

## Step 5: Produce the Eke romanisation file (`*-kn-eke.md`)

Romanise **key passages** from the **good (🟢) parts only**. For garbled/disabled parts, note the gap.

**Header format:**

```markdown
# {title in Eke}

**lEkhakaru:** Di. en. Sankara baT
**mULa:** YouTube udangaLu — {N} bagagaLu
**odidaravaru:** {reader in Eke, if known}

> mUla paThya (kannaDa lipi): [{NN}-{slug}.md](./{NN}-{slug}.md)
> ingliS viSlEShaNe: [{NN}-{slug}-en.md](./{NN}-{slug}-en.md)

---

## oLapiDi

- [viShaya 1 — {theme 1 in Eke}](#theme-1)
- [viShaya 2 — {theme 2 in Eke}](#theme-2)
```

**For each thematic group:**

```markdown
<a id="theme-1"></a>

## viShaya 1 — {title in Eke}

*bagagaLu {N}–{M}*

[📼 bagagaLu {N}–{M} →](./{NN}-{slug}.md#part-{N})

{Eke transliteration of 3–5 key sentences from the best part in this group.
Pick sentences that capture the core idea — a definition, a key example, or a thesis statement.}

> *(bagagaLu {X}, {Y} dorakalavillDa / kannaDavagalilla)*
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
| ಮಾತು | mAtu |
| ಉಲಿ | uli |
| ಭಾಷೆ | bASe |
| ವ್ಯಾಕರಣ | vyAkaraNa |
| ಪದ | pada |
| ಅರ್ಥ | arta |
| ಸ್ವರ | svara |
| ವ್ಯಂಜನ | vyanjana |
| ಕ್ರಿಯಾಪದ | kriyApada |
| ನಾಮಪದ | nAmapada |
| ಉಚ್ಚಾರಣೆ | uccAraNe |
| ಅಕ್ಷರ | akSara |
| ಸೊಲ್ಲರಿಮೆ | sollarime |
| ಒಳರಚನೆ | oLaracane |
| ಹವ್ಯಕ | havyaka |
| ಉಪಭಾಷೆ | upabASe |
| ಮಾತಿನ | mAtina |

---

## Quality notes

**Be honest about coverage.** Always state the cleaned-part count in the header.

- **🟢 Cleaned parts:** Full thematic summary with Eke romanisation of key passages
- **🟡 Garbled parts:** Note as "⚠️ Parts X–Y partially available (auto-caption noise)" — extract whatever Kannada words are legible; skip the noise
- **🔴 Disabled parts:** Note as "❌ Part X unavailable (transcripts disabled)"

**Don't invent content.** If a section's transcripts are missing or garbled, say so explicitly. Use the structure from the book's `-claude-prompt.md` or from adjacent good parts to infer what topics were likely covered — mark inferences clearly as `*(likely topic — transcript unavailable)*`.

**Prelim parts (P1–P6):** Some books (e.g., 09) have prefix parts read by Malati Bhat or others. Treat these as an introduction section. They often introduce DNS Bhat and give context.

---

## Cross-reference and external links footer (always include in -en.md)

```markdown
---

## Cross-References to Other DNS Bhat Works

| Related Book | Connection |
|---|---|
| [08 — Kannadakke Mahaprana Yake Beda](../08-kannadakke-mahaprana-yake-beda/) | {how it relates} |
| [05 — Mathina Olaguttu](../05-mathina-olaguttu/) | {how it relates} |

---

## External Links

- **Author's website (archived):** {archive URL from *-website.md}
- **YouTube playlist:** {link from transcript file's Table of Contents, if available}
```

See `references/book-cross-references.md` for the full thematic index.

---

## File naming conventions

| File | Naming |
|------|--------|
| Folder README | `README.md` |
| Transcript source | `{NN}-{slug}.md` |
| English summary | `{NN}-{slug}-en.md` |
| Eke romanisation | `{NN}-{slug}-kn-eke.md` |
| AI prompt | `{NN}-{slug}-claude-prompt.md` |

Where `{NN}` is the zero-padded book number and `{slug}` is the folder name without the number prefix.

---

## Reference files

- `references/book-cross-references.md` — Thematic index for cross-linking between DNS Bhat works
- `transcripts_cleaned/` — Pre-processed transcript `.txt` files (source for cleaned parts)
- `format-transcripts.py` — Script that substituted cleaned transcripts into the `.md` files
