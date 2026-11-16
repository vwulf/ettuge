<a id="ch1"></a>
# Implementing Functional Languages: a tutorial

> Simon L. Peyton Jones and David R. Lester · Prentice Hall, 1992 (free electronic edition) · [the PDF in Drive](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

PDF page = printed page + 1. Appendices (utilities module, example Core programs) and chapter conclusions are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A hands-on course in building implementations of lazy functional languages, written as runnable Miranda (easily read as Haskell). It defines a small Core language with a parser and pretty-printer, then builds a sequence of increasingly realistic evaluators, each in numbered “Marks”: a template-instantiation graph reducer, the G-machine (compiling supercombinators to stack code), the Three Instruction Machine (TIM, a spineless closure-based design), and a parallel G-machine. A final chapter covers the front-end transformations that feed them: lambda lifting, Johnsson-style lifting, full laziness and dependency analysis. Every machine is specified as a state transition system, which makes the designs easy to compare.

**Contents**

1. [The Core language](ch1): Core, a tiny lazy language used throughout, and its front end.
2. [Template instantiation](ch2): Graph reduction by instantiating function bodies, step by step.
3. [The G-machine](ch3): Compiling supercombinators to code for a stack machine.
4. [TIM: the three instruction machine](ch4): The Three Instruction Machine: a spineless, frame-based alternative.
5. [A Parallel G-machine](ch5): Running graph reduction in parallel.
6. [Lambda Lifting](ch6): Transforming programs into supercombinators, and full laziness.


---

## The Core language

*PDF pp. 11–42*

Core, a tiny lazy language used throughout, and its front end.

**An overview of the Core language**  
What Core contains: supercombinators, let(rec), case, constructors.  
*Terms:* Core language, supercombinators  
→ PDF pp. 12–15 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Syntax of the Core language**  
Concrete syntax.  
*Terms:* syntax  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Data types for the Core language**  
The Haskell-style data types for Core programs.  
*Terms:* abstract syntax tree  
→ PDF pp. 17–19 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**A small standard prelude**  
A minimal prelude (I, K, S, compose, twice).  
*Terms:* prelude, SKI  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**A pretty-printer for the Core language**  
A pretty-printer built with an abstract iseq type for efficient layout.  
*Terms:* pretty-printer, iseq  
→ PDF pp. 21–28 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**A parser for the Core language**  
A lexer and parser written with parser combinators.  
*Terms:* parser combinators, lexer  
→ PDF pp. 29–42 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)


---

<a id="ch2"></a>
## Template instantiation

*PDF pp. 43–83*

Graph reduction by instantiating function bodies, step by step.

**A review of template instantiation**  
How template instantiation evaluates by rewriting the graph.  
*Terms:* template instantiation, graph reduction  
→ PDF pp. 43–48 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**State transition systems**  
Describing machines as state transition systems.  
*Terms:* state transition system  
→ PDF pp. 49–50 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 1: A minimal template instantiation graph reducer**  
A minimal reducer with stack, dump, heap and globals.  
*Terms:* spine, stack, heap, dump  
→ PDF pp. 51–62 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 2: let(rec) expressions**  
Adding let and letrec.  
*Terms:* let, letrec  
→ PDF p. 63 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 3: Adding updating**  
Updating redexes so shared work is not repeated.  
*Terms:* updating, sharing, indirection  
→ PDF pp. 64–65 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 4: Adding arithmetic**  
Arithmetic and strict primitives.  
*Terms:* arithmetic primitives  
→ PDF pp. 66–68 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 5: Structured data**  
Constructors, case and data structures.  
*Terms:* structured data, constructors  
→ PDF pp. 69–74 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Alternative implementations**  
Other ways to build the reducer.  
*Terms:* alternative implementations  
→ PDF pp. 75–76 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Garbage collection**  
Mark-scan, copying and other collectors for the heap.  
*Terms:* garbage collection, mark-scan, copying collector  
→ PDF pp. 77–83 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)


---

<a id="ch3"></a>
## The G-machine

*PDF pp. 84–143*

Compiling supercombinators to code for a stack machine.

