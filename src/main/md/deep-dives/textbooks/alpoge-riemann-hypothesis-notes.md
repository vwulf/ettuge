<a id="ch1"></a>
# Notes on Alpöge's Proof of the Riemann Hypothesis

> AI-generated lecture notes (Claude Fable 5.2 and Claude Opus 5.5 in Claude Code), printed by Taylor Dupuy · 21 November 2026 · [original PDF](https://tdupu.github.io/riemann-public/riemann-book.pdf) · [the PDF in Drive](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view)

PDF page = printed page + 14 (printed page 1, the start of the Introduction, is PDF page 15). The preface (PDF 7) and Alpöge's four-page note, which the book reproduces in full (PDF 9–14), are not broken out; nor is the bibliography (PDF 263–271). **Read with care:** the book says on its first page that AI agents wrote it, that no human has reviewed it, and that it does not verify the argument or the Lean archive. It proves the main theorem only relative to twenty black boxes, and gives complete proofs for just a few of them (its Table 3.3, PDF 135). Its account of the archive comes from reading the Lean source as text; the archive was not built. The Lean archive itself was declared verified by the Lean and Mathlib communities on 21 November; see [Math Deep Dives › RH](https://vwulf.github.io/ettuge/Deep-Dives/math/ch3#rh-verified). The public original is at [tdupu.github.io/riemann-public](https://tdupu.github.io/riemann-public/riemann-book.pdf); it is the same file as the Drive copy (same name, date and contents), and each chapter and section below links straight to its page there. Summaries are in our own words; the text stays in the PDF.

### What the 25 November rewrite changes

These notes describe Alpöge's original archive, which the community verified and which now sits on branch [`alpoge`](https://github.com/leanprover-community/riemann-hypothesis/tree/alpoge). On 25 November the community repo's `main` became a **rewrite** of that proof, written by Claude ([lsernau/grh-lean](https://github.com/lsernau/grh-lean)): a readable edition of about 300,000 lines of code (477,124 lines in all, against 17.4 million in Alpöge's 175,187-file archive) and a compact one of about 76,000 lines of code (112,827 in all) on branch `grh-lean`. It keeps the method, proves many steps differently, and reports acceptance by nanoda, con-leche, con-ron and Comparator with only the three standard axioms; the community has not yet repeated its review for it. Chapter by chapter (from the rewrite's `GUIDE.md` and file list):

- [Ch 1](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch2) (the idea) holds and becomes literal: CM theta jets divisible at inert primes, m ∈ [√x, 2√x] lifts, a chain of theta lifts and a seesaw identity are the proof itself, and Stepanov's count appears in it. [Ch 2](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch3) is unaffected.
- [Ch 3](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch4) needs a new skeleton: Theorems A (short forms), B (enough forms) and C (integral forms are long) give one main inequality, then R_q₀(x) ≤ x^(−1/2+ε), then GRH. The black-box status table and open points describe the old code.
- [Ch 4](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch5): no windows. The bound holds for all large x; the criterion is of ordinary Landau type, with real zeros handled by choosing a prime d whose quadratic twists have no zeros in a box (a zero-density count from Pólya–Vinogradov).
- [Ch 5](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch6): largely replaced by one CM field E = K(ζ_q₁), K = ℚ(√−d). [Ch 6](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch7): recast as weighted prime sums at a- and b-places with "gains".
- [Ch 7](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch8): the tower and lifts survive; slope records, the frame theorem and Bost's inequality give way to twisted lattices (heights, index, covolume, product formula).
- [Ch 8](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch9): **gone.** No resolution of singularities, Arakelov geometry, Moriwaki, compactifications, vanishing theorems or prismatic theory. Theorem B (spanning by a second moment: Petersson-type trace formula, Bessel functions, Kloosterman sums, a sieve) and Theorem C (determinants of theta lifts, Rallis norms, an exchange identity, Hecke L-values as squared norms) replace it.
- [Ch 9](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch10): becomes the main inequality, without windows; 1/2 still comes from m ≈ √x.
- [Ch 10](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch11): a uniform bound for the odd part of Sha from Stickelberger and a Kolyvagin system of Jacobi sums, plus anticyclotomic twists with small Selmer groups (Greenberg–Wiles). The Vandiver-strength gap, and the reason for windows, disappear.
- [Ch 11](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch12): weaker and differently sourced: representations match Hecke polynomials for most Frobenii only, with no Weil–Deligne representation or local Langlands; built from Shimura varieties, crystalline comparison, Kisin modules and base change for definite unitary groups.
- [Ch 12](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch13): Green's characters and Behrend's sparse sets survive; the window-matching question is moot. [Appendix A](https://vwulf.github.io/ettuge/Deep-Dives/textbooks/alpoge-riemann-hypothesis-notes/ch14)'s findings about the archive describe the original only.

A four-page [riemann-rev note](https://nasqret.github.io/riemann-rev/summary/grh-condensed-summary.pdf) (26 Nov, unsigned) maps the compact edition the same way: Landau's positivity criterion; a main inequality m·rem ≤ f·a·(log b)⁵ with m ≈ √x, so "the saving x^(−1/2) is 1/m"; and Theorems A and B (upper bound) against C (lower bound), whose main terms cancel. Two points it adds: Alpöge's route through Ferrero–Washington is used in neither edition, the odd Tate–Shafarevich bound taking that role (the Chapter 10 change above); and of 196 citations in the rewrite's REFERENCES.md, 57 were compared with their sources. It calls itself a map of the code, not a verification, and says no mathematician has read the proof through.

## The book in one paragraph

The first book-length account of Levent Alpöge's Lean-only proof of RH and GRH for Dirichlet L-functions, written for professional mathematicians and graduate students within a day of the release. It is organised top-down. Chapter 1 explains the idea through Stepanov's elementary proof of RH for curves over finite fields: a function vanishing to order m at every rational point is weighed against its poles. Over the integers the product formula plays the part of 'zeros equal poles' ('divisibility is at most size'), and a chain of about √x theta lifts between definite unitary groups supplies the missing multiplicity. Chapter 2 gives the finite-field model in full (Stepanov–Bombieri), plus a conditional reconstruction of the 'sign-only' identity qN = M^k + R from Alpöge's footnote. Chapter 3 states the main theorem and proves it from twenty black boxes. Chapters 4–12 treat those boxes: a windowed Landau criterion for smoothed Chebyshev functions, CM host fields and averaging over auxiliary primes, the balance identity, Hermitian lattices with Bost slopes and the theta tower, the covolume bound (where arithmetic geometry enters), the Chebyshev inequality on windows (where the exponent 1/2 comes from balancing x/m against m), Tate–Shafarevich groups of Tate twists, Galois representations with truncated local–global compatibility, and the existence of families. An appendix documents the agents, reviews and token costs. The book is careful about what it does not establish: it marks every statement as a full proof, an outline of Alpöge's route, a description of inputs or an explanatory sketch, and lists the points it leaves open.

**Contents**

1. [Introduction](ch1): States the main theorem (RH plus GRH for Dirichlet L-functions), sketches the idea and the four-part structure of the proof, and is explicit that the notes explain the argument rather than verify it.
2. [Chapter 1. The basic idea](ch2): An informal overview of the whole argument by analogy with Stepanov's proof, with proofs of only the elementary steps and pointers to where each step is developed.
3. [Chapter 2. The function-field model: Stepanov–Bombieri and the sign-only proof](ch3): The finite-field model in full: a complete Stepanov–Bombieri proof of RH for curves, then a conditional reconstruction of Alpöge's 'sign-only' argument, ending in a dictionary that rates how well each step transfers to the integers.
4. [Chapter 3. The argument assembled](ch4): States the main theorem and proves it in a few lines from twenty black boxes, each restated with its role and the chapter that treats it, then records exactly what the book does and does not establish for each.
5. [Chapter 4. Smoothed Chebyshev functions and a windowed Landau criterion](ch5): The analytic end: a one-sided bound for a positive combination of smoothed twisted Chebyshev functions, assumed only on windows [Y, Y^(1+δ)], already forces a zero-free half-plane.
6. [Chapter 5. Host fields and averaging over auxiliary primes](ch6): Builds the CM host fields in which a primitive character ψ is placed, and controls the unwanted characters of their Galois groups by averaging over two auxiliary primes.
7. [Chapter 6. The balance identity and Fourier analysis on the Galois group](ch7): Proves the balance identity, which writes a Legendre-type prime sum as a main term plus twisted Chebyshev functions, and outlines the core bound that turns a bound on the prime sum into a bound on the combination G.
8. [Chapter 7. Hermitian lattices, the theta tower and slope records](ch8): The geometric side: the tower of unitary groups and the chain of theta lifts over a host field, Hermitian lattices and their slopes, and the 'slope record' through which the geometry reaches the analysis.
9. [Chapter 8. Families and the covolume bound](ch9): Collects packages into families and states the covolume bound for lattices of integral automorphic forms, the single place where arithmetic geometry enters.
10. [Chapter 9. The Chebyshev inequality on windows](ch10): Proves the Chebyshev inequality on windows: for a family tied at every large scale, G(x) ≤ x^(1/2+O(ε)); the exponent 1/2 is the balance of x/m against m at m = √x.
11. [Chapter 10. Tate–Shafarevich groups of Tate twists](ch11): States a uniform bound for Tate–Shafarevich groups of the Tate twists Q_ℓ/Z_ℓ(−e) over host fields, which controls the congruence defects of the theta chain; it holds only on windows.
12. [Chapter 11. Galois representations and local–global compatibility](ch12): States the Galois-theoretic input: weak local Langlands maps and a truncated local–global compatibility for regular algebraic polarized cuspidal representations over CM fields, which the archive proves rather than assumes.
13. [Chapter 12. Existence of families](ch13): The existence results: host fields on windows, Green's parametrisation, admissible families, and from them zero-freeness of L(s, ψ) for primitive ψ in Re s > 1/2.
14. [Appendix A. Software and AI methods](ch14): How the book was made: agents, models, sources, reviews, computations, literature checks, the static reading of the Lean archive, and token accounting.


---

## Introduction

*PDF pp. 15–22* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=15)

States the main theorem (RH plus GRH for Dirichlet L-functions), sketches the idea and the four-part structure of the proof, and is explicit that the notes explain the argument rather than verify it.

**The main theorem**  
The theorem: every nontrivial zero of ζ and of every Dirichlet L-function lies on Re s = 1/2; proved relative to 20 black boxes, of which the book fully proves only a few  
*Terms:* Riemann hypothesis, GRH Dirichlet, main theorem, black boxes  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=15)

**The idea of the argument**  
The idea: Stepanov's zeros-against-poles over F_q, its integer analogue via the product formula (Chebyshev's binomial bound as the multiplicity-one case), and a one-sided bound on a smoothed Chebyshev function as the target  
*Terms:* Stepanov method, product formula, Chebyshev binomial bound, smoothed Chebyshev function, von Mangoldt  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=16)

**The structure of the proof**  
Four parts: the analytic end (windowed Landau criterion), the inequality (host fields, balance identity, theta tower, covolume, gap bound), the arithmetic inputs (Sha bound, Galois representations) and existence of families  
*Terms:* windowed Landau criterion, host fields, theta lifts, slope inequality, Sha bound  
→ PDF pp. 17–18 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=17)

