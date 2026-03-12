---
title: Data Engineering
created: 2026-02-25
source: personal notes (self.md, self-1.md)
---

# Data Engineering

> Derived from personal notes · Created: 2026-02-25

Links, notes, and resources on data pipelines, system design, databases, and data infrastructure.

---

## System Design

**GitHub - Coder-World04/Complete-System-Design**
https://github.com/Coder-World04/Complete-System-Design

A comprehensive GitHub repository covering system design concepts end-to-end: distributed systems fundamentals, CAP theorem, database selection, caching strategies, load balancing, message queues, and interview-ready design walkthroughs for common systems like URL shorteners and social feeds. **[→ data-engineering; algorithms-data-structures]**

**GitHub - Coder-World04/Tech-Interview-Important-Topics-and-Techniques**
https://github.com/Coder-World04/Tech-Interview-Important-Topics-and-Techniques

A companion repository covering both algorithmic and system design interview topics — data structures, complexity, and distributed system patterns — useful for candidates preparing for L5/L6-level interviews. **[→ algorithms-data-structures; data-engineering]**

**Neo Kim (@systemdesign42): I spent 5+ hours studying how Instagram scaled to 2.5 billion users.**
https://x.com/systemdesign42/status/1800491019663970354

A detailed tweet thread by system design educator Neo Kim dissecting Instagram's scaling story: horizontal sharding, cassandra for metadata, S3 for media, CDN strategy, and how they maintained reliability across 2.5 billion monthly users. A dense, high-signal system design reference. **[→ data-engineering]**

**1: TinyURL + PasteBin — Systems Design Interview Questions With Ex-Google SWE**
38 minutes
https://youtu.be/5V6Lam8GZo4

A 38-minute YouTube video by a former Google SWE walking through URL shortener and paste-bin design interviews: database choice, base62 encoding, caching, and scalability at load. Good entry-level system design walkthrough with clear trade-off reasoning. **[→ data-engineering; algorithms-data-structures]**

**Mike (@cambridgemike): Rearchitecting core services at X**
https://x.com/cambridgemike/status/1835774409786986572

Thread by Mike (@cambridgemike) on the technical rearchitecture of X (formerly Twitter) post-acquisition: decomposing the monolith, cutting infrastructure costs dramatically, and restructuring services. Provides an insider perspective on large-scale legacy system migration. **[→ data-engineering; infrastructure-devops]**

## APIs & GraphQL

**Why, after 6 years, I'm over GraphQL (bessey.dev)**
https://bessey.dev/

A candid retrospective by Phil Bessey after six years building with GraphQL in production. Concludes that GraphQL's complexity, N+1 problems, caching difficulties, and security surface area outweigh its benefits for most applications compared to well-designed REST APIs. **[→ data-engineering]**

**Conexus data interoperability**

A note on Conexus — a data interoperability framework or standard for connecting heterogeneous data sources. Likely referenced in the context of building data pipelines that bridge different schema formats or protocols. **[→ data-engineering]**

## Scheduling

**Artificial Intelligence to Solve Production Scheduling Problems in Real Industrial Settings**
Systematic Literature Review — particle swarm optimization, neural networks, reinforcement learning are the most widely used techniques.
AI solutions have reduced production costs, increased energy efficiency, improved scheduling.
www.mdpi.com
https://www.mdpi.com/2079-9292/12/23/4732

A systematic literature review in MDPI Electronics surveying AI approaches to production scheduling in industry. Finds that particle swarm optimisation, neural networks, and reinforcement learning dominate the literature, with documented results showing cost reduction, energy savings, and throughput improvements in real factory settings. **[→ data-engineering; machine-learning-ai; algorithms-data-structures]**

**Graph neural networks for exact solving scheduling problems (local PDF reference)**
file:///Users/vishwas/Downloads/2022Exactsolvingschedulingproblemsacceleratedbygraphneuralnetworks_RG.pdf

A 2022 research paper on using GNNs to accelerate exact branch-and-bound solvers for scheduling problems. The GNN learns branching heuristics from problem structure, dramatically reducing the search space while preserving optimality guarantees — a hybrid of ML and classical OR. **[→ algorithms-data-structures; machine-learning-ai]**

## Spark / Big Data

**Apache Spark (general reference)**
incubator-nlpcraft project (Apache NLPCraft NLP framework)

