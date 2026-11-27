<a id="ch1"></a>
# The condensed Lean proof of RH and GRH: a reading

> riemann-rev · first handout, working draft of 26 November 2026 · readers, writer and referees are AI systems (Claude agents, with an independent AI second reader) · [online PDF](https://nasqret.github.io/riemann-rev/writeup/handout.pdf) · [the PDF in Drive](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view)

PDF page = printed page + 1. The handout reads the **compact edition** of lsernau/grh-lean (`grh-compact`, commit 72fead1), the Claude-written rewrite of Alpöge's proof, unit by unit from the final theorems down. Its own numbering is odd: the eight chapters are I–VIII, and the 47 notes inside them are numbered 0.1–0.47. Each note opens with a summary and a box saying what it proves in full and what it takes as input, and every statement carries a LEAN line naming the declarations it renders. **Read with care:** no human mathematician has refereed it. The handout says plainly that the program check compares quotations and arguments with the source, not their meaning; that the independent kernel build and the dependency export were still pending on 26 November; that the 2,944 background results are quoted rather than read, with 113 compared against a published source; and that four quoted results have no identified published counterpart in the form needed (see the Summary). Each chapter and section below links to its page in the [online PDF](https://nasqret.github.io/riemann-rev/writeup/handout.pdf) and gives its range in the Drive copy. For the original archive and the earlier Dupuy notes, see [Notes on Alpöge's Proof](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes) and [Math Deep Dives › RH](https://vwulf.github.io/ettuge/Deep-Dives/math/ch3#rh-rewrite). Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A 1,353-page mathematical reading of the 113,000-line compact Lean proof of RH and GRH for Dirichlet L-functions, produced by AI agents that rewrote each of the code's 24 units as mathematics from 986 program-checked structured proofs. The argument runs top-down: A, B and C give the main inequality, the main inequality gives a one-sided bound for primes, that bound gives the zero-free half-plane, and the half-plane gives the five theorems. Primes enter through a remainder R(x) of a weighted prime sum that counts only primes not split in K = ℚ(√−d). Because zeros of L(s, ξ) and of the twists L(s, ξχ_K) enter its Laplace transform with opposite signs, Landau's theorem on non-negative functions turns an *upper* bound R(x) ≤ x^(8ε−1/2) into a zero-free half-plane; the prime d is chosen so its twists have no zeros in a box. The bound comes from one covolume bounded from two sides over a CM field E = K(ζ). Theorem A says Poincaré series of ramified columns have short, nearly integral images under a chain of m ≈ √x theta lifts (via a seesaw identity and the divisibility of jets of CM theta functions at non-split primes). Theorem B says few translates of these Poincaré series span almost all rows (a Petersson-type second moment with Bessel functions and a sieve). Theorem C says integral forms cannot be that short (lift volumes as Hecke L-values, an exchange identity, heights indexed by embeddings, twists chosen through Selmer groups by Ribet's method, Taylor–Wiles primes and Kisin modules). The main amounts cancel and the saving x^(−1/2) is 1/m. The handout ends with a catalogue of the 2,944 quoted background declarations and a record of who checked what.

**Contents**

1. [Summary](ch1): What the formal text claims, the ideas that carry the proof and where they live, how the reading was done, what it does not establish, and how to read it.
2. [Overview of the argument](ch2): A ten-page overview with full definitions: the five theorems and what one must trust, the weighted prime sum and Landau's criterion, the main inequality and where √x enters, the statements of Theorems A, B and C, the twists, what is quoted, and a map from chapters to Lean files.
3. [I. The theorems, and what one must trust](ch3): The root of the argument: the five final theorems and the propositions they prove, and the top unit, where the main inequality is assembled from A, B and C and turned into the one-sided bound and the zero-free half-plane.
4. [II. From a one-sided bound for primes to a zero-free half-plane](ch4): Analytic number theory that closes the argument: the remainder's Laplace transform is meromorphic with residues equal to differences of orders of vanishing, Landau's lemma turns an upper bound for all primes d of a class into a zero-free half-plane, a companion finds a good point in every window, and the last steps of A, B and C.
5. [III. The data: parameters, fields and scales](ch5): The record on which the whole argument runs: the parameters and the CM field, then the admissible data with their scales and sizes, and a proof that such data exist at every large scale.
6. [IV. Heights and twisted lattices](ch6): Heights indexed by embeddings, which let each prime ℓ and embedding use its own auxiliary object; the product formula; a height bound for ratios of Gram determinants; and a linear-algebra lemma that few spread translates nearly span.
7. [V. Theorem A: short forms](ch7): Theorem A, short forms: the chain of theta lifts of a Poincaré series is moved to definite groups by a seesaw identity, where lifts are finite sums of jets of CM theta functions whose size and divisibility at non-split primes can be computed; the excess is paid by the level prime, and losses are recovered on images of Hecke operators.
8. [VI. Theorem B: enough forms](ch8): Theorem B, enough forms: translates of Poincaré series by the finite group of the chosen primes are spread, proved by a Petersson-type second moment whose main term is bounded by local Bessel integrals and a sieve; most of the chapter is the local and archimedean analysis behind that bound.
9. [VII. Theorem C: integral forms are long](ch9): Theorem C, integral forms are long: the volume of the chain of lifts is a product of single-lift volumes governed by Hecke L-values, ratios of twisted to untwisted values have bounded height, an exchange identity completes families to bases, and Galois representations control labels.
10. [VIII. The twists: congruences, Selmer groups, lifting](ch10): The twists: one per embedding, chosen on the Galois side so that the ℓ-adic denominators of the projection to theta lifts stay within budget.
11. [Catalogue of quoted results](ch11): The catalogue of the 2,944 background declarations the argument quotes, by area, each classed as a definition (977), an elementary lemma (1,773), a named theorem (110) or a substantial unnamed result (84), with references and the relation to the published statement where known; 113 entries were checked against a source by the second reader.
12. [Record of checks](ch12): Who checked what as of 26 November: the authors' reported build, axioms, three independent checkers and Comparator; the community's continuous integration (finished runs passed); riemann-rev's source scan (nothing found); its own independent build, interrupted at 9,788 of 9,843 steps by cluster downtime and requeued; the dependency export, still queued; and a mathematician's reading, which nobody has done yet.


---

## Summary

*PDF pp. 2–9* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=2)

