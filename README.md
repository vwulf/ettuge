# ettuge

ettuge is a personal knowledge garden at the intersection of language, computation and close reading, held together by curiosity about how structure gives rise to meaning.

**Read it at [vwulf.github.io/ettuge](https://vwulf.github.io/ettuge/).** This repository holds the sources: Markdown under [`src/main/md`](src/main/md), which a GitHub Actions workflow turns into the site. The sections below follow the site's sidebar, in the same order.

---

## [Deep Dives](https://vwulf.github.io/ettuge/Deep-Dives/)

Close readings of papers and books, written up after the fact. Each entry gives the claim, how it works, and what is still open. Source: [`src/main/md/deep-dives`](src/main/md/deep-dives).

- **[Mathematics](https://vwulf.github.io/ettuge/Deep-Dives/math)**: the 2026 AI-math results (Unique Games, the ETH refutation, quasi-RH), complexity and number theory, Navier–Stokes and Yang–Mills, and what Lean checking does and doesn't settle
- **[AI and Machine Learning](https://vwulf.github.io/ettuge/Deep-Dives/ai)**: transformer theory, attention as an algorithm, compositional structure, interpretability, architecture, training at scale, serving and decision models
- **[Health and Fitness](https://vwulf.github.io/ettuge/Deep-Dives/fitness)**: protein and longevity, body composition and DXA, active rest, lactate and the heart, training intensity, *Outlive* against the papers
- **[Ellara Kannada](https://vwulf.github.io/ettuge/Deep-Dives/ellara-kannada)**: DNS Bhat's grammar applied to Pampa, the two kinds of "we", auxiliaries, Sangam Tamil in Eke, the ಎ-ಎಣಿಕೆ notation, tense–aspect–mood against Chomsky
- **[Textbooks](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/)**: more than 70 textbooks broken down book → chapter → section → PDF pages, grouped by subject (AI and ML, computer science, mathematics, linguistics, physics)
- **[Karate › Reading the sources](https://vwulf.github.io/ettuge/karate/50-reading-the-sources)**: Motobu, Nagamine and Quast, read between the lines

## [ಕನ್ನಡ — Language and DNS Bhat](https://vwulf.github.io/ettuge/kannaDa/)

Source: [`src/main/md/kannada`](src/main/md/kannada).

- **[Dr. D. N. Shankara Bhat — digital archive](https://vwulf.github.io/ettuge/kannaDa/dnsbhat/)**: all 33 known works by the linguist whose central argument is that Kannada grammar must be built from Kannada's own structure. Transcripts, recovered blog posts and OCR'd books, each with structured Kannada text, Eke romanisation and an English summary. The [catalogue](src/main/md/kannada/dnsbhat/README.md) gives each book's status, and the [project recap](docs/dnsbhat/PROJECT-RECAP.md) documents the pipeline: OCR, legacy-font decoding, cross-link audits and Eke romanisation.
- **[Eke — a romanisation for Kannada](https://vwulf.github.io/ettuge/kannaDa/eke/reference)**: a lightweight scheme between informal internet habits and Harvard-Kyoto, following Bhat's *Ellara Kannada* in dropping aspirates that natural Kannada speech doesn't have. Full specification: [`Eke.md`](src/main/md/kannada/Eke.md).
- **[Grammar](https://vwulf.github.io/ettuge/kannaDa/grammar/)**: illustrated verb paradigms (ಮಾಡು, ಇರು, ಇಲ್ಲ) and Bhat's framework compared with others.
- **[Zero Speculation](https://vwulf.github.io/ettuge/kannaDa/eke/zero-speculation-illustrated.html)**: an essay linking the Tamil *puḷḷi*, the possible Dravidian etymology of *śūnya* and the K-127 Cambodia inscription (683 CE) to argue that the substrate for zero may be older and Dravidian.

## [CS & AI](https://vwulf.github.io/ettuge/FP/)

Articles and deep dives on programming-language theory, algebra and categories, algorithms, effects in LLM systems and formal proof, worked out mostly in Haskell, Scala and Lean. Sources: [`src/main/md/pl`](src/main/md/pl) (topic pages in [`pl/buckets`](src/main/md/pl/buckets)), [`haskell`](src/main/md/haskell) and [`kojo`](src/main/md/kojo).

- **[Foundations: λ-calculus and Types](https://vwulf.github.io/ettuge/FP/bucket-foundations)**: ॐλ, reduction strategies, fixed points, parsers that terminate
- **[Algebra and Categories](https://vwulf.github.io/ettuge/FP/bucket-algebra-categories)**: monoids, applicatives vs monads, representable functors, Yoneda, Kan extensions, adjunctions, Poly, Markov and traced categories, Funcformer
- **[Algorithms, Functionally](https://vwulf.github.io/ettuge/FP/bucket-algorithms)**: lazy min-k, the ಕಳ್ಳ pumpkin puzzle, Bird–Gibbons vs CLRS, recursion schemes
- **[Effects and LLM Systems](https://vwulf.github.io/ettuge/FP/bucket-effects-llm)**: λ-RLM, RLM and Context LMs, DSPy as effects, decision models, languages for agents
- **[Proof and Formalization](https://vwulf.github.io/ettuge/FP/bucket-proof-formalization)**: Lean, autoformalization, Rocq proofs over compiled binaries
- **[Creative Coding](https://vwulf.github.io/ettuge/FP/bucket-creative-coding)**: *rangapura vihAra* in Euterpea, Kojo turtle graphics

## [Books](https://vwulf.github.io/ettuge/Books/Books)

A [catalog of books](src/main/md/Books/Books.md) that changed how the author thinks, with summaries and takeaways. Alongside it are the [technical shelf](src/main/md/Books/Technical.md) and the [papers](src/main/md/Books/Papers.md) behind the deep dives, marked 🔍.

## [Karate](https://vwulf.github.io/ettuge/karate/)

An ongoing series on Matsubayashi-ryū karate and kobudō: kata attribution, terminology, training structure and reflections. Source: [`src/main/md/karate`](src/main/md/karate).

## [Reflection](https://vwulf.github.io/ettuge/Reflection/)

Raw notes: years of reading and bookmarking, exported from a Signal self-channel and sorted by topic but otherwise unprocessed. The processed versions live under Deep Dives. Source: [`src/main/md/self-reflection`](src/main/md/self-reflection).

## [Tinkering](https://vwulf.github.io/ettuge/Tinkering/)

Hardware and making posts, starting with a Diwali postmortem on a clap-activated diya. Source: [`src/main/md/tinkering`](src/main/md/tinkering).

## [日本語](https://vwulf.github.io/ettuge/nihongo/)

The Japanese writing system, read through Kannada: every kana beside its matching ಕನ್ನಡ akshara and Eke spelling, and a searchable page of all 2,136 jōyō kanji. Source: [`src/main/md/nihongo`](src/main/md/nihongo).

---

## How the site is built

- **Workflow:** [`.github/workflows/pages.yml`](.github/workflows/pages.yml) copies the sources into `docs/`, splits long pages into chapters, writes the sidebar front matter and builds with Jekyll ([just-the-docs](https://just-the-docs.com/)). Source files carry no front matter unless their section says otherwise.
- **Before pushing:** `python3 .claude/skills/ettuge-pre-deploy-check/scripts/sanity_check.py` checks the config, the sidebar orders and the source files the workflow expects.
- **For contributors and Claude sessions:** [`CLAUDE.md`](CLAUDE.md) has the full project guide: directory layout, the DNS Bhat methodology, Eke rules and the transcript pipeline.
