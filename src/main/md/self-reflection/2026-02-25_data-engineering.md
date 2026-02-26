---
title: Data Engineering
created: 2026-02-25
source: ../self.md
---

# Data Engineering

> Derived from [`self.md`](../self.md) · Created: 2026-02-25

Links, notes, and resources on data pipelines, system design, databases, and data infrastructure.

---

## System Design

GitHub - Coder-World04/Complete-System-Design
https://github.com/Coder-World04/Complete-System-Design

GitHub - Coder-World04/Tech-Interview-Important-Topics-and-Techniques
https://github.com/Coder-World04/Tech-Interview-Important-Topics-and-Techniques

Neo Kim (@systemdesign42): I spent 5+ hours studying how Instagram scaled to 2.5 billion users.
https://x.com/systemdesign42/status/1800491019663970354

1: TinyURL + PasteBin — Systems Design Interview Questions With Ex-Google SWE
38 minutes
https://youtu.be/5V6Lam8GZo4

Mike (@cambridgemike): Rearchitecting core services at X
https://x.com/cambridgemike/status/1835774409786986572

## APIs & GraphQL

Why, after 6 years, I'm over GraphQL (bessey.dev)
https://bessey.dev/

Conexus data interoperability

## Scheduling

Artificial Intelligence to Solve Production Scheduling Problems in Real Industrial Settings
Systematic Literature Review — particle swarm optimization, neural networks, reinforcement learning are the most widely used techniques.
AI solutions have reduced production costs, increased energy efficiency, improved scheduling.
www.mdpi.com
https://www.mdpi.com/2079-9292/12/23/4732

Graph neural networks for exact solving scheduling problems (local PDF reference)
file:///Users/vishwas/Downloads/2022Exactsolvingschedulingproblemsacceleratedbygraphneuralnetworks_RG.pdf

## Spark / Big Data

Apache Spark (general reference)
incubator-nlpcraft project (Apache NLPCraft NLP framework)

## Kannada Data Pipeline (alar.ink)

Nushell command: parse alar.txt linkchecker output to JSON:
```nushell
open alar.txt | parse -r '(((URL *\x60(?P<Url>[^\x27]*)\x27)\n)|((Name *\x60(?P<Name>.*)\x27)\n)|(Parent URL *(?P<Purl>(?P<phttp>[^,]*), line (?P<pline>[^,]*), col (?P<pcol>[^\n]*))\n)|((Real URL *(?P<Rurl>.*))\n)){4}' | select Url Name Rurl phttp pline pcol| to json | save -f "alar-url.txt"
```

Nushell Kannada character class variables (for alar.ink 5-syllable word extraction):
```nushell
$env.vowelfull = $env.vowel + $env.vowelend
$env.consnooth = $env.cons + $env.consend
$env.consotth1 = $env.cons + $env.hal + $env.cons + $env.consend
$env.consotth2 = $env.cons + $env.hal + $env.cons + $env.hal + $env.cons + $env.consend
$env.block = $"\(\(($env.vowelfull)\)|\(($env.consnooth)\)|\(($env.consotth1)\)|\(($env.consotth2)\)\)"
egrep $"\^($env.block){5}[್]?\$" alar-212-sorted-uniq-2.txt | save -f alar-5.txt
# Result: 21416 words of 5+ syllables
```

## Benchmarking

IndicGenBench — multilingual benchmark, 29 Indic languages
arxiv 2404.16816
https://arxiv.org/abs/2404.16816

GitHub: google-research-datasets/indic-gen-bench
https://github.com/google-research-datasets/indic-gen-bench

## Educational

Spintronics — Build Mechanical Circuits (upperstory.com)
https://upperstory.com/

DEXA scan info (dexafit.com pre-test protocols)

---

## From self-1.md (Oct 2024 – Feb 2026)

### System Design & Distributed Systems

**Santiago @svpino: RAG data pipelines**
Traditional data pipelines don't work for RAG applications — x.com — https://x.com/svpino/status/1846163161587585248

**Raul Junco: System Design 80% of interviews**
Scalable data storage, SQL vs NoSQL, partitioning — x.com — https://x.com/RaulJuncoV/status/1861038062987297267

**Raul Junco: 17 real-world System Design questions**
x.com — https://x.com/RaulJuncoV/status/1863574782085607823

**The Design Patterns for Distributed Systems Handbook**
freecodecamp.org — https://www.freecodecamp.org/news/design-patterns-for-distributed-systems/

**Sahn Lam: Netflix Tech Stack**
x.com — https://x.com/sahnlam/status/1880124144957944205

**Alex Xu: System Design Blueprint**
x.com — https://x.com/alexxubyte/status/1879932894963225022

