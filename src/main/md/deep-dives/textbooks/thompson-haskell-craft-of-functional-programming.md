<a id="ch1"></a>
# Haskell: The Craft of Functional Programming (3rd edition)

> Simon Thompson · Addison-Wesley 2011; free CC BY-NC-ND PDF, 2023 · [the PDF in Drive](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

PDF page = printed page + 19. This free 2023 PDF is still the current version; the author plans a revised interactive online edition. Exercises and the appendices (imperative vs. functional, glossary, operators, practicalities, GHCi errors, project ideas) are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A first course in functional programming with Haskell that stresses the craft of designing, testing and reasoning about programs rather than language features. Using a running Pictures example and other case studies, it moves from basic types, definitions and recursion through tuples, lists and list comprehensions, I/O with a rock–paper–scissors game, and proof by induction, to higher-order functions and patterns of computation, type classes and type inference, algebraic and abstract data types (Huffman codes, queues, search trees, sets, graphs), lazy and infinite structures with a parsing case study, monads, domain-specific languages including QuickCheck generators, and time and space behaviour.

**Contents**

1. [Introducing functional programming](ch1): What functional programming is, with pictures as an example.
2. [Getting started with Haskell and GHCi](ch2): Using GHC and GHCi.
3. [Basic types and definitions](ch3): Basic types and definitions.
4. [Designing and writing programs](ch4): Designing and writing programs.
5. [Data types, tuples and lists](ch5): Tuples, lists and algebraic types.
6. [Programming with lists](ch6): Programming with lists.
7. [Defining functions over lists](ch7): Defining functions over lists.
8. [Playing the game: I/O in Haskell](ch8): I/O in Haskell.
9. [Reasoning about programs](ch9): Proof about programs.
10. [Generalization: patterns of computation](ch10): Patterns of computation and higher-order functions.
11. [Higher-order functions](ch11): Higher-order functions in depth.
12. [Developing higher-order programs](ch12): Developing higher-order programs.
13. [Overloading, type classes and type checking](ch13): Type classes and type checking.
14. [Algebraic types](ch14): Algebraic data types.
15. [Case study: Huffman codes](ch15): Case study: Huffman coding.
16. [Abstract data types](ch16): Abstract data types.
17. [Lazy programming](ch17): Laziness.
18. [Programming with monads](ch18): Programming with monads.
19. [Domain-Specific Languages](ch19): Domain-specific languages.
20. [Time and space behaviour](ch20): Time and space behaviour.


---

## Introducing functional programming

*PDF pp. 20–45*

What functional programming is, with pictures as an example.

**Computers and modelling**  
Computers and modelling.  
*Terms:* modelling  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**What is a function?**  
Functions.  
*Terms:* function  
→ PDF p. 22 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Pictures and functions**  
Pictures and functions.  
*Terms:* Pictures  
→ PDF p. 23 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Types**  
Types.  
*Terms:* types  
→ PDF pp. 24–25 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The Haskell programming language**  
Haskell.  
*Terms:* Haskell  
→ PDF p. 26 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Expressions and evaluation**  
Expressions and evaluation.  
*Terms:* evaluation  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Definitions**  
Definitions.  
*Terms:* definitions  
→ PDF pp. 28–29 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Function definitions**  
Function definitions.  
*Terms:* function definitions  
→ PDF pp. 30–32 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Types and functional programming**  
Types and FP.  
*Terms:* type checking  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Calculation and evaluation**  
Calculation.  
*Terms:* calculation  
→ PDF p. 34 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The essence of Haskell programming**  
The essence of Haskell programming.  
*Terms:* essence  
→ PDF p. 35 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Domain-specific languages**  
DSLs.  
*Terms:* DSL  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Two models of Pictures**  
Two models of Pictures.  
*Terms:* Pictures models  
→ PDF pp. 37–40 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Tests, properties and proofs**  
Tests, properties and proofs.  
*Terms:* QuickCheck, properties  
→ PDF pp. 41–45 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch2"></a>
## Getting started with Haskell and GHCi

*PDF pp. 46–59*

Using GHC and GHCi.

**A first Haskell program**  
A first program.  
*Terms:* first program  
→ PDF p. 46 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Using Haskell in practice**  
Haskell in practice.  
*Terms:* practice  
→ PDF p. 47 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Using GHCi**  
GHCi.  
*Terms:* GHCi  
→ PDF pp. 48–51 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The standard prelude and the Haskell libraries**  
The Prelude and libraries.  
*Terms:* Prelude  
→ PDF p. 52 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Modules**  
Modules.  
*Terms:* modules  
→ PDF p. 53 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**A second example: pictures**  
Pictures.  
*Terms:* pictures  
→ PDF pp. 54–57 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Errors and error messages**  
Errors.  
*Terms:* error messages  
→ PDF pp. 58–59 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch3"></a>
## Basic types and definitions

*PDF pp. 60–85*

Basic types and definitions.

**The Booleans: Bool**  
Bool.  
*Terms:* Bool  
→ PDF pp. 60–63 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The integers: Integer and Int**  
Integer and Int.  
*Terms:* Integer, Int  
→ PDF pp. 64–65 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Overloading**  
Overloading.  
*Terms:* overloading  
→ PDF p. 66 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Guards**  
Guards.  
*Terms:* guards  
→ PDF pp. 67–70 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Characters and strings**  
Char and String.  
*Terms:* Char, String  
→ PDF pp. 71–74 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Floating-point numbers: Float**  
Float.  
*Terms:* Float  
→ PDF pp. 75–78 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Syntax**  
Syntax and layout.  
*Terms:* layout, syntax  
→ PDF pp. 79–85 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch4"></a>
## Designing and writing programs

*PDF pp. 86–117*

Designing and writing programs.

**Where do I start? Designing a program in Haskell**  
Where to start.  
*Terms:* design  
→ PDF pp. 86–90 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Solving a problem in steps: local definitions**  
Local definitions.  
*Terms:* where, let  
→ PDF pp. 91–97 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Defining types for ourselves: enumerated types**  
Enumerated types.  
*Terms:* enumerated types  
→ PDF pp. 98–99 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Recursion**  
Recursion.  
*Terms:* recursion  
→ PDF pp. 100–103 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Primitive recursion in practice**  
Primitive recursion.  
*Terms:* primitive recursion  
→ PDF pp. 104–106 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Extended exercise: pictures**  
Pictures exercise.  
*Terms:* pictures  
→ PDF pp. 107–108 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**General forms of recursion**  
General recursion.  
*Terms:* general recursion  
→ PDF pp. 109–111 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Program testing**  
Testing.  
*Terms:* testing, QuickCheck  
→ PDF pp. 112–117 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch5"></a>
## Data types, tuples and lists

*PDF pp. 118–143*

Tuples, lists and algebraic types.

**Introducing tuples and lists**  
Introducing tuples and lists.  
*Terms:* tuples, lists  
→ PDF pp. 118–119 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Tuple types**  
Tuple types.  
*Terms:* tuple types  
→ PDF pp. 120–123 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Introducing algebraic types**  
Algebraic types.  
*Terms:* algebraic types  
→ PDF pp. 124–129 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Our approach to lists**  
Approach to lists.  
*Terms:* lists  
→ PDF p. 130 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Lists in Haskell**  
Lists in Haskell.  
*Terms:* list syntax  
→ PDF pp. 130–131 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**List comprehensions**  
List comprehensions.  
*Terms:* list comprehensions  
→ PDF pp. 132–137 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**A library database**  
A library database.  
*Terms:* database example  
→ PDF pp. 138–143 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch6"></a>
## Programming with lists

*PDF pp. 144–179*

Programming with lists.

**Generic functions: polymorphism**  
Polymorphism.  
*Terms:* polymorphism  
→ PDF pp. 144–146 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Haskell list functions in the Prelude**  
Prelude list functions.  
*Terms:* Prelude functions  
→ PDF pp. 147–149 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Finding your way around the Haskell libraries**  
Finding library functions (Hoogle).  
*Terms:* Hoogle  
→ PDF pp. 150–156 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The Picture example: implementation**  
Implementing Pictures.  
*Terms:* Pictures  
→ PDF pp. 157–161 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Extended exercise: alternative implementations of pictures**  
Alternative Pictures.  
*Terms:* alternatives  
→ PDF pp. 162–166 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Extended exercise: positioned pictures**  
Positioned pictures.  
*Terms:* positioned pictures  
→ PDF pp. 167–169 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Extended exercise: supermarket billing**  
Supermarket billing.  
*Terms:* billing  
→ PDF pp. 170–174 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Extended exercise: cards and card games**  
Card games.  
*Terms:* cards  
→ PDF pp. 175–179 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch7"></a>
## Defining functions over lists

*PDF pp. 180–201*

Defining functions over lists.

**Pattern matching revisited**  
Pattern matching.  
*Terms:* pattern matching  
→ PDF pp. 180–181 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Lists and list patterns**  
List patterns.  
*Terms:* list patterns  
→ PDF pp. 182–184 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Primitive recursion over lists**  
Primitive recursion on lists.  
*Terms:* primitive recursion  
→ PDF p. 185 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Finding primitive recursive definitions**  
Finding definitions.  
*Terms:* design  
→ PDF pp. 186–191 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**General recursions over lists**  
General recursion on lists.  
*Terms:* general recursion  
→ PDF pp. 192–194 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Example: text processing**  
Text processing.  
*Terms:* text processing  
→ PDF pp. 195–201 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch8"></a>
## Playing the game: I/O in Haskell

*PDF pp. 202–221*

I/O in Haskell.

**Rock - Paper - Scissors: strategies**  
Rock–paper–scissors strategies.  
*Terms:* strategies  
→ PDF pp. 202–205 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Why is I/O an issue?**  
Why I/O is special.  
*Terms:* purity  
→ PDF p. 206 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The basics of input/output**  
Basic I/O.  
*Terms:* IO  
→ PDF pp. 207–209 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The do notation**  
do notation.  
*Terms:* do notation  
→ PDF pp. 210–213 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Loops and recursion**  
Loops and recursion.  
*Terms:* loops  
→ PDF pp. 214–216 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Rock - Paper - Scissors: playing the game**  
Playing the game.  
*Terms:* game  
→ PDF pp. 217–221 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch9"></a>
## Reasoning about programs

*PDF pp. 222–241*

Proof about programs.

**Understanding definitions**  
Understanding definitions.  
*Terms:* definitions  
→ PDF p. 223 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Testing and proof**  
Testing vs. proof.  
*Terms:* testing, proof  
→ PDF pp. 224–225 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Definedness, termination and finiteness**  
Definedness and termination.  
*Terms:* termination  
→ PDF p. 226 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**A little logic**  
Logic.  
*Terms:* logic  
→ PDF p. 227 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Induction**  
Induction.  
*Terms:* structural induction  
→ PDF pp. 228–231 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Further examples of proofs by induction**  
More induction proofs.  
*Terms:* proofs  
→ PDF pp. 232–236 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Generalizing the proof goal**  
Generalizing goals.  
*Terms:* generalization  
→ PDF pp. 237–241 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch10"></a>
## Generalization: patterns of computation

*PDF pp. 242–259*

Patterns of computation and higher-order functions.

**Patterns of computation over lists**  
Patterns over lists.  
*Terms:* patterns  
→ PDF pp. 243–244 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Higher-order functions: functions as arguments**  
Functions as arguments (map, filter).  
*Terms:* map, filter  
→ PDF pp. 245–250 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Folding and primitive recursion**  
Folding.  
*Terms:* foldr  
→ PDF pp. 251–254 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Generalizing: splitting up lists**  
Splitting lists.  
*Terms:* splitting  
→ PDF pp. 255–256 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Case studies revisited**  
Case studies revisited.  
*Terms:* case studies  
→ PDF pp. 257–259 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch11"></a>
## Higher-order functions

*PDF pp. 260–293*

Higher-order functions in depth.

**Operators: function composition and application**  
Composition and application operators.  
*Terms:* composition, $  
→ PDF pp. 261–264 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Expressions for functions: lambda abstractions**  
Lambda abstractions.  
*Terms:* lambda  
→ PDF pp. 265–267 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Partial application**  
Partial application.  
*Terms:* partial application  
→ PDF pp. 268–271 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Under the hood: curried functions**  
Currying.  
*Terms:* currying  
→ PDF pp. 272–276 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Defining higher-order functions**  
Defining higher-order functions.  
*Terms:* higher-order functions  
→ PDF pp. 277–281 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Verification and general functions**  
Verification of general functions.  
*Terms:* verification  
→ PDF pp. 282–293 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch12"></a>
## Developing higher-order programs

*PDF pp. 294–319*

Developing higher-order programs.

**Revisiting the Picture example**  
Pictures revisited.  
*Terms:* Pictures  
→ PDF pp. 294–297 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Functions as data: strategy combinators**  
Strategy combinators.  
*Terms:* strategy combinators  
→ PDF pp. 298–299 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Functions as data: recognising regular expressions**  
Regular expression recognizers.  
*Terms:* regular expressions  
→ PDF pp. 300–303 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Case studies: functions as data**  
Functions as data.  
*Terms:* functions as data  
→ PDF pp. 304–305 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Example: creating an index**  
Building an index.  
*Terms:* index  
→ PDF pp. 306–312 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Development in practice**  
Development practice.  
*Terms:* development  
→ PDF pp. 313–315 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Understanding programs**  
Understanding programs.  
*Terms:* program understanding  
→ PDF pp. 316–319 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch13"></a>
## Overloading, type classes and type checking

*PDF pp. 320–357*

Type classes and type checking.

**Why overloading?**  
Why overloading.  
*Terms:* overloading  
→ PDF p. 320 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Introducing classes**  
Classes.  
*Terms:* type classes  
→ PDF pp. 321–324 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Signatures and instances**  
Signatures and instances.  
*Terms:* instances  
→ PDF pp. 325–332 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**A tour of the built-in Haskell classes**  
Built-in classes.  
*Terms:* Eq, Ord, Show, Num  
→ PDF pp. 333–341 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Type checking and type inference: an overview**  
Type inference overview.  
*Terms:* type inference  
→ PDF pp. 342–343 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Monomorphic type checking**  
Monomorphic checking.  
*Terms:* monomorphic  
→ PDF pp. 344–345 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Polymorphic type checking**  
Polymorphic checking (unification).  
*Terms:* unification  
→ PDF pp. 346–354 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Type checking and classes**  
Checking with classes.  
*Terms:* class constraints  
→ PDF pp. 355–357 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch14"></a>
## Algebraic types

*PDF pp. 358–393*

Algebraic data types.

**Algebraic type definitions revisited**  
Definitions revisited.  
*Terms:* algebraic types  
→ PDF pp. 359–360 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Recursive algebraic types**  
Recursive types.  
*Terms:* recursive types, trees  
→ PDF pp. 361–368 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Polymorphic algebraic types**  
Polymorphic types.  
*Terms:* polymorphic types  
→ PDF pp. 369–372 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Modelling program errors**  
Modelling errors (Maybe, Either).  
*Terms:* Maybe, Either  
→ PDF pp. 373–376 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Design with algebraic data types**  
Design.  
*Terms:* design  
→ PDF pp. 377–381 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Algebraic types and type classes**  
Types and classes.  
*Terms:* deriving, instances  
→ PDF pp. 382–386 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Reasoning about algebraic types**  
Reasoning about algebraic types.  
*Terms:* structural induction  
→ PDF pp. 387–393 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch15"></a>
## Case study: Huffman codes

*PDF pp. 394–415*

Case study: Huffman coding.

**Modules in Haskell**  
Modules.  
*Terms:* modules  
→ PDF pp. 394–397 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Modular design**  
Modular design.  
*Terms:* modular design  
→ PDF p. 398 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Coding and decoding**  
Coding and decoding.  
*Terms:* encoding  
→ PDF pp. 399–401 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Implementation – I**  
Implementation I.  
*Terms:* implementation  
→ PDF pp. 402–404 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Building Huffman trees**  
Building Huffman trees.  
*Terms:* Huffman trees  
→ PDF p. 405 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Design**  
Design.  
*Terms:* design  
→ PDF pp. 406–407 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Implementation – II**  
Implementation II.  
*Terms:* implementation  
→ PDF pp. 408–415 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch16"></a>
## Abstract data types

*PDF pp. 416–457*

Abstract data types.

**Type representations**  
Representations.  
*Terms:* representation  
→ PDF pp. 416–417 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The Haskell abstract data type mechanism**  
Haskell’s ADT mechanism.  
*Terms:* abstract types, modules  
→ PDF pp. 418–421 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Queues**  
Queues.  
*Terms:* queues  
→ PDF pp. 422–425 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Design**  
Design.  
*Terms:* design  
→ PDF pp. 426–427 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Simulation**  
Simulation.  
*Terms:* simulation  
→ PDF pp. 428–429 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Implementing the simulation**  
Implementing the simulation.  
*Terms:* implementation  
→ PDF pp. 430–433 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Search trees**  
Search trees.  
*Terms:* binary search trees  
→ PDF pp. 434–439 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Sets**  
Sets.  
*Terms:* sets  
→ PDF pp. 440–445 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Relations and graphs**  
Relations and graphs.  
*Terms:* relations, graphs  
→ PDF pp. 446–457 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch17"></a>
## Lazy programming

*PDF pp. 458–505*

Laziness.

**Lazy evaluation**  
Lazy evaluation.  
*Terms:* lazy evaluation  
→ PDF pp. 459–460 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Calculation rules and lazy evaluation**  
Calculation rules.  
*Terms:* calculation rules  
→ PDF pp. 461–463 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**List comprehensions revisited**  
Comprehensions revisited.  
*Terms:* list comprehensions  
→ PDF pp. 464–471 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Data-directed programming**  
Data-directed programming.  
*Terms:* data-directed  
→ PDF pp. 472–475 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Case study: parsing expressions**  
Parsing expressions.  
*Terms:* parser combinators  
→ PDF pp. 476–486 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Infinite lists**  
Infinite lists.  
*Terms:* infinite lists  
→ PDF pp. 487–492 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Why infinite lists?**  
Why infinite lists.  
*Terms:* streams  
→ PDF pp. 493–495 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Case study: simulation**  
Simulation.  
*Terms:* simulation  
→ PDF pp. 496–497 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Proof revisited**  
Proofs revisited.  
*Terms:* proof  
→ PDF pp. 498–505 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch18"></a>
## Programming with monads

*PDF pp. 506–531*

Programming with monads.

**I/O programming**  
I/O programming.  
*Terms:* IO  
→ PDF pp. 506–508 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Further I/O**  
Further I/O.  
*Terms:* files  
→ PDF pp. 509–511 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The calculator**  
A calculator.  
*Terms:* calculator  
→ PDF pp. 512–514 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The do notation revisited**  
do revisited.  
*Terms:* do notation  
→ PDF pp. 515–516 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Monads: languages for functional programming**  
Monads as languages.  
*Terms:* monads  
→ PDF pp. 517–523 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Example: monadic computation over trees**  
Monadic computation over trees.  
*Terms:* State, tree traversal  
→ PDF pp. 524–531 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch19"></a>
## Domain-Specific Languages

*PDF pp. 532–555*

Domain-specific languages.

**Programming languages everywhere**  
Languages everywhere.  
*Terms:* DSL  
→ PDF pp. 532–534 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Why DSLs in Haskell?**  
Why Haskell for DSLs.  
*Terms:* embedding  
→ PDF p. 535 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Shallow and deep Embeddings**  
Shallow vs. deep embeddings.  
*Terms:* shallow, deep embedding  
→ PDF pp. 536–539 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**A DSL for regular expressions**  
A regex DSL.  
*Terms:* regular expressions  
→ PDF pp. 540–544 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Monadic DSLs**  
Monadic DSLs.  
*Terms:* monadic DSL  
→ PDF pp. 545–546 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**DSLs for computation: generating data in QuickCheck**  
QuickCheck generators as a DSL.  
*Terms:* QuickCheck, Gen  
→ PDF pp. 547–552 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Taking it further**  
Further.  
*Terms:* further  
→ PDF pp. 553–555 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)


---

<a id="ch20"></a>
## Time and space behaviour

*PDF pp. 556–581*

Time and space behaviour.

**Complexity of functions**  
Complexity of functions.  
*Terms:* complexity  
→ PDF pp. 556–560 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**The complexity of calculations**  
Complexity of calculations.  
*Terms:* cost  
→ PDF pp. 561–564 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Implementations of sets**  
Set implementations.  
*Terms:* sets  
→ PDF p. 565 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Space behaviour**  
Space behaviour.  
*Terms:* space leaks  
→ PDF pp. 566–568 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Folding revisited**  
Folding revisited (foldl vs foldr).  
*Terms:* foldl, foldr, strictness  
→ PDF pp. 569–575 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

**Avoiding recomputation: memoization**  
Memoization.  
*Terms:* memoization, dynamic programming  
→ PDF pp. 576–581 in [the PDF](https://drive.google.com/file/d/1CkaCtIK52HUPBShoELp57GDXcZ8hZ5w7/view)