What the formal text claims, the ideas that carry the proof and where they live, how the reading was done, what it does not establish, and how to read it. It names the four quoted results that have no identified published counterpart in the form needed: a prime d whose quadratic twists have no zero in a box for all characters at once, a uniform odd-Sha bound for abelian CM fields, a finite detecting set of Galois elements, and relations at split primes.

*Terms:* five theorems, Mathlib statements, one-sided bound, main inequality, Theorems A B C, how it was read, dossiers, structured proofs, AI referee, what is not established, unpublished inputs, zero-free box, odd Sha bound

→ PDF pp. 2–9 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=2)


---

<a id="ch2"></a>
## Overview of the argument

*PDF pp. 10–19* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=10)

A ten-page overview with full definitions: the five theorems and what one must trust, the weighted prime sum and Landau's criterion, the main inequality and where √x enters, the statements of Theorems A, B and C, the twists, what is quoted, and a map from chapters to Lean files.

**1. What is claimed**  
The five theorems; what one must trust: the statement file, Mathlib's definitions and the kernel  
*Terms:* Riemann hypothesis, GRH, trusted base, statement file  
→ PDF p. 10 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=10)

**2. From primes to zeros**  
The weight Λ(ν)(1 − χ_K(ν)) on ν ≡ 1 mod M, the remainder R, its Laplace transform with residues of opposite sign at zeros and at twisted zeros, Landau's criterion, and the choice of d  
*Terms:* weighted prime sum, von Mangoldt, Laplace transform, Landau theorem, quadratic twist  
→ PDF p. 11 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=11)