**What is proved in these notes**  
What kind of argument each statement gets, and the two main open points: matching the window exponents of the Sha bound and the host supply, and an unproved étale-vanishing hypothesis in the sign-only model  
*Terms:* proof kinds, open points, window exponents  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=19)

**Prerequisites and conventions**  
Background assumed: curves and Riemann–Roch, ℓ-adic cohomology for the sign-only part, analytic number theory, Hermitian lattices, theta correspondence, Shimura varieties, Galois cohomology  
*Terms:* prerequisites, Riemann–Roch, theta correspondence, Poitou–Tate  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=20)

**Organization of the notes**  
Reading order and the chapter-to-step map (Figure I.1)  
*Terms:* reading map  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=20)

**AI and Software Discussion**  
AI disclosure: drafted and assembled by Claude Fable 5.2 and Claude Opus 5.5 in Claude Code on 20–21 Nov 2026; no human review  
*Terms:* AI disclosure, Claude Fable, Claude Opus, no human review  
→ PDF pp. 21–22 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=21)


---

<a id="ch2"></a>
## Chapter 1. The basic idea

*PDF pp. 23–44* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=23)

An informal overview of the whole argument by analogy with Stepanov's proof, with proofs of only the elementary steps and pointers to where each step is developed.

**1.1. Stepanov's method over a finite field**  
Stepanov–Bombieri bound N ≤ q + (2g+1)√q: an auxiliary function built by Riemann–Roch linear algebra vanishes to order m (a power of p) at each rational point; counting zeros against poles, with m ≈ √q  
*Terms:* Stepanov method, Bombieri, Weil bound, Riemann–Roch, auxiliary function, multiplicity  
→ PDF pp. 23–26 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=23)

