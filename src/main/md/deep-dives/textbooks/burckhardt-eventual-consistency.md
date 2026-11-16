<a id="ch1"></a>
# Principles of Eventual Consistency

> Sebastian Burckhardt · Foundations and Trends in Programming Languages, 2014 · [the PDF in Drive](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

The Drive file is named “Linerarity of Consistency”; the book is Burckhardt’s monograph. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A formal framework for specifying and verifying replicated systems that stay available by letting replicas diverge temporarily. Burckhardt models what clients observe as histories, explains them with abstract executions (visibility and arbitration orders over events), and states consistency guarantees as axioms on those orders. Replicated data types such as counters, registers and sets get precise specifications, and the guarantees are arranged in a hierarchy from basic eventual consistency through causal consistency to sequential consistency and linearizability. The second half gives a pseudocode language and its operational semantics, protocol templates (epidemic, broadcast, global-sequence), a version of the CAP theorem, and correctness proofs connecting implementations to specifications.

**Contents**

1. [Introduction](ch1): Why eventual consistency, where it is used, a warm-up example, and the plan of the book.
2. [Preliminaries](ch2): Mathematical background: relations, orders and event graphs.
3. [Consistency Specifications](ch3): Histories of client operations, abstract executions that explain them, and guarantees as axioms.
4. [Replicated Data Types](ch4): Specifying data types under replication: sequential specs, replicated specs, and return-value consistency.
5. [Consistency](ch5): The spectrum of guarantees from eventual to causal to strong, and how they relate.
6. [Implementations](ch6): Pseudocode implementations of counters and key-value stores, and reusable protocol templates.
7. [Concrete Executions](ch7): Operational semantics: transitions, trajectories, observable histories, infinite runs.
8. [Protocols](ch8): Role automata, transport guarantees, and compiling pseudocode to protocols.
9. [Implementability](ch9): What can and cannot be implemented: CAP and progress guarantees.
10. [Correctness](ch10): Proof techniques showing that epidemic, broadcast and global-sequence protocols meet their specifications.
11. [Related Work](ch11): How the framework relates to work in distributed systems, databases, memory models, algorithms and verification.
12. [Conclusion](ch12): Summary and open directions.


---

## Introduction

*PDF pp. 15–30*

Why eventual consistency, where it is used, a warm-up example, and the plan of the book.

**General Motivation**  
Availability and partition tolerance motivate weaker consistency.  
*Terms:* eventual consistency, availability, partition tolerance  
→ PDF pp. 17–19 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Applications**  
Cloud storage, collaborative editing and mobile apps.  
*Terms:* cloud storage, geo-replication, collaborative editing  
→ PDF pp. 20–21 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Warmup**  
A simple replicated counter and the anomalies clients can see.  
*Terms:* replicated counter, anomalies  
→ PDF pp. 22–28 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Overview**  
The book’s structure.  
*Terms:* overview  
→ PDF pp. 29–30 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch2"></a>
## Preliminaries

*PDF pp. 31–40*

Mathematical background: relations, orders and event graphs.

**Sets and Functions**  
Relations, partial and total orders.  
*Terms:* relations, partial order, total order  
→ PDF pp. 31–35 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Event Graphs**  
Event graphs as the common structure.  
*Terms:* event graph  
→ PDF pp. 36–40 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch3"></a>
## Consistency Specifications

*PDF pp. 41–50*

Histories of client operations, abstract executions that explain them, and guarantees as axioms.

**Histories**  
What clients observe: operations and results.  
*Terms:* history  
→ PDF pp. 42–45 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Abstract Executions**  
Visibility and arbitration relations that justify a history.  
*Terms:* abstract execution, visibility, arbitration  
→ PDF p. 46 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Consistency Guarantees**  
Guarantees as conditions on abstract executions.  
*Terms:* consistency guarantee, axioms  
→ PDF p. 47 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Background**  
Origins of the approach.  
*Terms:* background  
→ PDF pp. 48–50 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch4"></a>
## Replicated Data Types

*PDF pp. 51–62*

Specifying data types under replication: sequential specs, replicated specs, and return-value consistency.

**Basic Definitions**  
Operations and return values.  
*Terms:* data type, operations  
→ PDF pp. 51–52 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Sequential Data Types**  
Specs of sequential types.  
*Terms:* sequential specification  
→ PDF pp. 53–55 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Replicated Data Types**  
Specs for replicated types such as counters, registers, sets and multi-value registers.  
*Terms:* replicated data type, CRDT, counter, register, OR-set, multi-value register  
→ PDF pp. 56–60 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Return Value Consistency**  
Return values consistent with the visible operations.  
*Terms:* return value consistency  
→ PDF pp. 61–62 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch5"></a>
## Consistency

*PDF pp. 63–74*

The spectrum of guarantees from eventual to causal to strong, and how they relate.

**Basic Eventual Consistency**  
Eventual visibility and convergence.  
*Terms:* basic eventual consistency, convergence  
→ PDF pp. 64–68 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Causal Consistency**  
Causality-respecting visibility.  
*Terms:* causal consistency  
→ PDF p. 69 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Strong Models**  
Sequential consistency and linearizability.  
*Terms:* sequential consistency, linearizability  
→ PDF pp. 70–72 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Hierarchy of Models**  
The partial order of models.  
*Terms:* consistency hierarchy  
→ PDF pp. 73–74 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch6"></a>
## Implementations

*PDF pp. 75–94*

Pseudocode implementations of counters and key-value stores, and reusable protocol templates.

**Overview**  
Implementation style.  
*Terms:* implementations  
→ PDF pp. 75–78 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Pseudocode Semantics**  
Meaning of the pseudocode.  
*Terms:* pseudocode semantics  
→ PDF p. 79 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Counters**  
Replicated counter implementations.  
*Terms:* counter implementation  
→ PDF pp. 80–82 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Stores**  
Replicated key-value stores.  
*Terms:* key-value store  
→ PDF pp. 83–85 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Protocol Templates**  
Epidemic, broadcast and global-sequence templates.  
*Terms:* protocol templates  
→ PDF pp. 86–94 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch7"></a>
## Concrete Executions

*PDF pp. 95–106*

Operational semantics: transitions, trajectories, observable histories, infinite runs.

**Transitions**  
Transition systems.  
*Terms:* transition system  
→ PDF pp. 95–96 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Trajectories**  
Runs as trajectories.  
*Terms:* trajectory  
→ PDF pp. 97–98 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Concrete Executions**  
Concrete executions with messages.  
*Terms:* concrete execution  
→ PDF pp. 99–100 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Observable History**  
Deriving the observable history.  
*Terms:* observable history  
→ PDF pp. 101–104 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Infinite Executions**  
Liveness over infinite runs.  
*Terms:* liveness, infinite executions  
→ PDF pp. 105–106 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch8"></a>
## Protocols

*PDF pp. 107–114*

Role automata, transport guarantees, and compiling pseudocode to protocols.

**Role Automata**  
Replicas and clients as role automata.  
*Terms:* role automata  
→ PDF pp. 107–108 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Transport Guarantees**  
Message delivery assumptions.  
*Terms:* transport guarantees, reliable delivery  
→ PDF pp. 109–110 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Protocols**  
Protocol definitions.  
*Terms:* protocols  
→ PDF pp. 111–112 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Pseudocode Compilation**  
Translating pseudocode into protocols.  
*Terms:* pseudocode compilation  
→ PDF pp. 113–114 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch9"></a>
## Implementability

*PDF pp. 115–124*

What can and cannot be implemented: CAP and progress guarantees.

**CAP**  
A formal CAP theorem: availability under partitions rules out strong consistency.  
*Terms:* CAP theorem  
→ PDF pp. 116–119 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Progress**  
Progress and liveness guarantees.  
*Terms:* progress, wait-freedom  
→ PDF pp. 120–124 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch10"></a>
## Correctness

*PDF pp. 125–144*

Proof techniques showing that epidemic, broadcast and global-sequence protocols meet their specifications.

**Proof Structure**  
How the correctness proofs are organized.  
*Terms:* proof structure, simulation  
→ PDF pp. 125–126 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Epidemic Protocols**  
Epidemic (gossip) protocols.  
*Terms:* epidemic protocols, gossip  
→ PDF pp. 127–133 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Broadcast Protocols**  
Reliable-broadcast protocols.  
*Terms:* broadcast protocols  
→ PDF pp. 134–135 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Global-Sequence Protocols**  
Protocols that agree on a global sequence.  
*Terms:* global-sequence protocols, consensus  
→ PDF pp. 136–144 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch11"></a>
## Related Work

*PDF pp. 145–152*

How the framework relates to work in distributed systems, databases, memory models, algorithms and verification.

**Distributed Systems**  
Distributed systems.  
*Terms:* distributed systems  
→ PDF p. 145 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Databases**  
Database isolation.  
*Terms:* databases, isolation levels  
→ PDF pp. 146–147 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Shared-Memory Multiprocessors**  
Weak memory models.  
*Terms:* memory models  
→ PDF p. 148 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Distributed Algorithms**  
Distributed algorithms.  
*Terms:* distributed algorithms  
→ PDF p. 149 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

**Verification**  
Verification work.  
*Terms:* verification  
→ PDF pp. 150–152 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)


---

<a id="ch12"></a>
## Conclusion

*PDF pp. 153–154*

Summary and open directions.

*Terms:* conclusion

→ PDF pp. 153–154 in [the PDF](https://drive.google.com/file/d/1KUEAbAgneC5hMhY6mSIHjXVpOxbV2q4N/view)

