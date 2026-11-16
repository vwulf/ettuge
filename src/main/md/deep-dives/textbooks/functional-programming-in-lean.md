<a id="ch1"></a>
# Functional Programming in Lean

> David Thrane Christiansen · Lean FRO, current online edition (updated through 2025; code tested with recent Lean 4 releases), CC BY 4.0 · [the online book](https://lean-lang.org/functional_programming_in_lean/)

There is no official PDF of this book; it is published as a website. This breakdown follows the current online edition, so every section links to its page there instead of a PDF page range. Per-chapter “Summary” pages are not broken out. Summaries are in our own words.

## The book in one paragraph

An introduction to Lean 4 as a general-purpose functional programming language, for programmers who want to write real programs rather than proofs. It covers expressions, types, structures, inductive datatypes, polymorphism and strings; compiling and running programs with IO and Lake; type classes, coercions and instance search; monads and do-notation; functors, applicative functors and universes; monad transformers and imperative-style do features; programming with dependent types and indexed families; a short course on induction proofs with tactics (including grind); and finally writing fast code that is also proved correct: tail recursion, termination, bounded indices, in-place array mutation and runtime representations.

**Contents**

1. [Getting to Know Lean](ch1): Lean’s basic language: values, types, functions and data.
2. [Hello, World!](ch2): Writing and running programs with side effects.
3. [Interlude: Propositions, Proofs, and Indexing](ch3): A short introduction to propositions, proofs and safe indexing.
4. [Overloading and Type Classes](ch4): Overloading with type classes.
5. [Monads](ch5): Monads as a common interface for effects.
6. [Functors, Applicative Functors, and Monads](ch6): The hierarchy from Functor to Monad.
7. [Monad Transformers](ch7): Combining effects with monad transformers.
8. [Programming with Dependent Types](ch8): Types that depend on values.
9. [Interlude: Tactics, Induction, and Proofs](ch9): Proving things about programs by induction, with tactics.
10. [Programming, Proving, and Performance](ch10): Writing programs that are both fast and proved correct.
11. [Next Steps](ch11): Where to go next.


---

## Getting to Know Lean

Lean’s basic language: values, types, functions and data.

**Evaluating Expressions**  
Evaluating expressions with #eval.  
*Terms:* #eval, expressions  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Evaluating-Expressions/)

**Types**  
Types and type annotations.  
*Terms:* types  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Types/)

**Functions and Definitions**  
Defining functions and values.  
*Terms:* def, functions  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Functions-and-Definitions/)

**Structures**  
Structures and their fields.  
*Terms:* structures  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Structures/)

**Datatypes and Patterns**  
Inductive datatypes and pattern matching.  
*Terms:* inductive types, pattern matching, recursion  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Datatypes-and-Patterns/)

**Polymorphism**  
Polymorphic functions and datatypes.  
*Terms:* polymorphism, List, Option  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Polymorphism/)

**Characters, Strings, and Slices**  
Characters, strings, string slices and matching on them.  
*Terms:* Char, String, slices  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Characters___-Strings___-and-Slices/)

**Additional Conveniences**  
Implicit arguments, pattern-matching shorthands and other conveniences.  
*Terms:* implicit arguments, anonymous constructor  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Getting-to-Know-Lean/Additional-Conveniences/)


---

<a id="ch2"></a>
## Hello, World!

Writing and running programs with side effects.

**Running a Program**  
The main function and running with lean --run.  
*Terms:* main, IO  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Hello___-World___/Running-a-Program/)

**Step By Step**  
IO actions step by step.  
*Terms:* IO actions, do  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Hello___-World___/Step-By-Step/)

**Starting a Project**  
Lake projects and packages.  
*Terms:* Lake, project  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Hello___-World___/Starting-a-Project/)

**Worked Example: cat**  
A cat clone.  
*Terms:* cat, streams  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Hello___-World___/Worked-Example___--cat/)