**1.2. The dictionary**  
The dictionary curve ↔ integers: points ↔ primes, multiplicity ↔ divisibility, poles ↔ archimedean size, zeros = poles ↔ product formula / slope inequality, Frobenius power ↔ chain of theta lifts  
*Terms:* dictionary, product formula, slope inequality, Frobenius  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=27)

**1.3. The quantity to bound**  
The quantity to bound: the smoothed Chebyshev function G_ζ, its Mellin transform, and Landau's theorem showing a one-sided bound G_ζ(x) ≤ x^θ forces ζ ≠ 0 for Re s > θ; why the curve analogue fails (Pringsheim)  
*Terms:* smoothed Chebyshev function G_ζ, Mellin transform, Landau theorem, one-sided bound, Pringsheim  
→ PDF pp. 28–33 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=28)

**1.4. Divisibility is at most size**  
Divisibility is at most size: Taylor coefficients of CM theta functions divisible to Legendre-type orders at inert primes; Hermitian lattices, Arakelov degree and Bost's slope inequality  
*Terms:* CM theta function, Legendre formula, inert primes, Hermitian lattice, Arakelov degree, Bost slope inequality  
→ PDF pp. 34–38 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=34)

**1.5. Multiplicity is the bottleneck**  
Why one CM abelian variety stalls at 3/4 and why the exponent 1/2 forces a multiplicity m ≈ √x  
*Terms:* exponent 3/4, chain length √x, exponent budget  
→ PDF p. 39 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=39)

