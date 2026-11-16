<a id="ch1"></a>
# Functional Programming in Lean

> David Thrane Christiansen · Lean FRO, 2023 (CC BY 4.0); this PDF is a browser print of the online book · [the PDF in Drive](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

The PDF is a 347-page print that stops partway through “Programming with Dependent Types” (the online book has 461 printed pages). The tactics interlude and the chapter on programming, proving and performance are therefore missing. Per-chapter “Summary” pages are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An introduction to Lean 4 as a general-purpose functional programming language, for programmers who want to write real programs rather than proofs. It covers expressions, types, structures, inductive datatypes and polymorphism; compiling and running programs with IO and Lake; type classes, coercions and instance search; monads and do-notation; functors, applicative functors and universes; monad transformers and imperative-style do features; and programming with dependent types and indexed families.

**Contents**

1. [Getting to Know Lean](ch1): Lean’s basic language: values, types, functions and data.
2. [Hello, World!](ch2): Writing and running programs with side effects.
3. [Interlude: Propositions, Proofs, and Indexing](ch3): A short introduction to propositions, proofs and safe indexing.
4. [Overloading and Type Classes](ch4): Overloading with type classes.
5. [Monads](ch5): Monads as a common interface for effects.
6. [Functors, Applicative Functors, and Monads](ch6): The hierarchy from Functor to Monad.
7. [Monad Transformers](ch7): Combining effects with monad transformers.
8. [Programming with Dependent Types (partial in this PDF)](ch8): Types that depend on values.


---

## Getting to Know Lean

*PDF pp. 8–66*

Lean’s basic language: values, types, functions and data.

**Evaluating Expressions**  
Evaluating expressions with #eval.  
*Terms:* #eval, expressions  
→ PDF pp. 9–12 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Types**  
Types and type annotations.  
*Terms:* types  
→ PDF pp. 13–14 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Functions and Definitions**  
Defining functions and values.  
*Terms:* def, functions  
→ PDF pp. 15–19 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Structures**  
Structures and their fields.  
*Terms:* structures  
→ PDF pp. 20–27 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Datatypes and Patterns**  
Inductive datatypes and pattern matching.  
*Terms:* inductive types, pattern matching, recursion  
→ PDF pp. 28–35 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Polymorphism**  
Polymorphic functions and datatypes.  
*Terms:* polymorphism, List, Option  
→ PDF pp. 36–50 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Additional Conveniences**  
Implicit arguments, pattern matching shorthands and other conveniences.  
*Terms:* implicit arguments, anonymous constructor  
→ PDF pp. 51–63 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)


---

<a id="ch2"></a>
## Hello, World!

*PDF pp. 67–96*

Writing and running programs with side effects.

**Running a Program**  
The main function and running with lean --run.  
*Terms:* main, IO  
→ PDF pp. 68–72 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Step By Step**  
IO actions step by step.  
*Terms:* IO actions, do  
→ PDF pp. 73–78 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Starting a Project**  
Lake projects and packages.  
*Terms:* Lake, project  
→ PDF pp. 79–82 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Worked Example: cat**  
A cat clone.  
*Terms:* cat, streams  
→ PDF pp. 83–88 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Additional Conveniences**  
Conveniences such as nested actions.  
*Terms:* nested actions  
→ PDF pp. 89–93 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)


---

<a id="ch3"></a>
## Interlude: Propositions, Proofs, and Indexing

*PDF pp. 97–104*

A short introduction to propositions, proofs and safe indexing.

*Terms:* propositions, proofs, decide, simp, array indexing

→ PDF pp. 97–104 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)


---

<a id="ch4"></a>
## Overloading and Type Classes

*PDF pp. 105–157*

Overloading with type classes.

