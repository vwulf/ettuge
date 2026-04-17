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
| `ettuge-content-qa` | Answer questions from: **Books** (89+ influential books — summaries + personal takeaways), **FP notes** (Haskell/ZIO/Kyo), and **Reflection** (20 topic files: AI/ML, Kannada, martial arts, health, history, cricket, travel, and more — distilled from Signal bookmarks) | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/07-content-qa.md) |
| `vetted-kannaDa-dictionary` | Look up Bhat's settled native Kannada equivalents (Books 15 + 31) before coining; precedence VETTED-15 > VETTED-31 > COINED | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/08-vetted-dictionary.md) |
| `kannada-script-reform` | Why mahaprana letters are unnecessary in Kannada, the social justice argument, comparative reforms, Bhat's *hosa baraha* (Books 08, 28, 29, 30) | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/09-kannada-script-reform.md) |
| `old-kannada-grammar` | How ancient grammarians wrongly applied Sanskrit to Old Kannada; actual Dravidian grammatical principles; rational/non-rational gender; Nagavarma, Kesiraja (Book 14) | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/10-old-kannada-grammar.md) |
| `havyaka-kannada` | Havyaka dialect: preserved vowels, four-tense verbs, social honorifics (not sex-based), inclusive-exclusive pronouns (Books 20, 09) | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/11-havyaka-kannada.md) |
| `kannada-sound-change` | Sound change theory applied to Kannada: mahaprana merger, vowel-raising, comparative reconstruction. Book 22 not yet extracted — Books 08 + 26 available | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/12-kannada-sound-change.md) |
| `kannada-syntax` | Kannada sentence structure: SOV order, converb co-reference constraint, pre-nominal relative clauses, verbal noun chains (Books 25, 07) | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/13-kannada-syntax.md) |
| `kannada-reference-grammar` | **Book 07** — Bhat's 4-volume comprehensive grammar of written Kannada: 36-verb-form paradigm, pAngu semantic roles, compound verbs, converbs, hosa baraha. The deepest single reference in the corpus | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/16-kannada-reference-grammar.md) |

---

## Agents and Repository Context

Agents, CLAUDE.md files, and repository conventions:
[`https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/06-agents-and-context.md`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/06-agents-and-context.md)

---

## Deployment and Sync Skills

| Skill | Purpose | File |
|-------|---------|------|
| `ettuge-pre-deploy-check` | Sanity check before every `git push` — catches config errors, broken sidebar links, missing anchors | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/14-ettuge-pre-deploy-check.md) |
| `ettuge-sync` | Sync all Claude context files after a work session — CLAUDE.md files, book primers, skill docs, commit + push | [`fetch`](https://raw.githubusercontent.com/vwulf/ettuge/master/docs/skills/15-ettuge-sync.md) |

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
| "what books", "recommend a book on", "your notes on", "what did you save about", "FP notes", "Haskell question", "what's in your knowledge base about", "influential books", "what have you read about", "self-reflection", "your thoughts on", "books you've read", "what do your notes say about", "what have you saved about", "tell me about [book]", "martial arts notes", "AI notes", "Kannada notes", "health notes", "cricket notes" | `07-content-qa.md` |
| "what did Bhat use for X", "look up X in the dictionary", "vetted word for", "is there a settled Kannada word for" | `08-vetted-dictionary.md` |
| "mahaprana", "script reform", "hosa baraha", "ಮಹಾಪ್ರಾಣ", "why doesn't Kannada need aspirated letters" | `09-kannada-script-reform.md` |
| "old Kannada grammar", "Kesiraja", "Nagavarma", "ಹಳೆಗನ್ನಡ ವ್ಯಾಕರಣ", "rational non-rational gender", "Sanskrit imposed on Kannada" | `10-old-kannada-grammar.md` |
| "Havyaka", "ಹವ್ಯಕ ಕನ್ನಡ", "coastal Kannada dialect", "four-tense verb", "Havyaka honorifics", "vowel raising Kannada" | `11-havyaka-kannada.md` |
| "sound change", "ಉಲಿ ಮಾರ್ಪಾಡು", "assimilation", "vowel raising", "Neogrammarian", "comparative reconstruction Dravidian" | `12-kannada-sound-change.md` |
| "Kannada sentence structure", "SOV", "word order", "relative clause Kannada", "converb", "clause combining", "ಕನ್ನಡ ವಾಕ್ಯ" | `13-kannada-syntax.md` |
| "Book 07", "sollarime", "ಸೊಲ್ಲರಿಮೆ", "36 verb forms", "pAngu", "compound verb Kannada", "modalEsaka", "complete Kannada grammar" | `16-kannada-reference-grammar.md` |