**1.6. Theta lifts instead of differentiating integers**  
Theta lifts between definite unitary groups (Gross's algebraic modular forms) as the integer substitute for 'differentiating integers'; each lift collects the forced divisibility again  
*Terms:* theta lift, unitary group, algebraic modular forms, Gross, Rallis inner product, seesaw  
→ PDF pp. 40–42 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=40)

**1.7. What the outline omits, and where to read on**  
What the outline leaves out: host fields, congruence defects bounded by Sha groups, Galois representations, existence of families; not a verification  
*Terms:* host fields, congruence defects, Tate–Shafarevich, Vandiver  
→ PDF pp. 43–44 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=43)


---

<a id="ch3"></a>
## Chapter 2. The function-field model: Stepanov–Bombieri and the sign-only proof

*PDF pp. 45–108* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=45)

The finite-field model in full: a complete Stepanov–Bombieri proof of RH for curves, then a conditional reconstruction of Alpöge's 'sign-only' argument, ending in a dictionary that rates how well each step transfers to the integers.

**2.1. Setting**  
Function fields over F_q, places, divisors, Riemann–Roch; Weil's theorem as the target  
*Terms:* function field, place, divisor, Riemann–Roch, Weil theorem  
→ PDF pp. 46–48 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=46)

**2.2. The zeta function**  
The zeta function, its rationality and functional equation, the L-polynomial and reciprocal roots  
*Terms:* zeta function, L-polynomial, functional equation, reciprocal roots  
→ PDF pp. 49–51 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=49)

**2.3. The upper bound**  
The upper bound N ≤ q + (2g+1)√q via an adapted basis and the auxiliary section (Bombieri's theorem); the square-root error is forced by the method  
*Terms:* Bombieri theorem, auxiliary section, adapted basis, square-root barrier  
→ PDF pp. 52–63 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=52)

**2.4. Route 1: the lower bound by Galois averaging**  
Route 1 to the lower bound: Galois averaging over twists of a cover, as Bombieri does  
*Terms:* Galois averaging, twists, lower bound  
→ PDF pp. 64–69 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=64)

**2.5. The Riemann hypothesis**  
Combining both bounds to get |α_i| = √q, i.e. RH for curves  
*Terms:* Riemann hypothesis for curves  
→ PDF p. 70 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=70)

**2.6. Route 2: a one-sided bound and a Landau–Pringsheim lemma**  
Route 2: a one-sided bound plus a Landau–Pringsheim lemma, and why it corresponds to a lower bound on point counts (the sign reversal)  
*Terms:* Landau–Pringsheim lemma, one-sided bound, sign reversal  
→ PDF pp. 71–79 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=71)

**2.7. Stepanov's derivative form over a prime field**  
Stepanov's original derivative form over a prime field  
*Terms:* Stepanov derivative form, prime field  
→ PDF pp. 80–84 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=80)

**2.8. The sign-only identity qN = M^k + R**  
The sign-only identity qN = M^k + R for a weighted count on a path quadric  
*Terms:* sign-only identity, qN = M^k + R, path quadric, Gauss sum  
→ PDF pp. 85–87 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=85)

**2.9. Iterated Parseval: the bound on R**  
Bounding R by iterated Parseval  
*Terms:* iterated Parseval  
→ PDF pp. 88–90 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=88)

