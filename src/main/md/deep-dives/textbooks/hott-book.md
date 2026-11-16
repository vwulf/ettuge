<a id="ch1"></a>
# Homotopy Type Theory: Univalent Foundations of Mathematics

> The Univalent Foundations Program, Institute for Advanced Study · 2013 (online build 1270-g3f17b85), CC BY-SA · [the PDF in Drive](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

The book is maintained on GitHub with nightly builds; content has been stable since 2013 apart from corrections. Exercises and chapter notes are not broken out. There is no official HTML edition. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The collaborative “HoTT book” that set out univalent foundations: Martin-Löf dependent type theory read homotopically, where types are spaces (∞-groupoids), identity proofs are paths, and the univalence axiom makes equivalent types equal. Part I develops the foundations: basic type theory, the homotopical reading of identity types and function extensionality, sets and mere propositions with propositional truncation, the theory of equivalences, inductive types as initial algebras, higher inductive types (circles, spheres, pushouts, truncations, quotients) and homotopy n-types with connectedness and modalities. Part II applies this to mathematics: synthetic homotopy theory (π₁(S¹), Freudenthal, Hopf fibration, van Kampen), univalent category theory and the Rezk completion, set theory with cardinals and ordinals, and constructive real numbers (Dedekind and Cauchy reals) plus surreal numbers. An appendix gives formal presentations of the theory.

**Contents**

1. [Introduction](ch1): Why univalent foundations, and an overview.
2. [1 Type theory](ch2): Informal dependent type theory.
3. [2 Homotopy type theory](ch3): The homotopical reading of type theory.
4. [3 Sets and logic](ch4): Sets, mere propositions and logic.
5. [4 Equivalences](ch5): Coherent notions of equivalence.
6. [5 Induction](ch6): Inductive types.
7. [6 Higher inductive types](ch7): Higher inductive types.
8. [7 Homotopy n-types](ch8): Truncation levels and connectedness.
9. [8 Homotopy theory](ch9): Synthetic homotopy theory.
10. [9 Category theory](ch10): Univalent category theory.
11. [10 Set theory](ch11): Set theory in univalent foundations.
12. [11 Real numbers](ch12): Constructive analysis.
13. [A Formal type theory](ch13): Formal presentations of the type theory.


---

## Introduction

*PDF pp. 13–28*

Why univalent foundations, and an overview.

*Terms:* univalent foundations, homotopy type theory, univalence axiom, Voevodsky, overview

→ PDF pp. 13–28 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch2"></a>
## 1 Type theory

*PDF pp. 29–70*

Informal dependent type theory.

**1.1 Type theory versus set theory**  
Types vs. sets as foundations.  
*Terms:* type theory vs set theory  
→ PDF pp. 29–32 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.2 Function types**  
Function types.  
*Terms:* function types  
→ PDF pp. 33–35 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.3 Universes and families**  
Universes and type families.  
*Terms:* universes, type families  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.4 Dependent function types (Π-types)**  
Π-types.  
*Terms:* dependent functions, Pi  
→ PDF p. 37 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.5 Product types**  
Product types.  
*Terms:* products  
→ PDF pp. 38–41 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.6 Dependent pair types (Σ-types)**  
Σ-types.  
*Terms:* Sigma types, dependent pairs  
→ PDF pp. 42–44 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.7 Coproduct types**  
Coproducts.  
*Terms:* coproduct  
→ PDF p. 45 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.8 The type of booleans**  
Booleans.  
*Terms:* booleans  
→ PDF pp. 46–47 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.9 The natural numbers**  
Natural numbers.  
*Terms:* natural numbers, induction  
→ PDF pp. 48–50 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.10 Pattern matching and recursion**  
Pattern matching and recursion.  
*Terms:* recursion principles  
→ PDF pp. 51–52 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.11 Propositions as types**  
Propositions as types.  
*Terms:* Curry-Howard  
→ PDF pp. 53–58 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**1.12 Identity types**  
Identity types.  
*Terms:* identity types, path induction  
→ PDF pp. 59–65 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch3"></a>
## 2 Homotopy type theory

*PDF pp. 71–118*

The homotopical reading of type theory.

**2.1 Types are higher groupoids**  
Types as higher groupoids.  
*Terms:* higher groupoids, paths  
→ PDF pp. 74–82 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.2 Functions are functors**  
Functions act on paths.  
*Terms:* ap, functoriality  
→ PDF p. 83 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.3 Type families are fibrations**  
Families as fibrations, transport.  
*Terms:* transport, fibrations  
→ PDF pp. 83–86 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.4 Homotopies and equivalences**  
Homotopies and equivalences.  
*Terms:* homotopy, equivalence  
→ PDF pp. 87–90 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.5 The higher groupoid structure of type formers**  
Paths in type formers.  
*Terms:* characterizing path spaces  
→ PDF p. 91 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.6 Cartesian product types**  
Products.  
*Terms:* products  
→ PDF pp. 92–94 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.7 Σ-types**  
Σ-types.  
*Terms:* Sigma  
→ PDF pp. 95–96 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.8 The unit type**  
Unit.  
*Terms:* unit  
→ PDF p. 97 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.9 Π-types and the function extensionality axiom**  
Π-types and function extensionality.  
*Terms:* function extensionality  
→ PDF pp. 98–100 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.10 Universes and the univalence axiom**  
Universes and univalence.  
*Terms:* univalence axiom  
→ PDF p. 101 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.11 Identity type**  
Identity types.  
*Terms:* identity type  
→ PDF pp. 102–103 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.12 Coproducts**  
Coproducts.  
*Terms:* coproducts  
→ PDF pp. 104–106 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.13 Natural numbers**  
Natural numbers.  
*Terms:* natural numbers  
→ PDF pp. 107–108 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.14 Example: equality of structures**  
Example: equality of structures.  
*Terms:* structure identity  
→ PDF pp. 109–111 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**2.15 Universal properties**  
Universal properties.  
*Terms:* universal properties  
→ PDF pp. 112–113 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch4"></a>
## 3 Sets and logic

*PDF pp. 119–140*

Sets, mere propositions and logic.

**3.1 Sets and n-types**  
Sets and n-types.  
*Terms:* sets, h-levels  
→ PDF pp. 119–120 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.2 Propositions as types?**  
Why not all types are propositions.  
*Terms:* propositions as types  
→ PDF pp. 121–122 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.3 Mere propositions**  
Mere propositions.  
*Terms:* mere propositions  
→ PDF pp. 123–124 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.4 Classical vs. intuitionistic logic**  
Classical vs. intuitionistic logic.  
*Terms:* LEM, classical logic  
→ PDF p. 125 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.5 Subsets and propositional resizing**  
Subsets and resizing.  
*Terms:* subsets, propositional resizing  
→ PDF pp. 126–127 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.6 The logic of mere propositions**  
Logic of mere propositions.  
*Terms:* logic  
→ PDF p. 128 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.7 Propositional truncation**  
Propositional truncation.  
*Terms:* propositional truncation  
→ PDF p. 129 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.8 The axiom of choice**  
Axiom of choice.  
*Terms:* axiom of choice  
→ PDF pp. 130–131 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.9 The principle of unique choice**  
Unique choice.  
*Terms:* unique choice  
→ PDF p. 132 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.10 When are propositions truncated?**  
When are propositions truncated?  
*Terms:* truncation  
→ PDF pp. 133–134 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**3.11 Contractibility**  
Contractibility.  
*Terms:* contractible types  
→ PDF pp. 135–137 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch5"></a>
## 4 Equivalences

*PDF pp. 141–160*

Coherent notions of equivalence.

**4.1 Quasi-inverses**  
Quasi-inverses.  
*Terms:* quasi-inverse  
→ PDF pp. 141–143 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.2 Half adjoint equivalences**  
Half-adjoint equivalences.  
*Terms:* half adjoint equivalence  
→ PDF pp. 144–147 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.3 Bi-invertible maps**  
Bi-invertible maps.  
*Terms:* bi-invertible map  
→ PDF p. 148 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.4 Contractible fibers**  
Contractible fibers.  
*Terms:* contractible fibers  
→ PDF p. 148 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.5 On the definition of equivalences**  
Why these definitions.  
*Terms:* isEquiv as proposition  
→ PDF p. 149 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.6 Surjections and embeddings**  
Surjections and embeddings.  
*Terms:* surjection, embedding  
→ PDF p. 150 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.7 Closure properties of equivalences**  
Closure properties.  
*Terms:* 2-out-of-3  
→ PDF pp. 151–153 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.8 The object classifier**  
The object classifier.  
*Terms:* object classifier  
→ PDF pp. 154–155 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**4.9 Univalence implies function extensionality**  
Univalence implies function extensionality.  
*Terms:* funext from univalence  
→ PDF pp. 156–157 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch6"></a>
## 5 Induction

*PDF pp. 161–190*

Inductive types.

**5.1 Introduction to inductive types**  
Inductive types introduced.  
*Terms:* inductive types  
→ PDF pp. 161–163 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**5.2 Uniqueness of inductive types**  
Uniqueness up to equivalence.  
*Terms:* uniqueness  
→ PDF pp. 164–165 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**5.3 W-types**  
W-types.  
*Terms:* W-types  
→ PDF pp. 166–168 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**5.4 Inductive types are initial algebras**  
Initial algebras.  
*Terms:* initial algebra  
→ PDF pp. 169–171 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**5.5 Homotopy-inductive types**  
Homotopy-inductive types.  
*Terms:* homotopy-initial  
→ PDF pp. 172–175 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**5.6 The general syntax of inductive definitions**  
General syntax.  
*Terms:* syntax  
→ PDF pp. 176–179 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**5.7 Generalizations of inductive types**  
Generalizations.  
*Terms:* inductive families, induction-recursion  
→ PDF pp. 180–181 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**5.8 Identity types and identity systems**  
Identity systems.  
*Terms:* identity systems  
→ PDF pp. 182–185 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch7"></a>
## 6 Higher inductive types

*PDF pp. 191–232*

Higher inductive types.

**6.1 Introduction**  
Motivation.  
*Terms:* HITs  
→ PDF pp. 191–192 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.2 Induction principles and dependent paths**  
Induction principles and dependent paths.  
*Terms:* dependent paths  
→ PDF pp. 193–196 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.3 The interval**  
The interval.  
*Terms:* interval  
→ PDF pp. 197–198 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.4 Circles and spheres**  
Circles and spheres.  
*Terms:* circle S1, spheres  
→ PDF pp. 199–200 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.5 Suspensions**  
Suspensions.  
*Terms:* suspension  
→ PDF pp. 201–203 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.6 Cell complexes**  
Cell complexes (torus).  
*Terms:* torus, cell complexes  
→ PDF p. 204 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.7 Hubs and spokes**  
Hubs and spokes.  
*Terms:* hubs and spokes  
→ PDF pp. 205–206 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.8 Pushouts**  
Pushouts.  
*Terms:* pushouts  
→ PDF pp. 207–209 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.9 Truncations**  
Truncations as HITs.  
*Terms:* truncation  
→ PDF pp. 210–212 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.10 Quotients**  
Set quotients.  
*Terms:* quotients  
→ PDF pp. 213–217 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.11 Algebra**  
Algebra (free groups).  
*Terms:* free groups  
→ PDF pp. 218–222 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.12 The flattening lemma**  
The flattening lemma.  
*Terms:* flattening lemma  
→ PDF pp. 223–227 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**6.13 The general syntax of higher inductive definitions**  
General syntax.  
*Terms:* syntax  
→ PDF pp. 228–229 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch8"></a>
## 7 Homotopy n-types

*PDF pp. 233–270*

Truncation levels and connectedness.

**7.1 Definition of n-types**  
n-types.  
*Terms:* n-types  
→ PDF pp. 233–236 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**7.2 Uniqueness of identity proofs and Hedberg's theorem**  
UIP and Hedberg’s theorem.  
*Terms:* Hedberg theorem, UIP  
→ PDF pp. 237–239 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**7.3 Truncations**  
n-truncations.  
*Terms:* truncation  
→ PDF pp. 240–245 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**7.4 Colimits of n-types**  
Colimits of n-types.  
*Terms:* colimits  
→ PDF pp. 246–249 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**7.5 Connectedness**  
Connectedness.  
*Terms:* n-connected maps  
→ PDF pp. 250–254 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**7.6 Orthogonal factorization**  
Orthogonal factorization systems.  
*Terms:* factorization systems  
→ PDF pp. 255–258 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**7.7 Modalities**  
Modalities.  
*Terms:* modalities  
→ PDF pp. 259–263 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch9"></a>
## 8 Homotopy theory

*PDF pp. 271–318*

Synthetic homotopy theory.

**8.1 π₁(S¹)**  
The fundamental group of the circle is ℤ.  
*Terms:* pi1 of circle, encode-decode  
→ PDF pp. 274–282 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.2 Connectedness of suspensions**  
Connectedness of suspensions.  
*Terms:* suspension connectivity  
→ PDF p. 283 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.3 π_(k≤n) of an n-connected space and π_(k<n)(Sⁿ)**  
Low homotopy groups of spheres.  
*Terms:* homotopy groups of spheres  
→ PDF p. 284 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.4 Fiber sequences and the long exact sequence**  
Fiber sequences and long exact sequences.  
*Terms:* fiber sequence, long exact sequence  
→ PDF pp. 285–288 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.5 The Hopf fibration**  
Hopf fibration.  
*Terms:* Hopf fibration  
→ PDF pp. 289–294 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.6 The Freudenthal suspension theorem**  
Freudenthal suspension theorem.  
*Terms:* Freudenthal suspension  
→ PDF pp. 295–300 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.7 The van Kampen theorem**  
van Kampen.  
*Terms:* van Kampen  
→ PDF pp. 301–309 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.8 Whitehead's theorem and Whitehead's principle**  
Whitehead’s theorem and principle.  
*Terms:* Whitehead theorem  
→ PDF pp. 310–313 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.9 A general statement of the encode-decode method**  
The encode–decode method in general.  
*Terms:* encode-decode method  
→ PDF p. 314 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**8.10 Additional Results**  
Further results.  
*Terms:* further results  
→ PDF p. 315 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch10"></a>
## 9 Category theory

*PDF pp. 319–352*

Univalent category theory.

**9.1 Categories and precategories**  
Precategories and categories.  
*Terms:* precategory, univalent category  
→ PDF pp. 320–322 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.2 Functors and transformations**  
Functors and transformations.  
*Terms:* functors  
→ PDF pp. 323–326 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.3 Adjunctions**  
Adjunctions.  
*Terms:* adjunctions  
→ PDF p. 327 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.4 Equivalences**  
Equivalences.  
*Terms:* equivalence of categories  
→ PDF pp. 328–332 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.5 The Yoneda lemma**  
Yoneda.  
*Terms:* Yoneda lemma  
→ PDF pp. 333–336 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.6 Strict categories**  
Strict categories.  
*Terms:* strict categories  
→ PDF p. 337 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.7 †-categories**  
†-categories.  
*Terms:* dagger categories  
→ PDF p. 337 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.8 The structure identity principle**  
Structure identity principle.  
*Terms:* structure identity principle  
→ PDF pp. 338–340 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**9.9 The Rezk completion**  
Rezk completion.  
*Terms:* Rezk completion  
→ PDF pp. 341–348 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch11"></a>
## 10 Set theory

*PDF pp. 353–384*

Set theory in univalent foundations.

**10.1 The category of sets**  
The category of sets as a ΠW-pretopos.  
*Terms:* category of sets, ETCS  
→ PDF pp. 353–361 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**10.2 Cardinal numbers**  
Cardinals.  
*Terms:* cardinal numbers  
→ PDF pp. 362–364 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**10.3 Ordinal numbers**  
Ordinals.  
*Terms:* ordinal numbers  
→ PDF pp. 365–370 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**10.4 Classical well-orderings**  
Classical well-ordering under choice.  
*Terms:* well-ordering, choice  
→ PDF pp. 371–373 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**10.5 The cumulative hierarchy**  
The cumulative hierarchy V as a HIT.  
*Terms:* cumulative hierarchy  
→ PDF pp. 374–379 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch12"></a>
## 11 Real numbers

*PDF pp. 385–436*

Constructive analysis.

**11.1 The field of rational numbers**  
Rationals as an ordered field.  
*Terms:* rational numbers  
→ PDF p. 386 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**11.2 Dedekind reals**  
Dedekind reals.  
*Terms:* Dedekind reals  
→ PDF pp. 386–392 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**11.3 Cauchy reals**  
Cauchy reals as a higher inductive-inductive type.  
*Terms:* Cauchy reals, HIIT  
→ PDF pp. 393–411 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**11.4 Comparison of Cauchy and Dedekind reals**  
Comparing them.  
*Terms:* comparison  
→ PDF p. 412 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**11.5 Compactness of the interval**  
Compactness of [0,1].  
*Terms:* compactness  
→ PDF pp. 413–418 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**11.6 The surreal numbers**  
Surreal numbers.  
*Terms:* surreal numbers  
→ PDF pp. 419–430 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)


---

<a id="ch13"></a>
## A Formal type theory

*PDF pp. 437–453*

Formal presentations of the type theory.

**A.1 The first presentation**  
First presentation (judgments and rules).  
*Terms:* formal type theory, judgments  
→ PDF pp. 439–442 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**A.2 The second presentation**  
Second presentation (with explicit equality).  
*Terms:* definitional equality  
→ PDF pp. 443–449 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**A.3 Homotopy type theory**  
Rules specific to HoTT.  
*Terms:* univalence, HIT rules  
→ PDF p. 450 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

**A.4 Basic metatheory**  
Basic metatheory.  
*Terms:* metatheory  
→ PDF pp. 451–452 in [the PDF](https://drive.google.com/file/d/1fymq_3-J4FqK7iffzsDBFHRo_yveTWq9/view)

