<a id="ch1"></a>
# Category Theory for Programmers (Scala edition)

> Bartosz Milewski, Scala examples by Typelevel contributors · community LaTeX edition, build v36 (2023), CC BY-SA 4.0 · [the PDF in Drive](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view)

PDF page = printed page + 21. This is the latest build of the community PDF (hmemcpy/milewski-ctfp-pdf), which also exists in Haskell-only, OCaml and Reason editions; the Scala edition shows Scala next to the Haskell and C++ code. The same text is online as Bartosz Milewski’s blog series (Haskell and C++ only): each chapter links to its post, and each section links straight to its heading there. “Challenges” and bibliography subsections are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An introduction to category theory aimed at working programmers, told through code. Part One builds the basics from composition: categories, types as sets, Kleisli categories, universal constructions (products, coproducts, exponentials), algebraic data types, functors, bifunctors and profunctors, and natural transformations. Part Two covers limits and colimits, free monoids, representable functors and the Yoneda lemma and embedding. Part Three goes deeper: adjunctions, monads from the programmer’s and the categorical side, comonads, F-algebras and catamorphisms, algebras for monads and lenses, ends and coends, Kan extensions, enriched categories, topoi, Lawvere theories, and monads as monoids in bicategories.

**Contents**

1. [1. Category: The Essence of Composition](ch1): Categories as objects and composable arrows, and why composition matters for programming.
2. [2. Types and Functions](ch2): Types as sets and functions as morphisms.
3. [3. Categories Great and Small](ch3): Small examples of categories.
4. [4. Kleisli Categories](ch4): Embellished functions and the Kleisli category.
5. [5. Products and Coproducts](ch5): Universal constructions: initial, terminal, products, coproducts.
6. [6. Simple Algebraic Data Types](ch6): Algebraic data types as products and sums.
7. [7. Functors](ch7): Functors between categories and in code.
8. [8. Functoriality](ch8): Functors of several arguments and variance.
9. [9. Function Types](ch9): Function objects, currying and cartesian closed categories.
10. [10. Natural Transformations](ch10): Natural transformations and functor categories.
11. [11. Declarative Programming](ch11): Why the categorical, declarative view suits programming and physics.
12. [12. Limits and Colimits](ch12): Limits and colimits as generalized universal constructions.
13. [13. Free Monoids](ch13): Free monoids and the list type.
14. [14. Representable Functors](ch14): Functors isomorphic to hom-functors.
15. [15. The Yoneda Lemma](ch15): The Yoneda lemma.
16. [16. Yoneda Embedding](ch16): Embedding a category in its functor category.
17. [17. It's All About Morphisms](ch17): A restatement of the main ideas in terms of morphisms and hom-sets.
18. [18. Adjunctions](ch18): Adjunctions, two ways.
19. [19. Free/Forgetful Adjunctions](ch19): Free constructions as left adjoints to forgetful functors.
20. [20. Monads: Programmer's Definition](ch20): Monads as programmers meet them.
21. [21. Monads and Effects](ch21): How monads model effects in pure code.
22. [22. Monads Categorically](ch22): Monads as monoids in a category of endofunctors.
23. [23. Comonads](ch23): Comonads and context-dependent computation.
24. [24. F-Algebras](ch24): Recursion schemes through F-algebras.
25. [25. Algebras for Monads](ch25): Algebras for monads and coalgebras for comonads.
26. [26. Ends and Coends](ch26): Ends, coends and profunctors.
27. [27. Kan Extensions](ch27): Kan extensions.
28. [28. Enriched Categories](ch28): Categories whose hom-sets are objects of a monoidal category.
29. [29. Topoi](ch29): Topoi as generalized universes of sets.
30. [30. Lawvere Theories](ch30): Lawvere theories as categorical universal algebra.
31. [31. Monads, Monoids, and Categories](ch31): Monads as monads in bicategories, and categories as monads.


---

## 1. Category: The Essence of Composition

*PDF pp. 22–31* · [read online](https://bartoszmilewski.com/2014/11/04/category-the-essence-of-composition/)

Categories as objects and composable arrows, and why composition matters for programming.

**Arrows as Functions**  
Functions as arrows and their composition.  
*Terms:* arrows, morphisms, composition  
→ PDF pp. 22–24 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/04/category-the-essence-of-composition/#:~:text=Arrows%20as%20Functions,-Is%20this%20already)

**Properties of Composition**  
Associativity and identities.  
*Terms:* associativity, identity  
→ PDF pp. 25–27 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/04/category-the-essence-of-composition/#:~:text=Properties%20of%20Composition,-There%20are%20two)

**Composition is the Essence of Programming**  
Composition as the core of decomposing problems.  
*Terms:* composition, programming  
→ PDF pp. 28–29 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/04/category-the-essence-of-composition/#:~:text=Composition%20is%20the%20Essence%20of%20Programming,-Functional%20programmers%20have)


---

<a id="ch2"></a>
## 2. Types and Functions

*PDF pp. 32–48* · [read online](https://bartoszmilewski.com/2014/11/24/types-and-functions/)

Types as sets and functions as morphisms.

**Who Needs Types?**  
Why static types help.  
*Terms:* static typing  
→ PDF p. 32 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/24/types-and-functions/#:~:text=Who%20Needs%20Types%3F,-There%20seems%20to)

**Types Are About Composability**  
Types make composition checkable.  
*Terms:* composability  
→ PDF pp. 33–34 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/24/types-and-functions/#:~:text=Types%20Are%20About%20Composability,-Category%20theory%20is)

**What Are Types?**  
Types as sets, bottom and partial functions.  
*Terms:* types as sets, bottom  
→ PDF pp. 35–37 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/24/types-and-functions/#:~:text=What%20Are%20Types%3F,-The%20simplest%20intuition)

**Why Do We Need a Mathematical Model?**  
Denotational semantics.  
*Terms:* denotational semantics  
→ PDF pp. 38–40 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/24/types-and-functions/#:~:text=Why%20Do%20We%20Need%20a%20Mathematical%20Model%3F,-As%20a%20programmer)

**Pure and Dirty Functions**  
Pure vs. effectful functions.  
*Terms:* pure functions, side effects  
→ PDF p. 41 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/24/types-and-functions/#:~:text=Pure%20and%20Dirty%20Functions,-The%20things%20we)

**Examples of Types**  
Void, unit, Bool and functions between them.  
*Terms:* Void, unit, Bool, absurd  
→ PDF pp. 42–45 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/11/24/types-and-functions/#:~:text=Examples%20of%20Types,-Once%20you%20realize)


---

<a id="ch3"></a>
## 3. Categories Great and Small

*PDF pp. 49–60* · [read online](https://bartoszmilewski.com/2014/12/05/categories-great-and-small/)

Small examples of categories.

**No Objects**  
The empty category.  
*Terms:* empty category  
→ PDF p. 49 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/05/categories-great-and-small/#:~:text=No%20Objects,-The%20most%20trivial)

**Simple Graphs**  
Free categories from graphs.  
*Terms:* free category, graphs  
→ PDF p. 49 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/05/categories-great-and-small/#:~:text=Simple%20Graphs,-You%20can%20build)

**Orders**  
Preorders, partial and total orders as thin categories.  
*Terms:* preorder, partial order, thin category  
→ PDF p. 50 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/05/categories-great-and-small/#:~:text=Orders,-And%20now%20for)

**Monoid as Set**  
Monoids as sets with an operation.  
*Terms:* monoid  
→ PDF pp. 51–55 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/05/categories-great-and-small/#:~:text=Monoid%20as%20Set,-Monoid%20is%20an)

**Monoid as Category**  
A monoid as a one-object category.  
*Terms:* monoid as category  
→ PDF pp. 56–58 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/05/categories-great-and-small/#:~:text=Monoid%20as%20Category,-That%20was%20the)


---

<a id="ch4"></a>
## 4. Kleisli Categories

*PDF pp. 61–75* · [read online](https://bartoszmilewski.com/2014/12/23/kleisli-categories/)

Embellished functions and the Kleisli category.

**The Writer Category**  
Logging functions that return a value plus a log.  
*Terms:* Writer, logging  
→ PDF pp. 66–68 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/23/kleisli-categories/#:~:text=The%20Writer%20Category,-The%20idea%20of)

**Writer in Haskell**  
Writer in Haskell.  
*Terms:* Writer monad  
→ PDF pp. 69–72 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/23/kleisli-categories/#:~:text=Writer%20in%20Haskell,-The%20same%20thing)

**Kleisli Categories**  
The general Kleisli construction.  
*Terms:* Kleisli category, fish operator  
→ PDF p. 73 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2014/12/23/kleisli-categories/#:~:text=Kleisli%20Categories)


---

<a id="ch5"></a>
## 5. Products and Coproducts

*PDF pp. 76–99* · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/)

Universal constructions: initial, terminal, products, coproducts.

**Initial Object**  
Initial objects (Void).  
*Terms:* initial object, Void  
→ PDF pp. 77–78 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/#:~:text=Initial%20Object,-The%20simplest%20shape)

**Terminal Object**  
Terminal objects (unit).  
*Terms:* terminal object, unit  
→ PDF pp. 79–80 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/#:~:text=Terminal%20Object,-Let%E2%80%99s%20continue%20with)

**Duality**  
Duality and opposite categories.  
*Terms:* duality, opposite category  
→ PDF p. 81 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/#:~:text=Duality,-You%20can%E2%80%99t%20help)

**Isomorphisms**  
Isomorphisms.  
*Terms:* isomorphism  
→ PDF pp. 81–82 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/#:~:text=Isomorphisms,-As%20programmers%20we)

**Products**  
Products via a universal property.  
*Terms:* product, universal property  
→ PDF pp. 83–90 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/#:~:text=Products,-The%20next%20universal)

**Coproduct**  
Coproducts and Either.  
*Terms:* coproduct, sum, Either  
→ PDF pp. 91–94 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/#:~:text=Coproduct,-Like%20every%20construction)

**Asymmetry**  
Why Set is asymmetric.  
*Terms:* asymmetry  
→ PDF pp. 95–97 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/07/products-and-coproducts/#:~:text=Asymmetry,-We%E2%80%99ve%20seen%20two)


---

<a id="ch6"></a>
## 6. Simple Algebraic Data Types

*PDF pp. 100–120* · [read online](https://bartoszmilewski.com/2015/01/13/simple-algebraic-data-types/)

Algebraic data types as products and sums.

**Product Types**  
Tuples and the product monoid.  
*Terms:* product types, tuples  
→ PDF pp. 100–105 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/13/simple-algebraic-data-types/#:~:text=Product%20Types,-The%20canonical%20implementation)

**Records**  
Records.  
*Terms:* records  
→ PDF pp. 106–107 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/13/simple-algebraic-data-types/#:~:text=Records)

**Sum Types**  
Sum types like Maybe and lists.  
*Terms:* sum types, Maybe, List  
→ PDF pp. 108–113 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/13/simple-algebraic-data-types/#:~:text=Sum%20Types,-Just%20as%20the)

**Algebra of Types**  
Type algebra: semiring laws, lists as solutions to equations.  
*Terms:* algebra of types, semiring  
→ PDF pp. 114–118 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/13/simple-algebraic-data-types/#:~:text=Algebra%20of%20Types,-Taken%20separately%20product)


---

<a id="ch7"></a>
## 7. Functors

*PDF pp. 121–148* · [read online](https://bartoszmilewski.com/2015/01/20/functors/)

Functors between categories and in code.

**Functors in Programming**  
Maybe, list, reader as functors; fmap and laws.  
*Terms:* functor, fmap, functor laws, Maybe, Reader  
→ PDF pp. 124–140 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/20/functors/#:~:text=Functors%20in%20Programming,-Let%E2%80%99s%20get%20down)

**Functors as Containers**  
Functors as containers.  
*Terms:* containers  
→ PDF pp. 141–143 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/20/functors/#:~:text=Functors%20as%20Containers,-We%E2%80%99ve%20seen%20some)

**Functor Composition**  
Composing functors.  
*Terms:* functor composition, Cat  
→ PDF pp. 144–147 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/01/20/functors/#:~:text=Functor%20Composition,-It%E2%80%99s%20not%20hard)


---

<a id="ch8"></a>
## 8. Functoriality

*PDF pp. 149–175* · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/)

Functors of several arguments and variance.

**Bifunctors**  
Bifunctors.  
*Terms:* bifunctor  
→ PDF pp. 149–152 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=Bifunctors,-Since%20functors%20are)

**Product and Coproduct Bifunctors**  
Product and Either as bifunctors.  
*Terms:* product, coproduct  
→ PDF pp. 153–154 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=Product%20and%20Coproduct%20Bifunctors,-An%20important%20example)

**Functorial Algebraic Data Types**  
Building functorial ADTs, Const and Identity.  
*Terms:* Const, Identity, deriving Functor  
→ PDF pp. 155–159 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=Functorial%20Algebraic%20Data%20Types,-We%E2%80%99ve%20seen%20several)

**Functors in C++**  
Functors in C++.  
*Terms:* C++ templates  
→ PDF pp. 160–162 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=Functors%20in%20C%2B%2B,-If%20you%20are)

**The Writer Functor**  
Writer as a functor.  
*Terms:* Writer  
→ PDF pp. 163–165 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=The%20Writer%20Functor,-I%20promised%20that)

**Covariant and Contravariant Functors**  
Contravariant functors and op.  
*Terms:* contravariant functor  
→ PDF pp. 166–169 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=Covariant%20and%20Contravariant%20Functors,-Now%20that%20we%E2%80%99ve)