**2.10. The sign-only theorem**  
The sign-only theorem, conditional on two cohomological hypotheses; one fails for the quadric as written for some k  
*Terms:* conditional theorem, étale cohomology, hypothesis H2  
→ PDF pp. 91–95 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=91)

**2.11. Multiplicity versus sign**  
Multiplicity versus sign as two different resources  
*Terms:* multiplicity versus sign  
→ PDF pp. 96–98 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=96)

**2.12. What the identity is for**  
What the identity is for, and the O(2, n) observation in the note  
*Terms:* O(2 n), Katz, Gabber hypersurface  
→ PDF pp. 99–101 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=99)

**2.13. Dictionary with Alpöge's argument**  
Dictionary with Alpöge's argument: where the analogy is exact, loose or broken  
*Terms:* dictionary, analogy  
→ PDF pp. 102–103 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=102)

**2.14. Remarks and questions**  
Remarks and open questions, including the positivity Weil uses and this route avoids  
*Terms:* Weil positivity, open questions  
→ PDF pp. 104–108 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=104)


---

<a id="ch4"></a>
## Chapter 3. The argument assembled

*PDF pp. 109–138* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=109)

States the main theorem and proves it in a few lines from twenty black boxes, each restated with its role and the chapter that treats it, then records exactly what the book does and does not establish for each.

**3.1. The main theorem**  
Theorem 3.1.1 for all Dirichlet characters; how the archive's final Lean statements relate to it (Mathlib's definitions, primitive characters upstream)  
*Terms:* main theorem, Lean final statements, Mathlib riemannZeta  
→ PDF p. 109 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=109)

**3.2. The skeleton of the proof**  
The skeleton: a one-sided bound for character-weighted smoothed Chebyshev functions on long windows  
*Terms:* skeleton, smoothed Chebyshev, windows  
→ PDF p. 110 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=110)

**3.3. The vocabulary of the black boxes**  
Vocabulary: levels, windows, scales, hosts, packages, families, ties  
*Terms:* levels, windows, scales, hosts, packages, families, ties  
→ PDF pp. 111–114 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=111)

**3.4. Black box: Galois representations**  
Black box: Galois representations and weak local Langlands maps  
*Terms:* Galois representations, weak local Langlands  
→ PDF p. 115 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=115)

**3.5. Black box: the Sha bound on windows**  
Black box: the Sha bound on windows  
*Terms:* Sha bound on windows  
→ PDF p. 116 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=116)

**3.6. Black box: the supply of hosts**  
Black box: supply of hosts and good pairs of auxiliary primes  
*Terms:* host supply, good pairs  
→ PDF p. 117 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=117)

**3.7. Black box: the covolume bound**  
Black box: the covolume bound  
*Terms:* covolume bound  
→ PDF p. 118 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=118)

**3.8. Black box: packages, Green's parametrisation, tied families**  
Black box: packages, Green's parametrisation, tied families  
*Terms:* packages, Green parametrisation, tied families  
→ PDF pp. 119–120 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=119)

**3.9. Black box: the Chebyshev inequality on windows**  
Black box: the Chebyshev inequality on windows, with the m ≈ √x bookkeeping  
*Terms:* Chebyshev inequality on windows, m ≈ √x  
→ PDF pp. 121–125 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=121)

**3.10. Black box: the windowed Landau criterion**  
Black box: the windowed Landau criterion  
*Terms:* windowed Landau criterion  
→ PDF p. 126 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=126)

**3.11. Black box: from a half-plane to the critical line**  
Black box: primitive to imprimitive characters and the functional equation  
*Terms:* imprimitive characters, functional equation, critical line  
→ PDF p. 127 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=127)

**3.12. Proof of the main theorem**  
The six-step proof of the main theorem from the boxes  
*Terms:* proof of main theorem  
→ PDF pp. 127–129 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=127)

**3.13. Chebyshev's comparison and the function-field model**  
Chebyshev's comparison as the common thread with the function-field model  
*Terms:* Chebyshev comparison  
→ PDF pp. 130–132 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=130)

**3.14. The status of the inputs**  
Status of the inputs: Table 3.3 of proof kinds, schematic definitions, static scans of the archive, and the list of open points  
*Terms:* status of inputs, Table 3.3, open points, schematic definitions  
→ PDF pp. 133–138 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=133)


---

<a id="ch5"></a>
## Chapter 4. Smoothed Chebyshev functions and a windowed Landau criterion

*PDF pp. 139–148* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=139)

