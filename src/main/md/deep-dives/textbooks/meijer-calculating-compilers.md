<a id="ch1"></a>
# Calculating Compilers

> Erik Meijer · PhD thesis, University of Nijmegen, 1992 · [the PDF in Drive](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

A scanned thesis with an imperfect text layer, so some symbols in the PDF are garbled. Printed page = PDF page − 17; the bibliography (PDF p. 138) and Dutch summary (p. 146) are not broken down. Summaries are in our own words.

## The book in one paragraph

Meijer’s thesis argues that compilers should be derived, not just verified: start from a denotational semantics of the source language and transform it by equational reasoning, in the Bird–Meertens style, until it becomes code for an abstract machine, so the result is correct by construction. Chapter 1 does this for a small functional language, ending in de Bruijn-indexed stack code. Chapter 2 is the theory, the famous “bananas, lenses, envelopes and barbed wire” paper: catamorphisms, anamorphisms, hylomorphisms and paramorphisms over algebraic data types in CPO, with their laws. The remaining chapters apply the method to Petri-net update schemes, an imperative language with procedures (via continuations, short-circuit evaluation and tail calls), and backtracking with success and failure continuations and cut.

**Contents**

1. [1. More Advice on Proving a Compiler Correct: Improve a Correct Compiler](ch1): Deriving a correct compiler for a small functional language from its semantics.
2. [2. Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire](ch2): A calculus of recursion schemes over algebraic data types, the theoretical core.
3. [3. From Pr/T-nets to Update Schemes](ch3): Transforming predicate/transition nets into update schemes.
4. [4. BNF for Syntax, BMF for Semantics](ch4): Deriving an imperative-language compiler with continuations.
5. [5. A Taxonomy of Backtracking](ch5): A family of semantics for backtracking derived step by step from a relational one.


---

## 1. More Advice on Proving a Compiler Correct: Improve a Correct Compiler

*PDF pp. 22–37*

Deriving a correct compiler for a small functional language from its semantics.

**1.1 The compiler correctness problem**  
Why proving compilers correct after the fact is hard, and why calculating them is better.  
*Terms:* compiler correctness  
→ PDF pp. 23–25 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**1.2–1.3 A simple functional language F and its syntax**  
The source language and its syntax.  
*Terms:* functional language, syntax  
→ PDF pp. 26–27 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**1.4 Semantics: static, standard, spineless, environment**  
Static and dynamic semantics, refined into a spineless, environment-based form.  
*Terms:* denotational semantics, static semantics, environment  
→ PDF pp. 27–34 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**1.5 Translating into de Bruijn form**  
Removing variable names to get machine-like code.  
*Terms:* de Bruijn indices  
→ PDF pp. 34–36 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**1.6 Towards a concrete implementation**  
From the derived semantics to an implementation.  
*Terms:* abstract machine, implementation  
→ PDF pp. 36–37 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)


---

<a id="ch2"></a>
## 2. Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire

*PDF pp. 38–71*

A calculus of recursion schemes over algebraic data types, the theoretical core.

**2.1 The data type of lists**  
Lists and their fold and unfold operators.  
*Terms:* lists, foldr, unfold  
→ PDF pp. 39–43 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.2 The category CPO**  
The category of complete partial orders as the setting.  
*Terms:* CPO, complete partial order  
→ PDF pp. 43–46 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.3 Functors**  
Functors and their laws.  
*Terms:* functors  
→ PDF pp. 46–50 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.4 Algebraic data types**  
Data types as least fixed points of functors.  
*Terms:* algebraic data types, fixed points  
→ PDF pp. 50–51 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.5 Recursion schemes**  
Catamorphisms (bananas), anamorphisms (lenses), hylomorphisms (envelopes) and paramorphisms (barbed wire), with fusion laws.  
*Terms:* catamorphism, anamorphism, hylomorphism, paramorphism, fusion, recursion schemes  
→ PDF pp. 51–61 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.6 Parametrized types**  
Data types with parameters, like lists of a.  
*Terms:* parametrized types  
→ PDF pp. 61–64 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.7 Mutual recursion**  
Mutually recursive types.  
*Terms:* mutual recursion  
→ PDF pp. 64–66 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.8 The induction principle for algebraic data types**  
Induction for algebraic data types.  
*Terms:* induction principle  
→ PDF pp. 66–67 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.9 Higher-order functions wreck calculations**  
Why higher-order functions complicate the calculus.  
*Terms:* higher-order functions  
→ PDF pp. 67–69 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**2.10–2.11 Continuous algebras and conclusions**  
Continuous algebras, and a summary.  
*Terms:* continuous algebras  
→ PDF pp. 69–71 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)