**3. The main inequality**  
Admissible data, places of E, tops and thick places, the prime sums Ask and rem, the main amount, and the identity writing rem through R at two scales  
*Terms:* admissible data, tops, thick places, prime sum, main amount, budget  
→ PDF pp. 12–13 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=12)

**4. Theorems A, B and C**  
Theorems A (short forms), B (enough forms) and C (integral forms are long), and how Hadamard's inequality and the product formula combine them into m·rem ≤ (log b)²·budget  
*Terms:* Theorem A, Theorem B, Theorem C, Hadamard inequality, product formula  
→ PDF pp. 14–15 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=14)

**5. The twists**  
Twists, one per embedding; anticyclotomic characters of ℓ-power order, Taylor–Wiles primes, odd Sha bounded by one integer, crystalline loss  
*Terms:* anticyclotomic twist, Taylor–Wiles primes, Tate–Shafarevich, crystalline  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=16)

**6. What is quoted**  
What is quoted from the background library, by area, and which results stand without a published counterpart  
*Terms:* background library, quoted results  
→ PDF p. 17 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=17)

**7. A map**  
A map: chapters, units, and the Lean file and lines of each statement  
*Terms:* Lean map  
→ PDF pp. 18–19 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=18)


---

<a id="ch3"></a>
## I. The theorems, and what one must trust

*PDF pp. 20–51* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=20)

The root of the argument: the five final theorems and the propositions they prove, and the top unit, where the main inequality is assembled from A, B and C and turned into the one-sided bound and the zero-free half-plane.

**0.1 The five final theorems, and what one must trust**  
The five final theorems, each a one-line deduction from the zero-free half-plane via the functional equations, and what trusting them gives and does not give  
*Terms:* final theorems, functional equation, trust  
→ PDF pp. 21–26 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=21)

**0.2 The four statements: the Riemann hypothesis and its generalisation to Dirichlet L-functions**  
The four propositions of the statement file, stated in ordinary language, the library objects they name, and why the half-plane statement implies the other three  
*Terms:* statement file, Mathlib zeta, Dirichlet L-function, primitive character  
→ PDF pp. 27–32 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=27)

**0.3 The main inequality, the bound for the primes, and the zero-free half-plane**  
The main inequality m·rem(D) ≤ (log b)²·budget(D) from one covolume bounded from both sides; the one-sided bound R ≤ x^(8ε−1/2) at a good point of a long window; the saving x^(−1/2) as 1/m  
*Terms:* main inequality, covolume, one-sided bound, saving 1/m  
→ PDF pp. 33–51 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=33)


---

<a id="ch4"></a>
## II. From a one-sided bound for primes to a zero-free half-plane

*PDF pp. 52–87* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=52)

Analytic number theory that closes the argument: the remainder's Laplace transform is meromorphic with residues equal to differences of orders of vanishing, Landau's lemma turns an upper bound for all primes d of a class into a zero-free half-plane, a companion finds a good point in every window, and the last steps of A, B and C.

**0.4 From a one-sided bound for primes to a zero-free half-plane**  
Meromorphy and residues of the remainder's transform; the one-sided criterion by Landau's lemma; a good point in every window [v₀, v₀²]; the remainder of the data as a combination of the R; the last steps of Theorems A, B and C  
*Terms:* Laplace transform, residues, order of vanishing, Landau lemma, one-sided criterion, window, Legendre symbol, quadratic twist, endgame  
→ PDF pp. 53–87 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=53)


---

<a id="ch5"></a>
## III. The data: parameters, fields and scales

*PDF pp. 88–125* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=88)

The record on which the whole argument runs: the parameters and the CM field, then the admissible data with their scales and sizes, and a proof that such data exist at every large scale.

