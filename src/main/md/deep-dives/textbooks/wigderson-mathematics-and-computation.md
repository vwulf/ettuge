<a id="ch1"></a>
# Mathematics and Computation

> Avi Wigderson · Princeton University Press, 2019 (author’s online draft, August 2019) · [the PDF in Drive](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

The long reference list is not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A panoramic tour of the theory of computation written for mathematicians and curious scientists rather than specialists. Wigderson surveys computational complexity (P, NP, reductions, circuits and lower bounds, proof complexity), the role of randomness (pseudo-randomness, derandomization, expanders, extractors), interactive and probabilistically checkable proofs, quantum and arithmetic complexity, and models of limited resources (space, communication, online, learning, cryptography, distributed computing). A long interlude shows concrete two-way traffic between complexity and fields from number theory to invariant theory, and the epilogue argues that computation is a lens on all of science.

**Contents**

1. [Introduction](ch1): Why math and computation are intertwined, and how the book is organized.
2. [Prelude: Computation, undecidability, and limits to mathematical knowledge](ch2): Turing, Gödel and the limits of what can be computed or proved.
3. [Computational complexity 101: The basics, P, and NP](ch3): The core definitions of efficient computation and verification.
4. [Problems and classes inside (and around) NP](ch4): Search, counting and other problem types, and what lies between P and NP.
5. [Lower bounds, Boolean circuits, and attacks on P vs. NP](ch5): Why proving lower bounds is hard and what circuits reveal.
6. [Proof complexity](ch6): How long must proofs of tautologies be?.
7. [Randomness in computation](ch7): What randomness buys algorithms, and why it may be unnecessary.
8. [Abstract pseudo-randomness](ch8): Pseudo-randomness as a unifying idea across mathematics.
9. [Weak random sources and randomness extractors](ch9): Purifying imperfect sources of randomness.
10. [Randomness and interaction in proofs](ch10): Proofs that use interaction and randomness.
11. [Quantum computing](ch11): Quantum computation from the complexity viewpoint.
12. [Arithmetic complexity](ch12): The complexity of computing polynomials.
13. [Interlude: Concrete interactions between math and computational complexity](ch13): Concrete results where complexity meets other fields.
14. [Space complexity: Modeling limited memory](ch14): Computation with limited memory.
15. [Communication complexity: Modeling information bottlenecks](ch15): Lower bounds from limited communication.
16. [On-line algorithms: Coping with an unknown future](ch16): Decisions without knowing the future.
17. [Computational learning theory, AI, and beyond](ch17): Learning theory from computational and statistical angles.
18. [Cryptography: Modeling secrets and lies, knowledge and trust](ch18): Complexity-based cryptography.
19. [Distributed computing: Coping with asynchrony](ch19): Distributed computing as coping with uncertainty and asynchrony.
20. [Epilogue: A broader perspective of ToC](ch20): The theory of computation in a wider frame.


---

## Introduction

*PDF pp. 17–26*

Why math and computation are intertwined, and how the book is organized.

**On the interactions of math and computation**  
Historical and conceptual links between mathematics and computing.  
*Terms:* mathematics and computation  
→ PDF pp. 17–19 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Computational complexity theory**  
What complexity theory asks.  
*Terms:* complexity theory  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The nature, purpose, and style of this book**  
The book’s aims and informal style.  
*Terms:* style  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Who is this book for?**  
Intended readers.  
*Terms:* audience  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Organization of the book**  
A chapter-by-chapter guide.  
*Terms:* organization  
→ PDF pp. 22–25 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Notation and conventions**  
Notation.  
*Terms:* notation  
→ PDF p. 26 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch2"></a>
## Prelude: Computation, undecidability, and limits to mathematical knowledge

*PDF pp. 27–30*

Turing, Gödel and the limits of what can be computed or proved.

*Terms:* undecidability, halting problem, Turing machine, Gödel incompleteness, Hilbert program

→ PDF pp. 27–30 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch3"></a>
## Computational complexity 101: The basics, P, and NP

*PDF pp. 31–52*

The core definitions of efficient computation and verification.

**Motivating examples**  
Examples of easy and hard problems.  
*Terms:* examples  
→ PDF pp. 31–32 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Efficient computation and the class P**  
Polynomial time and the class P.  
*Terms:* P, polynomial time  
→ PDF pp. 33–35 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Efficient verification and the class NP**  
Efficient verification and NP.  
*Terms:* NP, verification  
→ PDF pp. 36–38 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The P vs. NP question: Its meaning and importance**  
Why P vs. NP matters.  
*Terms:* P vs NP  
→ PDF pp. 39–41 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The class coNP, the NP vs. coNP question, and efficiently characterizable structures**  
coNP and efficient characterizations.  
*Terms:* coNP, good characterization  
→ PDF pp. 42–44 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Reductions: A partial order of computational difficulty**  
Reductions.  
*Terms:* reductions  
→ PDF p. 45 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Completeness: Problems capturing complexity classes**  
Complete problems.  
*Terms:* completeness  
→ PDF p. 46 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**NP-completeness**  
The Cook–Levin theorem.  
*Terms:* NP-completeness, Cook-Levin  
→ PDF pp. 46–47 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Some NP-complete problems**  
Classic NP-complete problems.  
*Terms:* SAT, 3-coloring  
→ PDF p. 48 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The nature and impact of NP-completeness**  
The impact of NP-completeness across sciences.  
*Terms:* impact  
→ PDF pp. 49–52 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch4"></a>
## Problems and classes inside (and around) NP

*PDF pp. 53–63*

Search, counting and other problem types, and what lies between P and NP.

**Other types of computational problems and complexity classes**  
Search, optimization, counting and their classes.  
*Terms:* search problems, #P  
→ PDF p. 53 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Between P and NP**  
Factoring, graph isomorphism and Ladner’s theorem.  
*Terms:* Ladner theorem, graph isomorphism, factoring  
→ PDF pp. 54–55 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Constraint satisfaction problems (CSPs)**  
CSPs and dichotomy theorems.  
*Terms:* CSP, dichotomy  
→ PDF pp. 56–58 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Average-case complexity**  
Hardness on average.  
*Terms:* average-case complexity  
→ PDF p. 59 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**One-way functions, trap-door functions, and cryptography**  
One-way functions and cryptography.  
*Terms:* one-way functions, trapdoor, cryptography  
→ PDF pp. 60–63 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch5"></a>
## Lower bounds, Boolean circuits, and attacks on P vs. NP

*PDF pp. 64–72*

Why proving lower bounds is hard and what circuits reveal.

**Diagonalization and relativization**  
Diagonalization and the relativization barrier.  
*Terms:* diagonalization, relativization  
→ PDF p. 64 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Boolean circuits**  
Circuit lower bounds, natural proofs and restricted models.  
*Terms:* Boolean circuits, lower bounds, natural proofs, monotone circuits  
→ PDF pp. 65–72 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch6"></a>
## Proof complexity

*PDF pp. 73–85*

How long must proofs of tautologies be?

**The pigeonhole principle—a motivating example**  
The pigeonhole principle as a hard tautology.  
*Terms:* pigeonhole principle  
→ PDF p. 75 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Propositional proof systems and NP vs. coNP**  
Proof systems and NP vs. coNP.  
*Terms:* propositional proof systems, Cook-Reckhow  
→ PDF p. 76 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Concrete proof systems**  
Resolution, Frege, cutting planes and algebraic systems.  
*Terms:* resolution, Frege, cutting planes  
→ PDF pp. 77–83 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Proof complexity vs. circuit complexity**  
Links between proof and circuit lower bounds.  
*Terms:* proof complexity vs circuit complexity  
→ PDF pp. 84–85 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch7"></a>
## Randomness in computation

*PDF pp. 86–97*

What randomness buys algorithms, and why it may be unnecessary.

**The power of randomness in algorithms**  
Randomized algorithms such as polynomial identity testing.  
*Terms:* randomized algorithms, BPP, polynomial identity testing  
→ PDF pp. 86–87 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The weakness of randomness in algorithms**  
Hardness versus randomness and derandomization.  
*Terms:* derandomization, hardness vs randomness  
→ PDF pp. 88–90 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Computational pseudo-randomness and pseudo-random generators**  
Pseudo-random generators from hard functions.  
*Terms:* pseudo-random generators  
→ PDF pp. 91–97 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch8"></a>
## Abstract pseudo-randomness

*PDF pp. 98–112*

Pseudo-randomness as a unifying idea across mathematics.

**Motivating examples**  
Examples.  
*Terms:* pseudo-randomness  
→ PDF p. 98 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**General pseudo-random properties and finding hay in haystacks**  
Finding explicit objects with random-like properties.  
*Terms:* explicit constructions  
→ PDF p. 99 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The Riemann hypothesis**  
The Riemann hypothesis as a pseudo-randomness statement.  
*Terms:* Riemann hypothesis  
→ PDF pp. 100–101 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**P vs. NP**  
P vs. NP in the same light.  
*Terms:* P vs NP  
→ PDF p. 102 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Computational pseudo-randomness and de-randomization**  
Derandomization.  
*Terms:* derandomization  
→ PDF pp. 103–104 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Quasi-random graphs**  
Quasi-random graphs.  
*Terms:* quasi-random graphs  
→ PDF p. 105 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Expanders**  
Expander graphs.  
*Terms:* expanders  
→ PDF pp. 106–108 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Structure vs. pseudo-randomness**  
The structure-versus-randomness dichotomy.  
*Terms:* structure vs randomness  
→ PDF pp. 109–112 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch9"></a>
## Weak random sources and randomness extractors

*PDF pp. 113–118*

Purifying imperfect sources of randomness.

**Min-entropy and randomness extractors**  
Min-entropy and extractors.  
*Terms:* min-entropy, randomness extractor  
→ PDF pp. 114–115 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Explicit constructions of extractors**  
Explicit extractor constructions.  
*Terms:* explicit constructions  
→ PDF pp. 116–117 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Structured weak sources, and deterministic extractors**  
Deterministic extractors for structured sources.  
*Terms:* deterministic extractors  
→ PDF p. 118 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch10"></a>
## Randomness and interaction in proofs

*PDF pp. 119–129*

Proofs that use interaction and randomness.

**Interactive proof systems**  
Interactive proofs and IP = PSPACE.  
*Terms:* interactive proofs, IP=PSPACE  
→ PDF pp. 120–121 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Zero-knowledge proof systems**  
Zero-knowledge proofs.  
*Terms:* zero-knowledge  
→ PDF pp. 122–124 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Probabilistically checkable proofs (PCPs), and hardness of approximation**  
The PCP theorem and hardness of approximation.  
*Terms:* PCP theorem, hardness of approximation  
→ PDF pp. 125–126 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Perspective and impact**  
Their influence.  
*Terms:* impact  
→ PDF pp. 127–129 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch11"></a>
## Quantum computing

*PDF pp. 130–139*

Quantum computation from the complexity viewpoint.

**Building a quantum computer**  
Physical challenges.  
*Terms:* quantum computer  
→ PDF p. 133 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Quantum proofs, quantum Hamiltonian complexity, and dynamics**  
QMA and Hamiltonian complexity.  
*Terms:* QMA, local Hamiltonian  
→ PDF pp. 134–136 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Quantum interactive proofs, and testing quantum mechanics**  
Quantum interactive proofs and testing quantum mechanics.  
*Terms:* quantum interactive proofs  
→ PDF p. 137 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Quantum randomness: Certification and expansion**  
Certified randomness.  
*Terms:* certified randomness  
→ PDF pp. 138–139 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch12"></a>
## Arithmetic complexity

*PDF pp. 140–150*

The complexity of computing polynomials.

**Motivation: Univariate polynomials**  
Univariate examples.  
*Terms:* arithmetic complexity  
→ PDF p. 140 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Basic definitions, questions, and results**  
Arithmetic circuits and formulas.  
*Terms:* arithmetic circuits  
→ PDF pp. 140–141 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The complexity of basic polynomials**  
Determinant, permanent and matrix multiplication.  
*Terms:* determinant, permanent, matrix multiplication  
→ PDF pp. 142–145 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Reductions and completeness, VP and VNP**  
VP vs. VNP.  
*Terms:* VP, VNP, Valiant  
→ PDF pp. 146–147 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Restricted models**  
Restricted models.  
*Terms:* restricted models  
→ PDF pp. 148–150 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch13"></a>
## Interlude: Concrete interactions between math and computational complexity

*PDF pp. 151–169*

Concrete results where complexity meets other fields.

**Number theory**  
Number theory.  
*Terms:* number theory  
→ PDF pp. 151–152 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Combinatorial geometry**  
Combinatorial geometry.  
*Terms:* combinatorial geometry  
→ PDF p. 153 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Operator theory**  
Operator theory (Kadison–Singer).  
*Terms:* Kadison-Singer  
→ PDF p. 154 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Metric geometry**  
Metric embeddings.  
*Terms:* metric embeddings  
→ PDF p. 155 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Group theory**  
Group theory.  
*Terms:* group theory  
→ PDF pp. 156–157 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Statistical physics**  
Statistical physics.  
*Terms:* statistical physics  
→ PDF pp. 158–159 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Analysis and probability**  
Analysis and probability.  
*Terms:* Fourier analysis  
→ PDF pp. 160–162 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Lattice theory**  
Lattices.  
*Terms:* lattices  
→ PDF pp. 163–164 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Invariant theory**  
Invariant theory and GCT.  
*Terms:* invariant theory, geometric complexity theory  
→ PDF pp. 165–169 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch14"></a>
## Space complexity: Modeling limited memory

*PDF pp. 170–176*

Computation with limited memory.

**Basic space complexity**  
L, PSPACE and Savitch’s theorem.  
*Terms:* space complexity, Savitch  
→ PDF pp. 170–171 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Streaming and sketching**  
Streaming algorithms and sketches.  
*Terms:* streaming, sketching  
→ PDF pp. 172–173 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Finite automata and counting**  
Automata and counting.  
*Terms:* finite automata  
→ PDF pp. 174–176 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch15"></a>
## Communication complexity: Modeling information bottlenecks

*PDF pp. 177–194*

Lower bounds from limited communication.

**Basic definitions and results**  
Two-party protocols and rank, fooling sets.  
*Terms:* communication complexity  
→ PDF pp. 177–179 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Applications**  
Applications to circuits, data structures, streaming.  
*Terms:* applications  
→ PDF pp. 180–187 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Interactive information theory and coding theory**  
Information complexity and interactive coding.  
*Terms:* information complexity, interactive coding  
→ PDF pp. 188–194 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch16"></a>
## On-line algorithms: Coping with an unknown future

*PDF pp. 195–200*

Decisions without knowing the future.

**Paging, caching, and the k-server problem**  
Competitive analysis of paging and k-server.  
*Terms:* online algorithms, competitive ratio, paging, k-server  
→ PDF p. 196 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Expert advice, portfolio management, repeated games, and the multiplicative weights algorithm**  
Experts and multiplicative weights.  
*Terms:* multiplicative weights, experts  
→ PDF pp. 197–200 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch17"></a>
## Computational learning theory, AI, and beyond

*PDF pp. 201–217*

Learning theory from computational and statistical angles.

**Classifying hyperplanes: A motivating example**  
Learning a separating hyperplane.  
*Terms:* perceptron  
→ PDF pp. 202–203 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Classification/Identification: Some choices and modeling issues**  
Modeling choices for learning.  
*Terms:* learning models  
→ PDF p. 204 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Identification in the limit: A linguistic/recursion theoretic approach**  
Gold’s identification in the limit.  
*Terms:* identification in the limit  
→ PDF pp. 205–207 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Probably, approximately correct (PAC) learning: A statistical approach**  
PAC learning, VC dimension, boosting.  
*Terms:* PAC learning, VC dimension, boosting  
→ PDF pp. 208–217 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch18"></a>
## Cryptography: Modeling secrets and lies, knowledge and trust

*PDF pp. 218–233*

Complexity-based cryptography.

**The ambitions of modern cryptography**  
What modern crypto aims for.  
*Terms:* cryptography  
→ PDF p. 218 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Information theory vs. complexity theory: Take 1**  
Shannon secrecy vs. computational secrecy.  
*Terms:* perfect secrecy  
→ PDF p. 219 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The axioms of modern, complexity-based cryptography**  
One-way functions as axioms.  
*Terms:* one-way functions  
→ PDF p. 219 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Cryptographic definitions**  
Defining security.  
*Terms:* security definitions  
→ PDF pp. 220–221 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Probabilistic encryption**  
Probabilistic encryption.  
*Terms:* probabilistic encryption  
→ PDF p. 222 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Basic paradigms for security definitions**  
Simulation-based definitions.  
*Terms:* simulation paradigm  
→ PDF pp. 223–226 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Secure multi-party computation**  
Secure multi-party computation.  
*Terms:* secure multiparty computation  
→ PDF pp. 227–228 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Information theory vs. complexity theory: Take 2**  
Revisiting information vs. complexity.  
*Terms:* information theoretic  
→ PDF p. 229 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**More recent advances**  
FHE, obfuscation and other advances.  
*Terms:* homomorphic encryption, obfuscation  
→ PDF pp. 230–231 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Physical attacks**  
Side-channel attacks.  
*Terms:* side channels  
→ PDF p. 232 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The complexity of factoring**  
The difficulty of factoring.  
*Terms:* factoring  
→ PDF p. 233 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch19"></a>
## Distributed computing: Coping with asynchrony

*PDF pp. 234–247*

Distributed computing as coping with uncertainty and asynchrony.

**High-level modeling issues**  
Modeling issues.  
*Terms:* distributed models  
→ PDF pp. 234–235 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Sharing resources and the dining philosophers problem**  
Dining philosophers.  
*Terms:* dining philosophers  
→ PDF pp. 236–237 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Coordination: Consensus and Byzantine generals**  
Consensus and Byzantine agreement.  
*Terms:* consensus, Byzantine generals  
→ PDF pp. 238–239 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Renaming, k-set agreement, and beyond**  
Renaming and k-set agreement via topology.  
*Terms:* renaming, k-set agreement, topology  
→ PDF pp. 240–245 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Local synchronous coloring**  
Local coloring.  
*Terms:* local algorithms, coloring  
→ PDF pp. 246–247 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)


