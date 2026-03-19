# Kannada Directory — CLAUDE.md

This directory contains the PRIMARY linguistic work for the ettuge project.

## Key Files
- `Eke.md` — Full Eke romanization specification (153KB) — do NOT edit casually
- `Eke.kn.md` — Complete Kannada translation of Eke.md (DNS Bhat compliant, complete)
- `Eke.eke.md` — Eke romanization of Eke.kn.md (complete)
- `brahmi-nabatian-phoenician-hieroglyphs-lineage.md` — Script history documentation
- `kannada-mnemonics-hieroglyph-hook.md` — Kannada mnemonic table
- `malatibhat_dns_bhat_chat.md` / `malatibhat_dns_bhat_videos.md` — Video references and analysis
- `malatibhat_dns_bhat_videos_links.txt` — Raw video link list

## Subdirectories

### `dnsbhat/` — DNS Bhat Book Collection (29 books, numbered 01–29)
Each book directory follows this file structure:
- `*-book.md` / `*-blog.md` — Raw OCR archive (do NOT edit)
- `*-kn.md` — Structured Kannada source: paragraph breaks, ಪರಿವಿಡಿ TOC, `<a id="adhyAya-N">` anchors
- `*-kn-eke.md` — Eke romanisation (regenerate after kn.md changes)
- `*-en.md` — Chapter-wise English summary with kn.md cross-links
- `*-claude-prompt.md` — Condensed prompt for Claude sessions
- `README.md` — Book index

**Citation quotes:** Standardised to curly single quotes `'word'` (U+2018/U+2019) in kn.md and kn-eke.md. Never use backtick as open-quote.
**Unrounded-u:** `u^` in kn-eke.md = ಉ್ (Havyaka phoneme) — do not alter.
**Nudi OCR:** Books 14–29 were Nudi-encoded; OCR produces garbled Latin. See `.claude/CLAUDE.md` for fix pipeline.
**Project history:** `docs/dnsbhat/PROJECT-RECAP.md`

### `transcripts/` — Raw YouTube transcripts (349+ files, may have ASR artifacts)
### `transcripts_cleaned/` — AI-processed transcripts (130+ files)
### `sections/` — Extracted transcript sections

## Rules for This Directory
1. All new Kannada vocabulary must follow DNS Bhat's native (Dravidian-root) methodology. Reference: `dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
2. Avoid Sanskrit-derived terms when a native Kannada equivalent exists.
3. Eke romanization rules — TWO modes:
   - **Romanising existing Kannada text:** aspirates PRESERVED (ಭ→bh, ಧ→dh, ಖ→kh etc.); retroflexes UPPERCASE (T, D, N, L, S); long vowels UPPERCASE (A, I, U, E, O); vocalic ṛ → x; anusvara ಂ → assimilated nasal (never standalone M); N = exclusively ಣ; r = ರ always, R = rare archaic ಱ.
   - **New native word coining (Ellara):** avoid aspirated consonants — prefer k, g, c, j, T, D, t, d, p, b. All other rules same.
   - Full canonical error table: `.claude/CLAUDE.md` → "Eke Canonical Rules".
4. Always prefer `transcripts_cleaned/` over `transcripts/` for analysis.
5. Files may have Kannada-script names — handle Unicode carefully.

## Unicode
Kannada script range: U+0C80–U+0CFF. Filenames and content may contain Kannada Unicode characters.