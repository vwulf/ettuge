<a id="ch1"></a>
# Algebraic Effects for Functional Programming

> Daan Leijen · Microsoft Research technical report MSR-TR-2016-29 (December 2016 update); extended version of “Type Directed Compilation of Row-Typed Algebraic Effects”, POPL 2017 · [the PDF in Drive](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

PDF pages match the report’s pages (1–14). The conclusion and references are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An end-to-end account of algebraic effect handlers in a compiled language. Leijen shows in Koka how handlers cover exceptions, state, iterators, backtracking, async and parsers; extends Koka’s row-typed effect inference (with duplicate labels) to user-defined effects and handlers, plus a new way to simplify polymorphic effect types; gives an operational semantics with a soundness proof and an optimisation for tail-resumptive operations; and compiles handlers to JavaScript and the JVM with a type-directed selective CPS translation, so only effectful code pays for continuations. The typed, compiled counterpart to the Plotkin–Pretnar theory, and the closest published design to Kyo’s A < S.

**Contents**

1. [1. Introduction](ch1): Why handlers, and what is new: practical algebraic effects with row-typed inference and an efficient compilation scheme.
2. [2. Overview](ch2): Handlers by example: exceptions, state as resumption, iterators, nondeterminism by resuming more than once, async, and a domain-specific parser effect.
3. [3. Type Rules](ch3): The type system extended to handlers: effect rows with duplicate labels, inference, and simplification of polymorphic effect types (also needed for efficient compilation).
4. [4. Operational Semantics](ch4): Dynamic semantics of handlers, a cheap path for tail-resumptive operations, the relation to delimited continuations, and soundness: well-typed handlers cannot go wrong.
5. [5. Compilation](ch5): Compiling handlers without runtime stack control: a type-directed selective CPS translation that leaves total code direct, coercions between CPS and non-CPS code, polymorphic duplication, and the runtime.
6. [6. Related Work](ch6): How this compares with Eff, Frank, Links, Multicore OCaml, monadic encodings and other handler implementations.


---

## 1. Introduction

*PDF p. 1*

Why handlers, and what is new: practical algebraic effects with row-typed inference and an efficient compilation scheme.

*Terms:* algebraic effect handlers, Koka, contributions, compiled implementation

→ PDF p. 1 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)


---

<a id="ch2"></a>
## 2. Overview

*PDF pp. 1–5*

Handlers by example: exceptions, state as resumption, iterators, nondeterminism by resuming more than once, async, and a domain-specific parser effect.

**2.1. Exceptions as Algebraic Effects**  
Exceptions as Algebraic Effects  
*Terms:* exceptions, raise, handler without resume  
→ PDF p. 2 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**2.2. State: Resuming Operations**  
State: Resuming Operations  
*Terms:* state, get/put, resume, parameterised handler  
→ PDF p. 2 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**2.3. Iterators**  
Iterators  
*Terms:* iterators, yield  
→ PDF p. 3 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**2.4. Ambiguity: Multiple Resumptions**  
Ambiguity: Multiple Resumptions  
*Terms:* ambiguity, flip, multiple resumptions, backtracking  
→ PDF p. 3 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**2.5. Asynchronous Programming**  
Asynchronous Programming  
*Terms:* async, await, callbacks  
→ PDF p. 4 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**2.6. Domain Specific Effects: Parsing**  
Domain Specific Effects: Parsing  
*Terms:* parser effect, many, choice, combinators via handlers  
→ PDF pp. 4–5 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)


---

<a id="ch3"></a>
## 3. Type Rules

*PDF pp. 6–7*

The type system extended to handlers: effect rows with duplicate labels, inference, and simplification of polymorphic effect types (also needed for efficient compilation).

**3.1. Type Inference**  
Type Inference  
*Terms:* type rules, handler typing, row types, duplicate labels, effect inference  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**3.2. Simplifying Types**  
Simplifying Types  
*Terms:* simplifying effect types, open/closed rows, polymorphic effects  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**3.3. Type Inference**  
Type Inference  
*Terms:* inference algorithm, principal types  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)


---

<a id="ch4"></a>
## 4. Operational Semantics

*PDF pp. 7–9*

Dynamic semantics of handlers, a cheap path for tail-resumptive operations, the relation to delimited continuations, and soundness: well-typed handlers cannot go wrong.

**4.1. Optimizing Tail-Resumptions**  
Optimizing Tail-Resumptions  
*Terms:* tail-resumptive operations, optimisation, no continuation capture  
→ PDF p. 8 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**4.2. Comparison with Delimited Continuations**  
Comparison with Delimited Continuations  
*Terms:* delimited continuations, shift/reset, expressiveness  
→ PDF p. 8 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**4.3. Soundness: Well Typed Effect Handlers Cannot Go Wrong**  
Soundness: Well Typed Effect Handlers Cannot Go Wrong  
*Terms:* soundness, subject reduction, progress  
→ PDF p. 9 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**4.4. Faulty Expressions**  
Faulty Expressions  
*Terms:* faulty expressions, unhandled operations  
→ PDF p. 9 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)


---

<a id="ch5"></a>
## 5. Compilation

*PDF pp. 10–12*

Compiling handlers without runtime stack control: a type-directed selective CPS translation that leaves total code direct, coercions between CPS and non-CPS code, polymorphic duplication, and the runtime.

**5.1. A Type-Directed Selective CPS Translation.**  
A Type-Directed Selective CPS Translation.  
*Terms:* selective CPS, type-directed translation, translation rules, JavaScript, JVM  
→ PDF p. 10 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**5.2. Opening: Non-CPS to CPS**  
Opening: Non-CPS to CPS  
*Terms:* opening, lifting direct code into CPS  
→ PDF p. 11 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**5.3. Closing: CPS to Non-CPS**  
Closing: CPS to Non-CPS  
*Terms:* closing, polymorphic duplication, assuming identity  
→ PDF pp. 11–12 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

**5.4. The Runtime System**  
The Runtime System  
*Terms:* runtime system, handler stack, continuations  
→ PDF p. 12 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)


---

<a id="ch6"></a>
## 6. Related Work

*PDF pp. 12–13*

How this compares with Eff, Frank, Links, Multicore OCaml, monadic encodings and other handler implementations.

*Terms:* related work, Eff, Frank, Links, Multicore OCaml, effect libraries, data types à la carte, monads

→ PDF pp. 12–13 in [the PDF](https://drive.google.com/file/d/1_xFD6DeBNmMuHHqDf9H9jkTYWgZPLblW/view)

