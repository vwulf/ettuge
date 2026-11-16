<a id="ch1"></a>
# The Formal Semantics of Programming Languages: An Introduction

> Glynn Winskel · MIT Press (Foundations of Computing), 1993 · [the PDF in Drive](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

PDF page = printed page + 21. “Further reading” sections are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A classic course on giving programming languages precise mathematical meaning. Using a small imperative language (IMP), Winskel presents operational, denotational and axiomatic (Hoare-logic) semantics and proves them consistent, with the induction principles and fixed-point theory needed. He then develops domain theory and applies it to recursion equations, call-by-value and call-by-name, higher-order eager and lazy languages, full abstraction, information systems and recursive types, and closes with nondeterminism and concurrency (guarded commands, CSP-style processes, CCS, the modal μ-calculus and model checking), plus an appendix on undecidability and Gödel incompleteness.

**Contents**

1. [1 Basic set theory](ch1): Logic and set-theory notation used later.
2. [2 Introduction to operational semantics](ch2): Big-step operational semantics for IMP.
3. [3 Some principles of induction](ch3): Induction principles for reasoning about programs.
4. [4 Inductive definitions](ch4): Rules, rule induction and least fixed points.
5. [5 The denotational semantics of IMP](ch5): Denotational semantics of IMP.
6. [6 The axiomatic semantics of IMP](ch6): Hoare logic for IMP.
7. [7 Completeness of the Hoare rules](ch7): Relative completeness of Hoare logic.
8. [8 Introduction to domain theory](ch8): CPOs and constructions on them.
9. [9 Recursion equations](ch9): Recursive function definitions under two evaluation strategies.
10. [10 Techniques for recursion](ch10): Reasoning about recursive definitions.
11. [11 Languages with higher types](ch11): Higher-order languages, eager and lazy.
12. [12 Information systems](ch12): Information systems as a way to solve recursive domain equations.
13. [13 Recursive types](ch13): Languages with recursive types.
14. [14 Nondeterminism and parallelism](ch14): Nondeterminism, communicating processes and modal logic.
15. [A Incompleteness and undecidability](ch15): Computability background.


---

## 1 Basic set theory

*PDF pp. 22–31*

Logic and set-theory notation used later.

**1.1 Logical notation**  
Logical notation.  
*Terms:* logic notation  
→ PDF p. 22 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**1.2 Sets**  
Sets and constructions.  
*Terms:* sets  
→ PDF pp. 23–26 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**1.3 Relations and functions**  
Relations and functions.  
*Terms:* relations, functions  
→ PDF pp. 27–30 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch2"></a>
## 2 Introduction to operational semantics

*PDF pp. 32–47*

Big-step operational semantics for IMP.

**2.1 IMP: a simple imperative language**  
The language IMP.  
*Terms:* IMP  
→ PDF pp. 32–33 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**2.2 The evaluation of arithmetic expressions**  
Evaluating arithmetic expressions.  
*Terms:* arithmetic expressions, evaluation  
→ PDF pp. 34–37 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**2.3 The evaluation of boolean expressions**  
Boolean expressions.  
*Terms:* boolean expressions  
→ PDF pp. 38–39 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**2.4 The execution of commands**  
Executing commands.  
*Terms:* commands, big-step semantics  
→ PDF p. 40 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**2.5 A simple proof**  
A first proof about the semantics.  
*Terms:* proof  
→ PDF pp. 41–44 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**2.6 Alternative semantics**  
Small-step alternatives.  
*Terms:* small-step semantics  
→ PDF pp. 45–46 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch3"></a>
## 3 Some principles of induction

*PDF pp. 48–61*

Induction principles for reasoning about programs.

**3.1 Mathematical induction**  
Mathematical induction.  
*Terms:* mathematical induction  
→ PDF p. 48 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**3.2 Structural induction**  
Structural induction.  
*Terms:* structural induction  
→ PDF pp. 49–51 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**3.3 Well-founded induction**  
Well-founded induction.  
*Terms:* well-founded induction  
→ PDF pp. 52–55 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**3.4 Induction on derivations**  
Induction on derivations.  
*Terms:* induction on derivations  
→ PDF pp. 56–59 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**3.5 Definitions by induction**  
Definitions by induction.  
*Terms:* inductive definitions  
→ PDF p. 60 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch4"></a>
## 4 Inductive definitions

*PDF pp. 62–75*

Rules, rule induction and least fixed points.

**4.1 Rule induction**  
Rule induction.  
*Terms:* rule induction  
→ PDF pp. 62–64 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**4.2 Special rule induction**  
Special rule induction.  
*Terms:* special rule induction  
→ PDF p. 65 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**4.3 Proof rules for operational semantics**  
Proof rules for the semantics.  
*Terms:* operational semantics proofs  
→ PDF pp. 66–72 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**4.4 Operators and their least fixed points**  
Least fixed points of operators.  
*Terms:* least fixed point  
→ PDF pp. 73–74 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch5"></a>
## 5 The denotational semantics of IMP

*PDF pp. 76–97*

Denotational semantics of IMP.

**5.1 Motivation**  
Why denotations.  
*Terms:* motivation  
→ PDF p. 76 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**5.2 Denotational semantics**  
Meaning functions.  
*Terms:* denotational semantics  
→ PDF pp. 77–81 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**5.3 Equivalence of the semantics**  
Equivalence with operational semantics.  
*Terms:* equivalence  
→ PDF pp. 82–88 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**5.4 Complete partial orders and continuous functions**  
CPOs and continuity.  
*Terms:* cpo, continuous functions, Kleene fixed point  
→ PDF pp. 89–94 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**5.5 The Knaster-Tarski Theorem**  
Knaster–Tarski.  
*Terms:* Knaster-Tarski  
→ PDF p. 95 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch6"></a>
## 6 The axiomatic semantics of IMP

*PDF pp. 98–119*

Hoare logic for IMP.

**6.1 The idea**  
The idea of assertions.  
*Terms:* axiomatic semantics  
→ PDF pp. 98–100 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**6.2 The assertion language Assn**  
The assertion language.  
*Terms:* assertion language  
→ PDF pp. 101–104 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**6.3 Semantics of assertions**  
Its semantics.  
*Terms:* assertion semantics  
→ PDF pp. 105–109 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**6.4 Proof rules for partial correctness**  
Proof rules.  
*Terms:* Hoare rules, partial correctness  
→ PDF pp. 110–111 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**6.5 Soundness**  
Soundness.  
*Terms:* soundness  
→ PDF pp. 112–113 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**6.6 Using the Hoare rules: an example**  
A worked example.  
*Terms:* example, loop invariant  
→ PDF pp. 114–116 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch7"></a>
## 7 Completeness of the Hoare rules

*PDF pp. 120–139*

Relative completeness of Hoare logic.

**7.1 G del's Incompleteness Theorem**  
Gödel’s incompleteness.  
*Terms:* incompleteness  
→ PDF p. 120 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**7.2 Weakest preconditions and expressiveness**  
Weakest preconditions and expressiveness.  
*Terms:* weakest precondition, expressiveness  
→ PDF pp. 121–130 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**7.3 Proof of G del's Theorem**  
Proof of Gödel’s theorem.  
*Terms:* Gödel  
→ PDF pp. 131–132 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**7.4 Verification conditions**  
Verification conditions.  
*Terms:* verification conditions  
→ PDF pp. 133–135 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**7.5 Predicate transformers**  
Predicate transformers.  
*Terms:* predicate transformers, Dijkstra  
→ PDF pp. 136–137 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch8"></a>
## 8 Introduction to domain theory

*PDF pp. 140–161*

CPOs and constructions on them.

**8.1 Basic definitions**  
Basic definitions.  
*Terms:* domain theory, cpo  
→ PDF pp. 140–141 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**8.2 Streams: an example**  
Streams example.  
*Terms:* streams  
→ PDF pp. 142–143 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**8.3 Constructions on cpo's**  
Products, functions, lifting, sums.  
*Terms:* constructions, lifting, function space  
→ PDF pp. 144–155 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**8.4 A metalanguage**  
A metalanguage for denotations.  
*Terms:* metalanguage  
→ PDF pp. 156–159 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch9"></a>
## 9 Recursion equations

*PDF pp. 162–183*

Recursive function definitions under two evaluation strategies.

**9.1 The language REC**  
The language REC.  
*Terms:* REC  
→ PDF pp. 162–163 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**9.2 Operational semantics of call-by-value**  
CBV operational.  
*Terms:* call-by-value  
→ PDF p. 164 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**9.3 Denotational semantics of call-by-value**  
CBV denotational.  
*Terms:* denotational  
→ PDF pp. 165–169 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**9.4 Equivalence of semantics for call-by-value**  
Equivalence for CBV.  
*Terms:* equivalence  
→ PDF pp. 170–173 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**9.5 Operational semantics of call-by-name**  
CBN operational.  
*Terms:* call-by-name  
→ PDF p. 174 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**9.6 Denotational semantics of call-by-name**  
CBN denotational.  
*Terms:* denotational  
→ PDF pp. 175–177 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**9.7 Equivalence of semantics for call-by-name**  
Equivalence for CBN.  
*Terms:* equivalence  
→ PDF pp. 178–181 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**9.8 Local declarations**  
Local declarations.  
*Terms:* let  
→ PDF p. 182 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch10"></a>
## 10 Techniques for recursion

*PDF pp. 184–203*

Reasoning about recursive definitions.

**10.1 Bekic's Theorem**  
Bekič’s theorem.  
*Terms:* Bekič theorem  
→ PDF pp. 184–186 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**10.2 Fixed-point induction**  
Fixed-point (Scott) induction.  
*Terms:* fixed-point induction  
→ PDF pp. 187–194 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**10.3 Well-founded induction**  
Well-founded induction.  
*Terms:* well-founded induction  
→ PDF pp. 195–196 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**10.4 Well-founded recursion**  
Well-founded recursion.  
*Terms:* well-founded recursion  
→ PDF pp. 197–199 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**10.5 An exercise**  
Exercise.  
*Terms:* exercise  
→ PDF pp. 200–201 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch11"></a>
## 11 Languages with higher types

*PDF pp. 204–243*

Higher-order languages, eager and lazy.

**11.1 An eager language**  
An eager language.  
*Terms:* eager language  
→ PDF pp. 204–206 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.2 Eager operational semantics**  
Eager operational semantics.  
*Terms:* operational  
→ PDF pp. 207–208 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.3 Eager denotational semantics**  
Eager denotational semantics.  
*Terms:* denotational  
→ PDF pp. 209–210 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.4 Agreement of eager semantics**  
Their agreement.  
*Terms:* adequacy  
→ PDF pp. 211–220 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.5 A lazy language**  
A lazy language.  
*Terms:* lazy language  
→ PDF p. 221 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.6 Lazy operational semantics**  
Lazy operational semantics.  
*Terms:* operational  
→ PDF pp. 222–223 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.7 Lazy denotational semantics**  
Lazy denotational semantics.  
*Terms:* denotational  
→ PDF p. 224 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.8 Agreement of lazy semantics**  
Their agreement.  
*Terms:* adequacy  
→ PDF pp. 225–229 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.9 Fixed-point operators**  
Fixed-point operators.  
*Terms:* fixed-point operators  
→ PDF pp. 230–235 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.10 Observations and full abstraction**  
Full abstraction.  
*Terms:* full abstraction, observational equivalence  
→ PDF pp. 236–239 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**11.11 Sums**  
Sum types.  
*Terms:* sums  
→ PDF pp. 240–241 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch12"></a>
## 12 Information systems

*PDF pp. 244–271*

Information systems as a way to solve recursive domain equations.

**12.1 Recursive types**  
Recursive types motivation.  
*Terms:* recursive types  
→ PDF pp. 244–245 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**12.2 Information systems**  
Information systems.  
*Terms:* information systems  
→ PDF pp. 246–248 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**12.3 Closed families and Scott predomains**  
Closed families and Scott predomains.  
*Terms:* Scott predomains  
→ PDF pp. 249–253 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**12.4 A cpo of information systems**  
A cpo of information systems.  
*Terms:* cpo of information systems  
→ PDF pp. 254–256 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**12.5 Constructions**  
Constructions.  
*Terms:* constructions  
→ PDF pp. 257–269 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch13"></a>
## 13 Recursive types

*PDF pp. 272–317*

Languages with recursive types.

**13.1 An eager language**  
Eager language.  
*Terms:* recursive types  
→ PDF pp. 272–275 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.2 Eager operational semantics**  
Operational semantics.  
*Terms:* operational  
→ PDF pp. 276–277 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.3 Eager denotational semantics**  
Denotational semantics.  
*Terms:* denotational  
→ PDF pp. 278–282 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.4 Adequacy of eager semantics**  
Adequacy.  
*Terms:* adequacy  
→ PDF pp. 283–287 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.5 The eager λ-calculus**  
Eager λ-calculus.  
*Terms:* eager lambda calculus  
→ PDF pp. 288–298 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.6 A lazy language**  
Lazy language.  
*Terms:* lazy language  
→ PDF p. 299 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.7 Lazy operational semantics**  
Operational.  
*Terms:* operational  
→ PDF pp. 299–301 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.8 Lazy denotational semantics**  
Denotational.  
*Terms:* denotational  
→ PDF pp. 302–308 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.9 Adequacy of lazy semantics**  
Adequacy.  
*Terms:* adequacy  
→ PDF pp. 309–310 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**13.10 The lazy λ-calculus**  
Lazy λ-calculus.  
*Terms:* lazy lambda calculus  
→ PDF pp. 311–315 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch14"></a>
## 14 Nondeterminism and parallelism

*PDF pp. 318–357*

Nondeterminism, communicating processes and modal logic.

**14.1 Introduction**  
Overview.  
*Terms:* nondeterminism  
→ PDF p. 318 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**14.2 Guarded commands**  
Dijkstra’s guarded commands.  
*Terms:* guarded commands  
→ PDF pp. 319–323 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**14.3 Communicating processes**  
Communicating processes.  
*Terms:* communicating processes, CSP  
→ PDF pp. 324–328 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**14.4 Milner's CCS**  
Milner’s CCS.  
*Terms:* CCS  
→ PDF pp. 329–331 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**14.5 Pure CCS**  
Pure CCS.  
*Terms:* pure CCS, bisimulation  
→ PDF pp. 332–336 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**14.6 A specification language**  
A specification language.  
*Terms:* specification  
→ PDF pp. 337–341 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**14.7 The modal ν-calculus**  
The modal ν-calculus.  
*Terms:* modal mu-calculus  
→ PDF pp. 342–347 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**14.8 Local model checking**  
Local model checking.  
*Terms:* model checking  
→ PDF pp. 348–355 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)


---

<a id="ch15"></a>
## A Incompleteness and undecidability

*PDF pp. 358–373*

Computability background.

**A.1 Computability**  
Computability.  
*Terms:* computability  
→ PDF pp. 358–359 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**A.2 Undecidability**  
Undecidability.  
*Terms:* undecidability, halting  
→ PDF pp. 360–363 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**A.3 G del's incompleteness theorem**  
Gödel incompleteness.  
*Terms:* Gödel incompleteness  
→ PDF pp. 364–365 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**A.4 A universal program**  
A universal program.  
*Terms:* universal program  
→ PDF pp. 366–367 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

**A.5 Matiyasevich's Theorem**  
Matiyasevich’s theorem.  
*Terms:* Matiyasevich, Hilbert tenth problem  
→ PDF pp. 368–371 in [the PDF](https://drive.google.com/file/d/12WkGhXZLcw9l6yMqqHBRpUBQ5R1cwxUk/view)

