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
- `dnsbhat/` — DNS Bhat word formation articles, prompts, and 13 book directories
- `transcripts/` — Raw YouTube transcripts (349+ files, may have ASR artifacts)
- `transcripts_cleaned/` — AI-processed transcripts (130+ files)
- `sections/` — Extracted transcript sections

## Rules for This Directory
1. All new Kannada vocabulary must follow DNS Bhat's native (Dravidian-root) methodology. Reference: `dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
2. Avoid Sanskrit-derived terms when a native Kannada equivalent exists.
3. Eke romanization rules: aspirates removed (kh→k, gh→g, ch→c, jh→j, th→t, dh→d, ph→p, bh→b), retroflexes preserved (T, D, N, L), velar nasals (G, Y).
4. Always prefer `transcripts_cleaned/` over `transcripts/` for analysis.
5. Files may have Kannada-script names — handle Unicode carefully.

## Unicode
Kannada script range: U+0C80–U+0CFF. Filenames and content may contain Kannada Unicode characters.