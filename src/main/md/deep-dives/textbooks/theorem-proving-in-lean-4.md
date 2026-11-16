<a id="ch1"></a>
# Theorem Proving in Lean 4

> Jeremy Avigad, Leonardo de Moura, Soonho Kong and Sebastian Ullrich · Lean 4 edition · [the PDF in Drive](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)

This PDF is a browser print of the online book, so it has no table of contents or printed page numbers; chapter ranges here are PDF pages. Sections are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The standard introduction to proving theorems in Lean 4. It teaches the dependent type theory underneath Lean (the Calculus of Inductive Constructions with universes) and uses propositions-as-types throughout: a proof is a term, logical connectives and quantifiers are types, and equality is an inductive family. With that foundation it covers term-mode proofs, tactic proofs, the practicalities of working in Lean, inductive types and recursion (structural and well-founded), structures, type classes, conv mode, and the axioms (propositional and function extensionality, quotients, choice) together with their computational cost.

**Contents**

1. [1. Introduction](ch1): Computers in proof: automated versus interactive theorem proving, and Lean’s place among them.
2. [2. Dependent Type Theory](ch2): Lean’s type theory from simple types to dependent types: definitions, variables, sections, namespaces and implicit arguments.
3. [3. Propositions and Proofs](ch3): Propositions as types: proofs as terms, the logical connectives, and classical reasoning as an extra axiom.
4. [4. Quantifiers and Equality](ch4): The universal and existential quantifiers, equality, rewriting and calculational proofs.
5. [5. Tactics](ch5): Building proofs interactively with tactics: intro, apply, exact, rw, simp, cases, induction, and combinators.
6. [6. Interacting with Lean](ch6): Practical Lean: imports, sections, namespaces, attributes, notation, coercions and settings.
7. [7. Inductive Types](ch7): Defining inductive types (enumerations, structures, recursive and indexed families) and their eliminators.
8. [8. Induction and Recursion](ch8): Pattern matching, structural and well-founded recursion, mutual and nested recursion, and dependent pattern matching.
9. [9. Structures and Records](ch9): Structures as single-constructor inductive types, with projections, inheritance and anonymous constructor notation.
10. [10. Type Classes](ch10): Type classes for overloading and canonical structures: instances, defaults, outParams, coercions and instance resolution.
11. [11. The Conversion Tactic Mode](ch11): The conv mode for rewriting inside specific subterms of a goal.
12. [12. Axioms and Computation](ch12): Propositional extensionality, function extensionality, quotients and choice, and what they do to computation.


---

## 1. Introduction

*PDF pp. 1–3*

Computers in proof: automated versus interactive theorem proving, and Lean’s place among them.

*Terms:* interactive theorem proving, automated theorem proving, Lean 4

→ PDF pp. 1–3 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch2"></a>
## 2. Dependent Type Theory

*PDF pp. 4–22*

Lean’s type theory from simple types to dependent types: definitions, variables, sections, namespaces and implicit arguments.

*Terms:* dependent type theory, simple type theory, universes, definitions, namespaces, implicit arguments, #check, #eval

→ PDF pp. 4–22 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch3"></a>
## 3. Propositions and Proofs

*PDF pp. 23–40*

Propositions as types: proofs as terms, the logical connectives, and classical reasoning as an extra axiom.

*Terms:* propositions as types, Curry-Howard, conjunction, disjunction, negation, classical logic, Classical.em

→ PDF pp. 23–40 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch4"></a>
## 4. Quantifiers and Equality

*PDF pp. 41–58*

The universal and existential quantifiers, equality, rewriting and calculational proofs.

*Terms:* universal quantifier, existential quantifier, equality, Eq.subst, rewriting, calc

→ PDF pp. 41–58 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch5"></a>
## 5. Tactics

*PDF pp. 59–86*

Building proofs interactively with tactics: intro, apply, exact, rw, simp, cases, induction, and combinators.

*Terms:* tactics, intro, apply, exact, rw, simp, cases, induction, tactic combinators

→ PDF pp. 59–86 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch6"></a>
## 6. Interacting with Lean

*PDF pp. 87–106*

Practical Lean: imports, sections, namespaces, attributes, notation, coercions and settings.

*Terms:* imports, sections, attributes, notation, coercions, set_option

→ PDF pp. 87–106 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch7"></a>
## 7. Inductive Types

*PDF pp. 107–134*

Defining inductive types (enumerations, structures, recursive and indexed families) and their eliminators.

*Terms:* inductive types, constructors, recursors, enumerated types, indexed families

→ PDF pp. 107–134 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch8"></a>
## 8. Induction and Recursion

*PDF pp. 135–164*

Pattern matching, structural and well-founded recursion, mutual and nested recursion, and dependent pattern matching.

*Terms:* pattern matching, structural recursion, well-founded recursion, mutual recursion, dependent pattern matching

→ PDF pp. 135–164 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch9"></a>
## 9. Structures and Records

*PDF pp. 165–170*

Structures as single-constructor inductive types, with projections, inheritance and anonymous constructor notation.

*Terms:* structures, projections, inheritance, anonymous constructor

→ PDF pp. 165–170 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch10"></a>
## 10. Type Classes

*PDF pp. 171–189*

Type classes for overloading and canonical structures: instances, defaults, outParams, coercions and instance resolution.

*Terms:* type classes, instances, instance resolution, outParam, default instances, coercions

→ PDF pp. 171–189 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch11"></a>
## 11. The Conversion Tactic Mode

*PDF pp. 190–194*

The conv mode for rewriting inside specific subterms of a goal.

*Terms:* conv mode, rewriting subterms

→ PDF pp. 190–194 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)


---

<a id="ch12"></a>
## 12. Axioms and Computation

*PDF pp. 195–211*

Propositional extensionality, function extensionality, quotients and choice, and what they do to computation.

*Terms:* propext, funext, quotients, Quot, axiom of choice, Classical.choice, noncomputable

→ PDF pp. 195–211 in [the PDF](https://drive.google.com/file/d/10fv1H-P3lHBOn8_d1XdfErqupQxiCDAi/view)

