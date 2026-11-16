<a id="ch1"></a>
# The Science of Functional Programming: A Tutorial, with Examples in Scala

> Sergei Winitzki · version of 4 September 2024, lulu.com (GNU FDL) · [the PDF in Drive](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

At about 1,300 pages, summaries and terms are given per chapter; each numbered section is still listed with its PDF page range. Exercise, summary and solved-example subsections and appendices other than C are not broken out. There is no HTML edition. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A mathematically rigorous course in functional programming that derives FP idioms and their laws by symbolic reasoning, with Scala code. The introductory part treats functions as formulas, induction and recursion, disjunctive types, curried and fully parametric functions, and the Curry–Howard correspondence with type isomorphisms. The intermediate part develops functors and contrafunctors, a notation for deriving code, typeclasses and their structural derivation, filterable functors, monads, applicatives and traversables, proving laws and building instances systematically. The advanced part covers free typeclass constructions (free monads, applicatives) and an extensive theory of monad transformers. Essays argue for “applied functional type theory”, and an appendix proves parametricity and naturality laws.

**Contents**

1. [1 Mathematical formulas as code. I. Nameless functions](ch1): Functions as formulas and anonymous functions.
2. [2 Mathematical formulas as code. II. Mathematical induction](ch2): Induction, recursion and folds.
3. [3 The logic of types. I. Disjunctive types](ch3): Case classes and disjunctive (sum) types.
4. [4 The logic of types. II. Curried functions](ch4): Currying and fully parametric functions.
5. [5 The logic of types. III. The Curry-Howard correspondence](ch5): Types as propositions.
6. [Essay: Towards functional data engineering with Scala](ch6): Essay: data engineering as applied mathematics.
7. [6 Functors and contrafunctors](ch7): Functors and contrafunctors.
8. [7 Reasoning about code. Techniques of symbolic derivation](ch8): Notation and techniques for deriving code.
9. [8 Typeclasses and functions of types](ch9): Typeclasses and type-level functions.
10. [9 Computations in functor blocks. I. Filterable functors and contrafunctors](ch10): Filterable functors.
11. [10 Computations in functor blocks. II. Semi-monads and monads](ch11): Semi-monads and monads.
12. [11 Applicative functors and contrafunctors](ch12): Applicative functors and contrafunctors.
13. [12 Traversable functors](ch13): Traversable functors.
14. [Essay: Software engineers and software artisans](ch14): Essay: programmers as artisans vs.
15. [Essay: Declarative programming as a silver bullet](ch15): Essay: declarative programming and DSLs.
16. [13 Free typeclass constructions](ch16): Free constructions.
17. [14 Computations in functor blocks. III. Monad transformers](ch17): Monad transformers in depth.
18. [15 Summary of the book](ch18): Summary and open topics.
19. [``Applied functional type theory'': A proposal](ch19): A proposal for “applied functional type theory”.
20. [Essay: Why category theory is useful in functional programming](ch20): Essay: why category theory helps FP.
21. [C Parametricity theorem and naturality laws](ch21): Parametricity and naturality laws.


---

## 1 Mathematical formulas as code. I. Nameless functions

*PDF pp. 25–48*

Functions as formulas and anonymous functions.

*Terms:* nameless functions, map, filter, aggregation, sum, product

**1.1 Translating mathematics into code**  
→ PDF pp. 25–30 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**1.2 Aggregating data from sequences**  
→ PDF pp. 31–32 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**1.3 Filtering and truncating a sequence**  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**1.4 Examples**  
→ PDF pp. 34–36 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**1.7 Discussion**  
→ PDF pp. 40–48 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch2"></a>
## 2 Mathematical formulas as code. II. Mathematical induction

*PDF pp. 49–108*

Induction, recursion and folds.

*Terms:* tuples, foldLeft, recursion, unfold, scan, tail recursion, mathematical induction

**2.1 Tuple types**  
→ PDF pp. 49–65 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**2.2 Converting a sequence into a single value**  
→ PDF pp. 66–82 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**2.3 Generating a sequence from a single value**  
→ PDF pp. 83–84 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**2.4 Transforming a sequence into another sequence**  
→ PDF pp. 85–86 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch3"></a>
## 3 The logic of types. I. Disjunctive types

*PDF pp. 109–154*

Case classes and disjunctive (sum) types.

*Terms:* case classes, sealed traits, Either, Option, recursive types, lists, trees

**3.1 Scala's ``case classes''**  
→ PDF pp. 109–114 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**3.2 Disjunctive types**  
→ PDF pp. 115–129 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**3.3 Lists and trees as recursive disjunctive types**  
→ PDF pp. 130–141 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch4"></a>
## 4 The logic of types. II. Curried functions

*PDF pp. 155–190*

Currying and fully parametric functions.

*Terms:* curried functions, parametric polymorphism, symbolic calculations

**4.1 Functions that return functions**  
→ PDF pp. 155–160 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**4.2 Fully parametric functions**  
→ PDF pp. 161–168 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**4.3 Symbolic calculations with nameless functions**  
→ PDF pp. 169–175 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch5"></a>
## 5 The logic of types. III. The Curry-Howard correspondence

*PDF pp. 191–276*

Types as propositions.

*Terms:* Curry-Howard, CH-propositions, type equivalence, type isomorphisms, implementability

**5.1 Values computed by fully parametric functions**  
→ PDF pp. 191–202 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**5.2 The logic of CH-propositions**  
→ PDF pp. 203–229 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**5.3 Equivalence of types**  
→ PDF pp. 230–251 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch6"></a>
## Essay: Towards functional data engineering with Scala

*PDF pp. 277–284*

Essay: data engineering as applied mathematics.

*Terms:* functional data engineering, Scala, abstraction

**Data is math**  
→ PDF p. 277 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Functional programming is math**  
→ PDF p. 278 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**The power of abstraction**  
→ PDF p. 279 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Scala is Java on math**  
→ PDF p. 280 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch7"></a>
## 6 Functors and contrafunctors

*PDF pp. 285–348*

Functors and contrafunctors.

*Terms:* functor laws, contrafunctors, profunctors, functor constructions

**6.1 Practical use**  
→ PDF pp. 285–321 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**6.2 Laws and structure**  
→ PDF pp. 322–342 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**6.4 Further developments**  
→ PDF pp. 345–348 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch8"></a>
## 7 Reasoning about code. Techniques of symbolic derivation

*PDF pp. 349–368*

Notation and techniques for deriving code.

*Terms:* code notation, symbolic derivation, equational reasoning

**7.1 This book's notation for code**  
→ PDF pp. 349–356 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**7.2 Derivation techniques**  
→ PDF pp. 357–368 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch9"></a>
## 8 Typeclasses and functions of types

*PDF pp. 369–462*

Typeclasses and type-level functions.

*Terms:* typeclasses, instances, structural derivation, higher-kinded types

**8.1 Motivation and first examples**  
→ PDF pp. 369–371 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**8.2 Implementing typeclasses**  
→ PDF pp. 372–390 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**8.3 Deriving typeclass instances via structural analysis**  
→ PDF pp. 391–429 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**8.5 Further developments**  
→ PDF pp. 444–462 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch10"></a>
## 9 Computations in functor blocks. I. Filterable functors and contrafunctors

*PDF pp. 463–544*

Filterable functors.

*Terms:* filterable functors, withFilter, laws, contrafunctors

**9.1 Practical uses of filtering**  
→ PDF pp. 463–478 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**9.2 Laws and structure**  
→ PDF pp. 479–522 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**9.4 Further developments**  
→ PDF pp. 531–544 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch11"></a>
## 10 Computations in functor blocks. II. Semi-monads and monads

*PDF pp. 545–642*

Semi-monads and monads.

*Terms:* flatMap, monad laws, semi-monads, monad constructions, Kleisli

**10.1 Practical use of monads**  
→ PDF pp. 545–582 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**10.2 Laws of semi-monads and monads**  
→ PDF pp. 583–624 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**10.3 Further developments**  
→ PDF pp. 625–642 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch12"></a>
## 11 Applicative functors and contrafunctors

*PDF pp. 643–734*

Applicative functors and contrafunctors.

*Terms:* applicative laws, zip, map2, applicative profunctors

**11.1 Motivation and first examples**  
→ PDF pp. 643–647 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**11.2 Practical use of applicative functors**  
→ PDF pp. 648–665 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**11.3 Laws and structure of applicative functors**  
→ PDF pp. 666–697 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**11.4 Applicative contrafunctors and profunctors**  
→ PDF pp. 698–719 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch13"></a>
## 12 Traversable functors

*PDF pp. 735–820*

Traversable functors.

*Terms:* foldMap, traverse, traversable laws

**12.1 Motivation**  
→ PDF pp. 735–737 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**12.2 Practical use of folding and traversing operations**  
→ PDF pp. 738–765 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**12.3 Laws and structure**  
→ PDF pp. 766–802 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch14"></a>
## Essay: Software engineers and software artisans

*PDF pp. 821–830*

Essay: programmers as artisans vs. engineers.

*Terms:* software engineering, craft

**Engineering disciplines**  
→ PDF p. 821 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Artisanship: Trades and crafts**  
→ PDF p. 822 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Programmers today are artisans, not engineers**  
→ PDF pp. 822–825 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Towards true engineering in software**  
→ PDF pp. 826–827 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Does software need engineers, or are artisans sufficient?**  
→ PDF pp. 828–830 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch15"></a>
## Essay: Declarative programming as a silver bullet

*PDF pp. 831–842*

Essay: declarative programming and DSLs.

*Terms:* declarative programming, DSL, specification languages

**The silver bullets we know and love**  
→ PDF pp. 831–832 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**What is ``declarative programming''**  
→ PDF pp. 833–835 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Specification languages**  
→ PDF p. 836 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**How to use the silver bullet today: make your own DSL**  
→ PDF pp. 837–838 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Conclusion**  
→ PDF pp. 839–842 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch16"></a>
## 13 Free typeclass constructions

*PDF pp. 843–936*

Free constructions.

*Terms:* free monad, DSL, encodings, free applicative, free functor, laws of free constructions

**13.1 Motivation for the free monad: create a DSL in five stages**  
→ PDF pp. 843–859 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.2 Different encodings of the free monad**  
→ PDF pp. 860–869 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.3 Free constructions for other typeclasses**  
→ PDF pp. 870–883 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.4 Advanced applications**  
→ PDF p. 884 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.5 Laws of free constructions**  
→ PDF pp. 884–906 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.6 Slides**  
→ PDF pp. 907–916 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.7 Properties of free constructions**  
→ PDF pp. 917–920 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.8 Working with quantified types**  
→ PDF pp. 921–931 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**13.9 Discussion**  
→ PDF pp. 932–936 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch17"></a>
## 14 Computations in functor blocks. III. Monad transformers

*PDF pp. 937–1142*

Monad transformers in depth.

*Terms:* monad transformers, laws, composed-inside, composed-outside, linear monads, rigid monads, recursive monads

**14.1 Practical use**  
→ PDF pp. 937–970 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.2 Laws of monad transformers**  
→ PDF pp. 971–991 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.3 Common properties of compositional transformers**  
→ PDF pp. 992–1008 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.4 Composed-inside transformers. Linear monads**  
→ PDF pp. 1009–1018 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.5 Composed-outside transformers. Rigid monads**  
→ PDF pp. 1019–1031 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.6 Transformers for some monad constructions**  
→ PDF pp. 1032–1049 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.7 Transformers for recursive monads**  
→ PDF pp. 1050–1082 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.8 Incomplete transformers**  
→ PDF pp. 1083–1098 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**14.9 Further developments**  
→ PDF pp. 1099–1142 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch18"></a>
## 15 Summary of the book

*PDF pp. 1143–1156*

Summary and open topics.

*Terms:* summary, topics not covered, exercises

**15.1 Main points and results by chapter**  
→ PDF pp. 1143–1144 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**15.2 Topics not covered in this book**  
→ PDF pp. 1145–1146 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**15.3 Additional exercises and problems**  
→ PDF pp. 1147–1156 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch19"></a>
## ``Applied functional type theory'': A proposal

*PDF pp. 1157–1164*

A proposal for “applied functional type theory”.

*Terms:* applied functional type theory, curriculum

**AFTT is not covered by courses in computer science**  
→ PDF pp. 1157–1158 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**AFTT is not category theory, type theory, or formal logic**  
→ PDF pp. 1159–1164 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch20"></a>
## Essay: Why category theory is useful in functional programming

*PDF pp. 1165–1190*

Essay: why category theory helps FP.

*Terms:* category theory, endofunctors, natural transformations

**A ``types/functions'' category for a programming language**  
→ PDF p. 1165 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**The use of endofunctors**  
→ PDF p. 1166 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**The use of natural transformations**  
→ PDF p. 1167 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Other properties of the ``types/functions'' category**  
→ PDF p. 1168 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Some useful sub-categories of endofunctors**  
→ PDF pp. 1169–1170 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**Category theory and the laws of FP idioms**  
→ PDF pp. 1171–1190 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)


---

<a id="ch21"></a>
## C Parametricity theorem and naturality laws

*PDF pp. 1191–1250*

Parametricity and naturality laws.

*Terms:* parametricity, relational parametricity, naturality laws, free theorems

**C.1 Practical use of parametricity properties**  
→ PDF pp. 1194–1201 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

**C.2 Relational formulation of parametricity**  
→ PDF pp. 1202–1250 in [the PDF](https://drive.google.com/file/d/1w6tmvwtlcT0XxiZ98cRwMdww0G8BW3AY/view)