The analytic end: a one-sided bound for a positive combination of smoothed twisted Chebyshev functions, assumed only on windows [Y, Y^(1+δ)], already forces a zero-free half-plane.

**4.1. Conventions for Chapters 3–12**  
Conventions for Chapters 3–12: attributions and the four kinds of proof block  
*Terms:* proof kinds, attribution conventions  
→ PDF p. 139 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=139)

**4.2. Smoothed Chebyshev functions**  
Smoothed Chebyshev functions twisted by Dirichlet characters and their normalisation  
*Terms:* twisted Chebyshev function, normalisation  
→ PDF p. 140 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=140)

**4.3. The windowed Landau criterion**  
The windowed Landau criterion, proved in outline via Taylor coefficients of a Laplace transform; its novelty is left as a question  
*Terms:* windowed Landau criterion, Laplace transform, Mellin transform  
→ PDF pp. 141–144 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=141)

**4.4. Levels**  
Levels: finite sets of primitive characters closed under inversion, with positive weights so real zeros all push one way  
*Terms:* levels, kept characters, positive weights, real zeros  
→ PDF p. 145 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=145)

**4.5. From a half-plane to the critical line**  
From the half-plane Re s > 1/2 to the critical line, via Euler factors and the functional equation  
*Terms:* functional equation, critical line, imprimitive characters  
→ PDF pp. 146–148 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=146)


---

<a id="ch6"></a>
## Chapter 5. Host fields and averaging over auxiliary primes

*PDF pp. 149–162* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=149)

Builds the CM host fields in which a primitive character ψ is placed, and controls the unwanted characters of their Galois groups by averaging over two auxiliary primes.

**5.1. Frames and hosts**  
Frames and host fields: abelian CM fields containing an imaginary quadratic field, built from ψ and auxiliary primes q, d  
*Terms:* host field, CM field, imaginary quadratic field, frame  
→ PDF pp. 149–150 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=149)

**5.2. Kept and bounded characters**  
Kept versus bounded characters of the host's Galois group  
*Terms:* kept characters, bounded characters  
→ PDF pp. 151–152 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=151)

**5.3. Scales and the explicit-formula condition**  
Scales and the explicit-formula condition  
*Terms:* scales, explicit formula  
→ PDF pp. 153–154 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=153)

**5.4. Averaging over the auxiliary prime**  
Averaging over the auxiliary prime: head sums and boxes, and why most pairs (q, d) are good  
*Terms:* auxiliary primes, averaging, good pairs, head sum  
→ PDF pp. 155–158 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=155)

**5.5. The strength of the analytic input**  
How strong the analytic input is, and which classical results it cites; one uniformity constant is not reconstructed  
*Terms:* analytic input, L'(1 χ)/L(1 χ), uniformity  
→ PDF pp. 159–162 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=159)


---

<a id="ch7"></a>
## Chapter 6. The balance identity and Fourier analysis on the Galois group

*PDF pp. 163–176* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=163)

Proves the balance identity, which writes a Legendre-type prime sum as a main term plus twisted Chebyshev functions, and outlines the core bound that turns a bound on the prime sum into a bound on the combination G.

**6.1. The additive model and arithmetic data**  
The additive model and the arithmetic data; the balance identity by orthogonality of characters on the Galois group  
*Terms:* balance identity, Legendre formula, Fourier analysis on Galois group, orthogonality  
→ PDF pp. 163–168 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=163)

**6.2. Thick and thin weights**  
Thick and thin weights coming from the theta tower's geometry  
*Terms:* thick weights, thin weights  
→ PDF pp. 169–170 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=169)

**6.3. Averaging over shifts and top places**  
Averaging over shifts and top places; the core Chebyshev bound and where the square root appears  
*Terms:* averaging over shifts, top places, core bound, square root  
→ PDF pp. 171–176 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=171)


---

<a id="ch8"></a>
## Chapter 7. Hermitian lattices, the theta tower and slope records

*PDF pp. 177–192* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=177)

The geometric side: the tower of unitary groups and the chain of theta lifts over a host field, Hermitian lattices and their slopes, and the 'slope record' through which the geometry reaches the analysis.

**7.1. The tower of unitary groups and the theta chain**  
The tower of Hermitian spaces and the theta chain U(X_0) → … → U(X_m)  
*Terms:* unitary group tower, theta chain, Hermitian space  
→ PDF pp. 177–179 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=177)

**7.2. Hermitian lattices and slopes**  
Hermitian lattices, slopes and Bost's slope inequality; packages of automorphic data  
*Terms:* Hermitian lattice, slope, Bost inequality, packages  
→ PDF pp. 180–181 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=180)

