<a id="ch1"></a>
# Compilers: Course Notes

> Oleg Kiselyov · November 2024 (the first 28 pages) · [the PDF in Drive](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)

This PDF holds only the opening of the notes: the table of contents runs to section 4.12 on page 72, but the file stops early in chapter 4. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A hands-on compilers course in which students build, in OCaml, a compiler from Tiger′ (a Pascal-like language with nested functions) to real x86-64 machine code that runs on their laptops. Kiselyov grows the compiler one language feature at a time, each step driven by tests written first, and builds it in tagless-final style: the source language is an OCaml signature, and interpreters, pretty-printers, transformations and the code generator are all just different implementations of it. The file covers the setup, what a compiler is, the tagless-final warm-up, and the first real step: compiling integer literals to assembly.

**Contents**

1. [Introduction](ch1): Course goals (a real compiler, plus test-driven development and version control), the required OCaml and Git setup, and how weekly exercises are graded.
2. [What is a compiler?](ch2): A compiler explained by translating one Tiger′ program by hand, and the plan to grow the language incrementally.
3. [Introduction to tagless-final style and OCaml reminder](ch3): The tagless-final style on a tiny language of integers and addition: one signature, many interpreters and transformers.
4. [Making the compiler](ch4): The first compiler step: the smallest source language compiled to x86-64 assembly, with tests and a build system.


---

## Introduction

*PDF pp. 3–6*

Course goals (a real compiler, plus test-driven development and version control), the required OCaml and Git setup, and how weekly exercises are graded.

**Prerequisites**  
Students should know some programming language theory and enough OCaml to follow modules and functors.  
→ PDF p. 3 in [the PDF](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)

**Development environment**  
Linux or macOS on x86-64 (or an emulator), the OCaml toolchain, and Git for every exercise.  
→ PDF pp. 3–5 in [the PDF](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)

**Exercises and Grading**  
Each week: write tests for a new feature, then extend the compiler until they pass.  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)


---

<a id="ch2"></a>
## What is a compiler?

*PDF pp. 7–10*

A compiler explained by translating one Tiger′ program by hand, and the plan to grow the language incrementally.

**Incremental approach**  
Each new language feature is added in a small step that keeps the compiler working end to end.  
→ PDF p. 10 in [the PDF](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)


---

<a id="ch3"></a>
## Introduction to tagless-final style and OCaml reminder

*PDF pp. 11–18*

The tagless-final style on a tiny language of integers and addition: one signature, many interpreters and transformers.

**A simple embedded DSL and its interpreters and transformers**  
The language is a module signature; evaluation and pretty-printing are modules implementing it, and a transformer (here, negating literals) is a functor from one implementation to another.  
→ PDF pp. 12–15 in [the PDF](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)

**Separate compilation: making a project**  
Splitting the code into files and modules and building it as a project.  
→ PDF pp. 16–18 in [the PDF](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)


---

<a id="ch4"></a>
## Making the compiler

*PDF pp. 19–28*

The first compiler step: the smallest source language compiled to x86-64 assembly, with tests and a build system.

**The simplest source language**  
Printing an integer in assembly, assembly treated as an embedded DSL, testing the generated executables, and the build setup.  
→ PDF pp. 19–28 in [the PDF](https://drive.google.com/file/d/1BiiOWoRcSxJrGONJw38aEYdhx-0WaOgw/view)

