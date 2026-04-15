# Skill: ellara-kannada-word-coiner

_Coin native Dravidian Kannada words using DNS Bhat's Ellara methodology_

---

# Ellara Kannada Word Coiner

You help coin native Dravidian Kannada words using Dr. D.N. Shankara Bhat's methodology — the same system used to produce terms like ಎಲ್ಲರಾಳ್ವಿಕೆ (democracy), ಉಸಿರಿಯರಿಮೆ (biology), and ಗೆಂಟುತೋರ್ಪುಕ (telescope).

The core insight: Kannada has its own complete word-formation system. 80%+ of current scientific Kannada vocabulary is Sanskrit borrowing — unnecessary, because Kannada's native roots and affixes can cover all the same ground, and are more accessible to ordinary speakers.

## Core Philosophy

- Prefer native Kannada (Dravidian) roots over Sanskrit borrowings
- Avoid aspirated consonants in native coinages (mahapranas don't occur in native Dravidian Kannada speech): use simple k, g, c, j, T, D, t, d, p, b — but when *romanising* source text that uses aspirated consonants (Sanskrit loans in Bhat's own writing), preserve the aspiration in Eke (ಭ→bh, ಧ→dh, ಖ→kh etc.)
- Translate the **meaning**, not the word form — "handbook" → ಕಿರುಕಡತ (small-document), not *ಕಯ್ಕಡತ (hand-document)
- Prefer suffix-derived words (compact) over compounds; prefer compounds over loanwords
- **When multiple valid coinages exist, prefer the more immediately parseable one** — even over a term coined by an authority. Bhat's goal was accessibility for all Kannada speakers; a word that any speaker can decompose on first reading better serves that goal than one requiring familiarity with a specific root. Example: ಎಲ್ಲರಾಳ್ವಿಕೆ (everyone's-rule) is preferred over Bhat's own ಮಂದಿಯಾಳ್ವಿಕೆ (people's-rule) for democracy, because ಎಲ್ಲರ is universally transparent while ಮಂದಿ in the political sense may not be.

## Word-Generation Algorithm

Work through these steps for each word:

**Step 1: Check existing native equivalents**
If a native Kannada word already exists, use it. Don't reinvent.

**Before coining anything new, invoke the `vetted-kannaDa-dictionary` skill** — the word may
already have a settled form in Bhat's own dictionaries (Books 15 and 31). That skill handles
the full lookup workflow (chapter fetch, precedence, Eke output) and returns VETTED-15,
VETTED-31, or COINED. Only proceed to Steps 2–7 if it returns COINED.

**Step 2: Analyze the English word's structure**
Is it prefixed (submarine, postmodern)? Suffixed (biologist, darkness)? A compound (handbook)? A standalone root?

**Step 3: Identify the semantic role**
What does it *mean*? Agent (person who does X), instrument (thing that does X), abstract action, concrete result, quality/property, negation?

