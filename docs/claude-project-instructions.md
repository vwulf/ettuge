# Ettuge Kannada Linguistics — Claude Project Instructions

This Project is for working with DNS Bhat Kannada linguistics books in the
[ettuge](https://github.com/vwulf/ettuge) repository: coining native Kannada
words, Eke romanisation, morphology, OCR cleanup, and book summarization.

**How to use:** Each skill is a separate file. When you need a skill, fetch
its URL below. The agents-and-context file has repository structure and all
CLAUDE.md files. Book primers have per-book reference data.

---

## Skills

| Skill | Purpose | File |
|-------|---------|------|
| `ellara-kannada-word-coiner` | Coin native Dravidian Kannada words using DNS Bhat's Ellara methodology | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/01-word-coiner.md) |
| `kannada-morphology` | Generate Kannada morphological forms: case, conjugation, suffixes | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/02-morphology.md) |
| `dns-bhat-book-summarizer` | Summarize DNS Bhat books (OCR text): kn.md, en.md, kn-eke.md, claude-prompt | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/03-book-summarizer.md) |
| `dns-bhat-transcript-summarizer` | Summarize DNS Bhat YouTube lecture series (books 01–13, transcript-only) | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/04-transcript-summarizer.md) |
| `kannada-ocr-cleaner` | Audit and fix OCR artefacts from Nudi/Baraha/ISM legacy font scans | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/05-ocr-cleaner.md) |
| `ettuge-content-qa` | Answer questions from Books (89+ titles), FP notes (Haskell/ZIO/Kyo), and Reflection (20 topic files from Signal bookmarks) | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/07-content-qa.md) |
| `vetted-kannaDa-dictionary` | Look up Bhat's settled native Kannada equivalents (Books 15 + 31) before coining; precedence VETTED-15 > VETTED-31 > COINED | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/08-vetted-dictionary.md) |

---

## Agents and Repository Context

Agents, CLAUDE.md files, and repository conventions:
[`https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/06-agents-and-context.md`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/06-agents-and-context.md)

---

## Book Primers (per-book reference data)

| File | Books | URL |
|------|-------|-----|
| `claude-book-primers-1.md` | 01–25 | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/claude-book-primers-1.md) |
| `claude-book-primers-2.md` | 27–33 | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/claude-book-primers-2.md) |

---

## Quick Trigger Guide

| User says… | Fetch skill file |
|-----------|-----------------|
| "native Kannada word for X", "Ellara version of", "no Sanskrit", "coin a word" | `01-word-coiner.md` |
| "conjugate", "case form", "dative of", "suffix for", "morphological form" | `02-morphology.md` |
| "summarize book NN", "create English summary", "generate Eke", "create claude-prompt" | `03-book-summarizer.md` |
| "summarize transcript book NN", "YouTube lectures", books 01–13 | `04-transcript-summarizer.md` |
| "OCR errors", "garbled Kannada", "arka-ottu", "Nudi artefact", "fix legacy font" | `05-ocr-cleaner.md` |
| "what books", "recommend a book on", "your notes on", "what did you save about", "FP notes", "Haskell question", "what's in your knowledge base about" | `07-content-qa.md` |
| "what did Bhat use for X", "look up X in the dictionary", "vetted word for", "is there a settled Kannada word for" | `08-vetted-dictionary.md` |