---

<a id="ch20"></a>
## Epilogue: A broader perspective of ToC

*PDF pp. 248–281*

The theory of computation in a wider frame.

**Close collaborations and interactions**  
Collaborations with other sciences.  
*Terms:* interdisciplinary  
→ PDF pp. 249–253 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**What is computation?**  
What counts as computation.  
*Terms:* computation  
→ PDF p. 254 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**ToC methodology**  
ToC’s methodology.  
*Terms:* methodology  
→ PDF pp. 255–257 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The computational complexity lens on the sciences**  
Computation as a lens on biology, physics, economics and more.  
*Terms:* sciences  
→ PDF pp. 258–268 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Conceptual contributions; or, algorithms and philosophy**  
Philosophical contributions.  
*Terms:* philosophy  
→ PDF pp. 269–270 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Algorithms and technology**  
Technology.  
*Terms:* technology  
→ PDF pp. 271–272 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**Some important challenges of ToC**  
Open challenges.  
*Terms:* open problems  
→ PDF pp. 273–277 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**K–12 education**  
Education.  
*Terms:* education  
→ PDF pp. 278–279 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

**The ToC community**  
The research community.  
*Terms:* community  
→ PDF pp. 280–281 in [the PDF](https://drive.google.com/file/d/1eLYGv4VWu9qOWTEvj6uxuCP6RtFqyHtx/view)