**Profunctors**  
Profunctors.  
*Terms:* profunctor, dimap  
→ PDF pp. 170–172 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=Profunctors,-We%E2%80%99ve%20seen%20that)

**The Hom-Functor**  
The hom-functor.  
*Terms:* hom-functor  
→ PDF p. 173 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/02/03/functoriality/#:~:text=The%20Hom-Functor,-The%20above%20examples)


---

<a id="ch9"></a>
## 9. Function Types

*PDF pp. 176–196* · [read online](https://bartoszmilewski.com/2015/03/13/function-types/)

Function objects, currying and cartesian closed categories.

**Universal Construction**  
The universal construction of a function object.  
*Terms:* function object, eval  
→ PDF pp. 178–182 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/03/13/function-types/#:~:text=Universal%20Construction,-Let%E2%80%99s%20forget%20for)

**Currying**  
Currying.  
*Terms:* currying, uncurry  
→ PDF pp. 183–186 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/03/13/function-types/#:~:text=Currying)

**Exponentials**  
Exponentials.  
*Terms:* exponential  
→ PDF p. 187 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/03/13/function-types/#:~:text=Exponentials,-In%20mathematical%20literature)

**Cartesian Closed Categories**  
Cartesian closed categories.  
*Terms:* cartesian closed category  
→ PDF p. 188 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/03/13/function-types/#:~:text=Cartesian%20Closed%20Categories,-Although%20I%20will)

**Exponentials and Algebraic Data Types**  
Exponent laws as type isomorphisms.  
*Terms:* exponential laws, type isomorphisms  
→ PDF pp. 189–192 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/03/13/function-types/#:~:text=Exponentials%20and%20Algebraic%20Data%20Types,-The%20interpretation%20of)

**Curry-Howard Isomorphism**  
Curry–Howard.  
*Terms:* Curry-Howard isomorphism  
→ PDF pp. 193–195 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/03/13/function-types/#:~:text=Curry-Howard%20Isomorphism,-I%20have%20already)


---

<a id="ch10"></a>
## 10. Natural Transformations

*PDF pp. 197–223* · [read online](https://bartoszmilewski.com/2015/04/07/natural-transformations/)

Natural transformations and functor categories.

**Polymorphic Functions**  
Polymorphic functions as natural transformations; parametricity.  
*Terms:* natural transformation, polymorphism, parametricity, naturality  
→ PDF pp. 201–209 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/07/natural-transformations/#:~:text=Polymorphic%20Functions,-We%20talked%20about)

**Beyond Naturality**  
Naturality beyond functors.  
*Terms:* contravariant  
→ PDF pp. 210–212 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/07/natural-transformations/#:~:text=Beyond%20Naturality,-A%20parametrically%20polymorphic)

**Functor Category**  
Functor categories.  
*Terms:* functor category  
→ PDF pp. 213–216 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/07/natural-transformations/#:~:text=Functor%20Category,-Now%20that%20we)

**2-Categories**  
2-categories and horizontal/vertical composition.  
*Terms:* 2-category, horizontal composition, interchange law  
→ PDF pp. 217–221 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/07/natural-transformations/#:~:text=2-Categories,-With%20that%20out)


---

<a id="ch11"></a>
## 11. Declarative Programming

*PDF pp. 225–232* · [read online](https://bartoszmilewski.com/2015/04/15/category-theory-and-declarative-programming/)

Why the categorical, declarative view suits programming and physics.

*Terms:* declarative programming, universal constructions, composition, physics

→ PDF pp. 225–232 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/15/category-theory-and-declarative-programming/)


---

<a id="ch12"></a>
## 12. Limits and Colimits

*PDF pp. 233–257* · [read online](https://bartoszmilewski.com/2015/04/15/limits-and-colimits/)

Limits and colimits as generalized universal constructions.

**Limit as a Natural Isomorphism**  
Limits as cones and natural isomorphisms.  
*Terms:* limit, cone, diagram  
→ PDF pp. 239–243 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/15/limits-and-colimits/#:~:text=Limit%20as%20a%20Natural%20Isomorphism,-There%20is%20still)

**Examples of Limits**  
Equalizers and pullbacks.  
*Terms:* equalizer, pullback  
→ PDF pp. 244–251 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/15/limits-and-colimits/#:~:text=Examples%20of%20Limits,-We%E2%80%99ve%20seen%20that)

**Colimits**  
Colimits, coequalizers, pushouts.  
*Terms:* colimit, pushout  
→ PDF p. 252 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/15/limits-and-colimits/#:~:text=Colimits,-Just%20like%20all)

**Continuity**  
Continuity of functors.  
*Terms:* continuous functor  
→ PDF pp. 253–255 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/04/15/limits-and-colimits/#:~:text=Continuity,-I%20said%20previously)


---

<a id="ch13"></a>
## 13. Free Monoids

*PDF pp. 258–267* · [read online](https://bartoszmilewski.com/2015/07/21/free-monoids/)

Free monoids and the list type.

**Free Monoid in Haskell**  
Lists as free monoids in Haskell.  
*Terms:* free monoid, list  
→ PDF pp. 260–261 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/07/21/free-monoids/#:~:text=Free%20Monoid%20in%20Haskell,-A%20two%20element)

**Free Monoid Universal Construction**  
The universal property of the free monoid.  
*Terms:* universal construction, forgetful functor  
→ PDF pp. 262–265 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/07/21/free-monoids/#:~:text=Free%20Monoid%20Universal%20Construction,-If%20you%20recall)


---

<a id="ch14"></a>
## 14. Representable Functors

*PDF pp. 268–281* · [read online](https://bartoszmilewski.com/2015/07/29/representable-functors/)

Functors isomorphic to hom-functors.

**The Hom Functor**  
The hom functor.  
*Terms:* hom functor  
→ PDF pp. 269–272 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/07/29/representable-functors/#:~:text=The%20Hom%20Functor,-Every%20category%20comes)

**Representable Functors**  
Representable functors and memoization; streams.  
*Terms:* representable functor, tabulate, index, memoization  
→ PDF pp. 273–279 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/07/29/representable-functors/#:~:text=Representable%20Functors)


---

<a id="ch15"></a>
## 15. The Yoneda Lemma

*PDF pp. 282–293* · [read online](https://bartoszmilewski.com/2015/09/01/the-yoneda-lemma/)

The Yoneda lemma.

**Yoneda in Haskell**  
Yoneda in Haskell: natural transformations from Reader are values.  
*Terms:* Yoneda lemma, Reader  
→ PDF pp. 289–291 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/09/01/the-yoneda-lemma/#:~:text=Yoneda%20in%20Haskell,-We%20have%20already)

**Co-Yoneda**  
The co-Yoneda lemma.  
*Terms:* co-Yoneda  
→ PDF p. 292 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/09/01/the-yoneda-lemma/#:~:text=Co-Yoneda,-As%20usual%20we)


---

<a id="ch16"></a>
## 16. Yoneda Embedding

*PDF pp. 294–303* · [read online](https://bartoszmilewski.com/2015/10/28/yoneda-embedding/)

Embedding a category in its functor category.

**The Embedding**  
The Yoneda embedding.  
*Terms:* Yoneda embedding  
→ PDF p. 296 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/10/28/yoneda-embedding/#:~:text=The%20Embedding,-The%20contravariant%20functor)

**Application to Haskell**  
Application to Haskell (continuation-passing).  
*Terms:* CPS, Haskell  
→ PDF pp. 297–298 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/10/28/yoneda-embedding/#:~:text=Application%20to%20Haskell,-In%20Haskell%20the)

**Preorder Example**  
Preorders.  
*Terms:* preorder  
→ PDF pp. 299–300 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/10/28/yoneda-embedding/#:~:text=Preorder%20Example,-This%20example%20was)

**Naturality**  
Naturality.  
*Terms:* naturality  
→ PDF pp. 301–302 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/10/28/yoneda-embedding/#:~:text=Naturality,-The%20Yoneda%20lemma)


---

<a id="ch17"></a>
## 17. It's All About Morphisms

*PDF pp. 305–312* · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/)

A restatement of the main ideas in terms of morphisms and hom-sets.

**Functors**  
Functors.  
*Terms:* functors  
→ PDF p. 305 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/#:~:text=Functors,-To%20begin%20with)

**Commuting Diagrams**  
Commuting diagrams.  
*Terms:* commuting diagrams  
→ PDF p. 306 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/#:~:text=Commuting%20Diagrams,-A%20lot%20of)

**Natural Transformations**  
Natural transformations.  
*Terms:* natural transformations  
→ PDF pp. 307–308 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/#:~:text=Natural%20Transformations,-In%20general%20natural)

**Natural Isomorphisms**  
Natural isomorphisms.  
*Terms:* natural isomorphism  
→ PDF p. 309 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/#:~:text=Natural%20Isomorphisms,-A%20natural%20isomorphism)

**Hom-Sets**  
Hom-sets.  
*Terms:* hom-set  
→ PDF p. 309 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/#:~:text=Hom-Sets,-But%20what%20are)

**Hom-Set Isomorphisms**  
Hom-set isomorphisms.  
*Terms:* hom-set isomorphism  
→ PDF p. 310 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/#:~:text=Hom-Set%20Isomorphisms,-A%20lot%20of)

**Asymmetry of Hom-Sets**  
Asymmetry of hom-sets.  
*Terms:* asymmetry  
→ PDF p. 311 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2015/11/17/its-all-about-morphisms/#:~:text=Asymmetry%20of%20Hom-Sets,-There%20is%20one)


---

<a id="ch18"></a>
## 18. Adjunctions

*PDF pp. 313–332* · [read online](https://bartoszmilewski.com/2016/04/18/adjunctions/)

Adjunctions, two ways.

**Adjunction and Unit/Counit Pair**  
Unit and counit.  
*Terms:* adjunction, unit, counit  
→ PDF pp. 314–319 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/04/18/adjunctions/#:~:text=Adjunction%20and%20Unit%2FCounit%20Pair,-When%20we%20talk)

**Adjunctions and Hom-Sets**  
Adjunction as a hom-set isomorphism.  
*Terms:* hom-set adjunction  
→ PDF pp. 320–325 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/04/18/adjunctions/#:~:text=Adjunctions%20and%20Hom-Sets,-There%20is%20an)

**Product from Adjunction**  
Products from an adjunction.  
*Terms:* product, diagonal functor  
→ PDF pp. 326–329 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/04/18/adjunctions/#:~:text=Product%20from%20Adjunction,-We%20have%20previously)

**Exponential from Adjunction**  
Exponentials from an adjunction (currying).  
*Terms:* exponential, currying  
→ PDF pp. 330–331 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/04/18/adjunctions/#:~:text=Exponential%20from%20Adjunction)


---

<a id="ch19"></a>
## 19. Free/Forgetful Adjunctions

*PDF pp. 333–340* · [read online](https://bartoszmilewski.com/2016/06/15/freeforgetful-adjunctions/)

Free constructions as left adjoints to forgetful functors.

**Some Intuitions**  
Intuitions for free/forgetful pairs.  
*Terms:* free functor, forgetful functor, free monoid  
→ PDF pp. 337–339 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/06/15/freeforgetful-adjunctions/#:~:text=Some%20Intuitions,-What%20follows%20are)


---

<a id="ch20"></a>
## 20. Monads: Programmer's Definition

*PDF pp. 341–357* · [read online](https://bartoszmilewski.com/2016/11/21/monads-programmers-definition/)

Monads as programmers meet them.

**The Kleisli Category**  
Monads from Kleisli composition.  
*Terms:* monad, Kleisli category  
→ PDF pp. 343–346 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/11/21/monads-programmers-definition/#:~:text=The%20Kleisli%20Category,-We%20have%20previously)

**Fish Anatomy**  
Unpacking the fish into bind and join.  
*Terms:* bind, join, return  
→ PDF pp. 347–350 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/11/21/monads-programmers-definition/#:~:text=Fish%20Anatomy,-When%20implementing%20the)

**The do Notation**  
do-notation.  
*Terms:* do-notation  
→ PDF pp. 351–357 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/11/21/monads-programmers-definition/#:~:text=The%20do%20Notation,-One%20way%20of)


---

<a id="ch21"></a>
## 21. Monads and Effects

*PDF pp. 358–380* · [read online](https://bartoszmilewski.com/2016/11/30/monads-and-effects/)

How monads model effects in pure code.

**The Problem**  
Partiality, nondeterminism, reader, writer, state, exceptions, continuations, IO as problems.  
*Terms:* effects, purity  
→ PDF p. 358 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/11/30/monads-and-effects/#:~:text=The%20Problem)

**The Solution**  
The monadic solutions to each.  
*Terms:* Maybe, List, Reader, Writer, State, Cont, IO monads  
→ PDF pp. 359–378 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/11/30/monads-and-effects/#:~:text=The%20Solution,-First%20let%E2%80%99s%20analyze)


---

<a id="ch22"></a>
## 22. Monads Categorically

*PDF pp. 381–402* · [read online](https://bartoszmilewski.com/2016/12/27/monads-categorically/)

Monads as monoids in a category of endofunctors.

**Monoidal Categories**  
Monoidal categories.  
*Terms:* monoidal category  
→ PDF pp. 386–393 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/12/27/monads-categorically/#:~:text=Monoidal%20Categories,-Let%E2%80%99s%20go%20back)

**Monoid in a Monoidal Category**  
Monoids inside them.  
*Terms:* monoid object  
→ PDF p. 394 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/12/27/monads-categorically/#:~:text=Monoid%20in%20a%20Monoidal%20Category,-We%20are%20now)

**Monads as Monoids**  
Monads as monoids in endofunctors.  
*Terms:* monad as monoid, endofunctor  
→ PDF pp. 395–397 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/12/27/monads-categorically/#:~:text=Monads%20as%20Monoids,-Monoidal%20structures%20pop)

**Monads from Adjunctions**  
Monads arising from adjunctions (State).  
*Terms:* adjunction, State monad  
→ PDF pp. 398–402 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2016/12/27/monads-categorically/#:~:text=Monads%20from%20Adjunctions)


---

<a id="ch23"></a>
## 23. Comonads

*PDF pp. 403–422* · [read online](https://bartoszmilewski.com/2017/01/02/comonads/)

Comonads and context-dependent computation.

**Programming with Comonads**  
Co-Kleisli arrows.  
*Terms:* comonad, co-Kleisli  
→ PDF p. 405 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/01/02/comonads/#:~:text=Programming%20with%20Comonads,-Let%E2%80%99s%20compare%20the)

**The Product Comonad**  
The product (environment) comonad.  
*Terms:* product comonad, environment  
→ PDF pp. 405–406 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/01/02/comonads/#:~:text=The%20Product%20Comonad,-Remember%20the%20reader)

**Dissecting the Composition**  
extract, duplicate, extend.  
*Terms:* extract, duplicate, extend  
→ PDF pp. 407–409 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/01/02/comonads/#:~:text=Dissecting%20the%20Composition,-Continuing%20the%20process)

**The Stream Comonad**  
Streams.  
*Terms:* stream comonad  
→ PDF pp. 410–413 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/01/02/comonads/#:~:text=The%20Stream%20Comonad,-This%20process%20of)

**Comonad Categorically**  
Comonads categorically.  
*Terms:* comonad categorically  
→ PDF pp. 414–417 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/01/02/comonads/#:~:text=Comonad%20Categorically,-Defining%20a%20comonad)

**The Store Comonad**  
Store and its link to lenses.  
*Terms:* Store comonad, lens  
→ PDF pp. 418–421 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/01/02/comonads/#:~:text=The%20Store%20Comonad,-Another%20important%20example)


---

<a id="ch24"></a>
## 24. F-Algebras

*PDF pp. 423–446* · [read online](https://bartoszmilewski.com/2017/02/28/f-algebras/)

Recursion schemes through F-algebras.

**Recursion**  
Expressions and fixed points of functors.  
*Terms:* recursion, Fix  
→ PDF pp. 427–430 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/02/28/f-algebras/#:~:text=Recursion,-One%20way%20to)

**Category of F-Algebras**  
The category of F-algebras.  
*Terms:* F-algebra  
→ PDF pp. 431–433 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/02/28/f-algebras/#:~:text=Category%20of%20F-Algebras,-Here%E2%80%99s%20the%20oldest)

**Natural Numbers**  
Natural numbers as an initial algebra.  
*Terms:* natural numbers, initial algebra, Lambek  
→ PDF pp. 434–435 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/02/28/f-algebras/#:~:text=Natural%20Numbers,-Natural%20numbers%20can)

**Catamorphisms**  
Catamorphisms.  
*Terms:* catamorphism  
→ PDF pp. 436–437 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/02/28/f-algebras/#:~:text=Catamorphisms,-Let%E2%80%99s%20rewrite%20the)

**Folds**  
Folds on lists.  
*Terms:* fold  
→ PDF pp. 438–440 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/02/28/f-algebras/#:~:text=Folds,-A%20list%20of)

**Coalgebras**  
Coalgebras, anamorphisms and streams.  
*Terms:* coalgebra, anamorphism, terminal coalgebra  
→ PDF pp. 441–445 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/02/28/f-algebras/#:~:text=Coalgebras,-As%20usual%20we)


---

<a id="ch25"></a>
## 25. Algebras for Monads

*PDF pp. 447–461* · [read online](https://bartoszmilewski.com/2017/03/14/algebras-for-monads/)

Algebras for monads and coalgebras for comonads.

**T-algebras**  
T-algebras (Eilenberg–Moore).  
*Terms:* T-algebra, Eilenberg-Moore  
→ PDF pp. 450–453 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/14/algebras-for-monads/#:~:text=T-algebras,-Since%20mathematicians%20prefer)

**The Kleisli Category**  
The Kleisli category again.  
*Terms:* Kleisli category  
→ PDF pp. 454–456 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/14/algebras-for-monads/#:~:text=The%20Kleisli%20Category,-We%E2%80%99ve%20seen%20the)

**Coalgebras for Comonads**  
Coalgebras for comonads.  
*Terms:* coalgebra for comonad  
→ PDF p. 457 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/14/algebras-for-monads/#:~:text=Coalgebras%20for%20Comonads,-Analogous%20constructions%20can)

**Lenses**  
Lenses as Store coalgebras.  
*Terms:* lenses  
→ PDF pp. 457–460 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/14/algebras-for-monads/#:~:text=Lenses,-Let%E2%80%99s%20go%20back)


---

<a id="ch26"></a>
## 26. Ends and Coends

*PDF pp. 462–482* · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/)

Ends, coends and profunctors.

**Dinatural Transformations**  
Dinatural transformations.  
*Terms:* dinatural transformation  
→ PDF pp. 464–465 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/#:~:text=Dinatural%20Transformations,-Since%20profunctors%20are)

**Ends**  
Ends.  
*Terms:* end  
→ PDF pp. 466–469 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/#:~:text=Ends,-We%20are%20now)

**Ends as Equalizers**  
Ends as equalizers.  
*Terms:* equalizer  
→ PDF pp. 470–472 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/#:~:text=Ends%20as%20Equalizers,-The%20commutation%20condition)

**Natural Transformations as Ends**  
Natural transformations as ends.  
*Terms:* natural transformations as ends  
→ PDF pp. 473–474 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/#:~:text=Natural%20Transformations%20as%20Ends,-The%20most%20important)

**Coends**  
Coends.  
*Terms:* coend  
→ PDF pp. 475–478 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/#:~:text=Coends,-As%20expected%20the)

**Ninja Yoneda Lemma**  
Ninja Yoneda lemma.  
*Terms:* ninja Yoneda  
→ PDF pp. 479–480 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/#:~:text=Ninja%20Yoneda%20Lemma,-The%20set%20of)

**Profunctor Composition**  
Profunctor composition.  
*Terms:* profunctor composition  
→ PDF pp. 481–482 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/03/29/ends-and-coends/#:~:text=Profunctor%20Composition,-Let%E2%80%99s%20explore%20further)


---

<a id="ch27"></a>
## 27. Kan Extensions

*PDF pp. 483–504* · [read online](https://bartoszmilewski.com/2017/04/17/kan-extensions/)

Kan extensions.

**Right Kan Extension**  
Right Kan extension.  
*Terms:* right Kan extension  
→ PDF pp. 486–487 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/04/17/kan-extensions/#:~:text=Right%20Kan%20Extension,-The%20right%20Kan)

**Kan Extension as Adjunction**  
Kan extensions as adjoints.  
*Terms:* adjunction  
→ PDF pp. 488–489 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/04/17/kan-extensions/#:~:text=Kan%20Extension%20as%20Adjunction,-Now%20suppose%20that)

**Left Kan Extension**  
Left Kan extension.  
*Terms:* left Kan extension  
→ PDF pp. 490–492 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/04/17/kan-extensions/#:~:text=Left%20Kan%20Extension)

**Kan Extensions as Ends**  
Kan extensions as ends and coends.  
*Terms:* ends, coends  
→ PDF pp. 493–495 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/04/17/kan-extensions/#:~:text=Kan%20Extensions%20as%20Ends,-The%20real%20power)

**Kan Extensions in Haskell**  
Ran and Lan in Haskell.  
*Terms:* Ran, Lan, Haskell  
→ PDF pp. 496–500 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/04/17/kan-extensions/#:~:text=Kan%20Extensions%20in%20Haskell,-The%20end%20coend)

**Free Functor**  
The free functor.  
*Terms:* free functor  
→ PDF pp. 501–504 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/04/17/kan-extensions/#:~:text=Free%20Functor,-An%20interesting%20application)


---

<a id="ch28"></a>
## 28. Enriched Categories

*PDF pp. 505–518* · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/)

Categories whose hom-sets are objects of a monoidal category.

**Why Monoidal Category?**  
Motivation.  
*Terms:* enrichment  
→ PDF p. 506 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Why%20Monoidal%20Category%3F,-When%20constructing%20an)

**Monoidal Category**  
Monoidal categories.  
*Terms:* monoidal category  
→ PDF pp. 507–509 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Monoidal%20Category,-We%E2%80%99ve%20talked%20about)

**Enriched Category**  
Enriched categories.  
*Terms:* enriched category  
→ PDF pp. 510–511 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Enriched%20Category)

**Preorders**  
Preorders as enriched over Bool.  
*Terms:* preorders  
→ PDF p. 512 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Preorders,-A%20preorder%20is)

**Metric Spaces**  
Metric spaces as enriched categories.  
*Terms:* Lawvere metric spaces  
→ PDF pp. 513–514 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Metric%20Spaces,-An%20interesting%20example)

**Enriched Functors**  
Enriched functors.  
*Terms:* enriched functors  
→ PDF p. 515 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Enriched%20Functors,-The%20definition%20of)

**Self Enrichment**  
Self-enrichment.  
*Terms:* self-enrichment  
→ PDF pp. 516–517 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Self%20Enrichment,-A%20closed%20symmetric)

**Relation to 2-Categories**  
Relation to 2-categories.  
*Terms:* 2-categories  
→ PDF p. 518 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/05/13/enriched-categories/#:~:text=Relation%20to%202-Categories,-I%20talked%20about)


---

<a id="ch29"></a>
## 29. Topoi

*PDF pp. 519–527* · [read online](https://bartoszmilewski.com/2017/07/22/topoi/)

Topoi as generalized universes of sets.

**Subobject Classifier**  
Subobject classifiers.  
*Terms:* subobject classifier  
→ PDF pp. 520–524 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/07/22/topoi/#:~:text=Subobject%20Classifier,-Let%E2%80%99s%20start%20by)

**Topos**  
Toposes.  
*Terms:* topos  
→ PDF p. 525 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/07/22/topoi/#:~:text=Topos,-A%20topos%20is)

**Topoi and Logic**  
Internal logic of a topos.  
*Terms:* intuitionistic logic  
→ PDF p. 525 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/07/22/topoi/#:~:text=Topoi%20and%20Logic,-In%20set%20theory)


---

<a id="ch30"></a>
## 30. Lawvere Theories

*PDF pp. 528–547* · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/)

Lawvere theories as categorical universal algebra.

**Universal Algebra**  
Universal algebra.  
*Terms:* universal algebra  
→ PDF pp. 528–529 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/#:~:text=Universal%20Algebra,-There%20are%20many)

**Lawvere Theories**  
Lawvere theories.  
*Terms:* Lawvere theory  
→ PDF pp. 530–533 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/#:~:text=Lawvere%20Theories)

**Models of Lawvere Theories**  
Models.  
*Terms:* models  
→ PDF pp. 534–535 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/#:~:text=Models%20of%20Lawvere%20Theories,-The%20key%20to)

**The Theory of Monoids**  
The theory of monoids.  
*Terms:* monoids  
→ PDF p. 536 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/#:~:text=The%20Theory%20of%20Monoids,-The%20simplest%20nontrivial)

**Lawvere Theories and Monads**  
Relation to monads.  
*Terms:* monads  
→ PDF pp. 537–539 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/#:~:text=Lawvere%20Theories%20and%20Monads,-As%20you%20may)

**Monads as Coends**  
Monads as coends.  
*Terms:* coends  
→ PDF pp. 540–543 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/#:~:text=Monads%20as%20Coends,-Let%E2%80%99s%20explore%20the)

**Lawvere Theory of Side Effects**  
Side effects via Lawvere theories.  
*Terms:* algebraic effects  
→ PDF pp. 544–545 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/08/26/lawvere-theories/#:~:text=Lawvere%20Theory%20of%20Side%20Effects,-Since%20there%20is)


---

<a id="ch31"></a>
## 31. Monads, Monoids, and Categories

*PDF pp. 548–558* · [read online](https://bartoszmilewski.com/2017/09/06/monads-monoids-and-categories/)

Monads as monads in bicategories, and categories as monads.

**Bicategories**  
Bicategories.  
*Terms:* bicategory  
→ PDF pp. 548–553 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/09/06/monads-monoids-and-categories/#:~:text=Bicategories,-One%20of%20the)

**Monads**  
Monads in a bicategory; categories as monads in Span.  
*Terms:* monads in a bicategory, spans  
→ PDF pp. 554–557 in [the PDF](https://drive.google.com/file/d/1BiqmUxAfQeSnbV87d1UwP8O9y5_VqV3E/view) · [read online](https://bartoszmilewski.com/2017/09/06/monads-monoids-and-categories/#:~:text=Monads,-By%20now%20you)

