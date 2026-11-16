<a id="ch1"></a>
# Introducing Category Theory (2nd edition)

> Peter Smith · Logic Matters, version 2.1, 2025 (free PDF) · [the PDF in Drive](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

Short “Challenges!” and “Responses” subsections are not broken out; the interlude and bibliography are not covered. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A slow-paced, carefully motivated introduction to category theory for philosophers, logicians and mathematics students, by a logician known for teaching texts. Smith starts from categories of groups and questions about sets, classes and size, then builds the elementary theory: arrows and their kinds, initial and terminal objects, products and coproducts (first “pre-categorially”), internal groups, equalizers, exponentials and cartesian closed categories, limits and colimits, pullbacks and the existence of limits, subobjects and subobject classifiers. The middle part covers functors, comma categories, hom-functors, natural transformations, equivalence of categories, functor categories, Yoneda and representables, Galois connections and adjunctions. The final part introduces elementary toposes: power objects, natural numbers objects, internal logic, subobject lattices, complements, well-pointedness and ETCS.

**Contents**

1. [Introduction](ch1): Why study categories and how the book proceeds.
2. [Groups, and categories of groups](ch2): Groups as a warm-up for categorial ideas.
3. [Sets, classes, plurals](ch3): Foundational worries about collections.
4. [Where do categories of groups live?](ch4): What framework hosts the category of groups?.
5. [Categories in general](ch5): The definition of category and many examples.
6. [Diagrams, informally](ch6): Diagrams and commutativity.
7. [Categories beget categories](ch7): Constructing new categories.
8. [Kinds of arrows](ch8): Monos, epis, isos and friends.
9. [Initial and terminal objects](ch9): Initial and terminal objects.
10. [Pairs and products, pre-categorially](ch10): Products before category theory.
11. [Categorial products and coproducts](ch11): Products and coproducts categorially.
12. [Products more generally](ch12): n-ary and infinite products.
13. [Binary products explored](ch13): Theorems about binary products.
14. [Groups in categories](ch14): Internal group objects.
15. [Quotients, pre-categorially](ch15): Quotients before category theory.
16. [Equalizers and co-equalizers](ch16): Equalizers and coequalizers.
17. [Exponentials](ch17): Exponential objects.
18. [Cartesian closed categories](ch18): Cartesian closed categories.
19. [Limits and colimits defined](ch19): Limits and colimits.
20. [Pullbacks and pushouts](ch20): Pullbacks and pushouts.
21. [The existence of limits](ch21): When do all limits exist?.
22. [Subobjects](ch22): Subobjects.
23. [Subobject classifiers](ch23): Subobject classifiers.
24. [Functors introduced](ch24): Functors.
25. [What functors can do](ch25): Properties of functors.
26. [Functors, diagrams, and limits](ch26): Functors and limits.
27. [Functors and comma categories](ch27): Comma categories.
28. [Hom-sets (and some matters of size)](ch28): Hom-sets and size.
29. [Hom-functors](ch29): Hom-functors.
30. [Natural isomorphisms](ch30): Natural isomorphisms.
31. [Natural transformations](ch31): Natural transformations.
32. [Isomorphic categories, equivalent categories](ch32): Isomorphism vs.
33. [Categories of categories](ch33): Categories of categories.
34. [Functor categories](ch34): Functor categories.
35. [The Yoneda Embedding](ch35): The Yoneda embedding.
36. [The Yoneda Lemma](ch36): The full Yoneda lemma.
37. [Representables and universal elements](ch37): Representable functors and universal elements.
38. [Galois connections](ch38): Galois connections as adjunctions between posets.
39. [Adjunctions introduced](ch39): Adjunctions.
40. [Five basic theorems](ch40): Basic theorems about adjoints.
41. [Adjunctions explored](ch41): Adjunctions further.
42. [Toposes: defined, with examples](ch42): Elementary toposes.
43. [Two useful facts about toposes](ch43): Power objects and factorization.
44. [Natural numbers objects](ch44): Natural numbers objects.
45. [A very little logic in a topos](ch45): Internal logic of a topos.
46. [Subobjects, intersections, unions, etc.](ch46): Operations on subobjects.
47. [Complements of subobjects](ch47): Complements and pseudo-complements.
48. [Well-pointed toposes](ch48): Well-pointed toposes.
49. [Classical arenas and ETCS](ch49): Classical toposes and Lawvere’s ETCS.


---

## Introduction

*PDF pp. 15–18*

Why study categories and how the book proceeds.

**The categorial imperative**  
The case for categorial thinking.  
*Terms:* motivation  
→ PDF pp. 15–16 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**From a bird's eye view**  
An overview from above.  
*Terms:* overview  
→ PDF p. 17 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A slow ascent**  
The plan of slow ascent.  
*Terms:* plan  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch2"></a>
## Groups, and categories of groups

*PDF pp. 19–34*

Groups as a warm-up for categorial ideas.

**Groups defined**  
Group axioms.  
*Terms:* group  
→ PDF pp. 19–20 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Fixing notation**  
Notation.  
*Terms:* notation  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**New groups from old**  
Products and other constructions.  
*Terms:* direct product, quotient  
→ PDF pp. 21–24 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Group homomorphisms**  
Homomorphisms.  
*Terms:* homomorphism  
→ PDF pp. 25–26 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Isomorphisms, automorphisms**  
Isomorphisms and automorphisms.  
*Terms:* isomorphism, automorphism  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Redefining isomorphisms**  
Isomorphism as invertible homomorphism.  
*Terms:* inverse  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Homomorphisms and constructions**  
Homomorphisms and constructions.  
*Terms:* constructions  
→ PDF pp. 29–30 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**`Identical up to isomorphism'**  
Sameness up to isomorphism.  
*Terms:* up to isomorphism  
→ PDF p. 31 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Categories of groups**  
Categories of groups.  
*Terms:* category of groups  
→ PDF pp. 32–34 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch3"></a>
## Sets, classes, plurals

*PDF pp. 35–38*

Foundational worries about collections.

**Sets and (virtual) classes**  
Sets vs. virtual classes.  
*Terms:* sets, classes  
→ PDF p. 35 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Don't try to eliminate plurals!**  
Defending plural talk.  
*Terms:* plurals, plural logic  
→ PDF pp. 36–37 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Why fuss?**  
Why it matters.  
*Terms:* foundations  
→ PDF p. 38 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch4"></a>
## Where do categories of groups live?

*PDF pp. 39–48*

What framework hosts the category of groups?

**One `generous arena' in which to pursue group theory**  
A generous set-theoretic arena.  
*Terms:* set theory, universe  
→ PDF pp. 39–41 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Alternative implementations?**  
Alternative implementations.  
*Terms:* implementations  
→ PDF pp. 42–45 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**`The' category of groups?**  
Is there one category of groups?  
*Terms:* Grp, uniqueness  
→ PDF pp. 46–48 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch5"></a>
## Categories in general

*PDF pp. 49–63*

The definition of category and many examples.

**The very idea of a category**  
Objects, arrows, composition.  
*Terms:* category  
→ PDF pp. 49–51 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Identity arrows**  
Identities.  
*Terms:* identity  
→ PDF p. 52 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Monoids and pre-ordered collections**  
Monoids and preorders as categories.  
*Terms:* monoid, preorder  
→ PDF pp. 53–54 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some rather sparse categories**  
Sparse categories.  
*Terms:* discrete categories  
→ PDF pp. 55–56 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**More categories**  
More examples.  
*Terms:* examples  
→ PDF pp. 57–58 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**The category of sets**  
Set.  
*Terms:* Set  
→ PDF pp. 59–60 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Yet more examples**  
Further examples.  
*Terms:* Grp, Top, Vect  
→ PDF pp. 61–63 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch6"></a>
## Diagrams, informally

*PDF pp. 64–67*

Diagrams and commutativity.

**Diagrams, in two senses**  
Two senses of diagram.  
*Terms:* diagram  
→ PDF p. 64 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Commutative diagrams**  
Commuting diagrams.  
*Terms:* commutative diagram  
→ PDF pp. 65–66 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A revised definition**  
A revised definition.  
*Terms:* definition  
→ PDF p. 67 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch7"></a>
## Categories beget categories

*PDF pp. 68–76*

Constructing new categories.

**Subcategories, products, quotients**  
Subcategories, products, quotients.  
*Terms:* subcategory, product category, quotient category  
→ PDF pp. 68–70 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Duality**  
Opposites and duality.  
*Terms:* duality, opposite category  
→ PDF pp. 71–72 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Slice categories**  
Slices.  
*Terms:* slice category  
→ PDF pp. 73–74 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Arrow categories, and categories of variable sets**  
Arrow categories and variable sets.  
*Terms:* arrow category  
→ PDF pp. 75–76 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch8"></a>
## Kinds of arrows

*PDF pp. 77–90*

Monos, epis, isos and friends.

**Monomorphisms, epimorphisms**  
Monomorphisms and epimorphisms.  
*Terms:* monomorphism, epimorphism  
→ PDF pp. 77–79 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Inverses**  
Sections and retractions.  
*Terms:* inverse, section, retraction  
→ PDF pp. 80–82 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some more – less memorable? – terminology**  
Split monos/epis and more terms.  
*Terms:* split mono, bimorphism  
→ PDF p. 83 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Isomorphisms**  
Isomorphisms.  
*Terms:* isomorphism  
→ PDF pp. 84–86 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Isomorphic objects**  
Isomorphic objects.  
*Terms:* isomorphic objects  
→ PDF p. 87 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A couple more theorems**  
Further theorems.  
*Terms:* theorems  
→ PDF pp. 88–89 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Groups as categories, and groupoids**  
Groups and groupoids as categories.  
*Terms:* groupoid  
→ PDF p. 90 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch9"></a>
## Initial and terminal objects

*PDF pp. 91–98*

Initial and terminal objects.

**Initial and terminal defined**  
Definitions.  
*Terms:* initial, terminal object  
→ PDF pp. 91–93 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Uniqueness up to unique isomorphism**  
Uniqueness up to unique isomorphism.  
*Terms:* uniqueness  
→ PDF p. 94 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Elements**  
Elements as arrows from 1.  
*Terms:* global elements  
→ PDF p. 95 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Separators and well-pointed categories**  
Separators and well-pointedness.  
*Terms:* separator, well-pointed  
→ PDF p. 96 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**`Generalized elements'**  
Generalized elements.  
*Terms:* generalized elements  
→ PDF p. 97 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**`And what about arrows to 0?'**  
Arrows into 0.  
*Terms:* initial object  
→ PDF p. 98 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch10"></a>
## Pairs and products, pre-categorially

*PDF pp. 99–105*

Products before category theory.

**Ways of pairing numbers**  
Pairing numbers.  
*Terms:* pairing functions  
→ PDF pp. 99–100 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Pairing schemes more generally**  
Pairing schemes.  
*Terms:* pairing schemes  
→ PDF pp. 101–103 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Defining products, pre-categorially**  
Products defined by pairing.  
*Terms:* product  
→ PDF pp. 104–105 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch11"></a>
## Categorial products and coproducts

*PDF pp. 106–118*

Products and coproducts categorially.

**Products defined categorially**  
The universal property.  
*Terms:* product, universal property  
→ PDF pp. 106–107 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Examples**  
Examples.  
*Terms:* examples  
→ PDF pp. 108–109 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Products as terminal objects**  
Products as terminal cones.  
*Terms:* terminal object  
→ PDF pp. 110–111 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Uniqueness up to unique isomorphism**  
Uniqueness.  
*Terms:* uniqueness  
→ PDF pp. 112–113 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Notation for mediating arrows**  
Mediating-arrow notation.  
*Terms:* mediating arrow  
→ PDF p. 114 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Two general comments**  
Comments.  
*Terms:* remarks  
→ PDF p. 115 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Coproducts**  
Coproducts.  
*Terms:* coproduct  
→ PDF pp. 115–118 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch12"></a>
## Products more generally

*PDF pp. 119–121*

n-ary and infinite products.

**Ternary products**  
Ternary.  
*Terms:* ternary products  
→ PDF p. 119 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**More finite products**  
Finite.  
*Terms:* finite products  
→ PDF p. 120 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Infinite products**  
Infinite.  
*Terms:* infinite products  
→ PDF p. 121 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch13"></a>
## Binary products explored

*PDF pp. 122–130*

Theorems about binary products.

**Four simple theorems, and a non-theorem**  
Basic theorems and a non-theorem.  
*Terms:* product theorems  
→ PDF pp. 123–125 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Two more theorems on mediating arrows**  
Mediating-arrow theorems.  
*Terms:* mediating arrows  
→ PDF p. 126 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Products in Set/X.**  
Products in slices.  
*Terms:* slice category  
→ PDF p. 127 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Arrows between two products**  
Arrows between products.  
*Terms:* product of arrows  
→ PDF pp. 128–130 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch14"></a>
## Groups in categories

*PDF pp. 131–136*

Internal group objects.

**Instead of binary functions**  
Arrows instead of binary functions.  
*Terms:* group object  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Internal groups in Set, Top and Man**  
Groups in Set, Top and Man.  
*Terms:* topological groups, Lie groups  
→ PDF pp. 132–133 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Groups in Grp**  
Groups in Grp (abelian).  
*Terms:* Eckmann-Hilton  
→ PDF pp. 134–135 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**The story continues …**  
Outlook.  
*Terms:* outlook  
→ PDF p. 136 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch15"></a>
## Quotients, pre-categorially

*PDF pp. 137–141*

Quotients before category theory.

**Equivalence relations**  
Equivalence relations.  
*Terms:* equivalence relation  
→ PDF pp. 137–138 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Quotient schemes again**  
Quotient schemes.  
*Terms:* quotient  
→ PDF pp. 139–140 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A key result about quotients to carry forward**  
A key result.  
*Terms:* universal property  
→ PDF p. 141 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch16"></a>
## Equalizers and co-equalizers

*PDF pp. 142–150*

Equalizers and coequalizers.

**Forks and equalizers defined**  
Forks and equalizers.  
*Terms:* equalizer  
→ PDF p. 142 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Examples of equalizers**  
Examples.  
*Terms:* examples  
→ PDF pp. 143–144 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Uniqueness up to unique isomorphism**  
Uniqueness.  
*Terms:* uniqueness  
→ PDF pp. 145–146 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Co-forks and co-equalizers defined**  
Coforks and coequalizers.  
*Terms:* coequalizer  
→ PDF p. 149 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Examples of co-equalizers**  
Examples.  
*Terms:* examples  
→ PDF p. 150 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch17"></a>
## Exponentials

*PDF pp. 151–159*

Exponential objects.

**Instead of binary functions, again**  
Currying motivation.  
*Terms:* currying  
→ PDF pp. 151–152 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Exponentials in categories**  
Exponentials defined.  
*Terms:* exponential  
→ PDF p. 153 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some categories with exponentials**  
Examples.  
*Terms:* Set, Pos  
→ PDF pp. 153–154 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another example of a category with exponentials**  
Another example.  
*Terms:* example  
→ PDF p. 155 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Uniqueness up to unique isomorphism**  
Uniqueness.  
*Terms:* uniqueness  
→ PDF p. 156 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Further general results about exponentials**  
General results.  
*Terms:* results  
→ PDF pp. 157–158 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**`And what is the dual construction?'**  
The dual.  
*Terms:* co-exponential  
→ PDF p. 159 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch18"></a>
## Cartesian closed categories

*PDF pp. 160–164*

Cartesian closed categories.

**A definition and some initial results**  
Definition and first results.  
*Terms:* cartesian closed category  
→ PDF pp. 160–161 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Degeneracy**  
Degenerate CCCs.  
*Terms:* degeneracy  
→ PDF pp. 163–164 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch19"></a>
## Limits and colimits defined

*PDF pp. 165–174*

Limits and colimits.

**Cones over diagrams**  
Cones over diagrams.  
*Terms:* cone  
→ PDF pp. 165–166 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Limits**  
Limits.  
*Terms:* limit  
→ PDF p. 167 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Uniqueness up to unique isomorphism**  
Uniqueness.  
*Terms:* uniqueness  
→ PDF pp. 168–169 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Cocones and colimits**  
Cocones and colimits.  
*Terms:* colimit  
→ PDF pp. 173–174 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch20"></a>
## Pullbacks and pushouts

*PDF pp. 175–187*

Pullbacks and pushouts.

**Pullbacks defined**  
Pullbacks defined.  
*Terms:* pullback  
→ PDF p. 175 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Examples**  
Examples.  
*Terms:* examples  
→ PDF pp. 176–178 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**More on pullbacks and products**  
Pullbacks and products.  
*Terms:* products  
→ PDF p. 179 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Pullbacks, monos, equalizers**  
Pullbacks, monos and equalizers.  
*Terms:* monos, equalizers  
→ PDF pp. 180–181 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Pushouts**  
Pushouts.  
*Terms:* pushout  
→ PDF pp. 185–187 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch21"></a>
## The existence of limits

*PDF pp. 188–196*

When do all limits exist?

**The key theorems stated**  
The completeness theorems.  
*Terms:* finite completeness  
→ PDF p. 188 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Products plus equalizers imply pullbacks**  
Pullbacks from products and equalizers.  
*Terms:* pullbacks  
→ PDF pp. 189–190 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Deriving the finite completeness theorem**  
Finite completeness.  
*Terms:* finite limits  
→ PDF pp. 191–193 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Deriving the variant completeness theorem**  
A variant.  
*Terms:* variant  
→ PDF p. 194 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Infinite limits**  
Infinite limits.  
*Terms:* infinite limits  
→ PDF p. 195 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Dualizing again**  
Duals.  
*Terms:* cocompleteness  
→ PDF p. 196 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch22"></a>
## Subobjects

*PDF pp. 197–203*

Subobjects.

**Subsets revisited**  
Subsets revisited.  
*Terms:* subsets  
→ PDF p. 197 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Subobjects and monic arrows**  
Subobjects as classes of monos.  
*Terms:* subobject, monic  
→ PDF pp. 198–199 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Ordering subobjects**  
Ordering.  
*Terms:* order  
→ PDF p. 200 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**How many subobjects?**  
Counting subobjects.  
*Terms:* size  
→ PDF p. 201 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another way of thinking of subobjects?**  
Alternative views.  
*Terms:* alternatives  
→ PDF p. 202 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Images**  
Images.  
*Terms:* image  
→ PDF p. 203 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch23"></a>
## Subobject classifiers

*PDF pp. 204–217*

Subobject classifiers.

**Motivation**  
Motivation from characteristic functions.  
*Terms:* characteristic function  
→ PDF pp. 204–205 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Defining a subobject classifier (Ω, ⊤)**  
Defining (Ω, ⊤).  
*Terms:* subobject classifier, Omega  
→ PDF p. 206 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**⊤, ⊥, and ¬**  
⊤, ⊥ and ¬.  
*Terms:* true, false, negation  
→ PDF pp. 206–207 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**An instructive example**  
An example.  
*Terms:* example  
→ PDF pp. 208–209 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Four general theorems about subobject classifiers**  
General theorems.  
*Terms:* theorems  
→ PDF pp. 210–212 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another way of looking at subobject classifiers**  
Another view.  
*Terms:* power objects  
→ PDF p. 213 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Which categories have subobject classifiers?**  
Which categories have them.  
*Terms:* existence  
→ PDF p. 213 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A digression on duals**  
Duals.  
*Terms:* duals  
→ PDF p. 214 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another example?**  
Another example.  
*Terms:* example  
→ PDF pp. 214–217 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch24"></a>
## Functors introduced

*PDF pp. 220–231*

Functors.

**Functors defined**  
Definition.  
*Terms:* functor  
→ PDF pp. 220–221 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some elementary examples of functors**  
Elementary examples.  
*Terms:* examples  
→ PDF pp. 222–224 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Three endofunctors**  
Endofunctors.  
*Terms:* endofunctor  
→ PDF pp. 225–226 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another functor involving products**  
A product functor.  
*Terms:* product functor  
→ PDF p. 227 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A functor from Set to Mon**  
Free monoid functor.  
*Terms:* free monoid  
→ PDF p. 228 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Contravariance**  
Contravariance.  
*Terms:* contravariant functor  
→ PDF p. 229 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Functors and opposite categories**  
Opposites.  
*Terms:* opposite  
→ PDF pp. 230–231 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch25"></a>
## What functors can do

*PDF pp. 232–240*

Properties of functors.

**Images assembled by a functor needn't be categories**  
Functor images.  
*Terms:* image of functor  
→ PDF p. 232 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Preserving and reflecting**  
Preserving and reflecting.  
*Terms:* preserve, reflect  
→ PDF pp. 232–233 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Faithful, full, and essentially surjective functors**  
Faithful, full, essentially surjective.  
*Terms:* faithful, full, essentially surjective  
→ PDF pp. 234–236 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**An example from topology**  
A topology example.  
*Terms:* topology  
→ PDF pp. 237–238 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**An afterword on the idea of concrete categories**  
Concrete categories.  
*Terms:* concrete category  
→ PDF pp. 239–240 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch26"></a>
## Functors, diagrams, and limits

*PDF pp. 241–247*

Functors and limits.

**Diagrams redefined as functors**  
Diagrams as functors.  
*Terms:* diagram as functor  
→ PDF pp. 241–243 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Preserving limits**  
Preservation.  
*Terms:* limit preservation  
→ PDF p. 244 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A limit preservation theorem**  
A preservation theorem.  
*Terms:* theorem  
→ PDF p. 245 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Reflecting limits**  
Reflection.  
*Terms:* limit reflection  
→ PDF pp. 246–247 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch27"></a>
## Functors and comma categories

*PDF pp. 248–253*

Comma categories.

**Comma categories defined**  
Definition.  
*Terms:* comma category  
→ PDF pp. 248–249 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Three types of comma category**  
Slices, coslices and arrow categories as cases.  
*Terms:* slice, coslice  
→ PDF pp. 250–252 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**An application: free monoids again**  
Free monoids again.  
*Terms:* free monoid  
→ PDF p. 253 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch28"></a>
## Hom-sets (and some matters of size)

*PDF pp. 254–259*

Hom-sets and size.

**Defining categories again**  
Hom-set-based definition.  
*Terms:* hom-set  
→ PDF pp. 254–256 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Where do hom-sets live?**  
Where hom-sets live.  
*Terms:* size  
→ PDF p. 257 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Hom-sets, officially?**  
Local smallness.  
*Terms:* locally small  
→ PDF pp. 258–259 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch29"></a>
## Hom-functors

*PDF pp. 260–264*

Hom-functors.

**Two kinds of hom-functors**  
Covariant and contravariant.  
*Terms:* hom-functor  
→ PDF pp. 260–261 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Points of view**  
Viewpoints.  
*Terms:* viewpoints  
→ PDF p. 262 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Covariant hom-functors preserve limits**  
Hom-functors preserve limits.  
*Terms:* limit preservation  
→ PDF pp. 262–263 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A dual result?**  
The dual.  
*Terms:* dual  
→ PDF p. 264 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch30"></a>
## Natural isomorphisms

*PDF pp. 265–282*

Natural isomorphisms.

**Natural isomorphisms between functors defined**  
Definition.  
*Terms:* natural isomorphism  
→ PDF pp. 265–266 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some basic properties**  
Properties.  
*Terms:* properties  
→ PDF pp. 267–268 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Why `natural'?**  
Why natural.  
*Terms:* naturality  
→ PDF pp. 269–271 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**More examples of natural isomorphisms**  
Examples.  
*Terms:* examples  
→ PDF pp. 272–275 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another basic property of isomorphic functors**  
Further property.  
*Terms:* property  
→ PDF pp. 276–277 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Unnatural and natural isomorphisms between objects**  
Natural vs. unnatural isomorphisms.  
*Terms:* double dual  
→ PDF pp. 278–280 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**An `Eilenberg/Mac Lane Thesis'?**  
An Eilenberg–Mac Lane thesis.  
*Terms:* Eilenberg-Mac Lane  
→ PDF pp. 281–282 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch31"></a>
## Natural transformations

*PDF pp. 283–292*

Natural transformations.

**Natural transformations defined**  
Definition.  
*Terms:* natural transformation  
→ PDF pp. 283–284 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some examples**  
Examples.  
*Terms:* examples  
→ PDF pp. 285–287 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Horizontal composition of natural transformations**  
Horizontal composition.  
*Terms:* horizontal composition  
→ PDF pp. 288–290 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Cones as natural transformations**  
Cones as natural transformations.  
*Terms:* cones  
→ PDF pp. 291–292 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch32"></a>
## Isomorphic categories, equivalent categories

*PDF pp. 293–304*

Isomorphism vs. equivalence of categories.

**Isomorphic categories**  
Isomorphic categories.  
*Terms:* isomorphic categories  
→ PDF pp. 293–294 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Intuitively equivalent but non-isomorphic categories**  
Equivalent but non-isomorphic.  
*Terms:* equivalence examples  
→ PDF pp. 295–297 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Equivalent categories**  
Equivalence defined.  
*Terms:* equivalence of categories  
→ PDF pp. 298–300 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Why equivalence is the categorially nicer notion**  
Why equivalence is better.  
*Terms:* principle of equivalence  
→ PDF p. 301 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Skeletons and evil**  
Skeletons and “evil”.  
*Terms:* skeleton, evil  
→ PDF pp. 302–304 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch33"></a>
## Categories of categories

*PDF pp. 305–308*

Categories of categories.

**A definition, and some tame categories of categories**  
Definitions and examples.  
*Terms:* Cat  
→ PDF p. 305 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A universal category?**  
A universal category?  
*Terms:* universal category  
→ PDF p. 306 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Cat, CAT and CAT?**  
Cat vs. CAT.  
*Terms:* size, CAT  
→ PDF pp. 307–308 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch34"></a>
## Functor categories

*PDF pp. 309–316*

Functor categories.

**Functor categories officially defined**  
Definition.  
*Terms:* functor category  
→ PDF p. 309 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Four simple examples**  
Examples.  
*Terms:* examples  
→ PDF pp. 310–311 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Hom-functors from functor categories**  
Hom-functors on functor categories.  
*Terms:* hom-functors  
→ PDF pp. 312–313 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Categories of diagrams and limit functors**  
Diagram categories and limit functors.  
*Terms:* limit functor  
→ PDF pp. 314–316 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch35"></a>
## The Yoneda Embedding

*PDF pp. 317–328*

The Yoneda embedding.

**Natural transformations between hom-functors**  
Natural transformations between hom-functors.  
*Terms:* hom-functors  
→ PDF pp. 317–320 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**The Restricted Yoneda Lemma**  
A restricted Yoneda lemma.  
*Terms:* restricted Yoneda  
→ PDF p. 321 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**The Yoneda Embedding, the Yoneda Principle**  
Embedding and Yoneda principle.  
*Terms:* Yoneda embedding, Yoneda principle  
→ PDF pp. 322–324 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Yoneda meets Cayley**  
Cayley’s theorem.  
*Terms:* Cayley theorem  
→ PDF p. 325 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Putting the Yoneda Principle to work**  
Applying the principle.  
*Terms:* applications  
→ PDF p. 326 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**``Friendship is everything''**  
“Friendship is everything”.  
*Terms:* relational view  
→ PDF pp. 327–328 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch36"></a>
## The Yoneda Lemma

*PDF pp. 329–335*

The full Yoneda lemma.

**Onwards to the full Yoneda Lemma!**  
Generalizing.  
*Terms:* Yoneda lemma  
→ PDF p. 329 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**The generalizing move**  
The key move.  
*Terms:* generalization  
→ PDF pp. 330–331 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Making it all natural**  
Naturality.  
*Terms:* naturality  
→ PDF pp. 332–334 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Putting everything together**  
Assembling the proof.  
*Terms:* proof  
→ PDF p. 335 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch37"></a>
## Representables and universal elements

*PDF pp. 336–346*

Representable functors and universal elements.

**Representable functors**  
Representables.  
*Terms:* representable functor  
→ PDF p. 336 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Two elementary examples**  
Simple examples.  
*Terms:* examples  
→ PDF pp. 337–338 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**More examples of representables**  
More examples.  
*Terms:* examples  
→ PDF pp. 339–341 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Universal elements**  
Universal elements.  
*Terms:* universal element  
→ PDF pp. 342–343 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Limits and exponentials as universal elements**  
Limits and exponentials as universal elements.  
*Terms:* limits, exponentials  
→ PDF pp. 344–346 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch38"></a>
## Galois connections

*PDF pp. 347–358*

Galois connections as adjunctions between posets.

**Posets: some probably unnecessary reminders**  
Posets reminder.  
*Terms:* posets  
→ PDF p. 347 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A first example of a Galois connection**  
A first example.  
*Terms:* example  
→ PDF pp. 348–349 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Galois connections defined**  
Definition.  
*Terms:* Galois connection  
→ PDF pp. 350–352 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Galois connections re-defined**  
Alternative definition.  
*Terms:* alternative definition  
→ PDF p. 353 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some basic results about Galois connections**  
Basic results.  
*Terms:* results  
→ PDF pp. 354–355 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Isomorphisms and closures**  
Closures.  
*Terms:* closure operators  
→ PDF p. 356 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Syntax and semantics briefly revisited**  
Syntax and semantics.  
*Terms:* syntax-semantics duality  
→ PDF pp. 357–358 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch39"></a>
## Adjunctions introduced

*PDF pp. 359–371*

Adjunctions.

**Adjoint functors: a first definition**  
First definition.  
*Terms:* adjunction  
→ PDF pp. 359–360 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Examples**  
Examples.  
*Terms:* free-forgetful, examples  
→ PDF pp. 361–365 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Naturality**  
Naturality.  
*Terms:* naturality  
→ PDF p. 366 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**An alternative definition**  
Unit–counit definition.  
*Terms:* unit, counit  
→ PDF pp. 367–369 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Isomorphism, equivalence, adjointness**  
Isomorphism, equivalence, adjointness.  
*Terms:* equivalence  
→ PDF pp. 370–371 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch40"></a>
## Five basic theorems

*PDF pp. 372–379*

Basic theorems about adjoints.

**Two definitions again**  
Definitions again.  
*Terms:* definitions  
→ PDF pp. 372–373 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another definition?**  
Another definition.  
*Terms:* universal arrows  
→ PDF p. 374 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Uniqueness and composition**  
Uniqueness and composition.  
*Terms:* uniqueness, composition  
→ PDF pp. 375–376 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Equivalences and adjunctions again**  
Equivalences as adjunctions.  
*Terms:* adjoint equivalence  
→ PDF pp. 377–379 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch41"></a>
## Adjunctions explored

*PDF pp. 380–394*

Adjunctions further.

**Adjunctions and comma categories**  
Via comma categories.  
*Terms:* comma categories  
→ PDF pp. 380–382 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Adjunctions and fully faithful functors**  
And fully faithful functors.  
*Terms:* reflective subcategory  
→ PDF pp. 383–384 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Adjunctions and representables**  
And representables.  
*Terms:* representables  
→ PDF p. 385 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Right adjoints preserve limits (`RAPL')**  
Right adjoints preserve limits.  
*Terms:* RAPL  
→ PDF pp. 386–387 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Limit (non)preservation: a few examples**  
Examples of (non)preservation.  
*Terms:* examples  
→ PDF pp. 388–389 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**An afterword on monads**  
Monads, briefly.  
*Terms:* monads  
→ PDF pp. 390–392 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Further questions**  
Open questions.  
*Terms:* further questions  
→ PDF pp. 393–394 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch42"></a>
## Toposes: defined, with examples

*PDF pp. 396–400*

Elementary toposes.

**Defining an elementary topos**  
Definition.  
*Terms:* elementary topos  
→ PDF p. 396 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A note on our definition**  
Notes on the definition.  
*Terms:* definition  
→ PDF p. 397 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A few initial examples**  
First examples.  
*Terms:* Set, presheaves  
→ PDF pp. 397–398 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Toposes beget toposes**  
Slices and other constructions.  
*Terms:* slice topos  
→ PDF pp. 399–400 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch43"></a>
## Two useful facts about toposes

*PDF pp. 401–409*

Power objects and factorization.

**Power objects**  
Power objects.  
*Terms:* power object  
→ PDF pp. 401–403 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Proving that Y is a power object for Y**  
Proof for a key case.  
*Terms:* proof  
→ PDF pp. 404–405 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Epi-mono factorization in a topos**  
Epi–mono factorization.  
*Terms:* epi-mono factorization  
→ PDF pp. 406–409 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch44"></a>
## Natural numbers objects

*PDF pp. 410–419*

Natural numbers objects.

**NNOs defined**  
Definition.  
*Terms:* natural numbers object  
→ PDF pp. 410–412 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Proving that a NNO has an infinite object**  
NNOs give infinite objects.  
*Terms:* infinite object  
→ PDF pp. 413–414 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**The Dedekind-Peano postulates**  
Dedekind–Peano axioms.  
*Terms:* Peano axioms  
→ PDF p. 415 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Recursion**  
Recursion.  
*Terms:* recursion  
→ PDF pp. 416–419 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch45"></a>
## A very little logic in a topos

*PDF pp. 420–430*

Internal logic of a topos.

**Negation, conjunction, disjunction**  
Connective arrows.  
*Terms:* negation, conjunction, disjunction  
→ PDF pp. 420–422 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**A conditional arrow**  
Implication.  
*Terms:* implication  
→ PDF p. 423 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some logical laws, but not double negation**  
Intuitionistic laws, no double negation elimination.  
*Terms:* intuitionistic logic  
→ PDF pp. 424–425 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Varieties of internal logic**  
Kinds of internal logic.  
*Terms:* internal logic  
→ PDF pp. 426–427 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch46"></a>
## Subobjects, intersections, unions, etc.

*PDF pp. 431–443*

Operations on subobjects.

**The intersection and union of subobjects defined**  
Intersections and unions.  
*Terms:* intersection, union  
→ PDF pp. 431–432 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Alternative definitions?**  
Alternatives.  
*Terms:* alternatives  
→ PDF p. 433 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Intersections, unions, and order**  
Order.  
*Terms:* lattice  
→ PDF p. 434 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Some more theorems about intersections and unions**  
More theorems.  
*Terms:* theorems  
→ PDF pp. 435–436 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Another construction on subobjects**  
Another construction.  
*Terms:* construction  
→ PDF p. 437 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch47"></a>
## Complements of subobjects

*PDF pp. 444–452*

Complements and pseudo-complements.

**Complements: three definitions**  
Three definitions.  
*Terms:* complement  
→ PDF pp. 444–445 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Complements interrelated**  
Relations.  
*Terms:* relations  
→ PDF p. 446 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Complements via ⊤ and ⊥**  
Complements via ⊤ and ⊥.  
*Terms:* negation  
→ PDF pp. 447–448 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Relative pseudo-complements**  
Relative pseudo-complements.  
*Terms:* relative pseudo-complement  
→ PDF p. 449 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Lattices and their logics**  
Heyting and Boolean lattices.  
*Terms:* Heyting algebra, Boolean algebra  
→ PDF pp. 449–452 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch48"></a>
## Well-pointed toposes

*PDF pp. 453–458*

Well-pointed toposes.

**Well-pointedness and its implications**  
Well-pointedness.  
*Terms:* well-pointed topos  
→ PDF pp. 453–454 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Members of subobjects**  
Members of subobjects.  
*Terms:* members  
→ PDF pp. 455–456 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

**Contrasts**  
Contrasts with general toposes.  
*Terms:* contrasts  
→ PDF pp. 457–458 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)


---

<a id="ch49"></a>
## Classical arenas and ETCS

*PDF pp. 459–460*

Classical toposes and Lawvere’s ETCS.

*Terms:* ETCS, elementary theory of the category of sets, Lawvere, Boolean topos

→ PDF pp. 459–460 in [the PDF](https://drive.google.com/file/d/1Ig36hpBXfx9JUPp5q9ATy-DEbTT1lEBU/view)

