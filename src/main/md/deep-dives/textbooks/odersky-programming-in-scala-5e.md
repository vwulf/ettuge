<a id="ch1"></a>
# Programming in Scala (5th edition, Scala 3)

> Martin Odersky, Lex Spoon, Bill Venners and Frank Sommers · Artima, 2021 · [the PDF in Drive](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

This book is long and granular, so summaries and terms are given per chapter; each section is still listed with its PDF page range. Conclusion sections, the glossary, bibliography and index are not broken out. Chapters also link to the matching pages of the official Scala 3 documentation at docs.scala-lang.org (separate documentation, not the book’s text). Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The standard Scala book by the language’s designer, updated for Scala 3. It introduces the language from the REPL and scripts through classes, objects and basic types, builds functional objects (Rational), and covers control structures, functions and closures, control abstraction, composition and inheritance, traits, packages/imports/exports and pattern matching. It then treats lists and other collections, mutable objects with a circuit-simulation case study, the type hierarchy including union and intersection types, type parameterization and variance, enums and ADTs, abstract members and path-dependent types, and Scala 3’s contextual abstractions: givens, extension methods and typeclasses with derivation-style examples, before a deep tour of the collections library and testing.

**Contents**

1. [A Scalable Language](ch1): Why Scala and what makes it scalable.
2. [First Steps in Scala](ch2): First programs at the REPL and in scripts.
3. [Next Steps in Scala](ch3): Arrays, lists, tuples, sets, maps and functional style.
4. [Classes and Objects](ch4): Classes, singleton objects and case classes.
5. [Basic Types and Operations](ch5): Basic types, literals and operators.
6. [Functional Objects](ch6): Designing an immutable Rational class.
7. [Built-in Control Structures](ch7): if, while, for, try and match as expressions.
8. [Functions and Closures](ch8): Functions and closures.
9. [Control Abstraction](ch9): Building your own control abstractions.
10. [Composition and Inheritance](ch10): Composition vs.
11. [Traits](ch11): Traits.
12. [Packages, Imports, and Exports](ch12): Packages, imports, access and exports.
13. [Pattern Matching](ch13): Pattern matching.
14. [Working with Lists](ch14): Programming with lists.
15. [Working with Other Collections](ch15): Other collections.
16. [Mutable Objects](ch16): Mutable objects and a discrete-event simulation.
17. [Scala's Hierarchy](ch17): The class hierarchy and special types.
18. [Type Parameterization](ch18): Type parameters and variance.
19. [Enums](ch19): Enums and algebraic data types.
20. [Abstract Members](ch20): Abstract members and path-dependent types.
21. [Givens](ch21): Givens and context parameters.
22. [Extension Methods](ch22): Extension methods.
23. [Typeclasses](ch23): Typeclasses in Scala 3.
24. [Collections in Depth](ch24): The collections library in depth.
25. [Assertions and Tests](ch25): Assertions and testing.


---

## A Scalable Language

*PDF pp. 43–60*

Why Scala and what makes it scalable.

Scala 3 docs: [Scala features](https://docs.scala-lang.org/scala3/book/scala-features.html), [Why Scala 3](https://docs.scala-lang.org/scala3/book/why-scala-3.html)

*Terms:* scalability, object-functional, Scala roots, Java interop

**A language that grows on you**  
→ PDF pp. 44–46 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**What makes Scala scalable?**  
→ PDF pp. 47–50 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Why Scala?**  
→ PDF pp. 51–57 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Scala's roots**  
→ PDF p. 58 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch2"></a>
## First Steps in Scala

*PDF pp. 61–73*

First programs at the REPL and in scripts.

Scala 3 docs: [The REPL](https://docs.scala-lang.org/scala3/book/taste-repl.html), [Variables and data types](https://docs.scala-lang.org/scala3/book/taste-vars-data-types.html), [Control structures](https://docs.scala-lang.org/scala3/book/taste-control-structures.html)

*Terms:* REPL, val, var, def, scripts, while, if, foreach, for

**Learn to use the Scala REPL**  
→ PDF pp. 61–62 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Define some variables**  
→ PDF pp. 63–64 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Define some functions**  
→ PDF pp. 65–66 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Write some Scala scripts**  
→ PDF p. 67 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Loop with while; decide with if**  
→ PDF pp. 68–70 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Iterate with foreach and for-do**  
→ PDF pp. 71–72 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch3"></a>
## Next Steps in Scala

*PDF pp. 74–94*

Arrays, lists, tuples, sets, maps and functional style.

Scala 3 docs: [Collections](https://docs.scala-lang.org/scala3/book/taste-collections.html), [Functions](https://docs.scala-lang.org/scala3/book/taste-functions.html)

*Terms:* Array, List, tuples, Set, Map, functional style, map, for-yield

**Parameterize arrays with types**  
→ PDF pp. 74–77 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Use lists**  
→ PDF pp. 78–82 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Use tuples**  
→ PDF p. 83 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Use sets and maps**  
→ PDF pp. 84–87 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Learn to recognize the functional style**  
→ PDF pp. 88–90 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Transform with map and for-yield**  
→ PDF pp. 91–93 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch4"></a>
## Classes and Objects

*PDF pp. 95–107*

Classes, singleton objects and case classes.

Scala 3 docs: [Domain modeling tools](https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html), [Singleton objects](https://docs.scala-lang.org/scala3/book/taste-objects.html)

*Terms:* class, fields, methods, semicolon inference, object, companion, case class, main

**Classes, fields, and methods**  
→ PDF pp. 95–98 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Semicolon inference**  
→ PDF p. 99 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Singleton objects**  
→ PDF pp. 100–102 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Case classes**  
→ PDF pp. 103–104 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**A Scala application**  
→ PDF pp. 105–106 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch5"></a>
## Basic Types and Operations

*PDF pp. 108–128*

Basic types, literals and operators.

Scala 3 docs: [A first look at types](https://docs.scala-lang.org/scala3/book/first-look-at-types.html), [String interpolation](https://docs.scala-lang.org/scala3/book/string-interpolation.html)

*Terms:* Int, String, literals, string interpolation, operators as methods, equality, precedence, rich wrappers

**Some basic types**  
→ PDF p. 108 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Literals**  
→ PDF pp. 109–113 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**String interpolation**  
→ PDF pp. 114–115 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Operators are methods**  
→ PDF pp. 116–118 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Arithmetic operations**  
→ PDF p. 119 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Relational and logical operations**  
→ PDF p. 120 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Bitwise operations**  
→ PDF p. 121 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Object equality**  
→ PDF pp. 122–123 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Operator precedence and associativity**  
→ PDF pp. 124–126 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Rich operations**  
→ PDF p. 127 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch6"></a>
## Functional Objects

*PDF pp. 129–148*

Designing an immutable Rational class.

Scala 3 docs: [OOP modeling](https://docs.scala-lang.org/scala3/book/domain-modeling-oop.html)

*Terms:* Rational, require, auxiliary constructors, operators, identifiers, overloading, extension methods

**A specification for class Rational**  
→ PDF p. 129 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Constructing a Rational**  
→ PDF pp. 130–131 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Reimplementing the toString method**  
→ PDF p. 132 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Checking preconditions**  
→ PDF p. 133 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Adding fields**  
→ PDF pp. 134–135 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Self references**  
→ PDF p. 136 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Auxiliary constructors**  
→ PDF pp. 136–137 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Private fields and methods**  
→ PDF p. 138 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Defining operators**  
→ PDF pp. 139–140 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Identifiers in Scala**  
→ PDF pp. 141–143 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Method overloading**  
→ PDF pp. 144–145 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Extension methods**  
→ PDF p. 146 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**A word of caution**  
→ PDF p. 147 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch7"></a>
## Built-in Control Structures

*PDF pp. 149–171*

if, while, for, try and match as expressions.

Scala 3 docs: [Control structures](https://docs.scala-lang.org/scala3/book/control-structures.html)

*Terms:* if, while, for expressions, try, match, no break/continue, scope

**If expressions**  
→ PDF p. 150 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**While loops**  
→ PDF pp. 151–153 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**For expressions**  
→ PDF pp. 154–158 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Exception handling with try expressions**  
→ PDF pp. 159–162 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Match expressions**  
→ PDF p. 163 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Living without break and continue**  
→ PDF pp. 164–165 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Variable scope**  
→ PDF pp. 166–168 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Refactoring imperative-style code**  
→ PDF pp. 169–170 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch8"></a>
## Functions and Closures

*PDF pp. 172–191*

Functions and closures.

Scala 3 docs: [Anonymous functions](https://docs.scala-lang.org/scala3/book/fun-anonymous-functions.html), [Function variables](https://docs.scala-lang.org/scala3/book/fun-function-variables.html), [Eta expansion](https://docs.scala-lang.org/scala3/book/fun-eta-expansion.html)

*Terms:* local functions, function literals, placeholder syntax, partial application, closures, SAM types, tail recursion

**Methods**  
→ PDF p. 172 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Local functions**  
→ PDF pp. 173–174 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**First-class functions**  
→ PDF p. 175 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Short forms of function literals**  
→ PDF p. 176 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Placeholder syntax**  
→ PDF p. 177 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Partially applied functions**  
→ PDF pp. 178–180 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Closures**  
→ PDF pp. 181–182 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Special function call forms**  
→ PDF pp. 183–185 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**``SAM'' types**  
→ PDF pp. 186–187 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Tail recursion**  
→ PDF pp. 188–190 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch9"></a>
## Control Abstraction

*PDF pp. 192–205*

Building your own control abstractions.

Scala 3 docs: [Higher-order functions](https://docs.scala-lang.org/scala3/book/fun-hofs.html), [Methods returning functions](https://docs.scala-lang.org/scala3/book/fun-write-method-returns-function.html)

*Terms:* higher-order functions, currying, by-name parameters, loan pattern

**Reducing code duplication**  
→ PDF pp. 192–195 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Simplifying client code**  
→ PDF pp. 196–197 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Currying**  
→ PDF p. 198 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Writing new control structures**  
→ PDF pp. 199–201 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**By-name parameters**  
→ PDF pp. 202–203 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch10"></a>
## Composition and Inheritance

*PDF pp. 206–233*

Composition vs. inheritance via a layout library.

Scala 3 docs: [OOP modeling](https://docs.scala-lang.org/scala3/book/domain-modeling-oop.html)

*Terms:* abstract classes, parameterless methods, override, parametric fields, polymorphism, final, factory objects

**A two-dimensional layout library**  
→ PDF p. 206 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Abstract classes**  
→ PDF p. 207 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Defining parameterless methods**  
→ PDF pp. 208–210 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Extending classes**  
→ PDF pp. 211–212 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Overriding methods and fields**  
→ PDF p. 213 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Defining parametric fields**  
→ PDF pp. 214–215 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Invoking superclass constructors**  
→ PDF p. 216 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Using override modifiers**  
→ PDF pp. 217–218 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Polymorphism and dynamic binding**  
→ PDF pp. 219–220 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Declaring final members**  
→ PDF p. 221 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Using composition and inheritance**  
→ PDF pp. 222–223 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Implementing above, beside, and toString**  
→ PDF pp. 224–225 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Defining a factory object**  
→ PDF pp. 226–227 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Heighten and widen**  
→ PDF pp. 228–229 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Putting it all together**  
→ PDF pp. 230–232 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch11"></a>
## Traits

*PDF pp. 234–250*

Traits.

Scala 3 docs: [Domain modeling tools](https://docs.scala-lang.org/scala3/book/domain-modeling-tools.html), [OOP modeling](https://docs.scala-lang.org/scala3/book/domain-modeling-oop.html)

*Terms:* traits, rich interfaces, stackable modifications, linearization, trait parameters

**How traits work**  
→ PDF pp. 234–236 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Thin versus rich interfaces**  
→ PDF pp. 237–238 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Traits as stackable modifications**  
→ PDF pp. 239–242 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Why not multiple inheritance?**  
→ PDF pp. 243–247 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Trait parameters**  
→ PDF pp. 248–249 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch12"></a>
## Packages, Imports, and Exports

*PDF pp. 251–269*

Packages, imports, access and exports.

Scala 3 docs: [Packaging and imports](https://docs.scala-lang.org/scala3/book/packaging-imports.html), [Export clauses](https://docs.scala-lang.org/scala3/reference/other-new-features/export.html)

*Terms:* packages, imports, access modifiers, top-level definitions, export clauses

**Putting code in packages**  
→ PDF p. 251 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Concise access to related code**  
→ PDF pp. 252–255 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Imports**  
→ PDF pp. 256–258 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Implicit imports**  
→ PDF p. 259 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Access modifiers**  
→ PDF pp. 260–264 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Top-level definitions**  
→ PDF p. 265 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Exports**  
→ PDF pp. 266–268 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch13"></a>
## Pattern Matching

*PDF pp. 270–303*

Pattern matching.

Scala 3 docs: [Control structures (match)](https://docs.scala-lang.org/scala3/book/control-structures.html)

*Terms:* patterns, guards, sealed classes, Option, case sequences, expression simplifier

**A simple example**  
→ PDF pp. 270–273 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Kinds of patterns**  
→ PDF pp. 274–283 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Pattern guards**  
→ PDF p. 284 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Pattern overlaps**  
→ PDF pp. 285–286 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Sealed classes**  
→ PDF pp. 287–288 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Pattern matching Options**  
→ PDF pp. 289–290 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Patterns everywhere**  
→ PDF pp. 291–294 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**A larger example**  
→ PDF pp. 295–302 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch14"></a>
## Working with Lists

*PDF pp. 304–334*

Programming with lists.

Scala 3 docs: [Collection types](https://docs.scala-lang.org/scala3/book/collections-classes.html), [Collection methods](https://docs.scala-lang.org/scala3/book/collections-methods.html)

*Terms:* List, cons, list patterns, first-order methods, higher-order methods, foldLeft, type inference

**List literals**  
→ PDF p. 304 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**The List type**  
→ PDF p. 305 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Constructing lists**  
→ PDF p. 305 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Basic operations on lists**  
→ PDF p. 306 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**List patterns**  
→ PDF pp. 307–308 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**First-order methods on class List**  
→ PDF pp. 309–319 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Higher-order methods on class List**  
→ PDF pp. 320–326 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Methods of the List object**  
→ PDF pp. 327–328 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Processing multiple lists together**  
→ PDF pp. 329–330 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Understanding Scala's type inference algorithm**  
→ PDF pp. 331–333 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch15"></a>
## Working with Other Collections

*PDF pp. 335–354*

Other collections.

Scala 3 docs: [Collection types](https://docs.scala-lang.org/scala3/book/collections-classes.html)

*Terms:* Seq, ListBuffer, ArrayBuffer, Set, Map, mutable vs immutable, tuples

**Sequences**  
→ PDF pp. 335–338 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Sets and maps**  
→ PDF pp. 339–345 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Selecting mutable versus immutable collections**  
→ PDF pp. 346–347 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Initializing collections**  
→ PDF pp. 348–350 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Tuples**  
→ PDF pp. 351–352 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch16"></a>
## Mutable Objects

*PDF pp. 355–377*

Mutable objects and a discrete-event simulation.

*Terms:* mutable state, getters and setters, discrete event simulation, digital circuits

**What makes an object mutable?**  
→ PDF pp. 355–356 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Reassignable variables and properties**  
→ PDF pp. 357–360 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Case study: Discrete event simulation**  
→ PDF p. 361 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**A language for digital circuits**  
→ PDF pp. 362–364 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**The Simulation API**  
→ PDF pp. 365–368 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Circuit Simulation**  
→ PDF pp. 369–375 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch17"></a>
## Scala's Hierarchy

*PDF pp. 378–393*

The class hierarchy and special types.

Scala 3 docs: [A first look at types](https://docs.scala-lang.org/scala3/book/first-look-at-types.html), [Intersection types](https://docs.scala-lang.org/scala3/book/types-intersection.html), [Union types](https://docs.scala-lang.org/scala3/book/types-union.html)

*Terms:* Any, AnyVal, AnyRef, Nothing, Null, value classes, intersection types, union types, transparent traits

**Scala's class hierarchy**  
→ PDF pp. 378–381 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**How primitives are implemented**  
→ PDF pp. 382–383 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Bottom types**  
→ PDF p. 384 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Defining your own value classes**  
→ PDF pp. 385–387 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Intersection types**  
→ PDF p. 388 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Union types**  
→ PDF pp. 389–391 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Transparent traits**  
→ PDF p. 392 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch18"></a>
## Type Parameterization

*PDF pp. 394–415*

Type parameters and variance.

Scala 3 docs: [Generics](https://docs.scala-lang.org/scala3/book/types-generics.html), [Variance](https://docs.scala-lang.org/scala3/book/types-variance.html)

*Terms:* generic types, information hiding, variance annotations, covariance, contravariance, lower bounds, upper bounds

**Functional queues**  
→ PDF pp. 394–396 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Information hiding**  
→ PDF pp. 397–399 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Variance annotations**  
→ PDF pp. 400–404 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Checking variance annotations**  
→ PDF pp. 405–407 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Lower bounds**  
→ PDF p. 408 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Contravariance**  
→ PDF pp. 409–412 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Upper bounds**  
→ PDF pp. 413–414 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch19"></a>
## Enums

*PDF pp. 416–427*

Enums and algebraic data types.

Scala 3 docs: [ADTs and GADTs](https://docs.scala-lang.org/scala3/book/types-adts-gadts.html), [Enums (reference)](https://docs.scala-lang.org/scala3/reference/enums/enums.html)

*Terms:* enum, ADTs, GADTs

**Enumerated data types**  
→ PDF pp. 416–419 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Algebraic data types**  
→ PDF pp. 420–421 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Generalized ADTs**  
→ PDF p. 422 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**What makes ADTs algebraic**  
→ PDF pp. 423–426 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch20"></a>
## Abstract Members

*PDF pp. 428–454*

Abstract members and path-dependent types.

Scala 3 docs: [OOP modeling](https://docs.scala-lang.org/scala3/book/domain-modeling-oop.html), [Dependent function types](https://docs.scala-lang.org/scala3/book/types-dependent-function.html)

*Terms:* abstract types, abstract vals, lazy vals, path-dependent types, refinement types

**A quick tour of abstract members**  
→ PDF p. 428 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Type members**  
→ PDF p. 429 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Abstract vals**  
→ PDF p. 430 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Abstract vars**  
→ PDF pp. 430–431 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Initializing abstract vals**  
→ PDF pp. 432–438 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Abstract types**  
→ PDF pp. 439–440 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Path-dependent types**  
→ PDF pp. 441–443 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Refinement types**  
→ PDF p. 444 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Case study: Currencies**  
→ PDF pp. 445–452 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch21"></a>
## Givens

*PDF pp. 455–476*

Givens and context parameters.

Scala 3 docs: [Context parameters](https://docs.scala-lang.org/scala3/book/ca-context-parameters.html), [Given imports](https://docs.scala-lang.org/scala3/book/ca-given-imports.html)

*Terms:* given, using, context parameters, given imports, ambiguity

**How it works**  
→ PDF pp. 455–458 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Parameterized given types**  
→ PDF pp. 459–463 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Anonymous givens**  
→ PDF p. 464 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Parameterized givens as typeclasses**  
→ PDF pp. 465–467 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Given imports**  
→ PDF p. 468 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Rules for context parameters**  
→ PDF pp. 469–471 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**When multiple givens apply**  
→ PDF pp. 472–473 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Debugging givens**  
→ PDF pp. 474–475 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch22"></a>
## Extension Methods

*PDF pp. 477–492*

Extension methods.

Scala 3 docs: [Extension methods](https://docs.scala-lang.org/scala3/book/ca-extension-methods.html)

*Terms:* extension methods, generic extensions, collective extensions, typeclass syntax

**The basics**  
→ PDF pp. 477–479 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Generic extensions**  
→ PDF p. 480 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Collective extensions**  
→ PDF pp. 481–483 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Using a typeclass**  
→ PDF pp. 484–485 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Extension methods for givens**  
→ PDF pp. 486–489 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Where Scala looks for extension methods**  
→ PDF p. 490 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch23"></a>
## Typeclasses

*PDF pp. 493–524*

Typeclasses in Scala 3.

Scala 3 docs: [Type classes](https://docs.scala-lang.org/scala3/book/ca-type-classes.html), [Context bounds](https://docs.scala-lang.org/scala3/book/ca-context-bounds.html), [Multiversal equality](https://docs.scala-lang.org/scala3/book/ca-multiversal-equality.html), [Implicit conversions](https://docs.scala-lang.org/scala3/book/ca-implicit-conversions.html)

*Terms:* typeclasses, context bounds, @main, multiversal equality, CanEqual, implicit conversions, JSON serialization

**Why typeclasses?**  
→ PDF pp. 493–497 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Context bounds**  
→ PDF pp. 498–500 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Main methods**  
→ PDF pp. 501–504 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Multiversal equality**  
→ PDF pp. 505–510 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Implicit conversions**  
→ PDF pp. 511–513 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Typeclass case study: JSON serialization**  
→ PDF pp. 514–522 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch24"></a>
## Collections in Depth

*PDF pp. 525–588*

The collections library in depth.

Scala 3 docs: [Collections overview (2.13+)](https://docs.scala-lang.org/overviews/collections-2.13/introduction.html), [Performance characteristics](https://docs.scala-lang.org/overviews/collections-2.13/performance-characteristics.html)

*Terms:* Iterable, Seq, Set, Map, immutable and mutable collections, Array, String, performance, views, Iterator

**Mutable and immutable collections**  
→ PDF pp. 526–527 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Collections consistency**  
→ PDF pp. 528–529 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Trait Iterable**  
→ PDF pp. 530–536 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**The sequence traits Seq, IndexedSeq, and LinearSeq**  
→ PDF pp. 537–543 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Sets**  
→ PDF pp. 544–547 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Maps**  
→ PDF pp. 548–551 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Concrete immutable collection classes**  
→ PDF pp. 552–558 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Concrete mutable collection classes**  
→ PDF pp. 559–563 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Arrays**  
→ PDF pp. 564–567 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Strings**  
→ PDF p. 568 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Performance characteristics**  
→ PDF pp. 569–570 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Equality**  
→ PDF p. 571 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Views**  
→ PDF pp. 572–575 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Iterators**  
→ PDF pp. 576–583 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Creating collections from scratch**  
→ PDF pp. 584–585 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Conversions between Java and Scala collections**  
→ PDF pp. 586–587 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)


---

<a id="ch25"></a>
## Assertions and Tests

*PDF pp. 589–600*

Assertions and testing.

*Terms:* assert, ensuring, ScalaTest, specifications, property-based testing, ScalaCheck

**Assertions**  
→ PDF pp. 589–590 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Testing in Scala**  
→ PDF p. 591 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Informative failure reports**  
→ PDF pp. 592–593 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Tests as specifications**  
→ PDF pp. 594–596 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Property-based testing**  
→ PDF pp. 597–598 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

**Organizing and running tests**  
→ PDF p. 599 in [the PDF](https://drive.google.com/file/d/1Fb74dzEJ17KaajLtWVRldrzBJfpMqkxd/view)