**How Meta discovers data flows via lineage at scale**
engineering.fb.com — https://engineering.fb.com/2025/01/22/security/how-meta-discovers-data-flows-via-lineage-at-scale/

**Exploring the Potential of Stonebraker's New DBOS**
golem.cloud — https://www.golem.cloud/post/exploring-the-potential-of-stonebreaker-s-new-dbos

**How Three Guys Rebuilt the Foundation of Facebook (HHVM)**
wired.com — https://www.wired.com/2013/06/facebook-hhvm-saga/

### Databases & Storage

**SplinterDB: A Key-Value Store for Modern Storage Devices**
youtube — https://youtu.be/1gOlXfbiT_Y

**Composable SQL**
borretti.me — https://borretti.me/article/composable-sql

**Lightning Memory-Mapped Database**
Wikipedia — https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database

**Conflict-free Database over Virtual File System (CRDTs)**
bartoszsypytkowski.com — https://www.bartoszsypytkowski.com/conflict-free-database-over-virtual-file-system/

**A Distributed System from scratch, with Scala 3 - Part 3: Job submission, worker scaling, and leader election with Raft**
chollinger.com — https://chollinger.com/blog/2025/05/a-distributed-system-from-scratch-with-scala-3-part-3-job-submission-worker-scaling-and-leader-election-consensus-with-raft/

### Spark / Data Pipelines

**Scaladex: spark-wiki-parser**
index.scala-lang.org — https://index.scala-lang.org/nielsenbe/spark-wiki-parser

**Spark's groupByKey should be avoided**
gresearch.com — https://www.gresearch.com/news/sparks-groupbykey-should-be-avoided-and-heres-why/

### Kafka & Streaming

**Lenses.io (Kafka + Kubernetes)**
github.com — https://github.com/lensesio

### AI / Data Tooling

**Gen AI Toolbox for Databases**
googleapis.github.io — https://googleapis.github.io/genai-toolbox/getting-started/introduction/

**Tech with Mak: RAG architecture selection guide**
Standard RAG, Agentic RAG, Graph RAG, Modular RAG — x.com — https://x.com/techNmak/status/2023978105606676821

**Agentic Reasoning for Large Language Models**
Survey paper — arxiv.org — https://arxiv.org/abs/2601.12538

**Intelligent AI Delegation**
Adaptive framework for task allocation across AI agents and humans — arxiv.org — https://arxiv.org/abs/2602.11865

### Algorithms & CS Theory

**For Algorithms, a Little Memory Outweighs a Lot of Time**
First progress in 50 years on a famous CS question — quantamagazine.org — https://www.quantamagazine.org/for-algorithms-a-little-memory-outweighs-a-lot-of-time-20250521/

**For Algorithms, Memory Is a Far More Powerful Resource Than Time**
wired.com — https://www.wired.com/story/for-algorithms-a-little-memory-outweighs-a-lot-of-time/

**List Unfolding — unfold as the computational dual of fold**
fpilluminated.org — https://fpilluminated.org/deck/263

**IRS Direct File: fact-graph-scala (Scala 3 functional graph)**
github.com — https://github.com/IRS-Public/direct-file/tree/main/direct-file/fact-graph-scala

**Building Industrial Strength Software without Unit Tests**
chrispenner.ca — https://chrispenner.ca/posts/transcript-tests

**Which programming languages are most token-efficient?**
Comparing 19 languages via RosettaCode — martinalderson.com — https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/

**GitHub - Developer-Y/cs-video-courses**
List of Computer Science courses with video lectures — github.com — https://github.com/Developer-Y/cs-video-courses

### FP & Programming Languages

**Adam Hearn - Redefining Stream Composition with Algebraic Effects**
LambdaConf 2025 — youtu.be — https://youtu.be/WcYKTyQwEA0?si=3PQCFCXqz7PuXSql

**Francois Rene Rideau - Auto Merkleization: Where FP meets Algebra, Metaprogramming and OO**
LambdaConf 2025 — youtu.be — https://youtu.be/JFsmOzGNW3o?si=dnSl_aIbvOZg8IAz

**Unison Share**
Explore, read docs, and share Unison libraries — share.unison-lang.org — https://share.unison-lang.org/

**LLM-Generated Lean4 Proofs**
Research paper — github.com — https://github.com/lampless/LLM-Generated-Lean4-Proofs/blob/main/Dylan%20Miller_%20LLM-Generated%20Lean4%20Proofs.pdf

**GPT-5.2 derives a new result in theoretical physics**
New formula for gluon amplitude — openai.com — https://openai.com/index/new-result-theoretical-physics/
