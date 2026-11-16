<a id="ch1"></a>
# Type Theory and Functional Programming

> Simon Thompson · Addison-Wesley, 1991; author’s free edition, 1999 · [the PDF in Drive](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

PDF page = printed page + 13. Bibliography and rule tables are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An introduction to Martin-Löf’s constructive type theory as both a logic and a programming language. After background on logic, the λ-calculus and constructive mathematics, Thompson presents the theory through the Curry–Howard correspondence: propositions as types and proofs as programs, with rules for connectives, quantifiers, natural numbers, trees and equality. He then explores its metatheory (normalization, equality, universes, well-founded types), applies it to program development and verification (quicksort, vectors, the Polish flag, program transformation), and surveys extensions such as subset and quotient types, inductive and coinductive types and partial objects, ending with foundations and related work.

**Contents**

1. [Introduction](ch1): Why combine logic and programming: correctness and constructive reasoning.
2. [Introduction to Logic](ch2): Natural deduction for propositional and predicate logic.
3. [Functional Programming and λ-Calculi](ch3): Functional programming and the λ-calculus, typed and untyped.
4. [Constructive Mathematics](ch4): Constructive mathematics and the BHK interpretation.
5. [Introduction to Type Theory](ch5): The core of Martin-Löf type theory.
6. [Exploring Type Theory](ch6): Metatheory and refinements of the theory.
7. [Applying Type Theory](ch7): Using type theory to write and verify programs.
8. [Augmenting Type Theory](ch8): Extensions to the basic theory.
9. [Foundations](ch9): Proof-theoretic and model-theoretic foundations.
10. [Conclusions](ch10): Related systems and closing thoughts.


---

## Introduction

*PDF pp. 14–19*

Why combine logic and programming: correctness and constructive reasoning.

*Terms:* program correctness, constructive logic, propositions as types, Martin-Löf type theory

→ PDF pp. 14–19 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch2"></a>
## Introduction to Logic

*PDF pp. 20–41*

Natural deduction for propositional and predicate logic.

**Propositional Logic**  
Natural deduction rules for connectives.  
*Terms:* natural deduction, propositional logic  
→ PDF pp. 21–28 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Predicate Logic**  
Quantifiers, variables and substitution.  
*Terms:* predicate logic, quantifiers, substitution  
→ PDF pp. 29–41 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch3"></a>
## Functional Programming and λ-Calculi

*PDF pp. 42–71*

Functional programming and the λ-calculus, typed and untyped.

**Functional Programming**  
Functional programming ideas.  
*Terms:* functional programming  
→ PDF pp. 43–44 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**The untyped λ-calculus**  
Untyped λ-calculus.  
*Terms:* untyped lambda calculus  
→ PDF pp. 45–48 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Evaluation**  
Reduction and evaluation.  
*Terms:* reduction, evaluation  
→ PDF pp. 49–52 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Convertibility**  
Convertibility.  
*Terms:* convertibility  
→ PDF p. 53 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Expressiveness**  
Expressiveness.  
*Terms:* expressiveness  
→ PDF p. 54 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Typed λ-calculus**  
Simply typed λ-calculus.  
*Terms:* typed lambda calculus  
→ PDF pp. 55–57 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Strong normalisation**  
Strong normalization.  
*Terms:* strong normalization  
→ PDF pp. 58–62 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Further type constructors: the product**  
Product types.  
*Terms:* product type  
→ PDF pp. 63–65 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Base Types: Natural Numbers**  
Natural numbers.  
*Terms:* natural numbers  
→ PDF pp. 66–67 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**General Recursion**  
General recursion.  
*Terms:* general recursion  
→ PDF p. 68 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Evaluation revisited**  
Evaluation strategies.  
*Terms:* lazy, strict evaluation  
→ PDF pp. 69–71 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch4"></a>
## Constructive Mathematics

*PDF pp. 72–79*

Constructive mathematics and the BHK interpretation.

*Terms:* constructive mathematics, intuitionism, BHK interpretation, Bishop

→ PDF pp. 72–79 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch5"></a>
## Introduction to Type Theory

*PDF pp. 80–137*

The core of Martin-Löf type theory.

**Propositional Logic: an Informal View**  
Propositional logic informally.  
*Terms:* informal logic  
→ PDF pp. 82–83 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Judgements, Proofs and Derivations**  
Judgements and derivations.  
*Terms:* judgements, derivations  
→ PDF pp. 84–85 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**The Rules for Propositional Calculus**  
Rules for the propositional connectives.  
*Terms:* introduction, elimination rules  
→ PDF pp. 86–90 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**The Curry Howard Isomorphism**  
The Curry–Howard isomorphism.  
*Terms:* Curry-Howard isomorphism  
→ PDF pp. 91–95 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Some examples**  
Worked examples.  
*Terms:* examples  
→ PDF pp. 96–100 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Quantifiers**  
Π and Σ for quantifiers.  
*Terms:* dependent types, Pi, Sigma  
→ PDF pp. 101–108 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Base Types**  
Base types.  
*Terms:* base types  
→ PDF pp. 109–112 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**The natural numbers**  
Natural numbers and primitive recursion.  
*Terms:* natural numbers, recursion  
→ PDF pp. 113–117 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Well-founded types — trees**  
Well-founded trees.  
*Terms:* W-types, trees  
→ PDF pp. 118–121 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Equality**  
The identity type I.  
*Terms:* identity type, equality  
→ PDF pp. 122–129 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Convertibility**  
Convertibility.  
*Terms:* convertibility  
→ PDF pp. 130–137 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch6"></a>
## Exploring Type Theory

*PDF pp. 138–207*

Metatheory and refinements of the theory.

**Assumptions**  
Handling assumptions.  
*Terms:* assumptions  
→ PDF pp. 139–142 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Naming and abbreviations**  
Definitions and abbreviations.  
*Terms:* definitions  
→ PDF pp. 143–145 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Revising the rules**  
Revised rules.  
*Terms:* rules  
→ PDF pp. 146–151 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Derivability**  
Derivability.  
*Terms:* derivability  
→ PDF pp. 152–156 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Computation**  
Computation and normal forms.  
*Terms:* computation  
→ PDF pp. 157–165 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**TT0c: Normalisation and its corollaries**  
Normalization and consequences.  
*Terms:* normalization  
→ PDF pp. 166–175 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Equalities and Identities**  
Equalities and identities.  
*Terms:* equality, identity  
→ PDF pp. 176–180 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Different Equalities**  
Kinds of equality (definitional, propositional, extensional).  
*Terms:* intensional, extensional equality  
→ PDF pp. 181–186 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Universes**  
Universes.  
*Terms:* universes  
→ PDF pp. 187–191 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Well-founded types**  
General well-founded types.  
*Terms:* W-types  
→ PDF pp. 192–201 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Expressibility**  
Expressibility.  
*Terms:* expressibility  
→ PDF pp. 202–203 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**The Curry Howard Isomorphism?**  
Limits of Curry–Howard.  
*Terms:* Curry-Howard  
→ PDF pp. 204–207 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch7"></a>
## Applying Type Theory

*PDF pp. 208–265*

Using type theory to write and verify programs.

**Recursion**  
Recursion forms.  
*Terms:* recursion  
→ PDF pp. 209–219 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**A Case Study – Quicksort**  
Quicksort derived with its proof.  
*Terms:* quicksort  
→ PDF pp. 220–226 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Dependent types and quantifiers**  
Dependent types and quantifiers in programs.  
*Terms:* dependent types  
→ PDF pp. 227–238 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**A Case Study – Vectors**  
Length-indexed vectors.  
*Terms:* vectors  
→ PDF pp. 239–242 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Proof Extraction; Top-Down Proof**  
Extracting programs from proofs.  
*Terms:* proof extraction  
→ PDF pp. 243–246 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Program Development – Polish National Flag**  
The Polish national flag problem.  
*Terms:* Polish flag, program development  
→ PDF pp. 247–250 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Program Transformation**  
Program transformation.  
*Terms:* program transformation  
→ PDF pp. 251–259 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Imperative Programming**  
Imperative programs.  
*Terms:* imperative programming  
→ PDF pp. 260–261 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Examples in the literature**  
Examples from the literature.  
*Terms:* literature  
→ PDF pp. 262–265 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch8"></a>
## Augmenting Type Theory

*PDF pp. 266–327*

Extensions to the basic theory.

**Background**  
Background on extensions.  
*Terms:* extensions  
→ PDF pp. 268–273 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**The subset type**  
Subset types.  
*Terms:* subset type  
→ PDF pp. 274–277 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Propositions not types**  
Separating propositions from types.  
*Terms:* propositions vs types  
→ PDF pp. 278–280 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Are subsets necessary?**  
Whether subsets are needed.  
*Terms:* subsets  
→ PDF pp. 281–285 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Quotient or Congruence Types**  
Quotient types.  
*Terms:* quotient types, setoids  
→ PDF pp. 286–290 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Case Study – The Real Numbers**  
Constructive reals.  
*Terms:* real numbers  
→ PDF pp. 291–293 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Strengthened rules; polymorphism**  
Polymorphism and strengthened rules.  
*Terms:* polymorphism  
→ PDF pp. 294–298 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Well-founded recursion**  
Well-founded recursion.  
*Terms:* well-founded recursion  
→ PDF pp. 299–304 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Well-founded recursion in type theory**  
Well-founded recursion inside type theory.  
*Terms:* accessibility  
→ PDF pp. 305–310 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Inductive types**  
Inductive types.  
*Terms:* inductive types  
→ PDF pp. 311–315 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Co-inductions**  
Coinductive types.  
*Terms:* coinduction, streams  
→ PDF pp. 316–321 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Partial Objects and Types**  
Partial objects.  
*Terms:* partial functions  
→ PDF p. 322 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Modelling**  
Modelling.  
*Terms:* models  
→ PDF pp. 323–327 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch9"></a>
## Foundations

*PDF pp. 328–343*

Proof-theoretic and model-theoretic foundations.

**Proof Theory**  
Proof theory: normalization and consistency.  
*Terms:* proof theory  
→ PDF pp. 328–333 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**Model Theory**  
Model theory.  
*Terms:* model theory  
→ PDF pp. 334–336 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**A General Framework for Logics**  
Logical frameworks.  
*Terms:* logical framework  
→ PDF pp. 337–338 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

**The Inversion Principle**  
The inversion principle.  
*Terms:* inversion principle  
→ PDF pp. 339–343 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)


---

<a id="ch10"></a>
## Conclusions

*PDF pp. 344–351*

Related systems and closing thoughts.

**Related Work**  
Comparison with Nuprl, Coq, LF and other systems.  
*Terms:* Nuprl, Coq, ALF, related work  
→ PDF pp. 344–349 in [the PDF](https://drive.google.com/file/d/11zXscPa64bEsame74QbWo_pIIPpmeyjL/view)

