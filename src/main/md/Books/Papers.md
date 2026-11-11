# Papers

Research papers, theses and technical reports I keep in the Google Drive *Books › Papers* folder, arranged top-down by subject — the same layout as [Technical](Technical.md). Each entry gives the authors, where it appeared, and a line on what it does.

---

## Overview

- **[Mathematics](#mathematics)** (14)
  - [Category Theory](#category-theory) (5)
  - [Foundations and Logic](#foundations-and-logic) (1)
  - [History of Mathematics](#history-of-mathematics) (4)
  - [Recreational Mathematics](#recreational-mathematics) (3)
  - [Topology and Geometry](#topology-and-geometry) (1)
- **[Computer Science](#computer-science)** (66)
  - [Algorithms and Data Structures](#algorithms-and-data-structures) (6)
  - [Compilers and Language Implementation](#compilers-and-language-implementation) (4)
  - [Computer Architecture and Parallelism](#computer-architecture-and-parallelism) (4)
  - [Distributed and Data Systems](#distributed-and-data-systems) (6)
  - [Functional Programming](#functional-programming) (24)
  - [Networks and Security](#networks-and-security) (1)
  - [Operating Systems and Systems Programming](#operating-systems-and-systems-programming) (1)
  - [Programming Languages and Type Theory](#programming-languages-and-type-theory) (14)
  - [Software Design and Engineering](#software-design-and-engineering) (1)
  - [Theory of Computation](#theory-of-computation) (5)
- **[AI and Machine Learning](#ai-and-machine-learning)** (24)
  - [Applied ML](#applied-ml) (2)
  - [Deep Learning](#deep-learning) (6)
  - [Large Language Models](#large-language-models) (16)
- **[Physics and Engineering](#physics-and-engineering)** (4)
  - [Electrical Engineering](#electrical-engineering) (4)
- **[Linguistics and Languages](#linguistics-and-languages)** (15)
  - [Dravidian and Kannada Linguistics](#dravidian-and-kannada-linguistics) (3)
  - [Historical Linguistics and Scripts](#historical-linguistics-and-scripts) (6)
  - [Sanskrit and Indo-Aryan Linguistics](#sanskrit-and-indo-aryan-linguistics) (6)
- **[Other](#other)** (1)

---

## Mathematics

### Category Theory

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Higher category theory](https://arxiv.org/abs/2401.14311)** | Haugseng | Encyclopedia of Mathematical Physics (arXiv), 2024 | Introduction to the homotopical theory of higher categories, motivating the definitions of infinity-categories and (infinity,n)-categories. |
| **Intro to Category Theory: Natural Transformations** |  | Lecture notes | Lecture notes defining natural transformations as transformations between functors, with examples. |
| **Physics, Topology, Logic and Computation: A Rosetta Stone** | Baez & Stay | arXiv, 2009 | Explains, using symmetric monoidal categories, the analogy between Feynman diagrams in physics, cobordisms in topology, proofs in logic and programs in computation. |
| **Sheaf Theory** | Centazzo & Vitale | Categorical Foundations (book chapter VII), 2004 | Introductory chapter on sheaf theory, motivated by local-to-global problems in analysis. |
| **Value Iteration is Optic Composition** | Hedges & Rodriguez Sakamoto |  | Shows that value improvement in dynamic programming is composition in a category of optics, as a step toward describing reinforcement learning with parametrised optics. |

### Foundations and Logic

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **A Lean proof of Fermat's Last Theorem (blueprint)** | Buzzard & Taylor | Project blueprint, 2025 | Blueprint for formalising a proof of Fermat's Last Theorem in Lean, covering the reductions to Frey packages, Galois representations and elliptic curves. |

### History of Mathematics

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Concepts and Categories in Perspective** | Mac Lane | A Century of Mathematics in America, Part I (AMS), 1988 | Mac Lane's personal account of the development of algebra, algebraic topology and category theory in American mathematics. |
| **Development of Calculus in India** | Ramasubramanian & Srinivas | 2010 | Overview of calculus in the Indian mathematical tradition, from Aryabhata to Narayana Pandita and the Kerala School as presented in the Yuktibhasa. |
| **The ET Interview: Professor C.R. Rao** | Bera | Econometric Theory 19, 2003 | Long interview with statistician C.R. Rao covering his life and career, from joining the Indian Statistical Institute onward. |
| **Life and Work of Alexander Grothendieck** | Chai & Oort |  | Looks back at Grothendieck's life and his mathematical achievements in the period, roughly 1948-1970, in which he transformed several branches of mathematics. |

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
| **Graph Processing Library in Rust** | Bihani & Gagneja | Stanford course project report, 2017 | Explores three approaches to representing and processing graphs in Rust and compares their performance with the C++ SNAP library. |
| **[Optimal Bounds for Open Addressing Without Reordering](https://arxiv.org/abs/2501.02305)** | Farach-Colton, Krapivin & Kuszmaul | arXiv, 2025 | Constructs open-addressed hash tables without reordering that achieve much better expected search complexity than previously thought, disproving Yao's conjecture, with matching lower bounds. |
| **RRB-Trees: Efficient Immutable Vectors** | Bagwell & Rompf | EPFL technical report, 2011 | Introduces Relaxed Radix Balanced Trees, which give immutable vectors O(log N) concatenation, insert-at and split while keeping fast indexing, update and iteration. |
| **[The Ubiquitous Skiplist: A Survey of What Cannot be Skipped About the Skiplist and its Applications in Big Data Systems](https://arxiv.org/abs/2403.04582)** | Xing, Vadrevu & Aref | arXiv, 2024 | Surveys skiplists and their variants, their use in systems, and compares them with tree-based structures. |

### Compilers and Language Implementation

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Counting Immutable Beans: Reference Counting Optimized for Purely Functional Programming](https://arxiv.org/abs/1908.05647)** | Ullrich & de Moura | IFL 2019 | Explores reference-counting optimisations such as destructive updates for an eager purely functional language (Lean 4), including borrowed references and inferred borrow annotations. |
| **LLVM: An Infrastructure for Multi-Stage Optimization** | Lattner | MS thesis, University of Illinois at Urbana-Champaign, 2002 | Presents the design and implementation of LLVM, a compiler infrastructure supporting optimisation across compile, link, install and run time. |
| **A Mechanically Verified Garbage Collector for OCaml** | Shamsu et al. | 2025 | Presents a mechanically verified garbage collector for OCaml, whose GC has a copying minor heap and an incremental mark-and-sweep major heap. |
| **Retrofitting Parallelism onto OCaml** | Sivaramakrishnan et al. | ICFP 2020 | Describes the design, implementation and evaluation of a mostly-concurrent garbage collector for multicore OCaml while preserving compatibility with existing code. |

### Computer Architecture and Parallelism

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Powerlist: A Structure for Parallel Recursion** | Misra | ACM TOPLAS, 1994 | Proposes the powerlist data structure for succinctly describing recursive data-parallel algorithms (FFT, Batcher sort, prefix sum) and using its algebra to derive their properties. |
| **Understanding Real-World Concurrency Bugs in Go** | Tu, Liu, Song & Zhang | ASPLOS 2019 | Empirical study of concurrency bugs in real Go programs, comparing message passing with shared-memory synchronisation as sources of errors. |
| **What Every Programmer Should Know About Memory** | Drepper | 2007 | Explains the structure of memory subsystems and CPU caches on commodity hardware and what programs should do to use them well. |
| **What every systems programmer should know about concurrency** | Kline | 2020 | Covers concurrency fundamentals below the level of mutexes and semaphores: atomicity, memory ordering, and how compilers and hardware reorder code. |

### Distributed and Data Systems

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Architecture of a Database System** | Hellerstein, Stonebraker & Hamilton | Foundations and Trends in Databases 1(2), 2007 | Surveys the systems-design architecture of database management systems: process models, parallelism, storage, transactions and shared components. |
| **ClickHouse - Lightning Fast Analytics for Everyone** | Schulze et al. | VLDB 2024 | Presents an overview of ClickHouse, a column-oriented OLAP database designed for high-performance analytics over internet-scale data with many concurrent queries and real-time latencies. |
| **Don't Thrash: How to Cache Your Hash on Flash** | Bender et al. | VLDB 2012 | Presents alternatives to the Bloom filter, starting with the quotient filter, and designs for operating such filters efficiently on flash storage. |
| **[Flo: a Semantic Foundation for Progressive Stream Processing](https://arxiv.org/abs/2411.08274)** | Laddad, Cheung, Hellerstein & Milano | POPL 2025 | Identifies streaming progress and eager execution as semantic properties shared by streaming languages and formalises them in Flo, a parameterised streaming language with a type system for bounded and unbounded streams. |
| **Structured Interacting Computations (A position paper)** | Cook & Misra | 2008 | Describes the design philosophy of Orc: structuring concurrent programs hierarchically and allowing controlled interaction between subsystems by value passing. |
| **Workflow Patterns in Orc** | Cook, Patwardhan & Misra | COORDINATION 2006 | Implements van der Aalst's workflow patterns in Orc, a process calculus for orchestrating wide-area computations, as reusable definitions. |

### Functional Programming

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **'do' Unchained: Embracing Local Imperativity in a Purely Functional Language (Functional Pearl)** | Ullrich & de Moura | ICFP 2022 | Extends do-notation in Lean 4 with imperative features such as local mutation, early return and loops, translated into monadic code. |
| **Applicative programming with effects (Functional Pearl)** | McBride & Paterson | Journal of Functional Programming, 2008 | Introduces applicative functors as an abstraction of effectful applicative-style programming weaker than monads, with their laws, generic operations and relation to monads and arrows. |
| **Arrows and computation** | Paterson | The Fun of Programming (chapter), 2003 | Explores function-like 'notions of computation' through the common arrows interface, its subclasses, and its relation to monads. |
| **Build Systems a la Carte** | Mokhov, Mitchell & Peyton Jones | ICFP 2018 | Offers a systematic, executable framework for developing and comparing build systems, separating their components so they can be recombined into new build systems. |
| **Caml trading - experiences with functional programming on Wall Street** | Minsky & Weeks | Journal of Functional Programming 18(4), 2008 | Describes Jane Street Capital's use of OCaml as its primary language for trading systems, research and systems software, and why it values the language. |
| **Conjugate Hylomorphisms, Or: The Mother of All Structured Recursion Schemes** | Hinze, Wu & Gibbons | POPL 2015 | Develops a toolbox for assembling recursive coalgebras, based on a conjugate rule parametrised by an adjunction, unifying structured recursion schemes as hylomorphisms. |
| **Design Patterns for Parser Combinators (Functional Pearl)** | Willis & Wu | Haskell Symposium 2021 | Presents reusable patterns for writing parsers in combinator style that keep parsing code simple, separated and maintainable. |
| **Desugaring Haskell's do-Notation into Applicative Operations** | Marlow, Peyton Jones, Kmett & Mokhov | Haskell Symposium 2016 | Shows how do-notation can be desugared into Applicative operations where possible, implemented as a GHC extension (ApplicativeDo). |
| **Effect Handlers in Scope** | Wu, Schrijvers & Hinze | Haskell Symposium 2014 | Presents two ways to capture scoping constructs in the syntax of algebraic effect handlers and shows how reordering handlers gives different semantics. |
| **Fail Faster: Staging and Fast Randomness for High-Performance PBT** | Richey, Cutler, Goldstein & Pierce |  | Measures the performance of property-based-testing generators and removes combinator abstraction overhead with a multi-stage programming technique (Allegro) plus faster sources of randomness. |
| **Fold and Unfold for Program Semantics** | Hutton | ICFP 1998 | Shows how fold can structure denotational semantics and unfold operational semantics, and how their algebraic properties support reasoning about program semantics. |
| **Freer Monads, More Extensible Effects** | Kiselyov & Ishii | Haskell Symposium 2015 | Rationally reconstructs extensible effects from free monads to freer monads without a Functor constraint, yielding a faster and more comprehensible extensible-effects library. |
| **Fun with Semirings: A functional pearl on the abuse of linear algebra** | Dolan | ICFP 2013 | Defines a Haskell typeclass for closed semirings and uses matrix and polynomial operations over them to solve problems such as transitive closure and shortest paths. |
| **Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire** | Meijer, Fokkinga & Paterson | FPCA 1991 | Develops a calculus for lazy functional programming based on recursion operators (catamorphisms, anamorphisms, hylomorphisms, paramorphisms) and their algebraic laws. |
| **Garnishing Parsec with Parsley** | Willis & Wu | Scala Symposium 2018 | Describes Parsley, a Scala parser combinator library that keeps Parsec's style while achieving competitive performance. |
| **Generalising Monads to Arrows** | Hughes | Science of Computer Programming (2000), 1998 | Introduces arrows, a generalisation of monads, as an interface for combinator libraries whose program fragments do not fit the monadic interface. |
| **Lava: Hardware Design in Haskell** | Bjesse, Claessen, Sheeran & Singh | ICFP 1998 | Presents Lava, a set of Haskell modules for specifying, simulating, verifying and generating hardware circuits, using monads, type classes and higher-order functions. |
| **Monads for functional programming** | Wadler | Advanced Functional Programming (Bastad summer school), 1995 | Describes using monads to structure functional programs, with case studies on an evaluator, in-place-update arrays and parsers. |
| **Parsley: The Fastest Parser Combinator Library in the West** | Willis | MEng dissertation, University of Bristol, 2018 | Dissertation on the design and implementation of Parsley, a high-performance parser combinator library. |
| **Scans and Convolutions: A Calculational Proof of Moessner's Theorem** | Hinze | IFL 2008 | Introduces scans and convolutions as corecursion schemes for streams and uses them to give a calculational proof of Paasche's generalisation of Moessner's theorem. |
| **Species and Functors and Types, Oh My!** | Yorgey | Haskell Symposium 2010 | Teaches the theory of combinatorial species using functional-programming examples and introduces the Haskell species library. |
| **Stackless Scala With Free Monads** | Bjarnason | Scala Days 2012 | Introduces trampolines in Scala and extends them, via free monads, to eliminate stack use for all method calls, not only tail calls. |
| **A tutorial on the universality and expressiveness of fold** | Hutton | Journal of Functional Programming 9(4), 1999 | Tutorial on the universal property of fold as a proof and definition principle, and on the unexpected expressive power of fold with tuples and first-class functions. |
| **What You Needa Know about Yoneda: Profunctor Optics and the Yoneda Lemma (Functional Pearl)** | Boisseau & Gibbons | ICFP 2018 | Derives the profunctor representation of optics (lenses, prisms) from the concrete getter/setter representation as an application of the Yoneda Lemma. |

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
| **[Beyond Notations: Hygienic Macro Expansion for Theorem Proving Languages](https://arxiv.org/abs/2001.10490)** | Ullrich & de Moura | Logical Methods in Computer Science 18(2), 2022 | Presents a hygienic macro system for interactive theorem provers (Lean 4) that supports extensible syntax and tactic languages beyond ad hoc notation mechanisms. |
| **Characterizing functions mappable over GADTs** |  |  | Develops an algorithm that, given a term of a (deep) GADT type, returns the constraints a function must satisfy to be mappable over it. |
| **Computational lambda-calculus and monads** | Moggi | LICS 1989 | Gives a calculus based on a categorical semantics of computations that provides a correct basis for proving program equivalence independent of any specific computational model. |
| **A Denotational Semantics of Inheritance and its Correctness** | Cook & Palsberg | Information and Computation 114(2), 1994 | Presents a denotational model of inheritance as deriving modified versions of recursive definitions and proves it equivalent to an operational method-lookup semantics. |
| **[Do Be Do Be Do](https://arxiv.org/abs/1611.09259)** | Lindley, McBride & McLaughlin | POPL 2017 (arXiv) | Presents Frank, a strict functional language with a bidirectional effect type system in which functions generalise to operators that handle effects (multihandlers). |
| **Elastic Sheet-Defined Functions: Generalising Spreadsheet Functions to Variable-Size Input Arrays** | McCutchen et al. |  | Describes a principled way to generalise spreadsheet sheet-defined functions written over fixed-size arrays into elastic functions that work on inputs of arbitrary size. |
| **Integrating Functional and Imperative Programming** | Gifford & Lucassen | LFP 1986 | Presents fluent languages with separate functional and imperative sublanguages, checked by a static system that infers both the type and effect class of every expression. |
| **Notions of computation and monads** | Moggi | Information and Computation 93, 1991 | Introduces calculi based on a categorical (monadic) semantics of computations that give a correct basis for proving program equivalence across many notions of computation. |
| **OrcO: A Concurrency-First Approach to Objects** | Peters, Kitchin, Thywissen & Cook | OOPSLA 2016 | Presents OrcO, an object system for the Orc concurrent language designed with concurrency first. |
| **A Programmable Programming Language** | Felleisen et al. | Communications of the ACM, 2018 | Argues that language-oriented programming needs programmable programming languages, using Racket as the example. |
| **Reconciling Semantics and Reflection: Formalisms, Protocols, Applications and Architecture** | Rideau | PhD thesis draft, Ecole Nationale Superieure des Telecommunications, 2023 | Proposes an approach to reconciling semantics and reflection in computing systems, distinguishing three dimensions of meta-computation: ante/post (staging), hypo/hyper (semantic implementation and refinement) and back/fore (runtime effect control). |
| **Theorems for free!** | Wadler | FPCA 1989 | Shows how to derive a theorem from the type of any polymorphic function, using Reynolds' abstraction theorem for the polymorphic lambda calculus. |
| **A tutorial implementation of a dependently typed lambda calculus** | Loh, McBride & Swierstra | Fundamenta Informaticae, 2010 | Presents the type rules of a dependently typed core calculus with a Haskell implementation, highlighting the changes from a simply-typed calculus and extending it with data types. |
| **The Verse Calculus: a Core Calculus for Functional Logic Programming** | Augustsson et al. | Draft | Describes the Verse calculus, a core calculus for functional logic programming, equipped with a small-step rewrite semantics. |

### Software Design and Engineering

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Rewrite it in Rust: A Computational Physics Case Study](https://arxiv.org/abs/2410.19146)** | Veytsman, Zhai, Ding & Sefkow | arXiv, 2024 | Compares C++ and Rust (serial and parallel) implementations of a physics simulation, measuring runtime and parallel code complexity. |

### Theory of Computation

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Flat Origami is Turing Complete](https://arxiv.org/abs/2309.07932)** | Hull & Zakharevich | arXiv, 2023 | Proves that flat origami, viewed as a computational device, is Turing complete. |
| **A Fresh Look at the lambda-Calculus** | Accattoli | FSCD 2019 (invited talk) | Bird's-eye view of questions about the untyped lambda-calculus: measuring the complexity of terms, decomposing and implementing evaluation, and how these vary with the evaluation strategy. |
| **[A Programming Language Oriented Approach to Computability](https://arxiv.org/abs/1402.2949)** | Karper | Bachelor thesis, University of Bern, 2013 | Develops computability theory using simple programming languages (FOR and WHILE) and transformations between them. |
| **[Simulating Time With Square-Root Space](https://arxiv.org/abs/2502.17779)** | Williams | arXiv, 2025 | Shows that every multitape Turing machine running in time t can be simulated in space O(sqrt(t log t)), improving the 50-year-old Hopcroft-Paul-Valiant bound. |
| **A Tutorial Introduction to the Lambda Calculus** | Rojas | Lecture notes, FU Berlin, 1997 | Short introduction to the lambda calculus showing arithmetic and recursive definitions without named functions. |

## AI and Machine Learning

### Applied ML

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Mathematical Entities: Corpora and Benchmarks](https://arxiv.org/abs/2406.11577)** | Collard, de Paiva & Subrahmanian | arXiv, 2024 | Provides three annotated corpora of mathematical text (182,397 sentences with POS tags, lemmas and dependency trees) and evaluates NLP models on them. |
| **[Monolith: Real Time Recommendation System With Collisionless Embedding Table](https://arxiv.org/abs/2209.07663)** | Liu et al. | arXiv, 2022 | Describes ByteDance's Monolith, a real-time recommendation training system using collisionless embedding tables, addressing limits of general-purpose deep learning frameworks. |

### Deep Learning

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Algebraic Positional Encodings](https://arxiv.org/abs/2312.16045)** | Kogkalidis, Bernardy & Garg | arXiv, 2024 | Introduces a positional encoding for Transformers that maps the algebraic specification of a domain (sequences, grids, trees) to orthogonal operators, preserving its structure. |
| **Best of Both Worlds: Advantages of Hybrid Graph Sequence Models** | Behrouz et al. | arXiv, 2024 | Presents the Graph Sequence Model framework for applying sequence models (Transformers, linear RNNs) to graphs and analyses their strengths and weaknesses, motivating hybrid models. |
| **From Online Softmax to FlashAttention** | Ye | Course note, UW CSE 599M, 2023 | Explains why tiling self-attention is non-trivial and derives the FlashAttention computation from the online softmax trick. |
| **KAN or MLP: A Fairer Comparison** | Yu, Yu & Wang | arXiv, 2024 | Compares KAN and MLP models under matched parameters and FLOPs across ML, vision, audio, NLP and symbolic-formula tasks, finding MLP generally better except for symbolic formula representation. |
| **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)** | Frankle & Carbin | ICLR 2019 | Finds that standard pruning uncovers subnetworks whose initialisations let them train effectively, and states the hypothesis that dense networks contain such 'winning ticket' subnetworks. |
| **Matryoshka Representation Learning** | Kusupati et al. | NeurIPS 2022 | Introduces Matryoshka Representation Learning, which encodes information at multiple granularities so one embedding can be truncated to fit downstream compute constraints. |

### Large Language Models

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **[Are Language Models Agnostic to Linguistically Grounded Perturbations? A Case Study of Indic Languages](https://arxiv.org/abs/2412.10805)** | Ghosh, Dabre & Bhattacharyya | arXiv, 2024 | Studies whether pretrained language models are robust to linguistically grounded input perturbations across Indic languages and downstream tasks, compared with non-linguistic attacks. |
| **[Ask, and it shall be given: Turing completeness of prompting](https://arxiv.org/abs/2411.01992)** | Qiu, Xu, Bao & Tong | arXiv, 2024 | Shows that prompting is Turing-complete: a single finite-size Transformer can compute any computable function given a suitable prompt. |
| **[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)** | DeepSeek-AI | arXiv, 2024 | Presents DeepSeek-V3, a 671B-parameter Mixture-of-Experts model (37B active per token) using Multi-head Latent Attention, auxiliary-loss-free load balancing and multi-token prediction. |
| **[DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)** | Shao et al. | arXiv, 2024 | Introduces DeepSeekMath 7B, pretrained further on 120B math-related tokens, reaching 51.7% on the MATH benchmark; also introduces the GRPO reinforcement learning algorithm. |
| **The Future of Programming in the Age of Large Language Models** | Guha & Zorn | CCC/CRA-I Whitepaper, 2025 | Whitepaper on how LLMs are changing software development and computing education, and the research questions this raises. |
| **[Knowledge Mechanisms in Large Language Models: A Survey and Perspective](https://arxiv.org/abs/2407.15017)** | Wang et al. | arXiv, 2024 | Reviews analysis of knowledge mechanisms in LLMs under a taxonomy of knowledge utilisation (memorisation, comprehension, creation) and knowledge evolution. |
| **[Language Models Use Trigonometry to Do Addition](https://arxiv.org/abs/2502.00873)** | Kantamneni & Tegmark | arXiv, 2025 | Reverse-engineers how mid-sized LLMs compute addition, finding numbers represented as a generalised helix manipulated by a 'Clock' algorithm. |
| **LeanAgent: Lifelong Learning for Formal Theorem Proving** | Kumarappan et al. | arXiv, 2024 | Presents LeanAgent, a lifelong-learning framework for LLM-based theorem proving in Lean that works across multiple evolving mathematical repositories. |
| **[More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression](https://arxiv.org/abs/2412.12706)** | Zhang et al. | arXiv, 2024 | Investigates the trade-off between number of tokens and numeric precision in LLM KV-cache compression, finding that storing more tokens at lower precision (quantized pruning) improves long-context performance. |
| **[A Primer on the Inner Workings of Transformer-based Language Models](https://arxiv.org/abs/2405.00208)** | Ferrando, Sarti, Bisazza & Costa-jussa | arXiv, 2024 | Concise technical introduction to interpretability techniques for decoder-only Transformer language models and an overview of known internal mechanisms. |
| **[Rethinking Reflection in Pre-Training](https://arxiv.org/abs/2504.04022)** | Essential AI | arXiv, 2025 | Introduces deliberate errors into chains-of-thought and shows that language models' ability to recognise and correct them emerges during pre-training and improves with pre-training compute. |
| **[Self-Organizing Graph Reasoning Evolves into a Critical State for Continuous Discovery Through Structural-Semantic Dynamics](https://arxiv.org/abs/2503.18852)** | Buehler | arXiv, 2025 | Analyses agentic graph-reasoning systems and reports that they evolve toward a critical state in which semantic entropy persistently dominates structural entropy, sustaining discovery. |
| **Self-Taught Evaluators** | Wang et al. | arXiv, 2024 | Improves LLM-as-a-Judge evaluators without human preference labels, using an iterative self-improvement scheme over synthetic contrasting model outputs. |
| **Towards a Science of AI Agent Reliability** | Rabanser et al. | arXiv, 2026 | Argues single accuracy metrics are insufficient for AI agents and proposes a holistic reliability profile (consistency across runs, robustness to perturbation, predictable failure, bounded error severity) grounded in safety-critical engineering. |
| **[Understanding LLMs: A Comprehensive Overview from Training to Inference](https://arxiv.org/abs/2401.02038)** | Liu et al. | arXiv, 2024 | Survey of techniques for training and running large language models, from data and architecture to inference. |
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
| **An Efficient Kannada Dialect Identification Systems using NLP** | Anusha & Aditya | Grenze International Journal of Engineering and Technology | Analyses datasets and features for automatically identifying Kannada dialects, which fall into coastal, northern, southwestern and southern groups. |
| **Rice in Dravidian** | Southworth | Rice 4:142-148, 2012 | Uses linguistic evidence to trace Proto-Dravidian society and its agricultural vocabulary, the movement of Dravidian speakers into South Asia, and their role in rice cultivation. |
| **Treatment of Case Markers in Sabdamanidarpanam and Tolkappiam: A Comparative Study** | Kodagunti | 2021 | Compares how the traditional grammars of Kannada (Sabdamanidarpana) and Tamil (Tolkappiyam) describe case markers, showing similar forms in the early stages of both languages. |

### Historical Linguistics and Scripts

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **The Decipherment of Linear Elamite Writing** | Desset et al. | Zeitschrift fur Assyriologie 112(1), 2022 | Presents a decipherment of Linear Elamite, used in southern Iran c. 2300-1880 BCE, starting from eight inscribed silver beakers published in 2018. |
| **Drift, Convergence, and the Ergative Cycle** | Kiparsky |  | Examines drift, convergence and cyclic change as problems for the theory of language change, using the evolution of Indo-Iranian case and agreement syntax from nominative/accusative to ergative alignment. |
| **The Kikkuli Text. Hittite Training Instructions for Chariot Horses in the Second Half of the 2nd Millennium B.C. and Their Interdisciplinary Context** | Raulwing | 2009 | Examines the Hittite Kikkuli horse-training instructions and their philological, linguistic and historical context. |
| **Probabilistic Models of Evolution and Language Change** | Bouchard-Cote | Technical Report UCB/EECS-2010-153 (PhD thesis), UC Berkeley | Develops probabilistic models of evolution applied to language change, such as reconstructing ancestral word forms. |
| **Proposal for encoding the Indus script in Plane 1 of the UCS** | Everson | ISO/IEC JTC1/SC2/WG2 N1959, 1999 | Working-group proposal to encode the Indus script (386 characters) in Plane 1 of the Universal Character Set. |
| **Proto-Elamite and Linear Elamite, a Misunderstood Relationship?** | Dahl | 2023 | Argues that Linear Elamite was a new script created in the late 3rd millennium BC, inspired by recovered proto-Elamite tablets and Old Akkadian cuneiform, rather than a continuous development of proto-Elamite. |

### Sanskrit and Indo-Aryan Linguistics

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Data-driven dependency parsing of Vedic Sanskrit** | Hellwig, Nehrdich & Sellmer | Language Resources and Evaluation 57, 2023 | Describes the first data-driven dependency parser for Vedic Sanskrit, testing input feature representations including contextual embeddings and analysing parsing errors. |
| **The Death of Sanskrit** | Pollock | Comparative Studies in Society and History, 2001 | Examines the decline of Sanskrit as a language of literary and intellectual creativity in precolonial South Asia, against nationalist myths about its history. |
| **Developments of nasals in early Indo-Aryan: anunasika and anusvara** | Cardona | Tokyo University Linguistic Papers 33, 2013 | Establishes that the anunasika/anusvara distinction drawn by Panini and the phonetic treatises reflects a real linguistic difference between nasalised vowels/nasal stops and a post-vocalic nasal segment. |
| **A Mathematical Analysis of Panini's Sivasutras** | Petersen | Journal of Logic, Language and Information 13, 2004 | Gives a set-theoretic argument that Panini's ordering of phonological segments in the Sivasutras is optimal for representing natural classes as intervals. |
| **[One Model is All You Need: ByT5-Sanskrit, a Unified Model for Sanskrit NLP Tasks](https://arxiv.org/abs/2409.13920)** | Nehrdich, Hellwig & Keutzer | arXiv, 2024 | Presents ByT5-Sanskrit, a pretrained model for Sanskrit NLP evaluated on word segmentation and Vedic dependency parsing. |
| **Panini** |  | Handbook chapter (history of phonology) | Describes Panini's grammar of Sanskrit and its goal of a consistent, exhaustive and maximally concise formal analysis, and its phonetic and phonological background. |

## Other

| Paper | Authors | Where | About |
|-------|---------|-------|-------|
| **Ancient DNA reveals pervasive directional selection across West Eurasia** | Akbari et al. | Nature, 2026 | Uses large ancient-DNA samples to distinguish sustained directional selection from shifts due to migration and population structure in West Eurasian populations. |