**Introduction to the G-machine**  
Why compile instead of instantiate.  
*Terms:* G-machine, compilation  
→ PDF pp. 84–85 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Code sequences for building templates**  
Compilation schemes that build template graphs.  
*Terms:* compilation schemes, SC R C  
→ PDF pp. 86–89 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 1: A minimal G-machine**  
A minimal G-machine.  
*Terms:* stack machine  
→ PDF pp. 90–102 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 2: Making it lazy**  
Adding laziness with updates.  
*Terms:* laziness, update  
→ PDF pp. 103–105 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 3: let(rec) expressions**  
let(rec) in compiled code.  
*Terms:* letrec  
→ PDF pp. 106–111 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 4: Adding primitives**  
Primitive operations.  
*Terms:* primitives  
→ PDF pp. 112–119 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 5: Towards better handling of arithmetic**  
Avoiding graph building for arithmetic (strict contexts).  
*Terms:* strictness, B scheme  
→ PDF pp. 120–123 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 6: Adding data structures**  
Constructors and case in the G-machine.  
*Terms:* data structures, Pack, CaseJump  
→ PDF pp. 124–131 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 7: Further improvements**  
Further refinements toward an efficient machine.  
*Terms:* optimizations  
→ PDF pp. 132–141 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)


---

<a id="ch4"></a>
## TIM: the three instruction machine

*PDF pp. 144–196*

The Three Instruction Machine: a spineless, frame-based alternative.

**Background: How TIM works**  
How TIM uses frames and closures instead of a spine.  
*Terms:* TIM, three instruction machine, frames, closures  
→ PDF pp. 144–151 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 1: A minimal TIM**  
A minimal TIM with Take, Push and Enter.  
*Terms:* Take, Push, Enter  
→ PDF pp. 152–161 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 2: Adding arithmetic**  
Arithmetic with a value stack.  
*Terms:* value stack  
→ PDF pp. 162–167 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 3: let(rec) expressions**  
let(rec) via frame slots.  
*Terms:* letrec  
→ PDF pp. 168–172 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 4: Updating**  
Updating with markers.  
*Terms:* update markers  
→ PDF pp. 173–183 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 5: Structured data**  
Data structures with return continuations.  
*Terms:* structured data, continuations  
→ PDF pp. 184–189 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 6: Constant applicative forms and the code store**  
CAFs and code-store handling.  
*Terms:* constant applicative forms, CAF  
→ PDF pp. 190–192 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)


---

<a id="ch5"></a>
## A Parallel G-machine

*PDF pp. 197–217*

Running graph reduction in parallel.

**Introduction**  
Sources of parallelism in lazy programs and the par primitive.  
*Terms:* parallel graph reduction, par  
→ PDF pp. 197–200 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 1: A minimal parallel G-machine**  
A minimal parallel G-machine with many tasks.  
*Terms:* parallel G-machine  
→ PDF pp. 201–209 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 2: The evaluate-and-die model**  
Evaluate-and-die task management.  
*Terms:* evaluate-and-die  
→ PDF pp. 210–212 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 3: A realistic parallel G-machine**  
A more realistic machine with locking.  
*Terms:* locking, realistic model  
→ PDF pp. 213–214 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 4: A better way to handle blocking**  
Better handling of tasks that block on shared nodes.  
*Terms:* blocking  
→ PDF pp. 215–216 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)


---

<a id="ch6"></a>
## Lambda Lifting

*PDF pp. 218–262*

Transforming programs into supercombinators, and full laziness.

**Introduction**  
Why lambda lifting is needed.  
*Terms:* lambda lifting  
→ PDF p. 218 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Improving the expr data type**  
Annotating expressions for transformations.  
*Terms:* annotated expressions  
→ PDF pp. 218–221 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 1: A simple lambda lifter**  
A simple lambda lifter: free variables and abstraction.  
*Terms:* free variables  
→ PDF pp. 222–230 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 2: Improving the simple lambda lifter**  
Improvements to the simple lifter.  
*Terms:* improved lifter  
→ PDF p. 231 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 3: Johnsson-style lambda lifting**  
Johnsson’s lifting that adds only free variables as parameters.  
*Terms:* Johnsson lambda lifting  
→ PDF pp. 232–236 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 4: A separate full laziness pass**  
Full laziness as a separate pass that floats out maximal free expressions.  
*Terms:* full laziness, maximal free expressions  
→ PDF pp. 237–250 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 5: Improvements to full laziness**  
Refining full laziness.  
*Terms:* full laziness improvements  
→ PDF pp. 251–252 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

**Mark 6: Dependency analysis**  
Dependency analysis to split letrecs into strongly connected components.  
*Terms:* dependency analysis, strongly connected components  
→ PDF pp. 253–260 in [the PDF](https://drive.google.com/file/d/1JtwtruLzgG3QvHB6D5g7CF7_HAea71K2/view)