**0.5 The parameters and the CM field: places, Frobenius elements, the different**  
Parameters (N₀ a multiple of 18480, d ≡ N₀/2 − 1), the CM field E = K(ζ), its infinite places as a group, Frobenius elements, the ring of integers and a principal different  
*Terms:* parameters, CM field, cyclotomic, infinite places, Frobenius, different, root discriminant  
→ PDF pp. 89–107 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=89)

**0.6 Admissible data: scales, ranks and sizes, and their existence**  
Admissible data: scales log b ≪ x ≪ x₁ ≪ b, m ≈ √x lifts, rank r ≈ x⁵, thick places with no small multiplicative relations; comparison of sizes by exponents; existence by a weak Siegel–Walfisz, a class-group pigeonhole and a Behrend-type construction  
*Terms:* admissible data, scales, ranks, thick places, size exponents, Siegel–Walfisz, Behrend construction  
→ PDF pp. 108–125 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=108)


---

<a id="ch6"></a>
## IV. Heights and twisted lattices

*PDF pp. 126–147* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=126)

Heights indexed by embeddings, which let each prime ℓ and embedding use its own auxiliary object; the product formula; a height bound for ratios of Gram determinants; and a linear-algebra lemma that few spread translates nearly span.

**0.7 Heights and the product formula; few translates nearly span; the height of one Gram determinant**  
Heights for families indexed by (ℓ, ι), the product formula making the bound for the constant family non-negative, the height of a ratio of twisted to untwisted Gram determinants, few translates nearly span, and two auxiliary inequalities  
*Terms:* height, product formula, embeddings, Gram determinant, twisted lattice, index, spreading, Fourier inequality, Hilbert–Schmidt  
→ PDF pp. 127–147 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=127)


---

<a id="ch7"></a>
## V. Theorem A: short forms

*PDF pp. 148–415* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=148)

Theorem A, short forms: the chain of theta lifts of a Poincaré series is moved to definite groups by a seesaw identity, where lifts are finite sums of jets of CM theta functions whose size and divisibility at non-split primes can be computed; the excess is paid by the level prime, and losses are recovered on images of Hecke operators.

**0.8 The seesaw identity for the chain of theta lifts**  
The seesaw identity: up to one constant, the chain of lifts of a column's Poincaré series is a combination of chains of definite theta lifts, with denominators only at the twist's conductor  
*Terms:* seesaw identity, Poincaré series, Bessel period, conductor  
→ PDF pp. 149–188 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=149)

**0.9 Two consecutive theta lifts: admissible combinations, arrow pairs and zero terms**  
Two consecutive lifts at once: admissible combinations, arrow pairs and their zero terms, Gauss-sum translates of vacua  
*Terms:* admissible combinations, arrow pair, Weil representation, vacuum  
→ PDF pp. 189–220 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=189)

**0.10 Chains of definite theta lifts and the Gauss-sum operator at the level prime**  
At the level prime N: the Gauss-sum operator F, which slides through a chain of lifts, and what its powers cost in integrality  
*Terms:* Gauss-sum operator, level prime  
→ PDF pp. 221–247 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=221)

**0.11 The characters, the level prime and the index sets of the data; the grid spaces**  
The chosen objects of the data: chosen places, characters of U(1) via Weil's criterion, the level N with m log b ≤ log N ≤ 30 m log b, the finite group G(D), the grid spaces  
*Terms:* chosen places, Hecke characters, Weil criterion, level window  
→ PDF pp. 248–273 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=248)

**0.12 Theta functions of a CM elliptic curve: periods, tight frames, conjugates and divisibility of jets**  
Theta functions of a CM elliptic curve: tight frames, conjugates, integrality, and jets divisible at inert or ramified primes by an explicit and nearly sharp power of p; the ask, gain and loss  
*Terms:* CM elliptic curve, theta function, jets, formal group, inert prime, tight frame  
→ PDF pp. 274–316 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=274)

