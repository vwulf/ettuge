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

**One operator for all elementary functions, then Kannada names for it.** Odrzywołek shows that eml(x, y) = eˣ − ln y, together with the constant 1, generates every elementary function. It is the continuous analogue of a NAND gate, with grammar S → 1 | eml(S, S). Since eˣ = eml(x, 1), Euler's formula, cos and sin all reduce to trees of one node. The discussion then turned into an Ellara Kannada coinage exercise: a nine-symbol notation with no Latin letters. ಎ stands for eml, ಇ for the imaginary unit, ಅ for ln and ತಿ (from ತಿಳಿಯದ, "the unknown") for the variable. π is ಸುತ್ತುಪಾಲು, and the trig functions form a ಪಾಲು ("ratio") family: ನೇರಪಾಲು, ಪಕ್ಕಪಾಲು and ತಾಗುಪಾಲು. ತಾಗುಪಾಲು ("touching ratio") keeps the geometric meaning of *tangent* that the English word has lost.

**Chowla's cosine problem, solved twice at once.** Jin, Milojević, Tomon and Zhang go through spectral graph theory: small eigenvalues of Cayley graphs give large cuts, and MaxCut then bounds the minima of cosine sums. Bedert proved polynomial bounds independently. The two proofs appeared within days of each other, by unrelated methods.

**Fractals, measure and Kakeya.** Falconer's *Geometry of Fractal Sets* (Hausdorff dimension, projections, Kakeya-type sets) and Tao's measure-theory text supply the background for recent results in geometric measure theory and PDE. One was the contested claim of finite-time blowup for the forced Navier–Stokes equations. Its comparison with earlier 3D Euler blowup work turned on whether the forced case is the Millennium problem at all.

