# Lean, Foundations, and the AI Formalization of Mathematics

*Started Nov 1, 2026 · last updated Nov 10, 2026 · Vishwas*

## Summary

Lean 4 is the de facto platform for AI-assisted formalization of mathematics, and 2026 moved it from flagship projects to industrial scale. Fermat's Last Theorem (September) and the Classification of Finite Simple Groups (October) were both fully formalized by AI agent swarms in weeks.

- **Foundations:** Lean uses a variant of the Calculus of Inductive Constructions with an impredicative, definitionally proof-irrelevant `Prop`, built-in quotients and three classical axioms.
- **HoTT:** Lean 2 had a HoTT mode; Lean 3 removed it because definitional proof irrelevance implies UIP, which contradicts univalence. The AI-formalization industry does not need univalence, so the incompatibility is largely moot.
- **Coverage:** still well under 1% of the published research literature by paper count, but roughly 80–90% of the undergraduate canon and a large share of "load-bearing" theorems.
- **Open-problem releases** (OpenAI Astra, Anthropic's zeta-zeros result) add new formalized theorems but only incidentally extend coverage of existing math.
- **The bottleneck** has shifted from proving to consolidation: mathlib stays human-curated while permissive staging libraries absorb AI output.
- **Nov 2026:** Axiom published a Lean formalization of essentially all of the Stacks Project (\~18M lines), though \~99% of it is unreviewed AI output.
- **Algorithms lag mathematics:** CSLib (2026) is young; imperative algorithms are further along in F\*, Isabelle and Rocq, and amortized purely functional structures (Okasaki) are unformalized in Lean.
- **Trust in the kernel:** summer 2026 kernel bugs led Lean to ship independent and formally verified checkers (Oct 2026); statement fidelity remains the human step.
- **Nov 2026:** a just-published deterministic n^O(log n) graph isomorphism result arrived with a Lean proof of both correctness and running time, built on Axiom's CFSG.
- **Nov 6, 2026:** PSI announced an AI-produced proof of the Aaronson–Ambainis conjecture (open since 2008) with a compact, Comparator-checked Lean formalization.
- **Nov 9–10, 2026:** agent-driven verification reached deployed software (DeepMind's machine-code proofs for Signal; a Lean copy of 16% of CPython that found 418 bugs), and 1,000 Fable 5.2 agents re-formalized FLT in 28.7 hours.

## 1. Lean's foundational basis

Lean is built on dependent type theory, specifically a variant of the Calculus of Inductive Constructions (CIC), the same family as Rocq. Its distinctive choices:

| Component | Lean 4 choice |
| --- | --- |
| Universes | Hierarchy `Sort 0 = Prop`, `Sort 1 = Type`, … with universe polymorphism; non-cumulative |
| `Prop` | Impredicative, with definitional proof irrelevance (any two proofs of a proposition are judgmentally equal) |
| Inductive types | Kernel knows only recursors; pattern matching and well-founded recursion are elaborated down to them |
| Quotients | `Quot` and `Quot.sound` built into the kernel; function extensionality is a theorem |
| Axioms | `propext`, `Quot.sound`, `Classical.choice`; excluded middle follows via Diaconescu |

In practice Lean and mathlib are openly classical. One known cost: definitional proof irrelevance combined with subsingleton elimination (e.g. on `Acc`) makes Lean's definitional equality undecidable and non-transitive in the kernel (Abel & Coquand). This rarely matters in practice.

## 2. HoTT in Lean: added, then removed

Lean 2 (around 2015) shipped a HoTT mode; Lean 3 (2017) dropped it, and Lean 4 has no official HoTT support.

**Lean 2 HoTT mode** removed the impredicative proof-irrelevant `Prop`, assumed univalence as an axiom, and came with its own library.

**Why Lean 3 dropped it:**

- **Logical incompatibility.** Definitional proof irrelevance makes `Eq` a mere proposition, giving uniqueness of identity proofs (UIP). UIP contradicts univalence, so HoTT needed a second kernel configuration.
- **Maintenance cost.** Two kernels and two libraries were too much for a small team.
- **Strategic focus.** Development prioritized classical mathematics (what became mathlib), automation and performance.

A community HoTT library survived in Lean 3 by avoiding `Prop` and using a linter to reject proofs relying on incompatible features. It never became mainstream. For native, computational univalence the usual tool today is Cubical Agda.

## 3. Lean vs Rocq

Rocq (formerly Coq) has a more conservative kernel, which keeps it HoTT-compatible; Lean's choices make everyday classical mathematics smoother.

| Feature | Lean 4 | Rocq |
| --- | --- | --- |
| Universes | Non-cumulative | Cumulative (pCIC), plus universe polymorphism |
| Proof irrelevance | Definitional in `Prop` | Not by default; opt-in via `SProp` |
| Quotients | Primitive in the kernel | None; setoids or axioms |
| Default logic | Classical in practice | Constructive; axioms opt-in |
| Recursion in kernel | Recursors only | `fix`/`match` with a syntactic guard condition |
| HoTT | Incompatible | Coq-HoTT library works (avoids `Prop`, uses `-indices-matter`, univalence as axiom) |
| Main math library | mathlib (\~2M+ lines) | Mathematical Components, UniMath, Coq-HoTT |

## 4. AI + mathematicians: why Lean, and the HoTT question

The AI-for-math industry has standardized on Lean 4 and mathlib; Rocq barely figures in it.

**Major players** ([HackerNoon](https://sia.hackernoon.com/math-in-the-age-of-machine-proof)):

- Google DeepMind (AlphaProof), Harmonic (Aristotle), ByteDance (Seed Prover), Logical Intelligence (Aleph Prover)
- Math, Inc. (Gauss), Axiom Math, OpenAI, Anthropic
- Academic pipelines such as Meta's AutoformBot ([arXiv 2605.29955](https://arxiv.org/html/2605.29955)), M2F, Theo and EPFL's document-level autoformalization

**Typical workflow:** a human-written blueprint, then AI autoformalization, then humans checking that the formal statements match intent. On the strong PNT project, Math, Inc. said they manually checked critical statements and fixed misformalizations ([Lean Zulip](https://leanprover-community.github.io/archive/stream/219941-Machine-Learning-for-Theorem-Proving/topic/Math.2C.20Inc.2C.20and.20Gauss.20discussion.html)).

**Why Lean won:**

- **mathlib is the moat:** a single large, uniform library to build on and train on.
- **Community:** Buzzard, Tao and Kontorovich pulled working mathematicians into Lean.
- **Classical defaults** match how mathematicians write, so autoformalizing a typical paper doesn't fight the foundations.

**How the HoTT incompatibility is handled: mostly it isn't needed.**

- Most mathematics is set-level and classical; univalence was never a requirement.
- "Equivalent things are interchangeable" is handled in the library: `Equiv`, algebraic isomorphisms and transfer tactics. That boilerplate is cheap for LLMs.
- Higher categories are modelled classically via simplicial sets and quasi-categories (e.g. Riehl's ∞-cosmos project), not synthetic HoTT.
- Synthetic HoTT and univalent foundations remain a separate niche in Cubical Agda, Coq-HoTT and UniMath.

## 5. Landmark formalizations, 2025–2026

In 2026 AI agents formalized two of the largest proofs in mathematics, each in under a month; both artifacts dwarf mathlib.

| Date | Result | Who | Scale and notes |
| --- | --- | --- | --- |
| Oct 2026 | [Classification of Finite Simple Groups](https://www.unite.ai/?p=495307) | Axiom Math, agent swarms | 24 days; \~43.1M lines, 2.05M declarations, 715 sources; follows the first-generation proof; found an error in a published argument for the unbalanced group theorem |
| Aug 2026 | [FormaTheoria CFSG components](https://alphaxiv.org/abs/2608.10894v1) | Qiuzhen-CFSG | \~994K lines; through Bender–Suzuki, including Feit–Thompson; \~1.2M lines later reused by Axiom |
| Sep 2026 | [Fermat's Last Theorem](https://anthropic.com/research/formalizing-fermats-last-theorem) | Anthropic (Claude agents) | 11 days; \~13M lines; only Lean's three standard axioms; Buzzard reviewed; built on mathlib, Imperial's FLT project and flt-regular |
| Feb 2026 | [Sphere packing in dimension 8](https://arxiv.org/html/2604.23468v3) | Hariharan–Viazovska project + Math, Inc. Gauss | Gauss completed the final stages; codebase grew from \~20K to 80K lines, refactored to 60K |
| Sep 2025 | Strong Prime Number Theorem | Math, Inc. Gauss | 3 weeks; \~25K lines, 1,000+ theorems; completed the Tao–Kontorovich challenge |
| 2025 | Carleson's theorem | Human-led project | Major harmonic analysis result |

Other pieces: Meta's AutoformBot formalized 26 open textbooks into 45,000+ verified declarations ([arXiv 2605.29955](https://arxiv.org/html/2605.29955)); a constructive [ATLAS of finite simple groups](https://arxiv.org/pdf/2609.35847) in Lean; an independent [Renaissance Philanthropy CFSG project](https://www.renaissancephilanthropy.org/modular-humanai-approach-to-classification-of-finite-simple-groups) involving a GLS co-author.

## 6. How much math is formalized in Lean

Assuming formal statements are eventually verified to match intent: about 0.1% of the research literature by paper count, but most of the undergraduate canon. These are judgment estimates; no one measures this officially.

**Overall**

| Slice of math | Rough share formalized |
| --- | --- |
| Research literature (by paper count; denominator \~4M+ MathSciNet items) | \~0.1%; up to \~0.5% counting papers pulled in as dependencies |
| Standard graduate canon | \~40–60% |
| Standard undergraduate canon | \~80–90% |

mathlib itself is \~2M+ lines with roughly 280,000 theorems ([Lean Zulip](https://leanprover-community.github.io/archive/stream/287929-mathlib4/topic/2.20million.html)). The FLT and CFSG proofs are each many times larger and sit outside it.

**By area**

| Area | Core curriculum | Research | Landmarks |
| --- | --- | --- | --- |
| Algebra (groups, rings, fields, Galois) | Very high | Medium | CFSG, Sylow, Galois theory |
| Number theory | High | Medium | FLT, strong PNT, FLT for regular primes |
| Combinatorics and graph theory | High | Low–Medium | PFR conjecture, Equational Theories Project |
| Real and complex analysis | High | Low–Medium | Complex analysis gaps filled by Gauss |
| Measure theory and probability | High | Low | Ergodic and stochastic parts patchy |
| Point-set topology | Very high | Low | Mostly complete |
| Linear and multilinear algebra | Very high | — | Mostly complete |
| Logic and set theory | High | Low | Independence of CH (Flypitch) |
| Commutative and homological algebra | Medium–High | Low–Medium | Liquid Tensor Experiment |
| Category theory | Medium–High | Low | ∞-cosmos in progress |
| Harmonic analysis | Medium | Low | Carleson's theorem |
| Functional analysis | Medium | Low | Spectral theory partial |
| Euclidean and convex geometry | Medium | Low | Sphere packing in dimension 8 |
| Algebraic geometry | Very high (Stacks Project, mostly unreviewed) | Medium (foundations in place) | Axiom's Stacks: \~97% of results; \~4.9K EGA and \~4.5K SGA items tagged |
| Algebraic topology | Low–Medium | Very low | Few cohomology computations |
| Differential geometry and manifolds | Low–Medium | Very low | Sphere eversion |
| Representation theory | Low–Medium | Very low | Only what CFSG and FLT needed |
| PDE | Low | Very low | Little beyond basics |
| Dynamical systems | Low | Very low | — |
| Numerical, applied math, optimization | Low | Very low | Scattered projects |
| Statistics | Low | Very low | — |
| Mathematical physics | Very low | Very low | — |

Coverage is strongest where mathlib grew up (algebra, number theory, analysis) and weakest in geometric and applied areas with heavy definitions.

**Does CFSG cover most of group theory?** No. It classifies only the simple building blocks; the extension problem (how they assemble into arbitrary finite groups) is wide open, and infinite, geometric, Lie, algebraic and profinite group theory are largely untouched. Its main payoff is unlocking the many results proved "assuming CFSG".

## 7. Open-problem releases and their effect on coverage

The OpenAI and Anthropic open-problem releases mostly add a thin layer of new formalized theorems; they extend coverage of existing math only through the prerequisites they force.

| Date | Release | Formalization |
| --- | --- | --- |
| Aug 10, 2026 | [Anthropic: zeta zeros on the critical line](https://tech-insider.org/anthropic-claude-riemann-hypothesis-breakthrough-2026/), lower bound raised from 41.6% to 67.2% | Formalized in Lean |
| Aug 1, 2026 | [OpenAI Astra: ten problems open ≥10 years](https://www.implicator.ai/openai-astra-10-math-problems-lean-proofs.md) (non-sofic groups, Erdős 146/180/183, others) | Lean 4 certificates on GitHub (`openai/ten-proofs`), built on mathlib |
| May 2026 | OpenAI disproof of the Erdős unit-distance conjecture; Claude Mythos reportedly found a short proof days later | Partial |
| Later 2026 | OpenAI: 722 papers on 377 open problems | Lean coverage not confirmed |

**Effect on coverage**

- **New theorems, not old literature.** They barely move the share of existing math formalized, but a growing slice of new math is born formalized.
- **Prerequisites are the real gain.** A paper can cite a known result; a Lean proof must derive it ([Epoch](https://epoch.ai/latest/announcing-frontiermath-erdos)). Missing mathlib material gets built along the way.
- **Mostly not reusable yet.** That infrastructure sits in one-off repos with ad hoc definitions.
- **Narrow pull.** Open-problem work clusters in combinatorics, number theory and group theory, already mathlib's strongest areas.

The benchmark side is also moving to Lean: Epoch's FrontierMath Erdős poses 68 open Erdős problems in Lean.

## 8. Consolidation: getting AI output into mathlib

Mathlib has not loosened its standards; consolidation is becoming a two-tier pipeline, with permissive staging libraries feeding a human-curated mathlib.

**Mathlib's stance**

- Every PR is human-reviewed by about 60 reviewers, 28 of them maintainers who can merge ([Rothgang slides](https://www.math.uni-bonn.de/people/rothgang/slides_IntroMathlib_Berlin.pdf)).
- Maintainers warn against mass-adopting AI code that hasn't been battle-tested; Commelin, speaking personally, called current AI Lean "uncanny-valley-like" ([Lean Zulip](https://leanprover-community.github.io/archive/stream/287929-mathlib4/topic/Potentially.20useful.20results.20from.20an.20AI-assisted.20formalization.html)). AI output often duplicates existing mathlib material.
- Disclosure is becoming the norm: Tao proposed declaring AI use in PNT+ PRs ([Zulip](https://leanprover-community.github.io/archive/stream/423402-PrimeNumberTheorem+/topic/Disclosure.20of.20AI.20tools.20in.20PRs.html)).

**The emerging pipeline**

1. **Staging.** AI output lands in permissive libraries, nicknamed "sloplib" ([Zulip](https://leanprover-community.github.io/archive/stream/113488-general/topic/sloplib.html)): [Hexagon](https://hyper.ai/en/stories/d6b07ae78cf1fa40e2d4afe343118a9b) (launched Aug 2026, Buzzard and Vakil involved) and the [Lean Pool](https://lilys.ai/en/notes/daily-papers-20260923/lean-pool-ai-formal-math-archive) archive.
2. **Mining.** Humans and agents extract general lemmas and definitions from one-off proof glue.
3. **Refactoring.** Agents rewrite toward mathlib lints, naming and style ([tensor networks paper](https://arxiv.org/pdf/2607.07857), [Lean Refactor](https://arxiv.org/pdf/2605.20244)). Reviewers' bar: a PR ready to open, before review starts.
4. **Selective upstreaming.** MathlibLemma produced 1,506 checked lemmas but submitted only six hand-cleaned ones; three merged, one was rejected as redundant ([arXiv 2602.02561](https://arxiv.org/pdf/2602.02561)).

**Still unsolved**

- **Review bandwidth:** generation scales with compute; volunteer review doesn't.
- **Version drift:** mathlib renames weekly, so pinned AI repos rot quickly.
- **Design judgment:** generality, definitions and API design remain largely human, which is why curated rebuilds like Imperial's FLT project continue alongside the AI proofs.

## 9. The Stacks Project in Lean (November 2026)

On November 3, 2026, Axiom Math published [a Lean formalization of the Stacks Project](https://stacks.axiommath.ai/), de Jong's open-source reference on algebraic geometry. It claims every tag with formalizable content; exercises and obsolete chapters are out of scope. It turns algebraic geometry from one of Lean's weakest areas into its most completely covered reference work, but almost none of it has had human review.

**Scale.** Figures below come from cloning [the source](https://github.com/stacks/stacks-project) and [the formalization](https://github.com/AxiomMath/Stacks) on Nov 4, 2026.

|  | Stacks Project (LaTeX) | Axiom `Stacks` (Lean 4 v4.34.0-rc2) |
| --- | --- | --- |
| Size | 119 `.tex` files, \~740K lines | \~62.5K files, \~18M lines |
| Tags | 21,583 | \~16,300 carry `@[stacks TAG]` or `add_to_stacks` |
| Trust | Human refereeing | No `sorry`, no `native_decide`; only `propext`, `Classical.choice`, `Quot.sound` |

**Measured coverage** (tags in the LaTeX `tags` file matched against tag attributes in the Lean):

| Tag type | Formalized |
| --- | --- |
| Lemmas | 12,079 / 12,419 (97%) |
| Propositions | 316 / 324 (98%) |
| Theorems | 198 / 214 (93%) |
| Definitions | 1,544 / 1,681 (92%) |
| **All definitions and results** | **14,137 / 14,638 (96.6%)** |
| Examples / remarks | 83% / 74% |
| Exercises, section tags | Mostly not (out of scope) |

52 of 106 chapters are at 100%. The weakest are foundational chapters such as Fields (57%) and Categories (88%); those gaps are likely filled by `@[stacks]` attributes inside mathlib itself, which this count did not include. About 4,900 declarations are also tagged with EGA items and 4,500 with SGA items, so this is a partial formalization of Grothendieck too.

**Two tiers: the consolidation model made explicit.**

| Tier | Who wrote it | Files | Lines | Tags |
| --- | --- | --- | --- | --- |
| `StacksCore` | Humans; reviewed to mathlib standards | 445 | \~38K | 205 |
| `StacksFrontier` | AxiomProver agents; statements checked against tags but not human-reviewed | \~62.5K | \~18M | 15,103 |

Roughly 99% of the library is unreviewed. The kernel guarantees each proof proves its Lean statement, but whether each statement faithfully matches its tag is exactly what review must establish; the project's own metadata calls its review status "self-assessed". Contributors claim a tag with a blueprint (statement, Lean statement, dependencies, proof outline), a maintainer approves it, and every PR to either tier is reviewed by Kenny Lau, Brian Nugent, Ashvin A. Swaminathan or Yunzhou Xie. The stated goal is to move code into `StacksCore` and upstream what is reasonable to mathlib.

**What it changes.** Generation took weeks; review of 18M lines is now a human problem orders of magnitude larger than mathlib's entire history. By paper count the research literature is still \~0.1% formalized, but the foundations that algebraic geometry and Langlands-adjacent research build on are now largely present, at Frontier quality. It follows Axiom's CFSG release (Oct 26), where formalization surfaced 34 noteworthy deviations from the published proof.

## 10. CSLib and algorithms: imperative and purely functional

Algorithms are where Lean lags most relative to its mathematics. A shared CS library only started in 2026, imperative verification is further along in F\*, Isabelle and Rocq, and the core results of purely functional data structures (amortized bounds under persistence) cannot yet be stated in standard Lean.

### 10.1 CSLib: what exists today

[CSLib](https://arxiv.org/html/2602.04846v1) aims to be for computer science what mathlib is for mathematics. Authors include Barrett, Chaudhuri, Montesi, Grundy, Kohli, de Moura, Rademaker and Yingchareonthawornchai (Lean FRO, Amazon, Google DeepMind, Stanford, SDU), with Renaissance Philanthropy running a CSLib initiative. It depends on mathlib, is expert-curated, and has two pillars: (1) formalizing CS concepts, and (2) verified code via an intermediate language, Boole, with verification-condition generation and SMT hammers.

**State of the repo** ([leanprover/cslib](https://github.com/leanprover/cslib), cloned Nov 4, 2026; last commit Nov 2, Lean v4.36.0-rc2): 341 Lean files, \~52K lines. Small next to mathlib (\~2M+ lines) or Axiom's Stacks (\~18M).

| Area | What is there |
| --- | --- |
| Computability | Turing machines (multi-tape, space), URM, automata, languages, circuits (including Lupanov's synthesis bound), query complexity, distributed models |
| Languages and semantics | Lambda calculus, combinatory logic, CCS, stateful processes; Boole has only a README so far |
| Logics | Propositional, modal, Hennessy–Milner, linear logic, BTL |
| Algorithms | Insertion sort and merge sort only, plus a vending-machine CCS example and Diffie–Hellman |
| Other | Crypto primitives and protocols, PAC learning, probability, omega-sequences, free monads and polynomial functors |

**Cost models.** Two approaches already coexist:

- `TimeM T α`: a writer-style monad pairing a result with an accumulated cost `T`; a tick (✓) charges one unit. Correctness is proved on `.ret`, complexity on `.time`. Its own documentation stresses that time annotations are trusted, not checked against real cost, and it cites Danielsson 2008.
- Query complexity via `FreeM`: algorithms are written over a free monad of comparison queries (`LEQuery`), so cost is the number of queries, measured by interpretation rather than annotation. This yields the first genuinely nontrivial result: an information-theoretic lower bound for any correct comparison sort, `⌈log₂ n!⌉` queries, matched against merge sort's upper bound.

Both are monadic, with `IsMonadHom` used to transport results between interpretations. That is a design FP readers will recognize: write the algorithm once, polymorphic in the monad, then prove correctness in `Id` and cost in an instrumented monad.

**Roadmap.** The stated first major milestone is formalizing most of CLRS, with 2026–27 work on algorithms, data structures and models of computation, and Boole maturing for code verification. Measured against CLRS, current coverage is two sorting algorithms.

### 10.2 Imperative algorithms

CLRS-style algorithms are pointer- and array-heavy, which needs a program logic (separation logic or verification conditions) as well as a cost model.

| System | State |
| --- | --- |
| Lean | Mostly ahead of us: CSLib's Boole is not yet in the repo. Lean's `do` notation and `Std` verified hash/tree maps cover some ground, but there is no standard separation logic. Meta's ATLAS formalized Kelner's *Algorithmist's Toolkit* (83%), Sipser's *Theory of Computation* (71%) and Vempala's *Combinatorial Optimization* (61%) as mathematics, not as code. |
| F\* / Pulse | [AutoCLRS](https://risemsr.github.io/blog/2026-03-06-autoclrs) (Microsoft Research, March 2026): agents using Claude Opus 4.6 produced 100K+ lines covering 52 algorithms and data structures across 22 CLRS chapters, with functional correctness and some complexity bounds, in concurrent separation logic. Randomized and multithreaded chapters skipped. |
| Isabelle | Most mature: Archive of Formal Proofs entries, Isabelle-LLVM and Imperative/HOL refinement down to efficient code, and a [survey](https://link.springer.com/chapter/10.1007/978-3-030-59152-6_2) mapping verified CLRS algorithms including running times. |
| Rocq | CFML (characteristic formulae plus separation logic with time credits), Iris, and Appel's *Verified Functional Algorithms*. |

### 10.3 Purely functional algorithms and data structures

**Correctness is in reasonable shape.** Lean has verified red-black trees and heaps (Batteries), verified `Std.HashMap` and `Std.TreeMap` (weight-balanced trees), and [FAD](https://github.com/felipponn/fad), a Lean adaptation of Bird & Gibbons' *Algorithm Design with Haskell*. FAD covers divide and conquer, greedy (Kruskal, Prim, Dijkstra, union–find, Huffman), thinning, dynamic programming and exhaustive search, with refinement proofs between versions.

**Amortized persistent complexity is missing.** Nobody has formalized Okasaki's *Purely Functional Data Structures* in Lean, and the reason is foundational, not effort:

- Okasaki's central idea is that amortization survives persistence because lazy suspensions are memoized and shared across versions (banker's and physicist's methods on debits).
- Lean's logic has no notion of evaluation cost or sharing: `Thunk α` is logically `Unit → α`, and memoization is invisible to proofs. You must first build a cost semantics for memoized thunks.
- `TimeM` cannot express this: it charges each use separately, so a shared suspension is paid for every time.
- Lean's runtime pulls the other way: strict evaluation plus reference counting with in-place update of unshared values ("functional but in place"), so idiomatic Lean favors ephemeral `Array`s over lazy persistent queues.

Other systems have done it: Danielsson's thunk-monad framework in Agda (POPL 2008, which CSLib's `TimeM` cites), Charguéraud's CFML for much of Okasaki with time credits in Rocq, and Nipkow's *Functional Data Structures and Algorithms* plus "Amortized Complexity Verified" in Isabelle.

**A natural next step for CSLib:** a Danielsson-style monad of memoized, debit-carrying thunks, then Okasaki's banker's queue, real-time queues and deques on top. The free-monad and `IsMonadHom` infrastructure already in CSLib is the right substrate.

### 10.4 Summary

|  | Correctness | Complexity | Best system today |
| --- | --- | --- | --- |
| Mathematical CS (computability, automata, circuits) | Good and growing in CSLib | Some (Lupanov, query bounds) | Lean is competitive |
| Imperative (CLRS) | Sparse in Lean | Sparse | F\*/Pulse, Isabelle |
| Purely functional, eager | Good | Partial (`TimeM`) | Isabelle; Lean catching up |
| Purely functional, lazy and amortized (Okasaki) | Partial | None in Lean | Rocq (CFML), Agda, Isabelle |

### 10.5 Do agents actually use testing and verification? (Dan Luu, Nov 2026)

Dan Luu's evals are the best public evidence on whether coding agents get value from test and verification techniques. The short answer changed between model generations: GPT-5.6 Sol mostly produced caricatures of techniques, while GPT-6 Astra uses several of them meaningfully, though the evidence is thin.

**GPT-5.6 Sol (August 2026).** Agents implemented Zstd from its RFC under 26 prompt conditions (TDD, QuickCheck-style property testing, fuzzing, Lean 4, Verus, Kani, Alloy, TLA+ and others) plus a Default with no testing instructions. Naming a technique mostly made results worse: tests were superficial, fuzz inputs random, and Verus proofs vacuous, missing a real bitstream-order bug. Default was among the best conditions.

**GPT-6 Astra (published November 2026):**

| Eval | Result |
| --- | --- |
| Zstd | Saturated: Sol reached full holdout correctness \~63% of runs at \~$3.50 (medium) and \~77% at \~$5.50 (xhigh); Astra exceeds 99% at \~$1 regardless of technique. Fuzzing is now structured and finds real bugs, but the benchmark can't show whether that helps. |
| IMAP RFC | Too hard for Sol; with Astra, Default does well, and some conditions do somewhat better at higher cost (80 runs each). |
| Pandoc | Much harder: \~14 turns on average, no condition reaches 100%, 25 runs per condition, \~$90K at list price. Many techniques beat Default, but error bars are wide. |

**Notable findings (low confidence, per the author):**

- Differential testing pushed agents to examine boundary conditions closely, producing better "understanding" than other conditions.
- TDD underperformed again, but other many-small-tests conditions did not, which undercuts the usual explanation.
- ACL2 performed well, as it did in the Sol Zstd eval. Luu expects Lean to overtake it eventually given the investment, but suggests trying both today.
- Property-based testing libraries (e.g. proptest) finally produced tests that do what PBT is meant to do, apparently from general capability gains rather than targeted training.
- Testing skills don't transfer: a skill that helped Sol hurt Astra on Pandoc, and Hegel's skill cost more than Hegel without it.

**A reader case study.** One developer's statechart rewrite (about 30K lines of production change) grew a \~300K-line generated-testing harness that found \~20 of \~230 defects; agent reviewers found the rest. He counts it a negative result.

**Why it matters here.** It is the software counterpart of the faithfulness problem in sections 5 and 9: weaker agents game verification (vacuous proofs, hidden axioms), and stronger ones start using it for real. It also shows how expensive good evidence is, and that conclusions don't transfer across task size or model. Luu argues the viral claim that AI-written tests are useless rests on a small, easy benchmark and a 9% cost difference.

## 11. Can the kernel itself be trusted?

Every section above assumes Lean's kernel is correct. In summer 2026 AI-assisted work showed it was not, and by October Lean answered by shipping several independent kernels, two of them formally verified.

**The summer 2026 soundness bugs**

| Date | Event |
| --- | --- |
| Jul 25 | Ramana Kumar publishes an AI-assisted "disproof" of the Collatz conjecture that Lean accepts with no `sorry` or extra axioms. Investigating it, he finds Lean will accept `False` itself. |
| Jul 28 | Kiran Gopinathan reduces it to a small proof of `False` (issue #14576). Root cause: the kernel's handling of nested inductive types dropped phantom type parameters from auxiliary types. Reaching it required metaprogramming past the elaborator. A fix PR followed within an hour. The exploit also passed the independent nanoda checker, which had a separate bug. |
| Jul 30–Aug 20 | OpenAI (Daniel Selsam) runs security-focused AI over the kernel until it reports no further issues; several more implementation bugs are found and fixed. |
| Aug 1, Aug 24 | De Moura publishes postmortems; the second also covers runtime exploits (reference-count overflow, a GMP build issue) that nanoda rejected. |
| Aug 21 | Lean v4.33.1 ships the fixes. |
| Oct 9 | Thomas Hales' guest post on Tao's blog: what mathematicians should check after Lean accepts a proof. |
| Oct 15 | Lean v4.35.0 ships with verified kernels. |

De Moura's framing: the logic was sound; the kernel's implementation was not. The bugs were found by researchers with frontier models rather than attackers, which Hales reads as a good sign.

**What Lean now ships** ([de Moura, Oct 15](https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/))

| Kernel | Language | Assurance |
| --- | --- | --- |
| Official (`leanchecker`) | C++ | Tested; also built with a hardened allocator so memory corruption aborts |
| nanoda | Rust | Independent implementation, unverified |
| lean4lean | Lean | Follows the C++ kernel closely; verification expected within months |
| con-leche | Lean | Proven consistent: every environment it accepts has a model in set theory (Carneiro's model). Implemented and proved by Claude (Fable and Opus) under Joachim Breitner's supervision |
| con-ron | Rust | AI-assisted translation of con-leche, proven via Aeneas to refine its algorithm |

`lake check` re-exports a development and rechecks it with `leanchecker` in a sandbox; `lake check --paranoid` runs all of the kernels above. con-leche checks the whole of mathlib in about 100 seconds on eight threads, using 0.69× the instructions of the official kernel.

**What remains trusted**

- The compiler and runtime used to build each checker, including the bignum library. Running both con-leche (Lean toolchain) and con-ron (Rust toolchain) defends against this, since a shared compiler bug is unlikely.
- The consistency of the set theory used for con-leche's model, and the official kernel that checked con-leche's own proof.
- Statement fidelity, which no kernel addresses. Hales stresses this is the step humans must still do, usually easier than checking the proof, with Comparator to confirm no unexpected axioms.

**Scaling is the open problem.** External checkers don't yet scale to today's projects (FLT 13M+ lines, Tau Ceti 3M+, General Courtade–Kumar 50M+, Axiom's CFSG 43M and Stacks 18M). Binary export formats and incremental external checking are needed.

**Why it matters for this doc.** The trust story for AI-scale mathematics now has three layers: a verified kernel for the logic, diverse independent kernels for the implementation, and human review for statement fidelity. The first two are now largely automated; the third is the same bottleneck as sections 8 and 9.

## 12. Case study: graph isomorphism in n^O(log n), with a proven running time

On Nov 5, 2026, Mahdi JafariRaviz published [a Lean formalization](https://github.com/mahdi-jfri/GraphIsomorphismLog2) of Theorem 1.1 of Hajiaghayi and JafariRaviz, [*Deterministic n^O(log n) Graph Isomorphism Algorithm via Inherited Decompositions*](https://arxiv.org/abs/2611.01399v1) (arXiv, Nov 2026). It proves the algorithm's correctness and its running time over an explicit machine model, which is exactly the cost semantics section 10 found missing from mainstream Lean.

**Why the result matters.** Babai (2015) put graph isomorphism in quasipolynomial time, exp((log n)^O(1)), with Helfgott fixing the exponent at 3. n^O(log n) = exp(O(log² n)) is widely seen as the natural barrier, since group isomorphism (groups given by tables) reduces to graph isomorphism and has a trivial n^(log n) algorithm. The paper is days old and unrefereed; I found no expert reaction yet.

**What is proved.** The trusted statement is two files, \~440 lines:

- `Statement/Machine.lean` (179 lines): a log-cost RAM with procedure calls (Cook–Reckhow). Every operation costs one plus the bit length of each number it reads or writes; the machine is deterministic.
- `Statement/Main.lean`: there exist one program `p` and a constant `C` such that for every n and all graphs G, H laid out as adjacency matrices, `p` halts with a correct output at cost at most exp(C·log²(n+2)). A correct output is 0 if the graphs are not isomorphic; otherwise 1, an explicit isomorphism, and permutations generating exactly the automorphism group of G.

**How it is built** (cloned Nov 5, 2026; written by agents per its `formalization.yaml`):

| Part | Lines | Content |
| --- | --- | --- |
| `Impl/` | \~325K | The algorithm as machine programs, with proofs of output and cost |
| `Proved/` | \~34K | Cited polynomial-time subroutines: Schreier–Sims, normal closure, Hermite and Smith normal forms, Luks–Miyazaki vector stabilizer |
| `Algorithm/` + `Paper/` | \~32K | The paper's mathematics and the algorithm as an abstract recursion |
| `Lang/` + `Machine/` | \~18K | A small language, its compiler to the machine, cost-reasoning tools |
| `Assembly/`, `Cited/`, `Statement/` | \~7K | Final proof, cited results, trusted statement |
| **Total** | **\~457K** | 2,287 files, Lean v4.35.0-rc3 |

**First downstream use of Axiom's CFSG.** Three cited results rest on the classification: CFSG itself, Schreier's conjecture, and Maróti's bound on primitive group orders. They come from AxiomMath/CFSG plus a companion repo by the same author. `Cited/Facts.lean` imports \~75,000 modules and needs \~18 GB of RAM to build. That answers section 8's reuse question bluntly: import the whole thing.

**Trust assessment**

- For: no `sorry`; only the three standard axioms; a small, readable trusted statement that looks faithful (determinism rules out cheaper runs; cost charges bit lengths; output includes the automorphism group). Proof deviations from the paper are documented (Bochert's bound for Maróti's in two lemmas; Dixon's constant 5 instead of 5/2).
- Against: Comparator has not yet been run, since its kernel check would replay all of CFSG. Review status is "self-assessed", the formalizer co-wrote the paper, and the proof inherits CFSG's still-young trust status.

If experts confirm the \~440-line statement, this would be the first major complexity-theory result to arrive formally verified together with its running time.

## 13. Case study: the Aaronson–Ambainis conjecture

On Nov 6, 2026, PSI (Physical Superintelligence) [announced a proof](https://psi.inc/research/aaronson-ambainis/) of the Aaronson–Ambainis conjecture, open since 2008, with a [complete Lean formalization](https://github.com/physical-superintelligence/aaronson-ambainis). It is the opposite of section 12 in shape: small, mathlib-only, and checked end to end, which makes it about as auditable as an AI-produced proof currently gets.

**The conjecture.** Every polynomial of degree d on the Boolean cube with values in \[0, 1\] and variance at least ε has a variable whose influence (the average change in output from flipping that bit) is at least (ε/d)^O(1). Consequence: quantum query algorithms can be simulated classically with polynomial overhead on almost all inputs, so exponential quantum speedups require structured inputs. Previous general bounds decayed exponentially in d; only special cases were known, most recently Blanc, Docter, Strassle and Tan (Stanford, Aug 2026) for fixed-round parallel algorithms.

**The result.** Inf\_i ≥ (8√15 / 125π⁴)·ε^{5/2}/d⁶ ≥ (ε/d)⁷. The proof completes a plan of Lovett and Zhang by proving the inequality they left open, using a determinant-based pairing that strengthens Reimer's butterfly lemma.

**How it was made.** PSI's internal research system, running a non-public Anthropic model, had a Lean-accepted proof on day 3, then improved the bound twice. The AI drafted the paper and the formalization; David Turturean reviewed the paper and takes responsibility for it, and Jim Halverson audited the proof. The Stanford group is reading it, calls it "a huge result", and is writing a shorter exposition.

**Verification** (repo cloned Nov 6, 2026):

|  | Aaronson–Ambainis | Graph isomorphism (section 12) |
| --- | --- | --- |
| Size | \~9.4K lines, 95 files | \~457K lines |
| Dependencies | mathlib only | mathlib, Axiom CFSG, Tau Ceti; \~18 GB RAM |
| Trusted statement | `PrintedConjecture`, \~25 lines, in a file importing only mathlib | \~440 lines including a machine model |
| `sorry` / axioms | None; standard axioms only | None; standard axioms only |
| Comparator | Run in its sandbox, with negative controls (rejects four deliberately wrong solutions) | Not yet run |
| Independent kernels | `leanchecker` replay (also from an empty environment), nanoda, lean4lean | Not reported |

**Caveats**

- Toolchain is Lean v4.33.0, which predates the kernel fixes in v4.33.1 (section 11). The nanoda and lean4lean rechecks largely cover this; a rebuild on a fixed version or a con-leche check would close it.
- One of the four public theorems assumes an unformalized result of Agarwal and Ben-David, but it only improves the constant 4×; the main theorem is unconditional.
- The paper is unrefereed, the model is non-public, and expert reading is ongoing.

**The two shapes of AI formalization.** Section 12 is huge, rests on a 43M-line dependency, and has a larger statement to audit. This one is small, mathlib-only, with a short statement checked by Comparator and several kernels. The second shape is what makes "AI proved a famous conjecture" credible within days.

## 14. Verifying real software, and agent teams at scale

In November 2026 agent-driven formalization moved from mathematics to deployed software, and agent teams scaled to a thousand. In every case the architecture is the same: untrusted agents do the work, and Lean's kernel (with Comparator) decides what counts.

### 14.1 Three ways to connect proofs to real code

|  | AlphaProof Code: Signal | CPython in Lean | Aeneas / hax / Verus |
| --- | --- | --- | --- |
| Who | Google DeepMind (Nov 10, 2026) | Andrews & Zhang (Nov 9, 2026) | Academic and industry tools |
| Proofs are about | The compiled AArch64 binary of unmodified Rust code | A line-by-line Lean copy of CPython 3.15.2's C and Python | Rust source, translated automatically |
| Link to real code | Proved: Lean checks against the executable's bytes | Differential testing, 50K+ inputs per function | A translation tool, plus trusting rustc and LLVM |
| Compiler trusted? | No | Yes, and the copy must be faithful | Yes |
| Goal | Deep security guarantees for one system | Broad coverage and bug finding | Functional correctness |
| Scale | \~6.5M lines of proof; 5 people, 4 weeks | \~613K lines; 15.7% of 26,004 functions in \~11 days | Varies |

### 14.2 AlphaProof Code: Signal at the machine-code level

[DeepMind's paper](https://google-deepmind.github.io/code-verification) verifies `libsignal-protocol` v0.105.4 and `spqr` v1.6.0 (the PQXDH handshake plus the Triple Ratchet), compiled by stock rustc to an AArch64 binary of about 140,000 instructions. Theorems cover whole runs of the executable under a Lean model of AArch64 (467 instructions, 31 system calls), tested in lockstep against Arm's Sail model and qemu. The compiler is not trusted.

- **Security, two ways:** symbolic (Dolev–Yao) forward secrecy, post-compromise security, authentication, KCI and harvest-now-decrypt-later resistance, holding up to collisions; and a computational game-based bound under Gap-DH, XEdDSA, Kyber collision resistance, HKDF/HMAC PRF security and AES-CBC+HMAC. Reductions are written in a language with a cost semantics.
- **How it was made:** specs written with Gemini 4 Carbon and Claude Opus 5.5, reviewed by agents from a different model family and approved by humans (\~26K trusted lines). Proofs written entirely by Gemini 4 Carbon agent teams; a gatekeeper accepts only what Lean's kernel and Comparator accept. No RL.
- **Bug test:** two real, since-fixed bugs were reintroduced; for each, Lean proved the buggy binary insecure, with concrete attack inputs, by having the kernel parse the ELF and step through the machine code.
- **Caveats:** 39 routines (all low-level crypto, memcpy and similar) are trusted contracts; the binary is a CLI harness, not the apps; keygen, real randomness, threads, groups and side channels are out of scope; the computational bound is classical-only and vacuous after \~25,000 messages per session (8-byte MAC). The blog's "first verification of a widely deployed protocol's implementation by any method" overstates the paper's narrower claim. Spec-writing surfaced over 200 errors in the published security proofs.

### 14.3 CPython in Lean

[Andrews and Zhang](https://broyojo.com/python-formalization/) use Opus 5.5 agents to copy CPython functions into Lean line by line, test each copy against real CPython on 50,000+ inputs, prove properties (or their negations), and have a second agent try to break the work, including by checking whether a deliberately broken function would still pass a proof.

- **Status after \~11 days:** \~613K lines, 18,898 theorems, no `sorry`; 3,834 properties proved and 588 proved false. Coverage: grammar 100%, built-in types 35%, parser 31%, C modules 19%, interpreter core 10%, stdlib 9%.
- **Payoff:** 418 bug reports, about 55 of which crash or corrupt memory from ordinary Python code; 129 are C and Python implementations disagreeing.
- **Trust gap:** the copy is linked to CPython only by testing. Several Lean-valid proofs were wrong about real Python (allocation assumed never to fail, an off-by-nine recursion limit, subclass checks, memory address reuse), caught by running the claims against CPython.

### 14.4 A thousand agents: FLT with Claude Fable 5.2

[Anthropic re-ran the FLT formalization](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) with 1,000 agents on an early Claude Fable 5.2, with no researcher steering.

|  | Sept 2026 | Nov 2026 |
| --- | --- | --- |
| Agents | Dozens, plus a researcher | 1 lead + 999 helpers |
| Time | 11 days | 28.7 hours |
| Output tokens | \~6B | About a third |
| Proof size | \~13M lines | About a seventh |
| Coordination | Prove2Me platform | Git branches + 5 shared SQL tables |

- Agents organized into crews with captains; Langlands–Tunnell became a 2,418-task tree up to 10 levels deep, worked on by \~750 helpers.
- Agents initially judged 47 of 60 statements infeasible, then proved most of them.
- Safety layers: a VM per agent, no network, locked-down kernel, branch-only pushes; an LLM monitor on every command and edit, where any block halts the team for human review; offline audits. Across more than a million tool calls nothing was blocked.

### 14.5 What these show

- **Two trust problems, handled separately:** the kernel guarantees outputs; sandboxes and monitors guard against the agents themselves.
- **Specifications are the human bottleneck:** in the Signal work proofs were fully automated and the effort went into a 26K-line spec reviewed across two model families.
- **Line counts are partly verbosity:** FLT shrank sevenfold in two months.
- **Answer to Dan Luu's question (section 10.5):** with a strong checker in the loop, agents use verification for real, and differential testing keeps formal models honest.

## 15. Lean as a programming language

Lean the prover is now very trustworthy; Lean the programming language is mostly ordinary, unverified code with an unusually well-specified standard library. Figures below come from cloning [leanprover/lean4](https://github.com/leanprover/lean4) and mathlib on Nov 5, 2026.

### 15.1 How much of Lean itself is verified

| Part | Size | Theorems vs. definitions | Verified? |
| --- | --- | --- | --- |
| `src/Lean`: elaborator, tactics, compiler, language server | \~304K lines | 84 theorems vs. 17,699 defs (1,703 `partial` or `unsafe`) | \~0% |
| Kernel (C++) | \~8K lines | none | No, but proofs can be rechecked by verified kernels (section 11) |
| Runtime and support (C++) | \~27K lines | none | No |
| `Init`: core library | \~226K lines | 25,259 theorems vs. 4,129 defs | Heavily specified |
| `Std`: data structures | \~199K lines | 21,026 theorems vs. 4,294 defs | Heavily specified |

- The tool itself is essentially unverified, but its soundness now rests on separately verified checkers, so elaborator and tactic bugs cannot make a false proof pass.
- The library gap: \~790 functions are swapped at runtime for C or faster code via `@[extern]` or `implemented_by`. Proofs are about the reference definition; nothing checks the substitute agrees.
- Lean programs in the wild are almost entirely unverified; a few verification projects exist (AWS Cedar, SampCert).

### 15.2 Pure vs. mutation style

| Codebase | Lines | Theorems | Defs | `let mut` | `for` loops | `do` per 1K lines |
| --- | --- | --- | --- | --- | --- | --- |
| `src/Lean` | 304K | 222 | 20K | 2,300 | 2,154 | 69 |
| `Init` | 226K | 25K | 7.3K | 20 | 16 | 3 |
| `Std` | 199K | 21K | 6.0K | 78 | 68 | 5 |
| mathlib | 2.37M | 193K | 66K | 469 | 487 | 3 |

At least 95% of Lean code is proof-style pure code; mutation style is concentrated in tooling, metaprograms and the few applications. The distinction is mostly syntax:

- Mutation style is pure: `let mut`, `for`, `while` and early `return` are `do`-notation sugar over `StateT`, `ForIn` and early-exit monads. Only `IO.Ref` and `ST.Ref` are real references.
- Pure code mutates at runtime: reference counting lets an unshared `Array` be updated in place ("functional but in place"), which is why idiomatic Lean prefers `Array` to `List` and why Okasaki-style persistent sharing goes against the grain (section 10.3).

### 15.3 Tail calls

Tail call optimization is essential because loops are tail recursion underneath: `for` and `while` desugar into self-recursive `forIn` loops.

- **Guaranteed:** self tail calls. The C emitter (`LCNF/EmitC.lean`, `isTailCall`) turns a function calling itself in tail position into parameter reassignment and a jump.
- **Not guaranteed:** mutual and indirect tail calls, which rely on the C compiler. Comparable to Scala's `@tailrec`, not Scheme.
- **Verified stack-safe rewrites:** natural non-tail-recursive definitions stay as the specification, and \~100 `@[csimp]` lemmas (e.g. `foldr_eq_foldrTR`, `mergeSort_eq_mergeSortTR`) prove a tail-recursive version equal, which the compiler then substitutes. Unlike `@[extern]` swaps, these are proven.
- **Not applicable in the kernel:** proofs that compute (`decide`, `rfl`) are reduced by the kernel, which has its own recursion limits; `native_decide` trades this for trusting the compiler.

## 16. Lean in the wild

Lean is still niche by repository count, but in the past year it reached the same band as Haskell, Scala and Elixir for new projects, and it now dominates proof assistants. Counts are from GitHub's search API on Nov 5, 2026.

| Language | All repos | New, Nov 2025 – Nov 2026 |
| --- | --- | --- |
| Python | 35.7M | 12.7M |
| JavaScript | 48.7M | 10.2M |
| TypeScript | 19.7M | 8.8M |
| Java | 22.0M | 3.1M |
| C++ | 7.3M | 1.4M |
| Go | 2.6M | 612K |
| Rust | 1.46M | 530K |
| Scala | 261K | 11.0K |
| Haskell | 165K | 10.6K |
| Elixir | 134K | 15.2K |
| OCaml | 44K | 5.0K |
| Zig | 40K | 16.3K |
| F# | 35K | 3.5K |
| **Lean** | **21K** | **14.6K** |
| Nim | 14K | 2.7K |
| Rocq (Coq) | 8.8K | 1.6K |
| Agda | 3.4K | 365 |
| Isabelle | 1.5K | 251 |

- **Explosive and recent growth:** new Lean repos per year went 1.4K (Nov 2023–Oct 2024), 2.4K (Nov 2024–Oct 2025), then 14.6K (Nov 2025 to now). About 70% of all Lean repos are from the past year.
- **Against general languages:** Lean's stock is Nim-sized, but its new-repo rate now exceeds Haskell's and Scala's. Against the mainstream it is about 0.1% of Python's new repos.
- **Against provers:** about 9× Rocq's and 40× Agda's new repos last year. Isabelle is understated, since most of its Archive of Formal Proofs is not on GitHub.

**Few repos, but huge ones.** A handful of AI-generated projects dominate by volume: General Courtade–Kumar 50M+ lines, Axiom CFSG \~43M, Axiom Stacks \~18M, FLT \~13M, Tau Ceti 3M+, mathlib \~2.5M, the graph isomorphism proof \~0.46M, Lean core \~0.8M. Together that is \~130M lines, with each of the largest on the scale of the Linux kernel (\~40M lines of C), though inflated by AI verbosity (FLT is \~5× mathlib).

Caveats: GitHub counts are approximate and label repos by majority language; "Lean" includes Lean 3; many new repos are likely small AI experiments; and these measure activity, not production use.

## References

Sections 1–3 (foundations, HoTT, Rocq) draw on general knowledge of the systems; the rest are linked below.

**Landmark formalizations**

- [Anthropic: Formalizing Fermat's Last Theorem](https://anthropic.com/research/formalizing-fermats-last-theorem)
- [Anthropic news post on FLT](https://www.anthropic.com/news/formalizing-fermats-last-theorem)
- [Unite.AI: Axiom Math releases 43.1M-line CFSG proof](https://www.unite.ai/?p=495307)
- [FourWeekMBA: Axiom's agents checked a 15,000-page proof](https://fourweekmba.com/ai-axioms-ai-agents-checked-a-15000-page-proof-in-24-days/)
- [FormaTheoria toward CFSG (arXiv 2608.10894)](https://alphaxiv.org/abs/2608.10894v1)
- [A constructive ATLAS of finite simple groups in Lean](https://arxiv.org/pdf/2609.35847)
- [Renaissance Philanthropy: human–AI CFSG project](https://www.renaissancephilanthropy.org/modular-humanai-approach-to-classification-of-finite-simple-groups)
- [Sphere packing in dimension 8 (arXiv 2604.23468)](https://arxiv.org/html/2604.23468v3)
- [Math, Inc.: Introducing Gauss](https://hn.jakechampion.name/reader/https://www.math.inc/gauss)
- [Lean Zulip: Math, Inc. and Gauss discussion](https://leanprover-community.github.io/archive/stream/219941-Machine-Learning-for-Theorem-Proving/topic/Math.2C.20Inc.2C.20and.20Gauss.20discussion.html)
- [Meta: textbook autoformalization (arXiv 2605.29955)](https://arxiv.org/html/2605.29955)

**Open problems and benchmarks**

- [Implicator: OpenAI Astra ten problems with Lean proofs](https://www.implicator.ai/openai-astra-10-math-problems-lean-proofs.md)
- [Tech Insider: Anthropic zeta-zeros result](https://tech-insider.org/anthropic-claude-riemann-hypothesis-breakthrough-2026/)
- [Epoch: FrontierMath Erdős](https://epoch.ai/latest/announcing-frontiermath-erdos)

**Ecosystem and consolidation**

- [Math in the Age of Machine Proof (HackerNoon)](https://sia.hackernoon.com/math-in-the-age-of-machine-proof)
- [Lean Zulip: mathlib reaches 2 million lines](https://leanprover-community.github.io/archive/stream/287929-mathlib4/topic/2.20million.html)
- [Rothgang: Introduction to Mathlib (slides, Aug 2026)](https://www.math.uni-bonn.de/people/rothgang/slides_IntroMathlib_Berlin.pdf)
- [Lean Zulip: AI-assisted formalization results](https://leanprover-community.github.io/archive/stream/287929-mathlib4/topic/Potentially.20useful.20results.20from.20an.20AI-assisted.20formalization.html)
- [Lean Zulip: sloplib](https://leanprover-community.github.io/archive/stream/113488-general/topic/sloplib.html)
- [Lean Zulip: disclosure of AI tools in PNT+ PRs](https://leanprover-community.github.io/archive/stream/423402-PrimeNumberTheorem+/topic/Disclosure.20of.20AI.20tools.20in.20PRs.html)
- [Hexagon repository (hyper.ai)](https://hyper.ai/en/stories/d6b07ae78cf1fa40e2d4afe343118a9b)
- [Lean Pool archive](https://lilys.ai/en/notes/daily-papers-20260923/lean-pool-ai-formal-math-archive)
- [MathlibLemma (arXiv 2602.02561)](https://arxiv.org/pdf/2602.02561)
- [Multi-agent autoformalization of tensor network theory (arXiv 2607.07857)](https://arxiv.org/pdf/2607.07857)
- [Lean Refactor (arXiv 2605.20244)](https://arxiv.org/pdf/2605.20244)

**Stacks Project**

- [Stacks Project in Lean (Axiom Math)](https://stacks.axiommath.ai/)
- [AxiomMath/Stacks repository](https://github.com/AxiomMath/Stacks)
- [The Stacks Project source (stacks/stacks-project)](https://github.com/stacks/stacks-project)
- [AI/TLDR: Axiom CFSG formalization](https://ai-tldr.dev/releases/axiom-cfsg-lean-formalization/)

**CSLib and algorithms**

- [CSLib white paper (arXiv 2602.04846)](https://arxiv.org/html/2602.04846v1)
- [leanprover/cslib repository](https://github.com/leanprover/cslib)
- [CSLib slides (CLRS milestone)](https://docs.google.com/presentation/d/1aJFM3EaI4LcppHR_2YFQHiBjUfMMhMKxCeM3BfINi48/htmlpresent)
- [FAD: Algorithm Design with Haskell in Lean](https://github.com/felipponn/fad)
- [Swamy, Formalizing Data Structures and Algorithms with Agents (AutoCLRS)](https://risemsr.github.io/blog/2026-03-06-autoclrs)
- [Survey of verified textbook algorithms (Springer)](https://link.springer.com/chapter/10.1007/978-3-030-59152-6_2)
- [Okasaki, Purely Functional Data Structures (thesis PDF)](https://patterns.ponylang.io/assets/purely-functional-data-structures.pdf)
- [Meta ATLAS textbook autoformalization (arXiv 2605.29955)](https://arxiv.org/html/2605.29955)
- [Dan Luu, Test and verification technique effectiveness with GPT-6 Astra](https://danluu.com/astra-testing/)
- [Dan Luu, How well do agents use test and verification techniques?](https://danluu.com/agentic-testing/)
- [De Moura, Lean now ships with verified kernels (Oct 15, 2026)](https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/)
- [GIGAZINE: Collatz disproof exposes Lean kernel bug #14576](https://gigazine.net/gsc_news/en/20260803-collatz-lean-kernel-bug)
- [Summary of Hales' guest post on Lean trust (Chinese translation)](https://braindetox.kr/zh/posts/tao_what_mathematicians_should_know_lean_trust_ai_2026.html)
- [Science: AI is shaking up math. But can its proofs be trusted? (not read: paywalled to my tools)](https://www.science.org/content/article/ai-shaking-math-can-its-proofs-be-trusted)

**Graph isomorphism and Lean as a language**

- [GraphIsomorphismLog2 repository (JafariRaviz)](https://github.com/mahdi-jfri/GraphIsomorphismLog2)
- [Hajiaghayi & JafariRaviz, Deterministic n^O(log n) Graph Isomorphism (arXiv 2611.01399)](https://arxiv.org/abs/2611.01399v1)
- [Babai, Graph Isomorphism in Quasipolynomial Time (arXiv 1512.03547)](https://ui.adsabs.harvard.edu/abs/2015arXiv151203547B)
- [AxiomMath/CFSG repository](https://github.com/AxiomMath/CFSG)
- [leanprover/lean4 repository](https://github.com/leanprover/lean4)
- [mathlib4 repository](https://github.com/leanprover-community/mathlib4)
- [PSI: proof of the Aaronson–Ambainis conjecture](https://psi.inc/research/aaronson-ambainis/)
- [physical-superintelligence/aaronson-ambainis repository](https://github.com/physical-superintelligence/aaronson-ambainis)
- [Aaronson & Ambainis, The need for structure in quantum speedups (arXiv 0911.0996)](https://arxiv.org/abs/0911.0996v3)
- [Agarwal & Ben-David (arXiv 2410.19062)](https://arxiv.org/abs/2410.19062)
- [DeepMind, Introducing AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/)
- [AlphaProof Code: Verifying Signal's Security at the Machine-Code Level (paper)](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- [AlphaProof Code verification artifacts](https://google-deepmind.github.io/code-verification)
- [Formalizing CPython in Lean (Andrews & Zhang)](https://broyojo.com/python-formalization/)
- [Broyojo/python-formalization repository](https://github.com/Broyojo/python-formalization)
- [Safely scaling multi-agent teams with Claude Fable 5.2](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/)