**0.13 Columns on a definite unitary group: divisibility and size of the chain of theta lifts**  
Columns on a definite unitary group: integral small spanning columns, divisibility of the chain by p^gain on a small-index submodule, regained on scaled Hecke images; the size bound  
*Terms:* algebraic modular forms, divisibility, Hecke operators, size  
→ PDF pp. 317–362 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=317)

**0.14 Elementary divisors of a Frobenius-twisted Hecke operator**  
Elementary divisors of a Frobenius-twisted Hecke operator: a root lemma (zeros against degree, Stepanov-style), dimension bounds, an approximate projector, normal forms  
*Terms:* elementary divisors, root lemma, Stepanov, Levi subgroup  
→ PDF pp. 363–403 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=363)

**0.15 A crude bound for a class number, and divisibility of indices of submodules**  
A crude class-number bound for a hermitian genus, and a calculus for indices of submodules dividing an element  
*Terms:* class number, genus, Hermite normal form, index  
→ PDF pp. 404–415 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=404)


---

<a id="ch8"></a>
## VI. Theorem B: enough forms

*PDF pp. 416–796* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=416)

Theorem B, enough forms: translates of Poincaré series by the finite group of the chosen primes are spread, proved by a Petersson-type second moment whose main term is bounded by local Bessel integrals and a sieve; most of the chapter is the local and archimedean analysis behind that bound.

**0.16 Translates of Poincaré series fill the rows: the second moment over the level group and the filling theorem**  
The filling theorem: the second moment over the level group, its unfolding into amplitude sums, the main term bounded with constant 1, and Theorem B by a greedy choice of translates  
*Terms:* filling theorem, second moment, Petersson, greedy choice  
→ PDF pp. 417–460 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=417)

**0.17 The top floor at a finite place: finite Bessel functions, shell bounds and the top kernel**  
Finite Bessel functions at a finite place, the shell bound, decay in frequency, and the positive top kernel  
*Terms:* finite Bessel function, shell bound, top kernel  
→ PDF pp. 461–485 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=461)

**0.18 From amplitude sums to local correlations: filling levels at finitely many places, and the filling data of the admissible data**  
The dictionary from amplitude sums to local correlations at finitely many places; unfolding over double cosets; the filling data of the admissible data  
*Terms:* amplitude sums, local correlations, unfolding  
→ PDF pp. 486–507 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=486)

**0.19 Links of pairs of terms: integral lifts and the discriminant gain**  
Links of pairs of terms: the discriminant gain from integral lifts, by bordered determinants, Jacobi's identity and a Liouville-type inequality  
*Terms:* discriminant gain, Jacobi identity, Liouville inequality  
→ PDF pp. 508–523 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=508)

**0.20 The filling data: Bessel subgroups, links of frames, Siegel's lemma and strong approximation**  
The filling data set-up: Bessel subgroups, links of frames as Lagrangians, Siegel's lemma for hermitian lattices, strong approximation  
*Terms:* Bessel subgroup, Siegel lemma, strong approximation  
→ PDF pp. 524–565 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=524)

**0.21 Box partitions of arithmetic unipotent groups: frame counts, the covolume, amplitude sums**  
Box partitions of arithmetic unipotent groups: frame counts, the exact covolume, amplitude sums and their properties  
*Terms:* unipotent group, covolume, frame count  
→ PDF pp. 566–599 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=566)

**0.22 The energy of amplitude sums: Schur's test on thin classes, block bounds, incoherent and degenerate pairs**  
The energy of amplitude sums: Schur's test on thin classes, block bounds, negligible incoherent and degenerate pairs  
*Terms:* Schur test, energy, degenerate pairs  
→ PDF pp. 600–641 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=600)

**0.23 Poincaré series of cut Bessel functions: unfolding, one-sided Poisson summation, the adelic sieve, standard levels**  
Poincaré series of cut Bessel functions: convergence and unfolding, one-sided Poisson summation as a sieve, standard levels, Weyl's dimension formula  
*Terms:* Poisson summation, adelic sieve, Weyl dimension formula  
→ PDF pp. 642–677 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=642)

