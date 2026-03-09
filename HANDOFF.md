# Session Handoff — claude.ai → Claude Code
_Generated: 2026-03-08_

## What We Were Doing
Analyzing all sessions between Vishwas and Claude to:
1. Map recurring work patterns
2. Decide what to turn into Skills vs MCP plugins vs Agents vs CLAUDE.md
3. Benchmark against the Anthropic Complete Guide to Building Skills (fetched in full)
4. Read and analyze ettuge repo CLAUDE.md files (blocked by GitHub rate limits — do this first in Claude Code)

---

## Your Stack (always-on context)

- **Machine**: macOS Apple Silicon, Nix package manager
- **No npm global installs** — use `npx` or Nix shells
- **Languages**: Scala 3 (primary), Haskell, Python, Nushell
- **Build**: Mill (not SBT)
- **AI integration**: Kyo AI library (model-agnostic, type-safe Scala wrappers)
- **Claude Code install**: `npx @anthropic-ai/claude-code` (due to Nix read-only store)

---

## Your Projects

| Project | Description | Repo/Location |
|---|---|---|
| **ettuge** | Personal knowledge garden — Kannada linguistics, FP, Carnatic music, visual art | `~/code/ettuge`, `github.com/vwulf/ettuge` |
| **Ellara Kannada app** | Language learning app with 3 personalities (Formal / Bangalore Urban / Ellara) | Scala 3 + Kyo AI + Honalu scraper |
| **quic** | [Read from repo — unclear from sessions] | `~/code/` |

---

## Domains You Use Claude For (from session analysis)

### 1. Ellara Kannada / Linguistics (most frequent, deepest)
- Morphological generation from Dr. D.N. Shankara Bhat's grammar framework
- Noun case suffixes with phonological conditioning (dative -ge/-ige/-ge variations)
- Verb conjugation across tense/mood/person-number-gender
- Verbal noun chains: `māḍu → māḍuvudu → māḍuvudakke` (4-step derivation)
- Etymology classification: native Dravidian vs Sanskrit borrowings
  - Heuristics: aspirated consonants, repeated clusters, retroflex patterns
- Word coining for technical/modern concepts using native compounds
  - Examples: ನೀರೊಳದೋಣಿ (submarine), ಸಮರೂಪ (isomorphic)
- Eke romanization system (defined in `src/main/md/kannada/Eke.md`)
- Three language personalities:
  - **Formal**: literary/classical
  - **Bangalore Urban**: contemporary slang + English code-mixing
  - **Ellara**: pure Dravidian, no Sanskrit borrowings
- Vocabulary sourcing: Honalu.net + Kannada Wiktionary scraping

### 2. AI Model Architecture & Evaluation
- Comparing models for Indic tasks: Sarvam-M (24B, Indic specialist) vs Haiku 4.5 vs Kimi K2.5 (1T MoE)
- Groq LPU for fast inference (Sarvam-M not available there yet)
- MCP protocol architecture
- Agent frameworks: OpenClaw / NanoClaw / ClawdBot
- Local deployment tradeoffs (Mac mini, quantization, tokens/sec)

### 3. Scala / Build Tooling
- Scala 3 project architecture
- Mill vs SBT evaluation
- Kyo AI type-safe wrappers for model-agnostic LLM integration

### 4. Carnatic Music / Audio
- Euterpea (Haskell) music DSL — encoded Rangapura Vihara (Brindavana Saranga raga)
- MIDI → Web Audio API browser player
- Carnatic solfège display (S R G M P D N), raga arohanam/avarohanam

### 5. Dev Environment
- Nix on macOS Apple Silicon
- Claude Code installation + Nix compatibility issues
- npm global prefix workarounds

---

## Skills to Build (priority order)

### 🥇 `ellara-kannada-word-coiner`
**Trigger phrases**: "translate to Kannada", "native Kannada word for", "Dravidian equivalent of", "Ellara version of"

```yaml
---
name: ellara-kannada-word-coiner
description: Coins native Dravidian Kannada words for technical/modern concepts
  following Dr. D.N. Shankara Bhat's Ellara principles. Use when asked for Kannada
  translation of English terms, native alternatives to Sanskrit-derived words, or
  pure Dravidian compound formation. Avoids Sanskrit borrowings, aspirated consonants,
  uses Eke romanization.
---
```

**References to bundle**:
- `src/main/md/kannada/Eke.md` — romanization rules
- Bhat's principles (extract from `CLAUDE.md` and book analysis sessions)
- Example words already coined (ನೀರೊಳದೋಣಿ, ಸಮರೂಪ, ಒಳನಾಡಿಗೆ, etc.)

---

### 🥈 `kannada-morphology`
**Trigger phrases**: "Kannada suffix for", "conjugate this verb", "case form of", "morphological form"

```yaml
---
name: kannada-morphology
description: Generates Kannada morphological forms from root words using Bhat's
  grammatical framework. Use for noun case suffixes, verb conjugations, verbal noun
  chains, phonological conditioning rules. Covers human/non-human semantic splits,
  vowel/consonant stem conditioning, dative/accusative/locative forms.
---
```

