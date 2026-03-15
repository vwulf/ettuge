# Kannada Knowledge Gap: Two Perspectives
## Top-Down Translation vs Bottom-Up Knowledge Indexing

---

## The Problem

English dominates the internet's structured knowledge. English Wikipedia has 6.8M articles; Kannada Wikipedia has ~30,000. In scientific and technical domains, 80%+ of Kannada vocabulary consists of Sanskrit loanwords (per DNS Bhat), making even existing Kannada content inaccessible to ordinary speakers.

But the gap isn't just about volume — it's about what kind of knowledge exists where.

---

## The "English-as-Superset" Myth

The assumption that English Wikipedia contains everything other languages have — just more of it — has been conclusively debunked:

- **75% of topics** across all Wikipedias exist in only one language edition (Hecht & Gergle, 2010)
- English Wikipedia is missing **60% of articles** present in the Ukrainian edition
- On average, **44% of content** in a French article is missing from the paired English article (WikiGap, 2025)
- About **25% of each Wikipedia edition** is culturally specific content not found elsewhere (Miquel-Ribé & Laniado, 2018)

English Wikipedia is not a superset — it's a complement. Each language edition carries unique knowledge shaped by its cultural context.

---

## Perspective 1: Top-Down — Bring English Knowledge to Kannada Readers

### What it is

Auto-translate English Wikipedia articles into Kannada, using a native Kannada lexicon (built via the Wiktionary phase) to ensure translated content uses accessible vocabulary rather than Sanskrit loans or untranslated English terms.

### Two-phase approach

1. **Phase 1 (Wiktionary):** Generate a comprehensive native Kannada vocabulary using DNS Bhat's word-formation methodology. Cost: $17–431 for 265K entries depending on model choice.
2. **Phase 2 (Wikipedia):** Translate English Wikipedia articles, drawing on the Phase 1 lexicon for technical terms.

### Strengths

- Addresses the most visible gap: Kannada speakers currently cannot access vast amounts of globally shared knowledge in their language
- Systematic and automatable — clear input (English articles), clear output (Kannada articles)
- The lexicon-first approach solves a specific MT failure mode: untranslated technical terms
- Well-studied problem with existing pipelines (e.g., English→Hindi Wikipedia transfer, December 2024)

### Limitations

- **Transfers English editorial priorities, not just content.** An article on "rice" translated from English will emphasize global trade economics and botanical taxonomy — not paddy cultivation in Malenadu, temple offerings, or the dozen Kannada words for rice at different processing stages.
- **Still reads like translated content.** The Hindi Wikipedia transfer project (2024) found this to be a persistent issue — the result fills a gap but doesn't close it.
- **Perpetuates the superset myth.** If the only Kannada Wikipedia content is translated English content, it reinforces the idea that English is the canonical source of knowledge.
- **MT quality for Kannada remains poor.** A 2024 evaluation found that MT evaluation metrics for Kannada achieve only 0.32 Kendall Tau correlation with human judgments.

### Best tools

- AI4Bharat's IndicTrans2 for Kannada translation
- DNS Bhat word-formation prompt for lexicon generation
- Groq Batch API (Llama 4 Scout/Qwen3) for cost-effective generation

---

## Perspective 2: Bottom-Up — Index Informal Kannada Knowledge

### What it is

There is an enormous amount of Kannada knowledge that exists only in oral or informal form — YouTube lectures, podcast conversations, temple discourse recordings, agricultural extension talks, folk medicine discussions, literary criticism, regional history narrations. None of this is indexed, searchable, or citeable. It is effectively invisible to the structured knowledge web.

The pipeline: **Audio/Video → ASR transcription → LLM cleanup → Structured extraction → Encyclopedia-style entries**

### Proof of concept: DNS Bhat's books

The DNS Bhat transcript project in this repository is exactly this pipeline in miniature:
- YouTube narrations of DNS Bhat's linguistics books by Malati Bhat
- YouTube auto-captions failed catastrophically (garbled "foreign foreign foreign")
- Website articles manually extracted as cleaner source
- LLM-driven structured extraction into word-formation rules
- Result: a comprehensive prompt template that didn't exist in any structured form before

### What Kannada YouTube knowledge looks like

Content that exists in Kannada YouTube but nowhere in English Wikipedia or any structured knowledge base:
- Yakshagana performance traditions and techniques
- Malnad agricultural practices and seasonal calendars
- Virashaiva/Lingayat philosophical commentaries
- Havyaka dialect documentation and grammar
- Kannada computational linguistics lectures (Kuvempu University, etc.)
- Regional ecology and ethnobotany of Western Ghats
- Temple architecture traditions specific to Karnataka
- Folk medicine practices of specific communities
- Oral histories of freedom movement in Karnataka

This knowledge only flows one direction — from Kannada to the world — and it needs to be captured before the speakers are gone.

### Existing precedents

