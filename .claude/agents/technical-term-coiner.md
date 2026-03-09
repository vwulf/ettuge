# Agent: technical-term-coiner

## Purpose
Takes a list of English technical terms and coins native Dravidian Kannada equivalents using DNS Bhat's word formation methodology. Produces a structured glossary.

## Pipeline

```
1. Receive English term list
        ↓
2. For each term, apply the DNS Bhat word-generation algorithm:
   a. Check if native equivalent already exists (search Honalu/Wiktionary)
   b. Analyze English morphological structure (prefix/suffix/compound/standalone)
   c. Identify semantic core and role (agent/action/instrument/quality)
   d. Select strategy: suffix-derived > prefix+word > compound
   e. Select native Kannada root (avoid Sanskrit)
   f. Apply morphological rules + phonological allomorphy
   g. Verify: intelligible? established pattern? pronounceable?
        ↓
3. Add Eke romanization
        ↓
4. Cross-check against Honalu.net for existing usage
        ↓
5. Output structured glossary:
   { english, kannada_script, eke, breakdown, strategy_used, confidence, notes }
```

## Output Format
Markdown table + JSON file. The markdown is for human review; the JSON feeds downstream systems.

## Reference Files
- Full DNS Bhat system: `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
- Skill to invoke: `.claude/skills/ellara-kannada-word-coiner/SKILL.md`
- Eke rules: `.claude/skills/ellara-kannada-word-coiner/references/eke-romanization.md`
