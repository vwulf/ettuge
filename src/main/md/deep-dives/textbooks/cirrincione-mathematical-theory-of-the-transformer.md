<a id="ch1"></a>
# Mathematical Theory of the Transformer, Volume I: Foundations, Rationality, and the Incremental Transformer

> Giansalvo Cirrincione · manuscript prepared for MIT Press, 15 May 2026 (Zenodo DOI 10.5281/zenodo.20199413) · [the PDF in Drive](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

A research monograph with very fine sectioning, so summaries and terms are given per chapter; each section is listed with its PDF page range. Concluding-remarks sections and the four appendices (mathematical background, notation, experimental pipeline, Schatten deflation) are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A mathematical theory of the Transformer’s attention mechanism, built around the bilinear score matrix M = W_Q W_Kᵀ and its split into symmetric and antisymmetric parts. After setting up embeddings, positional encoding, layer norm, multi-head attention and BERT (with a SARS-CoV-2 classification case study), it proves results about reciprocity, directionality and post-softmax persistence, classifies attention heads into eight canonical local regimes and global “signature geographies”, and models information flow with a motor formalism of forward and backward dynamics. It studies how signatures emerge during training (orbits, sharpness, activation, silence), defines notions of head redundancy and design principles, and proposes a “Rationalised Transformer” and an incremental growth controller (INCRT) with guarantees, spectral gate analysis, experiments on proteomes, control and materials design, and a recommended anchored multi-head bilinear gated (A-MHB-G) architecture.

**Contents**

1. [1. Sequences, Embeddings, and Positional Encoding](ch1): Inputs to attention: embeddings, position and normalization.
2. [2. The Self-Attention Mechanism](ch2): The attention mechanism dissected.
3. [3. BERT: Pre-training, Fine-tuning, and Case Study](ch3): BERT and a case study.
4. [4. The Symmetric/Antisymmetric Decomposition](ch4): Splitting M into symmetric and antisymmetric parts.
5. [5. Post-Softmax Persistence](ch5): Which pre-softmax structure survives softmax.
6. [6. Local Analysis: The Eight Canonical Regimes of Attention](ch6): A taxonomy of eight local attention regimes.
7. [7. Global Analysis: Canonical Signatures and Attention Geography](ch7): Global signature geographies across layers.
8. [8. Signature Re-Extraction and Global Information Flow](ch8): Information flow and re-extraction of signatures.
9. [9. Motor Formalism for Signature Dynamics](ch9): Motors: a formalism for forward and backward dynamics.
10. [10. Self-Attention Motor Decomposition](ch10): Motor decomposition of self-attention.
11. [11. Signature Orbits and Training Dynamics](ch11): How signatures form during training.
12. [12. Sharpness, Activation, and Silence](ch12): When patterns sharpen, activate or fall silent.
13. [13. Redundancy and Design Principles](ch13): Redundant heads and design principles.
14. [14. The Rationalised Transformer](ch14): A redesigned “rationalised” Transformer block.
15. [15. INCRT I: From Static Rationalisation to Incremental Growth](ch15): Growing a Transformer incrementally (INCRT I).
16. [16. INCRT II: Extensions, Guarantees, and Applications](ch16): INCRT extensions and guarantees.
17. [17. Spectral Gate Dynamics: Degeneracy Regimes and the Unified Gate](ch17): Spectral gate dynamics.
18. [18. Experimental Validation](ch18): Experiments.
19. [19. Anchored Multi-Head Bilinear Gating: The Recommended Architecture](ch19): The recommended A-MHB-G architecture.


---

## 1. Sequences, Embeddings, and Positional Encoding

*PDF pp. 37–63*

Inputs to attention: embeddings, position and normalization.

*Terms:* embeddings, hidden state matrix, sinusoidal positional encoding, learned positional encoding, layer normalisation, rank neutrality, residual stream

**From Symbols to Vectors: The Vocabulary and the Embedding Map**  
→ PDF p. 38 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Hidden State Matrix**  
→ PDF p. 39 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Positional Encoding: Geometry of Order**  
→ PDF pp. 40–54 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Layer Normalisation**  
→ PDF pp. 55–56 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Rank-Neutrality Theorem**  
→ PDF pp. 57–58 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Residual Connections and the Cumulative Representation**  
→ PDF pp. 59–60 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch2"></a>
## 2. The Self-Attention Mechanism

*PDF pp. 64–119*

The attention mechanism dissected.

*Terms:* single head, score matrix M, four-term positional expansion, multi-head attention, feed-forward block, computational cost, empirical illustrations, multi-scale attention

**Structure and levels**  
→ PDF p. 65 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Single Attention Head**  
→ PDF pp. 65–75 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Positional Encoding in the Score: The Four-Term Expansion**  
→ PDF pp. 76–79 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Multi-Head Attention and the Canonical Pair (M,N)**  
→ PDF pp. 80–92 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Feed-Forward Block and the Residual Stream**  
→ PDF pp. 93–96 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Computational Cost of the Attention Mechanism**  
→ PDF pp. 97–99 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Structure of M**  
→ PDF pp. 100–108 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Empirical Illustrations**  
→ PDF pp. 109–114 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**For the Specialist: Multi-Scale Attention and the Resolution Problem**  
→ PDF pp. 115–117 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch3"></a>
## 3. BERT: Pre-training, Fine-tuning, and Case Study

*PDF pp. 120–139*

BERT and a case study.

*Terms:* BERT, masked language modeling, next sentence prediction, fine-tuning, rank collapse, SARS-CoV-2 classification

**Pre-training: MLM and NSP**  
→ PDF pp. 120–121 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Fine-tuning**  
→ PDF p. 122 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**State of the Art: Rank, MLP, and Beyond**  
→ PDF pp. 123–135 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Case Study: SARS-CoV-2 Classification**  
→ PDF pp. 136–138 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch4"></a>
## 4. The Symmetric/Antisymmetric Decomposition

*PDF pp. 140–154*

Splitting M into symmetric and antisymmetric parts.

*Terms:* symmetric-antisymmetric decomposition, reciprocity, directionality, cycle circulation, directional energy, asymmetry index

**The decomposition**  
→ PDF p. 140 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Proposition A: the Reciprocity–Directionality Identity**  
→ PDF p. 141 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Theorem B: the Cycle Circulation Theorem**  
→ PDF p. 142 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Theorem C: directional energy**  
→ PDF p. 143 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Relation with the concurrent work of Saponati et al.**  
→ PDF pp. 144–146 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The asymmetry index at initialisation**  
→ PDF pp. 147–148 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Parameter type and sequence activity**  
→ PDF p. 149 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Numerical verification principles**  
→ PDF p. 150 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Dynamics and layer normalisation**  
→ PDF pp. 151–153 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch5"></a>
## 5. Post-Softmax Persistence

*PDF pp. 155–178*

Which pre-softmax structure survives softmax.

*Terms:* attention sinks, antisymmetric sink theorem, edge persistence, taxonomy

**Why post-softmax persistence is non-trivial**  
→ PDF p. 155 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Related work and positioning**  
→ PDF pp. 156–161 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Antisymmetric Sink Theorem**  
→ PDF pp. 162–163 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Directional Edge Persistence Criterion**  
→ PDF p. 164 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Quantitative indices and the four-class taxonomy**  
→ PDF pp. 165–166 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Geometric reading of the sink condition**  
→ PDF p. 167 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Numerical illustration of the theorems**  
→ PDF pp. 167–171 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch6"></a>
## 6. Local Analysis: The Eight Canonical Regimes of Attention

*PDF pp. 179–233*

A taxonomy of eight local attention regimes.

*Terms:* attention patterns, identity, uniform, vertical, block, diagonal, canonical regimes, pattern completeness

**Local notation**  
→ PDF p. 180 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Two classification problems**  
→ PDF p. 181 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Prior taxonomies of attention patterns**  
→ PDF pp. 182–186 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Unified taxonomy of the eight canonical regimes**  
→ PDF p. 187 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Open gate: the identity pattern**  
→ PDF pp. 188–189 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Closed gate: the maximal-entropy pattern**  
→ PDF pp. 190–191 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Directional gate: the vertical line pattern**  
→ PDF pp. 192–193 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Cluster head: the block pattern**  
→ PDF pp. 194–196 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Backward contextual gate: the sub-diagonal pattern**  
→ PDF pp. 197–198 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Forward contextual gate: the super-diagonal pattern**  
→ PDF pp. 199–200 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Instance gate: the pointwise pattern**  
→ PDF p. 201 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Inverse directional gate: the horizontal pattern**  
→ PDF p. 202 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Pattern composition and linear decomposition**  
→ PDF pp. 203–204 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The rank-entropy duality**  
→ PDF pp. 205–206 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Relative completeness within the shift-regular grammar**  
→ PDF pp. 207–210 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Canonical signatures, projection, and stratification**  
→ PDF pp. 211–220 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Pattern emergence: corrected sufficient conditions**  
→ PDF pp. 221–224 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Subspace activation and silence: corrected**  
→ PDF pp. 225–227 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Minimal replacement statements for the original claims**  
→ PDF pp. 228–230 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Synthesis and Handover**  
→ PDF pp. 231–233 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch7"></a>
## 7. Global Analysis: Canonical Signatures and Attention Geography

*PDF pp. 234–284*

Global signature geographies across layers.

*Terms:* signature geography, layer geography, head-gauge symmetry, transport, transition matrices

**Signature Geography in BERT**  
→ PDF pp. 235–238 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Information Flow Along the Layers**  
→ PDF pp. 239–244 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Head-Gauge Symmetry and Channel Non-Identifiability**  
→ PDF pp. 245–247 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**From local signatures to global geographies**  
→ PDF pp. 248–249 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Dictionary coverage recalled**  
→ PDF p. 250 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Layer geography**  
→ PDF p. 250 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Signature transport across layers**  
→ PDF p. 251 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Coarse transition matrices as discretisations**  
→ PDF p. 251 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Global observables**  
→ PDF pp. 251–252 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Residual amplification and perturbation bounds**  
→ PDF p. 253 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Data-dependent Jacobian control**  
→ PDF p. 254 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Activation across depth**  
→ PDF p. 255 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The all-closed locus**  
→ PDF p. 256 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Linearised softmax at the closed locus**  
→ PDF p. 257 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Saddle escape and projected signatures**  
→ PDF p. 257 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Finite-noise selection**  
→ PDF p. 258 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Łojasiewicz convergence and signatures**  
→ PDF p. 259 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Layer-coupled structural stability**  
→ PDF p. 259 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Empirical validation: BERT-small from scratch**  
→ PDF p. 260 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Task dependence of geography**  
→ PDF p. 260 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Why backpropagation? A Roberts–Yaida–Hanin perspective**  
→ PDF p. 261 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Signature geography as mesoscopic state space**  
→ PDF p. 262 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Exploiting attention geography**  
→ PDF pp. 262–264 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Replacement map for the old theorems**  
→ PDF p. 265 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Hypotheses table**  
→ PDF pp. 265–267 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Synthesis**  
→ PDF p. 268 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Interpreting the C1–C4 geography**  
→ PDF p. 268 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Conjectures and empirical hypotheses**  
→ PDF p. 269 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Extended empirical protocol for signature geography**  
→ PDF p. 270 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Model comparison**  
→ PDF p. 271 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Signature-aware pruning**  
→ PDF p. 272 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Distribution shift and robustness**  
→ PDF p. 272 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Detailed experimental design for future chapters**  
→ PDF p. 273 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Dictionary expansion**  
→ PDF p. 274 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Examples of possible missing regimes**  
→ PDF p. 275 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Dependency map for later chapters**  
→ PDF p. 275 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Metric and transport geometry of signatures**  
→ PDF pp. 276–278 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Training-path geometry in signature space**  
→ PDF p. 279 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Canonical replacement and dictionary fidelity**  
→ PDF pp. 280–281 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Open programme: mean-field geography**  
→ PDF p. 282 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A rejected direction: sheaves over the input space**  
→ PDF p. 283 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch8"></a>
## 8. Signature Re-Extraction and Global Information Flow

*PDF pp. 285–311*

Information flow and re-extraction of signatures.

*Terms:* residual block, re-extraction cost, transport diagnostics, singular alignment

**From signature geography to information flow**  
→ PDF pp. 286–287 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Head-gauge symmetry and parametrisation non-identifiability**  
→ PDF p. 288 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Algebraic form of the residual block**  
→ PDF pp. 289–292 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The cost of re-extraction**  
→ PDF p. 293 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Transport between layer geographies**  
→ PDF pp. 293–294 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Transport diagnostics for global information flow**  
→ PDF pp. 295–296 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Cone geometry, singular alignment, and entropy control**  
→ PDF p. 297 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Margin–entropy control**  
→ PDF p. 298 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Conditional entropy proxy decay**  
→ PDF p. 299 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Compatibility profiles and transition layers**  
→ PDF p. 300 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Compatibility bounds behind the profile**  
→ PDF pp. 301–302 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A conditional compatibility theorem**  
→ PDF p. 303 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Projecting the compatibility profile onto signature space**  
→ PDF p. 304 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Small explanatory experiments**  
→ PDF p. 305 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Empirical protocol for a real model**  
→ PDF p. 306 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Worked finite-head transport example**  
→ PDF p. 307 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Reinterpretation of the older diagnostic figures**  
→ PDF p. 308 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Re-extraction, redundancy, and design implications**  
→ PDF p. 309 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Synthesis**  
→ PDF p. 309 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Interfaces with Subsequent Chapters**  
→ PDF pp. 310–311 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch9"></a>
## 9. Motor Formalism for Signature Dynamics

*PDF pp. 312–341*

Motors: a formalism for forward and backward dynamics.

*Terms:* motors, MLM head, computational graph, feed-forward as gated motor, LayerNorm

**Definition and taxonomy of motors**  
→ PDF p. 313 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Related work: the surrounding landscape**  
→ PDF pp. 314–316 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The masked-language-model head as primary signal motor**  
→ PDF p. 317 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The computational graph of one BERT encoder block**  
→ PDF pp. 318–319 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Differential anatomy of a BERT block**  
→ PDF p. 320 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The feed-forward block as a gated motor transformer**  
→ PDF p. 320 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**LayerNorm as a structural motor**  
→ PDF pp. 321–322 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Self-attention: convex value path and simplex motor**  
→ PDF p. 323 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Backpropagation through value, score, query, and key paths**  
→ PDF p. 324 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Headwise motor decomposition**  
→ PDF p. 325 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Block-level motor synthesis**  
→ PDF p. 325 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Motor recursion across stacked blocks**  
→ PDF p. 326 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Residual-path approximation**  
→ PDF p. 327 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Canonical QK-pair motors and signature variation**  
→ PDF p. 328 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Symmetric–antisymmetric score motors**  
→ PDF p. 329 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Global S–A pattern maps in the BERT/SARS case study**  
→ PDF pp. 330–331 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**From S–A maps to signature dynamics**  
→ PDF pp. 332–333 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Low-rank local motors**  
→ PDF p. 334 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Low-rank batch motors**  
→ PDF p. 334 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Motor observables and small experiments**  
→ PDF p. 335 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Anisotropy invariant of the value-path motor**  
→ PDF p. 336 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Motor anisotropy invariants**  
→ PDF p. 337 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Cone- and anisotropy-stratified motor bounds**  
→ PDF p. 338 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Interface with the next chapters**  
→ PDF p. 339 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Scope and limitations**  
→ PDF p. 340 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch10"></a>
## 10. Self-Attention Motor Decomposition

*PDF pp. 342–364*

Motor decomposition of self-attention.

*Terms:* QK pair, gauge-canonical, forward score geometry, softmax tangent, backward motor, signature velocity

**Inputs and outputs of the chapter**  
→ PDF p. 343 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The gauge-canonical QK pair**  
→ PDF p. 343 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Symmetric–antisymmetric decomposition**  
→ PDF p. 344 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Forward score geometry**  
→ PDF p. 344 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Interpretation of symmetric and antisymmetric motors**  
→ PDF p. 345 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Softmax response and tangent decomposition**  
→ PDF p. 346 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Backward score motor and adjoint S–A split**  
→ PDF p. 347 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**S–A signature velocity**  
→ PDF p. 348 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Two-flow dynamics of the S–A decomposition**  
→ PDF pp. 349–352 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The S–A/signature diagnostic**  
→ PDF p. 353 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**BERT/SARS S–A maps revisited**  
→ PDF pp. 354–355 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Detailed reading of the SARS v8 trace**  
→ PDF pp. 356–357 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**S–A interventions**  
→ PDF pp. 358–359 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**S–A redundancy and crowding**  
→ PDF p. 360 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Empirical status of the SARS v8 proof-of-mechanism run**  
→ PDF pp. 360–361 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Synthesis**  
→ PDF pp. 362–363 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch11"></a>
## 11. Signature Orbits and Training Dynamics

*PDF pp. 365–414*

How signatures form during training.

*Terms:* signature orbits, saturation, two-flow propagation, training traces, so(d) trajectories, emergence from initialization

**Signature Orbits: The Training-Time Object**  
→ PDF p. 366 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Saturation, Slack Tightening, and Two-Flow Propagation**  
→ PDF p. 367 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Empirical Orbit Atlas: Two SARS Training Traces**  
→ PDF pp. 367–372 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Layer-Wise View: Setup and Observables**  
→ PDF p. 373 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Trajectory of Ma(h,l) in so(d)**  
→ PDF pp. 374–381 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Emergence of the S–A Canonical Map from Random Initialisation**  
→ PDF pp. 382–386 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Residual Amplification Mechanism**  
→ PDF pp. 387–389 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Layer Rank Decay and the Channel Destruction Cascade**  
→ PDF p. 390 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Residual Directional Energy: Definition and Properties**  
→ PDF pp. 391–395 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Many Small Heads vs One Large Head: a Computational Analysis**  
→ PDF pp. 396–399 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Empirical Predictions**  
→ PDF pp. 400–401 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Coherence Chain Revisited: A Causal Reading**  
→ PDF pp. 402–403 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Experimental Validation (Exp. 1–9)**  
→ PDF pp. 404–406 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Proofs**  
→ PDF pp. 408–412 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch12"></a>
## 12. Sharpness, Activation, and Silence

*PDF pp. 415–453*

When patterns sharpen, activate or fall silent.

*Terms:* sharpness, activation operator, silence criterion, eigenplanes, antisymmetric inevitability

**From orbits to emergence**  
→ PDF p. 415 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Sharpness of pattern emergence**  
→ PDF pp. 416–424 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The activation operator**  
→ PDF pp. 425–428 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The silence criterion**  
→ PDF pp. 429–432 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Subspace activation and eigenplanes**  
→ PDF pp. 433–436 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Antisymmetric inevitability for oriented tasks**  
→ PDF pp. 437–444 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Possible extensions**  
→ PDF pp. 445–450 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Synthesis and Handover**  
→ PDF pp. 451–453 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch13"></a>
## 13. Redundancy and Design Principles

*PDF pp. 454–504*

Redundant heads and design principles.

*Terms:* redundancy, orbit crowding, marginal value of a head, self-sufficiency, feed-forward width, design principles

**From activation to marginal value**  
→ PDF pp. 454–455 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Three notions of redundancy**  
→ PDF pp. 456–458 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Functional redundancy and silence**  
→ PDF pp. 459–460 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Orbit crowding**  
→ PDF pp. 461–463 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Marginal value of a head**  
→ PDF pp. 464–482 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A hierarchy of redundancies**  
→ PDF pp. 483–484 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Dictionary-geometric framework**  
→ PDF pp. 485–488 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Self-sufficiency and feed-forward width**  
→ PDF pp. 489–491 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Six design principles**  
→ PDF pp. 492–495 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A training criterion for pruning, compression, and growth**  
→ PDF pp. 496–498 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Bridge to the rationalised transformer**  
→ PDF p. 499 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Synthesis and Outlook**  
→ PDF pp. 500–504 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch14"></a>
## 14. The Rationalised Transformer

*PDF pp. 505–546*

A redesigned “rationalised” Transformer block.

*Terms:* rationalised transformer, separate symmetric/antisymmetric channels, FLOPs, universality, static design

**Why MHA+MLP is not rationalised**  
→ PDF pp. 505–506 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Design requirements**  
→ PDF pp. 507–508 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Rationalised Transformer block**  
→ PDF pp. 509–511 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Separate symmetric and antisymmetric update channels**  
→ PDF pp. 512–513 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Parameter and FLOP accounting**  
→ PDF pp. 514–515 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Universality and subsumption claims**  
→ PDF pp. 516–517 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Static control of the signature geography**  
→ PDF pp. 518–521 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A concrete static design recipe**  
→ PDF pp. 522–523 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Comparison with the standard block**  
→ PDF pp. 524–525 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A static programming interface for Transformer design**  
→ PDF pp. 526–528 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Fixed-position channel intervention experiment**  
→ PDF pp. 529–532 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Minimal empirical illustrations**  
→ PDF pp. 533–536 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Implementation variants and safeguards**  
→ PDF pp. 537–540 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Resolution of the architectural degrees of freedom**  
→ PDF pp. 541–542 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Bridge to INCRT**  
→ PDF pp. 543–546 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch15"></a>
## 15. INCRT I: From Static Rationalisation to Incremental Growth

*PDF pp. 547–592*

Growing a Transformer incrementally (INCRT I).

*Terms:* INCRT, incremental growth, controller, architectural events, stability

**From static rationalisation to incremental growth**  
→ PDF p. 547 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The original INCRT as an operational principle**  
→ PDF p. 548 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Dynamic variables**  
→ PDF pp. 548–549 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Visual summary of the core controller**  
→ PDF p. 550 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The INCRT state**  
→ PDF p. 551 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**From diagnostics to architectural events**  
→ PDF p. 552 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Growth, tracking, preservation, and termination**  
→ PDF pp. 552–554 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Stability of diagnostic estimates**  
→ PDF p. 555 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Coverage residual decrease under growth**  
→ PDF p. 556 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Directional-tail preservation**  
→ PDF p. 557 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Finite termination**  
→ PDF p. 557 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Why the four dynamic hypotheses are sufficient**  
→ PDF p. 558 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Alignment with training criteria**  
→ PDF p. 558 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Recovered core mechanisms from the original INCRT**  
→ PDF pp. 559–560 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Growth criteria**  
→ PDF p. 561 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Directional task complexity and minimal head count**  
→ PDF p. 562 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Convergence and homeostatic stability**  
→ PDF p. 563 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Initialisation and knowledge preservation**  
→ PDF p. 564 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A complete core algorithm**  
→ PDF p. 565 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Worked four-dimensional example**  
→ PDF p. 566 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**What INCRT is not**  
→ PDF pp. 566–567 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Lyapunov proof sketch for the core controller**  
→ PDF p. 568 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Implementation-level event templates**  
→ PDF p. 568 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Monitoring windows and two-time-scale operation**  
→ PDF p. 569 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Core relationship with training dynamics**  
→ PDF p. 570 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Failure-mode case studies**  
→ PDF p. 571 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Balance with INCRT II**  
→ PDF p. 571 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Geometric picture of the incremental cycle**  
→ PDF p. 572 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Phases of an INCRT trajectory**  
→ PDF p. 573 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Synthesis of the core chapter**  
→ PDF p. 573 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The core INCRT block**  
→ PDF p. 574 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The dynamic programming interface**  
→ PDF p. 574 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Minimal empirical illustration**  
→ PDF pp. 575–576 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Implementation of growth events**  
→ PDF pp. 577–578 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Safeguards against dynamic failure modes**  
→ PDF pp. 579–580 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Calibration of the dynamic controller**  
→ PDF pp. 581–582 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A toy trajectory**  
→ PDF p. 583 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A worked single-layer growth calculation**  
→ PDF p. 584 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Core empirical protocol**  
→ PDF p. 585 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**What is deferred to INCRT II**  
→ PDF p. 585 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Relationship with the original INCRT formulation**  
→ PDF p. 585 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Implementation checklist for a programmer**  
→ PDF p. 586 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Remaining conditional points inside the core chapter**  
→ PDF p. 587 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**From scalar residual diagnostics to signed residual geometry**  
→ PDF pp. 588–591 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch16"></a>
## 16. INCRT II: Extensions, Guarantees, and Applications

*PDF pp. 593–681*

INCRT extensions and guarantees.

*Terms:* compressed sensing bound, task drift, mixture of experts, architectural transfer, optimizers

**Role of the second INCRT chapter**  
→ PDF p. 593 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Static notation**  
→ PDF p. 594 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The compressed-sensing bound**  
→ PDF pp. 595–597 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The three-level framework**  
→ PDF pp. 598–607 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Persistent task drift and homeostatic equilibrium**  
→ PDF pp. 608–613 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Input-conditional task complexity and the optimal expert count**  
→ PDF pp. 614–617 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Architectural transfer between related tasks**  
→ PDF pp. 618–620 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Adaptive optimisers and the preconditioned gate**  
→ PDF pp. 621–624 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**PAC guarantees for architecture selection**  
→ PDF pp. 625–627 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Beyond orthogonal deflation**  
→ PDF pp. 628–629 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Single-time-scale dynamics and Polyak–Ruppert recovery**  
→ PDF pp. 630–634 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Indefinite task operators and the signed compressed-sensing bound**  
→ PDF pp. 635–638 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Signed spectral stabilisation and INCRT as architecture initialisation**  
→ PDF pp. 639–649 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Rank-adaptive heads and the count–rank invariant**  
→ PDF pp. 650–656 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Identifiability of the head decomposition**  
→ PDF pp. 657–661 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Deployment constraints: minimum budget and quantisation**  
→ PDF pp. 662–668 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**In-context learning and implicit task estimation**  
→ PDF pp. 669–673 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Diffusion models and the time-conditional task family**  
→ PDF pp. 674–679 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Conjectures exported to Volume II**  
→ PDF p. 680 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch17"></a>
## 17. Spectral Gate Dynamics: Degeneracy Regimes and the Unified Gate

*PDF pp. 682–725*

Spectral gate dynamics.

*Terms:* spectral degeneracy, bidirectional gate, finite precision, unified gate

**From continuous time to finite arithmetic**  
→ PDF pp. 682–684 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Numerical analysis of the bidirectional gate**  
→ PDF pp. 685–689 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Three regimes of spectral degeneracy**  
→ PDF pp. 690–695 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Classical spectral methods revisited**  
→ PDF pp. 696–702 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**A unified gate**  
→ PDF pp. 703–709 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Implications, worked examples, and bridge to MHB-G**  
→ PDF pp. 710–719 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Towards an optimiser-aware spectral gate**  
→ PDF pp. 720–722 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch18"></a>
## 18. Experimental Validation

*PDF pp. 726–762*

Experiments.

*Terms:* cross-task validation, proteome MLM pretraining, Euler-Lagrange control, geopolymer inverse design

**Signed-INCRT stabilisation regime: cross-task validation**  
→ PDF pp. 726–732 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Self-architecting MLM pretraining on a reference proteome**  
→ PDF pp. 733–742 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Self-architecting attention for Euler–Lagrange control**  
→ PDF pp. 743–751 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Self-architecting prototypes for inverse design of geopolymers**  
→ PDF pp. 752–761 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)


---

<a id="ch19"></a>
## 19. Anchored Multi-Head Bilinear Gating: The Recommended Architecture

*PDF pp. 763–791*

The recommended A-MHB-G architecture.

*Terms:* multi-head bilinear gating, symmetry audit, parameter analysis, INCRT-compatible growth

**Design tensions identified in this monograph**  
→ PDF p. 763 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The synthesis question**  
→ PDF pp. 764–765 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**The Multi-Head Bilinear Gated layer**  
→ PDF pp. 766–770 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Symmetry audit of MHB-G and A-MHB-G**  
→ PDF pp. 771–773 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Parameter and FLOPs analysis**  
→ PDF pp. 774–775 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**INCRT-compatible growth of A-MHB-G**  
→ PDF pp. 776–780 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Variants that close residual design questions**  
→ PDF p. 781 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Related work and position vs SOTA**  
→ PDF pp. 782–783 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Empirical illustration**  
→ PDF pp. 784–786 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**Resolved design issues and residual questions**  
→ PDF pp. 787–788 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

**From incremental growth to spectral architecture design**  
→ PDF p. 789 in [the PDF](https://drive.google.com/file/d/1X1ytTAhoZ4uERo5zD--HQrRZFMenrR0G/view)

