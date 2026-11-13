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

**One operator for all elementary functions, then Kannada names for it.** Odrzywołek shows that eml(x, y) = eˣ − ln y, together with the constant 1, generates every elementary function. It is the continuous analogue of a NAND gate, with grammar S → 1 | eml(S, S). Since eˣ = eml(x, 1), Euler's formula, cos and sin all reduce to trees of one node. The discussion then turned into an Ellara Kannada coinage exercise: a nine-symbol notation with no Latin letters. ಏ stands for exp, ಅ for ln, ಎ = ಏ − ಅ for eml itself, ಇ for the imaginary unit and ತಿ (from ತಿಳಿಯದ, "the unknown") for the variable. π is ಸುತ್ತುಪಾಲು, and the trig functions form a ಪಾಲು ("ratio") family: ನೇರಪಾಲು, ಪಕ್ಕಪಾಲು and ತಾಗುಪಾಲು. ತಾಗುಪಾಲು ("touching ratio") keeps the geometric meaning of *tangent* that the English word has lost.

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

**Pampa's ಮಾನಸರ್ shows that Old Kannada assigns gender by what a word refers to, not by the source word's gender.**
In *Vikramārjuna Vijaya* (9.48, c. 941 CE), the line ನಾಮೆಲ್ಲಂ ಒಂದೆ ಗರುಡಿಯೊಳ್ ಓದಿದ ಮಾನಸರೆವು gives ಮಾನಸ the rational plural -ಅರ್ because it refers to people. That fits Chapter 7 of *nijakku halegannaDa vyAkaraNa entahadu?* (ಲಿಂಗ ಮತ್ತು ವಚನಗಳು): the rational/non-rational split does the work, and the "exceptions" that Keśirāja-style grammars have to explain away come from forcing Sanskrit's three genders onto Kannada. Bhat analyses this exact line in Chapter 11 (ex. ೬ಘ): ಮಾನಸ + ಅರ್ (the subject's gender and number) + ಎವು (the person ending for the speaker together with others). He also quotes it in Chapter 4 (ex. ೧೫ಗ). He glosses ಮಾನಸರ್ as ಮನುಷ್ಯರು, "people", and uses it the same way in ಇಂತೀ ನಾಲ್ವರೆ ಮಾನಸರ್ ("we four people"). That rules out Sanskrit *mānasa* ("mind") and native ಮಾನ + -ಸ as readings. The likeliest source is the Kannada form of Sanskrit *mānuṣa*, "human", but Bhat doesn't say that himself, so check a dictionary before quoting it. ಗರುಡಿ, the martial training hall, is native vocabulary in the same line. [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

