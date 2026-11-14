# Deep Dives

Short summaries of the discussions behind the 🔍 entries in [Papers](Papers.md) and [Technical](Technical.md), grouped by theme. Each one records what was asked and where the discussion ended up, not the paper's abstract. Functional programming themes live with their articles in the [Functional Programming](../FP/index.md) section, one page per topic:

- [Foundations: λ-calculus and types](../FP/bucket-foundations.md)
- [Algebra and Categories](../FP/bucket-algebra-categories.md) — applicatives, Poly, Markov and traced categories, categories in ML
- [Algorithms, Functionally](../FP/bucket-algorithms.md)
- [Effects and LLM Systems](../FP/bucket-effects-llm.md) — λ-RLM, RLM, DSPy as effects, OpenClaw-RL, languages for agents
- [Proof and Formalization](../FP/bucket-proof-formalization.md) — Lean and the 2026 AI-proof wave
- [Creative Coding](../FP/bucket-creative-coding.md)

---

## Mathematics

**One operator for all elementary functions, then Kannada names for it.** Odrzywołek shows that eml(x, y) = eˣ − ln y, together with the constant 1, generates every elementary function. It is the continuous analogue of a NAND gate, with grammar S → 1 | eml(S, S). Since eˣ = eml(x, 1), Euler's formula, cos and sin all reduce to trees of one node. The discussion then turned into an Ellara Kannada coinage exercise: a nine-symbol notation with no Latin letters. ಏ stands for exp, ಅ for ln, ಎ = ಏ − ಅ for eml itself, ಇ for the imaginary unit and ತಿ (from ತಿಳಿಯದ, "the unknown") for the variable. π is ಸುತ್ತುಪಾಲು, and the trig functions form a ಪಾಲು ("ratio") family: ನೇರಪಾಲು, ಪಕ್ಕಪಾಲು and ತಾಗುಪಾಲು. ತಾಗುಪಾಲು ("touching ratio") keeps the geometric meaning of *tangent* that the English word has lost. The full notation is in [Ellara Kannada Deep Dives](../Reflection/ellara-kannada-deep-dives.md).

**Complexity, number theory and the Millennium problems.** Each has its own section in [Math Deep Dives](../Reflection/math-deep-dives.md):
- [the OpenAI release](../Reflection/math-deep-dives/ch1) (what was verified, and the six results covered in depth)
- [complexity theory](../Reflection/math-deep-dives/ch2): the Unique Games proof skeleton, SDP, the ETH refutation and which problems inherit it, Chowla via MaxCut
- [number theory](../Reflection/math-deep-dives/ch3): quasi-RH 7/8 and 11/12, Siegel zeros, prime gaps, Goldbach
- [mathematical physics](../Reflection/math-deep-dives/ch4): Navier–Stokes and the credit dispute, the two Yang–Mills efforts
- [books and formalization](../Reflection/math-deep-dives/ch5): Riehl, ATLAS, CLRS
- [themes across them](../Reflection/math-deep-dives/ch6)