Apache Spark is the dominant distributed data processing framework for large-scale ETL, ML pipelines, and analytics. Referenced here in the context of the NLPCraft project — which uses Spark for distributed NLP workload processing across the incubator-nlpcraft codebase. **[→ data-engineering; machine-learning-ai]**

## Kannada Data Pipeline (alar.ink)

**Nushell command: parse alar.txt linkchecker output to JSON:**
```nushell
open alar.txt | parse -r '(((URL *\x60(?P<Url>[^\x27]*)\x27)\n)|((Name *\x60(?P<Name>.*)\x27)\n)|(Parent URL *(?P<Purl>(?P<phttp>[^,]*), line (?P<pline>[^,]*), col (?P<pcol>[^\n]*))\n)|((Real URL *(?P<Rurl>.*))\n)){4}' | select Url Name Rurl phttp pline pcol| to json | save -f "alar-url.txt"
```

A Nushell pipeline for parsing the text output of a link checker run against the alar.ink Kannada dictionary. Extracts URL, name, real URL, and parent URL fields using a complex regex into structured JSON. An example of Nushell's data-oriented shell scripting for text processing tasks. **[→ data-engineering; kannada-language-linguistics; scala-functional-programming]**

**Nushell Kannada character class variables (for alar.ink 5-syllable word extraction):**
```nushell
$env.vowelfull = $env.vowel + $env.vowelend
$env.consnooth = $env.cons + $env.consend
$env.consotth1 = $env.cons + $env.hal + $env.cons + $env.consend
$env.consotth2 = $env.cons + $env.hal + $env.cons + $env.hal + $env.cons + $env.consend
$env.block = $"\(\(($env.vowelfull)\)|\(($env.consnooth)\)|\(($env.consotth1)\)|\(($env.consotth2)\)\)"
egrep $"\^($env.block){5}[್]?\$" alar-212-sorted-uniq-2.txt | save -f alar-5.txt
# Result: 21416 words of 5+ syllables
```

Nushell environment variables encoding Kannada phonological character classes (vowels, consonant clusters, halant sequences) as regex components. The pipeline extracts words of exactly 5+ syllables from the alar.ink dictionary, yielding 21,416 results — used for the Wordalla Kannada word game project. **[→ data-engineering; kannada-language-linguistics]**

## Benchmarking

**IndicGenBench — multilingual benchmark, 29 Indic languages**
arxiv 2404.16816
https://arxiv.org/abs/2404.16816

IndicGenBench is a comprehensive benchmark for evaluating LLM performance on generation tasks across 29 Indian languages, covering translation, summarisation, and question answering. An important resource for assessing Indic NLP progress and identifying gaps in coverage. **[→ machine-learning-ai; kannada-language-linguistics]**

**GitHub: google-research-datasets/indic-gen-bench**
https://github.com/google-research-datasets/indic-gen-bench

The Google Research Datasets repository for IndicGenBench — containing the benchmark data, evaluation scripts, and model outputs for the 29-language Indic generation benchmark. **[→ machine-learning-ai; kannada-language-linguistics]**

## Educational

**Spintronics — Build Mechanical Circuits (upperstory.com)**
https://upperstory.com/

Spintronics is a physical game/kit that lets you build working mechanical analogues of electronic circuits — gears and axles stand in for electrons and wires. A tactile way to learn circuit fundamentals and the relationship between mechanical and electrical systems. **[→ algorithms-data-structures; mathematics-science]**

**DEXA scan info (dexafit.com pre-test protocols)**

Notes on DEXA (Dual-Energy X-ray Absorptiometry) scan protocols from DexaFit, a commercial DEXA scanning service. DEXA is the gold standard for body composition measurement, providing visceral fat, lean mass, and bone density data. **[→ health-fitness]**

---

## From self-1.md (Oct 2024 – Feb 2026)

### System Design & Distributed Systems

**Santiago @svpino: RAG data pipelines**
Traditional data pipelines don't work for RAG applications — x.com — https://x.com/svpino/status/1846163161587585248

Santiago Valdarrama explains why traditional batch ETL pipelines are poorly suited for RAG (Retrieval-Augmented Generation) applications: RAG requires chunking strategies, embedding freshness, metadata-aware retrieval, and real-time indexing that batch pipelines cannot easily support. **[→ data-engineering; machine-learning-ai]**

**Raul Junco: System Design 80% of interviews**
Scalable data storage, SQL vs NoSQL, partitioning — x.com — https://x.com/RaulJuncoV/status/1861038062987297267

