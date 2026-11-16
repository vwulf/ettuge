<a id="ch1"></a>
# Practical Foundations for Programming Languages (2nd edition, abbreviated)

> Robert Harper · Cambridge University Press, 2016; abbreviated online edition with corrections, from the author’s site · [the PDF in Drive](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

The free online edition keeps all 18 parts but only 17 of the printed book’s chapters; omitted parts appear here as single entries that point to the corresponding chapters in the 2012 pre-publication draft, which is also in your Drive (harper.pdf). The appendices are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Harper’s framework for defining and analyzing programming languages with type theory: every feature is given a statics (typing judgments) and a dynamics (transition rules), and type safety is proved as progress plus preservation. The book builds from abstract binding trees and inductive definitions through total and partial functional languages (System T, PCF), finite and infinite data types, polymorphism (System F) and abstract types, dynamic typing as a special case of static typing, subtyping and dynamic dispatch, control (stacks, exceptions, continuations), symbols, mutable state (Modernized Algol, references), parallelism and cost semantics, concurrency (process calculus, Concurrent Algol), modules, and equational reasoning and parametricity. The abbreviated online edition includes the core chapters of each of these threads.

**Contents**

1. [I Judgments and Rules](ch1): Syntax and judgments as the basis for everything.
2. [II Statics and Dynamics](ch2): How to specify and prove a language safe.
3. [III Total Functions](ch3): Total functions with primitive recursion (Gödel’s T).
4. [IV Finite Data Types](ch4): Products and sums.
5. [V Types and Propositions](ch5): Propositions as types (constructive and classical logic).
6. [VI Infinite Data Types](ch6): Inductive, coinductive and recursive types.
7. [VII Variable Types](ch7): Polymorphism and abstraction.
8. [VIII Partiality and Recursive Types](ch8): General recursion and partiality.
9. [IX Dynamic Types](ch9): Dynamic typing as unityped static typing.
10. [X Subtyping](ch10): Subtyping.
11. [XI Dynamic Dispatch](ch11): Dynamic dispatch and objects.
12. [XII Control Flow](ch12): Control stacks and exceptions.
13. [XIII Symbolic Data](ch13): Symbols, fluid binding and dynamic classification.
14. [XIV Mutable State](ch14): Mutable state.
15. [XV Parallelism](ch15): Parallelism and cost.
16. [XVI Concurrency and Distribution](ch16): Concurrency.
17. [XVII Modularity](ch17): Modules, linking, signatures and type classes.
18. [XVIII Equational Reasoning](ch18): Equational reasoning and parametricity.


---

## I Judgments and Rules

*PDF pp. 17–48*

Syntax and judgments as the basis for everything.

**Abstract Syntax**  
Abstract syntax trees and abstract binding trees, with α-equivalence and substitution.  
*Terms:* abstract binding trees, alpha-equivalence, substitution  
→ PDF pp. 19–28 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

**Inductive Definitions**  
Inductive definitions by rules, rule induction, mutual and simultaneous definitions.  
*Terms:* inductive definitions, rule induction  
→ PDF pp. 29–38 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

**Hypothetical and General Judgments**  
Hypothetical and general judgments, structural properties, derivability vs. admissibility.  
*Terms:* hypothetical judgments, admissibility, derivability  
→ PDF pp. 39–48 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch2"></a>
## II Statics and Dynamics

*PDF pp. 49–71*

How to specify and prove a language safe.

**Statics**  
Typing rules for a simple expression language.  
*Terms:* statics, typing judgment  
→ PDF pp. 51–56 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

**Dynamics**  
Structural (transition) dynamics, contextual dynamics.  
*Terms:* structural dynamics, contextual dynamics  
→ PDF pp. 57–66 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

**Type Safety**  
Type safety via preservation and progress, run-time errors.  
*Terms:* type safety, progress, preservation  
→ PDF pp. 67–71 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch3"></a>
## III Total Functions

*PDF pp. 72–82*

Total functions with primitive recursion (Gödel’s T).

**System T of Higher-Order Recursion**  
System T: recursion over naturals, definability and termination. The draft also has chapters on function definitions and values (PDF pp. 87–94).  
*Terms:* System T, Gödel T, primitive recursion, termination, definability  
→ PDF pp. 75–82 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch4"></a>
## IV Finite Data Types

*PDF pp. 83–98*

Products and sums.

**Product Types**  
Nullary and binary products, tuples.  
*Terms:* product types, unit  
→ PDF pp. 85–90 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

**Sum Types**  
Nullary and binary sums, case analysis, booleans and options.  
*Terms:* sum types, void, case analysis  
→ PDF pp. 91–98 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch5"></a>
## V Types and Propositions

*PDF pp. 99–100*

Propositions as types (constructive and classical logic). Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 305–330.

*Terms:* constructive logic, classical logic, Curry-Howard, propositions as types

→ PDF pp. 99–100 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch6"></a>
## VI Infinite Data Types

*PDF pp. 101–102*

Inductive, coinductive and recursive types. Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 139–164.

*Terms:* inductive types, coinductive types, generic programming, polynomial functors

→ PDF pp. 101–102 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch7"></a>
## VII Variable Types

*PDF pp. 103–114*

Polymorphism and abstraction.

**System F of Polymorphic Types**  
System F: polymorphic types, impredicativity, definability, parametricity sketch. Abstract types and constructors/kinds are in the draft (PDF pp. 209–230).  
*Terms:* System F, polymorphism, impredicativity, parametricity  
→ PDF pp. 105–114 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch8"></a>
## VIII Partiality and Recursive Types

*PDF pp. 115–126*

General recursion and partiality.

**System PCF of Recursive Functions**  
PCF: general recursion, fixed points, definability of partial functions. Recursive types are in the draft (PDF pp. 155–164).  
*Terms:* PCF, general recursion, fixed point, partiality  
→ PDF pp. 117–126 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch9"></a>
## IX Dynamic Types

*PDF pp. 127–128*

Dynamic typing as unityped static typing. Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 165–194.

*Terms:* untyped lambda calculus, dynamic typing, hybrid typing, unitype

→ PDF pp. 127–128 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch10"></a>
## X Subtyping

*PDF pp. 129–131*

Subtyping. Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 231–256.

*Terms:* subtyping, variance, subsumption, singleton kinds

→ PDF pp. 129–131 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch11"></a>
## XI Dynamic Dispatch

*PDF pp. 132–134*

Dynamic dispatch and objects. Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 257–274.

*Terms:* dynamic dispatch, method matrix, inheritance, classes

→ PDF pp. 132–134 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch12"></a>
## XII Control Flow

*PDF pp. 135–150*

Control stacks and exceptions.

**Control Stacks**  
A stack machine (K machine) and its correctness.  
*Terms:* control stack, K machine  
→ PDF pp. 137–144 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

**Exceptions**  
Exceptions: raising and handling, exception values. Continuations are in the draft (PDF pp. 295–304).  
*Terms:* exceptions, handlers  
→ PDF pp. 145–150 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch13"></a>
## XIII Symbolic Data

*PDF pp. 151–152*

Symbols, fluid binding and dynamic classification. Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 331–356.

*Terms:* symbols, fluid binding, dynamic classification, gensym

→ PDF pp. 151–152 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch14"></a>
## XIV Mutable State

*PDF pp. 153–177*

Mutable state.

**Modernized Algol**  
Modernized Algol: commands vs. expressions, assignables, scoping.  
*Terms:* Modernized Algol, assignables, commands  
→ PDF pp. 155–166 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

**Assignable References**  
References as values, scope-free assignables, safety. Laziness and polarization are in the draft (PDF pp. 383–404).  
*Terms:* references, free assignables  
→ PDF pp. 167–177 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch15"></a>
## XV Parallelism

*PDF pp. 178–195*

Parallelism and cost.

**Nested Parallelism**  
Nested parallelism, cost dynamics, work and span, Brent’s theorem. Futures and speculation are in the draft (PDF pp. 421–430).  
*Terms:* parallelism, cost semantics, work, span, Brent theorem  
→ PDF pp. 180–195 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch16"></a>
## XVI Concurrency and Distribution

*PDF pp. 196–208*

Concurrency.

**Concurrent Algol**  
Concurrent Algol: processes, channels and communication in an Algol-style language. The process calculus and Distributed Algol chapters are in the draft (PDF pp. 433–474).  
*Terms:* Concurrent Algol, processes, channels  
→ PDF pp. 198–208 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch17"></a>
## XVII Modularity

*PDF pp. 209–210*

Modules, linking, signatures and type classes. Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 475–512.

*Terms:* modules, linking, signatures, type classes, hierarchy, parameterization

→ PDF pp. 209–210 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)


---

<a id="ch18"></a>
## XVIII Equational Reasoning

*PDF pp. 211–213*

Equational reasoning and parametricity. Omitted from this abbreviated edition; the 2012 draft covers it in [harper.pdf](https://drive.google.com/file/d/1iPLmHYy13bzVoFAgqyKtLzwTzsyDGZw6/view) at PDF pp. 513–564.

*Terms:* equational reasoning, observational equivalence, logical relations, parametricity, process equivalence, bisimulation

→ PDF pp. 211–213 in [the PDF](https://drive.google.com/file/d/1mRhdbups_JDtjYUR4-frV1Bhxr94NuEO/view)