**7.3. The slope record**  
The slope record: the list of sizes and inequalities the analysis uses  
*Terms:* slope record, size datum  
→ PDF pp. 182–186 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=182)

**7.4. The frame theorem**  
The frame theorem: a rank-weighted comparison of many source lattices with one target lattice  
*Terms:* frame theorem, frame operator  
→ PDF pp. 187–189 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=187)

**7.5. The archimedean side**  
The archimedean side: Stirling terms and a Chowla–Selberg-type CM period  
*Terms:* archimedean side, Stirling, Chowla–Selberg period  
→ PDF p. 190 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=190)

**7.6. The finite side**  
The finite side: Bessel-type periods and the forced divisibility at inert primes  
*Terms:* finite side, Bessel period, divisor bound  
→ PDF pp. 191–192 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=191)


---

<a id="ch9"></a>
## Chapter 8. Families and the covolume bound

*PDF pp. 193–200* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=193)

Collects packages into families and states the covolume bound for lattices of integral automorphic forms, the single place where arithmetic geometry enters.

**8.1. Families and closed properties**  
Families and closed properties: constants fixed before the family is chosen  
*Terms:* families, closed properties, thresholds  
→ PDF p. 193 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=193)

**8.2. The covolume bound**  
The covolume bound and the order in which it fixes its objects  
*Terms:* covolume bound, integral automorphic forms  
→ PDF pp. 194–196 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=194)

**8.3. How arithmetic geometry enters**  
How arithmetic geometry enters: integral models and toroidal compactifications of Shimura varieties, arithmetic Hilbert–Samuel, Moriwaki's bigness theorem, vanishing theorems; each used in a specific, sometimes weakened form; the proof is not reproduced  
*Terms:* arithmetic geometry, Shimura variety, toroidal compactification, arithmetic Hilbert–Samuel, Moriwaki bigness, Arakelov geometry  
→ PDF pp. 197–200 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=197)


---

<a id="ch10"></a>
## Chapter 9. The Chebyshev inequality on windows

*PDF pp. 201–210* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=201)

Proves the Chebyshev inequality on windows: for a family tied at every large scale, G(x) ≤ x^(1/2+O(ε)); the exponent 1/2 is the balance of x/m against m at m = √x.

**9.1. Window hypotheses and ties**  
Window hypotheses and ties between families and slope records  
*Terms:* window hypotheses, ties  
→ PDF pp. 201–203 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=201)

**9.2. The gap bound**  
The gap bound: upper and lower slope clauses cancel the heights  
*Terms:* gap bound, slope clauses, cancellation  
→ PDF pp. 204–206 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=204)

**9.3. The square-root bookkeeping**  
The square-root bookkeeping that picks m ≈ √x  
*Terms:* square-root bookkeeping, chain length m, balance x/m  
→ PDF p. 207 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=207)

**9.4. The Chebyshev inequality on windows**  
The inequality itself, as linear arithmetic once the gap bound is in place  
*Terms:* Chebyshev inequality on windows, exponent 1/2  
→ PDF pp. 208–210 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=208)


---

<a id="ch11"></a>
## Chapter 10. Tate–Shafarevich groups of Tate twists

*PDF pp. 211–228* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=211)

States a uniform bound for Tate–Shafarevich groups of the Tate twists Q_ℓ/Z_ℓ(−e) over host fields, which controls the congruence defects of the theta chain; it holds only on windows.

**10.1. The groups and the bound**  
The groups and the bound  
*Terms:* Tate–Shafarevich, Tate twist, Galois cohomology, Selmer, congruence defects  
→ PDF pp. 211–213 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=211)

**10.2. Eigenspaces and the case split**  
Eigenspaces under the abelian Galois group and the case split by the sign of complex conjugation (proved in full)  
*Terms:* eigenspaces, case split, complex conjugation  
→ PDF pp. 214–216 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=214)

**10.3. The minus part**  
The minus part  
*Terms:* minus part  
→ PDF pp. 217–218 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=217)

**10.4. The plus part**  
The plus part, where bounds of Vandiver/Greenberg strength are needed and no published result of that strength is known; a Kato-type vanishing theorem is used without outline  
*Terms:* plus part, Vandiver conjecture, Greenberg conjecture, Kato vanishing  
→ PDF pp. 219–224 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=219)

**10.5. The Sha bound on windows**  
The Sha bound on windows by a pigeonhole argument, which is why everything else must work on windows  
*Terms:* Sha bound on windows, pigeonhole  
→ PDF pp. 225–228 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=225)


