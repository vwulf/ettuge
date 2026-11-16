<a id="ch1"></a>
# Learn Programming with OCaml: Algorithms and Data Structures

> Sylvain Conchon and Jean-Christophe Filliâtre · English translation by Urmila Nair, OCaml Software Foundation, February 2025 · [the PDF in Drive](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

PDF page = printed page + 10. Exercise sections are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A two-part book that teaches programming in OCaml and then classic algorithms and data structures. Part I introduces the language through fourteen small, complete programs (leap years, Monte Carlo, the Mandelbrot set, the sieve, file copying, a Breakout clone, Logo turtle, music, quadtrees, N-queens) and then explains type checking, the runtime model and complexity. Part II implements and analyzes data structures and algorithms in a functional-first style: resizable and persistent arrays, bit vectors and ropes; search trees, AVL, hash tables, tries and Patricia trees; imperative and persistent queues and heaps; graph representations; union–find; zippers; arithmetic algorithms; memoization and hash-consing; sorting; and graph algorithms.

**Contents**

1. [The Working Environment](ch1): Setting up and running OCaml.
2. [First Steps with OCaml](ch2): Learning OCaml through fourteen small programs.
3. [OCaml Concepts: A Closer Look](ch3): How OCaml works under the hood.
4. [Arrays](ch4): Array-like structures.
5. [Sets and Dictionaries](ch5): Sets and maps.
6. [Queues](ch6): Queues and priority queues.
7. [Graphs](ch7): Representing graphs.
8. [Disjoint Sets](ch8): Union–find.
9. [Zippers](ch9): Zippers for navigating data.
10. [Arithmetic](ch10): Number-theoretic algorithms.
11. [Dynamic Programming and Memoization](ch11): Memoization, dynamic programming and sharing.
12. [Sorting Algorithms](ch12): Sorting.
13. [Graph Algorithms](ch13): Graph algorithms.


---

## The Working Environment

*PDF pp. 13–16*

Setting up and running OCaml.

**The Compiler and the Interpreter**  
Compiler vs. toplevel.  
*Terms:* ocamlc, ocamlopt, toplevel  
→ PDF p. 13 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**A First OCaml Program**  
A first program.  
*Terms:* first program  
→ PDF p. 14 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Programming Environments**  
Editors and environments.  
*Terms:* editors  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Installing OCaml Libraries**  
opam libraries.  
*Terms:* opam  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch2"></a>
## First Steps with OCaml

*PDF pp. 17–154*

Learning OCaml through fourteen small programs.

**Leap Years**  
Conditionals and integers.  
*Terms:* if, integers  
→ PDF pp. 18–25 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**The Monte-Carlo Method**  
Random numbers and floats.  
*Terms:* Monte Carlo, floats  
→ PDF pp. 26–36 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Drawing a Cardioid**  
Graphics.  
*Terms:* Graphics, cardioid  
→ PDF pp. 37–42 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**The Mandelbrot Set**  
Complex iteration and images.  
*Terms:* Mandelbrot  
→ PDF pp. 43–49 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Sieve of Eratosthenes**  
Arrays and loops.  
*Terms:* sieve of Eratosthenes, arrays  
→ PDF pp. 50–56 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Drawing a Curve**  
Plotting functions.  
*Terms:* curve plotting  
→ PDF pp. 57–67 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Copying a File**  
Files and buffers.  
*Terms:* file I/O  
→ PDF pp. 68–75 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Reversing the Order of Lines in a Text**  
Lists and strings.  
*Terms:* lists, reverse  
→ PDF pp. 76–83 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Converting Integers from an Arbitrary Base**  
Number bases.  
*Terms:* base conversion  
→ PDF pp. 84–92 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Breakout without Bricks**  
An interactive game loop.  
*Terms:* Breakout, event loop  
→ PDF pp. 93–104 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Logo Turtle**  
Turtle graphics and recursion.  
*Terms:* Logo turtle  
→ PDF pp. 105–111 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Playing a Musical Score**  
Audio and records.  
*Terms:* music, records  
→ PDF pp. 112–121 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Quadtrees**  
Recursive trees.  
*Terms:* quadtrees  
→ PDF pp. 122–127 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Solving the N-Queens Problem**  
Backtracking with bit sets.  
*Terms:* N-queens, backtracking  
→ PDF pp. 128–140 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch3"></a>
## OCaml Concepts: A Closer Look

*PDF pp. 155–174*

How OCaml works under the hood.

**Type-Checking Algorithm**  
Hindley–Milner type inference.  
*Terms:* type inference, Hindley-Milner  
→ PDF pp. 155–159 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Runtime Model**  
Values, boxing, stack and heap, GC.  
*Terms:* runtime model, boxing, garbage collection  
→ PDF pp. 160–165 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Analyzing the Execution Time of a Program**  
Complexity analysis.  
*Terms:* complexity, big-O  
→ PDF pp. 166–169 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch4"></a>
## Arrays

*PDF pp. 175–216*

Array-like structures.

**Resizeable Arrays**  
Amortized resizable arrays.  
*Terms:* resizable arrays, amortization  
→ PDF pp. 175–180 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Bit Vectors**  
Bit vectors.  
*Terms:* bit vectors  
→ PDF pp. 181–189 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Ropes**  
Ropes for long strings.  
*Terms:* ropes  
→ PDF pp. 190–206 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Persistent Arrays**  
Persistent arrays via rerooting.  
*Terms:* persistent arrays  
→ PDF pp. 207–210 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch5"></a>
## Sets and Dictionaries

*PDF pp. 217–276*

Sets and maps.

**Binary Search Trees**  
Binary search trees.  
*Terms:* BST  
→ PDF pp. 218–225 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**AVL Trees**  
AVL balancing.  
*Terms:* AVL trees  
→ PDF pp. 226–236 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Hash Tables**  
Hash tables.  
*Terms:* hash tables  
→ PDF pp. 237–247 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Prefix Trees**  
Tries.  
*Terms:* tries, prefix trees  
→ PDF pp. 248–257 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Patricia Trees**  
Patricia trees.  
*Terms:* Patricia trees  
→ PDF pp. 258–269 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch6"></a>
## Queues

*PDF pp. 277–304*

Queues and priority queues.

**Imperative Queues**  
Imperative queues.  
*Terms:* imperative queue  
→ PDF pp. 277–281 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Persistent Queues**  
Persistent queues with two lists.  
*Terms:* persistent queue  
→ PDF pp. 282–283 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Imperative Priority Queues**  
Binary heaps.  
*Terms:* binary heap  
→ PDF pp. 284–294 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Persistent Priority Queues**  
Leftist/skew heaps.  
*Terms:* leftist heap, persistent priority queue  
→ PDF pp. 295–298 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch7"></a>
## Graphs

*PDF pp. 305–322*

Representing graphs.

**Adjacency Matrix**  
Adjacency matrices.  
*Terms:* adjacency matrix  
→ PDF pp. 307–310 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Adjacency Lists**  
Adjacency lists.  
*Terms:* adjacency list  
→ PDF p. 311 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Adjacency Dictionaries**  
Adjacency maps.  
*Terms:* adjacency dictionary  
→ PDF pp. 312–317 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Performance Comparison**  
Comparing them.  
*Terms:* performance  
→ PDF p. 318 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch8"></a>
## Disjoint Sets

*PDF pp. 323–332*

Union–find.

**The Basic Idea**  
The idea.  
*Terms:* disjoint sets, union-find  
→ PDF pp. 323–324 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Implementation**  
Path compression and union by rank.  
*Terms:* path compression, union by rank  
→ PDF pp. 325–328 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch9"></a>
## Zippers

*PDF pp. 333–352*

Zippers for navigating data.

**Zippers on Lists**  
List zippers.  
*Terms:* zipper  
→ PDF pp. 333–336 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Zippers on Trees**  
Tree zippers.  
*Terms:* tree zipper  
→ PDF pp. 337–344 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Cursors**  
Cursors.  
*Terms:* cursor  
→ PDF pp. 345–347 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch10"></a>
## Arithmetic

*PDF pp. 353–366*

Number-theoretic algorithms.

**Euclid’s Algorithm**  
GCD.  
*Terms:* Euclid algorithm  
→ PDF pp. 353–354 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Exponentiation by Squaring**  
Fast exponentiation.  
*Terms:* exponentiation by squaring  
→ PDF p. 355 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Modular Arithmetic**  
Modular arithmetic.  
*Terms:* modular arithmetic  
→ PDF pp. 356–359 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Matrix Calculus**  
Matrix power (Fibonacci).  
*Terms:* matrix exponentiation  
→ PDF pp. 360–362 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch11"></a>
## Dynamic Programming and Memoization

*PDF pp. 367–384*

Memoization, dynamic programming and sharing.

**Basic Idea**  
The idea.  
*Terms:* memoization  
→ PDF pp. 367–370 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Mechanical Memoization**  
Generic memoization with fixpoints.  
*Terms:* memo fixpoint  
→ PDF pp. 371–373 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Differences between Memoization and Dynamic Programming**  
Memoization vs. DP.  
*Terms:* dynamic programming  
→ PDF pp. 374–375 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Hash-consing**  
Hash-consing.  
*Terms:* hash-consing  
→ PDF pp. 376–381 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch12"></a>
## Sorting Algorithms

*PDF pp. 385–422*

Sorting.

**Insertion Sort**  
Insertion sort.  
*Terms:* insertion sort  
→ PDF pp. 386–387 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Quicksort**  
Quicksort.  
*Terms:* quicksort  
→ PDF pp. 388–395 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Merge Sort**  
Merge sort.  
*Terms:* merge sort  
→ PDF pp. 396–402 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Heapsort**  
Heapsort.  
*Terms:* heapsort  
→ PDF pp. 403–409 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Optimal Complexity**  
Lower bound.  
*Terms:* comparison lower bound  
→ PDF p. 410 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Experimental Evaluation**  
Benchmarks.  
*Terms:* benchmarks  
→ PDF pp. 410–413 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)


---

<a id="ch13"></a>
## Graph Algorithms

*PDF pp. 423–444*

Graph algorithms.

**Breadth-First Search**  
BFS.  
*Terms:* breadth-first search  
→ PDF pp. 423–425 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Depth-First Search**  
DFS.  
*Terms:* depth-first search, topological sort  
→ PDF pp. 426–428 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Shortest Path**  
Dijkstra.  
*Terms:* Dijkstra, shortest path  
→ PDF pp. 429–437 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

**Minimum spanning tree**  
Kruskal and Prim.  
*Terms:* minimum spanning tree, Kruskal, Prim  
→ PDF pp. 438–441 in [the PDF](https://drive.google.com/file/d/1f7DTTU4A2PrdAldORaF-iwX26_UH5VoB/view)

