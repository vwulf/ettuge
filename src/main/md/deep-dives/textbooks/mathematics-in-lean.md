<a id="ch1"></a>
# Mathematics in Lean

> Jeremy Avigad and Patrick Massot · current online edition (v4.34.0, 2020–2025, Lean 4 and Mathlib), CC BY 4.0 · [the online book](https://leanprover-community.github.io/mathematics_in_lean/)

The book is published as a website (with exercise files in the companion repository leanprover-community/mathematics_in_lean), so every section links to its place in the current online edition instead of a PDF page range. The older Lean 3 edition (with Kevin Buzzard and Robert Y. Lewis) is superseded and not broken out. It can also be read with an AI reading companion on [ChapterPal](https://www.chapterpal.com/book/fd356955-a80d-4490-aa0b-b0e01bfe65bb/mathematics-in-lean). Summaries are in our own words.

## The book in one paragraph

A hands-on course in formalizing ordinary mathematics in Lean 4 with Mathlib, written for mathematicians rather than programmers. It starts with rewriting and calculation in rings and orders, then teaches the logical connectives as proof moves (intro, apply, rcases, use, by_contra), sets and functions, and elementary number theory with induction and recursion, including the formula 1 + ⋯ + n = n(n+1)/2. The middle chapters treat finite sets and counting, inductive types, and how structures, classes and algebraic hierarchies are designed in Mathlib (bundled morphisms, sub-objects, quotients); later chapters apply all of this to groups and rings, linear algebra, topology through filters, differential calculus in normed spaces, and measure theory and integration. Each section comes with exercises meant to be done in VS Code alongside the text.

**Contents**

1. [Introduction](ch1): How to install Lean, Mathlib and the exercise files, and how the book is meant to be read: with the editor open, doing exercises.
2. [Basics](ch2): Proving things by calculation: rewriting with equations, using library lemmas, and the first look at how algebraic structures are organized.
3. [Logic](ch3): The logical connectives as moves in a proof: how to prove and how to use each of ∀, →, ∃, ¬, ∧, ↔ and ∨, ending with limits of sequences.
4. [Sets and Functions](ch4): Sets as predicates on a type, functions between types, and a full formal proof of the Schröder–Bernstein theorem.
5. [Elementary Number Theory](ch5): Number theory as a testing ground for induction, recursion and finite sums: irrationality, the sum formula, and infinitely many primes.
6. [Discrete Mathematics](ch6): Finite combinatorics in Mathlib, and how to define and reason about one's own inductive types.
7. [Structures](ch7): How mathematical objects with several components are defined in Lean: structures, algebraic structures as classes, and a worked example.
8. [Hierarchies](ch8): How Mathlib builds hierarchies of classes without duplication or diamonds, bundles morphisms, and treats sub-objects and quotients.
9. [Groups and Rings](ch9): Mathlib's algebra in practice: monoids, groups and their actions, and rings, ideals and polynomials.
10. [Linear algebra](ch10): Linear algebra as Mathlib states it: modules over a field, maps, subspaces, endomorphisms, and matrices with bases.
11. [Topology](ch11): Topology the Mathlib way: filters as the unifying notion of limit, then metric and general topological spaces.
12. [Differential Calculus](ch12): Derivatives, first for real functions and then for maps between normed spaces.
13. [Integration and Measure Theory](ch13): Integration on intervals, measure theory, and the general Bochner integral.


---

## Introduction

How to install Lean, Mathlib and the exercise files, and how the book is meant to be read: with the editor open, doing exercises.

**Getting Started**  
Installing Lean 4, VS Code and the mathematics_in_lean repository; working from a copy of the exercise files and comparing with the solutions folder.  
*Terms:* installation, VS Code, Lake, Mathlib, exercises, solutions  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C01_Introduction.html#getting-started)

**Overview**  
What the book covers and its style: Lean as a language for mathematics, the infoview, and the habit of checking each step interactively.  
*Terms:* dependent type theory, infoview, #check, #eval, goals  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C01_Introduction.html#overview)


---

<a id="ch2"></a>
## Basics

Proving things by calculation: rewriting with equations, using library lemmas, and the first look at how algebraic structures are organized.

**Calculating**  
Rewriting with rw, chaining equations with calc, and the ring tactic for commutative-ring identities over the reals.  
*Terms:* rw, calc, ring, nth_rewrite, mul_comm, mul_assoc  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html#calculating)

**Proving Identities in Algebraic Structures**  
Proving identities from the axioms of a ring or group, with variables and sections, to see what ring automates.  
*Terms:* ring axioms, Group, variable, section, namespace  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html#proving-identities-in-algebraic-structures)

**Using Theorems and Lemmas**  
Applying library theorems with apply and exact, inequalities with le_trans and friends, and the linarith, norm_num and positivity tactics; min, max, abs and divisibility.  
*Terms:* apply, exact, le_trans, linarith, norm_num, positivity, exp_le_exp, abs  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html#using-theorems-and-lemmas)

**More examples using apply and rw**  
More practice with apply and rw on min, max, absolute value, gcd and lcm, and on lattices of divisibility.  
*Terms:* min, max, abs, Nat.gcd, Nat.lcm, dvd  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html#more-examples-using-apply-and-rw)

**Proving Facts about Algebraic Structures**  
Proving facts in partial orders, lattices, ordered rings and metric spaces from their axioms; reading Mathlib's class structure.  
*Terms:* PartialOrder, Lattice, inf, sup, OrderedRing, MetricSpace, dist  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html#proving-facts-about-algebraic-structures)


---

<a id="ch3"></a>
## Logic

The logical connectives as moves in a proof: how to prove and how to use each of ∀, →, ∃, ¬, ∧, ↔ and ∨, ending with limits of sequences.

**Implication and the Universal Quantifier**  
Proving and using ∀ and →: intro, apply, and definitions that unfold to quantified statements, such as bounds and monotonicity.  
*Terms:* intro, apply, ∀, →, upper bound, Monotone, dsimp  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html#implication-and-the-universal-quantifier)

**The Existential Quantifier**  
Proving ∃ with use and using it with rcases or obtain; worked examples with bounds and surjectivity.  
*Terms:* use, rcases, obtain, ∃, anonymous constructor  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html#the-existential-quantifier)

**Negation**  
Negation as implication to False: by_contra, push_neg, contrapose, absurd and exfalso, and classical reasoning.  
*Terms:* ¬, False, by_contra, push_neg, contrapose, exfalso, absurd, Classical  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html#negation)

**Conjunction and Iff**  
Proving and destructuring ∧ and ↔: constructor, anonymous constructor notation, rcases patterns, and iff lemmas in rewriting.  
*Terms:* ∧, ↔, constructor, ⟨_, _⟩, Iff.intro, rcases patterns  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html#conjunction-and-iff)

**Disjunction**  
Proving ∨ with left and right, case splits with rcases, and excluded middle via by_cases.  
*Terms:* ∨, left, right, Or.elim, by_cases, em  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html#disjunction)

**Sequences and Convergence**  
Putting it together: the ε–N definition of convergence, uniqueness of limits, and sums and products of convergent sequences.  
*Terms:* ConvergesTo, ε–N, limit uniqueness, convergent sequences  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html#sequences-and-convergence)


---

<a id="ch4"></a>
## Sets and Functions

Sets as predicates on a type, functions between types, and a full formal proof of the Schröder–Bernstein theorem.

**Sets**  
Sets in Mathlib as predicates: membership, subset, intersection, union, complement, set-builder notation and indexed unions and intersections; ext and the mem lemmas.  
*Terms:* Set, ∈, ⊆, ∩, ∪, complement, set-builder, ⋃, ⋂, ext, mem_setOf  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C04_Sets_and_Functions.html#sets)

**Functions**  
Images and preimages, injectivity and surjectivity, inverse functions and their construction with choice; Cantor's theorem on surjections to the power set.  
*Terms:* image, preimage, Injective, Surjective, invFun, Classical.choose, Cantor  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C04_Sets_and_Functions.html#functions)

**The Schröder-Bernstein Theorem**  
A formal proof that injections both ways give a bijection, built by iterating the two maps and choosing on the image.  
*Terms:* Schröder–Bernstein, bijection, injection, piecewise function  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C04_Sets_and_Functions.html#the-schroder-bernstein-theorem)


---

<a id="ch5"></a>
## Elementary Number Theory

Number theory as a testing ground for induction, recursion and finite sums: irrationality, the sum formula, and infinitely many primes.

**Irrational Roots**  
Irrationality of √2 and of roots of primes, coprimality, primes, and a counting argument with prime factorizations.  
*Terms:* irrational, √2, Nat.Coprime, Nat.Prime, factorization, even_of_even_sqr  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C05_Elementary_Number_Theory.html#irrational-roots)

**Induction and Recursion**  
Natural numbers as an inductive type; factorial and Fibonacci by recursion; induction proofs; finite sums with Finset.sum_range_succ, including the proof that 1 + ⋯ + n = n(n+1)/2 by doubling and dividing.  
*Terms:* Nat, induction, recursion, fac, fib, Finset.range, ∑, sum_range_succ, sum_id, ring, omega  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C05_Elementary_Number_Theory.html#induction-and-recursion)

**Infinitely Many Primes**  
Euclid's proof by factorials and by finite sets; strong induction for prime factors; infinitely many primes congruent to 3 mod 4.  
*Terms:* Euclid, infinitely many primes, strong induction, Finset, filter, primes 3 mod 4  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C05_Elementary_Number_Theory.html#infinitely-many-primes)

**More Induction**  
Further forms of induction: structural recursion with several base cases, strong induction and generalizing the hypothesis, applied to Fibonacci-style definitions.  
*Terms:* strong induction, generalizing, pattern-matching proofs, Fibonacci  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C05_Elementary_Number_Theory.html#more-induction)


---

<a id="ch6"></a>
## Discrete Mathematics

Finite combinatorics in Mathlib, and how to define and reason about one's own inductive types.

**Finsets and Fintypes**  
Finite sets (Finset) and finite types (Fintype): operations, filter, image, sums and products, cardinality, and induction over a finset.  
*Terms:* Finset, Fintype, DecidableEq, filter, image, card, Finset.induction_on, univ  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C06_Discrete_Mathematics.html#finsets-and-fintypes)

**Counting Arguments**  
Counting by products, disjoint unions, images and sums; double counting and the pigeonhole principle.  
*Terms:* card_product, card_union_of_disjoint, card_image_of_injective, double counting, pigeonhole  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C06_Discrete_Mathematics.html#counting-arguments)

**Inductively Defined Types**  
Custom inductive types (lists, binary trees, propositional formulas), defined by structural recursion and reasoned about by induction.  
*Terms:* inductive types, List, BinTree, PropForm, structural recursion, induction  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C06_Discrete_Mathematics.html#inductively-defined-types)


---

<a id="ch7"></a>
## Structures

How mathematical objects with several components are defined in Lean: structures, algebraic structures as classes, and a worked example.

**Defining structures**  
Declaring structures with fields, constructors and projections; extensionality, and proving properties of points and of a standard simplex.  
*Terms:* structure, fields, projections, @[ext], anonymous constructor  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C07_Structures.html#defining-structures)

**Algebraic Structures**  
Algebraic structures (groups and others) as structures and type classes; instances, and why instance search matters.  
*Terms:* class, instance, Group, AddGroup, type class inference  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C07_Structures.html#algebraic-structures)

**Building the Gaussian Integers**  
Defining the Gaussian integers ℤ[i] as a structure, giving it a commutative-ring instance, and proving a Euclidean division property.  
*Terms:* Gaussian integers, GaussInt, CommRing instance, norm, Euclidean domain  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C07_Structures.html#building-the-gaussian-integers)


---

<a id="ch8"></a>
## Hierarchies

How Mathlib builds hierarchies of classes without duplication or diamonds, bundles morphisms, and treats sub-objects and quotients.

**Basics**  
Classes that carry data versus classes that carry properties; extends, to_additive, and forgetful inheritance with default fields to avoid bad diamonds.  
*Terms:* class extends, to_additive, forgetful inheritance, diamonds, default fields  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C08_Hierarchies.html#basics)

**Morphisms**  
Morphisms as predicates versus bundled structures; coercion to functions, morphism classes with outParam, and DFunLike.  
*Terms:* MonoidHom, bundled morphisms, CoeFun, MonoidHomClass, outParam, DFunLike  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C08_Hierarchies.html#morphisms)

**Sub-objects**  
Sub-objects with SetLike, submonoid classes for shared lemmas, the lattice of sub-objects, and quotients by setoids.  
*Terms:* Submonoid, SetLike, SubmonoidClass, ⊓, ⊔, Setoid, quotient, HasQuotient  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C08_Hierarchies.html#sub-objects)


---

<a id="ch9"></a>
## Groups and Rings

Mathlib's algebra in practice: monoids, groups and their actions, and rings, ideals and polynomials.

**Monoids and Groups**  
Monoids and groups, homomorphisms and isomorphisms, subgroups and lattices of subgroups, concrete groups, group actions, quotient groups, and results such as Lagrange and Sylow.  
*Terms:* Monoid, Group, MonoidHom, MulEquiv, Subgroup, MulAction, orbit, stabilizer, quotient group, Lagrange, Sylow  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C09_Groups_and_Rings.html#monoids-and-groups)

**Rings**  
Rings, units, ring morphisms, ideals and quotients, the Chinese remainder theorem, algebras and polynomials.  
*Terms:* Ring, CommRing, units, RingHom, Ideal, quotient ring, Chinese remainder theorem, Algebra, Polynomial  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C09_Groups_and_Rings.html#rings)


---

<a id="ch10"></a>
## Linear algebra

Linear algebra as Mathlib states it: modules over a field, maps, subspaces, endomorphisms, and matrices with bases.

**Vector spaces and linear maps**  
Vector spaces as modules over a field; linear maps, their sums and composites, and linear equivalences.  
*Terms:* Module, vector space, LinearMap, →ₗ, LinearEquiv  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C10_Linear_Algebra.html#vector-spaces-and-linear-maps)

**Subspaces and quotients**  
Subspaces, their lattice, images and preimages under linear maps, and quotient spaces.  
*Terms:* Submodule, span, map, comap, quotient space  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C10_Linear_Algebra.html#subspaces-and-quotients)

**Endomorphisms**  
Endomorphisms, polynomials applied to them, eigenvalues and eigenvectors, and the Cayley–Hamilton theorem.  
*Terms:* Module.End, aeval, eigenvalue, eigenvector, Cayley–Hamilton  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C10_Linear_Algebra.html#endomorphisms)

**Matrices, bases and dimension**  
Matrices, bases and coordinates, the matrix of a linear map, and finite dimension and rank.  
*Terms:* Matrix, Basis, LinearMap.toMatrix, finrank, dimension  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C10_Linear_Algebra.html#matrices-bases-and-dimension)


---

<a id="ch11"></a>
## Topology

Topology the Mathlib way: filters as the unifying notion of limit, then metric and general topological spaces.

**Filters**  
Filters and the Tendsto relation as a single way to talk about limits, neighborhoods and "eventually"; the filter API.  
*Terms:* Filter, Tendsto, atTop, 𝓝, Eventually, ∀ᶠ, Frequently  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C11_Topology.html#filters)

**Metric spaces**  
Metric spaces: balls, open and closed sets, continuity, compactness, uniform continuity and completeness.  
*Terms:* MetricSpace, ball, IsOpen, IsClosed, Continuous, IsCompact, UniformContinuous, Cauchy, complete  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C11_Topology.html#metric-spaces)

**Topological spaces**  
Topological spaces: neighborhoods, continuity, separation, compactness, and how filters tie these together.  
*Terms:* TopologicalSpace, nhds, continuity, separation axioms, compactness  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C11_Topology.html#topological-spaces)


---

<a id="ch12"></a>
## Differential Calculus

Derivatives, first for real functions and then for maps between normed spaces.

**Elementary Differential Calculus**  
Derivatives of real functions: HasDerivAt, deriv, the sum rule, Rolle's theorem and the mean value theorem, and simp for computing derivatives.  
*Terms:* HasDerivAt, DifferentiableAt, deriv, Rolle, mean value theorem  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C12_Differential_Calculus.html#elementary-differential-calculus)

**Differential Calculus in Normed Spaces**  
Normed spaces and continuous linear maps, the operator norm, big-O and little-o comparisons, the Fréchet derivative, smoothness and the local inverse theorem.  
*Terms:* NormedSpace, continuous linear map, operator norm, IsBigO, IsLittleO, HasFDerivAt, fderiv, ContDiff, inverse function theorem  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C12_Differential_Calculus.html#differential-calculus-in-normed-spaces)


---

<a id="ch13"></a>
## Integration and Measure Theory

Integration on intervals, measure theory, and the general Bochner integral.

**Elementary Integration**  
Interval integrals on the reals, the fundamental theorem of calculus, and convolution.  
*Terms:* intervalIntegral, ∫, fundamental theorem of calculus, convolution  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C13_Integration_and_Measure_Theory.html#elementary-integration)

**Measure Theory**  
σ-algebras, measurable sets, measures and outer measures, and "almost everywhere" statements.  
*Terms:* MeasurableSpace, MeasurableSet, Measure, almost everywhere, ∀ᵐ  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C13_Integration_and_Measure_Theory.html#measure-theory)

**Integration**  
The Bochner integral for Banach-space-valued functions, dominated convergence, Fubini, convolution and change of variables.  
*Terms:* Bochner integral, dominated convergence, Fubini, integral_prod, change of variables  
→ [read online](https://leanprover-community.github.io/mathematics_in_lean/C13_Integration_and_Measure_Theory.html#integration)