Sources: [Papers › Mathematics](Papers#mathematics), [Technical › Topology and Geometry](Technical#topology-and-geometry).

## AI and Machine Learning

**A mathematical theory of the transformer.** Cirrincione's draft (Vol. I, built from seven arXiv preprints, including the *Hierarchical Kernel Transformer* paper) treats the transformer as an object of analysis: its foundations, rationality, and an incremental variant.

**SpikingBrain vs Hinton's program.** SpikingBrain converts Qwen2.5 into linear-attention and MoE models with "spiking" activations, trained on non-NVIDIA hardware. Against Hinton's ideas (Forward-Forward, mortal computation, fast weights, event-driven neurons) it captures only the energy side of spikes, which is skipping zeros. Training is ordinary backprop, and spikes are introduced only afterward as quantization. Spike *timing* as information, stochastic firing as regularization, and spike-timing-dependent plasticity are all absent. The genuine lineage link is fast-weight memory, which runs through linear attention.

**Neural operators.** Fourier Neural Operators and the general neural-operator framework learn maps between function spaces, so one trained model works across discretizations of a PDE. This connects naturally to the Navier–Stokes thread above.

**Programs in weight space.** *Sparks of Weight-Space Programming* reports frontier LLMs reading a small network's raw weights, inferring what it computes, and editing it directly. MATH-500 rose from 7.9% to 48.1% after changing 0.016% of the weights. Read alongside the mechanistic-interpretability survey (abstract and overview only), it frames interpretability as something a model might eventually do *to* another model.

Sources: [Papers › AI and Machine Learning](Papers#ai-and-machine-learning), [Technical › Deep Learning](Technical#deep-learning).

## LLM Inference Serving

**Disaggregated prefill and decode: the network becomes the product.** Prefill is compute-bound and decode is memory-bandwidth-bound, so modern stacks run them on separate workers. The discussion traced the full path through NVIDIA Dynamo's design, llm-d on Kubernetes, vLLM's NixlConnector and NIXL, and an OCP RoCE reference fabric:
- the KV cache moves from prefill workers to decode workers over the fabric
- routing is cache-aware: requests that share a prefix go to the replica that already holds it

Once that transfer is on the critical path, the fabric decides tail latency, which is the sense in which "the network is the product."

Sources: [Papers › LLM Inference Serving](Papers#llm-inference-serving).

## Linguistics and Scripts

**DNS Bhat's corpus.** All 33 of Bhat's books are catalogued under [DNS Bhat](../kannaDa/dnsbhat/). The deep dives returned repeatedly to his central claim: Kannada grammar has been described through Sanskrit (and later English) categories, which hide its Dravidian structure. A worked example comes from Book 14, *ನಿಜಕ್ಕೂ ಹಳೆಗನ್ನಡ ವ್ಯಾಕರಣ ಎಂತಹದು?*, applied to a Kumaravyasa verse. Old Kannada distinguishes inclusive ನಾಮ್ from exclusive ಎಮ್ "we", and the classical grammarians, working from a Sanskrit template, never described the distinction. The verse also preserves ೞ, the Dravidian sound shared with Tamil ழ.

**Where did zero's dot come from?** The hypothesis is that abugida scripts already had a visible "nothing in this slot" mark, the Tamil-Brāhmī puḷḷi, before positional zero appears in inscriptions, and that this was the conceptual precondition. Tamil kept additive numerals because it already had a native absence marker. Kannada adopted ೦ late, around the time its virama became consistently visible. The follow-up asked whether the earliest Indosphere zero, a Cambodian inscription, owes more to a Kadamba/Pallava-Grantha line than to Tamil-Brāhmī. See the [illustrated write-up](../kannaDa/eke/zero-speculation-illustrated.html).

**Paternal lineages between South Asia and South China.** He et al.'s large Y-chromosome study finds that modern Indian and South Chinese paternal lines share only a deep FT-M89 trunk (about 52–70 thousand years ago), with no Neolithic or later shared lineages. Rare F lineages persist along coastal (Guangdong) and inland (Yunnan) routes. Shared deep ancestry and recent contact are different claims, and this paper supports only the first.

Sources: [Papers › Linguistics and Languages](Papers#linguistics-and-languages), [Papers › Other](Papers#other).

## Martial Arts

**Reading Nagamine between the lines.** Read alongside Motobu's *My Art of Karate*, Nagamine's *Essence of Okinawan Karate-Do* supports a *honne/tatemae* reading. Writing under postwar political constraints, Nagamine encoded disagreement with the Itosu school-karate trajectory through curriculum rather than argument: keeping Motobu's Naihanchi, citing Motobu's approval of yakusoku kumite, and retaining the full Tomari-te stream.

**Language policy left fingerprints in kata names.** Under the ban on Okinawan in schools, kata taught in the school system acquired Sino-Japanese kanji names, such as Gōjūshiho (五十四歩). Kata passed on informally kept katakana names that point to non-Japanese origins. Uchinaaguchi sound correspondences (o→u, e→i, ki→chi, h→f before a, and more) make many older names legible again. One example: *Shuri* already means castle, so *Shuri-jō* is a cross-language tautology. More in [Karate](../karate/index.md).

## Health and Nutrition

The evidence discussed, without personal data:

- **Protein source matters more than protein amount** for cardiometabolic risk. In large US cohorts, a higher plant-to-animal protein ratio tracked with lower coronary risk, and replacing animal with vegetable protein tracked with lower type 2 diabetes risk.
- **Dietary patterns and healthy aging.** Over about 30 years, every healthy pattern helped, and the AHEI was strongest.
- **Creatine in middle and older age.** It increased lean mass and strength even without exercise, and more when combined with training and diet.
- **Protein restriction with methionine added back** (Longo lab) raised growth hormone, GLP-1 and FGF21 and reduced frailty in that model.
- **Sitting physiology.** Hadza squatting is "active rest". Textile EMG shows leg-muscle activity fading during long sitting, with about 25 minutes as a possible tipping point.
- **Population differences.** In GlasVEGAS, similar weight gain produced worse metabolic changes in South Asian men than in white European men. This is a reason to read DXA visceral-fat values against population reference ranges.
- **Other threads:** magnesium and serum lipids (a systematic review of 29 RCTs), and MCT1-mediated lactate import as the heart's backup fuel route.

Sources: [Papers › Health and Nutrition](Papers#health-and-nutrition), [Papers › Other](Papers#other).