Raul Junco's tweet identifying the core 20% of system design knowledge that appears in 80% of interviews: scalable storage selection, SQL vs NoSQL trade-offs, horizontal vs vertical partitioning, and caching layers — a useful minimum viable study list. **[→ data-engineering]**

**Raul Junco: 17 real-world System Design questions**
x.com — https://x.com/RaulJuncoV/status/1863574782085607823

A follow-up thread listing 17 real-world system design questions drawn from actual interviews at major tech companies, with hints on the key trade-offs each question is designed to probe. **[→ data-engineering]**

**The Design Patterns for Distributed Systems Handbook**
freecodecamp.org — https://www.freecodecamp.org/news/design-patterns-for-distributed-systems/

A freeCodeCamp handbook covering canonical distributed systems patterns: saga, CQRS, event sourcing, circuit breaker, outbox, and leader election — with explanations of when to apply each and what problems they solve. **[→ data-engineering; infrastructure-devops]**

**Sahn Lam: Netflix Tech Stack**
x.com — https://x.com/sahnlam/status/1880124144957944205

A tweet thread by Sahn Lam visualising the Netflix technology stack across streaming, recommendation, chaos engineering, and data infrastructure — a useful snapshot of how a major streaming platform is architected at scale. **[→ data-engineering; infrastructure-devops]**

**Alex Xu: System Design Blueprint**
x.com — https://x.com/alexxubyte/status/1879932894963225022

Alex Xu's system design blueprint diagram — a comprehensive visual showing the standard components (load balancer, API gateway, CDN, cache, message queue, database) and how they interconnect in a typical scalable web application. **[→ data-engineering]**

**How Meta discovers data flows via lineage at scale**
engineering.fb.com — https://engineering.fb.com/2025/01/22/security/how-meta-discovers-data-flows-via-lineage-at-scale/

Meta Engineering blog post on their data lineage system — automatically tracing how data flows through Meta's vast data infrastructure, from ingestion through transformation to serving. Critical for data governance, privacy compliance, and debugging data quality issues. **[→ data-engineering; infrastructure-devops]**

**Exploring the Potential of Stonebraker's New DBOS**
golem.cloud — https://www.golem.cloud/post/exploring-the-potential-of-stonebreaker-s-new-dbos

An analysis of DBOS (DataBase Operating System) — Michael Stonebraker's vision for a new OS architecture built on top of a distributed transactional database rather than traditional file systems. The post explores how this flips the storage abstraction hierarchy and its implications for reliability and recovery. **[→ data-engineering; infrastructure-devops]**

**How Three Guys Rebuilt the Foundation of Facebook (HHVM)**
wired.com — https://www.wired.com/2013/06/facebook-hhvm-saga/

Wired's account of how three engineers built HHVM (HipHop Virtual Machine) — a JIT compiler for PHP that gave Facebook 2x server efficiency. A story of pragmatic engineering under extreme scale constraints and the value of language-level performance investment. **[→ data-engineering; infrastructure-devops]**

### Databases & Storage

**SplinterDB: A Key-Value Store for Modern Storage Devices**
https://youtu.be/1gOlXfbiT_Y

A talk on SplinterDB, VMware Research's high-performance key-value store designed for modern NVMe SSDs. Achieves high throughput using a novel B-tree variant (Splinter Tree) that reduces write amplification — relevant to storage-intensive data engineering workloads. **[→ data-engineering; algorithms-data-structures]**

**Composable SQL**
borretti.me — https://borretti.me/article/composable-sql

An article by Fernando Borretti arguing for and demonstrating composable SQL patterns — using CTEs, views, and function abstractions to build SQL that can be composed and reused like functions in a programming language, reducing duplication in large data pipelines. **[→ data-engineering; scala-functional-programming]**

**Lightning Memory-Mapped Database**
Wikipedia — https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database

Wikipedia article on LMDB (Lightning Memory-Mapped Database) — an extremely fast embedded key-value store using memory-mapped I/O and a copy-on-write B+ tree. Notable for zero-copy reads, ACID transactions without a write-ahead log, and its use in LDAP and OpenLDAP. **[→ data-engineering; algorithms-data-structures]**

**Conflict-free Database over Virtual File System (CRDTs)**
bartoszsypytkowski.com — https://www.bartoszsypytkowski.com/conflict-free-database-over-virtual-file-system/

Bartosz Sypytkowski's exploration of building a conflict-free replicated database over a virtual file system using CRDTs (Conflict-free Replicated Data Types). Relevant to local-first software, offline-capable apps, and distributed database design without central coordination. **[→ data-engineering; scala-functional-programming]**

