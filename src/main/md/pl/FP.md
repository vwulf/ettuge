# Forays into Functional Programming

## Normal course of exposure
### Multiplication tables
### Arithmetic
### Algebra
### Calculator
## Bash
## Math in Signals
## Naive recursion in C++
### Trees and lists
### Template programming in C++
## Structure and Interpretation of Computer Programs

## 
My introduction to functional programming was though Lisp in compiler and AI classes, later scheme and then
ML for an undergraduate course on programming languages where I wrote frontends astonishingly easily in ML
(OCaml without any of the Object parts). I went on to TA an undergraduate CS honors programming language course
which taught LISP, Scheme and Haskell. Haskell remained completely opaque to me although I graded coursework and such.

I forgot all about it and got back to my home of C++ which I had spent half a decade by then and programmed C++ professionally
for another half a decade. In the course of work, I chanced upon Python (which seemed much cleaner than the Perl I had done in
an internship). When I saw list and dictionary comprehensions - esp nested ones, I was sold over the expressiveness.
I did some side projects in python and moved to a startup where I wanted to build a management plane in python.
Another colleauge was dead set against python and explained the problems of the Global Interpreter Lock (GIL) and how multithreading
is a joke of sorts. He wanted to build around the JVM stack. He asked me to look at Scala which has similar expressiveness to python
and was JVM based giving options to back out if needed. I protoptyped the first section of scala code for the startup and the scala
stack grew to become the entire management plane.

In the course of learning scala, the model of functional programming I thought I knew and what was needed was something else.
I had almost no insights into category theory when I did functional programming in the past - which explained my difficulties with haskell.

For the project I moved from exception based stack to eschewing exceptions by turning them to Options. Later I discovered scalaz and its Validation and preferred that to the default Either due to the more intutitive bias of Validation and the more principled design of scalaz.
However I had quite a few struggles with the usage of ValidationNel and the way errors were combined. The use case that I had was very different
from the usecase of ValidationNel. ValidationNel was great for getting list of all errors when doing a bunch of operations but not a bunch of
partial successes. I kept operator chasing to get my usecase done before I realized that I needed to understand the space comprehensively.
At the same time another portion of the stack started using twitter futures and monadic composition.

I took the coursera course from Odersky [^14]. I was introduced to immutable code. Vars were discouraged by compiler warnings. Tail recursion was
introduced and most of the exercises require solving them in an immutable fashion through tail recursion. Although these techniques were not directly required to Industtry coding where you are mostly consuming libraries, this kind of starts your journey from mutable to immutable.
I did notice around this time that the general exposure of programmers to immutable code, immutable containers, understanding tail recursive coding was pretty limited. There's a clear divide between imperative programmers (including OOP programmers) and functional programmers at this point. This divide is a hill across which neither camp can clearly look at and understand the other side. 

A lot of it has to do with CS education focusing on mutable datastructures for the most bit and being exposed to imperative programming in the beggining. People with a mathematical bend take to functional programming easily but it's not always the case. Case in point is Knuth's multipart volumes being heavily imperative. To really start the exploration in to this world, either real world implementation of the scala immutable and haskell libraries need to be studied *or* a pedagogic dive into Chris Okasaki's book is the best place to start [^16] [^18]. This book is interesting in that it's focused only on datastructure design and analysis techniques. It covers the space of immutable (also called persistent and pure functional) datastructures.

Approaching algorithm writing in a functional programming language is a different problem from designing datastructures. This book [^18] seems to address that gap. Otherwise standard algorithms text books tend to be heavily imperative and tend to use pseudo-code as well.

Although I studied [^18] in parallel to using scala's immutable libraries, from the perspective of building applications or systems code needs familiarity with well known functional idioms. Doing recursion naively, converting to tail recursion for real world needs can get tedious. That's roughly when you need an introduction to using higher order functions and combinators - like map, filter and fold.

At this time, I went through [^13] in parallel to [^12][^19] to understand functors, applicatives, monoids and monads. After I went through
the whole thing, it seemed straight forward in retrospective but it was quite a learning curve. Even here, there's a big gap between learning to use the above algebraic structures to defining your own.

Later I had encountered recursion schemes through this fantastic talk by tpolecat [^11]. This was much
after extensive stumbling around functional programming in scalaz [^12] years after grad school projects
writing compiler frontends in ocaml. 

[^8]: https://youtu.be/09-9LltqWLY?si=CJ1TbuAjvMGPwUX8
[^9]: https://www.youtube.com/watch?v=43XaZEn2aLc&list=PL1a1q1zrmyEwpA2PvYcM1UqE18zekujW-&index=17
[^10]: https://cs.stackexchange.com/questions/109954/writing-a-grammar-for-lambda-calculus
[^11]: https://www.youtube.com/watch?v=XHiTK4UOIf0
[^12]: http://eed3si9n.com/learning-scalaz/
[^13]: https://learnyouahaskell.com/
[^14]: https://www.coursera.org/learn/scala-functional-programming
[^15]: http://systemfw.org/posts/tailrec.html
[^16]: https://www.cs.cmu.edu/~rwh/students/okasaki.pdf
[^17]: https://drive.google.com/file/d/1nuRlrqrRRsxMhX20NTd9YTPVANQi5Of-/view?pli=1
[^18]: https://www.cambridge.org/core/books/purely-functional-data-structures/0409255DA1B48FA731859AC72E34D494
[^19]: https://youtu.be/6t6bsWVOIzs?si=KxRYX5VRfgK-MMRd

