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

**Complexity, number theory and the Millennium problems.** The Unique Games proof, the ETH refutation claim, Chowla and MaxCut, the quasi-Riemann results, Navier–Stokes and Yang–Mills each have their own section in [Math Deep Dives](../Reflection/math-deep-dives.md).

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

These summaries cover only the published evidence and include no personal measurements.

**Plant-heavy diets with some animal food came out best for healthy aging, and the strictly plant-based index came out worst.**
Tessier et al. scored eight dietary-pattern indices against a composite "healthy aging" outcome: reaching 70 free of major chronic disease, with cognitive, physical and mental health intact. Every healthy pattern helped. The AHEI was strongest, and the healthful plant-based index (hPDI), which penalises all animal foods, was weakest. That result is the one popular summaries tend to leave out. The data are self-reported food-frequency questionnaires from US health professionals, so the findings are associations. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**The plant-to-animal protein benefit for heart disease is a substitution effect, mostly from replacing red and processed meat.**
In Glenn et al., the highest plant-to-animal protein ratio was associated with about 19% lower cardiovascular risk and about 27% lower coronary risk. Because the exposure is a ratio, the effect depends on which animal protein gets displaced, which is why dairy and fish can look neutral or positive in other analyses. The cohort median moved only from roughly 1:3 to 1:2, so even the top group ate more animal than plant protein. The editorial that ran with it (Mariotti) is still unread. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**Animal protein tracks higher type 2 diabetes risk, but the headline 23% is the result of a swap, not of cutting back.**
Malik et al. found modestly higher diabetes risk with more animal protein and slightly lower risk with more vegetable protein. Swapping 5% of energy from animal to vegetable protein was associated with about 23% lower risk. That figure is often quoted as a main effect when it is a substitution result. This paper uses the same Nurses' Health Study and Health Professionals cohorts, and largely the same authors, as Tessier and Glenn, so the three are one research programme rather than three independent confirmations. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**Adding methionine back to a low-protein longevity diet targets frailty, not lifespan.**
Fanti et al. (Longo lab) fed aged, genetically diverse mice a low-protein, plant-based diet with methionine added. Fat mass and frailty fell with no loss of lean mass, IGF-1 dropped, and growth hormone, GLP-1 and FGF21 rose. FGF21 was required for the fat-loss and insulin effects. Maximum lifespan did not change: lifespan and frailty respond to protein along different curves, and methionine is tuned against the frailty curve. The human data are cross-sectional only, the authors disclose patents and a commercial interest, and a human trial is the stated next step. Longo's book *The Longevity Diet* gives the prescriptive version. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**Creatine raised lean mass and strength without exercise, but part of the lean-mass gain is probably water.**
In the Texas A&M trial (Chun, Kreider et al.), adults aged 45–65 took 10 g/day of creatine or placebo for 12 weeks. Lean mass rose about 1 kg even in people doing no exercise, and strength rose too. Creatine pulls water into muscle and DXA counts that water as lean tissue, so the strength gains are the more convincing result. Two open questions: the exercise arms were self-selected rather than randomised, and an earlier two-year trial in older women found no benefit without resistance training. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**Leg-muscle activity fades within minutes of sitting down, and roughly 25 minutes may be a tipping point.**
Brakenridge et al. measured thigh-muscle activity in real-world sitting with EMG sensors built into shorts. During continuous sitting, activity decays roughly as a power law: it is present about 10% of the time after ~9 minutes and about 1% after ~26 minutes. People whose sitting bouts were usually under 25 minutes had about 50% more muscle activity per hour of sitting. The study is small (84 people) and observational, and "break every 25 minutes" is an extrapolation, not a tested intervention. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**How you rest matters: squatting and kneeling keep the leg muscles working, and a chair does not.**
Raichlen et al. found that Hadza hunter-gatherers rest about as many hours a day as office workers, but mostly squatting, kneeling or sitting on the ground. These postures keep the postural muscles lightly active. The authors' "inactivity mismatch" hypothesis says the harm comes from prolonged muscular inactivity, not from rest as such, which is the same mechanism Brakenridge measures. No one has yet tied squat-resting directly to metabolic outcomes. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**DXA visceral-fat readings only mean something against reference values, and those depend on the population and the device.**
The Tromsø Study gives age- and sex-specific reference values for DXA visceral fat in adults over 40. Each age band has its own median and metabolic-syndrome threshold, and the bands are wide enough that one reading can sit in a different place depending on which band it's compared with. The standard visceral ratio divides by abdominal fat, not total body fat, so the two kinds of percentage can't be compared. The values come from one European cohort on one scanner type, so the trend across a person's own scans tells you more than a single figure. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**At the same weight gain, South Asian men stored more visceral and ectopic fat and lost far more insulin sensitivity than white European men.**
In GlasVEGAS (McLaren et al.), matched men were overfed to about a 4.5 kg gain. European men put roughly three times more of it into lean tissue. Insulin sensitivity fell about 38% in the South Asian men versus about 7% in the Europeans, consistent with limited room to expand subcutaneous fat, so the excess spills over into the viscera and liver. "More visceral fat at the same BMI" is well established and is why Asian BMI and waist cut-offs are lower. "More of each added kilogram goes to visceral fat" is supported, but exact coefficients are not pinned down. Read via write-ups, not the full paper. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**The heart burns lactate inside its mitochondria, but the paper shows that the pathway is needed, not that more lactate helps.**
Cluntun et al. show that in mouse heart muscle, the transporter MCT1 imports lactate into mitochondria, where LDHB oxidises it. Glucose oxidation in the cytosol can run at the same time, whereas in most tissues the two fuels compete. Without MCT1, hearts failed to adapt to pressure overload or ischaemia. Knockout mice nonetheless had normal heart function and treadmill capacity, because the pyruvate carrier covers for MCT1 at baseline. The paper has no sufficiency test (no overexpression, lactate supplementation or training), so it does not show that exercise or lactate exposure strengthens the heart. For lactate as a training signal in skeletal muscle, it points to Zhang et al. (*Science Advances*, 2024), still unread. [Papers › Health and Nutrition](Papers#health-and-nutrition)

**Other threads.** A systematic review of 29 RCTs on magnesium and serum lipids. [Papers › Other](Papers#other)
