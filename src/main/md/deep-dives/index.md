# Deep Dives

Close readings of papers and books, written up after the fact. Each entry gives the claim, how it works, and what is still open, not the paper's abstract. The papers and books themselves are catalogued (🔍) in [Papers](../Books/Papers) and [Technical](../Books/Technical). [Reflection](../Reflection/) has the older, unprocessed notes.

## Topics

- [Mathematics](math): the 2026 AI-math results, complexity theory, number theory, the Millennium problems, and formalization
- [AI and Machine Learning](ai): transformer theory, attention as an algorithm, interpretability, architecture, training at scale, serving
- [Health and Fitness](fitness): diet and protein, body composition, active rest, lactate, training intensity, *Outlive* against the papers
- [Ellara Kannada](ellara-kannada): DNS Bhat's books, Pampa's line, auxiliaries, Rudram, Sangam Tamil in Eke, the ಎ-ಎಣಿಕೆ notation
- [Karate › Reading the sources](../karate/50-reading-the-sources): Motobu, Nagamine and Quast

The [CS & AI](../FP/) section keeps its deep dives next to the articles they belong to:

- [Foundations: λ-calculus and types](../FP/bucket-foundations.md)
- [Algebra and Categories](../FP/bucket-algebra-categories.md): applicatives, Poly, Markov and traced categories, categories in ML
- [Algorithms, Functionally](../FP/bucket-algorithms.md)
- [Effects and LLM Systems](../FP/bucket-effects-llm.md): λ-RLM, RLM, DSPy as effects, OpenClaw-RL, languages for agents
- [Proof and Formalization](../FP/bucket-proof-formalization.md): Lean and the 2026 AI-proof wave
- [Creative Coding](../FP/bucket-creative-coding.md)

## Across the topics

The short summaries below link into the topic pages.

---

## Mathematics

**One operator for all elementary functions, then Kannada names for it.** Odrzywołek shows that eml(x, y) = eˣ − ln y, together with the constant 1, generates every elementary function. It is the continuous analogue of a NAND gate, with grammar S → 1 | eml(S, S). Since eˣ = eml(x, 1), Euler's formula, cos and sin all reduce to trees of one node. The discussion then turned into an Ellara Kannada coinage exercise: a nine-symbol notation with no Latin letters. ಏ stands for exp, ಅ for ln, ಎ = ಏ − ಅ for eml itself, ಇ for the imaginary unit and ತಿ (from ತಿಳಿಯದ, "the unknown") for the variable. π is ಸುತ್ತುಪಾಲು, and the trig functions form a ಪಾಲು ("ratio") family: ನೇರಪಾಲು, ಪಕ್ಕಪಾಲು and ತಾಗುಪಾಲು. ತಾಗುಪಾಲು ("touching ratio") keeps the geometric meaning of *tangent* that the English word has lost. The full notation is in [Ellara Kannada Deep Dives](ellara-kannada).

**Complexity, number theory and the Millennium problems.** Each has its own section in [Math Deep Dives](math):
- [the OpenAI release](math/ch1) (what was verified, and the six results covered in depth)
- [complexity theory](math/ch2): the Unique Games proof skeleton, SDP, the ETH refutation and which problems inherit it, Chowla via MaxCut
- [number theory](math/ch3): quasi-RH 7/8 and 11/12, Siegel zeros, prime gaps, Goldbach
- [mathematical physics](math/ch4): Navier–Stokes and the credit dispute, the two Yang–Mills efforts
- [books and formalization](math/ch5): Riehl, ATLAS, CLRS
- [themes across them](math/ch6)

