<a id="ch1"></a>
# Functional Programming Strategies in Scala with Cats (draft)

> Noel Welsh, building on Scala with Cats by Dave Pereira-Gurnell and Noel Welsh · draft of June 2024, CC BY-SA 4.0 · [the PDF in Drive](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

This free draft has since been superseded by the paid, still-in-progress book “Functional Programming Strategies”; the original Scala with Cats remains free online at scalawithcats.com. Exercise solutions (Part V) are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An expanded rewrite of Scala with Cats that organizes functional programming around reusable “strategies” as well as Cats type classes, using Scala 3. Part I lays foundations: algebraic data types with structural recursion and corecursion, objects as codata, contextual abstraction with givens and type classes, and reified interpreters. Part II is the classic Cats tour: monoids and semigroups, functors (including contravariant and invariant), monads (Id, Either, Eval, Writer, Reader, State, custom), monad transformers, Semigroupal/Applicative and Parallel, Foldable and Traverse. Part III covers indexed types and interpreter optimization down to stack machines, and Part IV keeps the case studies: testing async code, map-reduce, data validation and CRDTs.

**Contents**

1. [Three Levels for Thinking About Code](ch1): Three levels for reasoning about code.
2. [Functional Programming](ch2): What functional programming means here.
3. [Algebraic Data Types](ch3): Modeling data with ADTs and recursion schemes.
4. [Objects as Codata](ch4): Codata: objects defined by what you can do with them.
5. [Contextual Abstraction](ch5): Type classes via Scala 3 contextual abstraction.
6. [Reified Interpreters](ch6): Interpreters by reification.
7. [Using Cats](ch7): Getting started with Cats.
8. [Monoids and Semigroups](ch8): Monoid and Semigroup.
9. [Functors](ch9): Functors and their variants.
10. [Monads](ch10): Monads in Cats.
11. [Monad Transformers](ch11): Stacking monads with transformers.
12. [Semigroupal and Applicative](ch12): Combining independent effects.
13. [Foldable and Traverse](ch13): Folding and traversing.
14. [Indexed Types](ch14): Using types to track state at compile time.
15. [Tagless Final Interpreters](ch15): Tagless final (placeholder in this draft).
16. [Optimizing Interpreters and Compilers](ch16): Making interpreters faster.
17. [Case Study: Testing Asynchronous Code](ch17): Testing async code by abstracting effects.
18. [Case Study: Map-Reduce](ch18): Parallel map-reduce with monoids.
19. [Case Study: Data Validation](ch19): A validation library.
20. [Case Study: CRDTs](ch20): CRDTs via type classes.


---

## Three Levels for Thinking About Code

*PDF pp. 23–24*

Three levels for reasoning about code.

*Terms:* strategies, levels of abstraction, reasoning about code

→ PDF pp. 23–24 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch2"></a>
## Functional Programming

*PDF pp. 25–36*

What functional programming means here.

*Terms:* functional programming, local reasoning, composition, purity

→ PDF pp. 25–36 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch3"></a>
## Algebraic Data Types

*PDF pp. 37–74*

Modeling data with ADTs and recursion schemes.

**Building Algebraic Data Types**  
Products and sums.  
*Terms:* algebraic data types  
→ PDF p. 38 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Algebraic Data Types in Scala**  
Encoding in Scala 3 (enums, case classes).  
*Terms:* enum, case class  
→ PDF pp. 39–44 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Structural Recursion**  
Structural recursion.  
*Terms:* structural recursion, fold  
→ PDF pp. 45–57 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Structural Corecursion**  
Structural corecursion (unfold).  
*Terms:* corecursion, unfold  
→ PDF pp. 58–67 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The Algebra of Algebraic Data Types**  
The algebra of ADTs.  
*Terms:* algebra of types  
→ PDF pp. 68–70 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch4"></a>
## Objects as Codata

*PDF pp. 75–108*

Codata: objects defined by what you can do with them.

**Data and Codata**  
Data vs. codata.  
*Terms:* codata  
→ PDF pp. 76–78 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Codata in Scala**  
Codata as traits/functions.  
*Terms:* traits, functions  
→ PDF pp. 79–81 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Structural Recursion and Corecursion for Codata**  
Recursion and corecursion on codata.  
*Terms:* streams, corecursion  
→ PDF pp. 82–93 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Relating Data and Codata**  
Converting between data and codata.  
*Terms:* church encoding  
→ PDF pp. 94–100 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Data and Codata Extensibility**  
Extensibility trade-offs (expression problem).  
*Terms:* expression problem, extensibility  
→ PDF pp. 101–103 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch5"></a>
## Contextual Abstraction

*PDF pp. 109–138*

Type classes via Scala 3 contextual abstraction.

**The Mechanics of Contextual Abstraction**  
given and using.  
*Terms:* given, using, implicits  
→ PDF pp. 110–117 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Anatomy of a Type Class**  
Anatomy of a type class.  
*Terms:* type class anatomy  
→ PDF pp. 118–123 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Type Class Composition**  
Composing instances.  
*Terms:* instance derivation  
→ PDF pp. 124–125 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**What Type Classes Are**  
What type classes are.  
*Terms:* type classes  
→ PDF pp. 126–127 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Type Classes and Variance**  
Variance and type classes.  
*Terms:* variance  
→ PDF pp. 130–135 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch6"></a>
## Reified Interpreters

*PDF pp. 139–174*

Interpreters by reification.

**Regular Expressions**  
A regular-expression example.  
*Terms:* regular expressions  
→ PDF pp. 140–148 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Interpreters and Reification**  
Reifying programs as data and interpreting them.  
*Terms:* reification, interpreter  
→ PDF pp. 149–151 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Tail Recursive Interpreters**  
Making interpreters tail recursive.  
*Terms:* tail recursion, trampolining  
→ PDF pp. 152–168 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch7"></a>
## Using Cats

*PDF pp. 175–184*

Getting started with Cats.

**Quick Start**  
Quick start.  
*Terms:* Cats setup  
→ PDF p. 175 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Using Cats**  
Imports, instances, syntax.  
*Terms:* imports, syntax  
→ PDF pp. 176–178 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Example: Eq**  
The Eq type class.  
*Terms:* Eq  
→ PDF pp. 179–184 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch8"></a>
## Monoids and Semigroups

*PDF pp. 185–196*

Monoid and Semigroup.

**Definition of a Monoid**  
Monoid laws.  
*Terms:* monoid  
→ PDF p. 187 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Definition of a Semigroup**  
Semigroups.  
*Terms:* semigroup  
→ PDF pp. 188–189 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Monoids in Cats**  
Cats instances and syntax.  
*Terms:* Cats Monoid, |+|  
→ PDF pp. 190–192 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Applications of Monoids**  
Uses: big data, distributed systems.  
*Terms:* applications  
→ PDF p. 193 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch9"></a>
## Functors

*PDF pp. 197–226*

Functors and their variants.

**Examples of Functors**  
Examples: List, Option, Either, Future.  
*Terms:* functor  
→ PDF pp. 197–198 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**More Examples of Functors**  
Function composition as map.  
*Terms:* function composition  
→ PDF pp. 199–203 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Definition of a Functor**  
Definition and laws.  
*Terms:* functor laws  
→ PDF p. 204 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Aside: Higher Kinds and Type Constructors**  
Higher kinds.  
*Terms:* higher-kinded types  
→ PDF pp. 205–206 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Functors in Cats**  
Functor in Cats.  
*Terms:* Cats Functor  
→ PDF pp. 207–210 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Contravariant and Invariant Functors**  
Contravariant and invariant functors.  
*Terms:* contravariant, invariant  
→ PDF pp. 211–217 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Contravariant and Invariant in Cats**  
Cats Contravariant/Invariant.  
*Terms:* contramap, imap  
→ PDF pp. 218–219 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Aside: Partial Unification**  
Partial unification.  
*Terms:* partial unification  
→ PDF pp. 220–223 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch10"></a>
## Monads

*PDF pp. 227–282*

Monads in Cats.

**What is a Monad?**  
Definition and laws.  
*Terms:* monad, flatMap  
→ PDF pp. 227–233 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Monads in Cats**  
Cats Monad and syntax.  
*Terms:* Cats Monad  
→ PDF pp. 234–237 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The Identity Monad**  
Id.  
*Terms:* Id  
→ PDF pp. 238–239 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Either**  
Either.  
*Terms:* Either  
→ PDF pp. 240–246 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Aside: Error Handling and MonadError**  
MonadError.  
*Terms:* MonadError  
→ PDF pp. 247–251 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The Eval Monad**  
Eval for stack safety.  
*Terms:* Eval  
→ PDF pp. 252–259 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The Writer Monad**  
Writer.  
*Terms:* Writer  
→ PDF pp. 260–265 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The Reader Monad**  
Reader.  
*Terms:* Reader  
→ PDF pp. 266–270 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The State Monad**  
State.  
*Terms:* State  
→ PDF pp. 271–277 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Defining Custom Monads**  
Custom monads and tailRecM.  
*Terms:* tailRecM  
→ PDF pp. 278–280 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch11"></a>
## Monad Transformers

*PDF pp. 283–296*

Stacking monads with transformers.

**A Transformative Example**  
A worked example of stacking effects.  
*Terms:* monad composition, example  
→ PDF pp. 285–286 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Monad Transformers in Cats**  
Cats transformers (OptionT, EitherT).  
*Terms:* OptionT, EitherT  
→ PDF pp. 287–293 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch12"></a>
## Semigroupal and Applicative

*PDF pp. 297–316*

Combining independent effects.

**Semigroupal**  
Semigroupal.  
*Terms:* Semigroupal, product  
→ PDF pp. 299–300 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Apply Syntax**  
mapN apply syntax.  
*Terms:* mapN  
→ PDF pp. 301–303 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Semigroupal Applied to Different Types**  
Behavior for different types.  
*Terms:* Either, Future  
→ PDF pp. 304–307 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Parallel**  
Parallel.  
*Terms:* Parallel  
→ PDF pp. 308–310 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Apply and Applicative**  
Apply and Applicative.  
*Terms:* Applicative  
→ PDF pp. 311–313 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch13"></a>
## Foldable and Traverse

*PDF pp. 317–336*

Folding and traversing.

**Foldable**  
Foldable.  
*Terms:* Foldable, foldLeft, foldRight  
→ PDF pp. 317–323 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Traverse**  
Traverse and sequence.  
*Terms:* Traverse, traverse, sequence  
→ PDF pp. 324–331 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch14"></a>
## Indexed Types

*PDF pp. 337–352*

Using types to track state at compile time.

**Phantom Types**  
Phantom types.  
*Terms:* phantom types  
→ PDF pp. 338–340 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Indexed Codata**  
Indexed codata.  
*Terms:* indexed codata  
→ PDF pp. 341–351 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Indexed Data**  
Indexed data (GADTs).  
*Terms:* GADTs  
→ PDF p. 352 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch15"></a>
## Tagless Final Interpreters

*PDF pp. 353–354*

Tagless final (placeholder in this draft).

*Terms:* tagless final

→ PDF pp. 353–354 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch16"></a>
## Optimizing Interpreters and Compilers

*PDF pp. 355–388*

Making interpreters faster.

**Algebraic Manipulation**  
Algebraic simplification.  
*Terms:* algebraic optimization  
→ PDF pp. 355–364 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**From Continuations to Stacks**  
CPS to explicit stacks.  
*Terms:* continuations, stacks  
→ PDF pp. 365–369 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Compilers and Virtual Machines**  
Compiling to a virtual machine.  
*Terms:* compilers, virtual machines  
→ PDF pp. 370–371 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**From Interpreter to Stack Machine**  
From interpreter to stack machine.  
*Terms:* stack machine  
→ PDF pp. 372–380 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch17"></a>
## Case Study: Testing Asynchronous Code

*PDF pp. 389–394*

Testing async code by abstracting effects.

**Abstracting over Type Constructors**  
Abstracting over type constructors.  
*Terms:* higher-kinded abstraction  
→ PDF p. 391 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Abstracting over Monads**  
Abstracting over monads.  
*Terms:* Id for testing  
→ PDF p. 392 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch18"></a>
## Case Study: Map-Reduce

*PDF pp. 395–404*

Parallel map-reduce with monoids.

**Parallelizing map and fold**  
Parallelizing map and fold.  
*Terms:* map-reduce  
→ PDF pp. 395–396 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Implementing foldMap**  
foldMap.  
*Terms:* foldMap  
→ PDF pp. 397–398 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Parallelising foldMap**  
Parallel foldMap.  
*Terms:* parallelism, Future  
→ PDF pp. 399–403 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch19"></a>
## Case Study: Data Validation

*PDF pp. 405–422*

A validation library.

**Sketching the Library Structure**  
Library structure.  
*Terms:* validation  
→ PDF pp. 406–408 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The Check Datatype**  
Check type.  
*Terms:* Check  
→ PDF p. 409 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Basic Combinators**  
Combinators.  
*Terms:* combinators  
→ PDF p. 410 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Transforming Data**  
Transforming data.  
*Terms:* Predicate  
→ PDF pp. 411–416 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Kleislis**  
Kleisli arrows.  
*Terms:* Kleisli  
→ PDF pp. 417–420 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)


---

<a id="ch20"></a>
## Case Study: CRDTs

*PDF pp. 423–436*

CRDTs via type classes.

**Eventual Consistency**  
Eventual consistency.  
*Terms:* eventual consistency  
→ PDF p. 423 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**The GCounter**  
GCounter.  
*Terms:* GCounter  
→ PDF pp. 424–427 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Generalisation**  
Generalizing with bounded semilattices.  
*Terms:* bounded semilattice  
→ PDF pp. 428–430 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Abstracting GCounter to a Type Class**  
A type class.  
*Terms:* type class  
→ PDF pp. 431–432 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

**Abstracting a Key Value Store**  
Key-value stores.  
*Terms:* key-value store  
→ PDF pp. 433–434 in [the PDF](https://drive.google.com/file/d/12qqysiJLSvgCE3RrzPV5KY8YDgg9mDL4/view)

