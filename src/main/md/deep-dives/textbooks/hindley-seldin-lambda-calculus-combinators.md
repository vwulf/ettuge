<a id="ch1"></a>
# Lambda-Calculus and Combinators: An Introduction

> J. Roger Hindley and Jonathan P. Seldin · Cambridge University Press, 2008 · [the PDF in Drive](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

“Further reading” notes, the appendix on care of combinators, and answers to exercises are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The standard introduction to the two classic formalisms of computation by substitution, developed side by side. It defines λ-terms and combinatory logic, β- and weak reduction, fixed points and Böhm’s theorem, shows both represent exactly the recursive functions and that their equality is undecidable, and treats extensionality and the precise correspondence between λ and CL. The second half is on types: Church-style and Curry-style simple typing, subject reduction, principal types, propositions-as-types, and generalized (dependent, pure) type systems; then models: combinatory algebras, λ-models and Scott’s D∞. Appendices prove confluence and strong normalization.

**Contents**

1. [1 The lambda-calculus](ch1): Terms, substitution, β-reduction and β-equality.
2. [2 Combinatory logic](ch2): Combinatory logic: computation without bound variables.
3. [3 The power of lambda and combinators](ch3): Fixed points, Böhm’s theorem and normalizing strategies.
4. [4 Representing the computable functions](ch4): λ and CL compute exactly the partial recursive functions.
5. [5 The undecidability theorem](ch5): Equality of terms is undecidable (Scott–Curry theorem).
6. [6 The formal theories λβ and CLw](ch6): λβ and CLw as formal equational theories.
7. [7 Extensionality in lambda-calculus](ch7): Extensionality in the λ-calculus.
8. [8 Extensionality in combinatory logic](ch8): Extensionality in combinatory logic.
9. [9 Correspondence between lambda and CL](ch9): How closely λ and CL correspond.
10. [10 Simple typing, Church-style](ch10): Simple types attached to terms, Church-style.
11. [11 Simple typing, Curry-style in CL](ch11): Curry-style type assignment for combinatory logic.
12. [12 Simple typing, Curry-style in lambda](ch12): Curry-style type assignment for λ-terms.
13. [13 Generalizations of typing](ch13): Dependent types and pure type systems.
14. [14 Models of CL](ch14): Models of combinatory logic.
15. [15 Models of lambda-calculus](ch15): Models of the λ-calculus.
16. [16 Scott's D∞ and other models](ch16): Scott’s D∞ and other models.
17. [Appendix A1 Bound variables and alpha-conversion](ch17): Careful treatment of bound variables and α-conversion.
18. [Appendix A2 Confluence proofs](ch18): Proofs of confluence.
19. [Appendix A3 Strong normalization proofs](ch19): Proofs of strong normalization.


---

## 1 The lambda-calculus

*PDF pp. 15–34*

Terms, substitution, β-reduction and β-equality.

**1A Introduction**  
Motivation and notation.  
*Terms:* lambda-calculus  
→ PDF pp. 15–18 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**1B Term-structure and substitution**  
Term structure, free and bound variables, substitution.  
*Terms:* terms, free variables, substitution  
→ PDF pp. 19–24 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**1C beta-reduction**  
β-reduction and the Church–Rosser theorem.  
*Terms:* beta-reduction, Church-Rosser, normal form  
→ PDF pp. 25–29 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**1D beta-equality**  
β-equality.  
*Terms:* beta-equality  
→ PDF pp. 30–32 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch2"></a>
## 2 Combinatory logic

*PDF pp. 35–46*

Combinatory logic: computation without bound variables.

**2A Introduction to CL**  
S, K and I.  
*Terms:* combinatory logic, S K I  
→ PDF pp. 35–37 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**2B Weak reduction**  
Weak reduction.  
*Terms:* weak reduction  
→ PDF pp. 38–39 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**2C Abstraction in CL**  
Simulating abstraction with combinators.  
*Terms:* bracket abstraction  
→ PDF pp. 40–42 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**2D Weak equality**  
Weak equality.  
*Terms:* weak equality  
→ PDF pp. 43–45 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch3"></a>
## 3 The power of lambda and combinators

*PDF pp. 47–60*

Fixed points, Böhm’s theorem and normalizing strategies.

**3A Introduction**  
Overview.  
*Terms:* expressive power  
→ PDF p. 47 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**3B The fixed-point theorem**  
Fixed-point combinators such as Y.  
*Terms:* fixed-point combinator, Y combinator  
→ PDF pp. 48–49 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**3C Bohm’s theorem**  
Böhm’s separability theorem.  
*Terms:* Böhm theorem  
→ PDF pp. 50–53 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**3D The quasi-leftmost-reduction theorem**  
Leftmost reduction finds normal forms.  
*Terms:* leftmost reduction, normalization  
→ PDF pp. 54–56 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**3E History and interpretation**  
History and interpretations.  
*Terms:* history  
→ PDF pp. 57–60 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch4"></a>
## 4 Representing the computable functions

*PDF pp. 61–76*

λ and CL compute exactly the partial recursive functions.

**4A Introduction**  
Church numerals.  
*Terms:* Church numerals  
→ PDF pp. 61–63 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**4B Primitive recursive functions**  
Primitive recursive functions.  
*Terms:* primitive recursion  
→ PDF pp. 64–69 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**4C Recursive functions**  
Minimization and recursive functions.  
*Terms:* recursive functions, minimization  
→ PDF pp. 70–74 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**4D Abstract numerals and Z**  
Abstract numerals.  
*Terms:* numerals  
→ PDF pp. 75–76 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch5"></a>
## 5 The undecidability theorem

*PDF pp. 77–82*

Equality of terms is undecidable (Scott–Curry theorem).

*Terms:* undecidability, Scott-Curry theorem, Rice theorem

→ PDF pp. 77–82 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch6"></a>
## 6 The formal theories λβ and CLw

*PDF pp. 83–89*

λβ and CLw as formal equational theories.

**6A The definitions of the theories**  
Definitions of the theories.  
*Terms:* formal theories  
→ PDF pp. 83–85 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**6B First-order theories**  
Comparison with first-order theories.  
*Terms:* first-order theories  
→ PDF p. 86 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**6C Equivalence of theories**  
Equivalence between them.  
*Terms:* equivalence  
→ PDF pp. 87–89 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch7"></a>
## 7 Extensionality in lambda-calculus

*PDF pp. 90–95*

Extensionality in the λ-calculus.

**7A Extensional equality**  
Extensional equality.  
*Terms:* extensionality  
→ PDF pp. 90–92 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**7B lambdaeta-reduction in lambda-calculus**  
η-reduction.  
*Terms:* eta-reduction  
→ PDF pp. 93–95 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch8"></a>
## 8 Extensionality in combinatory logic

*PDF pp. 96–105*

Extensionality in combinatory logic.

**8A Extensional equality**  
Extensional equality in CL.  
*Terms:* extensional equality  
→ PDF pp. 96–98 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**8B Axioms for extensionality in CL**  
Axioms that make CL extensional.  
*Terms:* combinatory axioms  
→ PDF pp. 99–102 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**8C Strong reduction**  
Strong reduction.  
*Terms:* strong reduction  
→ PDF pp. 103–105 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch9"></a>
## 9 Correspondence between lambda and CL

*PDF pp. 106–120*

How closely λ and CL correspond.

**9A Introduction**  
Translations both ways.  
*Terms:* translation  
→ PDF pp. 106–108 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**9B The extensional equalities**  
Matching the extensional theories.  
*Terms:* extensional correspondence  
→ PDF pp. 109–113 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**9C New abstraction algorithms in CL**  
Better abstraction algorithms.  
*Terms:* abstraction algorithms  
→ PDF pp. 114–115 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**9D Combinatory beta-equality**  
Combinatory β-equality.  
*Terms:* combinatory beta-equality  
→ PDF pp. 116–120 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch10"></a>
## 10 Simple typing, Church-style

*PDF pp. 121–132*

Simple types attached to terms, Church-style.

**10A Simple types**  
Simple types.  
*Terms:* simple types  
→ PDF pp. 121–122 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**10B Typed lambda-calculus**  
Typed λ-calculus.  
*Terms:* typed lambda-calculus, Church-style  
→ PDF pp. 123–128 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**10C Typed CL**  
Typed CL.  
*Terms:* typed CL  
→ PDF pp. 129–132 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch11"></a>
## 11 Simple typing, Curry-style in CL

*PDF pp. 133–172*

Curry-style type assignment for combinatory logic.

**11A Introduction**  
Assigning types to untyped terms.  
*Terms:* type assignment  
→ PDF pp. 133–135 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11B The system TA→C**  
The system TA→C.  
*Terms:* TA→C  
→ PDF pp. 136–139 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11C Subject-construction**  
Subject construction.  
*Terms:* subject construction  
→ PDF p. 140 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11D Abstraction**  
Abstraction.  
*Terms:* abstraction  
→ PDF pp. 141–143 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11E Subject-reduction**  
Subject reduction.  
*Terms:* subject reduction  
→ PDF pp. 144–147 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11F Typable CL-terms**  
Which CL-terms are typable.  
*Terms:* typability  
→ PDF pp. 148–150 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11G Link with Church’s approach**  
Relation to Church’s style.  
*Terms:* Church vs Curry  
→ PDF p. 151 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11H Principal types**  
Principal types and the type-inference algorithm.  
*Terms:* principal type, Hindley-Milner  
→ PDF pp. 152–156 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11I Adding new axioms**  
Extra axioms.  
*Terms:* axioms  
→ PDF pp. 157–160 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**11J Propositions-as-types and normalization**  
Propositions-as-types and normalization.  
*Terms:* Curry-Howard, normalization  
→ PDF pp. 161–172 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch12"></a>
## 12 Simple typing, Curry-style in lambda

*PDF pp. 173–193*

Curry-style type assignment for λ-terms.

**12A The system TA→lambda**  
The system TA→λ.  
*Terms:* TA→λ  
→ PDF pp. 173–178 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**12B Basic properties of TA→lambda**  
Basic properties.  
*Terms:* subject reduction  
→ PDF pp. 179–183 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**12C Typable lambda-terms**  
Typable λ-terms.  
*Terms:* typability  
→ PDF pp. 184–186 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**12D Propositions-as-types and normalization**  
Propositions-as-types and normalization.  
*Terms:* Curry-Howard, strong normalization  
→ PDF pp. 187–189 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**12E The equality-rule Eq**  
The equality rule.  
*Terms:* equality rule  
→ PDF pp. 190–191 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch13"></a>
## 13 Generalizations of typing

*PDF pp. 194–233*

Dependent types and pure type systems.

**13A Introduction**  
Overview.  
*Terms:* generalized typing  
→ PDF p. 194 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**13B Dependent function types, introduction**  
Dependent function types.  
*Terms:* dependent types, Pi types  
→ PDF pp. 195–196 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**13C Basic generalized typing, Curry-style in lambda**  
Curry-style generalized typing.  
*Terms:* Curry-style  
→ PDF pp. 197–200 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**13D Deductive rules to define types**  
Rules for defining types.  
*Terms:* type formation rules  
→ PDF pp. 201–204 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**13E Church-style typing in lambda**  
Church-style typing, the λ-cube and PTSs.  
*Terms:* pure type systems, lambda cube  
→ PDF pp. 205–215 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**13F Normalization in PTSs**  
Normalization in PTSs.  
*Terms:* normalization  
→ PDF pp. 216–222 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**13G Propositions-as-types**  
Propositions-as-types in richer systems.  
*Terms:* Curry-Howard  
→ PDF pp. 223–230 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**13H PTSs with equality**  
PTSs with equality.  
*Terms:* equality  
→ PDF pp. 231–233 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch14"></a>
## 14 Models of CL

*PDF pp. 234–242*

Models of combinatory logic.

**14A Applicative structures**  
Applicative structures.  
*Terms:* applicative structure  
→ PDF pp. 234–236 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**14B Combinatory algebras**  
Combinatory algebras.  
*Terms:* combinatory algebra  
→ PDF pp. 237–242 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch15"></a>
## 15 Models of lambda-calculus

*PDF pp. 243–260*

Models of the λ-calculus.

**15A The definition of lambda-model**  
λ-models defined.  
*Terms:* lambda-model  
→ PDF pp. 243–249 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**15B Syntax-free definitions**  
Syntax-free characterizations.  
*Terms:* syntax-free definition  
→ PDF pp. 250–255 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**15C General properties of lambda-models**  
General properties.  
*Terms:* properties  
→ PDF pp. 256–260 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch16"></a>
## 16 Scott's D∞ and other models

*PDF pp. 261–289*

Scott’s D∞ and other models.

**16A Introduction: complete partial orders**  
Complete partial orders.  
*Terms:* cpo, domain theory  
→ PDF pp. 261–265 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**16B Continuous functions**  
Continuous functions.  
*Terms:* Scott continuity  
→ PDF pp. 266–269 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**16C The construction of D∞**  
Building D∞ as an inverse limit.  
*Terms:* D-infinity, inverse limit  
→ PDF pp. 270–280 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**16E D∞ is a lambda-model**  
Proof that D∞ is a λ-model.  
*Terms:* lambda-model  
→ PDF pp. 281–284 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**16F Some other models**  
Other models (Pω, filter models).  
*Terms:* Pω, graph model, filter model  
→ PDF pp. 285–288 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch17"></a>
## Appendix A1 Bound variables and alpha-conversion

*PDF pp. 290–295*

Careful treatment of bound variables and α-conversion.

*Terms:* bound variables, alpha-conversion, variable capture

→ PDF pp. 290–295 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch18"></a>
## Appendix A2 Confluence proofs

*PDF pp. 296–306*

Proofs of confluence.

**A2A Confluence of beta-reduction**  
Confluence of β via parallel reduction.  
*Terms:* confluence, parallel reduction, Tait-Martin-Löf  
→ PDF pp. 296–302 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**A2B Confluence of other reductions**  
Confluence of other reductions.  
*Terms:* other reductions  
→ PDF pp. 303–306 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)


---

<a id="ch19"></a>
## Appendix A3 Strong normalization proofs

*PDF pp. 307–336*

Proofs of strong normalization.

**A3A Simply typed lambda-calculus**  
Simply typed λ (reducibility).  
*Terms:* strong normalization, reducibility, Tait  
→ PDF pp. 308–310 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**A3B Simply typed CL**  
Simply typed CL.  
*Terms:* typed CL  
→ PDF pp. 311–312 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

**A3C Arithmetical system**  
An arithmetical system (Gödel’s T).  
*Terms:* Gödel T  
→ PDF pp. 313–318 in [the PDF](https://drive.google.com/file/d/11oKmzk-KIelEu9bUgNIul3_19Ne6Gbce/view)

