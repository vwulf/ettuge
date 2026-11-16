<a id="ch1"></a>
# Foundations of Probabilistic Programming

> Gilles Barthe, Joost-Pieter Katoen and Alexandra Silva (eds.) · Cambridge University Press, 2020 (open access) · [the PDF in Drive](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

An edited volume of 15 contributed chapters. Introduction, conclusion and related-work sections are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A survey volume on the theory of probabilistic programs, from the semantics of languages with random choice and conditioning to methods for verifying and analyzing them. It covers measure-theoretic and computable semantics, probabilistic λ-calculi, relational verification with couplings, expected-runtime calculi, termination via martingales, concentration-of-measure analysis, a logical/categorical account of Bayesian reasoning, quantitative equational reasoning, probabilistic abstract interpretation for privacy, quantitative information flow in Haskell, and three applied languages: Luck for property-based testing generators, Tabular for spreadsheet inference, and Rely for reasoning about unreliable hardware.

**Contents**

1. [1 Semantics of Probabilistic Programming: A Gentle Introduction](ch1): A gentle introduction to the semantics of probabilistic programs.
2. [2 Probabilistic Programs as Measures](ch2): Programs as measures, and the measurability problems.
3. [3 An Application of Computable Distributions to the Semantics of Probabilistic Programs](ch3): Computable distributions as a semantic basis.
4. [4 On Probabilistic λ-Calculi](ch4): Probabilistic λ-calculi.
5. [5 Probabilistic Couplings from Program Logics](ch5): Relational verification with couplings.
6. [6 Expected Runtime Analysis by Program Verification](ch6): Reasoning about expected running time.
7. [7 Termination Analysis of Probabilistic Programs with Martingales](ch7): Termination analysis with supermartingales.
8. [8 Quantitative Analysis of Programs with Probabilities and Concentration of Measure Inequalities](ch8): Quantitative analysis via concentration inequalities.
9. [9 The Logical Essentials of Bayesian Reasoning](ch9): A logical and categorical account of Bayesian reasoning.
10. [10 Quantitative Equational Reasoning](ch10): Equational logic with distances.
11. [11 Probabilistic Abstract Interpretation: Sound Inference and Application to Privacy](ch11): Abstract interpretation for probabilistic inference and privacy.
12. [12 Quantitative Information Flow with Monads in Haskell](ch12): Quantitative information flow in Haskell.
13. [13 Luck: A Probabilistic Language for Testing](ch13): Luck: a language for test-data generators.
14. [14 Tabular: Probabilistic Inference from the Spreadsheet](ch14): Tabular: Bayesian models in spreadsheets.
15. [15 Programming Unreliable Hardware](ch15): Reasoning about programs on unreliable hardware.


---

## 1 Semantics of Probabilistic Programming: A Gentle Introduction

*PDF pp. 17–58*

A gentle introduction to the semantics of probabilistic programs.

**Measure theory: What you need to know**  
The measure theory needed.  
*Terms:* measure theory, sigma-algebra, Lebesgue integral  
→ PDF pp. 21–30 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Semantics of a simple imperative probabilistic language**  
Semantics of a simple imperative probabilistic language.  
*Terms:* imperative probabilistic language, denotational semantics, Kozen  
→ PDF pp. 31–58 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch2"></a>
## 2 Probabilistic Programs as Measures

*PDF pp. 59–90*

Programs as measures, and the measurability problems.

**Informal semantics for probabilistic programming**  
Informal semantics with sampling and scoring.  
*Terms:* sample, score, observe  
→ PDF pp. 60–70 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Introduction to measurability issues**  
Measurability issues with higher-order functions.  
*Terms:* measurability, Borel  
→ PDF pp. 71–77 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Formal semantics of probabilistic programs as measures**  
Formal semantics as measures (s-finite kernels).  
*Terms:* s-finite kernels  
→ PDF pp. 78–85 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Reasoning with measures**  
Reasoning with measures.  
*Terms:* equational reasoning  
→ PDF p. 86 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Other approaches to semantics and open questions**  
Other approaches and open questions.  
*Terms:* quasi-Borel spaces  
→ PDF pp. 87–90 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch3"></a>
## 3 An Application of Computable Distributions to the Semantics of Probabilistic Programs

*PDF pp. 91–136*

Computable distributions as a semantic basis.

**Computability Revisited**  
Computability over reals.  
*Terms:* computable analysis  
→ PDF pp. 93–97 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**A Library for Computable Distributions**  
A library of computable distributions.  
*Terms:* computable distributions  
→ PDF pp. 98–104 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Mathematical Structures for Modeling the Library**  
Domain-theoretic structures.  
*Terms:* domains  
→ PDF pp. 105–118 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**A Semantics for a Core Language**  
Semantics for a core language.  
*Terms:* semantics  
→ PDF pp. 119–127 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Bayesian Inference**  
Bayesian inference computably.  
*Terms:* Bayesian inference, conditioning  
→ PDF pp. 128–131 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch4"></a>
## 4 On Probabilistic λ-Calculi

*PDF pp. 137–160*

Probabilistic λ-calculi.

**A Bird’s Eye View on Probabilistic Lambda Calculi**  
Overview of design choices.  
*Terms:* probabilistic lambda calculus  
→ PDF pp. 140–141 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**A Typed λ-Calculus with Binary Probabilistic Choice**  
A typed λ-calculus with binary choice and its operational semantics.  
*Terms:* typed calculus, binary choice  
→ PDF pp. 142–153 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Sampling and Conditioning**  
Sampling and conditioning.  
*Terms:* sampling, conditioning  
→ PDF pp. 154–160 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch5"></a>
## 5 Probabilistic Couplings from Program Logics

*PDF pp. 161–200*

Relational verification with couplings.

**Couplings and liftings: definitions and basic properties**  
Couplings and liftings.  
*Terms:* coupling, lifting  
→ PDF pp. 165–171 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Proof by coupling**  
Proof by coupling.  
*Terms:* proof by coupling  
→ PDF p. 172 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**A formal logic for coupling proofs**  
pRHL, a program logic for couplings.  
*Terms:* probabilistic relational Hoare logic  
→ PDF pp. 173–184 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Constructing couplings, formally**  
Constructing couplings formally.  
*Terms:* coupling construction  
→ PDF pp. 185–192 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch6"></a>
## 6 Expected Runtime Analysis by Program Verification

*PDF pp. 201–236*

Reasoning about expected running time.

**Probabilistic Programs**  
Probabilistic guarded commands.  
*Terms:* pGCL  
→ PDF pp. 204–206 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Semantic Intricacies**  
Semantic subtleties (positive almost-sure termination).  
*Terms:* almost-sure termination  
→ PDF pp. 207–208 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**The Expected Runtime Calculus**  
The ert calculus.  
*Terms:* expected runtime transformer  
→ PDF pp. 209–212 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Proof Rules for Loops**  
Proof rules for loops.  
*Terms:* loop invariants  
→ PDF pp. 213–224 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Application: Bayesian networks**  
Bayesian network sampling runtime.  
*Terms:* Bayesian networks  
→ PDF pp. 225–228 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch7"></a>
## 7 Termination Analysis of Probabilistic Programs with Martingales

*PDF pp. 237–274*

Termination analysis with supermartingales.

**Theoretical Foundations for Bounded Termination**  
Theory of bounded termination.  
*Terms:* ranking supermartingales  
→ PDF pp. 246–253 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Algorithms for Proving Bounded Termination**  
Algorithms (ranking supermartingales).  
*Terms:* algorithms, linear programming  
→ PDF pp. 254–256 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Beyond Bounded Termination**  
Beyond bounded termination.  
*Terms:* almost-sure termination  
→ PDF pp. 257–267 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch8"></a>
## 8 Quantitative Analysis of Programs with Probabilities and Concentration of Measure Inequalities

*PDF pp. 275–310*

Quantitative analysis via concentration inequalities.

**Quantitative Analysis: Problem and Approaches**  
The analysis problem and approaches.  
*Terms:* quantitative analysis  
→ PDF pp. 280–283 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Concentration of Measure Inequalities: a Primer**  
Concentration of measure primer.  
*Terms:* Chernoff, Hoeffding  
→ PDF pp. 284–293 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Control Deterministic Computations**  
Control-deterministic programs.  
*Terms:* control-deterministic  
→ PDF pp. 294–302 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Super-martingales and Concentration of Measure**  
Supermartingales and Azuma-type bounds.  
*Terms:* Azuma inequality, martingales  
→ PDF pp. 303–305 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch9"></a>
## 9 The Logical Essentials of Bayesian Reasoning

*PDF pp. 311–348*

A logical and categorical account of Bayesian reasoning.

**Perspectives**  
Perspectives.  
*Terms:* channel-based probability  
→ PDF pp. 313–318 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**States and predicates**  
States and predicates.  
*Terms:* states, predicates, validity  
→ PDF pp. 319–322 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Conditioning**  
Conditioning.  
*Terms:* conditioning  
→ PDF pp. 323–325 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Bayesian inference via state/predicate transformation**  
Inference via state/predicate transformers.  
*Terms:* state transformers, predicate transformers  
→ PDF pp. 326–330 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Inference in Bayesian networks**  
Inference in Bayesian networks.  
*Terms:* Bayesian networks  
→ PDF pp. 331–336 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**String diagrams for Bayesian probability**  
String diagrams.  
*Terms:* string diagrams  
→ PDF pp. 337–338 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**From joint states to Bayesian networks**  
From joint states to networks.  
*Terms:* disintegration  
→ PDF pp. 339–343 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch10"></a>
## 10 Quantitative Equational Reasoning

*PDF pp. 349–376*

Equational logic with distances.

**Equational Logic**  
Classical equational logic.  
*Terms:* equational logic  
→ PDF pp. 351–356 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Quantitative Equational Logic**  
Quantitative equational logic.  
*Terms:* quantitative equational theories, metric spaces  
→ PDF pp. 362–365 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Examples**  
Examples (Kantorovich metric).  
*Terms:* Kantorovich metric, examples  
→ PDF pp. 366–372 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch11"></a>
## 11 Probabilistic Abstract Interpretation: Sound Inference and Application to Privacy

*PDF pp. 377–406*

Abstract interpretation for probabilistic inference and privacy.

**Quantitative Properties**  
Quantitative properties.  
*Terms:* quantitative properties  
→ PDF pp. 378–379 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Distribution Semantics**  
Distribution semantics.  
*Terms:* distribution semantics  
→ PDF pp. 380–385 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Abstraction**  
Abstraction.  
*Terms:* abstraction  
→ PDF pp. 386–388 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Sound Domains with Conditioning**  
Sound domains with conditioning.  
*Terms:* probabilistic polyhedra, conditioning  
→ PDF pp. 389–390 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Abstract Semantics**  
Abstract semantics.  
*Terms:* abstract semantics  
→ PDF pp. 391–396 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Privacy Monitor**  
A privacy monitor.  
*Terms:* privacy, knowledge-based security  
→ PDF pp. 397–398 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch12"></a>
## 12 Quantitative Information Flow with Monads in Haskell

*PDF pp. 407–464*

Quantitative information flow in Haskell.

**QIF and hyper-distributions**  
QIF and hyper-distributions.  
*Terms:* quantitative information flow, hyper-distributions  
→ PDF pp. 418–424 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**A concrete programming language Kuifje, and its semantics**  
The Kuifje language and its semantics.  
*Terms:* Kuifje, monads  
→ PDF pp. 425–434 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Hyper-distributions: from leaked values**  
Hyper-distributions and leakage.  
*Terms:* leakage  
→ PDF pp. 435–440 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Case Studies**  
Case studies.  
*Terms:* case studies  
→ PDF pp. 441–449 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch13"></a>
## 13 Luck: A Probabilistic Language for Testing

*PDF pp. 465–504*

Luck: a language for test-data generators.

**Luck by Example**  
Luck by example.  
*Terms:* Luck  
→ PDF pp. 469–473 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Semantics of Core Luck**  
Core semantics.  
*Terms:* property-based testing, generators  
→ PDF pp. 474–490 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Implementation**  
Implementation.  
*Terms:* implementation  
→ PDF pp. 491–492 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Evaluation**  
Evaluation.  
*Terms:* evaluation  
→ PDF pp. 493–496 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch14"></a>
## 14 Tabular: Probabilistic Inference from the Spreadsheet

*PDF pp. 505–548*

Tabular: Bayesian models in spreadsheets.

**Introduction and Examples**  
Introduction and examples.  
*Terms:* Tabular  
→ PDF pp. 507–513 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Syntax of Tabular**  
Syntax.  
*Terms:* syntax  
→ PDF pp. 514–520 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Reduction to Core Tabular**  
Reduction to Core Tabular.  
*Terms:* core language  
→ PDF pp. 521–529 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Type System**  
Type system.  
*Terms:* type system  
→ PDF pp. 530–544 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)


---

<a id="ch15"></a>
## 15 Programming Unreliable Hardware

*PDF pp. 549–583*

Reasoning about programs on unreliable hardware.

**Example**  
An example.  
*Terms:* approximate computing  
→ PDF pp. 553–561 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Language Semantics**  
Language semantics.  
*Terms:* semantics  
→ PDF pp. 562–566 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Semantics of Quantitative Reliability**  
Quantitative reliability semantics.  
*Terms:* reliability  
→ PDF pp. 567–569 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

**Reliability Analysis**  
Reliability analysis.  
*Terms:* Rely analysis  
→ PDF pp. 570–578 in [the PDF](https://drive.google.com/file/d/1aNogWuvf46m9qNFtlssG5eUKKzxOiqnl/view)