**0.24 The tower method at a place: floor measures, gauges and the bounds on each floor**  
The tower method at a place: floors, floor measures convolving to Haar measure, gauges, Cauchy–Schwarz and Plancherel on each floor  
*Terms:* tower method, floor measures, Plancherel  
→ PDF pp. 678–704 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=678)

**0.25 The local theorem for floor forms and the band limits at the complex place**  
The local theorem for floor forms and the band limits at the complex place  
*Terms:* floor forms, band limits  
→ PDF pp. 705–732 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=705)

**0.26 The complex place: the open-cell chart, the Haar measure of the tower, the Bessel cut and the volume weight**  
The complex place: the open-cell chart and its Jacobian, the tower measure as Haar measure, the Bessel cut, a Hua-type kernel  
*Terms:* open-cell chart, Haar measure, Hua kernel  
→ PDF pp. 733–758 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=733)

**0.27 Discrete series coefficients near the identity, Laplace's method for two coefficients, and Bessel functions with a peak**  
Discrete series coefficients near the identity, Laplace's method for two coefficients, Bessel functions with a peak, and periods against deep-level Poincaré series  
*Terms:* discrete series, Flensted-Jensen, Laplace method  
→ PDF pp. 759–796 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=759)


---

<a id="ch9"></a>
## VII. Theorem C: integral forms are long

*PDF pp. 797–1074* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=797)

Theorem C, integral forms are long: the volume of the chain of lifts is a product of single-lift volumes governed by Hecke L-values, ratios of twisted to untwisted values have bounded height, an exchange identity completes families to bases, and Galois representations control labels.

**0.28 The volume of the chain of theta lifts as a product of lift volumes**  
The volume of the chain as a constant power times a product of m single-lift volumes, by a coset-sum Rallis inner product formula  
*Terms:* chain volume, lift volume, Rallis inner product formula  
→ PDF pp. 798–808 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=798)

**0.29 Auxiliary dual pairs, determinant polynomials and the carrier: the explicit matching of theta kernels**  
Auxiliary dual pairs, determinant polynomials, the carrier, and the explicit matching of theta kernels with constants given by Hecke L-values  
*Terms:* dual pair, carrier, theta kernel matching, Hecke L-values  
→ PDF pp. 809–834 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=809)

**0.30 Glued lattices, product forms and the integral comparison forms**  
Glued lattices, product forms and integral comparison forms valid for all twists at once  
*Terms:* glued lattice, comparison forms  
→ PDF pp. 835–860 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=835)

**0.31 The height of a ratio of lift volumes: twisted theta forms on one line and Hecke values**  
The height of a ratio of lift volumes: twisted theta forms on one line, detection of good forms, and the height of inverse ratios of Hecke values  
*Terms:* height of ratio, Hecke values, good forms  
→ PDF pp. 861–889 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=861)

**0.32 Partner data, vanishing on standard data, and the exchange identity at the top of the tower**  
Partner data and the exchange identity at the top of a tower: proportional theta integrals with constant a product of Hecke L-values  
*Terms:* exchange identity, partner data  
→ PDF pp. 890–924 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=890)

**0.33 The exchange theorem, one square of lifts, and the triangle of lifts and descents**  
The exchange theorem in general, one square of lifts, the triangle of lifts and descents, and injectivity of the composite lift  
*Terms:* exchange theorem, square of lifts, descent  
→ PDF pp. 925–956 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=925)

**0.34 The grid of lifts and descents, and the crude rows**  
The grid of lifts and descents and the crude rows that complete a family to a basis  
*Terms:* grid, crude rows, basis  
→ PDF pp. 957–981 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=957)

**0.35 Good forms and rows: equal Hecke traces on unitary groups that differ at the real places**  
Good forms and rows: equal Hecke traces on unitary groups differing only at real places, via cubic twists of the good idempotent  
*Terms:* Hecke traces, real places, cubic twist  
→ PDF pp. 982–1005 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=982)

