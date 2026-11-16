<a id="ch1"></a>
# Linear Algebra, Theory and Applications

> Kenneth Kuttler · Saylor Foundation / author’s edition, September 2017 (CC BY) · [the PDF in Drive](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

PDF page = printed page. Exercise sections and the appendices (positive matrices, functions of matrices, ODEs, compactness, field extensions, selected answers) are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A thorough undergraduate-to-early-graduate linear algebra text that mixes matrix computation with theory and analysis. It starts from preliminaries (complex numbers, the fundamental theorem of algebra, division algorithm, Fⁿ), covers matrices and linear maps, determinants with Cayley–Hamilton, row operations and rank, LU and QR factorizations, eigenvalues with Schur’s theorem and Gershgorin estimates, abstract vector spaces and fields, canonical forms (Jordan, rational), Markov chains, inner product spaces and least squares, self-adjoint operators with polar decomposition and SVD, norms and iterative methods, and numerical eigenvalue algorithms (power method, QR).

**Contents**

1. [Preliminaries](ch1): Background: numbers, algebra and Fⁿ.
2. [Linear Transformations](ch2): Matrices and linear transformations of Fⁿ.
3. [Determinants](ch3): Determinants.
4. [Row Operations](ch4): Row reduction and rank.
5. [Some Factorizations](ch5): LU and QR factorizations.
6. [Spectral Theory](ch6): Eigenvalues and spectral theory for matrices.
7. [Vector Spaces And Fields](ch7): Abstract vector spaces over fields.
8. [Linear Transformations](ch8): Linear transformations between abstract spaces.
9. [Canonical Forms](ch9): Canonical forms.
10. [Markov Processes](ch10): Markov chains with matrices.
11. [Inner Product Spaces](ch11): Inner product spaces.
12. [Self Adjoint Operators](ch12): Self-adjoint operators and their decompositions.
13. [Norms](ch13): Norms and iterative methods.
14. [Numerical Methods, Eigenvalues](ch14): Numerical eigenvalue algorithms.


---

## Preliminaries

*PDF pp. 11–38*

Background: numbers, algebra and Fⁿ.

**Sets And Set Notation**  
Set notation.  
*Terms:* sets  
→ PDF p. 11 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Functions**  
Functions.  
*Terms:* functions  
→ PDF p. 12 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Number Line And Algebra Of The Real Numbers**  
Real numbers.  
*Terms:* real numbers  
→ PDF pp. 12–13 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Ordered fields**  
Ordered fields.  
*Terms:* ordered field  
→ PDF p. 14 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Complex Numbers**  
Complex numbers.  
*Terms:* complex numbers  
→ PDF pp. 15–17 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Fundamental Theorem Of Algebra**  
Fundamental theorem of algebra.  
*Terms:* fundamental theorem of algebra  
→ PDF pp. 18–19 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Completeness of R**  
Completeness of ℝ.  
*Terms:* completeness  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Well Ordering And Archimedean Property**  
Well-ordering and Archimedean property.  
*Terms:* well ordering, Archimedean  
→ PDF pp. 22–23 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Division**  
Division algorithm and gcds.  
*Terms:* division algorithm, gcd  
→ PDF pp. 24–27 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Systems Of Equations**  
Linear systems.  
*Terms:* linear systems  
→ PDF pp. 28–32 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Fn**  
Fⁿ.  
*Terms:* F^n  
→ PDF p. 34 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Algebra in Fn**  
Vector algebra.  
*Terms:* vector operations  
→ PDF p. 34 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Inner Product In Fn**  
Inner product.  
*Terms:* inner product, Cauchy-Schwarz  
→ PDF pp. 35–37 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**What Is Linear Algebra?**  
What linear algebra studies.  
*Terms:* linear algebra  
→ PDF p. 38 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch2"></a>
## Linear Transformations

*PDF pp. 39–84*

Matrices and linear transformations of Fⁿ.

**Matrices**  
Matrix algebra and inverses.  
*Terms:* matrices, inverse  
→ PDF pp. 39–53 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Linear Transformations**  
Linear maps.  
*Terms:* linear transformation  
→ PDF pp. 56–57 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Some Geometrically Defined Linear Transformations**  
Rotations and projections.  
*Terms:* rotations, projections  
→ PDF pp. 58–60 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Null Space Of A Linear Transformation**  
Null space.  
*Terms:* null space  
→ PDF p. 61 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Subspaces And Spans**  
Subspaces and span.  
*Terms:* subspace, span, independence  
→ PDF pp. 62–66 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**An Application To Matrices**  
An application.  
*Terms:* application  
→ PDF p. 67 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Matrices And Calculus**  
Matrix calculus and derivatives.  
*Terms:* matrix calculus, Jacobian  
→ PDF pp. 68–77 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch3"></a>
## Determinants

*PDF pp. 85–112*

Determinants.

**Basic Techniques And Properties**  
Computation and properties.  
*Terms:* determinant, cofactor  
→ PDF pp. 85–88 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Mathematical Theory Of Determinants**  
Permutation definition and proofs.  
*Terms:* permutations  
→ PDF pp. 91–103 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Cayley Hamilton Theorem**  
Cayley–Hamilton.  
*Terms:* Cayley-Hamilton  
→ PDF pp. 104–105 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Block Multiplication Of Matrices**  
Block matrices.  
*Terms:* block multiplication  
→ PDF pp. 106–108 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch4"></a>
## Row Operations

*PDF pp. 113–130*

Row reduction and rank.

**Elementary Matrices**  
Elementary matrices.  
*Terms:* elementary matrices  
→ PDF pp. 113–118 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Rank Of A Matrix**  
Rank.  
*Terms:* rank  
→ PDF pp. 119–120 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Row Reduced Echelon Form**  
Reduced row echelon form.  
*Terms:* RREF  
→ PDF pp. 121–123 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Rank And Existence Of Solutions To Linear Systems**  
Solvability.  
*Terms:* existence of solutions  
→ PDF p. 124 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Fredholm Alternative**  
Fredholm alternative.  
*Terms:* Fredholm alternative  
→ PDF p. 125 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch5"></a>
## Some Factorizations

*PDF pp. 131–144*

LU and QR factorizations.

**LU Factorization**  
LU factorization.  
*Terms:* LU factorization  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Finding An LU Factorization**  
Computing it.  
*Terms:* multiplier method  
→ PDF pp. 131–132 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Solving Linear Systems Using An LU Factorization**  
Solving with LU.  
*Terms:* forward and back substitution  
→ PDF p. 133 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The P LU Factorization**  
PLU.  
*Terms:* PLU, pivoting  
→ PDF pp. 134–135 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Justification For The Multiplier Method**  
Why the multiplier method works.  
*Terms:* justification  
→ PDF p. 136 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Existence For The P LU Factorization**  
Existence of PLU.  
*Terms:* existence  
→ PDF p. 137 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The QR Factorization**  
QR via Gram–Schmidt/Householder.  
*Terms:* QR factorization  
→ PDF pp. 138–140 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch6"></a>
## Spectral Theory

*PDF pp. 145–188*

Eigenvalues and spectral theory for matrices.

**Eigenvalues And Eigenvectors Of A Matrix**  
Eigenvalues and eigenvectors.  
*Terms:* eigenvalues, eigenvectors  
→ PDF pp. 145–152 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Some Applications Of Eigenvalues And Eigenvectors**  
Applications.  
*Terms:* applications  
→ PDF pp. 153–155 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Schur’s Theorem**  
Schur’s theorem.  
*Terms:* Schur theorem  
→ PDF pp. 162–168 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Trace And Determinant**  
Trace and determinant.  
*Terms:* trace  
→ PDF p. 169 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Quadratic Forms**  
Quadratic forms.  
*Terms:* quadratic forms  
→ PDF p. 170 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Second Derivative Test**  
Second-derivative test.  
*Terms:* Hessian, second derivative test  
→ PDF pp. 171–174 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Estimation Of Eigenvalues**  
Gershgorin estimates.  
*Terms:* Gershgorin  
→ PDF p. 175 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Advanced Theorems**  
Advanced results.  
*Terms:* advanced theorems  
→ PDF pp. 176–178 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch7"></a>
## Vector Spaces And Fields

*PDF pp. 189–214*

Abstract vector spaces over fields.

**Vector Space Axioms**  
Axioms.  
*Terms:* vector space axioms  
→ PDF p. 189 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Subspaces And Bases**  
Subspaces, bases, dimension.  
*Terms:* basis, dimension  
→ PDF pp. 190–194 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Lots Of Fields**  
Many fields: field extensions and algebraic numbers.  
*Terms:* fields, field extensions  
→ PDF pp. 195–208 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch8"></a>
## Linear Transformations

*PDF pp. 215–232*

Linear transformations between abstract spaces.

**Matrix Multiplication As A Linear Transformation**  
Matrices as maps.  
*Terms:* linear maps  
→ PDF p. 215 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**L (V, W ) As A Vector Space**  
L(V,W) as a space.  
*Terms:* L(V, W)  
→ PDF pp. 215–216 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Matrix Of A Linear Transformation**  
Matrix of a map, change of basis.  
*Terms:* matrix representation, change of basis, similarity  
→ PDF pp. 217–227 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Eigenvalues And Eigenvectors Of Linear Transformations**  
Eigen-theory for maps.  
*Terms:* eigenvalues  
→ PDF p. 228 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch9"></a>
## Canonical Forms

*PDF pp. 233–262*

Canonical forms.

**A Theorem Of Sylvester, Direct Sums**  
Sylvester and direct sums.  
*Terms:* direct sum, Sylvester  
→ PDF pp. 233–235 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Direct Sums, Block Diagonal Matrices**  
Block diagonal forms.  
*Terms:* block diagonal  
→ PDF pp. 236–238 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Cyclic Sets**  
Cyclic sets.  
*Terms:* cyclic subspaces  
→ PDF pp. 239–242 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Nilpotent Transformations**  
Nilpotent maps.  
*Terms:* nilpotent  
→ PDF pp. 243–245 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Jordan Canonical Form**  
Jordan form.  
*Terms:* Jordan canonical form  
→ PDF pp. 246–248 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Rational Canonical Form∗**  
Rational canonical form.  
*Terms:* rational canonical form  
→ PDF pp. 254–255 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Uniqueness**  
Uniqueness.  
*Terms:* uniqueness  
→ PDF pp. 256–260 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch10"></a>
## Markov Processes

*PDF pp. 263–272*

Markov chains with matrices.

**Regular Markov Matrices**  
Regular Markov matrices and steady states.  
*Terms:* Markov matrix, steady state  
→ PDF pp. 263–266 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Migration Matrices**  
Migration models.  
*Terms:* migration matrices  
→ PDF p. 267 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Absorbing States**  
Absorbing states.  
*Terms:* absorbing states  
→ PDF pp. 267–269 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch11"></a>
## Inner Product Spaces

*PDF pp. 273–292*

Inner product spaces.

**General Theory**  
General theory.  
*Terms:* inner product space  
→ PDF pp. 273–274 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Gram Schmidt Process**  
Gram–Schmidt.  
*Terms:* Gram-Schmidt  
→ PDF pp. 275–277 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Riesz Representation Theorem**  
Riesz representation.  
*Terms:* Riesz representation  
→ PDF pp. 278–280 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Tensor Product Of Two Vectors**  
Tensor products of vectors.  
*Terms:* outer product  
→ PDF pp. 281–282 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Least Squares**  
Least squares.  
*Terms:* least squares  
→ PDF p. 283 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Fredholm Alternative Again**  
Fredholm again.  
*Terms:* Fredholm alternative  
→ PDF p. 284 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Determinant And Volume**  
Determinants and volume.  
*Terms:* volume, determinant  
→ PDF pp. 289–290 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch12"></a>
## Self Adjoint Operators

*PDF pp. 293–322*

Self-adjoint operators and their decompositions.

**Simultaneous Diagonalization**  
Simultaneous diagonalization.  
*Terms:* simultaneous diagonalization  
→ PDF pp. 293–295 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Schur’s Theorem**  
Schur again.  
*Terms:* Schur  
→ PDF pp. 296–297 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Spectral Theory Of Self Adjoint Operators**  
Spectral theorem.  
*Terms:* spectral theorem  
→ PDF pp. 298–301 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Positive And Negative Linear Transformations**  
Positive maps.  
*Terms:* positive definite  
→ PDF pp. 302–303 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Square Root**  
Square roots.  
*Terms:* square root  
→ PDF p. 304 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Fractional Powers**  
Fractional powers.  
*Terms:* fractional powers  
→ PDF p. 305 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Square Roots And Polar Decompositions**  
Polar decomposition.  
*Terms:* polar decomposition  
→ PDF pp. 306–308 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**An Application To Statistics**  
Statistics application.  
*Terms:* covariance, statistics  
→ PDF pp. 309–310 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Singular Value Decomposition**  
SVD.  
*Terms:* singular value decomposition  
→ PDF pp. 311–322 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch13"></a>
## Norms

*PDF pp. 323–354*

Norms and iterative methods.

**The p Norms**  
p-norms and operator norms.  
*Terms:* p-norm, operator norm  
→ PDF pp. 329–330 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Condition Number**  
Condition number.  
*Terms:* condition number  
→ PDF pp. 331–332 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The Spectral Radius**  
Spectral radius.  
*Terms:* spectral radius  
→ PDF pp. 333–334 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Series And Sequences Of Linear Operators**  
Series of operators.  
*Terms:* Neumann series, matrix exponential  
→ PDF pp. 335–339 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Iterative Methods For Linear Systems**  
Jacobi and Gauss–Seidel.  
*Terms:* Jacobi, Gauss-Seidel  
→ PDF pp. 340–344 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**Theory Of Convergence**  
Convergence theory.  
*Terms:* convergence  
→ PDF pp. 345–347 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)


---

<a id="ch14"></a>
## Numerical Methods, Eigenvalues

*PDF pp. 355–384*

Numerical eigenvalue algorithms.

**The Power Method For Eigenvalues**  
The power method and shifted inverse power.  
*Terms:* power method, inverse iteration  
→ PDF pp. 355–368 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

**The QR Algorithm**  
The QR algorithm.  
*Terms:* QR algorithm, Hessenberg  
→ PDF pp. 369–382 in [the PDF](https://drive.google.com/file/d/1f8CW5Md2ZtYH7C8pQCpKsgyHP13EM1aZ/view)

