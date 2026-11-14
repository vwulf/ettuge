---
title: AI Deep Dives
created: 2026-11-13
updated: 2026-11-14
source: deep-dive reading sessions on AI/ML papers, books and posts (Oct–Nov 2026)
---

<a id="ch1"></a>
# AI Deep Dives

> Created: 2026-11-13 · Covers Oct–Nov 2026

These notes come from close readings of machine-learning books, papers and blog posts. Most were weeks old when read. Each entry states the claim, how it works, and what is still open. Where only an abstract, an overview or companion preprints were read, the entry says so. Several sources are blog posts or unrefereed preprints, so treat their numbers as the authors' own.

**Related pages on this site**
- [Deep Dives](https://vwulf.github.io/ettuge/Deep-Dives/): the index of all deep dives, across topics.
- [Papers › AI and Machine Learning](https://vwulf.github.io/ettuge/Books/Papers#ai-and-machine-learning) and [Technical › Deep Learning](https://vwulf.github.io/ettuge/Books/Technical#deep-learning): the 🔍 catalog entries for everything discussed here.
- [Effects and LLM Systems](https://vwulf.github.io/ettuge/FP/bucket-effects-llm): λ-RLM, RLM, Context LMs, DSPy as effects, OpenClaw-RL and typed decision models, seen from functional programming.
- [Decision Points as Effects](https://vwulf.github.io/ettuge/FP/decision-points-as-effects): the rules → decision model → reasoning model cascade, with measured latencies.
- [Algorithms, Functionally](https://vwulf.github.io/ettuge/FP/bucket-algorithms) and [Algebra and Categories](https://vwulf.github.io/ettuge/FP/bucket-algebra-categories): recursion schemes, applicatives and categorical accounts of attention.
- [Math Deep Dives › Millennium problems](https://vwulf.github.io/ettuge/Deep-Dives/math/ch4): Navier–Stokes, which neural operators (chapter 5) also target.
- [Machine Learning & AI](https://vwulf.github.io/ettuge/Reflection/machine-learning-ai/ch1): older links and notes on the same field.

**Contents**
1. [Transformer theory](ch1): Cirrincione's *Mathematical Theory of the Transformer*, and what "optimal" would mean
2. [Attention as an algorithm](ch2): lookup, joins, semirings, DP and RASP
3. [Compositional structure](ch3): an MDL definition, and where rose trees fit
4. [Networks as programs](ch4): mechanistic interpretability and weight-space programming
5. [Architecture](ch5): eight architectural ideas, SpikingBrain, neural operators and what changed since FNO
6. [Training at scale](ch6): nine systems techniques, how they compose, and BendTorch
7. [Serving and judging](ch7): disaggregated inference, decision models, evals
8. [Themes across the deep dives](ch8): including Fourier analysis as a recurring tool

---

## 1. Transformer theory

**Cirrincione's *Mathematical Theory of the Transformer, Vol. I* is a proof-first account of the architecture. Its positional-encoding results hold up better than its claims about self-growing architectures.**
[Technical › Deep Learning](https://vwulf.github.io/ettuge/Books/Technical#deep-learning)

Giansalvo Cirrincione's pre-publication draft (Zenodo record 20199413, v1.0 posted May 15, 2026, headed for MIT Press) is the first of two volumes. It treats positional encodings, layer normalisation, rank dynamics and attention geometry, and builds toward the author's Incremental Transformer (INCRT). Any claim without a proof is labelled a conjecture. The book draws together seven of the author's 2025–26 arXiv preprints. Volume II will cover generation and self-organising architectures.

The book PDF couldn't be read in the session: it fetched as raw binary, and the sandbox couldn't reach Zenodo. The review below is of the preprints. The book, or its newer Zenodo version, may already fix some of these points. The linear-algebra check on head-channel identifiability was done independently. The other gaps come from a model-assisted read of the PDFs. **[→ machine-learning-ai]**

---

**INCRT grows and prunes attention heads from an energy criterion. Both of its theorems have gaps.**
[INCRT, arXiv:2604.10703](https://arxiv.org/abs/2604.10703)

- **How it works.** Each layer tracks a residual matrix: roughly, the symmetrised token Gram matrix pushed through the mean antisymmetric component of the existing heads, projected onto directions no head yet captures. Two online eigenvector trackers follow its top and bottom eigenvectors, one with Oja's rule and one with MCA EXIN.
- **Growing and pruning.** A head is added when the top eigenvalue passes a threshold θ_w (by default 0.4 of the initial residual energy) and there is a direction worth suppressing. A head is pruned when its captured energy stays below about 0.05·θ_w.
- **Claimed theorems.** (1) Convergence to a configuration that is minimal and sufficient, via a Lyapunov argument. (2) A head-count bound of about κ²·log(initial energy / θ_w).
- **Gaps.** The Lyapunov function is said to be monotone, but a prune step can raise it. Only a net decrease per grow/prune cycle is actually shown. The bound's proof removes two eigen-directions per step, while the algorithm adds one head per step.
- **Scope.** "Minimal and sufficient" is relative to the chosen θ_w. The paper says itself that this implies nothing about accuracy or generalisation. **[→ machine-learning-ai]**

---

**Rank-neutrality of layer norm is right up to a missing hypothesis.**
[Rank, Head-Channel Non-Identifiability, and Symmetry Breaking, arXiv:2604.23681](https://arxiv.org/abs/2604.23681)

The claim is that layer normalisation preserves the affine rank of the token set, meaning the dimension of its affine hull. The proof has three steps: centering, per-row scaling, then the γ/β map, which is invertible when every γ ≠ 0. The scaling step needs both σ and the all-ones vector **1** to lie outside the column space of the centered tokens. The paper appears to state only the σ condition. Without the second condition, affine rank can rise by one. That is a fix to the hypothesis, not a broken result. **[→ machine-learning-ai]**

---

**"Head-channel non-identifiability" is likely wrong for BERT-base, and with it the stated motivation for PG-OP.**

The paper argues that once the output projection sums the heads, each head's contribution can't be recovered. But that sum is just the concatenated head outputs multiplied by the stacked output projection. In BERT-base that projection is a square 768×768 matrix, invertible in general, so a fixed linear map recovers each head's contribution exactly. The proposed fix, the Position-Gated Output Projection (PG-OP), adds per-token scalar gates. Those gates don't change the recoverability argument either way. Its parameter overhead also looks undercounted: closer to 3% than the stated 1.6% once the positional term is included. The other architectural proposal, Multi-Head Bilinear Gating (MHB-G), wasn't examined in depth. **[→ machine-learning-ai]**

---

**The positional-encoding results are the book's strongest part.**
[On the Geometry of Positional Encodings in Transformers, arXiv:2604.05217](https://arxiv.org/abs/2604.05217)

- **Necessity.** Without positional information, tasks that depend on word order are impossible.
- **Positional Separation Theorem.** At any global minimum, distinct positions get distinct vectors. This is a conditional result.
- **MDS–Hellinger construction.** Classical multidimensional scaling on Hellinger distances between positional distributions gives a best-approximation encoding, scored by MDS "stress". On that score, ALiBi does much better than sinusoidal encodings or RoPE. **[→ machine-learning-ai]**

---

**Nothing in the book shows that attention is optimal. Its own companion paper argues the opposite.**
[Hierarchical Kernel Transformer, arXiv:2604.08829](https://arxiv.org/abs/2604.08829)

Each "optimal" result holds only inside a fixed frame. The MDS–Hellinger encoding is optimal *positional input* under its criterion. INCRT is minimal relative to θ_w. The necessity and separation theorems say what a Transformer needs, not that it beats alternatives. The *Hierarchical Kernel Transformer* paper treats standard single-head attention as a special case of a richer multi-scale kernel mechanism. The richer mechanism wins on ListOps, sequential CIFAR and character-level IMDB.

A real optimality theorem would need the form "for task class X under budget Y, no architecture does better than attention." Results in the wider literature tend to cut the other way:
- circuit-complexity limits on fixed-depth Transformers
- difficulty with tasks such as parity
- conditional lower bounds showing that exact attention can't easily beat quadratic cost

The fair reading is that the monograph is a theory of the Transformer, not a proof that the Transformer is the answer. **[→ machine-learning-ai]**

---

<a id="ch2"></a>
## 2. Attention as an algorithm

**Attention can't be an algorithmic paradigm like dynamic programming. It is one operation, and DP is a way of structuring a whole computation.**
[Algorithms, Functionally](https://vwulf.github.io/ettuge/FP/bucket-algorithms)

Two corrections first. Attention isn't a technique for *optimizing* networks; gradient descent is. And attention isn't proven optimal (chapter 1).

- **Attention is a soft dictionary lookup.** A query is compared with every key, and the result is a weighted average of the values. As the softmax temperature goes to zero it becomes a hard lookup: argmax, a hash join, a content-addressable memory read. That is a primitive, not a design strategy.
- **DP is a recursion scheme.** It exploits optimal substructure and overlapping subproblems, and gives exact answers that can be proved correct. In recursion-scheme terms it is a hylomorphism with memoization. Attention has no such guarantee. Its power comes from *learned* Q/K/V, not from structure it exploits.
- **They meet in semirings.** A Bellman–Ford relaxation, `d[v] = min_u (d[u] + w(u,v))`, is "attend over predecessors" in the tropical (min, +) semiring. Softmax is a smoothed max, so attention is roughly one soft, learned DP step over the ordinary (+, ×) semiring. That is why neural algorithmic reasoning work (Veličković; Xu et al., *What Can Neural Networks Reason About?*) finds that GNNs and attention align with DP and learn it well.
- **What's missing is the recursion.** A Transformer applies a fixed number of these steps, which puts it in a shallow circuit class (TC⁰). It can't run DP to convergence on arbitrary inputs without chain of thought or a looped/recurrent Transformer. Softmax also blurs as inputs grow: Veličković's "softmax is not enough" shows attention can't stay sharp over long sequences, which an exact algorithm needs.

In short, attention is a smoothed, learnable version of the *inner step* of many algorithms (lookup, relaxation, message passing). DP is the *outer loop* that guarantees correctness. **[→ machine-learning-ai; cross-link → algorithms-data-structures]**

---

**One attention head is a select-and-aggregate, and the temperature sets how strict "select" is.**

| Temperature τ | Selection | Classical equivalent |
|---|---|---|
| → 0, one match | the argmax key | dictionary lookup |
| → 0, ties | every key that satisfies a predicate | equi-join + `GROUP BY q` + `AVG` |
| finite | weighted by similarity | kernel smoothing, a "soft join" |
| → ∞ | every key equally | global mean / reduce |

In SQL, one head is roughly `SELECT q.id, AVG(k.v) FROM Q JOIN K ON pred(q, k) GROUP BY q.id`. Two caveats:
- **It's always a nested-loop join.** Attention scores every query–key pair, which is where the O(n²) comes from. A real hash join only touches matching buckets. LSH attention (Reformer) and other sparse schemes approximate that.
- **Finite τ is a weighted join.** It lines up with database *provenance semirings*. Change the semiring and you get counting, probabilistic or tropical joins. The tropical case is the DP-relaxation link above. **[→ machine-learning-ai; cross-link → data-engineering]**

---

**RASP turns the τ → 0 case into a programming language, and Tracr compiles it into real weights.**
[Algebra and Categories](https://vwulf.github.io/ettuge/FP/bucket-algebra-categories)

RASP (Weiss, Goldberg and Yahav, *Thinking Like Transformers*, 2021) has these primitives:
- `tokens`, `indices`: the input sequences
- `map`: an elementwise function, which is what the MLP layers do
- `select(keys, queries, pred)`: builds a boolean selector matrix
- `aggregate(selector, values)`: averages the selected values
- `selector_width(selector)`: counts the matches

Reversing a sequence:
```
length  = selector_width(select(tokens, tokens, TRUE))
flip    = select(indices, length - indices - 1, ==)
reverse = aggregate(flip, tokens)
```
A histogram is `selector_width(select(tokens, tokens, ==))`. Each chained select/aggregate costs about one layer, so a RASP program's depth bounds the layers it needs. DeepMind's Tracr (2023) compiles RASP programs into Transformer weights.

As a technique, this gives a way to reason about what a fixed-depth Transformer can express. Follow-up work (Zhou et al. on RASP-expressible tasks and length generalization; Sanford et al. on Transformers and massively parallel computation) ties RASP expressibility to which tasks Transformers actually generalize on, and links attention layers to MPC rounds. Tracr-style compilation comes back in chapter 4, where a frontier model writes networks by hand. **[→ machine-learning-ai; cross-link → scala-functional-programming]**

---

<a id="ch3"></a>
## 3. Compositional structure

**Compositional structure can be defined as the extra description a whole's model needs beyond its parts' models.**
[Papers › Foundations](https://vwulf.github.io/ettuge/Books/Papers#foundations) · [arXiv:2610.20922](https://arxiv.org/abs/2610.20922)

*Defining and Generating Compositional Structure* (Elmoznino, Kasetty, Agüera y Arcas, Bengio and Lajoie; Mila, Google, LawZero; October 2026) starts from algorithmic information theory.
- **The definition.** Take the MDL-optimal ("Occam's razor") model of each part and of the whole. Compositional novelty is K(m_x | m_xa, m_xb): the extra information needed to describe the whole's model, given the parts' models. Computing it at every node of a decomposition tree gives a multiscale *compositional structure profile*.
- **The library analogy.** The model is a library. Combining fragments counts as compositional only if it forces a new abstraction or a refactor, such as redefining a norm in terms of an existing matmul routine. Two cases score zero: calling an existing library more often, which gives high mutual information but no new structure, and putting two unrelated programs side by side.
- **Relation to mutual information.** The measure implies algorithmic mutual information, but not conversely.
- **Positioning.** It deliberately contrasts with functor-style compositional semantics. Those assume the parts and composition rules are given in advance; this measure tries to find structure in raw data.
- **Experiments.** The measure is turned into a reward. Strings are evolved with an MDL-guided RePair grammar compressor. Images are evolved as CPPNs under NEAT, essentially Picbreeder with this reward in place of human choice. Compared with a reward for raw structure alone, it produced deeper, more nested but *smaller* grammars, and more unified images. The structure-only images tended toward disjoint colour bands.
- **Implications claimed.** It explains why depth is a good inductive bias, and suggests scoring curricula by how much each new segment reorganizes what came before.
- **Open.** Empirical scores depend on the chosen compressor, and their robustness is untested. Which decomposition tree is "right" is unresolved. The authors conjecture it is the tree that maximizes total compositionality. **[→ machine-learning-ai; cross-link → mathematics]**

---

**The paper's decomposition tree is already a rose tree, and its profile is a plain fold over it.**

The definition allows rooted, ordered trees whose internal nodes have any number (≥ 2) of children. That is `Rose`, with one invariant: each node's label is the concatenation of its children's labels. So it is a rose tree annotated with a monoid measure, like a finger tree's cached `measure`:

```haskell
data Rose a = Node a [Rose a]

-- labels: substrings; invariant: label = mconcat (map label kids)
profile :: (String -> Model) -> (Model -> [Model] -> Double)
        -> Rose String -> Rose (Maybe Double)
profile fit cond = go
  where
    go (Node s [])   = Node Nothing []
    go (Node s kids) = Node (Just (cond (fit s) (map (fit . label) kids)))
                            (map go kids)
```

The total score is a `sum` over the result. Each node's model depends only on its own substring, not on its children's models, so this is a catamorphism; no paramorphism is needed. **[→ scala-functional-programming; cross-link → machine-learning-ai]**

---

**Arity only matters at the extremes: the maximal decomposition reduces to binary splits, the minimal one to a flat tree.**

- **Maximal.** An appendix shows any n-ary join can be replaced by a left-associated chain of binary joins (`foldl1` over the children), at most a constant cost per join. Under the conjectured canonical choice, rose trees therefore collapse to binary trees.
- **Minimal.** One root with n leaf children. It scores about K(m_x) for every string, which is why the paper rejects it as uninformative.
- **Optimal substructure.** The paper's recursive-consistency theorem gives the maximal tree optimal substructure. Finding it is therefore an interval DP over binary splits, like CYK parsing or matrix-chain ordering, *if* the conditional complexity could be computed. It can't be computed exactly, so in practice it is approximated with a compressor. **[→ algorithms-data-structures]**

---

**A rose tree can also be the object measured, which gives the paper's open conjecture a clean test.**

Serialize the tree, for example as an S-expression, and run the string machinery on it. The grammar model acts like hash-consing: it turns the tree into a DAG of shared subtrees. Compositional novelty should spike at joins where sibling subtrees share a subtree that wasn't worth naming inside either sibling alone. The test: does the maximal tree computed for a serialized rose tree recover the tree's own shape? That is the "intrinsic decomposition" conjecture in its simplest form. The likely answer is "only when siblings genuinely share substructure"; independent siblings score near zero and can be bracketed arbitrarily.

One wrinkle: decompositions are contiguous splits of a sequence, so the branching has to come from the serialization order. Pre-order and level-order traversals give different decomposition spaces for the same tree. **[→ scala-functional-programming]**

---

<a id="ch4"></a>
## 4. Networks as programs

**Mechanistic interpretability can catch what behavioral tests miss, but "understanding makes models safer" is still mostly untested.**
[Papers › Large Language Models](https://vwulf.github.io/ettuge/Books/Papers#large-language-models) · [arXiv:2611.08438](https://arxiv.org/abs/2611.08438)

*Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety* (Nov 5, 2026) is a survey by more than 40 authors from Oxford, Mila, EleutherAI, MIT, Anthropic and others. It contains no new experiment. It was reviewed from the abstract page and overview; repeated attempts to read the full text were rate-limited.
- **Foundations covered.** Features, polysemanticity, how Transformers compute, circuits.
- **Methods covered.** Sparse autoencoders and feature extraction, circuit discovery with causal checks, natural-language explanations of intermediate states, learning dynamics, training-data attribution.
- **How to judge an explanation.** Five axes: attribution faithfulness, completeness, stability across seeds and prompts, causal validity, and human interpretability. The point is that plausibility alone rewards explanations that sound convincing but are wrong.
- **Six research orientations.** Pragmatic, Ambitious, Developmental, Across Time, Introspective and Automated. They trade scalability and time to impact against robustness to deception. Pragmatic work is quick and scales; Ambitious work is slow but harder to fool.
- **Safety uses and limits.** Knowledge editing, steering and monitoring. Explanations can be partial, interventions can break under distribution shift, and the methods carry adversarial and opportunity-cost risks.
- **Motivating example.** A linear probe on activations caught a planted "sleeper agent" backdoor at over 99% AUROC. The authors stress that this shows a detectable signal for a *deliberately trained* backdoor, not a general ability to detect deception or remove the behavior.
- **Conclusion.** Interpretability should complement behavioral testing and other safeguards, not stand alone as a guarantee. The paper ships code notebooks that reproduce key findings. It can be read alongside the Bereska and Gavves 2024 review. **[→ machine-learning-ai]**

---

**A frontier model can read and edit small networks' raw weights. The headline gains come from removing a bug, not adding a skill.**
[Papers › Large Language Models](https://vwulf.github.io/ettuge/Books/Papers#large-language-models) · [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)

The MIT CSAIL post (Takehi, Teoh, Zhang, Khattab) reports a model doing three things straight from weights:
- naming which game a policy network was trained on
- finding induction heads in a Transformer without running it
- writing a 1.5M-parameter Go network from all-zero weights that beat an equal-sized PPO network trained on 20 million games

The striking framing is recursive self-improvement: a model that fixes its own weights instead of launching training jobs. Three things make that framing too strong:
- **The headline fix removes a bug.** Qwen3.5-0.8B went from 7.9% to 48.1% on MATH-500 by finding the direction behind its known thinking loops and subtracting it, changing 0.016% of the weights. That is close to existing directional-ablation methods. On Gemma 3 270M, which doesn't loop, nothing improved. The authors conclude that editing can uncover a hidden ability but not create a missing one.
- **"From scratch" means compiled.** For Breakout, the model worked out where the ball would land and wired that rule into the network layer by layer. That is Tracr-style compilation (chapter 2) done by reasoning, not learned intelligence. The more interesting reading is that networks are basically programs.
- **There are limits.** It couldn't identify a sycophantic model from weights alone and needed attention patterns.

The post is not peer-reviewed, though it releases full logs. The application that matters most is *auditing*: spotting backdoors or hidden behaviors from weights before deployment. That connects directly to the survey above. **[→ machine-learning-ai]**

---

<a id="ch5"></a>
## 5. Architecture

**Architecture decides what a model computes; systems decide whether it can be trained at all.** This chapter and the next treat eight architectural ideas and nine systems techniques, each by the problem it solves, its mechanism, its weaknesses and where it is used. Original papers are catalogued under [Papers › Large Language Models](https://vwulf.github.io/ettuge/Books/Papers#large-language-models) and [Papers › Deep Learning](https://vwulf.github.io/ettuge/Books/Papers#deep-learning).

---

**Mixture of Experts separates how much a model knows from how much a token costs.**
Each FFN block becomes N expert FFNs plus a learned router that sends each token to its top-k experts (usually 1–8). Parameters scale with N, but compute per token scales with k. The lineage runs from Jacobs and Jordan (1991) through Shazeer's sparsely gated MoE (2017), GShard (2020) and Switch Transformer (2021), which showed top-1 routing works. The hard parts are router collapse (countered with a load-balancing loss), unstable router logits (router z-loss), and holding every expert in memory. DeepSeekMoE added fine-grained experts plus always-on shared ones. DeepSeek-V3 swapped the auxiliary loss for a routing bias term, with 671B total and 37B active parameters. Used in Mixtral, DeepSeek-V2/V3, Qwen3-MoE, Llama 4, gpt-oss, Kimi K2 and most frontier models. **[→ machine-learning-ai]**

---

**Grouped Query Attention shrinks the KV cache by sharing K/V heads.**
Decoding is bandwidth-bound: each new token reads the whole KV cache. Multi-Query Attention (Shazeer, 2019) shares one K/V head across all query heads, at some cost in quality. GQA (Ainslie et al., 2023) splits H query heads into G groups, each sharing a K/V head, shrinking the cache by H/G. G = 1 is MQA and G = H is MHA; 8 KV heads is common. An existing MHA checkpoint can be *uptrained* to GQA by mean-pooling its K/V heads, using about 5% of the original pretraining compute. Used in Llama 2 70B and later, Mistral, Qwen and Gemma. **[→ machine-learning-ai]**

---

**Multi-head Latent Attention compresses K/V instead of removing it.**
DeepSeek-V2 (2024) projects each token to a small latent (about 512 dimensions) and caches only that. Per-head K and V come from up-projections, which at inference can be *absorbed* into the query and output projections, so attention runs directly on the latent. RoPE breaks the absorption, so MLA adds a small *decoupled RoPE* key (about 64 dimensions) shared across heads and cached alongside. The cache is about the size of GQA with two or three groups, with quality reported at or above full MHA. Used in DeepSeek-V2/V3/R1 and Kimi K2; TransMLA converts GQA models to MLA. **[→ machine-learning-ai]**

---

**Selective state-space models (Mamba) make a linear recurrence content-aware.**
S4-style SSMs, h_t = Āh_{t−1} + B̄x_t, have time-invariant parameters. That lets training run as one long convolution, but it means they can't keep or drop information based on content, so they fail tasks like selective copying. Mamba (Gu and Dao, 2023) makes B, C and the step Δ depend on the input. The convolution trick is lost, so it uses a hardware-aware parallel scan that keeps the expanded state in SRAM. Training is linear in length, and inference keeps a constant-size state with no KV cache. Mamba-2 shows selective SSMs are structured (semiseparable) linear attention, which runs on tensor cores. A fixed state can't reliably recall arbitrary distant tokens, so production models are hybrids with a few attention layers: Jamba, Zamba, Nemotron-H, Falcon-H1, and Gated DeltaNet in Qwen3-Next. **[→ machine-learning-ai]**

---

**Diffusion language models generate many tokens per step, at the cost of the KV cache.**
Masked diffusion masks each token with probability t, trains a bidirectional Transformer to predict all masked tokens (a weighted cross-entropy that bounds log-likelihood), and samples by unmasking over several steps, the most confident first. The lineage runs D3PM (2021), SEDD (ICML 2024 best paper), MDLM, and LLaDA (2025), an 8B model competitive with Llama 3 8B. Mercury and Gemini Diffusion are commercial versions. Strengths: high throughput (especially for code), native infilling, no left-to-right asymmetry such as the reversal curse. Weaknesses: no standard KV cache, and usually a fixed output length. Block diffusion (BD3-LM) is autoregressive over blocks and diffuses within each block. **[→ machine-learning-ai]**

---

**Test-time-training layers make the hidden state the weights of a small model that trains as it reads.**
In TTT (Sun et al., 2024), each token's update is a gradient step on a self-supervised loss, such as reconstructing one learned projection of the token from another. The output is the updated inner model applied to the token. TTT-Linear uses a linear inner model and TTT-MLP a two-layer MLP. Mini-batch TTT and a "dual form" turn the steps into matmuls. Linear attention is TTT with a linear model and a particular loss, and DeltaNet is online regression, so the framework unifies much of the linear-RNN literature. Perplexity kept improving with context where Mamba plateaued, and large-chunk TTT has scaled to minute-long video. **[→ machine-learning-ai]**

---

**Titans adds a neural long-term memory that writes surprising tokens harder.**
Titans (Behrouz, Zhong and Mirrokni, Google, 2024) updates a deep MLP memory at test time to minimize ‖M(k) − v‖². The gradient measures *surprise*. Momentum carries surprise forward, so the context after a surprising event is stored too. A data-dependent decay gate forgets. Attention handles short-term precise memory, the neural memory handles long-term compressed memory, and persistent tokens hold task knowledge. They can be wired three ways: Memory as Context, as Gate, or as Layer. Results are strong on needle-in-a-haystack and BABILong past 2M tokens. Atlas, MIRAS and Nested Learning/Hope generalize it into "learned optimizer as memory." **[→ machine-learning-ai]**

---

**Mixture of Depths decides *whether* a token uses a block at all.**
MoD (Raposo et al., DeepMind, 2024) routes the top-k tokens (say 12.5% capacity) through each routed block's attention and MLP. The rest skip it via the residual. A fixed k keeps the compute graph static and hardware-friendly, unlike most early-exit schemes. The block output is scaled by the router weight so the router gets gradients. Top-k over the whole sequence isn't available when sampling autoregressively, so a small auxiliary predictor guesses membership. It matches baseline quality with fewer FLOPs and faster sampling. It combines with MoE (MoDE) and relates to LayerSkip and Mixture-of-Recursions. **[→ machine-learning-ai]**

---

**Proven ideas and promising ones carry very different evidence.** MoE, GQA and MLA are proven at frontier scale. TTT, Titans, MoD and diffusion LMs are promising but not dominant. A list of what actually shaped today's LLMs should add three unglamorous components found in nearly every model: RoPE, pre-norm with RMSNorm, and SwiGLU. **[→ machine-learning-ai]**

---

**SpikingBrain captures only the energy side of spiking, not Hinton's program.**
[Papers › Deep Learning](https://vwulf.github.io/ettuge/Books/Papers#deep-learning) · [arXiv:2509.05276](https://arxiv.org/abs/2509.05276)

SpikingBrain-7B and 76B-A12B are linear-attention and MoE models converted from Qwen2.5, with "spiking" activations, trained on non-NVIDIA (MetaX) GPUs. Measured against Hinton's ideas (Forward-Forward, mortal computation, fast weights, event-driven neurons), they capture only the energy saving of skipping zeros. Training is ordinary backprop, and spikes are added afterward as a form of quantization. Spike *timing* as information, stochastic firing as regularization, and spike-timing-dependent plasticity are all absent. The genuine lineage link is fast-weight memory, which runs through linear attention and, per the TTT view above, through test-time training. **[→ machine-learning-ai]**

---

**Neural operators learn maps between function spaces, so one trained model works across discretizations.**
[Papers › Deep Learning](https://vwulf.github.io/ettuge/Books/Papers#deep-learning)

*Neural Operator* (JMLR 2023) generalizes networks to operators between infinite-dimensional function spaces, with discretization-invariant architectures for PDE solution maps. The *Fourier Neural Operator* (ICLR 2021) parameterizes the integral kernel in Fourier space, giving fast, resolution-independent solvers for PDE families such as Navier–Stokes. That links it to the blowup work in [Math Deep Dives › Millennium problems](https://vwulf.github.io/ettuge/Deep-Dives/math/ch4). A fast surrogate is not a proof, though: neural operators approximate smooth solution maps, which is exactly what breaks near a singularity. **[→ machine-learning-ai; cross-link → mathematics]**

---

**Since FNO, the field has moved to irregular geometry, transformers, generative rollouts and pretraining, and become more sober about speed-ups.**
[Operator Learning: Algorithms and Analysis, arXiv:2402.15715](https://arxiv.org/abs/2402.15715) · [A Unifying View of PINNs and Neural Operators, arXiv:2601.14517](https://arxiv.org/abs/2601.14517) · [PDEs in the Age of Machine Learning, arXiv:2603.07655](https://arxiv.org/abs/2603.07655)

This entry is a survey-level overview drawn from recent reviews, not a close reading of each paper.

- **Theory.** FNO is a universal approximator of continuous operators. But its claim to work at any resolution is weaker than first presented, because pointwise nonlinearities alias on a grid. Representation-equivalent neural operators (ReNO) and the Convolutional Neural Operator (CNO) are attempts to make discretization-invariance precise. The 2024 review by Kovachki, Lanthaler and Stuart still describes the theory as incomplete.
- **Geometry and architecture.** FNO assumes a uniform grid. Geo-FNO, GINO and graph-based operators handle irregular meshes, and transformer operators (OFormer, GNOT, Transolver, UPT) now often beat FNO on 3D and mesh problems. Physics-informed variants such as PINO add the PDE residual to the loss. A 2026 survey argues that PINNs and neural operators approximate the same specification-to-solution map and are not competing paradigms.
- **Long rollouts.** Step-by-step prediction drifts and becomes unstable. Diffusion-based refinement (PDE-Refiner) and probabilistic operators handle long-horizon and chaotic dynamics better.
- **Weather is the largest payoff.** FourCastNet (Adaptive FNO) and the spherical FNO came directly from this line. GraphCast, Pangu-Weather, GenCast and Aurora followed, and ML forecast models now run operationally (ECMWF's AIFS).
- **Foundation models.** Transformers pretrained on many physical systems and fine-tuned with little data: MPP, DPOT, Poseidon, and OmniArch (ICML 2025), which keeps a Fourier encoder-decoder inside a transformer.
- **Benchmarks and caution.** PDEBench and The Well standardized comparisons. McGreivy and Hakim (*Nature Machine Intelligence*, 2024) found that many reported speed-ups came from weak baselines. A 2026 synthesis puts the difference this way: classical solvers have error bounds derived from the PDE, while ML accuracy depends on how close a problem is to the training data. That gap is why hybrid ML-plus-solver methods get so much attention. **[→ machine-learning-ai; cross-link → mathematics]**

---

<a id="ch6"></a>
## 6. Training at scale

**Tensor parallelism splits each layer's matrices across GPUs, and pays for it with communication on every layer.**
Megatron-LM (Shoeybi et al., 2019) makes the MLP's first GEMM column-parallel, so GeLU applies locally, and the second row-parallel, followed by an all-reduce. Attention is split by heads, with an all-reduce after the output projection. That is two all-reduces forward and two backward per layer, plus vocab-parallel embeddings and loss. Because the communication is on the critical path every layer, TP needs NVLink-class bandwidth and is almost always kept within a node (TP ≤ 8). **[→ machine-learning-ai]**

---

**ZeRO/FSDP shard the 16 bytes per parameter that plain data parallelism copies to every GPU.**
With Adam in mixed precision, each parameter costs about 16 bytes: 2 for weights, 2 for gradients, and 12 for the fp32 master copy and the two moments. ZeRO (Rajbhandari et al., 2020) shards this across N data-parallel ranks in stages:
- **Stage 1** shards optimizer states, giving 4Ψ + 12Ψ/N.
- **Stage 2** also shards gradients, using reduce-scatter.
- **Stage 3** also shards parameters, all-gathering each layer just in time, giving 16Ψ/N at about 1.5× the communication.

Prefetching overlaps the gathers with compute. FSDP is PyTorch's version (FSDP2 shards per parameter via DTensor). HSDP shards within a node and replicates across nodes. ZeRO-Offload and ZeRO-Infinity spill to CPU or NVMe. **[→ machine-learning-ai]**

---

**Pipeline parallelism sends only stage-boundary activations, which makes it the natural choice across nodes.**
GPipe (Huang et al., 2019) splits the layers into p stages and each batch into m micro-batches. The idle "bubble" fraction is (p−1)/(m+p−1), so m must be much larger than p. GPipe kept every micro-batch's activations and relied on recomputation. Refinements: 1F1B (PipeDream) caps in-flight activations at p; interleaved stages (Megatron, 2021) shrink the bubble; zero-bubble schedules split the backward pass into input-gradient and weight-gradient steps; DualPipe (DeepSeek-V3) runs pipelines in both directions and hides communication completely. **[→ machine-learning-ai]**

---

**Mixed precision halves the bytes per number each generation, and keeps training stable with a few safeguards.**
Micikevicius et al. (2017) do matmuls and store activations in 16-bit, while keeping an fp32 master copy of the weights, dynamic loss scaling for fp16, and fp32 accumulation and sensitive ops (softmax, norms, loss). BF16 has fp32's exponent range and needs no loss scaling, so it is now the default. FP8 on Hopper uses E4M3 forward and E5M2 for gradients. DeepSeek-V3 trained in FP8 at frontier scale with fine-grained block scaling (1×128 tiles for activations, 128×128 for weights) and periodic promotion to fp32. Microscaling formats (MXFP8/MXFP4, NVFP4 on Blackwell) share a scale across 16–32 elements. Each halving roughly doubles matmul throughput and halves memory traffic. **[→ machine-learning-ai]**

---

**FlashAttention is exact attention made IO-aware, and long-context training depends on it.**
Standard attention writes the n×n score matrix to HBM and reads it back: bandwidth-bound and O(n²) in memory. FlashAttention (Dao et al., 2022) tiles Q, K and V into SRAM, uses an online softmax (running max and sum) to stay exact without a full row of scores, and stores only the per-row log-sum-exp, recomputing scores in the backward pass. Memory falls to O(n). FA2 roughly doubled speed with better parallelism over the sequence. FA3 uses Hopper's warp specialization, TMA and WGMMA, overlaps softmax with GEMMs and supports FP8. FA4 targets Blackwell. Its impact on what is practically trainable is comparable to TP or ZeRO, so it arguably ranks above most of this list. **[→ machine-learning-ai]**

---

**Activation checkpointing trades about a third more compute for most of the activation memory.**
At large batch × sequence × layers, activations dominate memory. Chen et al. (2016), building on Griewank, store selected checkpoints and recompute in between, reaching O(√n) memory for one extra forward pass. In Transformers you typically save each layer's input and recompute the layer, adding about 33%. Selective recomputation (Korthikanti et al., 2022) recomputes only memory-heavy, compute-cheap pieces (softmax, dropout masks, norms) for a few percent overhead. DeepSeek-V3 recomputes RMSNorm and the MLA up-projections. Offloading activations to CPU is the alternative. **[→ machine-learning-ai]**

---

**Sequence parallelism comes free with tensor parallelism.**
TP leaves the regions between attention and the MLP (LayerNorm, dropout, residuals) replicated on every rank. Korthikanti et al. (2022) split those regions along the sequence dimension. Each all-reduce becomes a reduce-scatter in and an all-gather out: the same communication volume, with activation memory there divided by the TP size. DeepSpeed-Ulysses uses the name differently: an all-to-all re-shards from sequence to heads before attention and back afterward. Its degree is capped by the number of heads, which is small under GQA. **[→ machine-learning-ai]**

---

**Context parallelism shards a single sequence across GPUs for every layer, attention included.**
At 128K–1M+ tokens, one sequence's activations don't fit on a GPU. Ring Attention (Liu, Zaharia and Abbeel, 2023) keeps each GPU's Q block and rotates K/V blocks around a ring, computing blockwise attention with FlashAttention's online softmax while the next block is in transit. Under a causal mask later chunks do more work, so zigzag/striped sharding gives each rank chunks i and 2N−1−i. Llama 3 all-gathered K/V instead of using a ring, which works because GQA keeps K/V small. USP combines Ulysses-style and ring-style partitioning. **[→ machine-learning-ai]**

---

**Expert parallelism places experts on different GPUs, and its bottleneck is all-to-all across nodes.**
GShard (2020) runs each MoE layer as: all-to-all dispatch of tokens to their experts' GPUs, local expert compute, then all-to-all combine. A capacity factor caps tokens per expert; overflow passes through the residual, or "dropless" MoE (MegaBlocks) uses block-sparse grouped GEMMs. DeepSeek-V3 limits each token to at most four nodes, uses its DeepEP kernels, and hides all-to-all behind compute with DualPipe. Load imbalance creates stragglers, which is a systems reason routing balance matters. Very wide EP, across hundreds of GPUs, is how DeepSeek-class models are served. **[→ machine-learning-ai]**

---

**A modern run stacks all of these, and two frontier recipes show the range.**
Within a node: TP + SP. For long sequences: CP. Across node groups: PP. Outermost: FSDP/ZeRO data parallelism. MoE layers: EP, laid across the other dimensions. Mixed precision, FlashAttention and checkpointing apply everywhere. Llama 3 405B used TP + CP + PP + FSDP. DeepSeek-V3 skipped TP entirely, leaning on EP + PP + ZeRO-1 with FP8. **[→ machine-learning-ai; cross-link → infrastructure-devops]**

---

**BendTorch's real contribution is its oracle harness, not its speed.**
[Papers › Deep Learning](https://vwulf.github.io/ettuge/Books/Papers#deep-learning)

Every training step is checked against PyTorch eager, with the same weights and batches and a per-step tolerance. Only PyTorch eager and BendTorch pass all four workloads. Most of the drift in other frameworks traced to small numeric choices: AdamW bias correction in float32 instead of double, where epsilon sits, float32 loss summation, and silent TF32. These are the same precision decisions as in the mixed-precision entry above, made silently. BendTorch is 3–6× slower than PyTorch on large matrix products (it has no BLAS), faster on tiny models where dispatch dominates, and weak on GPU. Still open: the same author built both the harness and the fixes for the other frameworks, and the results come from one machine and one run. **[→ machine-learning-ai]**

---

<a id="ch7"></a>
## 7. Serving and judging

**Disaggregated prefill and decode make the network the product.**
[Papers › LLM Inference Serving](https://vwulf.github.io/ettuge/Books/Papers#llm-inference-serving)

Prefill is compute-bound and decode is memory-bandwidth-bound, so modern stacks run them on separate workers. The discussion traced the full path:
- **Design:** NVIDIA Dynamo's disaggregated serving, with conditional disaggregation and KV-cache transfer.
- **Orchestration:** llm-d, running vLLM at scale on Kubernetes with an inference-aware scheduler.
- **Transfer:** vLLM's NixlConnector hands the KV cache from prefill to decode workers over NIXL, whose backends include UCX, GPUDirect Storage and POSIX.
- **Routing:** llm-d's endpoint picker indexes cache state across replicas and sends requests sharing a prefix to the replica already holding it.
- **Fabric:** an open RoCE reference architecture for disaggregated inference clusters, contributed to OCP.

Once KV transfer sits on the critical path, the fabric decides tail latency. That is the sense in which "the AI network is the product." It is the serving-side mirror of chapter 6: the KV cache that GQA and MLA shrink is exactly what now crosses the network. **[→ machine-learning-ai; cross-link → infrastructure-devops]**

---

**Decision models like Laya and Jev use Transformers as classifiers, not generators.**
[Decision Points as Effects](https://vwulf.github.io/ettuge/FP/decision-points-as-effects)

- **Laya (open source, Convai).** The English model is ModernBERT-large plus a small two-layer decision head, about 421M parameters; a multilingual version uses mmBERT. Attention is bidirectional, so nothing is decoded left to right. Each supplied option gets its own mask token. The hidden state at each mask becomes a score, and a softmax runs across options, so new categories need no retraining. It handles pick-one, ordinal-scale and yes/no-probability questions. It is trained with RL against proper scoring rules, to learn honest probabilities.
- **Jev (TypeSafe AI).** The same idea as a hosted API. Its architecture is unpublished, so it isn't even confirmed to be a Transformer.

| | Decision model | Reasoning model |
|---|---|---|
| Attention | bidirectional encoder | causal decoder |
| Output | probabilities over supplied options | generated text |
| Compute | one forward pass, tens of ms | many decode steps, often seconds |
| Extra thinking | none | chain of thought at inference time |
| Failure mode | confidently wrong choice | invented content, malformed output |

"Can't hallucinate" only means it can't answer outside your options; it can still pick the wrong one confidently. Laya's base model scores below the majority-class baseline zero-shot on its own benchmark, so the headline accuracy needs fine-tuning. On a phishing test Jev scored 62.6% against 81.3% for Claude Haiku 4.5. The division of labour: decision models for fast, high-volume routing and triage, reasoning models where the answer must be worked out. **[→ machine-learning-ai]**

---

**Decision models only pay off as eval judges after you tune and calibrate them on your own labels.**
[Papers › Applied ML](https://vwulf.github.io/ettuge/Books/Papers#applied-ml) · [Effects and LLM Systems](https://vwulf.github.io/ettuge/FP/bucket-effects-llm)

Hamel Husain and Antaripa Saha's guide sets out the method:
- Get human pass/fail labels on real traces.
- Tune each model's threshold separately with 5-fold cross-validation, on the same splits for every model; the default 0.5 is not to be trusted.
- Set minimum precision and recall for the use case (80%/80% for alerting) and drop models that miss them.
- Plot F1 against cost and choose from the Pareto frontier.
- Check calibration with reliability curves and Brier scores before reading a score as a confidence.
- Use one judge per failure mode, and keep a held-out test set.

On 98 apartment-leasing traces:
- **OpenAI Decisions** had the best F1 (0.87) and the highest cost (3.72¢ per 100 runs). It is LLM-backed.
- **Perplexity Decider** was the cheapest to pass, at F1 0.79 for 0.82¢.
- **Liquid d1-ultra** passed and was well calibrated.
- **Liquid d1 and Cloudflare Clef Flash** fell short. In one Clef Flash bucket, the model predicted about 8% failures where 60% actually failed.
- **Platt scaling** helped some models, slightly hurt OpenAI's and barely moved Jev's.
- **Jev's prompt.** Swapping Jev's plain prompt for a failure-type checklist moved its F1 from 0.78 to 0.80.

This fits the classifier picture above. Calibration and zero-shot accuracy are the weak spots, so value appears only after tuning. The best performer had an LLM underneath, consistent with LLMs earning their cost when spotting a failure takes reasoning. Caveats: one small dataset, no latency measurements (usually the main reason to pick a decision model; see Decision Points as Effects for measured latencies), and Laya untested. **[→ machine-learning-ai]**

---

<a id="ch8"></a>
## 8. Themes across the deep dives

**Networks are programs.** RASP and Tracr compile programs into attention layers (chapter 2). Weight-space programming compiles reasoned rules into weights and reads behavior back out (chapter 4). The compositionality measure treats a model as a library that composition must refactor (chapter 3). Interpretability is the reverse direction: decompiling weights into circuits and features.

**Structure versus learned soft operations.** DP is a recursion scheme with guarantees; attention is a learned soft step without them. The rose-tree profile is a catamorphism and the maximal decomposition an interval DP. λ-RLM ([Effects and LLM Systems](https://vwulf.github.io/ettuge/FP/bucket-effects-llm)) wraps a fixed set of lawful combinators around a model. In each case, the guarantees come from the structure around the learned part, not from the learned part.

**"Optimal" always has a frame.** The Transformer book's optimality results hold within a criterion or a chosen threshold. INCRT is minimal relative to θ_w. A probe's 99% AUROC holds for a planted backdoor. A decision model's F1 holds after threshold tuning on one dataset. Every headline number came with a scope, and the scope was where the discussion did its work.

**Memory bandwidth is the recurring constraint.** GQA and MLA shrink the KV cache. Mamba, TTT and Titans replace it with a fixed state. FlashAttention avoids HBM round trips. Disaggregated serving moves the KV cache across a network. Much of the architecture and systems progress is about where the cache lives and how many bytes it costs.

**Fourier analysis keeps coming back.** The Fourier transform diagonalizes operators that commute with a group action: translations on a line or grid, rotations on a sphere. So wherever an architecture builds in a symmetry, a Fourier basis tends to appear.
- *Position* (chapter 1). RoPE rotates queries and keys at a range of frequencies, so attention scores depend only on relative position. That is a phase shift. Context extension (NTK-aware scaling, YaRN) works by rescaling those frequencies. Sinusoidal encodings, and the Fourier features used in NeRF-style coordinate networks, belong to the same family.
- *Computation* (chapter 5). The FFT turns a length-n convolution from O(n²) into O(n log n). Long-convolution and state-space models (S4, Hyena, FlashFFTConv) depend on it. FNet replaces attention with a plain FFT and keeps much of BERT's accuracy. FNO and Adaptive FNO mix information in the frequency domain.
- *How networks learn.* Spectral bias, or the frequency principle: networks fit low frequencies first. That helps explain why they generalize and why they blur fine detail. Diffusion models can be read as spectral autoregression, settling coarse structure before fine detail.
- *Interpretability* (chapter 4). Small transformers that grok modular addition turn out to implement a discrete Fourier transform internally, adding by rotating phases (Nanda et al., 2023). Pretrained LLMs have been found to represent numbers with Fourier features: low frequencies for magnitude, high frequencies for digits such as the value mod 10.
- *Beyond grids.* Spectral graph convolutions use Laplacian eigenvectors as a graph Fourier basis. Equivariant networks for molecules and proteins (e3nn, MACE) use spherical harmonics, the Fourier analysis of rotations. Speech models such as Whisper still take log-Mel spectrograms as input.

Categorically, with a group seen as a one-object category, equivariant maps are natural transformations, and Fourier analysis is the change of basis that makes them diagonal. Related categorical notes are in [Algebra and Categories](https://vwulf.github.io/ettuge/FP/bucket-algebra-categories). **[→ machine-learning-ai; cross-link → mathematics]**

**Judge the claim by its evidence.** Sources here range from a proof-based monograph read through its preprints, to an abstract-only survey, to a blog post with released logs, to a single-author benchmark on one machine. Each entry above records which. **[→ machine-learning-ai]**
