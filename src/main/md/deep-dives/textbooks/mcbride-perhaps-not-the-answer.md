<a id="ch1"></a>
# Perhaps Not The Answer You Were Expecting But You Asked For It

> Conor McBride · “an accidental blook” of Stack Overflow answers, October 2019 · [the PDF in Drive](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

A compilation of Stack Overflow answers grouped by theme. Each section is one answer, listed under the question it answers; only the chapters are summarized. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Conor McBride (“pigworker” on Stack Overflow) collected his answers into a book. Read in sequence they form an unusual course in typed functional programming: Haskell’s corners, recursion schemes, applicative functors and why they compose when monads do not, the calculus of datatypes (derivatives as one-hole contexts, zippers and comonads), dependently typed programming in Haskell with GADTs, singletons and type families, and finally type theory itself. The tone is playful and the arguments are precise.

**Contents**

1. [Haskell Curiosities](ch1): Short, opinionated answers on Haskell basics and oddities: the unit type, numeric defaulting, ambiguity, folds and monoids, rank-n types, cofree comonads, purely functional editors, and initial algebras for rose trees.
2. [Pattern Matching](ch2): How pattern matching works, from typechecking ML-style patterns to why some patterns are disallowed.
3. [Recursion](ch3): Folds and recursion schemes: paramorphisms, why foldl and foldr differ, lazy infinite structures, and monoidal folds over fixed points.
4. [Applicative Functors](ch4): The applicative-functor answers: how applicatives differ from monads, why they compose, Const and zippy applicatives, applicatives from monoids, and traversals.
5. [Monads](ch5): Monads explained through join, examples of non-composition, the Pause monad, and why zippy colists are not a monad.
6. [Differential Calculus for Types](ch6): McBride’s derivative of a datatype as its type of one-hole contexts: zippers, comonads on grids and trees, traversability, and Naperian (representable) functors.
7. [Dependently Typed Haskell](ch7): Dependent types in Haskell: singletons, data kinds, indexed monads, GADTs, type families, and how Haskell compares with Idris and Agda.
8. [Type Theory](ch8): Answers from type theory proper: containers, equalisers, combinatory logic for intuitionistic type theory, observational type theory, and Coq and Agda practice.


---

## Haskell Curiosities

*PDF pp. 7–48*

Short, opinionated answers on Haskell basics and oddities: the unit type, numeric defaulting, ambiguity, folds and monoids, rank-n types, cofree comonads, purely functional editors, and initial algebras for rose trees.

**What is () in Haskell, exactly?**  
  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**What does () mean in Haskell?**  
  
→ PDF p. 8 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Implement the function lines in Haskell**  
  
→ PDF p. 9 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Boolean Expression evaluation (subtle type error)**  
  
→ PDF p. 9 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Purely functional data structures for text editors**  
  
→ PDF pp. 10–11 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**What are some motivating examples for Cofree CoMonad in Haskell?**  
  
→ PDF pp. 12–14 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Find indices of things in lists**  
  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How do I extend this mergeWords function to any number of strings?**  
  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Example of UndecidableInstances yielding nonterminating typecheck**  
  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why do 3 and x (which was assigned 3) have different inferred types in Haskell?**  
  
→ PDF p. 17 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Use case for rank-3 (or higher) polymorphism?**  
  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why don't Haskell compilers facilitate deterministic memory management?**  
  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How does ArrowLoop work? Also, mfix?**  
  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**What does mean in a type signature?**  
  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Meaning of Double and Floating point?**  
  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Haskell terminology: meaning of type vs. data type, are they synonyms?**  
  
→ PDF p. 22 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Can you formulate the Bubble sort as a monoid or semigroup?**  
  
→ PDF p. 23 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Is this a correctly implemented mergesort in Haskell?**  
  
→ PDF pp. 24–25 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Haskell type system nuances (ambiguity)**  
  
→ PDF p. 26 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Understanding a case of Haskell Type Ambiguity**  
  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why does Haskell use instead of =?**  
  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Is it possible to make a type an instance of a class if its type parameters are in the wrong order?**  
  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Functor type variables for Flip data type**  
  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why does product [] return 1?**  
  
→ PDF p. 30 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Minimum of Two Maybes**  
  
→ PDF p. 30 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Is the equivalent of Haskell's Foldable and Traversable simply a sequence in Clojure?**  
  
→ PDF p. 31 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How do you keep track of multiple properties of a string without traversing it multiple times?**  
  
→ PDF p. 32 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Checking whether a binary tree is a binary search tree**  
  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Finding a leaf with value x in a binary tree**  
  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Taking from a list until encountering a duplicate**  
  
→ PDF p. 34 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**RankNTypes and PolyKinds (quantifier alternation issues)**  
  
→ PDF p. 35 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to write this case expression with the view pattern syntax?**  
  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Recursive Type Families**  
  
→ PDF pp. 36–37 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Determine whether a value is a function in Haskell**  
  
→ PDF p. 38 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Automatic Functor Instance (not)**  
  
→ PDF p. 38 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How do I apply the first partial function that works in Haskell?**  
  
→ PDF p. 39 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**`Zipping' a plain list with a nested list**  
  
→ PDF pp. 39–40 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Bunched accumulations**  
  
→ PDF p. 41 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Functor on Phantom Type**  
  
→ PDF p. 42 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Creating an Interpreter (with store) in Haskell**  
  
→ PDF pp. 43–44 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Existential type wrappers necessity**  
  
→ PDF p. 45 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Non-linear Patterns in Type-Level Functions**  
  
→ PDF p. 46 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Initial algebra for rose trees**  
  
→ PDF pp. 46–48 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)


---

<a id="ch2"></a>
## Pattern Matching

*PDF pp. 49–54*

How pattern matching works, from typechecking ML-style patterns to why some patterns are disallowed.

**Algorithm for typechecking ML-like pattern matching?**  
  
→ PDF p. 49 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Haskell Pattern Matching**  
  
→ PDF p. 50 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Complex pattern matching**  
  
→ PDF p. 51 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to return an element before I entered?**  
  
→ PDF p. 52 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Buzzard Bazooka Zoom**  
  
→ PDF pp. 52–53 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why +–+ is not allowed in pattern matching?**  
  
→ PDF p. 54 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)


---

<a id="ch3"></a>
## Recursion

*PDF pp. 55–68*

Folds and recursion schemes: paramorphisms, why foldl and foldr differ, lazy infinite structures, and monoidal folds over fixed points.

**What are paramorphisms?**  
  
→ PDF p. 55 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why can you reverse list with foldl, but not with foldr in Haskell**  
  
→ PDF pp. 56–58 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Can fold be used to create infinite lists?**  
  
→ PDF p. 59 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How do I give a Functor instance to a datatype built for general recursion schemes?**  
  
→ PDF pp. 59–60 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Are there (term-transforming) morphisms in Haskell?**  
  
→ PDF p. 61 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Is this Fibonacci sequence function recursive?**  
  
→ PDF p. 62 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Can someone explain this lazy Fibonacci solution?**  
  
→ PDF p. 63 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Monoidal folds on fixed points**  
  
→ PDF p. 64 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**List Created Evaluating List Elements**  
  
→ PDF p. 65 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Functions of GADTs**  
  
→ PDF pp. 66–68 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)


---

<a id="ch4"></a>
## Applicative Functors

*PDF pp. 69–94*

The applicative-functor answers: how applicatives differ from monads, why they compose, Const and zippy applicatives, applicatives from monoids, and traversals.

**Where to find programming exercises for applicative functors?**  
  
→ PDF pp. 69–70 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**N-ary tree traversal**  
  
→ PDF pp. 71–75 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Partial application of functions and currying, how to make a better code instead of a lot of maps?**  
  
→ PDF p. 76 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Translating monad to applicative**  
  
→ PDF p. 77 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Applicatives compose, monads don't**  
  
→ PDF p. 78 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Examples Separating Functor, Applicative and Monad**  
  
→ PDF p. 79 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Parsec: Applicatives vs Monads**  
  
→ PDF p. 80 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Refactoring do notation into applicative style**  
  
→ PDF p. 81 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Zip with default values instead of dropping values?**  
  
→ PDF p. 82 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**sum3 with zipWith3 in Haskell**  
  
→ PDF p. 82 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**What is the 'Const' applicative functor useful for?**  
  
→ PDF p. 83 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Applicative instance for free monad**  
  
→ PDF p. 83 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Examples of a monad whose Applicative part can be better optimized than the Monad part**  
  
→ PDF p. 84 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How arbitrary is the “ap” implementation for monads?**  
  
→ PDF p. 85 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Applicative without a functor (for arrays)**  
  
→ PDF p. 85 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Does this simple Haskell function already have a well-known name? (strength)**  
  
→ PDF p. 86 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**The Kids are all Right**  
  
→ PDF p. 87 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why is((,) r) a Functor that is NOT an Applicative?**  
  
→ PDF p. 87 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Applicative Rewriting (for reader)**  
  
→ PDF p. 88 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Serialised Diagonalisation**  
  
→ PDF p. 89 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Applicative style for infix operators?**  
  
→ PDF p. 89 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Where is the Monoid in Applicative?**  
  
→ PDF pp. 89–92 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Applicatives from Monoids including min and max**  
  
→ PDF pp. 93–94 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)


---

<a id="ch5"></a>
## Monads

*PDF pp. 95–104*

Monads explained through join, examples of non-composition, the Pause monad, and why zippy colists are not a monad.

**Why we use monadic functions a mb**  
  
→ PDF p. 95 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Monads with Join instead of Bind**  
  
→ PDF p. 96 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Using return versus not using return in the list monad**  
  
→ PDF p. 97 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Example showing monads don't compose**  
  
→ PDF p. 98 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**The Pause monad**  
  
→ PDF pp. 98–99 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Haskell monad return arbitrary data type**  
  
→ PDF p. 100 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Should I avoid using Monad fail?**  
  
→ PDF p. 100 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why isn't Kleisli an instance of Monoid?**  
  
→ PDF p. 101 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Monads at the prompt?**  
  
→ PDF p. 102 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Is this a case to use liftM?**  
  
→ PDF pp. 102–103 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Zappy colists do not form a monad**  
  
→ PDF p. 104 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Haskell io-streams and forever produces no output to stdout**  
  
→ PDF p. 104 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)


---

<a id="ch6"></a>
## Differential Calculus for Types

*PDF pp. 105–148*

McBride’s derivative of a datatype as its type of one-hole contexts: zippers, comonads on grids and trees, traversability, and Naperian (representable) functors.

**Find the preceding element of an element in list**  
  
→ PDF p. 105 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Splitting a List**  
  
→ PDF pp. 106–107 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**nub as a List Comprehension**  
  
→ PDF p. 108 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to make a binary tree zipper an instance of Comonad?**  
  
→ PDF pp. 109–114 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**What's the absurd function in Data.Void useful for?**  
  
→ PDF pp. 115–116 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Writing cojoin or cobind for n-dimensional grids**  
  
→ PDF pp. 117–121 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Zipper Comonads, Generically**  
  
→ PDF pp. 122–130 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Traversable and zippers: necessity and sufficiency**  
  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to write this (funny filter) function idiomatically?**  
  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Computing a term of a list depending on all previous terms**  
  
→ PDF pp. 132–136 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Reasonable Comonad implementations (for nonempty lists)**  
  
→ PDF pp. 137–139 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Representable (or Naperian) Functors**  
  
→ PDF pp. 140–142 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Tries as Naperian Functors; Matching via their Derivatives**  
  
→ PDF pp. 143–148 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)


---

<a id="ch7"></a>
## Dependently Typed Haskell

*PDF pp. 149–192*

Dependent types in Haskell: singletons, data kinds, indexed monads, GADTs, type families, and how Haskell compares with Idris and Agda.

**Dependently typed language best suited to “real world” programming?**  
  
→ PDF p. 149 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why not be dependently typed?**  
  
→ PDF pp. 149–153 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Simple dependent type example in Haskell for Dummies. How are they useful in practice in Haskell? Why should I care about dependent types ?**  
  
→ PDF p. 154 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Haskell singletons: What do we gain with SNat?**  
  
→ PDF p. 155 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Motivation for limitation on data kind promotion**  
  
→ PDF p. 156 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**What is an indexed monad?**  
  
→ PDF pp. 157–159 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Fixpoints of functors on indexed sets**  
  
→ PDF p. 160 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why is the type system refusing my seemingly valid program?**  
  
→ PDF pp. 161–163 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Is it possible to program and check invarants in Haskell?**  
  
→ PDF pp. 164–165 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why is typecase a bad thing?**  
  
→ PDF p. 166 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why can't I pattern match on a type family?**  
  
→ PDF p. 166 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Positive integer type**  
  
→ PDF p. 167 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Test if a value matches a constructor**  
  
→ PDF p. 168 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Difference between Haskell and Idris: Reflection of Runtime/Compiletime in the type universes**  
  
→ PDF p. 169 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why GADT/existential data constructors cannot be used in lazy patterns?**  
  
→ PDF p. 170 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Can GADTs be used to prove type inequalities in GHC?**  
  
→ PDF p. 171 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Implementing a zipper for length-indexed lists**  
  
→ PDF pp. 171–173 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Monoid for integers modulo**  
  
→ PDF pp. 174–175 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Are there non-trivial Foldable or Traversable instances that don't look like containers?**  
  
→ PDF p. 176 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Are GHC's Type Famlies An Example of System F-omega?**  
  
→ PDF p. 177 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to derive Eq for a GADT with a non-* kinded phantom type parameter**  
  
→ PDF p. 178 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Do all Type Classes in Haskell Have a Category Theoretic Analogue?**  
  
→ PDF p. 179 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Haskell type resolution in Type Classes (Generator, Comonad)**  
  
→ PDF p. 180 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Prove idempotency of type-level disjunction**  
  
→ PDF p. 181 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Recursively defined instances and constraints**  
  
→ PDF pp. 182–183 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How can I get the length of dependently typed interval?**  
  
→ PDF p. 184 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to make catamorphisms work with parameterized/indexed types?**  
  
→ PDF p. 185 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Constraining Constructors in a Signature**  
  
→ PDF p. 186 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Standard name of a sum type like Either but for 3 cases?**  
  
→ PDF p. 187 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to specify the type for a heterogenous collection in a GADT formulated AST?**  
  
→ PDF p. 188 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Type-threaded heterogenous lists and defaulting(?) with type families?**  
  
→ PDF p. 189 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Constructor that lifts (via DataKinds) to A**  
  
→ PDF p. 189 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How should the general type of a ``lemma'' function be understood?**  
  
→ PDF pp. 189–192 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)


---

<a id="ch8"></a>
## Type Theory

*PDF pp. 193–213*

Answers from type theory proper: containers, equalisers, combinatory logic for intuitionistic type theory, observational type theory, and Coq and Agda practice.

**What is the combinatory logic equivalent of intuitionistic type theory?**  
  
→ PDF pp. 193–197 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Do Hask or Agda have equalisers?**  
  
→ PDF pp. 198–199 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Why do we need containers?**  
  
→ PDF pp. 200–203 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**To what extent are Applicative/Monad instances uniquely determined?**  
  
→ PDF pp. 204–205 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Pattern matching in Observational Type Theory**  
  
→ PDF p. 206 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Provable coherence in OTT**  
  
→ PDF p. 207 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**How to solve goals with invalid type equalities in Coq?**  
  
→ PDF pp. 208–209 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Is it possible to express the type of balanced untagged binary trees on the calculus of constructions?**  
  
→ PDF p. 210 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

**Agda-like programming in Coq/Proof General?**  
  
→ PDF pp. 211–213 in [the PDF](https://drive.google.com/file/d/12qqWokXjZCH5qFZf9Zl99SP_QRLtqCLB/view)

