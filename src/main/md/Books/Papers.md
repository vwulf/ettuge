# Papers

Research papers, theses and technical reports I keep in the Google Drive *Books › Papers* folder, arranged top-down by subject — the same layout as [Technical](Technical.md). Each entry gives the authors, where it appeared, and a line on what it does. 🔍 marks papers I have gone through in detail with Claude; these link to the published version and may not be in Drive. 📝 marks papers cited in my own notes, with a link to the write-up. Summaries of the 🔍 discussions are collected in [Deep Dives](../Deep-Dives/).

---

## Overview

- **[Mathematics](#mathematics)** (44)
  - [Algebra](#algebra) (2)
  - [Analysis and Linear Algebra](#analysis-and-linear-algebra) (7)
  - [Category Theory](#category-theory) (12)
  - [Discrete Mathematics and Combinatorics](#discrete-mathematics-and-combinatorics) (2)
  - [Foundations and Logic](#foundations-and-logic) (10)
  - [History of Mathematics](#history-of-mathematics) (7)
  - [Recreational Mathematics](#recreational-mathematics) (3)
  - [Topology and Geometry](#topology-and-geometry) (1)
- **[Computer Science](#computer-science)** (119)
  - [Algorithms and Data Structures](#algorithms-and-data-structures) (8)
  - [Compilers and Language Implementation](#compilers-and-language-implementation) (8)
  - [Computer Architecture and Parallelism](#computer-architecture-and-parallelism) (4)
  - [Computer Vision](#computer-vision) (1)
  - [Computing Education](#computing-education) (1)
  - [Distributed and Data Systems](#distributed-and-data-systems) (8)
  - [Functional Programming](#functional-programming) (35)
  - [LLM Inference Serving](#llm-inference-serving) (7)
  - [Networks and Security](#networks-and-security) (1)
  - [Operating Systems and Systems Programming](#operating-systems-and-systems-programming) (1)
  - [Programming Languages and Type Theory](#programming-languages-and-type-theory) (26)
  - [Software Design and Engineering](#software-design-and-engineering) (5)
  - [Theory of Computation](#theory-of-computation) (14)
- **[AI and Machine Learning](#ai-and-machine-learning)** (107)
  - [Applied ML](#applied-ml) (20)
  - [Deep Learning](#deep-learning) (21)
  - [Foundations](#foundations) (3)
  - [Large Language Models](#large-language-models) (63)
- **[Physics and Engineering](#physics-and-engineering)** (4)
  - [Electrical Engineering](#electrical-engineering) (4)
- **[Linguistics and Languages](#linguistics-and-languages)** (30)
  - [Dravidian and Kannada Linguistics](#dravidian-and-kannada-linguistics) (6)
  - [Historical Linguistics and Scripts](#historical-linguistics-and-scripts) (15)
  - [Sanskrit and Indo-Aryan Linguistics](#sanskrit-and-indo-aryan-linguistics) (9)
- **[Other](#other)** (23)
  - [Health and Nutrition](#health-and-nutrition) (14)

---

## Mathematics

### Algebra

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[A constructive ATLAS of finite simple groups in Lean](https://arxiv.org/abs/2609.35847)** |  | arXiv, 2026 | A constructive, machine-checked ATLAS of the finite simple groups in Lean. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |
| **Group Algebras and Coding Theory** | Guerreiro | arXiv:1412.8042, 2015 | A survey of how group-algebra techniques, especially idempotents, are used to construct and analyze minimal abelian codes and their minimum weights. |

### Analysis and Linear Algebra

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[All elementary functions from a single operator](https://arxiv.org/abs/2603.21852)** | Odrzywołek | arXiv (cs.SC), 2026 | 🔍 Shows that the single binary operator eml(x, y) = eˣ − ln y, together with the constant 1, generates every elementary function — a "NAND gate" for continuous mathematics. I used it to coin an Ellara Kannada vocabulary for elementary functions: ಏ for exp, ಅ for ln, ಎ = ಏ − ಅ for eml itself, ಇ for the imaginary unit, and a trigonometry set built on ಪಾಲು ("ratio"): ನೇರಪಾಲು (sin), ಪಕ್ಕಪಾಲು (cos), ತಾಗುಪಾಲು (tan) and ಸುತ್ತುಪಾಲು (π). |
| **[Finite-time blowup for the forced Navier–Stokes equations](https://openai.com/index/navier-stokes-solution/)** | OpenAI | OpenAI announcement, 2026 | 🔍 Claims finite-time singularity formation for the forced 3D Navier–Stokes equations; contested over whether the forced case is the Millennium problem and over credit. Compared with Buckmaster–Alpöge work on 3D Euler blowup. |
| **Mathematics for Machine Learning: Linear Algebra, Week 1 slides** | DeepLearning.AI | DeepLearning.AI course slides, 2023 | Lecture slides for week 1 of course 1 (linear algebra) of DeepLearning.AI's Mathematics for ML specialization. |
| **Mathematics for Machine Learning: Linear Algebra, Week 3 slides** | DeepLearning.AI | DeepLearning.AI course slides, 2023 | Lecture slides for week 3 of course 1 (linear algebra) of DeepLearning.AI's Mathematics for ML specialization. |
| **Mathematics for Machine Learning: Linear Algebra, Week 4 slides** | DeepLearning.AI | DeepLearning.AI course slides, 2023 | Lecture slides for week 4 of course 1 (linear algebra) of DeepLearning.AI's Mathematics for ML specialization. |
| **[The Quasi-Riemann Hypothesis](https://quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019)** | OpenAI | OpenAI manuscript (openai/math), 2026 | 🔍 Two versions: a 199-page, Lean-checked proof of a zero-free region for ζ(s) with Re(s) > 7/8, and a 49-page, unchecked proof of the 11/12 bound. |
| **[A theory of regularity structures](https://arxiv.org/abs/1303.5113)** | Hairer | Inventiones Mathematicae, 2014 | Introduces regularity structures, a framework for giving meaning to and solving a class of singular stochastic partial differential equations such as the KPZ equation; the work behind Hairer's 2014 Fields Medal. |

### Category Theory

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Category theory for (big) data modeling and model's transformation** | Zhao | PhD thesis, Universite de Haute Alsace, 2019 | Thesis applying category theory to (big) data modelling and transformation between data models. |
| **[Formalizing Colimits in Cat](https://arxiv.org/abs/2503.20704)** | Carneiro & Riehl | ITP 2025 (LIPIcs) | 🔍 A Lean formalization of colimits in the category of categories, and the practical lessons it teaches about formalizing category theory. |
| **[Fundamental Components of Deep Learning: A category-theoretic approach](https://arxiv.org/abs/2403.13001)** | Gavranovic | PhD thesis, University of Strathclyde (arXiv:2403.13001), 2024 | Develops a category-theoretic foundation for deep learning based on parametric lenses and optics. |
| **[Higher category theory](https://arxiv.org/abs/2401.14311)** | Haugseng | Encyclopedia of Mathematical Physics (arXiv), 2024 | Introduction to the homotopical theory of higher categories, motivating the definitions of infinity-categories and (infinity,n)-categories. |
| **Intro to Category Theory: Natural Transformations** |  | Lecture notes | Lecture notes defining natural transformations as transformations between functors, with examples. |
| **Physics, Topology, Logic and Computation: A Rosetta Stone** | Baez & Stay | arXiv, 2009 | Explains, using symmetric monoidal categories, the analogy between Feynman diagrams in physics, cobordisms in topology, proofs in logic and programs in computation. |
| **[Polynomial Functors: A Mathematical Theory of Interaction](https://arxiv.org/abs/2312.00990)** | Niu & Spivak | Book draft (arXiv), 2023 | 🔍 Develops the category Poly of polynomial functors as a general language for interacting systems — dynamical systems, wiring diagrams, databases and more (drafts circulated from 2021). |
| **Sheaf Theory** | Centazzo & Vitale | Categorical Foundations (book chapter VII), 2004 | Introductory chapter on sheaf theory, motivated by local-to-global problems in analysis. |
| **[A synthetic approach to Markov kernels, conditional independence and theorems on sufficient statistics](https://arxiv.org/abs/1908.07021)** | Fritz | Advances in Mathematics, 2020 | 🔍 Develops Markov categories as a synthetic, category-theoretic setting for probability, proving results on conditional independence and sufficient statistics without measure-theoretic detail. |
| **[Traced monoidal categories](https://doi.org/10.1017/S0305004100074338)** | Joyal, Street & Verity | Mathematical Proceedings of the Cambridge Philosophical Society, 1996 | 🔍 Introduces traced monoidal categories — an abstract account of feedback and loops — and the Int construction that embeds them in compact closed categories. |
| **Value Iteration is Optic Composition** | Hedges & Rodriguez Sakamoto |  | Shows that value improvement in dynamic programming is composition in a category of optics, as a step toward describing reinforcement learning with parametrised optics. |
| **[The ∞-cosmos project (blueprint)](https://emilyriehl.github.io/infinity-cosmos/blueprint.pdf)** | Riehl et al. | Lean project, 2024– | 🔍 A collaborative Lean formalization of ∞-category theory via ∞-cosmoi, following Riehl–Verity; read with Riehl's "Prospects for formalizing weak ∞-categories" slides. |

### Discrete Mathematics and Combinatorics

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[From small eigenvalues to large cuts, and Chowla's cosine problem](https://arxiv.org/abs/2509.03490)** | Jin, Milojević, Tomon & Zhang | arXiv, 2025 | 🔍 Relates the smallest eigenvalues of Cayley graphs to large cuts and uses MaxCut to bound minima of cosine sums, giving polynomial bounds for Chowla's cosine problem; Bedert gave a parallel proof. |
| **[Polynomial bounds for the Chowla Cosine Problem](https://arxiv.org/abs/2509.05260)** | Bedert | arXiv, 2025 | 🔍 An independent, parallel proof of polynomial bounds for Chowla's cosine problem. |

### Foundations and Logic

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[ATLAS: autoformalizing 26 open textbooks in Lean](https://arxiv.org/abs/2605.29955)** | Meta | arXiv, 2026 | 🔍 An agentic system that formalized 26 open textbooks (mostly MIT lecture notes) into 45,000+ verified Lean declarations. |
| **Comparison of Two Theorem Provers: Isabelle/HOL and Coq** | Yushkovskiy | arXiv:1808.09701, 2018 | Compares Isabelle/HOL and Coq on their logics, proof styles and usability through worked examples. |
| **[CSLib](https://arxiv.org/abs/2602.04846)** |  | arXiv, 2026 | White paper for CSLib, a mathlib-style library for computer science in Lean. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |
| **A Lean proof of Fermat's Last Theorem (blueprint)** | Buzzard & Taylor | Project blueprint, 2025 | Blueprint for formalising a proof of Fermat's Last Theorem in Lean, covering the reductions to Frey packages, Galois representations and elliptic curves. |
| **[Lean Refactor](https://arxiv.org/abs/2605.20244)** |  | arXiv, 2026 | Agents that rewrite Lean code toward mathlib lints, naming and style. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |
| **The Lean Theorem Prover (system description)** | de Moura et al. | CADE-25, 2015 | Describes Lean, an open-source theorem prover from Microsoft Research and CMU with a small trusted kernel based on dependent type theory, meant to bridge interactive and automated theorem proving. |
| **[MathlibLemma](https://arxiv.org/abs/2602.02561)** |  | arXiv, 2026 | Produced 1,506 checked lemmas but upstreamed only six hand-cleaned ones to mathlib. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |
| **[Multi-agent autoformalization of tensor network theory](https://arxiv.org/abs/2607.07857)** |  | arXiv, 2026 | Multi-agent pipeline that formalizes tensor network theory and refactors toward mathlib style. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |
| **Number Theory in a Proof Assistant** | Thickstun | Manuscript (github.com/jthickstun/lean), 2017 | Describes formalizing elementary number theory in the Lean proof assistant from a mathematician's point of view, and what the author learned about proof assistants. |
| **[Sphere packing in dimension 8 (formalization)](https://arxiv.org/abs/2604.23468)** |  | arXiv, 2026 | Lean formalization of Viazovska's 8-dimensional sphere packing proof; Math, Inc.'s Gauss agent completed the final stages. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |

### History of Mathematics

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Concepts and Categories in Perspective** | Mac Lane | A Century of Mathematics in America, Part I (AMS), 1988 | Mac Lane's personal account of the development of algebra, algebraic topology and category theory in American mathematics. |
| **Development of Calculus in India** | Ramasubramanian & Srinivas | 2010 | Overview of calculus in the Indian mathematical tradition, from Aryabhata to Narayana Pandita and the Kerala School as presented in the Yuktibhasa. |
| **The Epic Story of Maximum Likelihood** | Stigler | Statistical Science 22(4), 2007 | History of the method of maximum likelihood from Bernoulli and Laplace to Fisher. |
| **The ET Interview: Professor C.R. Rao** | Bera | Econometric Theory 19, 2003 | Long interview with statistician C.R. Rao covering his life and career, from joining the Indian Statistical Institute onward. |
| **Life and Work of Alexander Grothendieck** | Chai & Oort |  | Looks back at Grothendieck's life and his mathematical achievements in the period, roughly 1948-1970, in which he transformed several branches of mathematics. |
| **Selected Mathematical Reviews related to the work of John Horton Conway** | American Mathematical Society | Bulletin of the AMS 58(3), 2021 | Reprints selected Mathematical Reviews of Conway's major works (ATLAS of Finite Groups, etc.) as a retrospective of his contributions. |
| **[A Severe Misalignment of AI in Mathematics](https://www.implicator.ai/25-fields-medalists-say-ai-labs-race-to-solve-math-problems-is-harming-mathematics/)** | Tao and 24 other Fields medalists | Statement, 2026 | 🔍 A statement arguing that AI labs' race to announce solutions to famous problems is harming mathematics — swamping referees and misplacing emphasis on headline results. |

### Recreational Mathematics

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **An efficient algorithm for the Knight's tour problem** | Parberry | Discrete Applied Mathematics 73, 1997 | Gives an efficient (linear-time) divide-and-conquer algorithm for constructing knight's tours on n x n boards. |
| **Knight's Tour Revisited** | Cull & De Curtins | Fibonacci Quarterly, 1978 | Shows that every rectangular board whose smaller side is at least 5 has a knight's path, and a circuit when the number of squares is even. |
| **A Simple Algorithm for Knight's Tours** | Ganzfried | Oregon State University (REU report, advisor P. Cull) | Investigates Warnsdorff's heuristic and tie-breaking rules for knight's tours, analysing a linear-time, low-memory algorithm consistent with it. |

### Topology and Geometry

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Short Introduction to Topology for Computer Science Grad Students** | Dominus | Draft v0.6, 2010 | Informal draft introduction to topology aimed at computer science graduate students, with an applications section. |

## Computer Science

### Algorithms and Data Structures

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Algorithmics** | IFIP Working Group 2.1 |  | Describes algorithmics, deriving efficient programs from high-level specifications by rigorous calculation, and the history and activities of IFIP WG 2.1. |
| **Calculating path algorithms** | Backhouse, van den Eijnde & van Gasteren | Science of Computer Programming 22, 1994 | Gives calculational derivations, based on the algebra of regular languages, of two abstract path algorithms generalising Warshall/Floyd and Dijkstra/graph search. |
| **Filtered-DiskANN: Graph Algorithms for Approximate Nearest Neighbor Search with Filters** | Gollapudi et al. | WWW 2023 | Presents graph-based ANN index algorithms (FilteredVamana, StitchedVamana) that support label filters on queries with high recall and throughput. |
| **Graph Processing Library in Rust** | Bihani & Gagneja | Stanford course project report, 2017 | Explores three approaches to representing and processing graphs in Rust and compares their performance with the C++ SNAP library. |
| **Ideal Hash Trees** | Bagwell | EPFL technical report, 2001 | Describes Hash Array Mapped Tries (HAMT), hash trees with near-constant insert/search/delete and low memory use, built on Array Mapped Tries. |
| **[Optimal Bounds for Open Addressing Without Reordering](https://arxiv.org/abs/2501.02305)** | Farach-Colton, Krapivin & Kuszmaul | arXiv, 2025 | Constructs open-addressed hash tables without reordering that achieve much better expected search complexity than previously thought, disproving Yao's conjecture, with matching lower bounds. |
| **RRB-Trees: Efficient Immutable Vectors** | Bagwell & Rompf | EPFL technical report, 2011 | Introduces Relaxed Radix Balanced Trees, which give immutable vectors O(log N) concatenation, insert-at and split while keeping fast indexing, update and iteration. |
| **[The Ubiquitous Skiplist: A Survey of What Cannot be Skipped About the Skiplist and its Applications in Big Data Systems](https://arxiv.org/abs/2403.04582)** | Xing, Vadrevu & Aref | arXiv, 2024 | Surveys skiplists and their variants, their use in systems, and compares them with tree-based structures. |

### Compilers and Language Implementation

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Counting Immutable Beans: Reference Counting Optimized for Purely Functional Programming](https://arxiv.org/abs/1908.05647)** | Ullrich & de Moura | IFL 2019 | Explores reference-counting optimisations such as destructive updates for an eager purely functional language (Lean 4), including borrowed references and inferred borrow annotations. |
| **LLVM: An Infrastructure for Multi-Stage Optimization** | Lattner | MS thesis, University of Illinois at Urbana-Champaign, 2002 | Presents the design and implementation of LLVM, a compiler infrastructure supporting optimisation across compile, link, install and run time. |
| **A Mechanically Verified Garbage Collector for OCaml** | Shamsu et al. | 2025 | Presents a mechanically verified garbage collector for OCaml, whose GC has a copying minor heap and an incremental mark-and-sweep major heap. |
| **Monadic Compiler Calculation** | Bahr & Hutton | ICFP 2022 (PACMPL) | Extends the method of calculating correct compilers to handle divergence by using the partiality monad, covering convergent and divergent behaviour together. |
| **Retrofitting Parallelism onto OCaml** | Sivaramakrishnan et al. | ICFP 2020 | Describes the design, implementation and evaluation of a mostly-concurrent garbage collector for multicore OCaml while preserving compatibility with existing code. |
| **SSA Translation is an Abstract Interpretation** | Lemerre | POPL 2023 (PACMPL) | Shows that translation to SSA form can be expressed as an abstract interpretation, which allows the translation to be combined with other static analyses for more precision. |
| **torch.fx: Practical Program Capture and Transformation for Deep Learning in Python** | Reed et al. | MLSys 2022 (arXiv:2112.08429) | Describes torch.fx, PyTorch's Python-level program capture and transformation toolkit. |
| **Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations** | Tillet, Kung & Cox | MAPL 2019 | Presents Triton, a tile-based language and compiler for writing efficient GPU kernels for neural networks. |

### Computer Architecture and Parallelism

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Powerlist: A Structure for Parallel Recursion** | Misra | ACM TOPLAS, 1994 | Proposes the powerlist data structure for succinctly describing recursive data-parallel algorithms (FFT, Batcher sort, prefix sum) and using its algebra to derive their properties. |
| **Understanding Real-World Concurrency Bugs in Go** | Tu, Liu, Song & Zhang | ASPLOS 2019 | Empirical study of concurrency bugs in real Go programs, comparing message passing with shared-memory synchronisation as sources of errors. |
| **What Every Programmer Should Know About Memory** | Drepper | 2007 | Explains the structure of memory subsystems and CPU caches on commodity hardware and what programs should do to use them well. |
| **What every systems programmer should know about concurrency** | Kline | 2020 | Covers concurrency fundamentals below the level of mutexes and semaphores: atomicity, memory ordering, and how compilers and hardware reorder code. |

### Computer Vision

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Direct Plane Parameter Estimation using Stereo Camera and Its Extension to Multi-view Application** | Sugimoto & Okutomi | IPSJ SIG Technical Report 2005-CVIM-151 | Fast Gauss-Newton estimation of 3D plane parameters from a calibrated stereo pair using the inverse compositional algorithm, extended to multi-camera setups. |

### Computing Education

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Getting started with Kojo: Programming. Math. Art. Analysis.** | Pant, Anusha & Aditya | Kogics booklet, 2023 | Short introductory guide to programming, math and art with the Scala-based Kojo environment. |

### Distributed and Data Systems

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Architecture of a Database System** | Hellerstein, Stonebraker & Hamilton | Foundations and Trends in Databases 1(2), 2007 | Surveys the systems-design architecture of database management systems: process models, parallelism, storage, transactions and shared components. |
| **ClickHouse - Lightning Fast Analytics for Everyone** | Schulze et al. | VLDB 2024 | Presents an overview of ClickHouse, a column-oriented OLAP database designed for high-performance analytics over internet-scale data with many concurrent queries and real-time latencies. |
| **Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores** | Armbrust et al. | VLDB 2020 | Describes Delta Lake, an ACID table storage layer over cloud object stores using a transaction log. |
| **Don't Thrash: How to Cache Your Hash on Flash** | Bender et al. | VLDB 2012 | Presents alternatives to the Bloom filter, starting with the quotient filter, and designs for operating such filters efficiently on flash storage. |
| **[Flo: a Semantic Foundation for Progressive Stream Processing](https://arxiv.org/abs/2411.08274)** | Laddad, Cheung, Hellerstein & Milano | POPL 2025 | Identifies streaming progress and eager execution as semantic properties shared by streaming languages and formalises them in Flo, a parameterised streaming language with a type system for bounded and unbounded streams. |
| **Keep CALM and CRDT On** | Laddad et al. | PVLDB 16(4), 2022 | Examines the limitations of CRDTs, especially for queries and consistency, and proposes research directions based on the CALM theorem. |
| **Structured Interacting Computations (A position paper)** | Cook & Misra | 2008 | Describes the design philosophy of Orc: structuring concurrent programs hierarchically and allowing controlled interaction between subsystems by value passing. |
| **Workflow Patterns in Orc** | Cook, Patwardhan & Misra | COORDINATION 2006 | Implements van der Aalst's workflow patterns in Orc, a process calculus for orchestrating wide-area computations, as reusable definitions. |

### Functional Programming

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **'do' Unchained: Embracing Local Imperativity in a Purely Functional Language (Functional Pearl)** | Ullrich & de Moura | ICFP 2022 | Extends do-notation in Lean 4 with imperative features such as local mutation, early return and loops, translated into monadic code. |
| **Applicative programming with effects (Functional Pearl)** | McBride & Paterson | Journal of Functional Programming, 2008 | 🔍 Introduces applicative functors as an abstraction of effectful applicative-style programming weaker than monads, with their laws, generic operations and relation to monads and arrows. |
| **Arrows and computation** | Paterson | The Fun of Programming (chapter), 2003 | Explores function-like 'notions of computation' through the common arrows interface, its subclasses, and its relation to monads. |
| **Bringing Back Monad Comprehensions** | Giorgidze et al. | Haskell Symposium 2011 | Describes a GHC extension generalising list-comprehension notation to arbitrary monads, including parallel/zip, SQL-like and grouping clauses. |
| **Build Systems a la Carte** | Mokhov, Mitchell & Peyton Jones | ICFP 2018 | Offers a systematic, executable framework for developing and comparing build systems, separating their components so they can be recombined into new build systems. |
| **Caml trading - experiences with functional programming on Wall Street** | Minsky & Weeks | Journal of Functional Programming 18(4), 2008 | Describes Jane Street Capital's use of OCaml as its primary language for trading systems, research and systems software, and why it values the language. |
| **Comprehensive Comprehensions: Comprehensions with 'Order by' and 'Group by'** | Wadler & Peyton Jones | Haskell Workshop 2007 | Extends list comprehensions with order-by, group-by and limit qualifiers to express SQL-like queries. |
| **Conjugate Hylomorphisms, Or: The Mother of All Structured Recursion Schemes** | Hinze, Wu & Gibbons | POPL 2015 | Develops a toolbox for assembling recursive coalgebras, based on a conjugate rule parametrised by an adjunction, unifying structured recursion schemes as hylomorphisms. |
| **Design Patterns for Parser Combinators (Functional Pearl)** | Willis & Wu | Haskell Symposium 2021 | Presents reusable patterns for writing parsers in combinator style that keep parsing code simple, separated and maintainable. |
| **Desugaring Haskell's do-Notation into Applicative Operations** | Marlow, Peyton Jones, Kmett & Mokhov | Haskell Symposium 2016 | Shows how do-notation can be desugared into Applicative operations where possible, implemented as a GHC extension (ApplicativeDo). |
| **Effect Handlers in Scope** | Wu, Schrijvers & Hinze | Haskell Symposium 2014 | Presents two ways to capture scoping constructs in the syntax of algebraic effect handlers and shows how reordering handlers gives different semantics. |
| **The F# Computation Expression Zoo** | Petricek & Syme | PADL 2014 | Describes F# computation expressions, a single syntax that covers monads, monoids, applicatives and monad transformers, with examples and formal semantics. |
| **Fail Faster: Staging and Fast Randomness for High-Performance PBT** | Richey, Cutler, Goldstein & Pierce |  | Measures the performance of property-based-testing generators and removes combinator abstraction overhead with a multi-stage programming technique (Allegro) plus faster sources of randomness. |
| **Fold and Unfold for Program Semantics** | Hutton | ICFP 1998 | Shows how fold can structure denotational semantics and unfold operational semantics, and how their algebraic properties support reasoning about program semantics. |
| **Freer Monads, More Extensible Effects** | Kiselyov & Ishii | Haskell Symposium 2015 | Rationally reconstructs extensible effects from free monads to freer monads without a Functor constraint, yielding a faster and more comprehensible extensible-effects library. |
| **Fun with Semirings: A functional pearl on the abuse of linear algebra** | Dolan | ICFP 2013 | Defines a Haskell typeclass for closed semirings and uses matrix and polynomial operations over them to solve problems such as transitive closure and shortest paths. |
| **Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire** | Meijer, Fokkinga & Paterson | FPCA 1991 | Develops a calculus for lazy functional programming based on recursion operators (catamorphisms, anamorphisms, hylomorphisms, paramorphisms) and their algebraic laws. |
| **Game of Life — Polyglot FP: Haskell, Scala, Unison (Part 1)** | Schwarz | Slide deck | Slides that code Conway's Game of Life in Haskell, translate it into Scala, and show how Unison replaces monadic effects with algebraic effects. |
| **Garnishing Parsec with Parsley** | Willis & Wu | Scala Symposium 2018 | Describes Parsley, a Scala parser combinator library that keeps Parsec's style while achieving competitive performance. |
| **Generalising Monads to Arrows** | Hughes | Science of Computer Programming (2000), 1998 | Introduces arrows, a generalisation of monads, as an interface for combinator libraries whose program fragments do not fit the monadic interface. |
| **Grisette: Symbolic Compilation as a Functional Programming Library** | Lu & Bodik | POPL 2023 | Haskell library for symbolic compilation to SMT constraints. |
| **Introduction to Programming with ZIO Functional Effects** | Vasquez | Scalac ebook, 2021 | A short ebook covering pure functions and functional effects and introducing the ZIO data type, its aliases, and a worked example application in Scala. |
| **An Introduction to the Theory of Lists** | Bird | Oxford PRG Technical Monograph PRG-56, 1986 | Introduces the Bird–Meertens calculus of lists for deriving efficient functional programs by equational reasoning. |
| **Kan Extensions for Program Optimisation, Or: Art and Dan Explain an Old Trick** | Hinze | MPC 2012 | Shows that absolute Kan extensions and the codensity monad underlie the program optimisation of converting direct-style programs to continuation-passing style. |
| **Lava: Hardware Design in Haskell** | Bjesse, Claessen, Sheeran & Singh | ICFP 1998 | Presents Lava, a set of Haskell modules for specifying, simulating, verifying and generating hardware circuits, using monads, type classes and higher-order functions. |
| **Monad Comprehensions: A Versatile Representation for Queries** | Grust | Chapter in The Functional Approach to Data Management (Springer), 2004 | Book chapter arguing monad comprehensions are a uniform query representation for database and collection processing. |
| **Monads for functional programming** | Wadler | Advanced Functional Programming (Bastad summer school), 1995 | Describes using monads to structure functional programs, with case studies on an evaluator, in-place-update arrays and parsers. |
| **Parsley: The Fastest Parser Combinator Library in the West** | Willis | MEng dissertation, University of Bristol, 2018 | Dissertation on the design and implementation of Parsley, a high-performance parser combinator library. |
| **Persistent Software Transactional Memory in Haskell** | Krauter et al. | ICFP 2021 (PACMPL) | Extends Haskell STM to persistent (non-volatile) memory so transactions remain crash-consistent, and evaluates the implementation. |
| **Scans and Convolutions: A Calculational Proof of Moessner's Theorem** | Hinze | IFL 2008 | Introduces scans and convolutions as corecursion schemes for streams and uses them to give a calculational proof of Paasche's generalisation of Moessner's theorem. |
| **Species and Functors and Types, Oh My!** | Yorgey | Haskell Symposium 2010 | Teaches the theory of combinatorial species using functional-programming examples and introduces the Haskell species library. |
| **Stackless Scala With Free Monads** | Bjarnason | Scala Days 2012 | Introduces trampolines in Scala and extends them, via free monads, to eliminate stack use for all method calls, not only tail calls. |
| **Theory and Practice of Fusion** | Hinze, Harper & James | IFL 2010 | Uses recursive coalgebras to unify the theory of fusion techniques for eliminating intermediate data structures in functional programs. |
| **A tutorial on the universality and expressiveness of fold** | Hutton | Journal of Functional Programming 9(4), 1999 | Tutorial on the universal property of fold as a proof and definition principle, and on the unexpected expressive power of fold with tuples and first-class functions. |
| **What You Needa Know about Yoneda: Profunctor Optics and the Yoneda Lemma (Functional Pearl)** | Boisseau & Gibbons | ICFP 2018 | Derives the profunctor representation of optics (lenses, prisms) from the concrete getter/setter representation as an application of the Yoneda Lemma. |

### LLM Inference Serving

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Disaggregated Inference: Why the AI Network Is the Product](https://hedgehog.cloud/blog/disaggregated-inference-why-the-ai-network-is-the-product)** | Hedgehog | Blog post, 2026 | 🔍 Argues that once prefill and decode are split across machines, the network fabric moving KV cache between them becomes the core of the inference product. |
| **[Dynamo Disaggregation: Separating Prefill and Decode for Enhanced Performance](https://docs.nvidia.com/dynamo/latest/design-docs/disaggregated-serving)** | NVIDIA | Design doc | 🔍 NVIDIA Dynamo's design for disaggregated serving: separate prefill and decode workers, conditional disaggregation and KV-cache transfer between them. |
| **[llm-d: Kubernetes-native distributed inference (disaggregation architecture)](https://docs.vllm.ai/en/stable/deployment/integrations/llm-d/)** | llm-d project | Documentation | 🔍 Architecture for running vLLM at scale on Kubernetes with prefill/decode disaggregation and an inference-aware scheduler. |
| **[NIXL (NVIDIA Inference Xfer Library): overview and backend guide](https://docs.nvidia.com/nixl/getting-started/overview.md)** | NVIDIA | Documentation | 🔍 The transfer library and plugin API used to move KV-cache blocks between GPUs, hosts and storage in disaggregated inference; backends include UCX, GPUDirect Storage and POSIX. |
| **[NixlConnector Usage Guide](https://docs.vllm.ai/en/stable/features/nixl_connector_usage/)** | vLLM | Documentation | 🔍 How vLLM splits prefill and decode across separate instances and machines, using NIXL to hand the KV cache from prefill to decode workers. |
| **[Open Cluster Designs: Aligned AI Inference Fabric Reference Architecture](https://www.opencompute.org/documents/open-cluster-designs-aligned-ai-inference-fabric-reference-architecture-pdf)** | Open Compute Project (Hedgehog) | OCP reference architecture, 2026 | 🔍 An open RoCE network reference architecture for disaggregated AI inference clusters, contributed to OCP by Hedgehog. |
| **[What is llm-d and why do we need it?](https://www.redhat.com/en/blog/what-llm-d-and-why-do-we-need-it)** | Clyburn & Nuland (Red Hat) | Blog post, 2025 | 🔍 Explains llm-d's endpoint picker, including KV-cache-aware routing: the scheduler indexes cache state across vLLM replicas and sends requests sharing a prefix to the pod that already holds it. |

### Networks and Security

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **AlphaProof Code: Verifying Signal's Security at the Machine-Code Level** | Chaudhuri et al. | Google DeepMind, 2026 | Introduces AlphaProof Code, a multi-agent framework for writing Lean specifications and proving them against a formal AArch64 semantics, used to verify security properties of libsignal at the machine-code level. |

### Operating Systems and Systems Programming

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **The Linux Scheduler: a Decade of Wasted Cores** | Lozi et al. | EuroSys 2016 | Shows that the Linux thread scheduler often breaks the invariant that ready threads run on idle cores, describes the resulting performance bugs and their impact. |

### Programming Languages and Type Theory

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **"Panini-Backus Form" suggested** | Ingerman | Communications of the ACM (letter), 1967 | Short letter proposing that Backus Normal Form be renamed Panini-Backus Form, crediting Panini's grammar as a precursor. |
| **ADEV: Sound Automatic Differentiation of Expected Values of Probabilistic Programs** | Lew et al. | POPL 2023 | Extends forward-mode AD to compute unbiased gradient estimators of expected values of probabilistic programs, with a soundness proof. |
| **[Beyond Notations: Hygienic Macro Expansion for Theorem Proving Languages](https://arxiv.org/abs/2001.10490)** | Ullrich & de Moura | Logical Methods in Computer Science 18(2), 2022 | Presents a hygienic macro system for interactive theorem provers (Lean 4) that supports extensible syntax and tactic languages beyond ad hoc notation mechanisms. |
| **Characterizing functions mappable over GADTs** |  |  | Develops an algorithm that, given a term of a (deep) GADT type, returns the constraints a function must satisfy to be mappable over it. |
| **Computational lambda-calculus and monads** | Moggi | LICS 1989 | Gives a calculus based on a categorical semantics of computations that provides a correct basis for proving program equivalence independent of any specific computational model. |
| **A Denotational Semantics of Inheritance and its Correctness** | Cook & Palsberg | Information and Computation 114(2), 1994 | Presents a denotational model of inheritance as deriving modified versions of recursive definitions and proves it equivalent to an operational method-lookup semantics. |
| **Dependent Types in Haskell: Theory and Practice** | Eisenberg | PhD thesis, University of Pennsylvania, 2016 | Designs Dependent Haskell, extending GHC's core language and surface syntax with full dependent types, and gives its metatheory. |
| **[Do Be Do Be Do](https://arxiv.org/abs/1611.09259)** | Lindley, McBride & McLaughlin | POPL 2017 (arXiv) | Presents Frank, a strict functional language with a bidirectional effect type system in which functions generalise to operators that handle effects (multihandlers). |
| **Elastic Sheet-Defined Functions: Generalising Spreadsheet Functions to Variable-Size Input Arrays** | McCutchen et al. |  | Describes a principled way to generalise spreadsheet sheet-defined functions written over fixed-size arrays into elastic functions that work on inputs of arbitrary size. |
| **Fixpoints for the Masses: Programming with First-Class Datalog Constraints** | Madsen & Lhoták | OOPSLA 2020 | Proposes first-class Datalog constraints in Flix so Datalog programs can be constructed, composed and solved at run time from a functional language. |
| **[Formal verification with Claude: Rocq proofs over RISC-V binaries](https://www.anthropic.com/research/formal-verification)** | Anthropic Frontier Red Team & Theorem | Research post, 2026 | 🔍 Reports Claude generating machine-checked Rocq proofs for 239 OSS-Fuzz entry points across 123 open-source libraries, over compiled RISC-V binaries in a modeled Linux environment. |
| **Integrating Functional and Imperative Programming** | Gifford & Lucassen | LFP 1986 | Presents fluent languages with separate functional and imperative sublanguages, checked by a static system that infers both the type and effect class of every expression. |
| **An Introduction to Algebraic Effects and Handlers** | Pretnar | MFPS 2015 (ENTCS) | A tutorial on algebraic effects and handlers with examples, an operational semantics, a type-and-effect system, and reasoning principles. |
| **An Introduction to Quantum Programming in Quipper** | Green et al. | RC 2013 / arXiv:1304.5485 | A tutorial introduction to Quipper that implements a quantum algorithm and shows its key language features. |
| **Modular Formal Verification of Rust Programs with Unsafe Blocks** | Rahimi Foroushaani & Jacobs | KU Leuven technical report / arXiv:2212.12976, 2022 | Presents a VeriFast-based approach to modularly verifying Rust programs that contain unsafe blocks, building on RustBelt semantics. |
| **Notions of computation and monads** | Moggi | Information and Computation 93, 1991 | Introduces calculi based on a categorical (monadic) semantics of computations that give a correct basis for proving program equivalence across many notions of computation. |
| **On Understanding Data Abstraction, Revisited** | Cook | OOPSLA 2009 Onward! Essays | Contrasts objects and abstract data types as two distinct forms of data abstraction. |
| **OrcO: A Concurrency-First Approach to Objects** | Peters, Kitchin, Thywissen & Cook | OOPSLA 2016 | Presents OrcO, an object system for the Orc concurrent language designed with concurrency first. |
| **A Programmable Programming Language** | Felleisen et al. | Communications of the ACM, 2018 | Argues that language-oriented programming needs programmable programming languages, using Racket as the example. |
| **The Quantum Effect: A Recipe for QuantumPi** | Carette et al. | arXiv:2302.01885, 2023 | Builds a quantum programming language from two copies of a reversible classical language via free categorical constructions. |
| **Quipper: A Scalable Quantum Programming Language** | Green et al. | PLDI 2013 / arXiv:1304.3390 | Introduces Quipper, a scalable, functional, higher-order quantum programming language embedded in Haskell for describing large quantum algorithms. |
| **Reconciling Semantics and Reflection: Formalisms, Protocols, Applications and Architecture** | Rideau | PhD thesis draft, Ecole Nationale Superieure des Telecommunications, 2023 | Proposes an approach to reconciling semantics and reflection in computing systems, distinguishing three dimensions of meta-computation: ante/post (staging), hypo/hyper (semantic implementation and refinement) and back/fore (runtime effect control). |
| **[Synthesizing Quantum-Circuit Optimizers](https://arxiv.org/abs/2211.09691)** | Xu, Molavi, Pick et al. | PLDI 2023 (arXiv) | Presents an approach that automatically synthesizes verified rewrite rules for quantum-circuit optimizers from a gate set, producing optimizers that match or beat hand-written ones. |
| **Theorems for free!** | Wadler | FPCA 1989 | Shows how to derive a theorem from the type of any polymorphic function, using Reynolds' abstraction theorem for the polymorphic lambda calculus. |
| **A tutorial implementation of a dependently typed lambda calculus** | Loh, McBride & Swierstra | Fundamenta Informaticae, 2010 | Presents the type rules of a dependently typed core calculus with a Haskell implementation, highlighting the changes from a simply-typed calculus and extending it with data types. |
| **The Verse Calculus: a Core Calculus for Functional Logic Programming** | Augustsson et al. | Draft | Describes the Verse calculus, a core calculus for functional logic programming, equipped with a small-step rewrite semantics. |

### Software Design and Engineering

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **On the Impact of Programming Languages on Code Quality: A Reproduction Study** | Berger et al. | ACM TOPLAS (arXiv:1901.10220), 2019 | Reproduces Ray et al.'s study and finds that most claimed associations between language and defect rates do not hold. |
| **A Pattern Language for Creating Pattern Languages: 364 Patterns for Pattern Mining, Writing, and Symbolizing** | Iba & Isaku | PLoP 2016 | Presents a 364-pattern language for mining, writing and symbolizing pattern languages, distilled from the Iba Lab's work on 20+ pattern languages. |
| **[Rewrite it in Rust: A Computational Physics Case Study](https://arxiv.org/abs/2410.19146)** | Veytsman, Zhai, Ding & Sefkow | arXiv, 2024 | Compares C++ and Rust (serial and parallel) implementations of a physics simulation, measuring runtime and parallel code complexity. |
| **SemFix: Program Repair via Semantic Analysis** | Nguyen et al. | ICSE 2013 | Automated program repair via symbolic execution, constraint solving and program synthesis. |
| **Varv: Reprogrammable Interactive Software as a Declarative Data Structure** | Borowski et al. | CHI 2022 | Presents Varv, a system where interactive software is defined as a declarative data structure so users can reprogram it. |

### Theory of Computation

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Agarwal & Ben-David, quantum query complexity](https://arxiv.org/abs/2410.19062)** | Agarwal & Ben-David | arXiv, 2024 | Follow-up on query-complexity separations between quantum and classical computation. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |
| **Complexity and Completeness of Finding Another Solution and Its Application to Puzzles** | Yato | Master's thesis, University of Tokyo, 2003 | Defines ASP-completeness, the complexity of finding another solution given one, and proves it for puzzles such as Slitherlink and Cross Sum. |
| **[Deterministic n^O(log n) Graph Isomorphism](https://arxiv.org/abs/2611.01399)** | Hajiaghayi & JafariRaviz | arXiv, 2026 | 🔍 A deterministic n^O(log n) graph isomorphism algorithm, shipped with a Lean proof of both correctness and running time. A case study in my Lean-formalization write-up. |
| **[The Exponential Time Hypothesis is False](https://thenextweb.com/news/openai-exponential-time-hypothesis-false-kakeya-yang-mills)** | OpenAI | OpenAI manuscript (openai/math), 2026 | 🔍 Claims a subexponential algorithm for counting solutions to fixed-width CNF formulas, refuting ETH and with it SETH. Released for scrutiny; verification status as of writing unsettled. |
| **[Flat Origami is Turing Complete](https://arxiv.org/abs/2309.07932)** | Hull & Zakharevich | arXiv, 2023 | Proves that flat origami, viewed as a computational device, is Turing complete. |
| **A Fresh Look at the lambda-Calculus** | Accattoli | FSCD 2019 (invited talk) | Bird's-eye view of questions about the untyped lambda-calculus: measuring the complexity of terms, decomposing and implementing evaluation, and how these vary with the evaluation strategy. |
| **Interaction Combinators** | Lafont | Information and Computation 137, 1997 | Shows that a simple system of three interaction combinators is universal for interaction nets. |
| **MIP* = RE** | Ji, Natarajan, Vidick, Wright & Yuen | arXiv:2001.04383, 2020 | Proves that the class MIP* of languages decidable by a classical verifier interacting with entangled quantum provers equals RE, which refutes Connes' embedding conjecture. |
| **[The need for structure in quantum speedups](https://arxiv.org/abs/0911.0996)** | Aaronson & Ambainis | arXiv, 2009 | Shows that quantum speedups need structure in the problem; total functions allow at most polynomial advantage. 📝 Discussed in my notes: [Lean, Foundations, and the AI Formalization of Mathematics](../FP/lean-ai-formalization.md). |
| **[A Programming Language Oriented Approach to Computability](https://arxiv.org/abs/1402.2949)** | Karper | Bachelor thesis, University of Bern, 2013 | Develops computability theory using simple programming languages (FOR and WHILE) and transformations between them. |
| **[A proof of the Aaronson–Ambainis conjecture](https://psi.inc/research/aaronson-ambainis/)** | PSI (Physical Superintelligence) | Research announcement, 2026 | 🔍 An AI-produced proof of the 2008 Aaronson–Ambainis conjecture with a compact, Comparator-checked Lean formalization. A case study in my Lean-formalization write-up. |
| **[A proof of the Unique Games Conjecture](https://quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007)** | OpenAI | OpenAI manuscript (openai/math #102), 2026 | 🔍 A ~50-page claimed proof built on 2-to-2 games and a "latent alphabet gadget", with a Lean verification; a related 2-to-1 conjecture proof appeared alongside it. |
| **[Simulating Time With Square-Root Space](https://arxiv.org/abs/2502.17779)** | Williams | arXiv, 2025 | Shows that every multitape Turing machine running in time t can be simulated in space O(sqrt(t log t)), improving the 50-year-old Hopcroft-Paul-Valiant bound. |
| **A Tutorial Introduction to the Lambda Calculus** | Rojas | Lecture notes, FU Berlin, 1997 | Short introduction to the lambda calculus showing arithmetic and recursive definitions without named functions. |

## AI and Machine Learning

### Applied ML

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[BhasaAnuvaad Speech Translation Dataset](https://arxiv.org/abs/2411.04699)** |  | arXiv, 2024 | 📝 Discussed in my notes: [Kannada content landscape](../kannaDa/dnsbhat/kannada-content-landscape.md). |
| **DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning** | Xiong, Hoang & Wang | EMNLP 2017 / arXiv:1707.06690 | Trains a policy-based RL agent in a knowledge-graph embedding space to find multi-hop relational paths for reasoning. |
| **[Effective Transfer of Knowledge from English to Hindi Wikipedia](https://arxiv.org/abs/2412.05708)** |  | arXiv, 2024 | 📝 Discussed in my notes: [Kannada knowledge-gap analysis](../kannaDa/dnsbhat/kannada-knowledge-gap-analysis.md). |
| **[Generative AI and LLMs in Language Preservation](https://arxiv.org/abs/2501.11496)** |  | arXiv, 2025 | 📝 Discussed in my notes: [Kannada knowledge-gap analysis](../kannaDa/dnsbhat/kannada-knowledge-gap-analysis.md). |
| **[How To Use Decision Models for Evals](https://hamel.dev/blog/posts/decision-model-evals/)** | Husain & Saha | Blog post, 2026 | 🔍 Argues for small, trained decision models as cheap, consistent stand-ins for LLM-as-judge in evaluation pipelines, and how to build and validate them. |
| **iNLTK: Natural Language Toolkit for Indic Languages** | Arora | NLP-OSS Workshop, EMNLP 2020 | Open-source toolkit of pretrained models and augmentation for 13 Indic languages. |
| **[Kumo Tabular and Jev crash study](https://arxiv.org/abs/2610.10321)** |  | arXiv, 2026 | Crash-data study pairing Kumo Tabular with an LLM to read coded records. 📝 Discussed in my notes: [Decision Points as Effects](../FP/decision-points-as-effects.md). |
| **[KumoRFM-2](https://arxiv.org/abs/2604.12596)** |  | arXiv, 2026 | Second-generation relational foundation model that predicts directly over multi-table databases. 📝 Discussed in my notes: [Decision Points as Effects](../FP/decision-points-as-effects.md). |
| **[Mathematical Entities: Corpora and Benchmarks](https://arxiv.org/abs/2406.11577)** | Collard, de Paiva & Subrahmanian | arXiv, 2024 | Provides three annotated corpora of mathematical text (182,397 sentences with POS tags, lemmas and dependency trees) and evaluates NLP models on them. |
| **[A mechanistic study of tabular foundation models](https://arxiv.org/abs/2605.21288)** |  | arXiv, 2026 | Looks inside tabular foundation models to see what they compute. 📝 Discussed in my notes: [Decision Points as Effects](../FP/decision-points-as-effects.md). |
| **[Monolith: Real Time Recommendation System With Collisionless Embedding Table](https://arxiv.org/abs/2209.07663)** | Liu et al. | arXiv, 2022 | Describes ByteDance's Monolith, a real-time recommendation training system using collisionless embedding tables, addressing limits of general-purpose deep learning frameworks. |
| **MusicLM: Generating Music From Text** | Agostinelli et al. | arXiv:2301.11325, 2023 | Hierarchical sequence-to-sequence model generating high-fidelity music from text descriptions. |
| **[Pre-training ULMFiT on Synthetically Generated Code-Mixed Data for Hate Speech Detection](https://arxiv.org/abs/2010.02094)** | Arora | HASOC-Dravidian-CodeMix FIRE 2020 | System description for hate-speech detection in Tamil-English and Malayalam-English code-mixed text using ULMFiT pretrained on synthetic data. |
| **Recommending What Video to Watch Next: A Multitask Ranking System** | Zhao et al. | RecSys 2019 | Describes YouTube's large-scale multitask ranking system, which uses Multi-gate Mixture-of-Experts and a shallow tower to reduce selection bias from implicit feedback. |
| **Revisiting Low Resource Status of Indian Languages in Machine Translation** | Philip et al. | CODS-COMAD 2021 / arXiv:2008.04860, 2020 | Builds larger parallel corpora for Indian languages by aligning news and government sources, and trains multilingual NMT models that improve on earlier benchmarks. |
| **[TabPFN v2.5 uncertainty study](https://arxiv.org/abs/2606.01427)** |  | arXiv, 2026 | Studies how well TabPFN v2.5 quantifies uncertainty. 📝 Discussed in my notes: [Decision Points as Effects](../FP/decision-points-as-effects.md). |
| **[TabPFN-2.5](https://arxiv.org/abs/2511.08667)** |  | arXiv, 2025 | TabPFN-2.5: scaling the in-context tabular foundation model to larger datasets. 📝 Discussed in my notes: [Decision Points as Effects](../FP/decision-points-as-effects.md). |
| **[TabPFN-3.5 Technical Report](https://arxiv.org/abs/2609.17895)** |  | arXiv, 2026 | Technical report for the latest TabPFN in-context tabular foundation model. 📝 Discussed in my notes: [Decision Points as Effects](../FP/decision-points-as-effects.md). |
| **[WikiGap: Promoting Epistemic Equity](https://arxiv.org/abs/2505.24195)** |  | arXiv, 2025 | 📝 Discussed in my notes: [Kannada content landscape](../kannaDa/dnsbhat/kannada-content-landscape.md). |
| **[Wu's Method can Boost Symbolic AI to Rival Silver Medalists and AlphaGeometry to Outperform Gold Medalists at IMO Geometry](https://arxiv.org/abs/2404.06405)** | Sinha et al. | arXiv:2404.06405, 2024 | Shows Wu's algebraic method combined with AlphaGeometry solves 27/30 IMO geometry problems. |

### Deep Learning

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Algebraic Positional Encodings](https://arxiv.org/abs/2312.16045)** | Kogkalidis, Bernardy & Garg | arXiv, 2024 | Introduces a positional encoding for Transformers that maps the algebraic specification of a domain (sequences, grids, trees) to orthogonal operators, preserving its structure. |
| **Best of Both Worlds: Advantages of Hybrid Graph Sequence Models** | Behrouz et al. | arXiv, 2024 | Presents the Graph Sequence Model framework for applying sequence models (Transformers, linear RNNs) to graphs and analyses their strengths and weaknesses, motivating hybrid models. |
| **Coinductive guide to inductive transformer heads** | Nemecek | arXiv:2302.01834, 2023 | Argues transformer components can be expressed via combinatorial Hopf algebras. |
| **Everything is Connected: Graph Neural Networks** | Velickovic | arXiv:2301.08210, 2023 | Short survey of graph neural networks and their foundations. |
| **[Fourier Neural Operator for Parametric Partial Differential Equations](https://arxiv.org/abs/2010.08895)** | Li et al. | arXiv (ICLR 2021), 2020 | 🔍 Parameterizes the integral kernel of a neural operator in Fourier space, giving fast, resolution-independent solvers for families of PDEs such as Navier–Stokes. |
| **From Online Softmax to FlashAttention** | Ye | Course note, UW CSE 599M, 2023 | Explains why tiling self-attention is non-trivial and derives the FlashAttention computation from the online softmax trick. |
| **[Generalized Transformers from Applicative Functors](https://cybercat.institute/2025/02/12/transformers-applicative-functors/)** | Laakkonen | Blog post (Cybercat Institute), 2025 | 🔍 "Funcformer": re-expresses the Transformer with applicative functors so attention can operate over functions, graphs or probability distributions rather than just vectors, using diagrammatic tube notation. |
| **ImageNet Classification with Deep Convolutional Neural Networks** | Krizhevsky, Sutskever & Hinton | NIPS 2012 | AlexNet: a deep CNN trained on ImageNet that greatly reduced error on ILSVRC. |
| **KAN or MLP: A Fairer Comparison** | Yu, Yu & Wang | arXiv, 2024 | Compares KAN and MLP models under matched parameters and FLOPs across ML, vision, audio, NLP and symbolic-formula tasks, finding MLP generally better except for symbolic formula representation. |
| **[KAN: Kolmogorov-Arnold Networks](https://arxiv.org/abs/2404.19756)** | Liu et al. | arXiv:2404.19756, 2024 | Proposes networks with learnable activation functions on edges, inspired by the Kolmogorov-Arnold representation theorem, as an alternative to MLPs. |
| **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)** | Frankle & Carbin | ICLR 2019 | Finds that standard pruning uncovers subnetworks whose initialisations let them train effectively, and states the hypothesis that dense networks contain such 'winning ticket' subnetworks. |
| **Matryoshka Representation Learning** | Kusupati et al. | NeurIPS 2022 | Introduces Matryoshka Representation Learning, which encodes information at multiple granularities so one embedding can be truncated to fit downstream compute constraints. |
| **[Neural Operator: Learning Maps Between Function Spaces](https://arxiv.org/abs/2108.08481)** | Kovachki, Li, Liu et al. | arXiv (JMLR 2023), 2021 | 🔍 Generalizes neural networks to learn operators between infinite-dimensional function spaces, with discretization-invariant architectures for PDE solution maps. |
| **[On the Anatomy of Attention](https://arxiv.org/abs/2407.02423)** | Khatri, Laakkonen, Liu & Wang-Maścianica | arXiv, 2024 | 🔍 A category-theoretic, diagrammatic account of attention mechanisms that decomposes variants into common building blocks; cited by the Funcformer post. |
| **[A pattern language for machine learning tasks](https://arxiv.org/abs/2407.02424)** |  | arXiv, 2024 | 🔍 Companion paper proposing a diagrammatic pattern language for specifying machine-learning tasks independently of architecture; cited by the Funcformer post. |
| **Self Supervision Does Not Help Natural Language Supervision at Scale** | Weers et al. | arXiv:2301.07836, 2023 | Finds that adding image self-supervision to CLIP-style training gives no benefit at large scale. |
| **[SpikingBrain Technical Report: Spiking Brain-inspired Large Models](https://arxiv.org/abs/2509.05276)** | Pan, Feng, Zhuang et al. | arXiv, 2025 | 🔍 Presents SpikingBrain-7B and 76B-A12B: linear-attention / mixture-of-experts models converted from Qwen2.5, using spike-based activations and trained on non-NVIDIA (MetaX) GPUs. I compared it with Hinton's ideas — Forward-Forward, mortal computation, fast weights, event-driven spikes. |
| **Symbolic Discovery of Optimization Algorithms** | Chen et al. | arXiv:2302.06675, 2023 | Uses program search to discover Lion, a sign-momentum optimizer. |
| **[Understanding Attention in LLMs](https://arxiv.org/abs/2409.03752)** |  | arXiv, 2024 | 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **Understanding Back-Translation at Scale** | Edunov, Ott, Auli & Grangier | EMNLP 2018 / arXiv:1808.09381 | Studies ways to generate synthetic source sentences for back-translation in NMT and finds that sampling or noised beam outputs work best except in low-resource settings. |
| **[Understanding Transformer Reasoning on Graph Algorithms (Oct 2024)](https://arxiv.org/abs/2405.18512)** |  | arXiv, 2024 | Research analyzing how transformers internally represent and execute graph algorithms — finding that they implement something structurally similar to breadth-first search in their attention patterns when trained on graph traversal tasks. 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |

### Foundations

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Defining and Generating Compositional Structure](https://arxiv.org/abs/2610.20922)** | Elmoznino, Kasetty, Agüera y Arcas, Bengio & Lajoie | arXiv, 2026 | 🔍 Gives a formal, complexity-based definition of compositional structure in representations and a way to generate data with controlled compositionality; read together with its rose-tree follow-up. |
| **Handbook of Convergence Theorems for (Stochastic) Gradient Methods** | Garrigos & Gower | arXiv:2301.11235, 2023 | Collects convergence proofs for gradient descent, SGD and variants under standard assumptions. |
| **Heckerthoughts** | Heckerman | arXiv:2302.05449, 2023 | Memoir-style essays on the author's work in probability, Bayesian networks and AI. |

### Large Language Models

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Agentic Reasoning for Large Language Models — Survey](https://arxiv.org/abs/2601.12538)** |  | arXiv, 2026 | Comprehensive survey paper organizing the landscape of agentic LLM reasoning: foundational reasoning (chain-of-thought, reflection), self-evolving reasoning (reinforcement learning, online adaptation), and multi-agent coordination patterns. 📝 Discussed in my notes: [Reflection: Scala & FP](../Reflection/scala-functional-programming.md). |
| **[Are Language Models Agnostic to Linguistically Grounded Perturbations? A Case Study of Indic Languages](https://arxiv.org/abs/2412.10805)** | Ghosh, Dabre & Bhattacharyya | arXiv, 2024 | Studies whether pretrained language models are robust to linguistically grounded input perturbations across Indic languages and downstream tasks, compared with non-linguistic attacks. |
| **[Ask, and it shall be given: Turing completeness of prompting](https://arxiv.org/abs/2411.01992)** | Qiu, Xu, Bao & Tong | arXiv, 2024 | Shows that prompting is Turing-complete: a single finite-size Transformer can compute any computable function given a suitable prompt. |
| **Attention Is All You Need** | Vaswani et al. | NeurIPS 2017 / arXiv:1706.03762 | 🔍 Introduces the Transformer, a sequence transduction architecture based only on attention, with state-of-the-art translation results. Cited in the kyo-lambda-rlm design. |
| **[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)** | Wei et al. | NeurIPS 2022 (arXiv:2201.11903) | Shows that prompting with intermediate reasoning steps markedly improves LLM performance on arithmetic, commonsense and symbolic reasoning. |
| **A Comprehensive Survey on Pretrained Foundation Models: A History from BERT to ChatGPT** | Li et al. | arXiv:2302.09419, 2023 | Survey of pretrained foundation models across text, image and graph modalities. |
| **[Context Language Models](https://arxiv.org/abs/2609.37725)** | Shao, Shen, Yin et al. | arXiv, 2026 | 🔍 Language models that edit their own live context as a file; introduces Suffix Cache Reuse, reported to cut server-side compute by about 35% versus standard SGLang at matched performance. Compared against λ-RLM. |
| **Data Selection for Language Models via Importance Resampling** | Xie et al. | arXiv:2302.03169 (NeurIPS 2023) | Proposes DSIR, selecting pretraining data by importance resampling on hashed n-gram features. |
| **[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)** | DeepSeek-AI | arXiv, 2025 | The full technical report for DeepSeek-R1 — a reasoning model trained primarily with reinforcement learning (GRPO) that demonstrated that extended chain-of-thought reasoning can be elicited through RL without requiring massive supervised reasoning data. 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)** | DeepSeek-AI | arXiv, 2024 | Presents DeepSeek-V3, a 671B-parameter Mixture-of-Experts model (37B active per token) using Multi-head Latent Attention, auxiliary-loss-free load balancing and multi-token prediction. |
| **[DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)** | Shao et al. | arXiv, 2024 | Introduces DeepSeekMath 7B, pretrained further on 120B math-related tokens, reaching 51.7% on the MATH benchmark; also introduces the GRPO reinforcement learning algorithm. |
| **Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP** | Khattab et al. | arXiv:2212.14024, 2023 | DSP framework composing retrieval models and LMs in multi-step pipelines. |
| **Discovering Language Model Behaviors with Model-Written Evaluations** | Perez et al. | arXiv:2212.09251, 2022 | Uses LMs to generate evaluation datasets and uncovers behaviours such as sycophancy and inverse scaling. |
| **[DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714)** | Khattab et al. | arXiv, 2023 | 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **[Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102)** | Pope et al. | arXiv:2211.05102 (MLSys 2023), 2022 | Models and optimises partitioning strategies for efficient large-transformer inference on TPUs. |
| **Formal Algorithms for Transformers** | Phuong & Hutter | arXiv:2207.09238, 2022 | Self-contained, mathematically precise pseudocode overview of transformer architectures and training. |
| **The Future of Programming in the Age of Large Language Models** | Guha & Zorn | CCC/CRA-I Whitepaper, 2025 | Whitepaper on how LLMs are changing software development and computing education, and the research questions this raises. |
| **[GLM-130B: An Open Bilingual Pre-trained Model](https://arxiv.org/abs/2210.02414)** | Zeng et al. | arXiv:2210.02414 (ICLR 2023), 2022 | Technical report on training an open 130B-parameter English-Chinese language model. |
| **[GPT-5.2 on Olympiad-Level Science — FrontierScience Benchmark (Jan 2026)](https://arxiv.org/abs/2601.21165)** | OpenAI | arXiv, 2026 | An OpenAI paper introducing FrontierScience, a benchmark of expert-level scientific reasoning in physics, chemistry and biology. 📝 Discussed in my notes: [Reflection: Mathematics & Science](../Reflection/mathematics-science.md). |
| **Improving Language Models by Retrieving from Trillions of Tokens (RETRO)** | Borgeaud et al. | ICML 2022 / arXiv:2112.04426 | Introduces RETRO, which conditions an autoregressive LM on document chunks retrieved from a 2-trillion-token database, matching much larger models with far fewer parameters. |
| **[IndicGenBench: A Multilingual Benchmark to Evaluate Generation Capabilities of LLMs on Indic Languages](https://arxiv.org/abs/2404.16816)** | Singh et al. | arXiv:2404.16816 (ACL 2024) | Benchmark of generation tasks across 29 Indic languages to evaluate LLMs. |
| **[Intelligent AI Delegation — Framework](https://arxiv.org/abs/2602.11865)** |  | arXiv, 2026 | Research paper proposing a framework for adaptive task allocation and authority transfer in multi-agent AI systems: how to decide when to delegate to a subagent, how to transfer context, and how to aggregate results with appropriate uncertainty calibration. 📝 Discussed in my notes: [Reflection: Scala & FP](../Reflection/scala-functional-programming.md). |
| **[Knowledge Mechanisms in Large Language Models: A Survey and Perspective](https://arxiv.org/abs/2407.15017)** | Wang et al. | arXiv, 2024 | Reviews analysis of knowledge mechanisms in LLMs under a taxonomy of knowledge utilisation (memorisation, comprehension, creation) and knowledge evolution. |
| **[Language Imbalance Can Boost Cross-lingual Generalisation](https://arxiv.org/abs/2404.07982)** | Schafer et al. | arXiv:2404.07982, 2024 | Finds that training with a dominant main language can improve cross-lingual generalisation in language models. |
| **[Language Models Use Trigonometry to Do Addition](https://arxiv.org/abs/2502.00873)** | Kantamneni & Tegmark | arXiv, 2025 | Reverse-engineers how mid-sized LLMs compute addition, finding numbers represented as a generalised helix manipulated by a 'Clock' algorithm. |
| **Large Language Models are Zero-Shot Reasoners** | Kojima et al. | NeurIPS 2022 (arXiv:2205.11916) | Shows that adding 'Let's think step by step' elicits zero-shot chain-of-thought reasoning. |
| **[Large Linguistic Models Paper — Analyzing Theoretical Linguistic Abilities of LLMs](https://arxiv.org/abs/2305.00948)** |  | arXiv, 2023 | 📝 Discussed in my notes: [Reflection: Linguistics](../Reflection/linguistics.md). |
| **LeanAgent: Lifelong Learning for Formal Theorem Proving** | Kumarappan et al. | arXiv, 2024 | Presents LeanAgent, a lifelong-learning framework for LLM-based theorem proving in Lean that works across multiple evolving mathematical repositories. |
| **[LLM Reasoning State — State of LLMs Mar 2025](https://arxiv.org/abs/2503.22732)** |  | arXiv, 2025 | 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **Looped Transformers as Programmable Computers** | Giannou et al. | arXiv:2301.13196, 2023 | Shows that a looped transformer with hard-coded weights can emulate a general-purpose computer. |
| **Memorizing Transformers** | Wu et al. | ICLR 2022 | Adds a kNN-retrievable external memory of past key-value pairs so language models can memorise new data at inference time. |
| **Modern language models refute Chomsky's approach to language** | Piantadosi | Book chapter / LingBuzz preprint, 2023 | Argues that the success of large language models undermines innateness claims of generative linguistics. |
| **[More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression](https://arxiv.org/abs/2412.12706)** | Zhang et al. | arXiv, 2024 | Investigates the trade-off between number of tokens and numeric precision in LLM KV-cache compression, finding that storing more tokens at lower precision (quantized pruning) improves long-context performance. |
| **[OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/abs/2603.10165)** | Wang, Chen, Jin et al. | arXiv, 2026 | 🔍 Argues that next-state signals — user replies, tool outputs — are training data agents throw away, and recovers them with binary RL scored by a process-reward judge plus on-policy distillation for token-level hints. The headline 0.17→0.81 gain comes from a simulated setting. Basis of my openclaw-rl skill. |
| **[Opportunities and Challenges of LLMs for Low-Resource Languages](https://arxiv.org/abs/2412.04497)** |  | arXiv, 2024 | 📝 Discussed in my notes: [Kannada knowledge-gap analysis](../kannaDa/dnsbhat/kannada-knowledge-gap-analysis.md). |
| **PaLM: Scaling Language Modeling with Pathways** | Chowdhery et al. | arXiv:2204.02311 (JMLR 2023), 2022 | Describes PaLM, a 540B-parameter dense transformer trained with the Pathways system. |
| **Parsel: A Unified Natural Language Framework for Algorithmic Reasoning** | Zelikman et al. | arXiv:2212.10561, 2022 | Introduces Parsel, which has code LLMs decompose a hierarchical natural-language function description into parts, implement each, and validate them with tests to solve complex algorithmic tasks. |
| **[A Primer on the Inner Workings of Transformer-based Language Models](https://arxiv.org/abs/2405.00208)** | Ferrando, Sarti, Bisazza & Costa-jussa | arXiv, 2024 | Concise technical introduction to interpretability techniques for decoder-only Transformer language models and an overview of known internal mechanisms. |
| **[RAT — Retrieval Augmented Thinking](https://arxiv.org/abs/2403.05313)** |  | arXiv, 2024 | 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **[Recursive Language Models](https://arxiv.org/abs/2512.24601)** | Zhang, Kraska & Khattab | arXiv, 2025 | 🔍 Instead of reading a long prompt directly, the model loads it into a Python REPL as a variable and writes code to inspect, split and recursively call itself on the pieces. Behind the prompt-decomposition design in my Kyo agent runtime. |
| **[Rethinking Reflection in Pre-Training](https://arxiv.org/abs/2504.04022)** | Essential AI | arXiv, 2025 | Introduces deliberate errors into chains-of-thought and shows that language models' ability to recognise and correct them emerges during pre-training and improves with pre-training compute. |
| **Scaling Instruction-Finetuned Language Models** | Chung et al. | arXiv:2210.11416, 2022 | Flan-PaLM/Flan-T5: scales instruction finetuning across tasks, model sizes and chain-of-thought data. |
| **[Self-Organizing Graph Reasoning Evolves into a Critical State for Continuous Discovery Through Structural-Semantic Dynamics](https://arxiv.org/abs/2503.18852)** | Buehler | arXiv, 2025 | Analyses agentic graph-reasoning systems and reports that they evolve toward a critical state in which semantic entropy persistently dominates structural entropy, sustaining discovery. |
| **Self-Taught Evaluators** | Wang et al. | arXiv, 2024 | Improves LLM-as-a-Judge evaluators without human preference labels, using an iterative self-improvement scheme over synthetic contrasting model outputs. |
| **[Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)** | Takehi, Teoh, Zhang & Khattab | Blog post (MIT CSAIL), 2026 | 🔍 Reports that frontier LLMs can read a small network's raw weights, infer what they compute and edit them directly without training — e.g. lifting Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1% by changing 0.016% of its weights. |
| **SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot** | Frantar & Alistarh | ICML 2023 / arXiv:2301.00774 | Shows that GPT-family models such as OPT-175B and BLOOM-176B can be pruned to at least 50% sparsity in one shot without retraining, with minimal accuracy loss. |
| **[State of LLM Reasoning Models](https://arxiv.org/abs/2501.09686)** |  | arXiv, 2025 | 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **[A State-Update Prompting Strategy for Multi-turn Dialogue](https://arxiv.org/abs/2509.17766)** | Liu | arXiv, 2025 | 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **[Tamil-Llama Paper](https://arxiv.org/abs/2311.05845)** |  | arXiv, 2023 | 📝 Discussed in my notes: [Reflection: Machine Learning & AI](../Reflection/machine-learning-ai.md). |
| **Thinking Like Transformers** | Weiss, Goldberg & Yahav | ICML 2021 (arXiv:2106.06981) | Proposes RASP, a programming language modelling the computation of a transformer encoder, and uses it to analyse what transformers can compute. |
| **Towards a Science of AI Agent Reliability** | Rabanser et al. | arXiv, 2026 | Argues single accuracy metrics are insufficient for AI agents and proposes a holistic reliability profile (consistency across runs, robustness to perturbation, predictable failure, bounded error severity) grounded in safety-critical engineering. |
| **[Towards Large Language Models as Copilots for Theorem Proving in Lean](https://arxiv.org/abs/2404.12534)** | Song, Yang & Anandkumar | arXiv:2404.12534, 2024 | Introduces Lean Copilot, a framework for running LLM inference inside Lean to suggest tactics and premises. |
| **Tracr: Compiled Transformers as a Laboratory for Interpretability** | Lindner et al. | NeurIPS 2023 / arXiv:2301.05062 | Introduces Tracr, a compiler from RASP programs to transformer weights, which yields models with known mechanisms as ground truth for interpretability research. |
| **Transcending Scaling Laws with 0.1% Extra Compute** | Tay et al. | arXiv:2210.11399, 2022 | U-PaLM: continued training of PaLM with the UL2 objective (UL2R) for improved scaling. |
| **[Transformers as Algorithms: Generalization and Implicit Model Selection in In-context Learning](https://arxiv.org/abs/2301.07067)** | Li et al. | arXiv:2301.07067 (ICML 2023) | Treats in-context learning as algorithm learning and gives generalisation bounds. |
| **UL2: Unifying Language Learning Paradigms** | Tay et al. | arXiv:2205.05131, 2022 | Proposes Mixture-of-Denoisers pretraining that unifies span corruption and causal LM objectives. |
| **[Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety](https://arxiv.org/abs/2611.08438)** | Barez, Wu, Batra et al. (incl. Geva, Biderman, Bengio) | arXiv, 2026 | 🔍 A broad survey of mechanistic interpretability as a tool for AI safety — what circuit- and feature-level methods can and cannot yet tell us about model internals. (Reviewed from the abstract and overview; arXiv rate-limited the full text.) |
| **Understanding and Detecting Hallucinations in Neural Machine Translation via Model Introspection** | Xu et al. | TACL (arXiv:2301.07779), 2023 | Analyses source-contribution patterns to detect hallucinated NMT outputs. |
| **[Understanding LLMs: A Comprehensive Overview from Training to Inference](https://arxiv.org/abs/2401.02038)** | Liu et al. | arXiv, 2024 | Survey of techniques for training and running large language models, from data and architecture to inference. |
| **Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor** | Honovich et al. | arXiv:2212.09689, 2022 | Builds a large instruction-tuning dataset generated by prompting an LLM, rivalling human-curated data. |
| **What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot Generalization?** | Wang et al. | ICML 2022 (arXiv:2204.05832) | Large-scale comparison of LM architectures and objectives for zero-shot generalisation. |
| **[The Y-Combinator for LLMs: Solving Long-Context Rot with λ-Calculus](https://arxiv.org/abs/2603.20105)** | Roy, Ji, Tutunov, Zimmer & Bou-Ammar | arXiv, 2026 | 🔍 λ-RLM: instead of having the model write control code, a deterministic planner recursively applies a fixed set of pre-verified operators (split, map, filter, reduce) over the prompt and the LM handles only small leaf chunks. Basis of kyo-lambda-rlm. |
| **[Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956)** | Rasmussen et al. | arXiv, 2025 | Introduces Zep, a memory layer for LLM agents built on Graphiti, a temporally-aware knowledge graph engine, evaluated on the Deep Memory Retrieval benchmark against MemGPT. |

## Physics and Engineering

### Electrical Engineering

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **A general memristor-based partial differential equation solver** | Zidan et al. | Nature Electronics 1, 2018 | Reports a complete memristor-based hardware and software system that performs high-precision computing tasks such as solving partial differential equations. |
| **Linear symmetric self-selecting 14-bit kinetic molecular memristors** | Sharma et al. | Nature, 2024 | Reports molecular memristors with 14-bit resolution and linear, symmetric behaviour aimed at high-precision neuromorphic computing. |
| **Multiply accumulate operations in memristor crossbar arrays for analog computing** | Chen, Li, Li & Miao | Journal of Semiconductors 42, 2021 | Brief review of mapping analog matrices onto memristor crossbars to perform parallel multiply-accumulate operations via Ohm's and Kirchhoff's laws, covering neural-network accelerators and numerical computing. |
| **XMAP: Programming Memristor Crossbars for Analog Matrix-Vector Multiplication: Towards High Precision using Representable Matrices** | Uysal, Zhang, Jha & Ewetz | IEEE TCAD, 2020 | Proposes XMAP, a framework for mapping arbitrary matrices onto memristor crossbars to improve the precision of analog matrix-vector multiplication despite parasitics and device variation. |

## Linguistics and Languages

### Dravidian and Kannada Linguistics

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **A Bayesian phylogenetic study of the Dravidian language family** | Kolipakam et al. | Royal Society Open Science 5:171504, 2018 | Applies Bayesian phylogenetic inference (BEAST 2) to Dravidian basic vocabulary to estimate the family's subgrouping and an age of about 4,000-5,500 years. |
| **An Efficient Kannada Dialect Identification Systems using NLP** | Anusha & Aditya | Grenze International Journal of Engineering and Technology | Analyses datasets and features for automatically identifying Kannada dialects, which fall into coastal, northern, southwestern and southern groups. |
| **Proto-Dravidian Agriculture** | Southworth |  | Uses reconstructed Proto-Dravidian vocabulary for crops, tools and farming practices to infer the agriculture of early Dravidian speakers, aimed at bridging historical linguistics and archaeology. |
| **Proto-Dravidian Languages in Indus Civilization: Ultraconserved Tooth-word Reveals Deep Ancestry** | Mukhopadhyay | SSRN preprint (later Palgrave Communications 2021), 2020 | Argues that Mesopotamian and Persian words for ivory and elephant were borrowed from a Proto-Dravidian word 'pīlu' used in the Indus civilization and related to the tooth-word '*pal'. |
| **Rice in Dravidian** | Southworth | Rice 4:142-148, 2012 | Uses linguistic evidence to trace Proto-Dravidian society and its agricultural vocabulary, the movement of Dravidian speakers into South Asia, and their role in rice cultivation. |
| **Treatment of Case Markers in Sabdamanidarpanam and Tolkappiam: A Comparative Study** | Kodagunti | 2021 | Compares how the traditional grammars of Kannada (Sabdamanidarpana) and Tamil (Tolkappiyam) describe case markers, showing similar forms in the early stages of both languages. |

### Historical Linguistics and Scripts

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **The Decipherment of Linear Elamite Writing** | Desset et al. | Zeitschrift fur Assyriologie 112(1), 2022 | Presents a decipherment of Linear Elamite, used in southern Iran c. 2300-1880 BCE, starting from eight inscribed silver beakers published in 2018. |
| **Drift, Convergence, and the Ergative Cycle** | Kiparsky |  | Examines drift, convergence and cyclic change as problems for the theory of language change, using the evolution of Indo-Iranian case and agreement syntax from nominative/accusative to ergative alignment. |
| **Gold and 'ratti' signs inscribed on Mohenjo-Daro's gold-assaying needles, fish-sign inscriptions signifying gemstones concentrated near lapidaries: Indus script's taxed commodities** | Mukhopadhyay | SSRN preprint, 2022 | Claims that certain Indus inscriptions record gold and 'ratti' weights and that fish signs denote gemstones, extending the author's taxation reading of the Indus script. |
| **Guild-based trading, taxation, tax farming, trade and craft licensing, access control: Economic practices of Indus civilization encoded in Indus script** | Mukhopadhyay | SSRN preprint, 2022 | Argues that Indus inscriptions are logographic, that stamp seals were mainly revenue and trade-regulation stamps, and that tablets were licenses for tax collectors and traders. |
| **The Hybrid Origin of Brāhmī Script from Aramaic, Phoenician and Greek Letters** | Pillai | Indi@logs 10, 93–122, 2023 | Proposes a letter-by-letter derivation of Brāhmī from Aramaic, with contributions from Phoenician and Greek letters. |
| **Indus Musicians in Mesopotamia: Bull Lyre of Indus Valley and 90 Words that Harappans May Have Spoken** | Vyas | Working draft, 2020 | Argues that Harappan musicians were present in Mesopotamia and links the bull lyre to the Indus Valley, proposing about 90 words that Harappans may have spoken. |
| **Interrogating Indus inscriptions to unravel their mechanisms of meaning conveyance** | Mukhopadhyay | Palgrave Communications 5, 73, 2019 | An epigraphic analysis arguing that Indus seals and tablets were formalized data carriers, like proto-cuneiform administrative tablets, using document-specific and linguistic signs. |
| **The Kikkuli Text. Hittite Training Instructions for Chariot Horses in the Second Half of the 2nd Millennium B.C. and Their Interdisciplinary Context** | Raulwing | 2009 | Examines the Hittite Kikkuli horse-training instructions and their philological, linguistic and historical context. |
| **Linear Elamite Writing** | Desset | The Elamite World (Routledge), ch. 20, 2018 | A survey of the Linear Elamite script: its corpus, history of research, sign inventory and progress toward decipherment. |
| **Modern Colloquial Eastern Elamite** | McAlpin | Al-Burz 14(1), 64–123, 2022 | Argues that a modern colloquial descendant of Eastern Elamite survives, and presents its phonology, morphology and vocabulary. |
| **Probabilistic Models of Evolution and Language Change** | Bouchard-Cote | Technical Report UCB/EECS-2010-153 (PhD thesis), UC Berkeley | Develops probabilistic models of evolution applied to language change, such as reconstructing ancestral word forms. |
| **Proposal for encoding the Indus script in Plane 1 of the UCS** | Everson | ISO/IEC JTC1/SC2/WG2 N1959, 1999 | Working-group proposal to encode the Indus script (386 characters) in Plane 1 of the Universal Character Set. |
| **Proto-Elamite and Linear Elamite, a Misunderstood Relationship?** | Dahl | 2023 | Argues that Linear Elamite was a new script created in the late 3rd millennium BC, inspired by recovered proto-Elamite tablets and Old Akkadian cuneiform, rather than a continuous development of proto-Elamite. |
| **Supplementary Materials for: Language trees with sampled ancestors support a hybrid model for the origin of Indo-European languages** | Heggarty et al. | Science 381, eabg0818, 2023 | Supplementary methods, figures and tables for a Bayesian phylogenetic study of Indo-European that uses ancient languages as sampled ancestors and supports a hybrid Caucasus/Steppe origin model. |
| **Unicode Encoding Proposal for the Indus Script - Early Draft** | Sarkar | Preprint (Zenodo 10.5281/zenodo.7794001), 2023 | Early draft proposal for encoding Indus script signs in Unicode. |

### Sanskrit and Indo-Aryan Linguistics

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Data-driven dependency parsing of Vedic Sanskrit** | Hellwig, Nehrdich & Sellmer | Language Resources and Evaluation 57, 2023 | Describes the first data-driven dependency parser for Vedic Sanskrit, testing input feature representations including contextual embeddings and analysing parsing errors. |
| **The Death of Sanskrit** | Pollock | Comparative Studies in Society and History, 2001 | Examines the decline of Sanskrit as a language of literary and intellectual creativity in precolonial South Asia, against nationalist myths about its history. |
| **Developments of nasals in early Indo-Aryan: anunasika and anusvara** | Cardona | Tokyo University Linguistic Papers 33, 2013 | Establishes that the anunasika/anusvara distinction drawn by Panini and the phonetic treatises reflects a real linguistic difference between nasalised vowels/nasal stops and a post-vocalic nasal segment. |
| **In Pāṇini We Trust: Discovering the Algorithm for Rule Conflict Resolution in the Aṣṭādhyāyī** | Rajpopat | PhD thesis, University of Cambridge, 2021 | Argues that Pāṇini's metarule 1.4.2 means choosing the rule that applies to the right-hand operand, which resolves rule conflicts in the Aṣṭādhyāyī without ad hoc exceptions. |
| **A Mathematical Analysis of Panini's Sivasutras** | Petersen | Journal of Logic, Language and Information 13, 2004 | Gives a set-theoretic argument that Panini's ordering of phonological segments in the Sivasutras is optimal for representing natural classes as intervals. |
| **On Pāṇini and the Generative Capacity of Contextualized Replacement Systems** | Penn & Kiparsky | COLING 2012 | Re-examines claims about the formal expressive power of Pāṇini's rule system relative to finite-state and context-free formalisms. |
| **[One Model is All You Need: ByT5-Sanskrit, a Unified Model for Sanskrit NLP Tasks](https://arxiv.org/abs/2409.13920)** | Nehrdich, Hellwig & Keutzer | arXiv, 2024 | Presents ByT5-Sanskrit, a pretrained model for Sanskrit NLP evaluated on word segmentation and Vedic dependency parsing. |
| **Panini** |  | Handbook chapter (history of phonology) | Describes Panini's grammar of Sanskrit and its goal of a consistent, exhaustive and maximally concise formal analysis, and its phonetic and phonological background. |
| **Substrate Languages in Old Indo-Aryan (Rgvedic, Middle and Late Vedic)** | Witzel | Electronic Journal of Vedic Studies 5(1), 1999 | Surveys non-Indo-Aryan substrate vocabulary in Vedic texts by region and period, from the Greater Panjab eastwards. |

## Other

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Ancient DNA from Protohistoric Period Cambodia indicates that South Asians admixed with local populations as early as 1st–3rd centuries CE** | Changmai et al. | Scientific Reports 12, 2022 | Ancient genomes from Vat Komnou, Cambodia, show South Asian admixture into Mainland Southeast Asian populations by the 1st–3rd centuries CE. |
| **Ancient DNA reveals pervasive directional selection across West Eurasia** | Akbari et al. | Nature, 2026 | Uses large ancient-DNA samples to distinguish sustained directional selection from shifts due to migration and population structure in West Eurasian populations. |
| **An Ancient Harappan Genome Lacks Ancestry from Steppe Pastoralists or Iranian Farmers** | Shinde et al. | Cell 179(3), 2019 | Reports a genome from Rakhigarhi in the Indus Valley Civilization with no detectable Steppe or Anatolian/Iranian farmer ancestry, from a population that is the largest source of ancestry for South Asians. |
| **[Complex peopling history and expansion events inferred from large-scale modern and ancient Y chromosome sequences](https://doi.org/10.1126/sciadv.adu7935)** | He, Wang, Wang et al. | Science Advances, 2026 | 🔍 A large modern-and-ancient Y-chromosome study of China. Modern Indian and South Chinese paternal lines share only a deep FT-M89 trunk (~52–70 thousand years ago), with no Neolithic or later shared lineages; F lineages persist in Guangdong and Yunnan. |
| **[Crosstalk of Magnesium and Serum Lipids in Dyslipidemia and Associated Disorders: A Systematic Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8146023/)** |  | Systematic review (PMC), 2021 | 🔍 Reviews the links between magnesium status and serum lipids in dyslipidemia and related disorders; the supplementation evidence rests on 29 randomized controlled trials. |
| **The Genetic Origin of the Indo-Europeans** | Lazaridis et al. | bioRxiv preprint, 2024 | Ancient-DNA study tracing the ancestry of Indo-European speakers to Caucasus-Lower Volga populations. |
| **Growing in a Foreign World: For a History of the 'Meluhha Villages' in Mesopotamia in the 3rd Millennium BC** | Vidale | Melammu Symposia 4, 2004 | Archaeological and textual evidence for communities of Indus (Meluhhan) people settled in Mesopotamia in the 3rd millennium BC. |
| **The origin and dispersal of millet cultivation in India** | Singh | Interregional Contacts in the Later Prehistory of Northeastern Africa (Poznan), 1996 | Reviews archaeological evidence for the origin and spread of millet cultivation in India. |
| **The Persian plateau served as hub for Homo sapiens after the main out of Africa dispersal** | Vallini et al. | Nature Communications, 2024 | Combines genetic and palaeoecological evidence to argue that the Persian plateau hosted the population ancestral to non-Africans between the out-of-Africa dispersal and later expansions. |

### Health and Nutrition

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Assessment of Metabolic Flexibility by Means of Measuring Blood Lactate, Fat, and Carbohydrate Oxidation Responses to Exercise in Professional Endurance Athletes and Less-Fit Individuals](https://doi.org/10.1007/s40279-017-0751-x)** | San-Millán & Brooks | Sports Medicine, 2018 | 🔍 (via *Outlive*) Professional cyclists kept blood lactate low and fat oxidation high even at high power, while sedentary men with metabolic syndrome had higher resting lactate than the professionals had during hard work. This is the basis for metabolic Zone 2. |
| **[Dietary plant-to-animal protein ratio and risk of cardiovascular disease in 3 prospective cohorts](https://pubmed.ncbi.nlm.nih.gov/39631999/)** | Glenn, Wang, Tessier et al. | American Journal of Clinical Nutrition, 2024 | 🔍 In three large US cohorts, a higher ratio of plant to animal protein was associated with lower cardiovascular and especially coronary heart disease risk. (Ran with an editorial by Mariotti.) |
| **[Dietary Protein Intake and Risk of Type 2 Diabetes in US Men and Women](https://pmc.ncbi.nlm.nih.gov/articles/PMC4832052/)** | Malik et al. | American Journal of Epidemiology, 2016 | 🔍 Higher animal-protein intake was associated with higher type 2 diabetes risk, while replacing animal with vegetable protein was associated with lower risk, in the Nurses' Health Studies and Health Professionals Follow-up Study. |
| **[Effects of Exercise Training on Mitochondrial and Capillary Growth in Human Skeletal Muscle: A Systematic Review and Meta-Regression](https://doi.org/10.1007/s40279-024-02120-2)** | Mølmen, Almquist & Skattebo | Sports Medicine, 2025 | 🔍 Endurance, high-intensity and sprint training raised mitochondrial content similarly (~23–27%) and VO₂max similarly (9–12%), with sprints most efficient per hour. Capillary density rose only with endurance and high-intensity training, and most with endurance. (Read via a summary write-up.) |
| **[Effects of creatine supplementation with and without exercise and diet intervention on body composition, cognitive function, and markers of health in middle-aged and older adults](https://doi.org/10.1080/15502783.2026.2716273)** | Chun, Kreider et al. | JISSN, 2026 | 🔍 Texas A&M trial: creatine increased lean mass and strength in middle-aged and older adults even without exercise; combined with exercise and a calorie-reduced diet it further improved strength and reduced body fat. |
| **[Leisure Time Physical Activity and Mortality: A Detailed Pooled Analysis of the Dose-Response Relationship](https://doi.org/10.1001/jamainternmed.2015.0533)** | Arem et al. | JAMA Internal Medicine, 2015 | 🔍 In ~661,000 adults, meeting the leisure-time activity guideline gave most of the mortality benefit (31% lower). Benefit topped out at 39% around 3–5× the guideline, with no harm at 10×. |
| **[MCT1-dependent mitochondrial lactate import sustains cardiac metabolism](https://doi.org/10.1038/s41586-026-11182-3)** | Cluntun et al. | Nature, 2026 | 🔍 Shows that the transporter MCT1 imports lactate into heart mitochondria and that this import sustains cardiac energy metabolism — the heart's "backup" fuel route. Read with the accompanying Nature News & Views. |
| **[Methionine-supplemented longevity diet increases growth hormone, GLP-1, and FGF21; reduces frailty; and promotes healthspan](https://doi.org/10.1016/j.cmet.2026.05.015)** | Fanti et al. (Longo lab) | Cell Metabolism, 2026 | 🔍 Reports that a low-protein, plant-based longevity diet supplemented with methionine raised growth hormone, GLP-1 and FGF21, reduced frailty and promoted healthspan. |
| **[Optimal dietary patterns for healthy aging](https://doi.org/10.1038/s41591-025-03570-5)** | Tessier et al. | Nature Medicine, 2025 | 🔍 Compares eight dietary-pattern indices over ~30 years of follow-up in two large US cohorts against a composite "healthy aging" outcome (surviving to 70 free of major chronic disease with intact cognitive, physical and mental health); all healthy patterns helped, with the AHEI strongest. |
| **[Physical activity and risk of breast cancer, colon cancer, diabetes, ischemic heart disease, and ischemic stroke events: systematic review and dose-response meta-analysis](https://doi.org/10.1136/bmj.i3857)** | Kyu et al. | BMJ, 2016 | 🔍 A Global Burden of Disease dose-response meta-analysis of total physical activity across 174 cohort studies: most of the risk reduction came by 3,000–4,000 MET-minutes a week (≈900 minutes of brisk walking), with diminishing returns beyond. |
| **[Reference Values for DXA-Derived Visceral Adipose Tissue in Adults 40 Years and Older from a European Population: The Tromsø Study 2015–2016](https://doi.org/10.1155/2021/6634536)** |  | Journal of Obesity, 2021 | 🔍 Population reference values (by age and sex) for visceral fat measured by DXA in adults 40+ from the Tromsø Study, for interpreting individual scans. |
| **[Sitting, squatting, and the evolutionary biology of human inactivity](https://pubmed.ncbi.nlm.nih.gov/32152112/)** | Raichlen et al. | PNAS, 2020 | 🔍 Hadza hunter-gatherers are sedentary for many hours a day but spend much of it squatting or kneeling, which keeps leg muscles more active than chair-sitting — "active rest" as a possible reason their inactivity carries less health cost. |
| **[Weight gain leads to greater adverse metabolic responses in South Asian compared with white European men: the GlasVEGAS study](https://doi.org/10.1038/s42255-024-01101-z)** | McLaren, Gao, Ghouri et al. | Nature Metabolism, 2024 | 🔍 A controlled weight-gain study: with similar gains, South Asian men showed larger adverse metabolic changes than white European men, linked to differences in where fat is stored and in fat-cell function. (Read via write-ups, not the full paper.) |
| **[When we sit: textile electromyography identifies decreasing muscle activity and implications for metabolic health](https://jyx.jyu.fi/handle/123456789/114063)** | Brakenridge et al. | npj (Exercise Medicine and Health), 2026 | 🔍 Uses EMG-instrumented shorts to measure leg-muscle activity across the day; muscle activity falls off during prolonged sitting, with ~25 minutes of uninterrupted sitting emerging as a possible tipping point for metabolic health. |
