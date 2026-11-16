<a id="ch1"></a>
# Distributed Computing Through Combinatorial Topology

> Maurice Herlihy, Dmitry Kozlov and Sergio Rajsbaum · Morgan Kaufmann, 2013 · [the PDF in Drive](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

Chapter notes, problems and bibliography are not broken out; many chapters have no section entries in the PDF outline, so they appear as single leaves. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A textbook showing that what fault-tolerant distributed systems can compute is a question about topology. Processes’ possible views form simplicial complexes, protocols are maps between complexes, and a task is solvable exactly when a suitable simplicial map exists. Starting from two-process systems, the book develops the combinatorial topology it needs (complexes, subdivisions, connectivity), characterizes colorless tasks in wait-free, t-resilient, message-passing and Byzantine models, and introduces simulations such as BG. The second half treats general (colored) tasks: manifold protocols, connectivity arguments for consensus and k-set agreement impossibility, the asynchronous computability theorem, renaming and orientation, reductions between shared-memory models, loop agreement classified by the fundamental group, and the immediate snapshot subdivision.

**Contents**

1. [1 Introduction](ch1): Why concurrency matters and two classic problems that frame the book.
2. [2 Two-Process Systems](ch2): Two processes as a warm-up: tasks and protocols as graphs, and why consensus is impossible.
3. [3 Elements of Combinatorial Topology](ch3): The topology the book uses: simplicial complexes, maps, subdivisions and connectivity.
4. [4 Colorless Wait-Free Computation](ch4): Colorless tasks in the wait-free read-write model and their exact solvability condition.
5. [5 Solvability of Colorless Tasks in Different Models](ch5): How solvability of colorless tasks changes with resilience, objects and message passing.
6. [6 Byzantine-Resilient Colorless Computation](ch6): Colorless computation when some processes are Byzantine.
7. [7 Simulations and Reductions](ch7): Simulating one model in another to transfer results.
8. [8 Read-Write Protocols for General Tasks](ch8): General (colored) tasks and read-write protocols for them.
9. [9 Manifold Protocols](ch9): Protocols whose complexes are pseudomanifolds, and impossibility via Sperner-type arguments.
10. [10 Connectivity](ch10): Connectivity of protocol complexes as the source of impossibility results.
11. [11 Wait-Free Computability for General Tasks](ch11): The asynchronous computability theorem characterizing wait-free solvable tasks.
12. [12 Renaming and Oriented Manifolds](ch12): Renaming and weak symmetry breaking via orientations of manifolds.
13. [13 Task Solvability in Different Models](ch13): Colored task solvability in models beyond wait-free read-write.
14. [14 Simulations and Reductions for Colored Tasks](ch14): Reductions between shared-memory models for colored tasks.
15. [15 Classifying Loop Agreement Tasks](ch15): Loop agreement tasks classified by algebraic topology.
16. [16 Immediate Snapshot Subdivisions](ch16): Discrete-geometry proof that the immediate snapshot complex is a subdivision.


---

## 1 Introduction

*PDF pp. 8–25*

Why concurrency matters and two classic problems that frame the book.

**1.1 Concurrency Everywhere**  
Multicores and networks make concurrency unavoidable.  
*Terms:* concurrency, multicore  
→ PDF pp. 8–13 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**1.2 Distributed Computing**  
What distributed computing models: processes, failures, communication.  
*Terms:* distributed computing, asynchrony, crash failures  
→ PDF pp. 14–16 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**1.3 Two Classic Distributed Computing Problems**  
Coordinated attack and consensus as motivating problems.  
*Terms:* two generals, coordinated attack, consensus  
→ PDF pp. 17–22 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch2"></a>
## 2 Two-Process Systems

*PDF pp. 26–44*

Two processes as a warm-up: tasks and protocols as graphs, and why consensus is impossible.

*Terms:* two-process tasks, graphs, approximate agreement, consensus impossibility, read-write memory, message passing

→ PDF pp. 26–44 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch3"></a>
## 3 Elements of Combinatorial Topology

*PDF pp. 45–69*

The topology the book uses: simplicial complexes, maps, subdivisions and connectivity.

*Terms:* simplicial complex, simplicial map, chromatic complex, subdivision, barycentric subdivision, carrier map, connectivity, Sperner lemma

→ PDF pp. 45–69 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch4"></a>
## 4 Colorless Wait-Free Computation

*PDF pp. 70–96*

Colorless tasks in the wait-free read-write model and their exact solvability condition.

*Terms:* colorless task, wait-free, read-write memory, barycentric agreement, set agreement, colorless protocol complex, solvability theorem

→ PDF pp. 70–96 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch5"></a>
## 5 Solvability of Colorless Tasks in Different Models

*PDF pp. 97–121*

How solvability of colorless tasks changes with resilience, objects and message passing.

*Terms:* t-resilience, message passing, adversaries, test-and-set, shared objects, colorless computability

→ PDF pp. 97–121 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch6"></a>
## 6 Byzantine-Resilient Colorless Computation

*PDF pp. 122–132*

Colorless computation when some processes are Byzantine.

**6.1 Byzantine Failures**  
Byzantine failure model.  
*Terms:* Byzantine failures  
→ PDF pp. 122–123 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**6.2 Byzantine Communication Abstractions**  
Reliable broadcast and related abstractions.  
*Terms:* reliable broadcast  
→ PDF pp. 124–126 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**6.3 Byzantine Set Agreement**  
Set agreement with Byzantine processes.  
*Terms:* set agreement  
→ PDF p. 127 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**6.4 Byzantine Barycentric Agreement**  
Barycentric agreement with Byzantine processes.  
*Terms:* barycentric agreement  
→ PDF p. 127 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**6.5 Byzantine Task Solvability**  
Solvability of colorless tasks under Byzantine failures.  
*Terms:* Byzantine task solvability  
→ PDF pp. 128–129 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**6.6 Byzantine Shared Memory**  
Byzantine shared memory.  
*Terms:* Byzantine shared memory  
→ PDF p. 130 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch7"></a>
## 7 Simulations and Reductions

*PDF pp. 133–144*

Simulating one model in another to transfer results.

**7.1 Motivation**  
Why reductions are useful.  
*Terms:* reductions  
→ PDF pp. 133–134 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**7.2 Combinatorial Setting**  
Simulations as simplicial maps.  
*Terms:* simulation, combinatorial  
→ PDF pp. 135–136 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**7.3 Applications**  
Consequences for colorless tasks.  
*Terms:* applications  
→ PDF p. 137 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**7.4 BG Simulation**  
Borowsky–Gafni simulation of t-resilient by wait-free systems.  
*Terms:* BG simulation  
→ PDF pp. 138–140 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch8"></a>
## 8 Read-Write Protocols for General Tasks

*PDF pp. 145–161*

General (colored) tasks and read-write protocols for them.

**8.1 Overview**  
From colorless to colored tasks.  
*Terms:* general tasks  
→ PDF p. 145 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**8.2 Tasks**  
Task definitions with input, output complexes and carrier maps.  
*Terms:* task specification  
→ PDF pp. 146–147 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**8.3 Examples of Tasks**  
Examples: consensus, set agreement, renaming, weak symmetry breaking.  
*Terms:* renaming, weak symmetry breaking  
→ PDF pp. 148–153 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**8.4 Protocols**  
Layered immediate-snapshot protocols.  
*Terms:* layered immediate snapshot, protocol complex  
→ PDF pp. 154–158 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch9"></a>
## 9 Manifold Protocols

*PDF pp. 162–185*

Protocols whose complexes are pseudomanifolds, and impossibility via Sperner-type arguments.

*Terms:* pseudomanifold, manifold protocol, Sperner lemma, set agreement impossibility, weak symmetry breaking

→ PDF pp. 162–185 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch10"></a>
## 10 Connectivity

*PDF pp. 186–199*

Connectivity of protocol complexes as the source of impossibility results.

**10.1 Consensus and Path Connectivity**  
Consensus fails because the protocol complex is path connected.  
*Terms:* consensus impossibility, path connectivity  
→ PDF pp. 186–187 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**10.2 Immediate Snapshot Model and Connectivity**  
Immediate snapshot complexes are connected.  
*Terms:* immediate snapshot  
→ PDF pp. 188–193 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**10.3 k-Set agreement and (k−1)-connectivity**  
k-set agreement fails because of (k−1)-connectivity.  
*Terms:* k-set agreement, k-connectivity  
→ PDF p. 194 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**10.4 Immediate Snapshot Model and k-Connectivity**  
Higher connectivity of immediate snapshot complexes.  
*Terms:* higher connectivity  
→ PDF pp. 194–197 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch11"></a>
## 11 Wait-Free Computability for General Tasks

*PDF pp. 200–223*

The asynchronous computability theorem characterizing wait-free solvable tasks.

*Terms:* asynchronous computability theorem, wait-free solvability, chromatic subdivision, simplicial approximation

→ PDF pp. 200–223 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch12"></a>
## 12 Renaming and Oriented Manifolds

*PDF pp. 224–239*

Renaming and weak symmetry breaking via orientations of manifolds.

*Terms:* renaming, oriented manifold, weak symmetry breaking, index lemma, counting

→ PDF pp. 224–239 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch13"></a>
## 13 Task Solvability in Different Models

*PDF pp. 240–264*

Colored task solvability in models beyond wait-free read-write.

*Terms:* t-resilient, adversaries, colored tasks, model comparisons

→ PDF pp. 240–264 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch14"></a>
## 14 Simulations and Reductions for Colored Tasks

*PDF pp. 265–279*

Reductions between shared-memory models for colored tasks.

**14.1 Model**  
Model setting.  
*Terms:* model  
→ PDF pp. 265–266 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**14.2 Shared-Memory Models**  
Shared-memory variants.  
*Terms:* shared-memory models  
→ PDF pp. 267–268 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**14.3 Trivial Reductions**  
Easy reductions.  
*Terms:* trivial reductions  
→ PDF p. 269 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**14.4 Layered Snapshot from Read-Write**  
Layered snapshot from read-write.  
*Terms:* layered snapshot  
→ PDF pp. 269–270 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**14.5 Immediate Snapshot from Snapshot**  
Immediate snapshot from snapshot.  
*Terms:* immediate snapshot  
→ PDF p. 271 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**14.6 Immediate Snapshot from Layered Immediate Snapshot**  
Immediate snapshot from layered immediate snapshot.  
*Terms:* layered immediate snapshot  
→ PDF pp. 272–275 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**14.7 Snapshot from Layered Snapshot**  
Snapshot from layered snapshot.  
*Terms:* snapshot  
→ PDF pp. 276–278 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch15"></a>
## 15 Classifying Loop Agreement Tasks

*PDF pp. 280–289*

Loop agreement tasks classified by algebraic topology.

**15.1 The Fundamental Group**  
The fundamental group.  
*Terms:* fundamental group  
→ PDF p. 281 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**15.2 Algebraic Signatures**  
Algebraic signatures of tasks.  
*Terms:* algebraic signature  
→ PDF pp. 282–283 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**15.3 Main Theorem**  
Main classification theorem.  
*Terms:* loop agreement  
→ PDF pp. 284–286 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**15.4 Applications**  
Applications.  
*Terms:* applications  
→ PDF p. 287 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

**15.5 Torsion Classes**  
Torsion classes.  
*Terms:* torsion  
→ PDF p. 288 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)


---

<a id="ch16"></a>
## 16 Immediate Snapshot Subdivisions

*PDF pp. 290–310*

Discrete-geometry proof that the immediate snapshot complex is a subdivision.

**16.1 A Glimpse of Discrete Geometry**  
A first look at discrete geometry.  
*Terms:* discrete geometry, chromatic subdivision  
→ PDF pp. 290–294 in [the PDF](https://drive.google.com/file/d/1xChCxVnGIY2ZcbBMSWjqwFVk779sdVUd/view)