---

<a id="ch3"></a>
## 3. From Pr/T-nets to Update Schemes

*PDF pp. 72–81*

Transforming predicate/transition nets into update schemes.

**3.1 Pr/T nets**  
Predicate/transition nets.  
*Terms:* Petri nets, Pr/T nets  
→ PDF pp. 73–75 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**3.2 Update schemes**  
Calculating efficient update schemes from net semantics.  
*Terms:* update schemes, program transformation  
→ PDF pp. 75–81 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)


---

<a id="ch4"></a>
## 4. BNF for Syntax, BMF for Semantics

*PDF pp. 82–109*

Deriving an imperative-language compiler with continuations.

**4.1–4.2 Overview and a simple imperative language W**  
The plan, and a small while-language with its semantics.  
*Terms:* imperative language, while language  
→ PDF pp. 82–89 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**4.3 Continuation semantics**  
Rewriting the semantics in continuation-passing style.  
*Terms:* continuation semantics, CPS  
→ PDF pp. 89–94 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**4.4 Expression continuations**  
Continuations for expressions.  
*Terms:* expression continuations  
→ PDF pp. 94–97 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**4.5 Short-circuit evaluation**  
Deriving jumping code for Boolean expressions.  
*Terms:* short-circuit evaluation, jumping code  
→ PDF pp. 97–101 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**4.6 Adding procedures: from W to C**  
Procedures and the extension to a C-like language.  
*Terms:* procedures  
→ PDF pp. 101–108 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**4.7–4.8 Tail-call elimination and a concrete implementation**  
Eliminating tail calls, and the resulting implementation.  
*Terms:* tail call elimination  
→ PDF pp. 108–109 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)


---

<a id="ch5"></a>
## 5. A Taxonomy of Backtracking

*PDF pp. 110–137*

A family of semantics for backtracking derived step by step from a relational one.

**5.1–5.3 A calculus of relations, the language B, relational semantics**  
Relations, a backtracking language and its relational meaning.  
*Terms:* relational semantics, backtracking  
→ PDF pp. 111–115 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**5.4 Success continuations**  
Adding success continuations.  
*Terms:* success continuation  
→ PDF pp. 115–117 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**5.5 Failure continuations**  
Adding failure continuations.  
*Terms:* failure continuation  
→ PDF pp. 117–121 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**5.6 Making recursion explicit**  
Making recursion explicit.  
*Terms:* explicit recursion  
→ PDF pp. 121–125 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**5.7 Introducing the cut**  
Adding Prolog-style cut.  
*Terms:* cut, Prolog  
→ PDF pp. 125–128 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**5.8 Comparison with other continuation semantics**  
How these relate to other continuation semantics.  
*Terms:* continuation semantics  
→ PDF pp. 128–129 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

**5.9–5.10 Concrete semantics and recomputing the input**  
A concrete semantics, and recomputing the input instead of storing it.  
*Terms:* concrete semantics  
→ PDF pp. 129–137 in [the PDF](https://drive.google.com/file/d/1-YaDtD6k_7x0gClgJdCEjTDcL8ZTWJYb/view)

