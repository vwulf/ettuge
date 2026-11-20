<a id="ch1"></a>
# Koka: Programming with Row-polymorphic Effect Types

> Daan Leijen · MSFP 2014, EPTCS 153, pp. 100–126 (arXiv:1406.2061) · [the PDF in Drive](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

PDF page N is printed page N+99. References (PDF pp. 22–24) are not broken out. This paper predates Koka’s algebraic effect handlers: effects here are built-in (exn, div, st), and handlers arrive in Leijen’s later papers. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An ML-like language whose function types carry an inferred effect row, so total, partial, divergent and stateful code are told apart by type. The key design choice is row polymorphism with duplicate labels: effect rows are equal up to reordering but ⟨exn, exn⟩ is not ⟨exn⟩, which keeps Hindley–Milner inference principal without lacks constraints or presence flags and gives catch a natural type. The paper gives the type system, a reduction semantics with scoped heaps, and soundness proofs showing the effects mean something: no exn means no uncaught exceptions, no div means termination, and run safely encapsulates local state (like runST) while making the ML value restriction unnecessary.

**Contents**

1. [1. Introduction](ch1): Motivation and contributions: effects should be visible in types and inferred automatically, using row polymorphism with duplicate labels, with a semantic (not merely syntactic) meaning.
2. [2. Overview](ch2): A tour of the language: effect-annotated function types, the basic effects and their aliases, polymorphic effects in higher-order functions, why duplicate labels help, heap effects and their encapsulation, safe state with let-polymorphism, divergence, and experience writing real programs.
3. [3. The type system](ch3): The formal system: kinds for values, effect rows, effect constants and heaps; effect equivalence up to reordering; and the declarative typing rules, including run and catch.
4. [4. Semantics of effects](ch4): Operational semantics with explicit heap binders: values and answers, reduction rules for exceptions, references and run, and evaluation contexts for strict evaluation.
5. [5. Semantic soundness](ch5): Type soundness in the Wright–Felleisen style: subject reduction (with a lemma that state cannot be silently discarded) and the absence of faulty expressions, including escaping references.
6. [6. Effectful semantics](ch6): Theorems giving effects semantic meaning: without exn there are no uncaught exceptions, without st no observable heap, and without div evaluation terminates (via a logical relation).
7. [7. Related work](ch7): Comparison with earlier effect systems, monadic approaches, region inference and Lindley–Cheney’s row-based effects.
8. [Appendix A. Type inference](ch8): The inference algorithm: a syntax-directed system, algorithmic rules, and unification for types and effect rows, sound and complete with respect to the declarative rules.


---

## 1. Introduction

*PDF pp. 1–2*

Motivation and contributions: effects should be visible in types and inferred automatically, using row polymorphism with duplicate labels, with a semantic (not merely syntactic) meaning.

*Terms:* effect types, effect inference, Hindley-Milner, row polymorphism, duplicate labels, contributions

→ PDF pp. 1–2 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)


---

<a id="ch2"></a>
## 2. Overview

*PDF pp. 2–10*

A tour of the language: effect-annotated function types, the basic effects and their aliases, polymorphic effects in higher-order functions, why duplicate labels help, heap effects and their encapsulation, safe state with let-polymorphism, divergence, and experience writing real programs.

**2.1. Effect types**  
Effect types  
*Terms:* function type (τ1..τn) → ε τ, strict semantics, uncurried application  
→ PDF p. 3 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**2.2. Basic effects**  
Basic effects  
*Terms:* total, exn, div, pure, st, io, ndet, effect aliases  
→ PDF pp. 3–4 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**2.3. Polymorphic effects**  
Polymorphic effects  
*Terms:* effect polymorphism, map, open effect rows, μ variables, union types avoided  
→ PDF pp. 4–5 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**2.4. Duplicate effects**  
Duplicate effects  
*Terms:* duplicate labels, ⟨exn, exn⟩, scoped labels, Wand, lacks constraints, presence flags, inject, catch typing  
→ PDF pp. 5–6 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**2.5. Heap effects**  
Heap effects  
*Terms:* ref, heap type variable h, st⟨h⟩, run, runST, local state encapsulation  
→ PDF pp. 6–7 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**2.6. Heap safety**  
Heap safety  
*Terms:* value restriction, let-polymorphism with references, imperative type variables  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**2.7. Divergence**  
Divergence  
*Terms:* div effect, termination checker, Landin’s knot, reading functions from the heap  
→ PDF pp. 7–8 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**2.8. Koka in practice**  
Koka in practice  
*Terms:* Madoko Markdown processor, inferred totality, tier-splitting, client/server effects  
→ PDF pp. 8–10 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)


---

<a id="ch3"></a>
## 3. The type system

*PDF pp. 10–14*

The formal system: kinds for values, effect rows, effect constants and heaps; effect equivalence up to reordering; and the declarative typing rules, including run and catch.

**3.1. Type rules**  
Type rules  
*Terms:* kinds, effect rows, effect equivalence, EQ-SWAP, typing rules, APP, LET, GEN, RUN, CATCH, ALLOC, READ, WRITE, THROW, FIX, principal types  
→ PDF pp. 11–13 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**3.2. Simplifying types**  
Simplifying types  
*Terms:* open effects, closed effects, simplifying inferred types, identity function typing  
→ PDF pp. 13–14 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)


---

<a id="ch4"></a>
## 4. Semantics of effects

*PDF pp. 14–16*

Operational semantics with explicit heap binders: values and answers, reduction rules for exceptions, references and run, and evaluation contexts for strict evaluation.

**4.1. Reductions**  
Reductions  
*Terms:* reduction semantics, heap binding hp φ, MERGE, LIFT, RUN rules, evaluation contexts, answers, strict evaluation  
→ PDF pp. 15–16 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)


---

<a id="ch5"></a>
## 5. Semantic soundness

*PDF pp. 16–19*

Type soundness in the Wright–Felleisen style: subject reduction (with a lemma that state cannot be silently discarded) and the absence of faulty expressions, including escaping references.

**5.1. Subject reduction**  
Subject reduction  
*Terms:* subject reduction, stateful effects lemma, ST-EXTEND, progress  
→ PDF pp. 16–18 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

**5.2. Faulty expressions**  
Faulty expressions  
*Terms:* faulty expressions, escaping references, state errors, type safety  
→ PDF pp. 18–19 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)


---

<a id="ch6"></a>
## 6. Effectful semantics

*PDF pp. 19–20*

Theorems giving effects semantic meaning: without exn there are no uncaught exceptions, without st no observable heap, and without div evaluation terminates (via a logical relation).

*Terms:* effect soundness, exception safety, purity theorem, divergence theorem, termination, logical relation, reducibility

→ PDF pp. 19–20 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)


---

<a id="ch7"></a>
## 7. Related work

*PDF pp. 20–21*

Comparison with earlier effect systems, monadic approaches, region inference and Lindley–Cheney’s row-based effects.

*Terms:* related work, effect systems, Lucassen-Gifford, monads and effects, region inference, Lindley-Cheney, Links, presence/absence flags

→ PDF pp. 20–21 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)


---

<a id="ch8"></a>
## Appendix A. Type inference

*PDF pp. 25–27*

The inference algorithm: a syntax-directed system, algorithmic rules, and unification for types and effect rows, sound and complete with respect to the declarative rules.

*Terms:* type inference algorithm, syntax-directed rules, unification, effect row unification, UNI-EFF, principal types, soundness and completeness

→ PDF pp. 25–27 in [the PDF](https://drive.google.com/file/d/1B-IN0-kxK9n0DewlaGueafUirDe_wMGl/view)

