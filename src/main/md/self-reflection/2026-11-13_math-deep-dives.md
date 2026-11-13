---
title: Math Deep Dives
created: 2026-11-13
source: deep-dive reading sessions on papers and books (Oct–Nov 2026)
---

# Math Deep Dives

> Created: 2026-11-13 · Covers Oct–Nov 2026

These notes come from close readings of papers, preprints and books, mostly the AI-generated mathematics that appeared in autumn 2026. Each entry gives the claim, how it works, and what is still unsettled. Most of these results were weeks old when read and had **not** been independently refereed, so treat every "proof" below as a claim unless it says otherwise.

The Lean and formalization thread is long enough to have its own article: [Lean, Foundations, and the AI Formalization of Mathematics](https://vwulf.github.io/ettuge/FP/lean-ai-formalization).

---

<a id="ch1"></a>
## The OpenAI Math Release

**The openai/math repository: 722 manuscripts (Oct 2026)**
<https://github.com/openai/math>

In October 2026 OpenAI released 722 mathematics manuscripts written by an unnamed internal model. Only about 162 of them (roughly one in five) come with machine-checked Lean proofs. The repo has issues disabled and pull requests restricted to collaborators. A Lean proof certifies only the theorem as stated, not that the statement matches the intended claim, so statement fidelity is still a human job. The release drew a public statement, "A Severe Misalignment of AI in Mathematics", posted on Terence Tao's blog and signed by Scholze, Viazovska, Hairer, Maynard and Yu Deng. **[→ mathematics; cross-link → machine-learning-ai]**

---

**Which results got real attention**
<https://github.com/openai/math>

Coverage of the release went into detail on a handful of results: the Flint Hills series, Hadwiger–Nelson plane coloring, Turán/Zarankiewicz/Hill crossing numbers, matrix and integer multiplication, and Navier–Stokes blowup. Others (UGC, quasi-RH, special cases of BSD and Hodge) were only named in passing. Plane coloring and quasi-RH use unrelated machinery: Moser-spindle geometry for the first, analytic number theory for the second. **[→ mathematics]**

---

<a id="ch2"></a>
## Complexity Theory

**The Unique Games Theorem (entry 102)**
<https://github.com/openai/math>

This is a claimed proof of Khot's Unique Games Conjecture, announced on Oct 6, 2026. It does not go through Small-Set Expansion. It builds on the 2-to-2 games machinery (the Khot–Minzer–Safra inverse theorem), adds a new "latent alphabet gadget" to fix the completeness gap in earlier 2-to-2 approaches, and amplifies with Dinur–Steurer parallel repetition. The Lean development is about 478 files and 187k lines with no `sorry` or extra axioms, and it matches the paper's Theorem 1.1. The 50-page paper itself was unreviewed, and Dana Moshkovitz called it unreadable without AI help. If it holds, Goemans–Williamson's ≈0.878 for Max-Cut becomes unconditionally optimal, as does the factor 2 for Vertex Cover. No complexity classes collapse, because UGC is a hardness-of-approximation statement inside NP. **[→ algorithms-data-structures; cross-link → mathematics]**

---

**Semidefinite programming (background)**

SDP is the algorithmic side of UGC: Goemans–Williamson's Max-Cut rounding is an SDP. In practice SDPs show up in control theory, robotics and SLAM, quantum information, polynomial (sum-of-squares) optimization, signal processing and power-grid optimization. Practical workhorses include the Burer–Monteiro low-rank trick and the MOSEK, SCS and Clarabel solvers. **[→ algorithms-data-structures]**

---

**The Exponential Time Hypothesis is False (Oct 25, 2026)**
<https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026>

This is a claimed deterministic algorithm that counts the satisfying assignments of a fixed-width CNF formula in time poly(n+m)·2^O(n·√(log log n / log n)) and polynomial space. That would refute both ETH and SETH without implying P = NP. The technique combines sparsification with polynomial interpolation. Corollaries include subexponential counting of independent sets, colorings and perfect matchings, plus a superlinear circuit lower bound for E^NP. The paper cites the Unique Games Theorem as [Ope26].

The speedup carries over only through reductions that are nearly linear in size (slack up to about N·√log N). So Independent Set, Clique, Vertex Cover, q-Coloring, Circuit-SAT and sparse Exact Cover/Dominating Set/Set Cover inherit it. Hamiltonian Cycle/TSP and Subset Sum/Knapsack don't follow directly, because their encodings blow up. **[→ algorithms-data-structures]**

---

**MaxCut, Cayley graphs and cosine sums (Jin–Milojević–Tomon–Zhang)**
<https://arxiv.org/abs/2509.03490>

This paper is about Chowla's cosine problem: how far below zero a sum of cosines over N frequencies must dip. The bridge to graphs is a classical spectral fact from the 1970s: the eigenvalues of the Cayley graph of the frequency set are exactly the values that cosine sum takes. The authors' extremal result on MaxCut in K_r-free graphs says a graph with no very negative eigenvalue must be dominated by cliques. A translation argument (shift a clique by 1 and you get another clique) then rules out large cliques in the sparse Cayley graph. The result is a minimum below −N^(1/10), against Bedert's parallel Fourier-analytic −N^(1/7) and Chowla's conjectured −N^(1/2). UGC plays no role. The MaxCut here is extremal, in the Hoffman-bound sense, not hardness of approximation. **[→ mathematics; cross-link → algorithms-data-structures]**

---

<a id="ch3"></a>
## Number Theory

**Quasi-Riemann Hypothesis: zero-free region Re(s) > 7/8**
<https://github.com/openai/math>

There are two versions. A 199-page, Lean-checked proof gives a zero-free half-plane Re(s) > 7/8 for ζ and related L-functions. A shorter 49-page proof pushes this to 11/12, but it isn't formalized, and that shorter paper is the one experts (Radziwiłł, Sarnak, Lichtman, Sawin, Bloom) actually scrutinized.

A uniform 7/8 bound is enough to make most "assume RH" arguments unconditional (with weaker exponents). It rules out Siegel zeros, which makes Siegel–Walfisz and class-number bounds effective and settles Euler's idoneal numbers. Conditional results built on the existence of Siegel zeros (Heath-Brown on twin primes, Friedlander–Iwaniec) become vacuous. **[→ mathematics]**

---

**Prime gaps: what RH does and doesn't buy**

The bounded-gap record stood at 240 (Stadlmann, Aug 2026), with unconfirmed claims of 236, 212 and 186. *Small* gaps depend on level-of-distribution estimates, which RH doesn't touch. *Large* gaps depend on zero-density estimates, which RH or quasi-RH do help. The real obstruction to twin primes is the sieve parity barrier, not where the zeros are. Montgomery's pair-correlation conjecture is a separate, heuristic link between zero spacing and prime correlations. **[→ mathematics]**

---

**Goldbach: state of play and generalizations**

The ternary (weak) conjecture is settled: Vinogradov proved it for sufficiently large n, and Helfgott finished it. The binary conjecture rests on Chen's theorem (p + P₂), exceptional-set density bounds, and verification up to 4×10¹⁸. GRH or quasi-RH sharpens the exceptional-set bounds but doesn't beat the minor-arc and parity obstacles. That is part of why Goldbach isn't a Millennium problem: RH was kept as the "root" problem from Hilbert's 8th. Generalizations include sums of s primes for s ≥ 3, Waring–Goldbach, Linnik's approximations, Green–Tao–Ziegler linear systems, function-field analogues and thin prime sets. Asking that *every* n be a sum of two primes fails for odd n whenever n − 2 is composite, with 11 as the first failure. **[→ mathematics]**

---

<a id="ch4"></a>
## Mathematical Physics (Millennium Problems)

**Navier–Stokes finite-time blowup, forced case (Sep 2026)**
<https://github.com/openai/math>

OpenAI claimed that smooth 3D Navier–Stokes flow can blow up in finite time, with an analytic proof and a Lean formalization. It was produced by about 10,000 coordinating agents over 88 hours. The catch is *external forcing*: the Clay problem asks about the unforced equations. There is a parallel dispute over credit. Buckmaster and Alpöge separately proved blowup for 3D incompressible Euler with AI assistance, and Euler is the easier target because it has no viscosity to resist blowup. Both proofs exploit forcing but construct the force differently. The OpenAI paper was revised to cite Córdoba and Martínez-Zoroa. **[→ mathematics-science]**

---

**Yang–Mills existence (OpenAI, Oct 26, 2026)**
<https://github.com/openai/math>

The Clay problem has two halves, existence and mass gap. The OpenAI claim covers existence only, and the proofs were initially withheld pending review by a panel that included Gross, Douglas, Jaffe, Klebanov and Nekrasov. Peter Woit and an advisory group on mathematics and AI pushed back on the framing and the withholding. The proof was later released as a roughly 1M-line Lean development (see the Lean article). **[→ mathematics-science]**

---

**Completing Bałaban's program for SU(2) Yang–Mills (Sussman, Alpöge, Claude)**
<https://github.com/ethanwsussman/Yang--Mills-LLM-experiment>

This 153-page LLM-assisted manuscript (Oct 6, 2026) completes Bałaban's 1980s renormalization-group program. It gives a lattice construction, continuum limits on tori and ℝ⁴, and satisfies the Osterwalder–Schrader axioms. It does not address the mass gap, has no Lean formalization, and the authors acknowledge gaps. It is probably the "completed Bałaban argument" Woit speculated OpenAI's approach resembles. **[→ mathematics-science]**

---

<a id="ch5"></a>
## Books and Formalization

**Emily Riehl, *Category Theory in Context* and *Elements of ∞-Category Theory* (with Verity)**
<https://emilyriehl.github.io/files/cosmos-project.pdf>

*Category Theory in Context* has no complete Lean formalization; a hobbyist companion covers only part of Chapter 1. Mathlib's 1-category library already holds most of the book's content, so what's missing is the exercises and the order of presentation. The ∞-cosmos project (Riehl, Carneiro, Verity, since 2024) follows *Elements*. It axiomatizes ∞-categories in Lean, while a separate synthetic track lives in Rzk (simplicial HoTT). A side result by Carneiro and Riehl ([arXiv:2503.20704](https://arxiv.org/abs/2503.20704)) is the first formal proof that the nerve functor is a fully faithful right adjoint and that Cat is cocomplete. **[→ mathematics-science; cross-link → scala-functional-programming]**

---

**Textbooks as formalization targets**

Meta's ATLAS (May 2026) autoformalized 26 open textbooks, mostly MIT lecture notes, at 71% of target statements overall. Analysis texts came out near complete, while Lie theory, algebraic geometry and manifolds stalled. Other books in the same thread: Tao's *Analysis I* (a Lean companion), Niu & Spivak's *Polynomial Functors*, CLRS (the first milestone for CSLib), and Bird & Gibbons's *Algorithm Design with Haskell* (a Lean adaptation). Details are in the [Lean article](https://vwulf.github.io/ettuge/FP/lean-ai-formalization). **[→ books-literature; cross-link → algorithms-data-structures]**