**A Distributed System from scratch, with Scala 3 - Part 3: Job submission, worker scaling, and leader election with Raft**
chollinger.com — https://chollinger.com/blog/2025/05/a-distributed-system-from-scratch-with-scala-3-part-3-job-submission-worker-scaling-and-leader-election-consensus-with-raft/

Part 3 of Christian Hollinger's series on building a distributed system from scratch in Scala 3: implementing job submission, dynamic worker scaling, and leader election using the Raft consensus protocol. Practical Scala 3 distributed systems engineering. **[→ data-engineering; scala-functional-programming]**

### Spark / Data Pipelines

**Scaladex: spark-wiki-parser**
index.scala-lang.org — https://index.scala-lang.org/nielsenbe/spark-wiki-parser

A Scala library on Scaladex for parsing Wikipedia XML dumps using Apache Spark — extracting wikitext, categories, and links at scale. Useful for building NLP datasets from Wikipedia corpora. **[→ data-engineering; machine-learning-ai]**

**Spark's groupByKey should be avoided**
gresearch.com — https://www.gresearch.com/news/sparks-groupbykey-should-be-avoided-and-heres-why/

A G-Research blog post explaining why `groupByKey` in Spark is a performance anti-pattern: it shuffles all data to reducers before aggregation, causing memory pressure and excessive network I/O. `reduceByKey` or `aggregateByKey` should be preferred as they combine locally before shuffling. **[→ data-engineering]**

### Kafka & Streaming

**Lenses.io (Kafka + Kubernetes)**
github.com — https://github.com/lensesio

Lenses.io provides a data streaming platform built on Kafka with a developer-friendly UI, SQL interface (LSQL), and Kubernetes-native deployment. Useful for managing Kafka topics, monitoring data flows, and building streaming data pipelines at scale. **[→ data-engineering; infrastructure-devops]**

### AI / Data Tooling

**Gen AI Toolbox for Databases**
googleapis.github.io — https://googleapis.github.io/genai-toolbox/getting-started/introduction/

Google's Gen AI Toolbox for Databases provides tools for connecting LLMs to database systems — enabling natural language queries, schema exploration, and AI-assisted data analysis using Google's AI stack and database products. **[→ data-engineering; machine-learning-ai]**

**Tech with Mak: RAG architecture selection guide**
Standard RAG, Agentic RAG, Graph RAG, Modular RAG — x.com — https://x.com/techNmak/status/2023978105606676821

A guide to selecting the right RAG architecture for different use cases: standard RAG for simple Q&A, agentic RAG for multi-step reasoning, graph RAG for entity-relationship-heavy knowledge bases, and modular RAG for customisable pipelines. Practical decision framework. **[→ machine-learning-ai; data-engineering]**

**Agentic Reasoning for Large Language Models**
Survey paper — arxiv.org — https://arxiv.org/abs/2601.12538

A comprehensive arxiv survey organising the landscape of agentic reasoning for LLMs into foundational techniques, self-evolving systems (reflection, self-critique), and multi-agent architectures. Provides a taxonomy useful for designing production agentic data pipelines. **[→ machine-learning-ai; data-engineering]**

**Intelligent AI Delegation**
Adaptive framework for task allocation across AI agents and humans — arxiv.org — https://arxiv.org/abs/2602.11865

An arxiv paper proposing an adaptive delegation framework for distributing tasks across AI agents and human workers based on competence, cost, and latency — formalising the orchestration problem in human-AI teaming pipelines. **[→ machine-learning-ai; data-engineering]**

### Algorithms & CS Theory

**For Algorithms, a Little Memory Outweighs a Lot of Time**
First progress in 50 years on a famous CS question — quantamagazine.org — https://www.quantamagazine.org/for-algorithms-a-little-memory-outweighs-a-lot-of-time-20250521/

Quanta reports on a major result: a new algorithm showing that a small amount of memory can compensate for exponentially more computation time in certain problems. The first significant progress in 50 years on Savitch's theorem and the TIME vs SPACE question in complexity theory. **[→ algorithms-data-structures; mathematics-science]**

**For Algorithms, Memory Is a Far More Powerful Resource Than Time**
wired.com — https://www.wired.com/story/for-algorithms-a-little-memory-outweighs-a-lot-of-time/

Wired's lay-accessible version of the same complexity theory breakthrough, explaining why memory is a more powerful resource than time in computation and what this means for the P vs NP landscape. **[→ algorithms-data-structures; mathematics-science]**