Sources: [Papers › Mathematics](Papers#mathematics), [Technical › Topology and Geometry](Technical#topology-and-geometry).

## AI and Machine Learning

**Cirrincione's *Mathematical Theory of the Transformer, Vol. I* proves its positional-encoding results, but its claims about the architecture growing itself have gaps.**
The book is built from seven of the author's arXiv preprints. Its MDS–Hellinger positional encoding and Positional Separation Theorem hold up. The Incremental Transformer (INCRT) adds or prunes attention heads based on eigenvectors that Oja and MCA EXIN rules track online. Its convergence proof claims a monotone Lyapunov function, but pruning can raise it; only a net decrease per grow/prune cycle is shown. Its head-count proof removes two eigen-directions per step while the algorithm adds one head. The "head-channel non-identifiability" claim also looks wrong for BERT-base, whose stacked output projection is square and generically invertible. The book does not show that attention is optimal, and its companion *Hierarchical Kernel Transformer* paper shows a multi-scale kernel beating standard attention. Volume II is still to come. Reviewed via the preprints, not the book PDF. [Technical › Deep Learning](Technical#deep-learning)

**SpikingBrain vs Hinton's program.** SpikingBrain converts Qwen2.5 into linear-attention and MoE models with "spiking" activations, trained on non-NVIDIA hardware. Against Hinton's ideas (Forward-Forward, mortal computation, fast weights, event-driven neurons) it captures only the energy side of spikes, which is skipping zeros. Training is ordinary backprop, and spikes are introduced only afterward as quantization. Spike *timing* as information, stochastic firing as regularization, and spike-timing-dependent plasticity are all absent. The genuine lineage link is fast-weight memory, which runs through linear attention.

**Neural operators.** Fourier Neural Operators and the general neural-operator framework learn maps between function spaces, so one trained model works across discretizations of a PDE. This connects naturally to the Navier–Stokes thread above.

**A frontier LLM can read and edit a small network's raw weights, but the headline gains come from removing bugs, not adding skill.**
The model named which game a policy was trained on from its weights alone. It found induction heads without running the network. It also wrote a 1.5M-parameter Go net that beat an equal-sized PPO net trained on 20 million games. The MATH-500 jump came from ablating the direction behind a known looping bug, close to existing directional-ablation methods, and it did not carry over to a model without that bug. The from-scratch networks were reasoned-out rules compiled into weights, much like Tracr done by hand. Spotting sycophancy needed attention patterns, not weights alone. The most useful application may be auditing models for hidden behaviors before deployment. This is a blog post with released logs, not a peer-reviewed paper. [Papers › AI and Machine Learning › Large Language Models](Papers#large-language-models)

**Mechanistic interpretability can find signals that behavioral tests miss, but whether it makes models safer is still mostly untested.**
This survey covers SAEs, circuit discovery with causal checks, probes and training-data attribution. It sorts the field into six research orientations that trade scalability against robustness to deception. It proposes judging explanations on faithfulness, completeness, stability, causal validity and human interpretability, because plausibility alone rewards convincing wrong stories. Its key example is a linear probe catching a planted backdoor at >99% AUROC, which does not show that models can detect deception in general. Reviewed from the abstract and overview, because arXiv rate-limited the full text. [Papers › AI and Machine Learning › Large Language Models](Papers#large-language-models)

**BendTorch's real result is its oracle harness, not its speed.**
Every training step is checked against PyTorch eager, with the same weights and batches and a per-step tolerance. Only PyTorch eager and BendTorch pass all four workloads. Most framework drift traced to small numeric choices: AdamW bias correction done in float32 instead of double, where epsilon sits, float32 loss summation, and silent TF32. Speed: 3–6× slower than PyTorch on large matrix products (no BLAS), faster on tiny models where dispatch dominates, and a weak GPU path. Still open: the author built both the harness and the fixes for the other frameworks, and it is one machine and one run.
[Papers › Deep Learning](Papers#deep-learning)

Sources: [Papers › AI and Machine Learning](Papers#ai-and-machine-learning), [Technical › Deep Learning](Technical#deep-learning).

## LLM Inference Serving

**Disaggregated prefill and decode: the network becomes the product.** Prefill is compute-bound and decode is memory-bandwidth-bound, so modern stacks run them on separate workers. The discussion traced the full path through NVIDIA Dynamo's design, llm-d on Kubernetes, vLLM's NixlConnector and NIXL, and an OCP RoCE reference fabric:
- the KV cache moves from prefill workers to decode workers over the fabric
- routing is cache-aware: requests that share a prefix go to the replica that already holds it

Once that transfer is on the critical path, the fabric decides tail latency, which is the sense in which "the network is the product."

Sources: [Papers › LLM Inference Serving](Papers#llm-inference-serving).

## Linguistics and Scripts

**DNS Bhat's corpus.** All 33 of Bhat's books are catalogued under [DNS Bhat](../kannaDa/dnsbhat/). The deep dives returned repeatedly to his central claim: Kannada grammar has been described through Sanskrit (and later English) categories, which hide its Dravidian structure.

**Ellara Kannada.** Pampa's ಮಾನಸರ್ and the two kinds of "we" in the same line, Bhat's verb counts and the missing auxiliaries, a native Śrī Rudram verse, *Aiṅkuṟunūṟu* 323 in Eke, the dhole/ಕಿರುಬ/ಚಿರತೆ etymologies, the ಎ-ಎಣಿಕೆ maths notation, karate terms, coinage precedence and the pangram each have their own section in [Ellara Kannada Deep Dives](../Reflection/ellara-kannada-deep-dives.md).

**Where did zero's dot come from?** The hypothesis is that abugida scripts already had a visible "nothing in this slot" mark, the Tamil-Brāhmī puḷḷi, before positional zero appears in inscriptions, and that this was the conceptual precondition. Tamil kept additive numerals because it already had a native absence marker. Kannada adopted ೦ late, around the time its virama became consistently visible. The follow-up asked whether the earliest Indosphere zero, a Cambodian inscription, owes more to a Kadamba/Pallava-Grantha line than to Tamil-Brāhmī. See the [illustrated write-up](../kannaDa/eke/zero-speculation-illustrated.html).

**Paternal lineages between South Asia and South China.** He et al.'s large Y-chromosome study finds that modern Indian and South Chinese paternal lines share only a deep FT-M89 trunk (about 52–70 thousand years ago), with no Neolithic or later shared lineages. Rare F lineages persist along coastal (Guangdong) and inland (Yunnan) routes. Shared deep ancestry and recent contact are different claims, and this paper supports only the first.

Sources: [Papers › Linguistics and Languages](Papers#linguistics-and-languages), [Papers › Other](Papers#other).

## Martial Arts

**What the karate sources say between the lines.** Motobu argues about the order in which kata and application are trained. Nagamine shows dissent through curriculum choices under *honne/tatemae*, and *Tales* gives the older masters their full weight. The *hōgen* ban left its mark on kata names, and attested kobudō names show competing Uchinaaguchi sound rules. Each is covered in [Karate › Reading the sources](../karate/50-reading-the-sources).

## Health and Nutrition

**Diet, body composition, exercise metabolism and training.** Each has its own section in [Fitness Deep Dives](../Reflection/fitness-deep-dives.md). These cover published evidence and general training principles only, with no personal measurements:
- [diet, protein and longevity](../Reflection/fitness-deep-dives/ch2): the Harvard cohort papers (Tessier, Glenn, Malik), Fanti's methionine-supplemented longevity diet, Longo's *The Longevity Diet*, and how much protein different goals need
- [body composition and how it is measured](../Reflection/fitness-deep-dives/ch3): creatine without exercise and the DXA water confound, Tromsø visceral-fat reference values, GlasVEGAS, scan hygiene, VO₂max per kilogram
- [sitting, squatting and active rest](../Reflection/fitness-deep-dives/ch4): textile-EMG sitting data and the Hadza
- [lactate and the heart](../Reflection/fitness-deep-dives/ch5): MCT1, necessity versus sufficiency, and what it does and doesn't say about zone training
- [training intensity](../Reflection/fitness-deep-dives/ch6): what "Zone 2" means, lab versus watch thresholds, RER, watch VO₂max
- [interval formats and cross-training](../Reflection/fitness-deep-dives/ch7): the 4×4, hill sprints, REHIT, erg substitutions, critical power, ergs versus resistance training
- [popular sources checked](../Reflection/fitness-deep-dives/ch8)
- [*Outlive* against the papers](../Reflection/fitness-deep-dives/ch9): Attia's book set against the evidence above
- [reading habits](../Reflection/fitness-deep-dives/ch10)

**Other threads.** A systematic review of 29 RCTs on magnesium and serum lipids. [Papers › Other](Papers#other)
