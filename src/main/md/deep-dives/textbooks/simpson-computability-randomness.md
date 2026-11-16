<a id="ch1"></a>
# Computability, Unsolvability, Randomness

> Stephen G. Simpson · Penn State lecture notes (2007), draft of February 2009 · [the PDF in Drive](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

Lecture notes taken during a one-semester course; homework sets, comments and solutions are interleaved with the sections and are not broken down separately. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An undergraduate course in recursion theory that ends at algorithmic randomness. It builds computability from register machines and primitive recursion, defines partial recursive functions with Gödel numbering, the enumeration and parametrization theorems, and proves the halting problem and other natural problems unsolvable, including word problems in group theory and Hilbert’s tenth problem. It then classifies unsolvable problems by the arithmetical hierarchy and by Turing degrees with oracles and the jump. The last third covers Kolmogorov complexity, effectively open and closed sets in Cantor space, Martin-Löf randomness and its characterization by initial-segment complexity, and advanced results such as the low basis theorem and the Kučera–Gács theorem.

**Contents**

1. [1. Computability](ch1): Computable functions via register machines, built up by composition, predicates and primitive recursion.
2. [2. Partial recursive functions](ch2): Partial functions, indices and the basic theorems about effective enumerations.
3. [3. Unsolvability](ch3): The halting problem and unsolvable problems across mathematics, compared by many-one reducibility.
4. [4. The arithmetical hierarchy](ch4): Classifying predicates by quantifier complexity (Σ⁰ₙ, Π⁰ₙ), complete sets and r.e.
5. [5. Oracles and relativization](ch5): Computing relative to an oracle, Turing degrees, the jump, and finite-extension constructions.
6. [6. Kolmogorov complexity](ch6): Plain and prefix-free Kolmogorov complexity and the Kraft–Chaitin theorem.
7. [7. The Cantor space](ch7): Partial recursive functionals and effectively open and closed subsets of 2^ℕ and ℕ^ℕ.
8. [8. Randomness](ch8): Why randomness matters for foundations, definitions of randomness, Martin-Löf randomness and initial-segment complexity.
9. [9. Some advanced topics](ch9): Degrees of random sequences, the low basis theorem, relative randomness, Kučera–Gács, and LR/LK reducibility.


---

## 1. Computability

*PDF pp. 6–23*

Computable functions via register machines, built up by composition, predicates and primitive recursion.

**1.1 Computable functions**  
Register machine programs and computable functions.  
*Terms:* register machine, computable function  
→ PDF pp. 6–8 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**1.2 Composing computable functions**  
Closure under composition.  
*Terms:* composition  
→ PDF pp. 9–11 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**1.3 Computable predicates**  
Computable predicates, bounded quantifiers and the μ-operator.  
*Terms:* computable predicate, mu-operator, bounded quantifier  
→ PDF pp. 12–16 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**1.4 Primitive recursion**  
Primitive recursion.  
*Terms:* primitive recursion  
→ PDF pp. 17–19 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**1.5 Prime power coding**  
Coding sequences with prime powers.  
*Terms:* prime power coding, sequence coding  
→ PDF pp. 20–21 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**1.6 Computable real numbers**  
Computable real numbers.  
*Terms:* computable real numbers  
→ PDF pp. 22–23 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch2"></a>
## 2. Partial recursive functions

*PDF pp. 24–32*

Partial functions, indices and the basic theorems about effective enumerations.

**2.1 Partial recursive functions**  
Partial recursive functions and the μ-operator.  
*Terms:* partial recursive function  
→ PDF pp. 24–25 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**2.2 Gödel numbers and indices**  
Gödel numbers and indices of programs.  
*Terms:* Gödel number, index  
→ PDF pp. 26–27 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**2.3 The Enumeration Theorem**  
The Enumeration Theorem: one universal function enumerates all.  
*Terms:* enumeration theorem  
→ PDF pp. 28–29 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**2.4 The Parametrization Theorem**  
The Parametrization (s-m-n) Theorem.  
*Terms:* parametrization theorem, s-m-n theorem  
→ PDF pp. 30–31 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**2.5 Universal partial recursive functions**  
Universal partial recursive functions.  
*Terms:* universal function  
→ PDF p. 32 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch3"></a>
## 3. Unsolvability

*PDF pp. 33–42*

The halting problem and unsolvable problems across mathematics, compared by many-one reducibility.

**3.1 Noncomputable sets and functions**  
Diagonal arguments give noncomputable sets.  
*Terms:* noncomputable set, diagonalization  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**3.2 An unsolvable decision problem**  
The halting set K is undecidable.  
*Terms:* halting problem, K  
→ PDF p. 34 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**3.3 Almost all problems are unsolvable**  
Counting shows almost all functions are noncomputable.  
*Terms:* cardinality argument  
→ PDF p. 35 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**3.4 Unsolvable problems in core mathematics**  
Word problems for groups and other natural unsolvable problems.  
*Terms:* word problem, Boone-Novikov theorem  
→ PDF pp. 36–38 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**3.5 A remark on Hilbert’s 10th Problem**  
Diophantine sets and Hilbert’s tenth problem.  
*Terms:* Hilbert’s tenth problem, Diophantine set, MRDP  
→ PDF p. 39 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**3.6 Many-one reducibility**  
Many-one reducibility as a way to compare problems.  
*Terms:* many-one reducibility  
→ PDF pp. 40–42 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch4"></a>
## 4. The arithmetical hierarchy

*PDF pp. 43–55*

Classifying predicates by quantifier complexity (Σ⁰ₙ, Π⁰ₙ), complete sets and r.e. sets.

**4.1 Definition of the arithmetical hierarchy**  
Σ⁰ₙ, Π⁰ₙ and Δ⁰ₙ predicates.  
*Terms:* arithmetical hierarchy, Sigma-n, Pi-n, Delta-n  
→ PDF p. 43 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**4.2 Closure properties**  
Closure under Boolean operations and quantifiers.  
*Terms:* closure properties  
→ PDF pp. 44–45 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**4.3 Distinguishing levels of the hierarchy**  
Each level is strictly larger than the last.  
*Terms:* hierarchy theorem  
→ PDF pp. 46–47 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**4.4 Many-one completeness**  
Complete sets at each level.  
*Terms:* many-one complete  
→ PDF p. 48 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**4.5 Recursively enumerable sets**  
Recursively enumerable sets and their characterizations.  
*Terms:* recursively enumerable set  
→ PDF pp. 49–50 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**4.7 Recursively enumerable sets**  
Simple and creative sets.  
*Terms:* simple set, creative set  
→ PDF pp. 51–52 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**4.8 Parametrization and uniformity**  
Uniform operations on r.e. sets.  
*Terms:* uniformity  
→ PDF pp. 53–55 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch5"></a>
## 5. Oracles and relativization

*PDF pp. 56–79*

Computing relative to an oracle, Turing degrees, the jump, and finite-extension constructions.

**5.1 Oracle computation**  
Computing with an oracle.  
*Terms:* oracle computation  
→ PDF pp. 56–57 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**5.2 Relativization**  
Relativizing earlier results.  
*Terms:* relativization  
→ PDF p. 58 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**5.3 Turing degrees**  
Turing reducibility and degrees.  
*Terms:* Turing reducibility, Turing degrees  
→ PDF pp. 58–59 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**5.4 The Turing jump operator**  
The jump operator and Post’s theorem.  
*Terms:* Turing jump, Post’s theorem  
→ PDF pp. 60–61 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**5.5 Finite approximation**  
Constructions by finite approximation.  
*Terms:* finite extension method  
→ PDF pp. 62–65 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**5.6 Structure of the Turing degrees**  
Structural facts about the degrees.  
*Terms:* structure of Turing degrees  
→ PDF pp. 66–79 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch6"></a>
## 6. Kolmogorov complexity

*PDF pp. 80–89*

Plain and prefix-free Kolmogorov complexity and the Kraft–Chaitin theorem.

**6.1 Kolmogorov complexity**  
Plain Kolmogorov complexity and incompressible strings.  
*Terms:* Kolmogorov complexity, incompressible  
→ PDF pp. 80–82 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**6.2 Prefix-free complexity**  
Prefix-free machines and complexity.  
*Terms:* prefix-free complexity  
→ PDF pp. 83–84 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**6.3 The Kraft/Chaitin Theorem**  
The Kraft–Chaitin theorem for building prefix-free machines.  
*Terms:* Kraft-Chaitin theorem  
→ PDF pp. 85–89 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch7"></a>
## 7. The Cantor space

*PDF pp. 90–103*

Partial recursive functionals and effectively open and closed subsets of 2^ℕ and ℕ^ℕ.

**7.1 Partial recursive functionals, etc**  
Partial recursive functionals on infinite sequences.  
*Terms:* partial recursive functional  
→ PDF pp. 90–93 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**7.3 Σ01 and Π01 sets in 2N and NN**  
Σ⁰₁ and Π⁰₁ classes in Cantor and Baire space.  
*Terms:* Pi01 class, Sigma01 class, Cantor space, Baire space  
→ PDF pp. 94–98 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**7.4 Compactness of 2N**  
Compactness of Cantor space.  
*Terms:* compactness  
→ PDF pp. 99–100 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**7.5 Σ01 and Π01 predicates in 2N**  
Σ⁰₁ and Π⁰₁ predicates on sequences.  
*Terms:* effectively closed set  
→ PDF pp. 101–103 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch8"></a>
## 8. Randomness

*PDF pp. 104–124*

Why randomness matters for foundations, definitions of randomness, Martin-Löf randomness and initial-segment complexity.

**8.1 Foundations of mathematics**  
Randomness and the foundations of mathematics.  
*Terms:* foundations of mathematics  
→ PDF p. 104 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**8.2 Definitions of randomness**  
Competing definitions of a random sequence.  
*Terms:* algorithmic randomness  
→ PDF pp. 105–108 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**8.4 Properties of Martin-Löf randomness**  
Martin-Löf tests and their properties, including a universal test.  
*Terms:* Martin-Löf randomness, universal test  
→ PDF pp. 109–118 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**8.7 Initial segment complexity**  
Random sequences have high initial-segment prefix complexity (Levin–Schnorr).  
*Terms:* Levin-Schnorr theorem, initial segment complexity  
→ PDF pp. 119–124 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)


---

<a id="ch9"></a>
## 9. Some advanced topics

*PDF pp. 125–150*

Degrees of random sequences, the low basis theorem, relative randomness, Kučera–Gács, and LR/LK reducibility.

**9.1 Turing degrees of random sequences**  
Turing degrees containing random sequences.  
*Terms:* degrees of random sequences  
→ PDF p. 125 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**9.2 The Low Basis Theorem**  
The low basis theorem for Π⁰₁ classes.  
*Terms:* low basis theorem  
→ PDF pp. 126–128 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**9.3 Randomness relative to an oracle**  
Randomness relative to an oracle.  
*Terms:* relative randomness  
→ PDF pp. 129–131 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**9.6 The Kučera/Gács Theorem**  
Every set is computable from a random sequence (Kučera–Gács).  
*Terms:* Kučera-Gács theorem  
→ PDF pp. 132–141 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

**9.11 LR- and LK-reducibility**  
LR- and LK-reducibility.  
*Terms:* LR-reducibility, LK-reducibility  
→ PDF pp. 142–150 in [the PDF](https://drive.google.com/file/d/127jSBS1xLQJcvq1WIal4DXkrzjp36mFx/view)