**List Unfolding — unfold as the computational dual of fold**
fpilluminated.org — https://fpilluminated.org/deck/263

A short article on `unfold` as the categorical dual of `fold`: while fold consumes a structure and produces a value, unfold takes a seed and produces a structure. Fundamental to understanding anamorphisms and corecursion in functional programming. **[→ scala-functional-programming; algorithms-data-structures]**

**IRS Direct File: fact-graph-scala (Scala 3 functional graph)**
github.com — https://github.com/IRS-Public/direct-file/tree/main/direct-file/fact-graph-scala

The IRS's open-source Direct File project includes a Scala 3 implementation of a functional fact graph — a declarative dependency graph for computing tax facts from input data. An unusually public example of production functional programming in a government context. **[→ scala-functional-programming; data-engineering]**

**Building Industrial Strength Software without Unit Tests**
chrispenner.ca — https://chrispenner.ca/posts/transcript-tests

Chris Penner's argument for transcript (golden) testing over unit testing for complex pipelines: record inputs and expected outputs end-to-end, then compare. Particularly relevant for data pipelines and compilers where the correct output is the primary specification. **[→ data-engineering; scala-functional-programming]**

**Which programming languages are most token-efficient?**
Comparing 19 languages via RosettaCode — martinalderson.com — https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/

An analysis comparing token counts for equivalent programs in 19 languages using RosettaCode examples. Relevant to LLM coding efficiency (fewer tokens = lower cost) and language design trade-offs. Clojure and Haskell perform well; C and Java poorly. **[→ machine-learning-ai; scala-functional-programming]**

**GitHub - Developer-Y/cs-video-courses**
List of Computer Science courses with video lectures — github.com — https://github.com/Developer-Y/cs-video-courses

A community-maintained list of computer science courses with freely available video lectures, spanning algorithms, systems, ML, programming languages, and databases. A comprehensive one-stop resource for self-taught CS education. **[→ algorithms-data-structures; machine-learning-ai]**

### FP & Programming Languages

**Adam Hearn - Redefining Stream Composition with Algebraic Effects**
LambdaConf 2025
https://youtu.be/WcYKTyQwEA0?si=3PQCFCXqz7PuXSql

A LambdaConf 2025 talk by Adam Hearn on using algebraic effects to redefine stream composition — replacing the monadic stack (IO, StateT, etc.) with a flat effect layer that allows streams to be composed without transformer stacking. Relevant to Kyo and Ox-style direct-style Scala. **[→ scala-functional-programming; data-engineering]**

**Francois Rene Rideau - Auto Merkleization: Where FP meets Algebra, Metaprogramming and OO**
LambdaConf 2025
https://youtu.be/JFsmOzGNW3o?si=dnSl_aIbvOZg8IAz

A LambdaConf 2025 talk on automatic Merkleization — deriving content-addressed, tamper-evident data structures from algebraic type definitions using metaprogramming. Bridges functional programming, cryptographic data structures, and OO design patterns. **[→ scala-functional-programming; data-engineering]**

**Unison Share**
Explore, read docs, and share Unison libraries — share.unison-lang.org — https://share.unison-lang.org/

The Unison Share platform for exploring and sharing Unison libraries — analogous to Hackage for Haskell or npm for JavaScript. Unison's content-addressed code model means dependencies are immutable by definition, enabling reliable sharing. **[→ scala-functional-programming]**

**LLM-Generated Lean4 Proofs**
Research paper — github.com — https://github.com/lampless/LLM-Generated-Lean4-Proofs/blob/main/Dylan%20Miller_%20LLM-Generated%20Lean4%20Proofs.pdf

Dylan Miller's research comparing how well GPT-5, Gemini, and other frontier LLMs can generate formally verified Lean 4 proofs. Finds that larger models succeed on simpler lemmas but struggle with deeper mathematical reasoning — relevant to AI for mathematics research. **[→ machine-learning-ai; mathematics-science]**

**GPT-5.2 derives a new result in theoretical physics**
New formula for gluon amplitude — openai.com — https://openai.com/index/new-result-theoretical-physics/

OpenAI's preprint reporting that GPT-5.2 proposed a new formula for gluon scattering amplitudes in quantum field theory that was subsequently formally verified by physicists — the first time an LLM has independently derived a new publishable result in theoretical physics. **[→ machine-learning-ai; mathematics-science]**
