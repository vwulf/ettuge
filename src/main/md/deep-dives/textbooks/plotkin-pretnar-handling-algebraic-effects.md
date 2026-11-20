<a id="ch1"></a>
# Handling Algebraic Effects

> Gordon D. Plotkin & Matija Pretnar · Logical Methods in Computer Science 9(4:23), 2013 (arXiv:1312.1399) · [the PDF in Drive](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

PDF pages match the printed journal pages (1–36). Conclusion, acknowledgments and references are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The paper that turned exception handlers into a general construct for every algebraic effect. Effects are given by operations plus equations (an effect theory); a computation is an element of the free model of that theory, and a handler supplies another model, so handling is the unique homomorphism out of the free model. The authors build this into a call-by-push-value calculus with value and computation types, show handlers for nondeterminism, CCS, I/O, timeout, rollback and stream redirection, give a denotational semantics, and study when a handler is correct (respects the equations): undecidable in general, with exact complexity bounds for simple signatures. A final section adds recursion over ω-cpos.

**Contents**

1. [Introduction](ch1): Why handlers: exceptions are the one algebraic effect whose standard construct (catching) is not an operation, and the paper sets out to generalise that construct to all effects, with semantics as homomorphisms from free models.
2. [1. Exception Handlers](ch2): Exceptions first: from a simple try/catch to Benton–Kennedy style handling with a success continuation, then the leap to handling arbitrary operations.
3. [2. Syntax](ch3): The calculus: signatures of operations with parameter and arity types, a call-by-push-value split between value and computation types, terms including handlers and the handling construct, typing rules, and derived forms.
4. [3. Examples](ch4): Six worked handlers that show the range of the construct beyond exceptions.
5. [4. Semantics](ch5): Denotational semantics: effect theories (operations plus equations over templates), their interpretation as models, and the meaning of values and computations, with handling as the induced homomorphism.
6. [5. Reasoning about handlers](ch6): A logic for reasoning about handlers, including when a handler is correct: its operation clauses are defined and respect the equations of the effect theory.
7. [6. Deciding handler correctness](ch7): How hard it is to check correctness: for simple signatures, deciding correctness of a single handler is Π2-complete, and Σ1-complete for uniformly simple families of handlers.
8. [7. Recursion](ch8): Adding recursion: models become pointed ω-cpos, free models come from a left adjoint to the forgetful functor, and the standard semantic monads reappear.
9. [Appendix A. Decidability of handler correctness](ch9): The proofs behind the decidability results of Section 6.


---

## Introduction

*PDF pp. 1–2*

Why handlers: exceptions are the one algebraic effect whose standard construct (catching) is not an operation, and the paper sets out to generalise that construct to all effects, with semantics as homomorphisms from free models.

*Terms:* algebraic effects, effect handlers, free model, homomorphism, exception handlers, deconstructor vs operation

→ PDF pp. 1–2 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch2"></a>
## 1. Exception Handlers

*PDF pp. 3–4*

Exceptions first: from a simple try/catch to Benton–Kennedy style handling with a success continuation, then the leap to handling arbitrary operations.

**1.1. Simple handling construct**  
Simple handling construct  
*Terms:* try/catch, raise, exception handler  
→ PDF p. 3 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**1.2. Extended handling construct**  
Extended handling construct  
*Terms:* Benton-Kennedy, handled with ... to x, success continuation  
→ PDF p. 4 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**1.3. Handling arbitrary algebraic effects**  
Handling arbitrary algebraic effects  
*Terms:* operation clauses, continuation k, arbitrary operations, generalisation  
→ PDF p. 5 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch3"></a>
## 2. Syntax

*PDF pp. 5–12*

The calculus: signatures of operations with parameter and arity types, a call-by-push-value split between value and computation types, terms including handlers and the handling construct, typing rules, and derived forms.

**2.1. Signatures**  
Signatures  
*Terms:* signature, operation op : α ⇝ β, parameter type, arity type, base types, function symbols  
→ PDF p. 5 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**2.2. Types**  
Types  
*Terms:* value types, computation types, call-by-push-value, U and F, handler type  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**2.3. Terms**  
Terms  
*Terms:* handler, op_x(k) ↦ M, handled with, generic effects, thunks  
→ PDF pp. 7–8 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**2.4. Typing judgements**  
Typing judgements  
*Terms:* typing judgements, value and computation contexts, well-typed handlers  
→ PDF p. 9 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**2.5. Abbreviations**  
Abbreviations  
*Terms:* syntactic sugar, sequencing, lambda  
→ PDF pp. 10–12 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch4"></a>
## 3. Examples

*PDF pp. 13–17*

Six worked handlers that show the range of the construct beyond exceptions.

**3.1. Explicit Nondeterminism**  
Explicit Nondeterminism  
*Terms:* nondeterminism, choice, collecting all results, list handler  
→ PDF p. 13 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**3.2. CCS**  
CCS  
*Terms:* CCS, process calculus, synchronisation, restriction as handler  
→ PDF p. 14 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**3.3. Interactive input and output (I/O)**  
Interactive input and output (I/O)  
*Terms:* input/output, read, write, interactive I/O, buffering  
→ PDF pp. 14–15 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**3.4. Timeout**  
Timeout  
*Terms:* timeout, clock, interrupting computations  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**3.5. Rollback**  
Rollback  
*Terms:* rollback, state, transactions, restoring state on failure  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**3.6. Stream redirection**  
Stream redirection  
*Terms:* stream redirection, pipes, redirecting output to input  
→ PDF p. 17 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch5"></a>
## 4. Semantics

*PDF pp. 18–25*

Denotational semantics: effect theories (operations plus equations over templates), their interpretation as models, and the meaning of values and computations, with handling as the induced homomorphism.

**4.1. Effect theories**  
Effect theories  
*Terms:* effect theory, equations, templates, Lawvere theory, state equations, nondeterminism equations  
→ PDF pp. 18–20 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**4.2. Interpreting effect theories**  
Interpreting effect theories  
*Terms:* models, free model, monad from theory, interpretation of signature  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

**4.3. Interpreting values and computations**  
Interpreting values and computations  
*Terms:* denotational semantics, handler as model, unique homomorphism, handling semantics, adequacy  
→ PDF pp. 22–25 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch6"></a>
## 5. Reasoning about handlers

*PDF pp. 26–27*

A logic for reasoning about handlers, including when a handler is correct: its operation clauses are defined and respect the equations of the effect theory.

*Terms:* handler correctness, respecting equations, reasoning, equational logic, empty handler, definedness

→ PDF pp. 26–27 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch7"></a>
## 6. Deciding handler correctness

*PDF pp. 28–29*

How hard it is to check correctness: for simple signatures, deciding correctness of a single handler is Π2-complete, and Σ1-complete for uniformly simple families of handlers.

*Terms:* decidability, handler correctness, Π2-complete, Σ1-complete, simple signature, uniformly simple handlers, finite equational theory

→ PDF pp. 28–29 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch8"></a>
## 7. Recursion

*PDF pp. 30–32*

Adding recursion: models become pointed ω-cpos, free models come from a left adjoint to the forgetful functor, and the standard semantic monads reappear.

*Terms:* recursion, ω-cpo, pointed cpo, strict continuous homomorphism, left adjoint, free model functor, locally continuous, exceptions monad

→ PDF pp. 30–32 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)


---

<a id="ch9"></a>
## Appendix A. Decidability of handler correctness

*PDF pp. 33–36*

The proofs behind the decidability results of Section 6.

*Terms:* decidability proof, Π2-completeness, Σ1-completeness, reduction

→ PDF pp. 33–36 in [the PDF](https://drive.google.com/file/d/1VbtjAEiQXtUtykIekL3khhD0OmA_mdMd/view)