**0.36 Primitive labels of general linear groups over finite fields: the share of bad types and the cubic twist**  
Primitive labels of GL_r over finite fields (Green's characters): the share of bad types and the cubic twist  
*Terms:* Green characters, primitive labels, bad types  
→ PDF pp. 1006–1015 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1006)

**0.37 The test datum of an auxiliary pair, joint harmonics with staircase weights, and the theta lift as a conjugate descent**  
The test datum of an auxiliary pair, staircase harmonics, and the theta lift as a conjugate descent  
*Terms:* Fock vector, staircase, conjugate descent  
→ PDF pp. 1016–1036 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1016)

**0.38 Vanishing of theta descents: reflection sums at the level, a maximum principle for Hecke polynomials, and adding hyperbolic planes**  
Vanishing of theta descents: reflection sums, a maximum principle for Hecke polynomials, climbing the tower  
*Terms:* theta descent, reflection sums, maximum principle  
→ PDF pp. 1037–1055 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1037)

**0.39 Decay of Heisenberg matrix coefficients of homogeneous Fock vectors, uniform in the degree**  
Decay of Heisenberg matrix coefficients of homogeneous Fock vectors, uniform in the degree  
*Terms:* Heisenberg group, Fock model, decay  
→ PDF pp. 1056–1063 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1056)

**0.40 At most one primitive label for a Hecke eigensystem, by attached Galois representations**  
At most one primitive label per Hecke eigensystem, through attached 2-adic Galois representations and tame inertia  
*Terms:* primitive label, Galois representation, tame inertia  
→ PDF pp. 1064–1074 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1064)


---

<a id="ch10"></a>
## VIII. The twists: congruences, Selmer groups, lifting

*PDF pp. 1075–1278* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1075)

The twists: one per embedding, chosen on the Galois side so that the ℓ-adic denominators of the projection to theta lifts stay within budget. Congruences give Selmer classes by Ribet's method; one anticyclotomic twist makes all Selmer groups short for m powers at once; Taylor–Wiles primes are added one at a time; the loss at ℓ is controlled through Kisin modules.

**0.41 Columns and rows as Galois representations: labels at the chosen places, anticyclotomic characters at new primes, families of L-values and the crystalline loss at one place**  
Columns and rows as conjugate self-dual ℓ-adic representations; labels, anticyclotomic characters at new primes, families of L-values, and the crystalline loss at one place  
*Terms:* Galois representations, conjugate self-dual, labels, anticyclotomic character, crystalline loss  
→ PDF pp. 1076–1118 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1076)

**0.42 Short Selmer groups after one anticyclotomic twist, balanced rows, and Ribet's lemma to first order**  
Short Selmer groups after one anticyclotomic twist, balanced rows, and Ribet's lemma to first order  
*Terms:* Selmer group, balanced rows, Ribet lemma  
→ PDF pp. 1119–1145 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1119)

**0.43 A fit family of twists exists: Ribet's method with tied primes, triangular Taylor–Wiles primes and the denominator of the projection to theta lifts**  
A fit family of twists exists: Ribet's method with tied primes, triangular Taylor–Wiles primes, and the denominator of the projection  
*Terms:* fit family, Taylor–Wiles primes, congruence denominator  
→ PDF pp. 1146–1172 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1146)

**0.44 A Taylor–Wiles prime at a time: ties of tame inertia to Frobenius and the denominator of the projection**  
One Taylor–Wiles prime at a time: ties of tame inertia to Frobenius and the denominator  
*Terms:* tame inertia, Frobenius, tie  
→ PDF pp. 1173–1199 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1173)

**0.45 Exponents of elements of Kisin modules, the cost of deepening them, and cokernel killers**  
Exponents of elements of Kisin modules, the cost of deepening them, and cokernel killers  
*Terms:* Kisin module, Breuil–Kisin, exponents  
→ PDF pp. 1200–1225 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1200)

