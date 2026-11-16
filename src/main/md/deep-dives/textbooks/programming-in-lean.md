<a id="ch1"></a>
# Programming in Lean

> Jeremy Avigad, Leonardo de Moura and Jared Roesch · unfinished draft for Lean 3 · [the PDF in Drive](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

A short, unfinished book: chapters 2–6 and parts of chapter 8 are placeholders describing what they would cover. The Lean 3 metaprogramming API it documents has since been replaced in Lean 4, so read it for the ideas rather than the syntax. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Lean is a theorem prover, but its logic is also a functional programming language, and this book was meant to teach it as one. What exists is the introduction, a chapter on monads (option, list, state, IO, with do-notation), and the parts on metaprogramming: writing tactics as programs in the tactic monad that inspect goals and build proof terms, ending with a complete tableau prover for propositional logic. The point it makes is that the same language serves for programs, specifications, proofs and the automation that writes proofs.

**Contents**

1. [Introduction](ch1): Why Lean doubles as a programming language, a first look at IO and metaprogramming, and a map of the planned contents.
2. [Chapters 2–6: outlines only](ch2): Five chapters that exist only as one-paragraph plans: basics, data structures, verifying programs, recursion and type classes.
3. [Monads](ch3): Monads as type classes, with do-notation, illustrated by option, list, state and IO, plus the related classes Lean defines.
4. [Writing Tactics](ch4): Tactics as programs: the tactic monad, quoting and inspecting expressions, worked tactics, and placeholder sections on reduction and unification.
5. [Writing Automation](ch5): A complete example of automation: a tableau prover for classical propositional logic written as a tactic.
6. [The Tactic Library](ch6): A placeholder for documenting the tactic library (simplifier API, data structures, pattern matching).


---

## Introduction

*PDF pp. 5–10*

Why Lean doubles as a programming language, a first look at IO and metaprogramming, and a map of the planned contents.

**Lean as a Programming Language**  
Lean’s logic, the Calculus of Inductive Constructions, is expressive enough to be a practical functional language, and programs can be evaluated by its virtual machine.  
→ PDF p. 5 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Examples**  
Short programs (hello world, printing squares) show the flavor.  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Input and Output**  
IO is done through an interface type class whose instance the virtual machine supplies.  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Metaprogramming in Lean**  
A first tactic that splits conjunction hypotheses shows metaprogramming: Lean programs that manipulate Lean proofs.  
→ PDF pp. 7–8 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Overview of the contents**  
The planned chapters: programming first, then verification, then tactics and automation.  
→ PDF pp. 9–10 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)


---

<a id="ch2"></a>
## Chapters 2–6: outlines only

*PDF pp. 11–15*

Five chapters that exist only as one-paragraph plans: basics, data structures, verifying programs, recursion and type classes.

**Programming Basics**  
Planned: functional programming with numbers, lists and strings, conditionals and simple pattern matching.  
→ PDF p. 11 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Data Structures**  
Planned: pairs, lists, enumerations, structures and subtypes.  
→ PDF p. 12 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Verifying Properties of Programs**  
Planned: proving properties of list functions and sorting, in two styles (separate properties, or subtypes).  
→ PDF p. 13 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Recursion**  
Planned: the function definition package, well-founded recursion and new inductive types.  
→ PDF p. 14 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Type Classes**  
Planned: making instances of common type classes.  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)


---

<a id="ch3"></a>
## Monads

*PDF pp. 16–25*

Monads as type classes, with do-notation, illustrated by option, list, state and IO, plus the related classes Lean defines.

**The option monad**  
Option chains computations that may fail; do-notation reads as “do this, then that, then return”, and the monad is found by type class inference.  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**The list monad**  
The same generic code reread in the list monad computes all possible results, nondeterminism for free.  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**The state monad**  
State threads a value through a computation; an example models reading and writing registers.  
→ PDF pp. 20–22 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**The IO monad**  
IO as a monad over an abstract interface, so programs stay pure and the VM supplies effects.  
→ PDF p. 23 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Related type classes**  
Functor, applicative and related classes, and how they fit under monad.  
→ PDF pp. 24–25 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)


---

<a id="ch4"></a>
## Writing Tactics

*PDF pp. 26–38*

Tactics as programs: the tactic monad, quoting and inspecting expressions, worked tactics, and placeholder sections on reduction and unification.

**A First Look at the Tactic Monad**  
A proof by tactic is just an expression of type tactic unit that the elaborator runs to fill a goal.  
→ PDF pp. 26–29 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Names and Expressions**  
Tactics read the goal and context as names and expressions, and build terms through quotation and antiquotation.  
→ PDF pp. 30–34 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Examples**  
Worked tactics that inspect goals and close them, including the difference between quoting at definition time and at run time.  
→ PDF pp. 35–36 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Reduction**  
Planned: reduction, weak head normal form and transparency settings.  
→ PDF p. 37 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

**Metavariables and Unification**  
Planned: goals as metavariables, and unification.  
→ PDF p. 38 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)


---

<a id="ch5"></a>
## Writing Automation

*PDF pp. 39–44*

A complete example of automation: a tableau prover for classical propositional logic written as a tactic.

**A Tableau Prover for Classical Propositional Logic**  
The prover breaks sequents down by connective until each branch closes or yields a counterexample; the method shows completeness of cut-free sequent calculus.  
→ PDF pp. 39–44 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)


---

<a id="ch6"></a>
## The Tactic Library

*PDF pp. 45–46*

A placeholder for documenting the tactic library (simplifier API, data structures, pattern matching).

→ PDF pp. 45–46 in [the PDF](https://drive.google.com/file/d/1oKE5c8p47zXIYh0V3hCOOHkzWpdzVdzu/view)