**Positive Numbers**  
Positive numbers as a running example.  
*Terms:* Pos, OfNat  
→ PDF pp. 107–115 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Type Classes and Polymorphism**  
Classes and polymorphic functions.  
*Terms:* type classes, instances  
→ PDF pp. 116–119 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Controlling Instance Search**  
Instance search and output parameters.  
*Terms:* instance search, outParam  
→ PDF pp. 120–124 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Arrays and Indexing**  
Arrays and GetElem indexing.  
*Terms:* Array, GetElem  
→ PDF pp. 125–129 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Standard Classes**  
Standard classes: BEq, Hashable, Ord, Functor and more.  
*Terms:* BEq, Hashable, Ord, Functor  
→ PDF pp. 130–140 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Coercions**  
Coercions.  
*Terms:* Coe, coercions  
→ PDF pp. 141–152 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Additional Conveniences**  
Deriving instances.  
*Terms:* deriving  
→ PDF pp. 153–154 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)


---

<a id="ch5"></a>
## Monads

*PDF pp. 158–210*

Monads as a common interface for effects.

**One API, Many Applications**  
Option, Except, State and logging as one API.  
*Terms:* Option, Except, State, Writer  
→ PDF pp. 158–171 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**The Monad Type Class**  
The Monad class.  
*Terms:* Monad, bind, pure  
→ PDF pp. 172–177 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Example: Arithmetic in Monads**  
Interpreting arithmetic in different monads.  
*Terms:* arithmetic evaluator  
→ PDF pp. 178–195 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**do-Notation for Monads**  
do-notation.  
*Terms:* do-notation  
→ PDF pp. 196–199 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**The IO Monad**  
How IO is a monad.  
*Terms:* IO monad  
→ PDF pp. 200–204 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Additional Conveniences**  
Conveniences.  
*Terms:* conveniences  
→ PDF pp. 205–208 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)


---

<a id="ch6"></a>
## Functors, Applicative Functors, and Monads

*PDF pp. 211–255*

The hierarchy from Functor to Monad.

**Structures and Inheritance**  
Structure inheritance.  
*Terms:* structure inheritance  
→ PDF pp. 212–217 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Applicative Functors**  
Applicative functors.  
*Terms:* Applicative, seq  
→ PDF pp. 218–226 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**The Applicative Contract**  
Applicative laws.  
*Terms:* applicative laws  
→ PDF pp. 227–234 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Alternatives**  
Alternative and failure.  
*Terms:* Alternative, orElse  
→ PDF pp. 235–241 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Universes**  
Universe levels.  
*Terms:* universes, Type u  
→ PDF pp. 242–248 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**The Complete Definitions**  
The full Functor/Applicative/Monad definitions.  
*Terms:* Functor, Applicative, Monad hierarchy  
→ PDF pp. 249–253 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)


---

<a id="ch7"></a>
## Monad Transformers

*PDF pp. 256–305*

Combining effects with monad transformers.

**Combining IO and Reader**  
ReaderT over IO.  
*Terms:* ReaderT  
→ PDF pp. 257–267 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**A Monad Construction Kit**  
OptionT, ExceptT, StateT and friends.  
*Terms:* OptionT, ExceptT, StateT  
→ PDF pp. 268–280 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Ordering Monad Transformers**  
How order of transformers changes behavior.  
*Terms:* transformer ordering  
→ PDF pp. 281–284 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**More do Features**  
Loops, mutable variables and early return in do.  
*Terms:* for loops, mut, return  
→ PDF pp. 285–300 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Additional Conveniences**  
Conveniences.  
*Terms:* conveniences  
→ PDF pp. 301–303 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)


---

<a id="ch8"></a>
## Programming with Dependent Types (partial in this PDF)

*PDF pp. 306–347*

Types that depend on values.

**Indexed Families**  
Indexed families such as length-indexed vectors.  
*Terms:* indexed families, Vect  
→ PDF pp. 308–315 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**The Universe Design Pattern**  
Universes of codes decoded to types.  
*Terms:* universe pattern  
→ PDF pp. 316–324 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Worked Example: Typed Queries**  
A typed query language.  
*Terms:* typed queries, database  
→ PDF pp. 325–345 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

**Indices, Parameters, and Universe Levels**  
When an argument is an index vs. a parameter.  
*Terms:* indices, parameters, universe levels  
→ PDF pp. 346–347 in [the PDF](https://drive.google.com/file/d/1LUhmap5okmULSqrOKLuwniE8cIIPTm9M/view)

