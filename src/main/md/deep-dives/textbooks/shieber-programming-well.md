<a id="ch1"></a>
# Programming Well: Abstraction and Design in Computation

> Stuart M. Shieber · draft textbook for Harvard CS51, © 2025 · [the PDF in Drive](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

PDF page = printed page. The “Supplementary material” notes, problem sets, mathematical background, style guide and exercise solutions at the back are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The textbook for Harvard’s CS51, teaching programming as a design discipline organized around abstraction, using OCaml. It covers expressions and syntax, values and types, naming and scope, functions and currying, structured data and pattern matching, higher-order functions (map, fold, filter), polymorphism, options and exceptions, algebraic and abstract data types with modules and signatures, a substitution-model semantics, complexity and recurrences, mutable state and imperative structures, loops, laziness and streams, objects and inheritance, an environment-model semantics, and concurrency. A final project builds an interpreter for MiniML.

**Contents**

1. [Introduction](ch1): Programming as design, illustrated with GCD.
2. [A Cook's tour of OCaml](ch2): A quick tour of the language.
3. [Expressions and the linguistics of programming languages](ch3): Syntax and how expressions are structured.
4. [Values and types](ch4): Values and static types.
5. [Naming and scope](ch5): let-binding and scope.
6. [Functions](ch6): Functions, recursion and testing.
7. [Structured data and composite types](ch7): Tuples, lists and records.
8. [Higher-order functions and functional programming](ch8): Higher-order functional programming.
9. [Polymorphism and generic programming](ch9): Parametric polymorphism.
10. [Handling anomalous conditions](ch10): Dealing with errors.
11. [Algebraic data types](ch11): Algebraic data types.
12. [Abstract data types and modular programming](ch12): Modules, signatures and abstract data types.
13. [Semantics: The substitution model](ch13): A substitution model of evaluation.
14. [Efficiency, complexity, and recurrences](ch14): Measuring efficiency.
15. [Mutable state and imperative programming](ch15): Mutable state.
16. [Loops and procedural programming](ch16): Loops and procedural style.
17. [Infinite data structures and lazy programming](ch17): Laziness and infinite data.
18. [Extension and object-oriented programming](ch18): Objects and extensibility.
19. [Semantics: The environment model](ch19): An environment model of evaluation.
20. [Concurrency](ch20): Concurrency basics.
21. [Final project: Implementing MiniML](ch21): Building a MiniML interpreter.


---

## Introduction

*PDF pp. 19–28*

Programming as design, illustrated with GCD.

**An extended example: greatest common divisor**  
Developing a GCD function.  
*Terms:* gcd example  
→ PDF pp. 21–23 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Programming as design**  
Design as the core skill.  
*Terms:* design  
→ PDF pp. 24–25 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**The OCaml programming language**  
Why OCaml.  
*Terms:* OCaml  
→ PDF pp. 26–27 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Tools and skills for design**  
Tools for design.  
*Terms:* tools  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch2"></a>
## A Cook's tour of OCaml

*PDF pp. 29–30*

A quick tour of the language.

*Terms:* OCaml overview

→ PDF pp. 29–30 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch3"></a>
## Expressions and the linguistics of programming languages

*PDF pp. 31–40*

Syntax and how expressions are structured.

**Specifying syntactic structure with rules**  
Grammar rules for syntax.  
*Terms:* BNF, grammar  
→ PDF pp. 31–33 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Disambiguating ambiguous expressions**  
Ambiguity, precedence and associativity.  
*Terms:* ambiguity, precedence  
→ PDF pp. 34–35 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Abstract and concrete syntax**  
Abstract vs. concrete syntax.  
*Terms:* abstract syntax  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Expressing your intentions**  
Writing to express intent.  
*Terms:* readability  
→ PDF pp. 37–40 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch4"></a>
## Values and types

*PDF pp. 41–50*

Values and static types.

**OCaml expressions have values**  
Evaluation to values.  
*Terms:* values  
→ PDF pp. 41–43 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**OCaml expressions have types**  
Types and type checking.  
*Terms:* types, type inference  
→ PDF pp. 44–47 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**The unit type**  
unit.  
*Terms:* unit  
→ PDF p. 48 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Functions are themselves values**  
Functions as first-class values.  
*Terms:* first-class functions  
→ PDF pp. 48–50 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch5"></a>
## Naming and scope

*PDF pp. 51–58*

let-binding and scope.

**Variables are names for values**  
Variables name values.  
*Terms:* variables  
→ PDF p. 51 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**The type of a let-bound variable can be inferred**  
Type inference for let.  
*Terms:* inference  
→ PDF p. 52 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**let expressions are expressions**  
let as an expression.  
*Terms:* let-in  
→ PDF p. 52 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Naming to avoid duplication**  
Naming to avoid repetition.  
*Terms:* irredundancy  
→ PDF pp. 53–54 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Scope**  
Lexical scope.  
*Terms:* lexical scope  
→ PDF pp. 55–56 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Global naming and top-level let**  
Top-level definitions.  
*Terms:* top-level let  
→ PDF pp. 57–58 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch6"></a>
## Functions

*PDF pp. 59–76*

Functions, recursion and testing.

**Function application**  
Application.  
*Terms:* application  
→ PDF p. 60 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Multiple arguments and currying**  
Currying.  
*Terms:* currying  
→ PDF p. 61 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Defining anonymous functions**  
fun expressions.  
*Terms:* anonymous functions  
→ PDF p. 62 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Named functions**  
Named functions.  
*Terms:* let functions  
→ PDF pp. 63–66 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Function abstraction and irredundancy**  
Abstraction to remove redundancy.  
*Terms:* abstraction  
→ PDF pp. 67–68 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Defining recursive functions**  
Recursion.  
*Terms:* recursion  
→ PDF pp. 69–71 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Unit testing**  
Unit tests.  
*Terms:* unit testing  
→ PDF pp. 72–75 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch7"></a>
## Structured data and composite types

*PDF pp. 77–94*

Tuples, lists and records.

**Tuples**  
Tuples.  
*Terms:* tuples  
→ PDF pp. 77–78 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Pattern matching for decomposing data structures**  
Pattern matching.  
*Terms:* pattern matching  
→ PDF pp. 79–82 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Lists**  
Lists.  
*Terms:* lists  
→ PDF pp. 83–89 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Records**  
Records.  
*Terms:* records  
→ PDF pp. 90–91 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Comparative summary**  
Comparison.  
*Terms:* comparison  
→ PDF pp. 92–94 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch8"></a>
## Higher-order functions and functional programming

*PDF pp. 95–106*

Higher-order functional programming.

**The map abstraction**  
map.  
*Terms:* map  
→ PDF pp. 95–96 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Partial application**  
Partial application.  
*Terms:* partial application  
→ PDF pp. 97–99 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**The fold abstraction**  
fold.  
*Terms:* fold_left, fold_right  
→ PDF pp. 100–101 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**The filter abstraction**  
filter.  
*Terms:* filter  
→ PDF p. 102 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Credit card numbers and the Luhn check**  
Luhn checksum exercise.  
*Terms:* Luhn algorithm  
→ PDF pp. 103–104 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch9"></a>
## Polymorphism and generic programming

*PDF pp. 107–116*

Parametric polymorphism.

**Polymorphism**  
Polymorphic types.  
*Terms:* polymorphism  
→ PDF p. 108 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Polymorphic map**  
Polymorphic map.  
*Terms:* polymorphic map  
→ PDF p. 109 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Regaining explicit types**  
Annotations.  
*Terms:* type annotations  
→ PDF pp. 110–111 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**The List library**  
The List library.  
*Terms:* List module  
→ PDF p. 112 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Function composition**  
Composition.  
*Terms:* function composition  
→ PDF p. 113 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Weak type variables**  
Weak type variables and the value restriction.  
*Terms:* weak type variables, value restriction  
→ PDF p. 114 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch10"></a>
## Handling anomalous conditions

*PDF pp. 117–136*

Dealing with errors.

**A non-solution: Error values**  
Why sentinel error values fail.  
*Terms:* error values  
→ PDF p. 118 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Option types**  
Option types.  
*Terms:* option  
→ PDF pp. 119–121 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Exceptions**  
Exceptions.  
*Terms:* exceptions  
→ PDF pp. 122–130 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Options or exceptions?**  
Choosing between them.  
*Terms:* option vs exception  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Unit testing with exceptions**  
Testing exceptions.  
*Terms:* testing  
→ PDF pp. 132–133 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch11"></a>
## Algebraic data types

*PDF pp. 137–154*

Algebraic data types.

**Built-in composite types as algebraic types**  
Built-ins as ADTs.  
*Terms:* variant types  
→ PDF p. 139 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Example: Boolean document search**  
Boolean document search.  
*Terms:* document search  
→ PDF pp. 140–145 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Example: Dictionaries**  
Dictionaries.  
*Terms:* dictionaries  
→ PDF pp. 146–148 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Example: Arithmetic expressions**  
Arithmetic expressions.  
*Terms:* expression trees  
→ PDF pp. 149–150 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Binary trees**  
Binary trees.  
*Terms:* binary trees  
→ PDF pp. 151–152 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch12"></a>
## Abstract data types and modular programming

*PDF pp. 155–194*

Modules, signatures and abstract data types.

**Modules**  
Modules.  
*Terms:* modules  
→ PDF p. 158 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**A queue module**  
A queue module.  
*Terms:* queue  
→ PDF pp. 159–161 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Signatures hide extra components**  
Signatures that hide.  
*Terms:* signatures, information hiding  
→ PDF pp. 162–164 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Modules with polymorphic components**  
Polymorphic modules.  
*Terms:* polymorphic modules  
→ PDF p. 165 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Abstract data types and programming for change**  
ADTs and change.  
*Terms:* abstraction barrier  
→ PDF pp. 166–180 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**A dictionary module**  
A dictionary module.  
*Terms:* dictionary  
→ PDF pp. 181–184 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Alternative methods for defining signatures and modules**  
Other ways to define signatures and modules (functors).  
*Terms:* functors, module types  
→ PDF pp. 185–187 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Library Modules**  
Library modules.  
*Terms:* standard library  
→ PDF p. 188 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Image manipulation**  
Image manipulation.  
*Terms:* image processing  
→ PDF p. 189 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: An abstract data type for intervals**  
Intervals ADT.  
*Terms:* intervals  
→ PDF p. 190 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Mobiles**  
Mobiles.  
*Terms:* mobiles  
→ PDF pp. 191–193 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch13"></a>
## Semantics: The substitution model

*PDF pp. 195–222*

A substitution model of evaluation.

**Semantics of arithmetic expressions**  
Arithmetic.  
*Terms:* substitution semantics  
→ PDF pp. 197–200 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Semantics of local naming**  
Local naming.  
*Terms:* let  
→ PDF pp. 201–203 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Defining substitution**  
Defining substitution and free variables.  
*Terms:* free variables, capture  
→ PDF pp. 204–206 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Implementing a substitution semantics**  
Implementing an evaluator.  
*Terms:* interpreter  
→ PDF pp. 207–211 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Semantics of booleans and conditionals**  
Booleans and conditionals.  
*Terms:* conditionals  
→ PDF p. 212 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Semantics of function application**  
Function application.  
*Terms:* beta reduction  
→ PDF pp. 212–217 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Substitution semantics of recursion**  
Recursion.  
*Terms:* recursion  
→ PDF pp. 218–220 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch14"></a>
## Efficiency, complexity, and recurrences

*PDF pp. 223–246*

Measuring efficiency.

**The need for an abstract notion of efficiency**  
Why abstract measures.  
*Terms:* efficiency  
→ PDF p. 224 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Two sorting functions**  
Insertion vs. merge sort.  
*Terms:* sorting  
→ PDF pp. 225–226 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Empirical efficiency**  
Timing experiments.  
*Terms:* empirical timing  
→ PDF pp. 227–228 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Big-O notation**  
Big-O.  
*Terms:* big-O  
→ PDF pp. 229–233 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Recurrence equations**  
Recurrence equations.  
*Terms:* recurrences  
→ PDF pp. 234–245 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Complexity of the Luhn check**  
Luhn complexity.  
*Terms:* complexity  
→ PDF p. 246 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch15"></a>
## Mutable state and imperative programming

*PDF pp. 247–270*

Mutable state.

**References**  
References.  
*Terms:* ref  
→ PDF pp. 249–253 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Other primitive mutable data types**  
Mutable arrays and strings.  
*Terms:* arrays, bytes  
→ PDF p. 254 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**References and mutation**  
Aliasing and mutation.  
*Terms:* aliasing  
→ PDF pp. 255–257 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Mutable lists**  
Mutable lists.  
*Terms:* mutable lists  
→ PDF pp. 258–259 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Imperative queues**  
Imperative queues.  
*Terms:* imperative queues  
→ PDF pp. 260–265 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Hash tables**  
Hash tables.  
*Terms:* hash tables  
→ PDF pp. 266–269 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch16"></a>
## Loops and procedural programming

*PDF pp. 271–284*

Loops and procedural style.

**Loops require impurity**  
Why loops need state.  
*Terms:* loops  
→ PDF p. 272 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Recursion versus iteration**  
Iteration vs. recursion, tail calls.  
*Terms:* tail recursion  
→ PDF pp. 273–274 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Saving data structure space**  
Space savings.  
*Terms:* space  
→ PDF pp. 275–277 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**In-place sorting**  
In-place sorting.  
*Terms:* in-place sort  
→ PDF pp. 278–282 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch17"></a>
## Infinite data structures and lazy programming

*PDF pp. 285–302*

Laziness and infinite data.

**Delaying computation**  
Delaying with thunks.  
*Terms:* delayed computation  
→ PDF pp. 285–286 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Streams**  
Streams.  
*Terms:* streams  
→ PDF pp. 287–290 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Lazy recomputation and thunks**  
Memoized laziness.  
*Terms:* Lazy.t, memoization  
→ PDF pp. 291–293 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Application: Approximating**  
Approximating π and sqrt.  
*Terms:* approximation  
→ PDF pp. 294–295 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Circuits and boolean streams**  
Circuits with boolean streams.  
*Terms:* circuits  
→ PDF p. 296 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**A unit testing framework**  
A test framework.  
*Terms:* testing  
→ PDF pp. 297–300 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**A brief history of laziness**  
History of laziness.  
*Terms:* laziness history  
→ PDF p. 301 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch18"></a>
## Extension and object-oriented programming

*PDF pp. 303–320*

Objects and extensibility.

**Drawing graphical elements**  
Drawing shapes example.  
*Terms:* graphics  
→ PDF pp. 304–307 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Objects introduced**  
Objects.  
*Terms:* objects  
→ PDF pp. 308–310 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Object-oriented terminology and syntax**  
OO terminology.  
*Terms:* methods, classes  
→ PDF pp. 311–312 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Inheritance**  
Inheritance.  
*Terms:* inheritance  
→ PDF pp. 313–315 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Subtyping**  
Subtyping.  
*Terms:* subtyping  
→ PDF pp. 316–318 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Problem section: Object-oriented counters**  
Counters exercise.  
*Terms:* counters  
→ PDF p. 319 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch19"></a>
## Semantics: The environment model

*PDF pp. 321–340*

An environment model of evaluation.

**Review of substitution semantics**  
Review.  
*Terms:* substitution review  
→ PDF p. 321 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Environment semantics**  
Environment semantics.  
*Terms:* environment semantics, closures  
→ PDF pp. 322–330 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Conditionals and booleans**  
Conditionals.  
*Terms:* conditionals  
→ PDF p. 331 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Recursion**  
Recursion and closures.  
*Terms:* recursion  
→ PDF pp. 332–333 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Implementing environment semantics**  
Implementation.  
*Terms:* implementation  
→ PDF p. 334 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Semantics of mutable storage**  
Mutable storage.  
*Terms:* store, mutation  
→ PDF pp. 335–339 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch20"></a>
## Concurrency

*PDF pp. 341–360*

Concurrency basics.

**Sequential, concurrent, and parallel computation**  
Sequential, concurrent, parallel.  
*Terms:* concurrency, parallelism  
→ PDF p. 342 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Dependencies**  
Dependencies.  
*Terms:* dependencies  
→ PDF p. 343 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Threads**  
Threads.  
*Terms:* threads  
→ PDF pp. 344–346 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Interthread communication**  
Communication.  
*Terms:* communication  
→ PDF pp. 347–349 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Futures**  
Futures.  
*Terms:* futures  
→ PDF pp. 350–351 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Futures are not enough**  
Limits of futures.  
*Terms:* limits  
→ PDF pp. 352–355 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Locks**  
Locks.  
*Terms:* locks, mutex  
→ PDF pp. 356–358 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Deadlock**  
Deadlock.  
*Terms:* deadlock  
→ PDF pp. 359–360 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)


---

<a id="ch21"></a>
## Final project: Implementing MiniML

*PDF pp. 361–376*

Building a MiniML interpreter.

**Overview**  
Overview.  
*Terms:* MiniML  
→ PDF pp. 361–362 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Implementing a substitution semantics for MiniML**  
Substitution semantics.  
*Terms:* substitution evaluator  
→ PDF pp. 363–367 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Implementing an environment semantics for MiniML**  
Environment semantics.  
*Terms:* environment evaluator, dynamic scope, lexical scope  
→ PDF pp. 368–370 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Extending the language**  
Extensions.  
*Terms:* extensions  
→ PDF pp. 371–374 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Submitting the project**  
Submission.  
*Terms:* submission  
→ PDF p. 375 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

**Alternative final projects**  
Alternatives.  
*Terms:* alternatives  
→ PDF p. 376 in [the PDF](https://drive.google.com/file/d/1FAELLCIIZ0Fm4_7lwV4PsTy4iotiw-sT/view)

