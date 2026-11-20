<a id="ch1"></a>
# Structured Asynchrony with Algebraic Effects

> Daan Leijen · Microsoft Research technical report MSR-TR-2017-21 (2017) · [the PDF in Drive](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

PDF pages match the report’s pages (1–14). The conclusion and references are not broken out. This is not the POPL 2017 *Type Directed Compilation of Row-Typed Algebraic Effects* paper, which is still missing from Drive. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Shows that async/await needs no compiler support once a language has algebraic effect handlers. After a tour of handlers in Koka (exceptions, resumable operations, state, iterators, multiple resumptions), the report builds an async effect whose handler sits on the Node.js event loop, then adds block-scoped interleaving, cancellation with resource release, timeouts, promises and ambient state that is local to one strand of asynchronous execution. It closes with a small typed calculus and operational semantics for handlers and compares them with delimited continuations. Close in spirit to how Kyo implements Async, Abort and resource safety as handled effects.

**Contents**

1. [1. Introduction](ch1): The argument: effect handlers subsume control features (exceptions, iterators, backtracking, async) that languages usually build in, so async can be a library.
2. [2. Overview](ch2): A quick course in Koka handlers: declaring effects and operations, handlers that resume or abort, state as a handler, iterators, and handlers that resume more than once.
3. [3. Asynchronous Programming](ch3): Async as an effect: an await operation handled on the event loop, then structured features built on it: interleaving with safely encapsulated state, cancellation and resource release, promises, and ambient state.
4. [4. Semantics](ch4): A typed core calculus for handlers: syntax, row-typed effects (as in the Koka MSFP paper), typing rules, an operational semantics, and how handlers relate to delimited continuations (shift/reset).


---

## 1. Introduction

*PDF p. 1*

The argument: effect handlers subsume control features (exceptions, iterators, backtracking, async) that languages usually build in, so async can be a library.

*Terms:* algebraic effect handlers, async-await as a library, control-flow abstractions, Koka

→ PDF p. 1 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)


---

<a id="ch2"></a>
## 2. Overview

*PDF pp. 1–4*

A quick course in Koka handlers: declaring effects and operations, handlers that resume or abort, state as a handler, iterators, and handlers that resume more than once.

**2.1. Exceptions as Algebraic Effects**  
Exceptions as Algebraic Effects  
*Terms:* exceptions, effect declaration, handle, no resumption  
→ PDF p. 2 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**2.2. Resuming Operations**  
Resuming Operations  
*Terms:* resume, continuation, return clause  
→ PDF p. 3 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**2.3. State**  
State  
*Terms:* state handler, get/put, parameterised handler  
→ PDF p. 3 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**2.4. Iterators**  
Iterators  
*Terms:* iterators, yield, generators  
→ PDF p. 4 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**2.5. Multiple Resumptions**  
Multiple Resumptions  
*Terms:* multiple resumptions, nondeterminism, backtracking, multi-shot continuations  
→ PDF p. 4 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)


---

<a id="ch3"></a>
## 3. Asynchronous Programming

*PDF pp. 5–10*

Async as an effect: an await operation handled on the event loop, then structured features built on it: interleaving with safely encapsulated state, cancellation and resource release, promises, and ambient state.

**3.1. An Asynchronous Effect**  
An Asynchronous Effect  
*Terms:* async effect, await operation, callbacks, Node.js event loop  
→ PDF p. 5 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**3.2. Implementing an asynchronous handler**  
Implementing an asynchronous handler  
*Terms:* async handler, CPS, resuming from callbacks  
→ PDF p. 5 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**3.3. Interleaving**  
Interleaving  
*Terms:* interleaving, block-scoped concurrency, safe state encapsulation, handler context sharing  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**3.4. Cancellation**  
Cancellation  
*Terms:* cancellation, cancelable, timeout, releasing resources, finally  
→ PDF pp. 7–9 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**3.5. Promises**  
Promises  
*Terms:* promises, resolve, awaiters  
→ PDF p. 10 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**3.6. Ambient Programming**  
Ambient Programming  
*Terms:* ambient state, strand-local state, implicit context  
→ PDF p. 10 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)


---

<a id="ch4"></a>
## 4. Semantics

*PDF pp. 11–13*

A typed core calculus for handlers: syntax, row-typed effects (as in the Koka MSFP paper), typing rules, an operational semantics, and how handlers relate to delimited continuations (shift/reset).

**4.1. Operational semantics**  
Operational semantics  
*Terms:* operational semantics, handle reduction, evaluation contexts, handled operations, row types  
→ PDF p. 12 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

**4.2. Comparison with Delimited Continuations**  
Comparison with Delimited Continuations  
*Terms:* delimited continuations, shift/reset, control/prompt, expressiveness  
→ PDF pp. 12–13 in [the PDF](https://drive.google.com/file/d/1E6HBgCW-nH0H3gBZPRlfBogy3kJYIHn7/view)