- **Te Hiku Media (New Zealand):** Built ASR with 92% accuracy for te reo Māori. Created a living knowledge repository from elder recordings. Built their own platform rather than relying on YouTube due to cultural sovereignty concerns. Chief technologist Peter Lucas Jones named by Time as one of the most influential people in AI (2024).
- **AI4Bharat's IndicVoices:** 23.7K hours of speech data across 22 Indian languages, CC BY 4.0 licensed. Includes Kannada ASR models.
- **Nigeria's multilingual LLM (2024):** Government-backed LLM trained on 5 low-resource languages.
- **InkubaLM (Lelapa AI):** 0.4B parameter SLM for low-resource African languages, showing that small specialized models can outperform large general ones.

### Cost estimate for Kannada YouTube knowledge indexing

| Component | Volume | Cost |
|-----------|--------|------|
| ASR transcription (Groq Whisper) | 10,000 hours of Kannada YouTube | ~$1,111 |
| LLM structuring (Qwen3 Groq Batch) | ~50M output tokens | ~$15 |
| Human review/curation | Community effort | $0 (volunteer) or grant-funded |
| **Total** | | **~$1,126** |

For ~$1,100 you could transcribe and structure 10,000 hours of Kannada knowledge content — content that doesn't exist in any written form, in any language, anywhere.

### Challenges

- **ASR quality for Kannada:** YouTube auto-captions fail badly. IndicWhisper/IndicASR is much better but still imperfect for dialectal speech, technical vocabulary, and code-mixed content.
- **Cultural sovereignty:** Some oral knowledge may be sensitive or community-specific. The Te Hiku Media lesson: build your own platform, don't just dump everything on the open web.
- **Curation bottleneck:** Raw transcriptions need human review. This requires a community of Kannada-literate volunteers or paid curators.
- **Copyright:** YouTube content creators own their content. A knowledge extraction project needs to either get permission, work with willing creators, or limit extraction to facts (not expression).

---

## Where the Two Perspectives Meet

The most powerful version of this project combines both:

| Layer | Source | Purpose |
|-------|--------|---------|
| **Vocabulary (Foundation)** | DNS Bhat's word-formation system | Native Kannada lexicon for all technical terms |
| **Global knowledge (Scaffold)** | Translated English Wikipedia | Ensure Kannada speakers can access globally shared knowledge |
| **Cultural knowledge (Crown jewel)** | Indexed Kannada YouTube + oral sources | Knowledge that doesn't exist in English at all |

### Execution order

1. **Wiktionary phase** — Generate native Kannada vocabulary ($17–431)
2. **Wikipedia translation phase** — Translate English articles using native lexicon (separate cost estimate needed)
3. **YouTube indexing phase** — Transcribe and structure informal Kannada knowledge (~$1,100 for 10K hours)
4. **Cultural Wikipedia phase** — Create original Kannada Wikipedia articles from indexed oral knowledge (human-in-the-loop)

### The key insight

Phase 3 and 4 are what make this project genuinely valuable rather than just another translation effort. Every language can translate English Wikipedia. Only Kannada speakers can surface the knowledge that exists in Kannada oral traditions, lectures, and informal media. That's where the real knowledge gap runs — not from English to Kannada, but from Kannada oral culture to the structured knowledge web.

---

## Research Sources

- [WikiGap: Promoting Epistemic Equity (2025)](https://arxiv.org/html/2505.24195v2)
- [The Sum of Human Knowledge? Not in One Wikipedia Language Edition — Hecht (2013)](https://wikipedia20.mitpress.mit.edu/pub/26ke5md7/release/15)
- [Wikipedia Culture Gap: Quantifying Content Imbalances Across 40 Language Editions (2018)](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2018.00054/full)
- [Information Asymmetry in Wikipedia Across Languages (Roy, 2022)](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24553)
- [Effective Transfer of Knowledge from English to Hindi Wikipedia (2024)](https://arxiv.org/html/2412.05708v1)
- [Generative AI and LLMs in Language Preservation (2025)](https://arxiv.org/html/2501.11496v1)
- [Opportunities and Challenges of LLMs for Low-Resource Languages (2024)](https://arxiv.org/html/2412.04497v3)
- [Can Small Language Models Revitalize Indigenous Languages? — Brookings (2025)](https://www.brookings.edu/articles/can-small-language-models-revitalize-indigenous-languages/)
- [AI4Bharat IndicVoices Dataset](https://huggingface.co/datasets/ai4bharat/IndicVoices)
- [AI4Bharat ASR](https://ai4bharat.iitm.ac.in/areas/asr)
- [AI4Bharat IndicTrans2](https://github.com/AI4Bharat/IndicTrans2)
- [Groq Pricing](https://groq.com/pricing)
- [Wikimedia Research: Knowledge Gaps Program](https://research.wikimedia.org/knowledge-gaps.html)

---

*Analysis date: 2026-02-23*