---

<a id="ch12"></a>
## Chapter 11. Galois representations and local–global compatibility

*PDF pp. 229–236* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=229)

States the Galois-theoretic input: weak local Langlands maps and a truncated local–global compatibility for regular algebraic polarized cuspidal representations over CM fields, which the archive proves rather than assumes.

**11.1. Weak local Langlands maps and truncated compatibility**  
Weak local Langlands maps and truncated compatibility (asks less than the published theorems); outline of the construction  
*Terms:* Galois representations, weak local Langlands, local–global compatibility, CM field, polarized cuspidal, Caraiani  
→ PDF pp. 229–233 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=229)

**11.2. A proposition on compact groups**  
A proposition on compact groups used in building the representations, stated without outline  
*Terms:* compact groups, eigenvalues  
→ PDF pp. 234–235 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=234)

**11.3. What the Sha bound uses**  
Exactly what the Sha bound needs from this chapter  
*Terms:* Sha bound inputs  
→ PDF p. 236 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=236)


---

<a id="ch13"></a>
## Chapter 12. Existence of families

*PDF pp. 237–248* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=237)

The existence results: host fields on windows, Green's parametrisation, admissible families, and from them zero-freeness of L(s, ψ) for primitive ψ in Re s > 1/2.

**12.1. The supply of hosts**  
Supply of hosts on windows; whether the scale changes between the Sha windows and the host windows is left open  
*Terms:* host supply, windows, scale  
→ PDF pp. 237–239 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=237)

**12.2. Green's parametrization**  
Green's parametrisation of cuspidal characters of GL_n(F_p), used only for local types  
*Terms:* Green parametrisation, cuspidal characters, GL_n(F_p)  
→ PDF p. 240 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=240)

**12.3. Admissible families**  
Admissible families and tied families  
*Terms:* admissible families, tied families  
→ PDF pp. 241–243 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=241)

**12.4. Zero-freeness for primitive characters**  
Zero-freeness for primitive characters  
*Terms:* zero-free primitive characters  
→ PDF p. 244 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=244)

**12.5. What this chapter supplies to the main proof**  
What the chapter supplies to the main proof  
*Terms:* summary  
→ PDF pp. 245–248 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=245)


---

<a id="ch14"></a>
## Appendix A. Software and AI methods

*PDF pp. 249–262* · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=249)

How the book was made: agents, models, sources, reviews, computations, literature checks, the static reading of the Lean archive, and token accounting.

**A.1. Typesetting**  
Typesetting  
*Terms:* typesetting  
→ PDF p. 250 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=250)

**A.2. Agent management**  
Agent management: a coordinating session with subagents  
*Terms:* agent management, subagents, Claude Code  
→ PDF p. 251 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=251)

**A.3. Natural language proofs**  
Natural-language proofs and what the agents drafted  
*Terms:* natural language proofs  
→ PDF p. 252 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=252)

**A.4. Adversarial reviews**  
Adversarial reviews (Chapters 1–3 had one AI review; 4–12 none as chapters)  
*Terms:* adversarial review  
→ PDF p. 253 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=253)

**A.5. AI assisted computations**  
AI-assisted computations, such as brute-force checks on small curves  
*Terms:* Python checks  
→ PDF p. 254 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=254)

**A.6. AI statement generation**  
AI statement generation  
*Terms:* statement generation  
→ PDF p. 255 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=255)

**A.7. Proofreading and adversarial review**  
Proofreading and adversarial review; results that originated with the agents  
*Terms:* proofreading, agent-originated results  
→ PDF pp. 255–256 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=255)

**A.8. Literature review**  
Literature review against zbMATH, Crossref and arXiv; no prior occurrence found for the windowed Landau criterion  
*Terms:* literature review, zbMATH, novelty  
→ PDF p. 257 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=257)

**A.9. Formalization**  
Formalization: the archive read as text, not built; it contains meta code, mechanical assembly and in-archive proofs of about 190 named theorems  
*Terms:* Lean archive static reading, meta code  
→ PDF p. 258 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=258)

**A.10. Record keeping and token accounting**  
Record keeping and token accounting by task  
*Terms:* token accounting, cost  
→ PDF pp. 259–262 in [the PDF](https://drive.google.com/file/d/1TFLiyKCINPw1_B5mBFz3X3K3W8qfiSX7/view) · [read online](https://tdupu.github.io/riemann-public/riemann-book.pdf#page=259)