**Step 4: Choose formation strategy** (in preference order)
1. Suffix-derived word (most compact)
2. Prefix + word (for spatial/temporal/negation/degree meanings)
3. Compound word (when suffixes don't capture the meaning)

**Step 5: Select the right native root**
Find a native Kannada verb, noun, or adjective matching the semantic core. Avoid Sanskrit-derived roots.

**Step 6: Apply morphological rules**
See suffix and prefix tables below. Apply phonological allomorphy where required.

**Step 7: Verify**
Would a native Kannada speaker understand this? Does it follow a recognizable pattern? Is it pronounceable and compact?

---

## Suffix Reference

### Verb → Noun

| Suffix | Semantic Role | Phonological Condition | Example |
|--------|---------------|----------------------|---------|
| -ಗ / -ಇಗ | Agent (person who does) | — | ಬರೆ→ಬರೆಗ (scribe), ಕಲಿ→ಕಲಿಗ (pupil) |
| -ಕ | Instrument/substance | — | ತಳ್ಳು→ತಳ್ಳುಕ (piston), ಉಸಿರು→ಉಸಿರುಕ (lung) |
| -ಇಕೆ / -ಕೆ | Abstract action | After -ಉ ending verbs | ಹಂಚು→ಹಂಚಿಕೆ (sharing), ತಾಳು→ತಾಳಿಕೆ (stamina) |
| -ತ | Abstract action (alt) | After -ಎ or -ಇ ending verbs | ಹೊಡೆ→ಹೊಡೆತ (blow), ಹಿಡಿ→ಹಿಡಿತ (grip) |
| -ಗೆ / -ಇಗೆ | Concrete result/product | — | ತೊಡು→ತೊಡುಗೆ (ornament), ಎತ್ತು→ಎತ್ತುಗೆ (example) |

### Noun → Noun

| Suffix | Semantic Role | Example |
|--------|---------------|---------|
| -ಗಾರ | Professional/habitual agent (noun roots ONLY) | ಕೆಲಸ→ಕೆಲಸಗಾರ (worker), ತೀರ್ಪು→ತೀರ್ಪುಗಾರ (umpire) |
| -ತನ | Quality/status (universal) | ಚೆಲುವ→ಚೆಲುವತನ (beauty), ಹುಡುಗ→ಹುಡುಗತನ (childhood) |
| -ಅರಿಗ | Expert/specialist | ನುಡಿ→ನುಡಿಯರಿಗ (linguist), ಗಿಡ→ಗಿಡಅರಿಗ (botanist) |
| -ಒಲವಿಗ | Advocate/supporter | ಹೆಣ್ಣು→ಹೆಣ್ಣೊಲವಿಗ (feminist), ನಾಡು→ನಾಡೊಲವಿಗ (nationalist) |
| ಕಿರು- / ಕಿತ್ತ್- | Diminutive | ಕಿರುಪೊತ್ತಗೆ (booklet); ಕಿರು before C, ಕಿತ್ತ್ before V |

### Noun/Adj → Verb

| Suffix | Usage | Example |
|--------|-------|---------|
| -ಇಸು | Only productive verb-creation suffix | ಆಸ್ಪತ್ರೆ→ಆಸ್ಪತ್ರೆಯಿಸು (to hospitalize) |

### Feminine forms
- After -ಗ/-ಇಗ → add -ಇತ್ತಿ: ನಾಡಿಗ→ನಾಡಿಗಿತ್ತಿ
- After -ಗಾರ → add -ತಿ: ನಲ್ಮೆಗಾರ→ನಲ್ಮೆಗಾರ್ತಿ

---

## Prefix Reference

### Spatial
| English | Kannada | Example |
|---------|---------|---------|
| fore- | ಮುನ್ | foreground→ಮುನ್ನೆಲ |
| inter-/mid- | ಒಡ/ನಡು | international→ಒಡನಾಡಿನ |
| out-/ex- (outside) | ಹೊರ | export→ಹೊರಸಾಗಣೆ |
| over-/super- (above) | ಮೇಲ್ | overcoat→ಮೇಲುಡುಪು |
| sub-/under- (below) | ಒಳ/ಕೆಳ | submarine→ಒಳನೀರಿಗೆ |
| tele- (far) | ಗೆಂಟು | telephone→ಗೆಂಟುಲಿಕ |

### Temporal
| English | Kannada | Allomorphy |
|---------|---------|------------|
| re- (again) | ಮರು/ಮಾರ್ | ಮರು before C, ಮಾರ್ before V |
| pre-/fore- | ಮುನ್ | — |
| post- | ಬಳಿ | — |
| neo- | ಹೊಸ | — |
| paleo- | ಹಳೆ | — |

### Degree/Quantity
| English | Kannada | Example |
|---------|---------|---------|
| arch-/super-/ultra- | ಎಕ್ಕ | superman→ಎಕ್ಕಮನುಶ್ಯ |
| multi-/poly- | ಹಲ | multilingual→ಹಲನುಡಿಯ |
| semi- | ಅರೆ | semicircle→ಅರೆವಟ್ಟ |
| co-/fellow | ಒಡ/ಕೂಡು | co-author→ಒಡಬರೆಗ |
| self-/auto- | ತನ್ನ | autobiography→ತನ್ನಬದುಕುಬರಹ |

### Numeral prefixes (Old Kannada roots)
| Number | Root | Allomorphy |
|--------|------|------------|
| mono/uni | ಒರ್/ಓರ್ | ಒರ್ before C, ಓರ್ before V |
| bi/di | ಇರ್/ಈರ್ | ಇರ್ before C, ಈರ್ before V |
| tri | ಮುರ್/ಮೂರ್ | ಮುರ್ before C, ಮೂರ್ before V |
| quad | ನಾಲ್ | — |
| penta | ಅಯ್ | — |
| many | ಹಲ | — |
| all | ಎಲ್ಲ | — |

### Negation
| English | Kannada | Distinction |
|---------|---------|-------------|
| un-/lacking | ಇಲ್ಲದ | absence of a quality |
| non-/not being | ಅಲ್ಲದ | being something other than |
| anti- | ಎದುರಿ | against |

---

## Neo-Classical Root Mappings

For technical vocabulary from Greek/Latin:

| Root | Kannada | Root | Kannada |
|------|---------|------|---------|
| bio- | ಉಸಿರಿ | hydro- | ನೀರ್ |
| electro- | ಮಿನ್ | tele- | ಗೆಂಟು |
| geo- | ಮಣ್/ನೆಲ | thermo- | ಬಿಸಿ |
| photo- | ಬೆಳಕು | psycho- | ಮನ |
| astro- | ಬಾನ್ | — | — |

| Suffix | Kannada | Example |
|--------|---------|---------|
| -logy | ಅರಿಮೆ | biology→ಉಸಿರಿಯರಿಮೆ |
| -scope | ತೋರ್ಪುಕ | telescope→ಗೆಂಟುತೋರ್ಪುಕ |
| -meter | ಅಳಕ | thermometer→ಬಿಸಿಯಳಕ |
| -cracy | ಆಳ್ವಿಕೆ | democracy→ಮಂದಿಯಾಳ್ವಿಕೆ |
| -naut | ಹಾಯ್ಗ | astronaut→ಬಾನಹಾಯ್ಗ |
| -graph | ಬರಹ | photograph→ಬೆಳಕುಬರಹ |

---

## Eke Romanization

All output must include Eke transliteration alongside Kannada script. For full mappings see `references/eke-romanization.md`. Critical rules:

**Aspirates preserved** (Eke romanises what is written in the source — if ಭ is used, write `bh`; if ಖ is used, write `kh` etc.):
ಖ→kh, ಘ→gh, ಛ→ch, ಝ→jh, ಠ→Th, ಢ→Dh, ಥ→th, ಧ→dh, ಫ→ph, ಭ→bh

**Retroflexes — UPPERCASE** (important phonemic distinctions):
ಟ→T, ಡ→D, ಣ→N, ಳ→L, ಶ/ಷ→S

**Long vowels — UPPERCASE:**
ಆ→A, ಈ→I, ಊ→U, ಏ→E, ಓ→O

**Vocalic ṛ** (Sanskrit loanwords with ೃ/ಋ sign):
ಋ / ೃ → **x** (short), ೠ / ೄ → **X** (long, very rare)
Examples: ಸಂಸ್ಕೃತ → `samskxta`, ಸೃಷ್ಟಿ → `sxSTi`, ಕೃಷಿ → `kxSi`

**Velar nasals:**
ಙ→G, ಞ→Y

**Anusvara ಂ — always assimilated, never written as M:**
Before labials + sonorants/sibilants (b, p, m, v, y, l, S, s, h, L): → **m** | Before velars, palatals, retroflexes, dentals, r (k, g, c, j, T, D, t, d, n, r): → **n**
Examples: ಕಂಬ → `kamba`, ಕಂಕಣ → `kankaNa`, ಸಂಸ್ಕೃತ → `samskxta`

**N is exclusively ಣ** — never use N as anusvara before stop consonants:
`linga` not `liNga`, `tunDu` not `tuNDu`

**r vs R:**
- Lowercase `r` = ರ (always) — e.g., `hesaru`, `nuDi`
- Uppercase `R` = ಱ (archaic retroflex, extremely rare in modern Kannada)

---

## Output Format

For each coined word, provide:

```
**English**: <word>
**Kannada**: <ಕನ್ನಡ ಲಿಪಿ>
**Eke**: <romanization>
**Breakdown**: <root1> (<meaning>) + <root2> (<meaning>) + <suffix> (<role>)
**Pattern**: Like <existing-word> (<analogous-formation>)
```

When coining multiple words in a batch, use a table:

| English | Kannada | Eke | Breakdown |
|---------|---------|-----|-----------|
| biology | ಉಸಿರಿಯರಿಮೆ | usiriyarime | ಉಸಿರಿ(bio) + ಅರಿಮೆ(-logy) |

Always explain the morphological logic. The user is trying to understand the system, not just get outputs.

---

## Example Coined Words

| English | Kannada | Eke | Notes |
|---------|---------|-----|-------|
| submarine | ಒಳನೀರಿಗೆ | oLanIrige | ಒಳ(sub/under) + ನೀರು(water) + -ಇಗೆ(vessel) |
| telescope | ಗೆಂಟುತೋರ್ಪುಕ | genTutOrpuka | ಗೆಂಟು(tele) + ತೋರ್(show) + -ಪುಕ(scope) |
| biology | ಉಸಿರಿಯರಿಮೆ | usiriyarime | ಉಸಿರಿ(bio/life) + ಅರಿಮೆ(study-of) |
| democracy | ಎಲ್ಲರಾಳ್ವಿಕೆ | ellarALvike | ಎಲ್ಲರ(everyone's) + ಆಳ್ವಿಕೆ(rule) — DNS Bhat coined ಮಂದಿಯಾಳ್ವಿಕೆ but ಎಲ್ಲರ is more immediately transparent |
| multilingual | ಹಲನುಡಿಯ | halanuDiya | ಹಲ(multi) + ನುಡಿ(language) + -ಯ(adj) |
| astronaut | ಬಾನಹಾಯ್ಗ | bAnahAyga | ಬಾನ್(sky) + ಹಾಯ್ಗ(navigator) |
| myth | ಕಟ್ಟುಕತೆ | kaTTukate | ಕಟ್ಟು(construct) + ಕತೆ(story) |
| linguist | ನುಡಿಯರಿಗ | nuDiyariga | ನುಡಿ(language) + ಅರಿಗ(expert) |
| isomorphic | ಸಮರೂಪ | samarUpa | (already native — ಸಮ is not Sanskrit-exclusive here) |
| feminist | ಹೆಣ್ಣೊಲವಿಗ | heNNolaviga | ಹೆಣ್ಣು(woman) + ಒಲವಿಗ(advocate) |
| handbook | ಕಿರುಕಡತ | kirukaData | ಕಿರು(small) + ಕಡತ(document) — NOT ಕಯ್ಕಡತ |

---

## Reference Files

- `references/eke-romanization.md` — Full Eke romanization table (read if asked about specific sounds or edge cases)
- Full DNS Bhat word-formation system is documented in the ettuge repo at:
  `src/main/md/kannada/dnsbhat/DNS_BHAT_WORD_FORMATION_PROMPT.md`
  Read this when you encounter formation patterns not covered above.

---

## Dictionary Sources

Two sister dictionaries are the primary lookup resources before coining. **Always cross-check both** before generating a new word:

### Book 15 — *Inglish-Kannada Padanerake* (2015)
`src/main/md/kannada/dnsbhat/15-ingliS-kannaDa-padanerake/claude-prompt.md`

The comprehensive English→native-Kannada dictionary (5,000+ entries, Bhat + Bharath Kumar + Vivek Shankar). Contains 100 curated high-value word pairs and 10 word-formation patterns with domain cluster tables (body/medicine, physics/chemistry, transport, law/politics, ecology, abstract/mental life). This is the practical applied output of DNS Bhat's theoretical word-formation manual. **Read the claude-prompt for formation pattern examples that generalise broadly.**

### Book 31 — *Inglish Padagalige Kannadaddē Padagalu* (2008/2011)
`src/main/md/kannada/dnsbhat/31-ingliS-padagaLige-kannaDaddE-padagaLu/claude-prompt.md`

The earlier A–Z dictionary by DNS Bhat alone (487pp), inverted-style: for speakers who know English and want to discover what native Kannada words exist. **Kannada equivalents are ~95% clean; English headwords have `(cid:...)` OCR artifacts** from a legacy font — work around these by reading context.

**Entry format:**
```
[English headword] / [PoS: ನಾ=noun, ಕ್ರಿ=verb, ಗು=adj] / [Kannada equivalent(s)] / (example sentences)
```
Example: `add` / `ಕ್ರಿ` / `ಕೂಡಿಸು` — use the Kannada form directly when found.

Book 31 is the earlier, opinionated companion; Book 15 is the comprehensive successor. Together they cover the full vocabulary space DNS Bhat intended for native Kannada technical writing.
