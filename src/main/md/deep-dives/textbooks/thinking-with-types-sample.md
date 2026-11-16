<a id="ch1"></a>
# Thinking with Types (sample)

> Sandy Maguire · free sample of the book on type-level programming in Haskell · [the PDF in Drive](https://drive.google.com/file/d/1wzl2EFpQ11zOUbpwsg_FcQTZBaKH3J8w/view)

This PDF is the free sample: the introduction and four chapters (1, 2, 4 and 5 of the full book). Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Maguire teaches type-level programming in Haskell as a way to make wrong programs fail to compile. The sample starts with the algebra of types: counting inhabitants, sums, products and exponentials, isomorphisms and the Curry–Howard correspondence. It then explains variance, which decides whether a type can be a Functor, and moves to the practical machinery GHC offers: scoped type variables, type applications, ambiguous types, the Constraint kind, GADTs and a heterogeneous list built with them.

**Contents**

1. [Introduction](ch1): Why type-level programming: types that rule out wrong programs also point toward better designs.
2. [I Fundamentals](ch2): The algebra of types and variance: the foundations the rest of the book builds on.
3. [II Lifting Restrictions](ch3): GHC features that lift the limits of Hindley–Milner: explicit type scoping and application, constraints and GADTs.


---

## Introduction

*PDF pp. 9–14*

Why type-level programming: types that rule out wrong programs also point toward better designs.

→ PDF pp. 9–14 in [the PDF](https://drive.google.com/file/d/1wzl2EFpQ11zOUbpwsg_FcQTZBaKH3J8w/view)


---

<a id="ch2"></a>
## I Fundamentals

*PDF pp. 15–38*

The algebra of types and variance: the foundations the rest of the book builds on.

**The Algebra Behind Types**  
Types have cardinalities, and sum, product and function types behave like addition, multiplication and exponentiation. That gives a way to test types for isomorphism, choose canonical representations, and read Curry–Howard (a worked tic-tac-toe example).  
→ PDF pp. 17–30 in [the PDF](https://drive.google.com/file/d/1wzl2EFpQ11zOUbpwsg_FcQTZBaKH3J8w/view)

**Variance**  
Whether a type constructor is covariant, contravariant or invariant in its parameter depends on where the parameter appears; only covariant ones can be Functors.  
→ PDF pp. 31–38 in [the PDF](https://drive.google.com/file/d/1wzl2EFpQ11zOUbpwsg_FcQTZBaKH3J8w/view)


---

<a id="ch3"></a>
## II Lifting Restrictions

*PDF pp. 39–61*

GHC features that lift the limits of Hindley–Milner: explicit type scoping and application, constraints and GADTs.

**Working with Types**  
Scoped type variables, explicit type applications, and why some types are ambiguous until you apply them.  
→ PDF pp. 41–50 in [the PDF](https://drive.google.com/file/d/1wzl2EFpQ11zOUbpwsg_FcQTZBaKH3J8w/view)

**Constraints and GADTs**  
Constraints are their own kind; type equalities and GADTs let constructors refine types, demonstrated by building a heterogeneous list with Show and Eq instances.  
→ PDF pp. 51–61 in [the PDF](https://drive.google.com/file/d/1wzl2EFpQ11zOUbpwsg_FcQTZBaKH3J8w/view)

