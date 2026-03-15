# Kannada Wiktionary Generation: Cost Analysis
## Claude vs Kimi K2.5 vs Groq (Llama 4 / Qwen3)

---

## Targets

| Scenario | Entry Count | Description |
|----------|-------------|-------------|
| **Base** | ~265,515 | Match current Kannada Wiktionary size |
| **Stretch** | ~9,860,000 | Match English Wiktionary scale |

---

## Assumptions

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| System prompt (word-formation guide) | ~10,000 tokens | The 750-line DNS_BHAT_WORD_FORMATION_PROMPT.md in Kannada Unicode |
| Words per API batch | 20 | Balance between context and quality |
| Fresh input per batch | ~700 tokens | 20 English words + brief context + format instructions |
| Output per batch | ~4,000 tokens | 20 words × ~200 tokens each (Kannada word + morphological breakdown + example + Sanskrit replacement) |
| Cache hit rate | ~100% | System prompt is identical across all calls |

---

## Token Volumes

### Base scenario (265,515 entries)

| Component | Calculation | Tokens |
|-----------|-------------|--------|
| API calls | 265,515 ÷ 20 | 13,276 |
| Cached input (system prompt) | 13,276 × 10,000 | 133M |
| Fresh input (word lists) | 13,276 × 700 | 9.3M |
| Output | 13,276 × 4,000 | 53M |

### Stretch scenario (9.86M entries)

| Component | Calculation | Tokens |
|-----------|-------------|--------|
| API calls | 9,860,000 ÷ 20 | 493,000 |
| Cached input | 493,000 × 10,000 | 4,930M |
| Fresh input | 493,000 × 700 | 345M |
| Output | 493,000 × 4,000 | 1,972M |

---

## Model Pricing (per 1M tokens)

| Model | Input | Cached Input | Output | Source |
|-------|-------|-------------|--------|--------|
| **Claude Sonnet 4.5 (Batch API)** | $1.50 | $0.15 | $7.50 | Anthropic (50% batch discount) |
| **Kimi K2.5 (OpenRouter)** | $0.50 | $0.10 | $2.80 | OpenRouter |
| **Kimi K2.5 (DeepInfra, cheapest)** | $0.45 | ~$0.10 | $2.25 | DeepInfra via OpenRouter |
| **Kimi K2.5 (OpenCode Zen, current)** | FREE | FREE | FREE | Temporary promotional period |
| **Llama 4 Scout (Groq)** | $0.11 | N/A* | $0.34 | groq.com |
| **Llama 4 Maverick (Groq)** | $0.50 | N/A* | $0.77 | groq.com |
| **Qwen3 32B (Groq)** | $0.29 | N/A* | $0.59 | groq.com |
| **Llama 4 Scout (Groq Batch)** | $0.055 | N/A* | $0.17 | groq.com (50% batch discount) |
| **Llama 4 Maverick (Groq Batch)** | $0.25 | N/A* | $0.385 | groq.com (50% batch discount) |
| **Qwen3 32B (Groq Batch)** | $0.145 | N/A* | $0.295 | groq.com (50% batch discount) |

*Groq does NOT offer prompt caching — all input tokens charged at full price. Total input per call = 10,700 tokens (system prompt sent every time).

---

## Cost Comparison: Base Scenario (265K entries)

Note: Groq has no prompt caching, so total input per call = 10,700 tokens (system prompt re-sent each time).
Total input for base = 13,276 × 10,700 = **142M tokens**. For stretch = 493,000 × 10,700 = **5,275M tokens**.

| Cost Component | Claude Sonnet 4.5 (Batch) | Kimi K2.5 (OpenRouter) | Kimi K2.5 (DeepInfra) | Llama 4 Scout (Groq) | Llama 4 Scout (Groq Batch) | Llama 4 Maverick (Groq) | Maverick (Groq Batch) | Qwen3 32B (Groq) | Qwen3 32B (Groq Batch) |
|---------------|---|---|---|---|---|---|---|---|---|
| Input (142M / 133M cached + 9.3M fresh) | $33.90 | $17.95 | $17.49 | $15.62 | $7.81 | $71.00 | $35.50 | $41.18 | $20.59 |
| Output (53M) | $397.50 | $148.40 | $119.25 | $18.02 | $9.01 | $40.81 | $20.41 | $31.27 | $15.64 |
| **TOTAL** | **$431** | **$166** | **$137** | **$34** | **$17** | **$112** | **$56** | **$72** | **$36** |
| vs Claude | — | 61% ↓ | 68% ↓ | 92% ↓ | **96% ↓** | 74% ↓ | 87% ↓ | 83% ↓ | 92% ↓ |

## Cost Comparison: Stretch Scenario (9.86M entries)

| Cost Component | Claude Sonnet 4.5 (Batch) | Kimi K2.5 (OpenRouter) | Kimi K2.5 (DeepInfra) | Llama 4 Scout (Groq) | Llama 4 Scout (Groq Batch) | Llama 4 Maverick (Groq) | Maverick (Groq Batch) | Qwen3 32B (Groq) | Qwen3 32B (Groq Batch) |
|---|---|---|---|---|---|---|---|---|---|
| Input (5,275M / 4,930M cached + 345M fresh) | $1,257.00 | $665.50 | $648.25 | $580.25 | $290.13 | $2,637.50 | $1,318.75 | $1,529.75 | $764.88 |
| Output (1,972M) | $14,790.00 | $5,521.60 | $4,437.00 | $670.48 | $335.24 | $1,518.44 | $759.22 | $1,163.48 | $581.74 |
| **TOTAL** | **$16,047** | **$6,187** | **$5,085** | **$1,251** | **$625** | **$4,156** | **$2,078** | **$2,693** | **$1,347** |
| vs Claude | — | 61% ↓ | 68% ↓ | 92% ↓ | **96% ↓** | 74% ↓ | 87% ↓ | 83% ↓ | 92% ↓ |