Sources: [Papers › Mathematics](../Books/Papers#mathematics), [Technical › Topology and Geometry](../Books/Technical#topology-and-geometry).

## AI and Machine Learning

**Transformer theory, attention as an algorithm, interpretability, architecture, training and serving.** Each has its own section in [AI Deep Dives](ai):
- [transformer theory](ai/ch1): Cirrincione's *Mathematical Theory of the Transformer* (INCRT, rank-neutrality, head-channel identifiability, positional encodings) and why none of it shows attention is optimal
- [attention as an algorithm](ai/ch2): soft lookup versus DP, semirings, the temperature scale from lookup to join, RASP and Tracr
- [compositional structure](ai/ch3): the MDL definition, and its decomposition tree as a rose tree
- [networks as programs](ai/ch4): the mechanistic-interpretability survey and weight-space programming
- [architecture](ai/ch5): MoE, GQA, MLA, Mamba, diffusion LMs, TTT, Titans, Mixture of Depths, SpikingBrain against Hinton, neural operators and what changed since FNO
- [training at scale](ai/ch6): tensor, pipeline, sequence, context and expert parallelism, ZeRO/FSDP, mixed precision, FlashAttention, checkpointing, how they stack, BendTorch's oracle harness
- [serving and judging](ai/ch7): disaggregated prefill/decode, decision models (Laya, Jev) versus reasoning models, decision models as eval judges
- [themes across them](ai/ch8), including Fourier analysis as a recurring tool

Sources: [Papers › AI and Machine Learning](../Books/Papers#ai-and-machine-learning), [Papers › LLM Inference Serving](../Books/Papers#llm-inference-serving), [Technical › Deep Learning](../Books/Technical#deep-learning).

## Linguistics and Scripts

**DNS Bhat's corpus.** All 33 of Bhat's books are catalogued under [DNS Bhat](../kannaDa/dnsbhat/). The deep dives returned repeatedly to his central claim: Kannada grammar has been described through Sanskrit (and later English) categories, which hide its Dravidian structure.

**Ellara Kannada.** Pampa's ಮಾನಸರ್ and the two kinds of "we" in the same line, Bhat's verb counts and the missing auxiliaries, a native Śrī Rudram verse, *Aiṅkuṟunūṟu* 323 in Eke, the dhole/ಕಿರುಬ/ಚಿರತೆ etymologies, the ಎ-ಎಣಿಕೆ maths notation, karate terms, coinage precedence and the pangram each have their own section in [Ellara Kannada Deep Dives](ellara-kannada).

**Where did zero's dot come from?** The hypothesis is that abugida scripts already had a visible "nothing in this slot" mark, the Tamil-Brāhmī puḷḷi, before positional zero appears in inscriptions, and that this was the conceptual precondition. Tamil kept additive numerals because it already had a native absence marker. Kannada adopted ೦ late, around the time its virama became consistently visible. The follow-up asked whether the earliest Indosphere zero, a Cambodian inscription, owes more to a Kadamba/Pallava-Grantha line than to Tamil-Brāhmī. See the [illustrated write-up](../kannaDa/eke/zero-speculation-illustrated.html).

**Paternal lineages between South Asia and South China.** He et al.'s large Y-chromosome study finds that modern Indian and South Chinese paternal lines share only a deep FT-M89 trunk (about 52–70 thousand years ago), with no Neolithic or later shared lineages. Rare F lineages persist along coastal (Guangdong) and inland (Yunnan) routes. Shared deep ancestry and recent contact are different claims, and this paper supports only the first.

Sources: [Papers › Linguistics and Languages](../Books/Papers#linguistics-and-languages), [Papers › Other](../Books/Papers#other).

## Martial Arts

**What the karate sources say between the lines.** Motobu argues about the order in which kata and application are trained. Nagamine shows dissent through curriculum choices under *honne/tatemae*, and *Tales* gives the older masters their full weight. The *hōgen* ban left its mark on kata names, and attested kobudō names show competing Uchinaaguchi sound rules. Each is covered in [Karate › Reading the sources](../karate/50-reading-the-sources).

## Health and Nutrition

**Diet, body composition, exercise metabolism and training.** Each has its own section in [Fitness Deep Dives](fitness). These cover published evidence and general training principles only, with no personal measurements:
- [diet, protein and longevity](fitness/ch2): the Harvard cohort papers (Tessier, Glenn, Malik), Fanti's methionine-supplemented longevity diet, Longo's *The Longevity Diet*, and how much protein different goals need
- [body composition and how it is measured](fitness/ch3): creatine without exercise and the DXA water confound, Tromsø visceral-fat reference values, GlasVEGAS, scan hygiene, VO₂max per kilogram
- [sitting, squatting and active rest](fitness/ch4): textile-EMG sitting data and the Hadza
- [lactate and the heart](fitness/ch5): MCT1, necessity versus sufficiency, and what it does and doesn't say about zone training
- [training intensity](fitness/ch6): what "Zone 2" means, lab versus watch thresholds, RER, watch VO₂max
- [interval formats and cross-training](fitness/ch7): the 4×4, hill sprints, REHIT, erg substitutions, critical power, ergs versus resistance training
- [popular sources checked](fitness/ch8)
- [*Outlive* against the papers](fitness/ch9): Attia's book set against the evidence above
- [reading habits](fitness/ch10)

**Other threads.** A systematic review of 29 RCTs on magnesium and serum lipids. [Papers › Other](../Books/Papers#other)
