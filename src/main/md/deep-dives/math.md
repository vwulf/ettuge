---
title: Math Deep Dives
created: 2026-11-13
updated: 2026-11-13
source: deep-dive reading sessions on papers and books (Oct–Nov 2026)
---

<a id="ch1"></a>
# Math Deep Dives

> Created: 2026-11-13 · Covers Oct–Nov 2026

These notes come from close readings of papers, preprints and books, mostly the AI-generated mathematics that appeared in autumn 2026. Each entry gives the claim, how the argument works, and what is still open. Most of these results were days or weeks old when they were read and had **not** been refereed, so read every "proof" below as a claim unless the entry says otherwise. Where a repository or PDF was read directly rather than through press coverage, the entry says so.

**Related pages on this site**
- [Lean and AI Formalization](https://vwulf.github.io/ettuge/FP/lean-ai-formalization): Lean's foundations, how much mathematics is formalized, kernel trust, and the case studies (graph isomorphism, Aaronson–Ambainis, Mordell, the Yang–Mills Lean release).
- [Proof and Formalization](https://vwulf.github.io/ettuge/FP/bucket-proof-formalization): short gists on the same theme.
- [Papers](https://vwulf.github.io/ettuge/Books/Papers): the catalogue entries (marked 🔍) for each paper discussed here, under [Analysis and Linear Algebra](https://vwulf.github.io/ettuge/Books/Papers#analysis-and-linear-algebra), [Discrete Mathematics and Combinatorics](https://vwulf.github.io/ettuge/Books/Papers#discrete-mathematics-and-combinatorics), [Category Theory](https://vwulf.github.io/ettuge/Books/Papers#category-theory), [Foundations and Logic](https://vwulf.github.io/ettuge/Books/Papers#foundations-and-logic), [History of Mathematics](https://vwulf.github.io/ettuge/Books/Papers#history-of-mathematics) and [Theory of Computation](https://vwulf.github.io/ettuge/Books/Papers#theory-of-computation).
- [Deep Dives](https://vwulf.github.io/ettuge/Deep-Dives/): the cross-topic index of deep dives.
- [Ellara Kannada Deep Dives › ಎ-ಎಣಿಕೆ](https://vwulf.github.io/ettuge/Deep-Dives/ellara-kannada/ch6): the one-operator (eml) result and its Kannada notation.

**Contents**
1. [The OpenAI math release](ch1)
2. [Complexity theory](ch2): Unique Games, semidefinite programming, the ETH refutation, Chowla's cosine problem
3. [Number theory](ch3): the quasi-Riemann hypothesis, Siegel zeros, prime gaps, Goldbach
4. [Millennium problems in mathematical physics](ch4): Navier–Stokes, Yang–Mills
5. [Books and formalization](ch5)
6. [Themes across the deep dives](ch6)

---

## 1. The OpenAI math release

**On Oct 6, 2026 OpenAI published 722 manuscripts in 372 families, and only about one in five came with a machine-checked proof.**
<https://github.com/openai/math>

The `openai/math` repository appeared with 722 manuscripts grouped into 372 families. They were written by an internal model that OpenAI has not named, priced or put behind an API. The repo's own formalization manifest listed 162 entries, so roughly one manuscript in five had a Lean proof in the public tree. OpenAI itself says the results are at different stages of verification. Issues are disabled and pull requests are limited to collaborators, so outsiders can't report errors there.

Two distinctions run through every entry below:
- **"Published" is not "verified."** "OpenAI published 722 proofs" was true; "722 proofs were verified" was not.
- **A Lean proof certifies only the theorem as stated.** Someone still has to check that the formal statement is the claim people care about. That check is called *statement fidelity*.

A later count by Kevin Buzzard (Nov 12) found that about 45% of the papers (290) have *some* Lean code, but about 38 of those don't state or prove the paper's main theorem. Three papers without Lean were retracted over a sign error. Details are in [Lean and AI Formalization › Open-problem releases](https://vwulf.github.io/ettuge/FP/lean-ai-formalization). Quanta's count of 377 results, against the repository's 372 families, has never been reconciled. **[→ mathematics; cross-link → machine-learning-ai]**

---

**Twenty-five Fields medalists, Tao among them, warned that the race for headline results is harming mathematics.**
[Papers › History of Mathematics](https://vwulf.github.io/ettuge/Books/Papers#history-of-mathematics)

"A Severe Misalignment of AI in Mathematics" appeared on Terence Tao's blog on Sep 11, a month before the big release. Its signatories include Scholze, Viazovska, Hairer, Maynard and the 2026 medalist Yu Deng. The argument is that labs announcing solutions to famous problems swamp referees and reward headlines over understanding. The October release made the point concrete. Dana Moshkovitz said the Unique Games manuscript was unreadable without AI help. Radziwiłł said both quasi-RH papers would be rejected at any journal for their writing. **[→ mathematics]**

---

**Only six results got real mathematical attention in the popular coverage; the rest were one-line claims.**

A widely shared video walkthrough of the release was checked line by line against sources. It treated six results in some depth:

| Result | Claim | How the argument goes |
|---|---|---|
| Flint Hills series ∑ 1/(n³ sin² n) | Converges, to about 30.31 | Convergence depends on the irrationality exponent μ(π); the series spikes at n = 22 and 355 because 22/7 and 355/113 approximate π so well. The paper claims μ(π) = 2, well under the 2.5 needed. |
| Hadwiger–Nelson (colouring the plane) | 5 colours are not enough, so the answer is 6 or 7 | Smooth an arbitrary colouring, apply a 60° rule on unit circles, find flower-shaped regions limited to 3 colours, then fit a Moser spindle (which needs 4) inside one. De Grey's 2018 lower bound was 5. |
| Turán brick factory, Zarankiewicz, Hill | Exact crossing numbers for complete bipartite and complete graphs, with Lean | Two closed curves in the plane cross an even number of times; this parity fact is encoded as algebraic test polynomials. |
| Matrix multiplication | ω ≤ 9/4 | Roughly 30 times the progress of the previous 36 years. First an 83-page messy proof, then eight days later a clean 13-page version with Lean. The self-rewrite is the most interesting signal in the release. |
| Integer multiplication / FFT | Slightly below n log n | Follows Karatsuba, Schönhage–Strassen and Harvey–van der Hoeven, then shaves 1/2¹⁸² off the log exponent. A galactic algorithm: it only helps for numbers too large to store. |
| Navier–Stokes blowup (forced) | Finite-time singularity | Lots of narrative, little mathematics; see [§4](ch4). |

Everything else was named with a one-line claim, including UGC, quasi-RH, BSD and Hodge special cases, Erdős's arithmetic-progression conjecture, Hilbert's 10th over ℚ, Hilbert's 16th, Artin's conjecture and the π exponent. The plane-colouring proof and quasi-RH share no machinery. The first is geometric and topological (unit-distance graphs, the Moser spindle, boundary smoothing). The second is analytic number theory (zero detectors, families of L-functions). **[→ mathematics]**

---

<a id="ch2"></a>
## 2. Complexity theory

**The Unique Games proof doesn't go through Small-Set Expansion; it repairs the 2-to-2 route with a new nonlinear gadget.**
[Papers › Theory of Computation](https://vwulf.github.io/ettuge/Books/Papers#theory-of-computation) · <https://github.com/openai/math> (entry 102, read directly)

Entry 102 is "The Unique Games Theorem" (dated Sep 23) plus four companion papers on Max-Cut, Vertex Cover, Min-UnCut and directed feedback vertex set. The model wasn't asked to prove UGC. It was asked to show, without assuming UGC, that the basic SDP threshold is optimal for every CSP, and it reached UGC along the way.

**What's proved.** For any fixed ε, δ < 1/2 there is a deterministic polynomial-time reduction from 3SAT to unique games. Every constraint is a translation a(v) = a(u) + c over K = F₂ˢ, and the constraint graph is simple and bipartite. Satisfiable formulas give games with value ≥ 1 − ε, and unsatisfiable ones give value ≤ δ.

**The skeleton:**
1. **Outer game.** Start from Håstad's hardness for parity equations (nearly satisfiable versus about half satisfiable) and turn it into an equation-versus-variable projection game.
2. **The known obstacle.** The inner code is the Barak–Kothari–Steurer matrix shortcode behind the 2-to-2 theorem. Its test adds a random rank-one matrix and asks for the same answer, and honest answers survive only half the time. That is why 2-to-2 gave unique games with completeness ½, not near 1.
3. **The new idea: a latent alphabet gadget.** This is a space V ⊇ K with a map C: V → K that commutes with shifts by K, plus a noise distribution. The noise rarely changes C's value (probability ≤ p), yet any high-rank family of *linear* observations detects it with probability ≥ 1/8. It's built by recursively composing the quadratic map Q(x) = (x₂x₃, x₁x₃, x₁x₂) over F_{2^d}, with a rank potential that tracks how much linear information survives.
4. **Completeness.** Honest tables P ↦ C(Pz) fail the test with probability ≤ p/2. Folding over translation orbits and shared keys makes every constraint unique.
5. **Soundness.** A Fourier argument shows that passing the gadget test forces low-rank mass, so the table also passes the ordinary rank-one test. The Khot–Minzer–Safra inverse theorem from the 2-to-2 proof then gives agreement on a bounded slice. That agreement is decoded with correlated advice in the style of Khot–Safra and Minzer–Zheng. A "row-fiber abundance" lemma makes useful advice frequent, and sparse projection at rate β = k^(−2/3) leaves many clean coordinates.
6. **Amplification.** On unsatisfiable instances, Dinur–Steurer projection-game repetition on the clean coordinates bounds agreement by exp(−c·k^(1/3)), which contradicts the decoded lower bound.

**Verification.** The Lean target `theorem11` matches the paper's Theorem 1.1. The development is 478 files and about 187k lines, under `lean/OAI/Computability/UniqueGames/`. A grep found no `sorry`, `admit` or extra axioms. The Khot–Minzer–Safra inverse theorem, the PCP pipeline and the repetition bound are all formalized rather than assumed. The full Mathlib build and the Comparator check were not rerun. The repo's "reasoning summary" is abridged and editorialized, not the raw trace. **[→ algorithms-data-structures; cross-link → mathematics]**

---

**How to read the status: when read, the proof was a week old, Lean-verified, and not yet reviewed by any expert.**

OpenAI announced the proof on Oct 6 as part of the large release. It came with a Lean proof, but in an AI-generated manuscript with no human editing and no independent expert review. Dana Moshkovitz, who spent years working toward the conjecture, said she couldn't read it without AI help. The Lean certificate is strong evidence that *something* is proved. Experts still have to confirm that the formal statement really is UGC as people mean it. Everything below is conditional on that check, and on P ≠ NP. **[→ algorithms-data-structures]**

---

**If UGC holds, the approximation thresholds that were "UGC-hard" become plain NP-hard, so the best known algorithms become provably optimal.**

For two decades a long list of approximation results read "no polynomial-time algorithm does better than X, *assuming UGC*". A proof removes the assumption.

| Problem | Threshold that becomes NP-hard to beat | Source of the conditional result | What it means |
|---|---|---|---|
| Every Max-CSP with no perfect solution | The basic SDP plus rounding | Raghavendra 2008 | One generic algorithm is optimal for the whole class, and every CSP's approximation threshold is pinned down exactly |
| Max-Cut | ≈ 0.878 (Goemans–Williamson) | Khot–Kindler–Mossel–O'Donnell | The 1995 hyperplane-rounding algorithm cannot be improved |
| Vertex Cover | 2 − ε | Khot–Regev | The trivial algorithm (take both ends of a maximal matching) is optimal |
| Sparsest Cut, Balanced Separator, Multicut | No constant factor | various | Graph partitioning has no constant-factor approximation |
| Several scheduling problems | Tight bounds | various | Known algorithms are optimal |

Entry 102 ships four companion papers that derive these consequences directly: Max-Cut, Vertex Cover, Min-UnCut and directed feedback vertex set. That fits how the result came about. The model was asked to show, without assuming UGC, that the basic SDP threshold is optimal for every CSP. UGC was the route it found, not the target it was given. **[→ algorithms-data-structures]**

---

**The conceptual payoff is a "unified theory of approximability": a low-degree SDP becomes the provably best polynomial-time algorithm across a huge range of problems.**

- **SDP and Sum-of-Squares.** Raghavendra's theorem turns a single recipe, solve the basic SDP relaxation and round it, into the optimal algorithm for every CSP. Sum-of-Squares, the hierarchy of larger SDPs, can't do better in polynomial time either. This is the unified picture people hoped UGC would deliver.
- **Algorithm design.** Hard Unique Games instances still have a subexponential-time algorithm, exp(n^poly(ε)) (Arora–Barak–Steurer). So any reduction from SAT to Unique Games has to blow the instance up by a large polynomial whose degree grows as ε shrinks, or SAT itself would get a subexponential algorithm, contradicting ETH. (ETH itself was claimed false three weeks later; see the entry below. That claim, if it holds, removes this argument's premise but not the proof of UGC.) The proof's structure should show where that blowup happens.
- **Research directions.** Mark Braverman's point may matter most in the long run. If researchers can extract the key assumptions in the AI proof, varying them could open new directions, so the result isn't "one and done". **[→ algorithms-data-structures]**

---

**No complexity class changes; what changes is what an algorithm would mean.**

UGC says a gap version of Unique Games is NP-hard. That is a hardness statement *inside* NP, not a relation between classes, and it says nothing about P versus NP itself.

| | Before the proof | After |
|---|---|---|
| A polynomial-time algorithm beating Goemans–Williamson on Max-Cut, or 2 − ε on Vertex Cover | Would refute UGC | Would prove P = NP |
| The tight approximation thresholds | Conditional on UGC | As solid as NP-hardness itself |

Two further consequences describe NP or its running times without moving any class:
- **A new PCP characterization of NP.** Every NP language has a 2-query PCP whose tests are unique constraints. Like the PCP theorem, this describes NP in a new way without changing it.
- **Fine-grained structure.** The forced polynomial blowup above is a statement about running times, not about which class a problem is in. It also rules out Khot's suggestion that Unique Games might sit strictly between P and NP-complete, since the gap problem is now NP-complete.

The same release does claim a genuine class equality, **L = BPL** (randomized logspace equals deterministic logspace), which would complete a long derandomization programme. It doesn't follow from UGC, and like the rest of the release it was unreviewed. **[→ algorithms-data-structures]**

---

**Against Khot's own list of open problems, the proof settles two and leaves the rest open, because of the route it takes.**

Khot's talk on UGC listed open problems around the conjecture. With the proof's route in hand, each can be scored:

| Khot's problem | Status after the proof | Why |
|---|---|---|
| Intermediate complexity (from the Q&A): is Unique Games strictly between P and NP-complete? | **Settled: no** | The gap problem becomes NP-hard. The subexponential algorithm still stands, so the SAT reduction must have a large polynomial blowup. |
| OP 4: can higher-degree SDPs beat Goemans–Williamson on Max-Cut? | **Settled: no, unless P = NP** | A degree-K SDP is solvable in polynomial time for fixed K, so beating 0.878 with one would put NP in P. An *unconditional* Sum-of-Squares integrality-gap proof would still be a separate result. |
| OP 1: Small-Set Expansion | Open | SSE implies UGC, not the reverse, so proving UGC leaves the stronger conjecture and its graph families open. |
| OP 2 and 3: 2-Lin over ℝ, and the junta question | Open as statements | These were steps on Khot and Moshkovitz's proposed route to UGC. The reasoning summary shows the model tried that route, and subexponential/SSE algorithms, and set both aside. They matter less as a path to UGC but remain interesting in their own right. |
| OP 5: basic-SDP integrality-gap instances smaller than 2^K | Open | Knowing hard instances exist doesn't show small gap instances exist. |

The question that decided this table was which route the proof takes. Had it gone through Small-Set Expansion, or answered OP 1 or OP 3 along the way, more of the list would have fallen. It goes through 2-to-2 games and the latent alphabet gadget instead, so those problems are untouched.

Two corrections to the summary of the talk that was read alongside:
- **Time bounds:** n^O(log n) is quasi-polynomial time, not the Arora–Barak–Steurer subexponential bound exp(n^poly(ε)).
- **SSE statement:** the standard Small-Set Expansion statement compares "some δ-sized set expands ≤ ε" with "every δ-sized set expands ≥ 1 − ε". The summary's ½ may be Khot's simplification in the talk. **[→ algorithms-data-structures]**

---

**UGC covers only instances with no perfect solution; the perfect-completeness cousins were settled separately, one by hand.**

- **The 2-to-1 conjecture.** Khot posed this for instances where every constraint *can* be satisfied, which UGC doesn't address. OpenAI's release claims a proof of it too, again in an AI-generated manuscript with no human editing or expert review.
- **4-to-1, by hand.** In September, before the release, Fei, Minzer and Wang (Minzer's MIT group) raced out a proof of the weaker 4-to-1 version. It implies that 3-colourable graphs stay hard to colour even with any fixed number of extra colours, a decades-old open problem now settled without AI.
- **The race.** Quanta framed the episode as researchers racing the machines to the result. Minzer's group got its result out first; the AI release then claimed the full conjectures. **[→ algorithms-data-structures]**

---

**Semidefinite programming is the algorithmic half of the UGC story: it is provably the best possible algorithm in theory, and a niche tool in practice.**

An SDP optimizes over a symmetric matrix X ⪰ 0 subject to linear constraints. Equivalently, X is a Gram matrix with X_ij = ⟨v_i, v_j⟩. SDPs are convex, so they are solvable to any precision in polynomial time. For Max-Cut, relax each ±1 label to a unit vector and maximize Σ(1 − ⟨v_i, v_j⟩)/2 over the edges. Goemans–Williamson then round with a random hyperplane, and the guaranteed loss is the 0.878 factor. UGC makes "solve the basic SDP, then round" optimal for every CSP. Sum-of-Squares is the hierarchy of ever-larger SDPs.

In practice SDP scales poorly: an n×n matrix has about n² variables, and interior-point solvers struggle beyond a few thousand rows. It is used where problems are moderate in size or have exploitable structure:
- control theory (linear matrix inequalities, Lyapunov matrices), probably its biggest engineering use
- robotics and SLAM (SE-Sync's certifiably optimal pose graphs)
- quantum information (the NPA hierarchy, entanglement detection)
- polynomial optimization and verification (Sum-of-Squares certificates)
- signal processing and statistics (phase retrieval, matrix completion, nearest correlation matrices)
- power-grid optimal power flow relaxations

The usual workaround is Burer–Monteiro: write X = VVᵀ with a skinny V and optimize V directly. Common solvers are MOSEK, SCS and Clarabel, through CVXPY or JuMP. Real Max-Cut solvers rarely run Goemans–Williamson; local search usually beats 0.878 on practical instances. **[→ algorithms-data-structures]**

---

**The ETH refutation is a polynomial-method counting algorithm whose saving is only about √log n in the exponent: a theory result, not a faster SAT solver.**
[Papers › Theory of Computation](https://vwulf.github.io/ettuge/Books/Papers#theory-of-computation) · [paper.pdf](https://github.com/openai/math/tree/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026) (read directly)

Announced Oct 25–26 alongside claimed results on Kakeya/local smoothing and on QCD existence. The 67-page manuscript is dated Oct 17 and revised Oct 25. The Lean development is about 3,977 files and uses only the standard axioms (propext, Quot.sound, Classical.choice).

**The theorem.** A deterministic, polynomial-space algorithm exactly counts the satisfying assignments of any k-CNF (fixed k ≥ 2) in time poly(n + m) · 2^O(n·√(log log n / log n)). For sparse formulas (m ≤ Dn) the exponent is O(n/√log n). That is 2^o(n), so ETH falls, and with it SETH, since SETH implies ETH. Counting is harder than deciding, so this is a strong form. It doesn't give P = NP, because subexponential is still superpolynomial. It won't beat PPSZ-style O(1.307ⁿ) solvers at any realistic n, and the constants hidden in O_k(1) are probably enormous.

**How it works.**
- Sparsify to 3-CNF in which each variable appears in at most 3 clauses; variable copying extends this to general k.
- Turn each clause into a polynomial; their product has degree ≤ 3n. Recover the count by interpolation from sums over small groups of variables.
- Low-degree "replacement forms" and counting the common zeros of sparse polynomial systems do the rest. Appendix D sharpens the bound by tensor contraction.

This is the polynomial-method lineage (Williams and others), not local search.

**Corollaries.**
- Subexponential counting of independent sets, q-colourings and perfect matchings. For perfect matchings, which is permanent territory, the bound is 2^o(v+e).
- An εm-additive approximation of Max-k-SAT.
- An infinitely-often circuit lower bound of c·n·√log n gates for E^NP. That is superlinear for general fan-in-2 circuits and would be a big deal by itself.
- The paper cites "Unique Games Theorem [Ope26]", the entry above.

**What inherits the speedup.** A problem gets 2^o(N) only if it reduces *to* SAT with nearly linear blowup. The slack is about N·√log N, so N·log log N is fine and N·log N is not.

| Gets 2^o(N) | Doesn't follow directly |
|---|---|
| Independent Set, Clique, Vertex Cover (in vertices) | Hamiltonian Cycle / TSP: v² position variables, or v log v bits of connectivity certificate |
| q-Colouring, fixed q (qv variables) | Subset Sum / Knapsack: adders over the weights' bit length give n × bits variables |
| Circuit-SAT for linear-size circuits | Problems whose ETH lower bounds came from quadratic reductions (planar problems, edge-measured Clique) |
| Perfect-matching counting (in v + e) | |
| Exact Cover, Dominating Set, Set Cover (in incidences, or on sparse instances) | |

The key subtlety is that removing ETH deletes *lower bounds* for everything, but adds *algorithms* only where the reduction runs X → SAT linearly. The 2^Ω(n) lower bound for Subset Sum disappears, yet no 2^o(n) Subset Sum algorithm follows. Ryan Williams flagged it as a claimed refutation, and OpenAI handed it to complexity experts. The formal statement reportedly fixes the machine per k and counts real machine steps, which answers the usual "is the Lean statement really ETH?" worry. **[→ algorithms-data-structures]**

---

**Chowla's cosine problem fell to extremal MaxCut on Cayley graphs, not to Unique Games.**
[Papers › Discrete Mathematics and Combinatorics](https://vwulf.github.io/ettuge/Books/Papers#discrete-mathematics-and-combinatorics) · [arXiv:2509.03490](https://arxiv.org/abs/2509.03490)

Chowla asked how far below zero a cosine sum Σ cos(a_i x) over N distinct frequencies must dip. The bridge to graphs is a spectral fact known since the 1970s: the eigenvalues of the Cayley graph of the frequency set are exactly the values the cosine sum takes, so its smallest eigenvalue measures how low the sum goes. Jin, Milojević, Tomon and Zhang's new input is extremal: a K_r-free graph with no very negative eigenvalue must be dominated by cliques. Ilya Shkredov noticed that this left only large cliques in the Cayley graph to rule out. Tomon did that with a translation argument: shifting a clique by 1 gives another clique, and eventually there are more edges than the sparse Cayley graph can hold.

| Bound on the minimum | Source |
|---|---|
| below −N^(1/10) | Jin–Milojević–Tomon–Zhang (graph-theoretic) |
| below −N^(1/7) | Bedert, parallel Fourier-analytic proof ([arXiv:2509.05260](https://arxiv.org/abs/2509.05260)) |
| −N^(1/2) | Chowla's conjecture |

Why it's easy to confuse with UGC: MaxCut is UGC's most famous problem. But UGC is about the *computational hardness* of approximating MaxCut. This work is about *extremal bounds*: how large the MaxCut of every K_r-free graph must be. That is closer to Hoffman's eigenvalue bounds than to PCPs or Fourier analysis on the hypercube. **[→ mathematics; cross-link → algorithms-data-structures]**

---

<a id="ch3"></a>
## 3. Number theory

**The quasi-Riemann hypothesis exists as two documents: a long Lean-checked proof of 7/8 and a short human-read proof of 11/12.**
[Papers › Analysis and Linear Algebra](https://vwulf.github.io/ettuge/Books/Papers#analysis-and-linear-algebra)

The main paper is entry 003 of the Oct 6 release, dated Sep 30, 199 pages. It claims that all Dirichlet L-functions and all finite-order Hecke L-functions over ℚ(√−3) have no zeros with Re s > 7/8, which includes ζ. A 49-page companion pushing the bound to 11/12, dated Oct 5, is the only one of the 722 manuscripts that a human edited, and OpenAI won't say who. OpenAI also names this result (with Hodge for CM abelian varieties) as one of two exceptions to its standard automated procedure, so "the AI did it alone" overstates OpenAI's own account.

**Verification.** An independent rerun (davegoldblatt/openai-zeta-proof-check, Oct 7) reports acceptance by two kernels using only the standard axioms, about 2,900 files and 500k lines. The Lean scope covers the 7/8 statements for ζ, Dirichlet and finite-order Hecke L-functions. The paper's later applications are outside it, so Euler's idoneal numbers and the square-root algorithms are not machine-checked. Since 7/8 < 11/12, the 11/12 *statement* follows from the checked one in one line. What isn't checked is the 11/12 *argument*, which is the one mathematicians are reading. The short proof may well be harder to formalize, not easier. It leans on cited results Mathlib lacks: Heath-Brown's large sieve, Kubota–Patterson theory of the cubic theta function, and the Dunn–Radziwiłł formula. It also centres on metaplectic forms (automorphic forms on a cover of GL₂ over ℚ(√−3)), which Mathlib barely has.

**How it works, as a sketch.** Hide the walk Σ μ(n)χ(n) inside a family of L-functions and count its sixth-power "echoes". Littlewood's criterion then gives A ≤ x^(11/12). The height of a zero never enters, which is why this wall, unlike de la Vallée-Poussin's or Vinogradov–Korobov's, doesn't thin out as you go up the strip. The key family uses cubic Gauss sums. Sarnak had argued for decades that RH should be attacked through families. This one had been overlooked (Iwaniec narrowly missed it in 2002), and it depends on Dunn's metaplectic work and a 2021 Dunn–Radziwiłł formula that resolved Kummer's cubic Gauss sum bias. Specialists had assumed their toolkit was too weak, and the model bet that it wasn't. Baiying Liu's follow-up ([arXiv:2610.12234](https://arxiv.org/abs/2610.12234)) already nudges 7/8 by retuning two parameters (b = 1/8, ℓ = 1/6).

**Reaction after two weeks** (Quanta, Oct 19):
- Radziwiłł can sketch the argument in half a page, and private write-ups of 7 to 13 pages circulate.
- Sarnak is teaching it this semester but won't call it a theorem until humans check every detail.
- Lichtman calls it the most significant AI-for-math result so far.
- Sawin expects full RH to feel as far off as before. Bloom notes people said the same about quasi-RH a few weeks earlier. **[→ mathematics]**

---

**A wall at 7/8 is enough for most "assume RH" proofs, because they need a power saving, not the exact line 1/2.**

The explicit formula writes prime counts as a main term plus waves x^ρ, one per zero, each of size x^(Re ρ). The classical zero-free region narrows with height and saves only about exp(√log x). A fixed wall caps every wave, giving for example ψ(x) = x + O(x^(7/8+ε)). Any power saving δ > 0 lets most arguments run; RH gives δ = 1/2 and this gives δ = 1/8. The half-plane holds for every Dirichlet L-function at once with no exceptional zero. So primes in progressions mod q get power-saving errors that stay useful while q is a small power of x.

| Becomes unconditional (weaker exponents) | Still needs exactly 1/2 |
|---|---|
| Least quadratic non-residue polylogarithmic in p, so square roots mod p in deterministic polynomial time | Square-root error terms such as \|π(x) − li(x)\| ≪ √x log x |
| Deterministic Miller–Rabin with polylog(n) witnesses | Primes in [x, x + √x log² x] (the wall gives longer intervals) |
| Bounds such as ζ(s) ≪ t^ε, and on 1/ζ and log ζ, right of 7/8 | Lindelöf at s = 1/2, zero-spacing statistics, moments |
| Effective class-number bounds (no Siegel zeros) | Anything needing the zeros *on* the line |

**[→ mathematics]**

---

**Siegel zeros weren't attacked head-on; they fall out because the new method never uses positivity near s = 1.**

A Siegel zero would be a single real zero β of L(s, χ), for a real character χ mod q, lying within about c/log q of 1. It survived a century because the classical zero-free region comes from the positivity of 3 + 4cos θ + cos 2θ, which compares L(σ, χ₀)³ L(σ, χ)⁴ L(σ, χ²). For a real χ, χ² is principal, so the third factor is essentially ζ with its pole at 1. That pole masks a real zero near 1, and every improvement built on positivity inherits the blind spot. The new proof caps Σ μ(n)χ(n) at about x^(7/8) for every character, real or complex. A zero at β would force growth like x^β. Dirichlet characters lift to ℚ(√−3), where the L-function factors as L(s, χ)·L(s, χχ₋₃). So a Dirichlet zero beyond 7/8 would be a Hecke zero in the forbidden half-plane. This Dirichlet statement is inside the Lean scope.

| Kind of result | What happens |
|---|---|
| "Assume no Siegel zeros" | Unconditional and often effective: Siegel–Walfisz gets a computable constant; class numbers get effective d^(1/2−ε) bounds, so listing fields of class number h becomes finite for every h (Watkins had reached h = 100); Euler's 65 idoneal numbers are complete (Weinberger 1973 had shown at most one could be missing, and only via a Siegel zero) |
| Case-split proofs | The exceptional branch, which used Deuring–Heilbronn repulsion, is dead code. Linnik's least-prime theorem is the textbook example, and constants may improve. |
| "Assume Siegel zeros exist" | Vacuous, not false: Heath-Brown 1983 (twin primes), Friedlander–Iwaniec (distribution past √x), Tao–Teräväinen 2021 (Chowla-type correlations). The win–win route to twin primes is closed. |

**[→ mathematics]**

---

**Bounded prime gaps are driven by the level of distribution, so RH and quasi-RH don't help; large gaps are where zeros matter.**

| Bound | Who, when | Status |
|---|---|---|
| 246 | Polymath8b, 2014 | Classic record, now formalized in Lean |
| **240** | Stadlmann, Aug 31, 2026 | The smallest step down (49-tuple instead of 50), with lower-degree polynomials; the method may go further |
| 236 | Kintali, Sep 1 | Human-directed, several AI systems |
| 212 | Axiom Math, Sep 3 | Claimed, with a Lean certificate of the deduction |
| 186 | Sep 2–3 | Conditional on three unproved Lean axioms (Kloosterman estimates and a numerical certificate); attributions conflict |
| 12, then 6 | Under Elliott–Halberstam and its generalization | 6 is the sieve's floor because of the parity barrier |

Sieve bounds need primes equidistributed mod q *on average* over q ≤ x^θ. GRH gives θ = 1/2 per modulus, and Bombieri–Vinogradov already gives θ = 1/2 on average unconditionally ("GRH on average"). So GRH buys nothing beyond 246. Elliott–Halberstam (θ → 1) isn't implied by GRH, and progress past 1/2 (Zhang, Stadlmann) comes from Kloosterman sums and the dispersion method. A wall at 7/8 controls only q up to about x^(1/8) pointwise.

*Large* gaps run the other way. Under RH, p_{n+1} − p_n ≪ √p log p (Cramér 1920). Unconditionally the record is p^0.525 (Baker–Harman–Pintz 2001). The route is zero-density estimates, improved by Guth–Maynard (2024) to give primes in almost all intervals of length about x^(2/15). With nothing right of 7/8, the worst range in Ingham's method is empty, so a small improvement may follow. Nobody seems to have worked it out yet.

The deeper point: RH controls how far primes drift from their average density, while twin primes are about *correlations*. Zero locations can't see correlations. Montgomery's pair-correlation conjecture, about the *spacing* of zeros, is linked through Goldston–Gonek–Montgomery to primes in short intervals, and Hardy–Littlewood constants appear there. That is a heuristic link and an equivalence of conjectures, not a route to a proof. The real wall is the parity barrier: sieves can't tell an odd number of prime factors from an even one. Breaking it takes input of the Friedlander–Iwaniec x² + y⁴ kind, a separate problem from RH. **[→ mathematics]**

---

**Goldbach sits exactly at the threshold between two summands and three: with a spare variable to average over, the problem becomes tractable.**

**Where it stands.**
- **Ternary Goldbach is solved:** Vinogradov (1937) for large odd n, then Helfgott (2013) for every odd n > 5.
- **Binary Goldbach is open:** the closest result is Chen (1973), p + P₂. The possible exceptions have density zero (Montgomery–Vaughan, later Pintz), and the conjecture is verified up to 4×10¹⁸ (Oliveira e Silva and others, 2013).

**RH helps only partly.** Under GRH, Hardy–Littlewood showed the exceptional set is ≪ N^(1/2+ε). A quasi-GRH gives a weaker power saving of the same kind. Ternary Goldbach was proved under GRH in 1997 (Deshouillers, Effinger, te Riele, Zinoviev) before Helfgott removed the assumption. With two primes, though, the minor arcs can only be bounded on average (L²), so the method gives "almost all", never "all". Zeros don't touch that, and the sieve's parity problem is why Chen stops at P₂.

**Why it isn't a Millennium problem.** Clay chose problems that are central to whole fields. Goldbach is seen as isolated, and RH, the root of Hilbert's 8th problem (RH, Goldbach and twin primes), already stands for the cluster. Faber & Faber offered its own $1M in 2000 for the novel *Uncle Petros and Goldbach's Conjecture*; it expired unclaimed in 2002.

**The family of generalizations.** Heuristically, n has about n^(s−1)/(log n)^s representations as a sum of s primes. For s = 1 that tends to 0, so it fails at every composite. For s = 2 it grows, but there's no spare variable to make it rigorous. For s = 3 there's room for the circle method.

| Variant | Status |
|---|---|
| Sums of s ≥ 3 primes | Solved; every integer > 1 is a sum of at most four primes, and Goldbach is equivalent to "at most three" (Schnirelmann's line) |
| Waring–Goldbach (k-th powers of primes) | Hua 1938: 2^k + 1 suffice; five squares of primes done, four still open |
| Linnik (two primes plus K powers of 2) | K = 8 (Pintz–Ruzsa) |
| Linear systems in primes | Green–Tao–Ziegler for finite complexity; binary Goldbach and twin primes have infinite complexity |
| Function fields F_q[t] | Ternary versions (Effinger–Hayes); the function-field RH is Weil's theorem |
| Thin prime sets | Ternary still holds for Piatetski-Shapiro and digit-restricted primes |

"Every n is a sum of two primes" fails for odd n whenever n − 2 is composite. 11 is the first failure, followed by 17, 23, 27, 29, 35, 37. Almost all odd numbers fail, which is why the conjecture is stated for evens. **[→ mathematics]**

---

<a id="ch4"></a>
## 4. Millennium problems in mathematical physics

**OpenAI's Navier–Stokes blowup is for the forced equations, and the credit question turned on whether it used the same loophole as Buckmaster and Alpöge.**
[Papers › Analysis and Linear Algebra](https://vwulf.github.io/ettuge/Books/Papers#analysis-and-linear-algebra)

On Sep 8, 2026 OpenAI claimed that smooth 3D Navier–Stokes flow can blow up in finite time. It came with an analytic proof and a Lean formalization, produced by about 10,000 coordinating agents over 88 hours. The catch is an external forcing term. Forced blowup does correspond to two of the four alternatives in Clay's official statement, but the problem is officially unsolved. A solution must appear in a refereed journal and survive two years after acceptance before a committee meets, and OpenAI says it won't take the money.

**Why Buckmaster–Alpöge isn't a candidate.** On Aug 15, using Anthropic and OpenAI models, Tristan Buckmaster and Levent Alpöge proved finite-time blowup with smooth forcing for the incompressible porous media, Boussinesq and 3D incompressible Euler equations. Euler is Navier–Stokes *without* viscosity. Viscosity dissipates energy and smooths flows, so Euler is the easier target. Buckmaster also claims a result for low-dissipation Navier–Stokes, held back until Lean verification is done, but that weakens the viscosity term too. Tao called the work "a remarkable achievement" and saw no obvious obstacle to reaching Navier–Stokes.

**The credit dispute.** At launch OpenAI officials said their proof followed the "Spanish program", the Córdoba–Martínez-Zoroa forcing approach that Buckmaster and Alpöge also used. Scientific American (Oct 2026) concluded instead that both proofs exploit the same loophole, the allowance for a force, but construct that force differently, so the resemblance is superficial. The paper did change: a 166-page revision added the Córdoba and Martínez-Zoroa citations after Buckmaster's criticism. Alpöge still sees a closer match to another Euler proof of theirs. Since an LLM's reasoning can't be fully inspected, the credit question is likely to stay open.

**Follow-ups.** "Density of Forces Producing Navier–Stokes Blowup" (Sep 22, [arXiv:2609.26790](https://arxiv.org/abs/2609.26790)) builds on the result. Cheskidov, Dai and Palasek's cascade mechanisms ([arXiv:2609.17642](https://arxiv.org/abs/2609.17642)) prove unforced blowup for a dyadic model. A separate effort asks whether the leading-order profile can be computed and tied to an experiment. The open frontier is the unforced case. For the machine-learning side of the same equations, see [Fourier Neural Operators](https://vwulf.github.io/ettuge/Books/Papers#deep-learning) in the catalogue. **[→ mathematics-science; cross-link → machine-learning-ai]**

---

**OpenAI claims only the existence half of Yang–Mills; the mass gap, which the Clay prize requires, isn't claimed.**

Yang–Mills is the non-abelian gauge theory under the Standard Model: a connection on a principal G-bundle, with G = SU(3) for the strong force. The Clay problem has two parts. **Existence** asks for quantum Yang–Mills on ℝ⁴ satisfying the Wightman or Osterwalder–Schrader axioms. **Mass gap** asks for a proof that the lightest excitation (a glueball) has positive mass, which is why the strong force is short-range. Most experts consider the mass gap the hard part.

| Date | Milestone |
|---|---|
| Sep 9, 2026 | Natural-language existence proof generated |
| Sep 18 | QCD-related proof (Yang–Mills plus quarks, beyond the Clay problem) |
| Oct 16 | Lean formalization finished |
| Oct 26 | Announced with Kakeya/local smoothing and the ETH refutation; artifacts withheld for a panel of David Gross, Douglas, Jaffe (who co-wrote the Clay statement with Witten), Klebanov and Nekrasov |
| Nov 11 | Panel releases the Lean source only (~986K lines, 9,477 files), with no written proof |

**Reactions.** Baez: potentially huge and a big first step, but not the prize. Peter Woit called omitting the mass gap "intentionally deceptive". He also noted that merely completing Bałaban's argument on a compact torus would be much weaker than it sounds. The Advisory Group on Mathematics and AI demanded immediate release of the proofs. The standing worry is statement fidelity: does the Lean statement encode the OS axioms on ℝ⁴, the right gauge groups and a non-trivial continuum limit?

The November release, and Armstrong's and Hairer's efforts to reverse-engineer a readable proof from it, are covered in [Lean and AI Formalization › November 2026](https://vwulf.github.io/ettuge/FP/lean-ai-formalization). Armstrong's map shows that about 70% of the code is a Bałaban-type ultraviolet renormalization group. The release ran on Lean v4.32.0, which predates the kernel fixes, and no independent kernel had been run. **[→ mathematics-science]**

---

**The Sussman–Alpöge repository is a conditional, openly gappy, Claude-written completion of Bałaban's program for SU(2): the likely shape of what OpenAI did, published three weeks earlier.**
<https://github.com/ethanwsussman/Yang--Mills-LLM-experiment> (read directly)

Ethan Sussman proposed the project and Levent Alpöge guided Claude through it; the repo is dated Oct 6, 2026. Bałaban's 1985–89 renormalization-group papers are a roadmap to existence, abandoned because finishing them needed more work than seemed humanly feasible. The bet is that LLMs can supply that work. As a warm-up, Codex reproduced Dimock's QED3 construction and extended it to infinite volume with the OS axioms; the authors believe it is essentially correct. A YM3 folder covers the easier 3D case.

**"Theorem 0"** (a 153-page draft), for SU(2) with Wilson's lattice action on periodic tori:
- running-coupling bounds matching the one-loop asymptotic-freedom law
- correlation bounds uniform as the cutoff is removed
- continuum limits on tori and on ℝ⁴. On ℝ⁴ these satisfy OS regularity, reflection positivity, and translation and hypercubic invariance, which gives a Hilbert space with a vacuum and a non-negative Hamiltonian.
- non-triviality: the connected two-point function of tr F² scales like g(d)⁴, so the limit isn't a free field
- full O(4) invariance only under an extra "flux" hypothesis

**The authors' own caveats.**
- The theorem is conditional on the proof inputs listed in Section 9, and on Bałaban's theorems as he stated them.
- Some supporting statements are not claimed as proved, and two are not yet written.
- The .tex files are raw LLM output with "certainly gaps and mistakes".
- There is no Lean; checking is LLM review plus some hand checks.
- There is no mass gap.

| | OpenAI | Sussman–Alpöge |
|---|---|---|
| Date | Oct 26 (Lean released Nov 11) | Oct 6 |
| Model | Unreleased internal model | Claude (Codex for the QED3 warm-up) |
| Scope | All compact groups with simple nonabelian Lie algebra; QCD claimed | SU(2) pure Yang–Mills |
| Status | Claimed unconditional | Explicitly conditional, gaps listed |
| Verification | Lean (claimed), panel review | LLM review, partial hand checks |
| Mass gap | Not claimed | Not claimed |

A quick test of OpenAI's release is whether it closes the open inputs in Section 9 of this draft, and whether it covers ℝ⁴ with full O(4) invariance rather than a torus. **[→ mathematics-science]**

---

<a id="ch5"></a>
## 5. Books and formalization

**Riehl's two books mark the two halves of category theory in Lean: the 1-categorical core is essentially done, and ∞-categories are just starting.**
[Papers › Category Theory](https://vwulf.github.io/ettuge/Books/Papers#category-theory) · [∞-cosmos project](https://emilyriehl.github.io/files/cosmos-project.pdf)

***Category Theory in Context.*** There is no complete formalization. A hobbyist Lean companion, modelled on Tao's *Analysis I* companion, covers only Chapter 1 §§1–4 with solutions. The book wasn't among ATLAS's 26; the only category-theory text there was Etingof's *Tensor Categories*, 60% done. Mathlib's 1-category library already holds almost all of the content: Yoneda, limits and colimits, adjunctions, monads, Kan extensions, abelian and monoidal categories. What's missing is the book itself, its exercises and its order of presentation.

***Elements of ∞-Category Theory* (with Verity).** Riehl's research programme runs on two tracks, each matched to a foundation:

| Track | System | Approach |
|---|---|---|
| ∞-cosmos project | Lean / mathlib | Axiomatic: ∞-categories as objects of an enriched category satisfying the ∞-cosmos axioms |
| Synthetic ∞-categories | Rzk | Simplicial homotopy type theory, a domain-specific type theory |

This is the HoTT story in miniature. Lean can't host univalent foundations, so the Lean track axiomatizes on top of classical 1-, 2- and enriched category theory. The synthetic version needs its own proof assistant. The ∞-cosmos project launched in Sep 2024, co-led with Mario Carneiro and Dominic Verity, and the definition of an ∞-cosmos is formalized. Phase two (2025) builds the 2-category of ∞-categories inside an ∞-cosmos. The hard step, proving that quasi-categories form an ∞-cosmos, is still ahead; it is done once, and then every theorem transfers.

A side result: Carneiro and Riehl ([arXiv:2503.20704](https://arxiv.org/abs/2503.20704), ITP 2025) gave the first formalized proof that the nerve functor is a fully faithful right adjoint and that Cat is cocomplete. Surprisingly, this was missing from every proof-assistant library. Riehl names reviewer bandwidth as the bottleneck, which is the same consolidation problem mathlib has with AI output. Mathlib has very little ∞-category theory, so algebraic K-theory, derived and spectral algebraic geometry and the Langlands programme stay out of reach. For the programming side of the same ideas see [Algebra and Categories](https://vwulf.github.io/ettuge/FP/bucket-algebra-categories). **[→ mathematics-science; cross-link → scala-functional-programming]**

---

**Meta's ATLAS formalized 26 textbooks at 71%, and the gaps fall exactly where mathlib lacks infrastructure.**
[Papers › Foundations and Logic](https://vwulf.github.io/ettuge/Books/Papers#foundations-and-logic)

AutoformBot, running mostly Opus 4.6, turned 26 open-access textbooks, mostly MIT OpenCourseWare notes, into about 484K lines and 45,000+ declarations. It formalized 2,855 of 4,007 target statements. Analysis came out near complete: Rodriguez's *Real Analysis* 99%, Helgason's *Complex Variables* 97%, Stanley's *Algebraic Combinatorics* 95%. Lie theory, algebraic geometry and manifolds stalled: Etingof's *Representations of Lie Groups* 40%, Minzer's *Boolean Functions* 41%. Sipser's *Theory of Computation* reached 71%.

The paper's own caveats:
- quality below expert Lean
- workers that tried to cheat by hiding axioms, weakening hypotheses, or oversimplifying manifolds and schemes
- in a human review of the Stanley book, the two hardest theorems rested on explicit placeholder axioms
- each book is a standalone project, not integrated into mathlib

The full table is in [Lean and AI Formalization](https://vwulf.github.io/ettuge/FP/lean-ai-formalization). **[→ books-literature; cross-link → mathematics]**

---

**Other books in the same thread.**
- **Tao, *Analysis I*:** has a Lean companion that shifts from hand-built definitions to mathlib's as it goes. His measure-theory book is in progress.
- **Niu and Spivak, *Polynomial Functors*:** a UW Math AI Lab formalization target ([Papers › Category Theory](https://vwulf.github.io/ettuge/Books/Papers#category-theory)).
- **Falconer, *Geometry of Fractal Sets*:** one targeted theorem formalized.
- **CLRS:** the first major milestone of CSLib, the new "mathlib for CS". Isabelle has the strongest record for algorithms, and the largest recent AI effort on CLRS used F*, not Lean.
- **Bird and Gibbons, *Algorithm Design with Haskell*:** a Lean adaptation reimplements its five design principles (divide and conquer, greedy, thinning, dynamic programming, exhaustive search), with refinement proofs between versions. See [Algorithms, Functionally](https://vwulf.github.io/ettuge/FP/bucket-algorithms).

Related popular books in the catalogue: [Fermat's Last Theorem](https://vwulf.github.io/ettuge/Books/influential/fermats-last-theorem), now itself formalized in Lean, and [Gödel's Proof](https://vwulf.github.io/ettuge/Books/influential/godels-proof). **[→ books-literature]**

---

<a id="ch6"></a>
## 6. Themes across the deep dives

**Machine checking settles correctness, not meaning, readability or credit.** The same pattern recurred across the results:
- **Two versions.** A long Lean-checked document sat beside a short unchecked one that humans actually read (quasi-RH, matrix multiplication).
- **Statement fidelity.** Is the formal statement ETH as people mean it? Is the Lean Yang–Mills theorem on ℝ⁴ or a torus? Are the OS axioms encoded faithfully?
- **Credit.** Navier–Stokes and Buckmaster–Alpöge.
- **Readability.** Moshkovitz on UGC, Radziwiłł on quasi-RH.

**Old tools, new combinations.** The landmark proofs mostly assembled existing machinery in combinations nobody had tried. Quasi-RH used a family of L-functions that had been overlooked. UGC used the 2-to-2 inverse theorem plus a new gadget. Chowla used a 1970s spectral fact plus extremal MaxCut. Yang–Mills completed Bałaban's 1980s programme. Experts' main surprise was that the existing toolkits were already strong enough.

**Where the walls still are.** The parity barrier blocks twin primes and binary Goldbach whatever happens to RH. Small-Set Expansion stays open after UGC. The unforced Navier–Stokes equations and the Yang–Mills mass gap are untouched. In each case the AI results moved the boundary right up to a known obstruction without crossing it. **[→ mathematics]**