**The same line uses both the inclusive and the exclusive "we."**
ನಾಮೆಲ್ಲಂ ("all of us, you included") and ಎಮ್ಮಂ ("us, not you," the oblique of ಆಮ್) appear in one sentence, so the distinction is doing real work in the text rather than just filling a paradigm table. Standard modern Kannada has folded both into ನಾವು. Still open: when the merger happened, traced through datable later texts such as Kumāravyāsa. [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

**The auxiliaries are the missing piece of the *kannaDa sollarime* verb-paradigm work.**
Counted Bhat's way (Vol. 2, §5.1.1), the paradigms for ಮಾಡು, ಇರು and ಇಲ್ಲ are already on the [grammar pages](../kannaDa/grammar/). ಆರ್, ಒಲ್, ಬಲ್, ಬೇಕು, ಬಹುದು and ಆಗು still need the same treatment, as does an account of how compounds like ಮಾಡಲಾರೆ relate to the base verb's count. Earlier claims about these auxiliaries were never checked against the book, so they stay out until they are. [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

**The opening verse of the Śrī Rudram (Namakam) can be prayed in native Kannada.**
Key choices are ಗುಡುಗ ("the thunderer") for Rudra and ಬಾಗುವೆ ("I bow") for the prayer-register verb. For "priest" there is Bhat's own ತಮ್ಮಡಿ, recovered by decoding a garbled OCR entry in his English-to-Kannada word list. Still open: the rest of the Namakam, with every sandhi checked. [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

**Eke can write Sangam Tamil by sound rather than by spelling.**
*Aiṅkuṟunūṟu* 323 (pālai tiṇai) was romanised with stops voiced after nasals and between vowels, sandhi carried across word boundaries, single and double ற kept apart, and ழ written Z/ೞ. In the poem, a man crossing a wasteland speaks to his own heart, and a dhole hunting for its pregnant mate mirrors his journey. Still open: adding it to the Eke examples page as its first Tamil text. [Technical › Writing Systems and Unicode](Technical#writing-systems-and-unicode)

**The Kannada ತೋಳ ("wolf") origin for English "dhole" doesn't hold up well.**
The proposed source has geographic and semantic problems, Tamil doesn't use the word for wolf, and the etymology remains uncertain. The same thread separated colloquial ಚಿಗಟೆ (cheetah) from ಚಿರತೆ (leopard), and left open whether ಚಿರತೆ relates to Sanskrit *citraka* or to a native root meaning "small" or "jump." Also open: whether Sumerian mentions of a "Meluhha dog" bear on any of this. [Papers › Other](Papers#other)

**Where did zero's dot come from?** The hypothesis is that abugida scripts already had a visible "nothing in this slot" mark, the Tamil-Brāhmī puḷḷi, before positional zero appears in inscriptions, and that this was the conceptual precondition. Tamil kept additive numerals because it already had a native absence marker. Kannada adopted ೦ late, around the time its virama became consistently visible. The follow-up asked whether the earliest Indosphere zero, a Cambodian inscription, owes more to a Kadamba/Pallava-Grantha line than to Tamil-Brāhmī. See the [illustrated write-up](../kannaDa/eke/zero-speculation-illustrated.html).

**Paternal lineages between South Asia and South China.** He et al.'s large Y-chromosome study finds that modern Indian and South Chinese paternal lines share only a deep FT-M89 trunk (about 52–70 thousand years ago), with no Neolithic or later shared lineages. Rare F lineages persist along coastal (Guangdong) and inland (Yunnan) routes. Shared deep ancestry and recent contact are different claims, and this paper supports only the first.

Sources: [Papers › Linguistics and Languages](Papers#linguistics-and-languages), [Papers › Other](Papers#other).

## Ellara Kannada: details

The longer working notes behind the Ellara Kannada items above, plus the coinage threads that came from them. Where a choice was revised along the way, the final choice is given and the rejected one is named only when the reason matters.

### Pampa's line, word by word

**Each word of the line can be read off Bhat's analysis without falling back on Sanskrit categories.**

> ನಾಮೆಲ್ಲಂ ಒಂದೆ ಗರುಡಿಯೊಳ್ ಓದಿದ ಮಾನಸರೆವು; ಎಮ್ಮಂ ನಿಮ್ಮಡಿ ಕೆಮ್ಮನೆ ಬೞಲಿಸ
> *nAmellaM onde garuDiyoL Odida mAnasarevu; emmaM nimmaDi kemmane baZalisa*
> "All of us are people who trained in the same garuDi; Your Lordship, do not torment us for nothing."

| Word | Parse | Note |
|------|-------|------|
| ನಾಮೆಲ್ಲಂ | ನಾಮ್ + ಎಲ್ಲಂ | inclusive "we, all of us" |
| ಒಂದೆ ಗರುಡಿಯೊಳ್ | ಒಂದೆ + ಗರುಡಿ + -ಒಳ್ | "in the very same training hall"; ಗರುಡಿ is native |
| ಓದಿದ | ಓದು + past participle | ಓದು in its older sense, "learn, train" |
| ಮಾನಸರೆವು | ಮಾನಸ + -ಅರ್ + -ಎವು | Bhat, Ch. 11: subject gender/number, then the first-person-plural ending |
| ಎಮ್ಮಂ | ಎಮ್ (oblique of ಆಮ್) + -ಅಂ | exclusive "us," the accusative object |
| ನಿಮ್ಮಡಿ | ನಿಮ್ಮ + ಅಡಿ | "your feet," the honorific way of saying "you" |
| ಕೆಮ್ಮನೆ | — | "for nothing, needlessly" |
| ಬೞಲಿಸ | ಬೞಲ್ + causative | "wear out, torment"; the exact negative or prohibitive form is still to be checked against Bhat |

Still open: the exact form of ಬೞಲಿಸ, and a dictionary check of ಮಾನಸ < *mānuṣa*.
→ [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

### Verb paradigms from *kannaDa barahada sollarime*, Vol. 2, §5.1.1

**Bhat's way of counting gives every verb class a fixed shape, and the auxiliaries are the classes that break it.**
His count splits finite forms (ಕೊನೆರೂಪ) from non-finite ones (ನಡುರೂಪ), and splits the finite forms again into indicative (ತಿಳಿವುರೂಪ) and imperative (ಅರಿಕೆರೂಪ). That gives:

| Verb | ತಿಳಿವುರೂಪ | ಅರಿಕೆರೂಪ | ಕೊನೆರೂಪ | ನಡುರೂಪ | Total |
|------|----------:|---------:|--------:|-------:|------:|
| ಮಾಡು (content verb) | 18 | 5 | 23 | 13 | 36 |
| ಇರು (auxiliary) | 27 | 5 | 32 | 10 | 42 |
| ಇಲ್ಲ (negator) | | | | | 5 |

ಇರು alone has three tenses. Its present, ಈಪೊತ್ತು (ಇದ್ದಾನೆ, ಇದ್ದಾಳೆ…), marks a state that holds now, as opposed to ongoing action or a completed past. ಇದೆ and ಇವೆ replace the expected neuter forms, ಇರದ is its only surviving negative participle (the other negative non-finites use ಇಲ್ಲ), and as a vector verb it carries continuation (ಮಾಡುತ್ತಿದ್ದೆ). The auxiliaries build on a content verb's non-finite form: ಮಾಡಲು + ಆರ್ → ಮಾಡಲಾರೆ ("I can't"), ಮಾಡಲು + ಒಲ್ → ಮಾಡಲೊಲ್ಲೆ ("I won't"), ಮಾಡ + ಬಲ್ → ಮಾಡಬಲ್ಲೆ ("I can"), with ಮಾಡಬೇಕು and ಮಾಡಬಹುದು formed the same way. These compounds fall outside ಮಾಡು's 36, and the base form differs from one auxiliary to the next. Still open: per-auxiliary form counts were once drafted from memory rather than read from §5.1.1, so they are left out here until checked.
→ [grammar pages](../kannaDa/grammar/) · [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

### Śrī Rudram, opening verse

**A native rendering works if the meaning is translated rather than the name, and the case endings follow the rational/non-rational split.**

```
ಒಲವಿನ ಗುಡುಗನಿಗೆ ಬಾಗುವೆ ಓಂ |
ಗುಡುಗ, ನಿನ್ನ ಉರಿಮೆಗೆ ಬಾಗುವೆ |
ಕಣೆಗೆ ಅಲ್ಲದೆ ಬಿಲ್ಲಿಗೂ ಬಾಗುವೆ |
ಅದಲ್ಲದೆ ತೋಳಿಗೂ ಬಾಗುವೆ ||

olavina guDuganige bAguve Om |
guDuga, ninna urimege bAguve |
kaNege allade billigU bAguve |
adallade tOLigU bAguve ||
```

| Sanskrit | Native | Why |
|----------|--------|-----|
| रुद्र | ಗುಡುಗ | ಗುಡುಗು "to thunder" + agent -ಅ; the onomatopoeia fits. Also considered: ಕರ್ಗ ("roarer"), ಬಿರುಗ ("the fierce one") |
| नमः | ಬಾಗುವೆ | "I bow," a first-person volitional form rather than the progressive -ತ್ತೇನೆ |
| भगवत् | ಒಲವಿನ | "of grace" |
| मन्यु | ಉರಿಮೆ | ಉರಿ "burn" + abstract -ಮೆ |
| इषु, धनुस्, बाहु | ಕಣೆ, ಬಿಲ್ಲು, ತೋಳು | already native |
| उत | ಅಲ್ಲದೆ / -ಊ | "and also" |

The dative endings follow the noun class: rational nouns take -ನಿ-ಗೆ (ಗುಡುಗನಿಗೆ), vowel-final non-rational nouns take -ಗೆ (ಉರಿಮೆಗೆ, ಕಣೆಗೆ), nouns ending in -ಉ take -ಇಗೆ (ಬಿಲ್ಲಿಗೆ), and plurals take -ಗಳಿಗೆ. Compound junctions follow Book 3 (*kannaDa padagaLa oLaracane*, §5.7). Still open: the remaining anuvākas.
→ [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

### *Aiṅkuṟunūṟu* 323 (Ōtalāntaiyār, pālai)

**Writing a Tamil poem by how it sounds puts its Kannada cognates in plain view.**

```
வள் எயிற்றுச் செந்நாய், வயவுறு பிணவிற்குக்
கள்ளியங் கடத்திடைக் கேழல் பார்க்கும்,
வெஞ்சுரக் கவலை நீந்தி
வந்த நெஞ்சம், நீ நயந்தோள் பண்பே.

vaL eyittRu^c cennAy, vayavuRu^ piNaviRku^k
kaLLiyan gaDattiDayk kEZal pArkkum,
venjurak kavalay nIndi
vanda nenjam, nI nayandOL paNbE.

ವಳ್ ಎಯಿತ್ತ್ಱುಚ್ ಚೆನ್ನಾಯ್, ವಯವುಱು ಪಿಣವಿಱ್ಕುಕ್
ಕಳ್ಳಿಯಂ ಗಡತ್ತಿಡಯ್ಕ್ ಕೇೞಲ್ ಪಾರ್ಕ್ಕುಮ್,
ವೆಂಜುರಕ್ ಕವಲಯ್ ನೀಂದಿ
ವಂದ ನೆಂಜಮ್, ನೀ ನಯಂದೋಳ್ ಪಣ್ಬೇ.
```

"O heart, you swam across the forking paths of this burning wasteland, where the sharp-toothed red dog watches for a boar to feed its pregnant, craving mate. What carried you through is the goodness of the one you love." The dhole's hunt mirrors the man's journey, and the poem credits her *paNbu*, not his courage.

How the transliteration was done:
- Stops are voiced after nasals (nIndi, venjurak, paNbE) and between vowels (gaDattiDay), and stay voiceless at the start of a word and when doubled.
- Sandhi carries across word boundaries (kaLLiyan gaDa…).
- A single ற is written R/ಱ, while double ற்ற, pronounced [tːr], is written ttR/ತ್ತ್ಱ.
- ழ is written Z/ೞ, and ஐ is written ay.
- Word-final ம் is written as a full m.
- The short unrounded *kuṟṟiyalukaram* is marked u^ in Eke but left as plain ು in the Kannada script.

Kannada cognates: ಕೆನ್ನಾಯಿ (dhole), ಕಳ್ಳಿ, ಕವಲು (fork), Old Kannada ನೀಂದು (swim). Still open: whether to show u^ in the Kannada script as ಉ್.
→ [Technical › Writing Systems and Unicode](Technical#writing-systems-and-unicode)

### Dhole, hyena, leopard, cheetah

**The animal names hold together better as sibling formations than as borrowings from one another.**
The Meluhha "dog" is the animal that a Ur III king, Ibbi-Sin, received as tribute through Marhashi. Its qualifier sign can be read *dar* ("red"), which fits a dhole, or *gun3* ("speckled"), which points to a spotted cat, and Sumerian *ur* covered large carnivores in general. A Dravidian *cem-nāy* ("red dog," like Tamil cennAy and Kannada ಕೆನ್ನಾಯಿ) would match the *dar* reading, but that rests on two unproven assumptions: that the animal was a dhole, and that Harappans spoke Dravidian. ಕಿರುಬ and ಚಿರತೆ look like siblings built on the two forms of the root for "small," ಕಿಱು- and ಚಿಱು-, compare Tamil ciRuttay. Many dialects use ಕಿರುಬ for the leopard and ಕತ್ತೆಕಿರುಬ ("donkey-kiruba") for the hyena. Colloquial ಚಿಗಟೆ is the cheetah. Still open: the standard edition of the Ibbi-Sin text (Frayne 1997, E3/2.1.5) hasn't been checked, and the "jump" root for ಚಿರತೆ needs dialect evidence.
→ [Papers › Other](Papers#other)

### ಎ-ಎಣಿಕೆ: a native notation for elementary functions

**The run of vowels ಏ → ಎ → ಇ follows the maths: the full operator, then the derived one, then the imaginary.**

| Symbol | From | Meaning |
|--------|------|---------|
| ಏ | — | exp, the full operator |
| ಅ | — | ln |
| ಎ | ಏ − ಅ | eml, the derived operator |
| ಇ | ಇಲ್ಲದ ("not there") | imaginary unit |
| ತಿ | ತಿರುವು ("a turn") | angle θ; the rotation sense was preferred over ಮೂಲೆ ("corner") |
| ಗೊ | ಗೊತ್ತಿಲ್ಲದ ("not known") | unknown x |
| ನೇ, ಪ, ತಾ, ಸು | ನೇರಪಾಲು, ಪಕ್ಕಪಾಲು, ತಾಗುಪಾಲು, ಸುತ್ತುಪಾಲು | sin, cos, tan, π |

Euler's formula becomes ಏ^(ಇ·ತಿ) = ಪ(ತಿ) + ಇ·ನೇ(ತಿ), and with ತಿ = ಸು, ಏ^(ಇ·ಸು) + ೧ = ೦. ನೇರ was chosen over ಎದುರು for sin so the ಎ- prefix stays reserved for the operator. For tan, ತಾಗುಪಾಲು ("touching ratio," from the circle) beat ಓರೆಪಾಲು ("slope ratio," from the triangle). Still open: the Mathematics summary above derives ತಿ from ತಿಳಿಯದ and uses it for the variable, while this session used ತಿ for the angle and ಗೊ for the unknown. Pick one.
→ [Papers › Analysis and Linear Algebra](Papers#analysis-and-linear-algebra)

### Karate and kobudō terms

**Weapon names come from shape and stance names from the body, so a few native roots go a long way.**
The building blocks are ಕಾಳಗ (fight), ಕೋಲ್ (stick), ಇರ್ಪು (stance, the gloss for *dachi*), ಗುದ್ದು (punch), ಒದೆ (kick) and ತಡೆ (block).

| Term | Native | Literally |
|------|--------|-----------|
| karate | ಬರಿಗೈಕಾಳಗ | empty-hand fight |
| kata | ನಡೆಅಚ್ಚು | movement mould |
| sai | ಮುರ್ಮೊನೆ | three points |
| nunchaku | ಕೊಂಡಿಕೋಲ್ | linked stick |
| sansetsukon | ಮುರ್ಗಣ್ಣುಕೋಲ್ | three-section stick |
| tonfa | ಅಡ್ಡಹಿಡಿಕೋಲ್ | cross-handled stick |
| kama, eku | ಕುಡುಗೋಲು, ಹುಟ್ಟು | sickle, oar (existing words) |
| shizentai, nekoashi, jigotai dachi | ತನ್ನಿರ್ಪು, ಬೆಕ್ಕುಕಾಲಿರ್ಪು, ಅಗಲಕಾಲಿರ್ಪು | natural, cat-foot, wide-leg stance |
| chūdan tsuki, mae geri, shutō uke | ನಡುಮಟ್ಟ ಗುದ್ದು, ಮುನ್ನೊದೆ, ಕೈಯಲಗು ತಡೆ | mid-level punch, front kick, hand-blade block |
| Wankan, Gojūshiho, Passai | ಅರಸಮುಡಿ, ಅಯ್ವತ್ತುನಾಲ್ ಹೆಜ್ಜೆ, ತಡೆದಾಟುಕಾಳಗ | king's crown, fifty-four steps, breaking-through fight |

Kata in a series take ordinal steps: ಅಡ್ಡಕಾಳಗ ಒರ್ಮೆಟ್ಟಿಲು (Naihanchi shodan), ತಣಿವುಕಾಳಗ ಮುರ್ಮೆಟ್ಟಿಲು (Pinan sandan). Still open: whether to add a native column to the [terminology page](../karate/31-terminology).
→ [Technical › Martial Arts](Technical#martial-arts)

### How coinages are chosen

**Bhat's own attested words come first, then existing idioms, and fresh coinages only last.**
The working order is to coin independently, then check against Bhat's lists and Kannada Wiktionary, and keep the attested form whenever there is one. Latin legal phrases made the case: the attested ಮುಯ್ಯಿಗೆ ಮುಯ್ಯಿ / ಕೊಡುಕೊಳೆ (quid pro quo), ಬಿಟ್ಟಿಕೆಲಸ (pro bono), ಮಯ್ದೋರಿಸಿ (habeas corpus), ಮೊದಲ ನೋಟ (prima facie), ಅದದಕ್ಕೆ (ad hoc) and ಎಂದಿನ ಪಾಡು (status quo) all beat the fresh compounds. Tadbhava forms with retroflexes are acceptable. Words often assumed to be Sanskrit, such as ತಂಡ and ಕೂಟ, are Dravidian, while ಸಂಜೆ is a tadbhava, ದಿನ gives way to ನಾಳು, and ಏಳ್ನಾಳು replaces ವಾರ for "week." Electronics terms share the prefix ಮಿನ್ನು-: ಮಿನ್ನುಕ (computer), ಮಿನ್ನವಿರು (software). Still open: Bhat's word for "authority."
→ [Technical › Dravidian and Kannada Linguistics](Technical#dravidian-and-kannada-linguistics)

### Ellara Kannada pangram

**One four-line verse aims to cover the whole ellara-kannaDa sound inventory, with no aspirates, ಷ or ಱ.**
The verse tells of a guard who shoots at a monkey; the monkey stumbles at the town festival and hits Shiva's bull. Sanskrit loans were swapped out to keep it native and to fill gaps: ಕಣೆ replaced ಬಾಣ, ಹೊತ್ತಿನಲ್ಲಿ replaced ದಿನ, and ಮಂಗನಿಗೆ supplied the ಂಗ cluster. Coverage was checked with a script that keeps independent vowels separate from vowel signs. Still open: ಈ, ಐ and ಔ (ಙ and ಞ set aside), and line 3 runs about 21–22 aksharas against a target of about 17. The earlier version is on the [Eke examples page](../kannaDa/eke/examples.html).
→ [Technical › Writing Systems and Unicode](Technical#writing-systems-and-unicode)

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
