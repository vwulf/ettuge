# Agent: ellara-vocab-builder

## Purpose
Builds a native Kannada vocabulary dataset by scraping Honalu.net and Kannada Wiktionary, classifying word etymology (Dravidian vs Sanskrit), and storing results in Eke romanization.

## Pipeline

```
1. Scrape word list from Honalu.net
        ↓
2. Classify etymology (native Dravidian vs Sanskrit borrowing)
   Heuristics:
   - Sanskrit signals: aspirated consonants (kh/gh/th/dh/ph/bh), Sanskrit clusters (pr-/tr-/kr-), ಷ (Sha)
   - Dravidian signals: no aspirates, has ಳ/ಣ/ಡ/ಟ, Tamil cognate matches
        ↓
3. Transliterate to Eke romanization
   Rules: aspirates→plain, retroflexes uppercase (T/D/N/L), long vowels uppercase (A/I/U/E/O)
        ↓
4. Store as structured dataset (JSON or CSV)
   Schema: { word_kn, word_eke, etymology_class, source_url, confidence }
```

## Key Constraints
- Honalu.net may rate-limit — use delays between requests
- Prefer Wiktionary for etymology confirmation
- Flag uncertain classifications for human review
- Output must be compatible with `ellara-kannada-word-coiner` skill format

## Reference Files
- DNS Bhat word formation: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Eke rules: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`
- Analysis: `src/main/md/kannada/dnsbhat/dns-bhat-analysis.md`