**Additional Conveniences**  
Conveniences such as nested actions.  
*Terms:* nested actions  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Hello___-World___/Additional-Conveniences/)


---

<a id="ch3"></a>
## Interlude: Propositions, Proofs, and Indexing

A short introduction to propositions, proofs and safe indexing.

*Terms:* propositions, proofs, decide, simp, array indexing

→ [read online](https://lean-lang.org/functional_programming_in_lean/Interlude___-Propositions___-Proofs___-and-Indexing/)


---

<a id="ch4"></a>
## Overloading and Type Classes

Overloading with type classes.

**Positive Numbers**  
Positive numbers as a running example.  
*Terms:* Pos, OfNat  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Overloading-and-Type-Classes/Positive-Numbers/)

**Type Classes and Polymorphism**  
Classes and polymorphic functions.  
*Terms:* type classes, instances  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Overloading-and-Type-Classes/Type-Classes-and-Polymorphism/)

**Controlling Instance Search**  
Instance search and output parameters.  
*Terms:* instance search, outParam  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Overloading-and-Type-Classes/Controlling-Instance-Search/)

**Arrays and Indexing**  
Arrays and GetElem indexing.  
*Terms:* Array, GetElem  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Overloading-and-Type-Classes/Arrays-and-Indexing/)

**Standard Classes**  
Standard classes: BEq, Hashable, Ord, Functor and more.  
*Terms:* BEq, Hashable, Ord, Functor  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Overloading-and-Type-Classes/Standard-Classes/)

**Coercions**  
Coercions.  
*Terms:* Coe, coercions  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Overloading-and-Type-Classes/Coercions/)

**Additional Conveniences**  
Deriving instances.  
*Terms:* deriving  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Overloading-and-Type-Classes/Additional-Conveniences/)


---

<a id="ch5"></a>
## Monads

Monads as a common interface for effects.

**One API, Many Applications**  
Option, Except, State and logging as one API.  
*Terms:* Option, Except, State, Writer  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monads/One-API___-Many-Applications/)

**The Monad Type Class**  
The Monad class.  
*Terms:* Monad, bind, pure  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monads/The-Monad-Type-Class/)

**Example: Arithmetic in Monads**  
Interpreting arithmetic in different monads.  
*Terms:* arithmetic evaluator  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monads/Example___-Arithmetic-in-Monads/)

**do-Notation for Monads**  
do-notation.  
*Terms:* do-notation  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monads/do--Notation-for-Monads/)

**The IO Monad**  
How IO is a monad.  
*Terms:* IO monad  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monads/The-IO-Monad/)

**Additional Conveniences**  
Conveniences.  
*Terms:* conveniences  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monads/Additional-Conveniences/)


---

<a id="ch6"></a>
## Functors, Applicative Functors, and Monads

The hierarchy from Functor to Monad.

**Structures and Inheritance**  
Structure inheritance.  
*Terms:* structure inheritance  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/)

**Applicative Functors**  
Applicative functors.  
*Terms:* Applicative, seq  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Functors___-Applicative-Functors___-and-Monads/Applicative-Functors/)

**The Applicative Contract**  
Applicative laws.  
*Terms:* applicative laws  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Functors___-Applicative-Functors___-and-Monads/The-Applicative-Contract/)

**Alternatives**  
Alternative and failure.  
*Terms:* Alternative, orElse  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Functors___-Applicative-Functors___-and-Monads/Alternatives/)

**Universes**  
Universe levels.  
*Terms:* universes, Type u  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Functors___-Applicative-Functors___-and-Monads/Universes/)

**The Complete Definitions**  
The full Functor/Applicative/Monad definitions.  
*Terms:* Functor, Applicative, Monad hierarchy  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Functors___-Applicative-Functors___-and-Monads/The-Complete-Definitions/)


---

<a id="ch7"></a>
## Monad Transformers

Combining effects with monad transformers.