---

## Summary Table

| Scenario | Claude 4.5 (Batch) | Kimi K2.5 | Llama 4 Scout (Groq) | Scout (Groq Batch) | Llama 4 Maverick (Groq) | Maverick (Groq Batch) | Qwen3 32B (Groq) | Qwen3 (Groq Batch) |
|----------|---|---|---|---|---|---|---|---|
| Base (265K) | $431 | $137–166 | $34 | **$17** | $112 | $56 | $72 | $36 |
| Stretch (9.86M) | $16,047 | $5,085–6,187 | $1,251 | **$625** | $4,156 | $2,078 | $2,693 | $1,347 |

**Cheapest option: Llama 4 Scout on Groq Batch — $17 for 265K entries, $625 for 9.86M entries.**

---

## Quality Considerations

### Groq Models (Llama 4 / Qwen3)

**Llama 4 Scout ($17 batch)** — The ultra-budget option:
- 17B active params (109B total MoE) — smallest model considered
- Likely weakest on Kannada morphology — may hallucinate suffixes or misapply sandhi rules
- Best for: Category A (legitimizing existing native words), where the task is mostly documentation
- Risk: May not handle Old Kannada roots or novel compounds reliably

**Llama 4 Maverick ($56 batch)** — Strong mid-tier:
- 17B active params (400B total, 128 experts) — much larger expert pool
- Better multilingual performance expected from larger MoE
- Meta's Llama models have decent Indic language training data
- Good candidate for the bulk of the work

**Qwen3 32B ($36 batch)** — Dense model alternative:
- 32.8B dense parameters (all active on every token)
- Qwen series has strong multilingual coverage including South Asian languages
- "Thinking mode" could help with morphological rule application
- May outperform larger MoE models on structured linguistic tasks

**Kimi K2.5 ($137)** — Established baseline:
- 1T total params (32B active), strong on structured tasks
- Scores 76.8% SWE-Bench — good instruction following

**Claude Sonnet 4.5 ($431 batch)** — Quality ceiling:
- Most likely to have the deepest Kannada training data
- Best for Old Kannada root revival and subtle phonological judgments
- 25x more expensive than Scout batch — only justified for hard cases

### Key Risk: Kannada is Low-Resource

All cheaper models share this risk: Kannada (especially Old Kannada morphology) is underrepresented in training data. The DNS Bhat word-formation rules are highly systematic, which helps — a model can follow rules even without deep Kannada knowledge — but phonological correctness (sandhi, gemination, allomorphy) requires genuine language understanding.

### Recommended Approach

1. **Pilot test**: Run 200 words through Scout, Maverick, Qwen3, Kimi K2.5, and Claude
2. **Blind evaluation**: Have a Kannada speaker rate outputs without knowing which model produced them
3. **Find the quality floor**: Identify the cheapest model that produces >85% acceptable output
4. **Tiered generation**: Use the cheapest acceptable model for bulk, Claude for the hardest 10-25%

---

## Hybrid Strategy (Updated with Groq)

| Task | Best Budget Model | Fallback | % of entries |
|------|------------------|----------|-------------|
| Category A: Legitimize existing native words | Llama 4 Scout (Groq Batch) | — | ~60% |
| Category B: Revive Old Kannada forms | Qwen3 32B or Maverick | Claude Sonnet 4.5 | ~15% |
| Category C: Novel coining | Llama 4 Maverick (Groq Batch) | Claude Sonnet 4.5 | ~25% |

### Hybrid cost estimates (Base scenario, 265K entries):

| Strategy | Models Used | Cost |
|----------|-----------|------|
| All Claude (Batch) | Claude only | $431 |
| All Kimi K2.5 | Kimi only | $137 |
| All Qwen3 (Groq Batch) | Qwen3 only | $36 |
| All Scout (Groq Batch) | Scout only | **$17** |
| **Hybrid: Scout + Claude** | 60% Scout Batch, 40% Claude Batch | **$180** |
| **Hybrid: Maverick + Claude** | 60% Maverick Batch, 40% Claude Batch | **$206** |
| **Hybrid: Qwen3 + Claude** | 75% Qwen3 Batch, 25% Claude Batch | **$135** |

### Hybrid cost estimates (Stretch scenario, 9.86M entries):

| Strategy | Cost |
|----------|------|
| All Claude (Batch) | $16,047 |
| All Scout (Groq Batch) | $625 |
| Hybrid: Scout + Claude (60/40) | $6,800 |
| **Hybrid: Qwen3 + Claude (75/25)** | **$5,025** |

---

*Analysis date: 2026-02-19*
*Prices as of Feb 2026 — verify before execution*

Sources:
- [Groq Pricing](https://groq.com/pricing)
- [Llama 4 on Groq](https://groq.com/blog/llama-4-now-live-on-groq-build-fast-at-the-lowest-cost-without-compromise)
- [Groq on OpenRouter](https://openrouter.ai/provider/groq)
- [Kimi K2.5 on OpenRouter](https://openrouter.ai/moonshotai/kimi-k2.5)
- [Kimi K2.5 Price Analysis](https://artificialanalysis.ai/models/kimi-k2-5)