**0.46 Cup products of crystalline classes vanish up to a power of p: the walk along Frobenius orbits**  
Cup products of crystalline classes vanish up to a power of p, by a walk along Frobenius orbits  
*Terms:* cup product, Artin–Schreier–Witt, Frobenius orbits  
→ PDF pp. 1226–1248 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1226)

**0.47 Crystalline classes with few low weights, sparse large weights and tame types: a length bound and rank-free exponents**  
Crystalline classes with few low weights and sparse large weights: a length bound and rank-free exponents for tame types  
*Terms:* crystalline classes, Hodge–Tate weights, tame type  
→ PDF pp. 1249–1278 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1249)


---

<a id="ch11"></a>
## Catalogue of quoted results

*PDF pp. 1279–1352* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1279)

The catalogue of the 2,944 background declarations the argument quotes, by area, each classed as a definition (977), an elementary lemma (1,773), a named theorem (110) or a substantial unnamed result (84), with references and the relation to the published statement where known; 113 entries were checked against a source by the second reader.

**Adelic**  
Adelic  
*Terms:* adelic unfolding, measures  
→ PDF pp. 1280–1290 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1280)

**Analytic**  
Analytic  
*Terms:* Landau, Siegel–Walfisz, prime number theorem  
→ PDF pp. 1291–1293 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1291)

**CM**  
CM  
*Terms:* complex multiplication, Chowla–Selberg  
→ PDF pp. 1294–1298 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1294)

**ClassField**  
Class field theory  
*Terms:* Artin reciprocity, Chebotarev, Greenberg–Wiles  
→ PDF pp. 1299–1307 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1299)

**Cyclotomic**  
Cyclotomic  
*Terms:* Stickelberger, Kolyvagin, odd Sha  
→ PDF p. 1308 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1308)

**DiscreteSeries**  
Discrete series  
*Terms:* discrete series  
→ PDF pp. 1308–1315 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1308)

**GLn**  
GL_n  
*Terms:* general linear group  
→ PDF p. 1316 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1316)

**GaloisRep**  
Galois representations  
*Terms:* eigenform Galois representations  
→ PDF pp. 1317–1323 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1317)

**General**  
General  
*Terms:* general algebra  
→ PDF pp. 1324–1327 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1324)

**LocalGL**  
Local GL  
*Terms:* Green characters, Shintani  
→ PDF pp. 1328–1333 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1328)

**PadicComparison**  
p-adic comparison  
*Terms:* crystalline comparison  
→ PDF p. 1334 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1334)

**PadicHodge**  
p-adic Hodge theory  
*Terms:* Kisin modules, Bloch–Kato  
→ PDF pp. 1334–1338 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1334)

**Shimura**  
Shimura varieties  
*Terms:* Shimura variety, Eichler–Shimura  
→ PDF pp. 1339–1340 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1339)

**SiegelWeil**  
Siegel–Weil  
*Terms:* Siegel–Weil, Rallis  
→ PDF pp. 1341–1344 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1341)

**Weil**  
Weil representation  
*Terms:* Weil representation, theta  
→ PDF pp. 1345–1352 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1345)


---

<a id="ch12"></a>
## Record of checks

*PDF p. 1353* · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1353)

Who checked what as of 26 November: the authors' reported build, axioms, three independent checkers and Comparator; the community's continuous integration (finished runs passed); riemann-rev's source scan (nothing found); its own independent build, interrupted at 9,788 of 9,843 steps by cluster downtime and requeued; the dependency export, still queued; and a mathematician's reading, which nobody has done yet.

*Terms:* record of checks, kernel, nanoda, con-leche, con-ron, Comparator, continuous integration, source scan, independent build, dependency export, no human reading

→ PDF p. 1353 in [the PDF](https://drive.google.com/file/d/1Ga4jiIxy1tTtW1BXmKNOw57tWEvrFDjD/view) · [read online](https://nasqret.github.io/riemann-rev/writeup/handout.pdf#page=1353)