**Combining IO and Reader**  
ReaderT over IO.  
*Terms:* ReaderT  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monad-Transformers/Combining-IO-and-Reader/)

**A Monad Construction Kit**  
OptionT, ExceptT, StateT and friends.  
*Terms:* OptionT, ExceptT, StateT  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monad-Transformers/A-Monad-Construction-Kit/)

**Ordering Monad Transformers**  
How order of transformers changes behavior.  
*Terms:* transformer ordering  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monad-Transformers/Ordering-Monad-Transformers/)

**More do Features**  
Loops, mutable variables and early return in do.  
*Terms:* for loops, mut, return  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monad-Transformers/More-do-Features/)

**Additional Conveniences**  
Conveniences.  
*Terms:* conveniences  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Monad-Transformers/Additional-Conveniences/)


---

<a id="ch8"></a>
## Programming with Dependent Types

Types that depend on values.

**Indexed Families**  
Indexed families such as length-indexed vectors.  
*Terms:* indexed families, Vect  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming-with-Dependent-Types/Indexed-Families/)

**The Universe Design Pattern**  
Universes of codes decoded to types.  
*Terms:* universe pattern  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming-with-Dependent-Types/The-Universe-Design-Pattern/)

**Worked Example: Typed Queries**  
A typed query language.  
*Terms:* typed queries, database  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming-with-Dependent-Types/Worked-Example___-Typed-Queries/)

**Indices, Parameters, and Universe Levels**  
When an argument is an index vs. a parameter.  
*Terms:* indices, parameters, universe levels  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/)

**Pitfalls of Programming with Dependent Types**  
Where dependent types get awkward: definitional equality, rewriting, overly specific types.  
*Terms:* pitfalls, definitional equality, propositional equality  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming-with-Dependent-Types/Pitfalls-of-Programming-with-Dependent-Types/)


---

<a id="ch9"></a>
## Interlude: Tactics, Induction, and Proofs

Proving things about programs by induction, with tactics.

*Terms:* induction tactic, recursion and induction, tactic golf, induction on lists and trees, grind tactic

→ [read online](https://lean-lang.org/functional_programming_in_lean/Interlude___-Tactics___-Induction___-and-Proofs/)


---

<a id="ch10"></a>
## Programming, Proving, and Performance

Writing programs that are both fast and proved correct.

**Tail Recursion**  
Accumulator-passing tail recursion.  
*Terms:* tail recursion, accumulator  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming___-Proving___-and-Performance/Tail-Recursion/)

**Proving Equivalence**  
Proving a tail-recursive version equals the naive one.  
*Terms:* equivalence proofs, induction  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming___-Proving___-and-Performance/Proving-Equivalence/)

**Arrays and Termination**  
Array loops and termination proofs.  
*Terms:* termination, decreasing_by  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming___-Proving___-and-Performance/Arrays-and-Termination/)

**More Inequalities**  
Proving inequalities (omega and friends).  
*Terms:* inequalities, omega  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming___-Proving___-and-Performance/More-Inequalities/)

**Bounded Numbers**  
Fin and bounded numbers.  
*Terms:* Fin, bounded numbers  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming___-Proving___-and-Performance/Bounded-Numbers/)

**Insertion Sort and Array Mutation**  
Insertion sort with in-place array mutation via reference counting.  
*Terms:* insertion sort, in-place mutation, reference counting  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming___-Proving___-and-Performance/Insertion-Sort-and-Array-Mutation/)

**Special Types**  
Runtime representations of special types.  
*Terms:* UInt, runtime representation, unboxing  
→ [read online](https://lean-lang.org/functional_programming_in_lean/Programming___-Proving___-and-Performance/Special-Types/)


---

<a id="ch11"></a>
## Next Steps

Where to go next.

*Terms:* Theorem Proving in Lean, Mathematics in Lean, Mathlib, dependent types in CS, further reading

→ [read online](https://lean-lang.org/functional_programming_in_lean/Next-Steps/)