**Key rules to encode**:
- Dative suffix: `-ge` (consonant-final, non-human), `-ige` (some consonant-final), `-ge` (vowel-final human)
- Verbal noun chain: verb root → `-vu` → `-du` → case suffix
- Human vs non-human noun conditioning

---

### 🥉 `carnatic-web-audio`
**Trigger phrases**: "play this Haskell music", "Euterpea to audio", "Carnatic browser player"

```yaml
---
name: carnatic-web-audio
description: Converts Carnatic music encoded in Haskell Euterpea library to
  browser-playable Web Audio API player. Use when given .hs files with Euterpea
  note sequences, raga definitions (arohanam/avarohanam), or asked to create
  audio player for Indian classical music. Handles MIDI pitch mapping, multi-harmonic
  synthesis, Carnatic solfege notation display.
---
```

---

## MCP Servers to Build

| Server | Purpose | Status |
|---|---|---|
| **honalu-scraper** | Live Honalu.net + Wiktionary vocab fetch + Dravidian classification | Designed in sessions, not built |
| **ettuge-reader** | Read local ettuge repo files (bypasses GitHub fetch restrictions) | Needed now |
| **kyo-model-router** | Route requests to Sarvam-M/Haiku/Kimi based on task type | Kyo AI exists, no MCP wrapper yet |

---

## Agents to Build

| Agent | Pipeline |
|---|---|
| **ellara-vocab-builder** | scrape Honalu → classify etymology → transliterate to Eke → store dataset |
| **technical-term-coiner** | English term list → Bhat rules → Dravidian compounds → Eke romanization → cross-check Honalu |
| **model-benchmark-runner** | Ellara test cases → run on Sarvam/Haiku/Kimi → comparison table |

---

## CLAUDE.md to Write (for ettuge repo root)

```markdown
# Vishwas's ettuge — Claude Context

## Language Philosophy
- All Kannada work follows Dr. D.N. Shankara Bhat's Ellara Kannada principles
- Prefer native Dravidian constructions over Sanskrit borrowings
- Drop aspirated consonants (mahapranas) — they don't exist in natural Kannada speech
- Use Eke romanization for all transliteration (see src/main/md/kannada/Eke.md)
- Three language personalities: Formal / Bangalore Urban / Ellara

## Tech Stack
- macOS Apple Silicon, Nix package manager (read-only /nix/store)
- Scala 3 + Mill (not SBT)
- Kyo AI for model-agnostic LLM integration
- No npm global installs — use npx or nix-shell
- Haskell for music/FP explorations (Euterpea, GHC)

## Model Preferences
- Kannada linguistic tasks → Sarvam-M or Claude Haiku
- General reasoning → Claude Sonnet/Opus
- Speed-sensitive → Groq-hosted models

## Repo Structure
- src/main/md/ — all readable documents
- src/main/md/kannada/ — Eke, morphology, Ellara principles
- src/main/md/haskell/ — FP explorations, Carnatic music (hsom.md)
- src/main/md/pl/ — lambda calculus, FP theory
- src/main/md/Books/ — reading catalog with DNS Bhat works
```

---

## Immediate Next Steps in Claude Code

1. **Read all CLAUDE.md files** in this repo:
   ```bash
   find . -name "CLAUDE.md" | xargs cat
   ```

2. **Run skill-creator** to generate the first skill:
   > "Use skill-creator to build a skill called ellara-kannada-word-coiner based on this HANDOFF.md"

3. **Check what's in `src/main/md/kannada/`** — this is the ground truth for skill content:
   ```bash
   ls src/main/md/kannada/
   cat src/main/md/kannada/Eke.md
   ```

4. **Read the DNS Bhat book analysis** from the repo to extract principles for the skills

5. **Create `.claude/` directory structure** for ettuge:
   ```
   .claude/
   ├── agents/
   │   ├── ellara-vocab-builder.md
   │   └── technical-term-coiner.md
   ├── skills/
   │   ├── ellara-kannada-word-coiner/
   │   │   └── SKILL.md
   │   ├── kannada-morphology/
   │   │   └── SKILL.md
   │   └── carnatic-web-audio/
   │       └── SKILL.md
   └── commands/
       └── coin-word.md
   ```

---

## Reference: Anthropic Skills Guide Key Points

- Skill = folder with `SKILL.md` (required) + `scripts/` + `references/` + `assets/`
- YAML frontmatter is loaded first (token-efficient) — description must include WHAT + WHEN + trigger phrases
- Description max 1024 chars, no XML tags, kebab-case name
- Three categories: (1) Document/Asset Creation, (2) Workflow Automation, (3) MCP Enhancement
- Test: skill should trigger on 90%+ of relevant queries
- Use `skill-creator` skill in Claude Code to generate first drafts
- Skills work identically across claude.ai, Claude Code, and API

---

## The Tweet We Couldn't Read
`https://x.com/roundtablespace/status/2030595632998580328`
— Share contents when you find it, to benchmark current state against it
