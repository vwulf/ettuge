<a id="ch1"></a>
# Linear Algebra for Computer Vision, Robotics, and Machine Learning

> Jean Gallier and Jocelyn Quaintance · University of Pennsylvania, version of 6 December 2024 (free online) · [the PDF in Drive](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

PDF page = printed page. This book is very long, so summaries and terms are given per chapter; each section is still listed with its PDF page range (section titles were parsed from the contents and a few long titles may be missing). Problems sections and the bibliography are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A rigorous, computation-aware linear algebra text aimed at vision, robotics and ML. It covers vector spaces, bases and linear maps, matrices, Haar wavelets and Hadamard matrices, direct sums and affine maps, determinants, Gaussian elimination with LU and Cholesky, vector and matrix norms, iterative solvers, duality, Euclidean and Hermitian spaces with QR via Householder, eigenvalues, quaternions and SO(3), spectral theorems, eigenvalue algorithms (QR iteration, Krylov), graph Laplacians and spectral graph drawing, SVD and polar form with pseudo-inverses, PCA and least squares, and finally annihilating polynomials, primary decomposition and the Jordan form.

**Contents**

1. [Introduction](ch1): Why linear algebra matters for these fields.
2. [Vector Spaces, Bases, Linear Maps](ch2): Vector spaces, bases and linear maps.
3. [Matrices and Linear Maps](ch3): Matrices representing linear maps.
4. [Haar Bases, Haar Wavelets, Hadamard Matrices](ch4): Haar wavelets and Hadamard matrices.
5. [Direct Sums, Rank-Nullity Theorem, Affine Maps](ch5): Direct sums, rank–nullity and affine maps.
6. [Determinants](ch6): Determinants.
7. [Gaussian Elimination, LU, Cholesky, Echelon Form](ch7): Solving linear systems.
8. [Vector Norms and Matrix Norms](ch8): Norms.
9. [Iterative Methods for Solving Linear Systems](ch9): Iterative solvers.
10. [The Dual Space and Duality](ch10): Dual spaces.
11. [Euclidean Spaces](ch11): Euclidean spaces.
12. [QR-Decomposition for Arbitrary Matrices](ch12): QR decomposition.
13. [Hermitian Spaces](ch13): Hermitian spaces.
14. [Eigenvectors and Eigenvalues](ch14): Eigenvalues and eigenvectors.
15. [Unit Quaternions and Rotations in SO(3)](ch15): Rotations via quaternions.
16. [Spectral Theorems](ch16): Spectral theorems.
17. [Computing Eigenvalues and Eigenvectors](ch17): Numerical eigenvalue methods.
18. [Graphs and Graph Laplacians; Basic Facts](ch18): Graphs and Laplacians.
19. [Spectral Graph Drawing](ch19): Spectral graph drawing.
20. [Singular Value Decomposition and Polar Form](ch20): Singular value decomposition.
21. [Applications of SVD and Pseudo-Inverses](ch21): Applications of SVD.
22. [Annihilating Polynomials; Primary Decomposition](ch22): Polynomials of linear maps.


---

## Introduction

*PDF pp. 13–16*

Why linear algebra matters for these fields.

*Terms:* motivation, applications

→ PDF pp. 13–16 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch2"></a>
## Vector Spaces, Bases, Linear Maps

*PDF pp. 17–84*

Vector spaces, bases and linear maps.

*Terms:* vector spaces, linear combinations, linear independence, bases, linear maps, quotient spaces, linear forms

**Motivations: Linear Combinations, Linear Independence, Rank**  
→ PDF pp. 17–28 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Vector Spaces P**  
→ PDF pp. 29–36 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Indexed Families; the Sum Notation i∈I ai**  
→ PDF pp. 37–41 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Linear Independence, Subspaces**  
→ PDF pp. 42–48 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Bases of a Vector Space**  
→ PDF pp. 49–56 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Matrices**  
→ PDF pp. 57–62 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Linear Maps**  
→ PDF pp. 63–71 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Linear Forms and the Dual Space**  
→ PDF pp. 72–84 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch3"></a>
## Matrices and Linear Maps

*PDF pp. 85–112*

Matrices representing linear maps.

*Terms:* matrices, change of basis, similarity, composition

**Representation of Linear Maps by Matrices**  
→ PDF pp. 85–89 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Composition of Linear Maps and Matrix Multiplication**  
→ PDF pp. 90–95 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Change of Basis Matrix**  
→ PDF pp. 96–100 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Effect of a Change of Bases on Matrices**  
→ PDF pp. 101–112 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch4"></a>
## Haar Bases, Haar Wavelets, Hadamard Matrices

*PDF pp. 113–138*

Haar wavelets and Hadamard matrices.

*Terms:* Haar basis, wavelets, image compression, Hadamard matrices

**Introduction to Signal Compression Using Haar Wavelets**  
→ PDF pp. 113–114 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Haar Matrices, Scaling Properties of Haar Wavelets**  
→ PDF pp. 115–119 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Kronecker Product Construction of Haar Matrices**  
→ PDF pp. 120–121 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Multiresolution Signal Analysis with Haar Bases**  
→ PDF pp. 122–124 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Haar Transform for Digital Images**  
→ PDF pp. 125–130 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Hadamard Matrices**  
→ PDF pp. 131–138 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch5"></a>
## Direct Sums, Rank-Nullity Theorem, Affine Maps

*PDF pp. 139–182*

Direct sums, rank–nullity and affine maps.

*Terms:* direct sum, rank-nullity theorem, projections, affine maps

**Direct Products**  
→ PDF p. 139 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Sums and Direct Sums**  
→ PDF pp. 140–144 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Matrices of Linear Maps and Multiplication by Blocks**  
→ PDF pp. 145–157 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Rank-Nullity Theorem; Grassmann’s Relation**  
→ PDF pp. 158–165 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Affine Maps**  
→ PDF pp. 166–182 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch6"></a>
## Determinants

*PDF pp. 183–220*

Determinants.

*Terms:* determinants, permutations, Cramer rule, characteristic polynomial, Cayley-Hamilton

**Permutations, Signature of a Permutation**  
→ PDF pp. 183–187 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Alternating Multilinear Maps**  
→ PDF pp. 188–191 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Definition of a Determinant**  
→ PDF pp. 192–200 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Inverse Matrices and Determinants**  
→ PDF pp. 201–202 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Systems of Linear Equations and Determinants**  
→ PDF pp. 203–205 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Determinant of a Linear Map**  
→ PDF p. 206 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Cayley–Hamilton Theorem**  
→ PDF pp. 206–211 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Permanents**  
→ PDF pp. 212–214 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Further Readings**  
→ PDF pp. 215–220 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch7"></a>
## Gaussian Elimination, LU, Cholesky, Echelon Form

*PDF pp. 221–300*

Solving linear systems.

*Terms:* Gaussian elimination, LU factorization, Cholesky, reduced row echelon form, transvections

**Motivating Example: Curve Interpolation**  
→ PDF pp. 221–224 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Gaussian Elimination**  
→ PDF pp. 225–229 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Elementary Matrices and Row Operations**  
→ PDF pp. 230–232 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**LU -Factorization**  
→ PDF pp. 233–238 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**P A = LU Factorization**  
→ PDF pp. 239–246 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Proof of Theorem 7.5 ~**  
→ PDF pp. 247–251 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Dealing with Roundoff Errors; Pivoting Strategies**  
→ PDF pp. 252–253 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Gaussian Elimination of Tridiagonal Matrices**  
→ PDF pp. 254–255 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**SPD Matrices and the Cholesky Decomposition**  
→ PDF pp. 256–264 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Reduced Row Echelon Form**  
→ PDF pp. 265–270 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**RREF, Free Variables, Homogeneous Systems**  
→ PDF pp. 271–273 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Uniqueness of RREF**  
→ PDF pp. 274–275 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Solving Linear Systems Using RREF**  
→ PDF pp. 276–281 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Elementary Matrices and Columns Operations**  
→ PDF p. 282 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Transvections and Dilatations ~**  
→ PDF pp. 283–300 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch8"></a>
## Vector Norms and Matrix Norms

*PDF pp. 301–350*

Norms.

*Terms:* vector norms, matrix norms, condition number, spectral radius

**Normed Vector Spaces**  
→ PDF pp. 301–312 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Matrix Norms**  
→ PDF pp. 313–317 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Subordinate Norms**  
→ PDF pp. 318–324 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Inequalities Involving Subordinate Norms**  
→ PDF pp. 325–326 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Condition Numbers of Matrices**  
→ PDF pp. 327–335 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**An Application of Norms: Inconsistent Linear Systems**  
→ PDF p. 336 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Limits of Sequences and Series**  
→ PDF pp. 337–339 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Matrix Exponential**  
→ PDF pp. 340–350 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch9"></a>
## Iterative Methods for Solving Linear Systems

*PDF pp. 351–374*

Iterative solvers.

*Terms:* Jacobi, Gauss-Seidel, relaxation, convergence

**Convergence of Sequences of Vectors and Matrices**  
→ PDF pp. 351–353 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Convergence of Iterative Methods**  
→ PDF pp. 354–355 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Methods of Jacobi, Gauss–Seidel, and Relaxation**  
→ PDF pp. 356–363 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Convergence of the Methods**  
→ PDF pp. 364–366 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Convergence Methods for Tridiagonal Matrices**  
→ PDF pp. 367–374 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch10"></a>
## The Dual Space and Duality

*PDF pp. 375–408*

Dual spaces.

*Terms:* dual space, annihilators, transpose, hyperplanes

**The Dual Space E ∗ and Linear Forms**  
→ PDF pp. 375–381 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Pairing and Duality Between E and E ∗**  
→ PDF pp. 382–386 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Duality Theorem and Some Consequences**  
→ PDF pp. 387–391 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Bidual and Canonical Pairings**  
→ PDF pp. 392–393 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Hyperplanes and Linear Forms**  
→ PDF p. 394 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Transpose of a Linear Map and of a Matrix**  
→ PDF pp. 395–399 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Properties of the Double Transpose**  
→ PDF pp. 400–401 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Four Fundamental Subspaces**  
→ PDF pp. 402–408 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch11"></a>
## Euclidean Spaces

*PDF pp. 409–462*

Euclidean spaces.

*Terms:* inner product, orthonormal bases, Gram-Schmidt, orthogonal group, isometries

**Inner Products, Euclidean Spaces**  
→ PDF pp. 409–417 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Orthogonality and Duality in Euclidean Spaces**  
→ PDF pp. 418–424 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Adjoint of a Linear Map**  
→ PDF pp. 425–427 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Existence and Construction of Orthonormal Bases**  
→ PDF pp. 428–434 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Linear Isometries (Orthogonal Transformations)**  
→ PDF pp. 435–437 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Orthogonal Group, Orthogonal Matrices**  
→ PDF pp. 438–439 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Rodrigues Formula**  
→ PDF pp. 440–442 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**QR-Decomposition for Invertible Matrices**  
→ PDF pp. 443–447 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Some Applications of Euclidean Geometry**  
→ PDF pp. 448–462 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch12"></a>
## QR-Decomposition for Arbitrary Matrices

*PDF pp. 463–484*

QR decomposition.

*Terms:* QR, Householder reflections

**Orthogonal Reflections**  
→ PDF pp. 463–467 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**QR-Decomposition Using Householder Matrices**  
→ PDF pp. 468–484 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch13"></a>
## Hermitian Spaces

*PDF pp. 485–524*

Hermitian spaces.

*Terms:* Hermitian inner product, unitary group, orthogonal projections

**Hermitian Spaces, Pre-Hilbert Spaces**  
→ PDF pp. 485–493 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Orthogonality, Duality, Adjoint of a Linear Map**  
→ PDF pp. 494–498 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Linear Isometries (Also Called Unitary Transformations)**  
→ PDF pp. 499–500 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Unitary Group, Unitary Matrices**  
→ PDF pp. 501–503 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Hermitian Reflections and QR-Decomposition**  
→ PDF pp. 504–508 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Orthogonal Projections and Involutions**  
→ PDF pp. 509–511 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Dual Norms**  
→ PDF pp. 512–524 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch14"></a>
## Eigenvectors and Eigenvalues

*PDF pp. 525–556*

Eigenvalues and eigenvectors.

*Terms:* eigenvalues, eigenvectors, diagonalization, Schur form, Gershgorin

**Eigenvectors and Eigenvalues of a Linear Map**  
→ PDF pp. 525–532 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Reduction to Upper Triangular Form**  
→ PDF pp. 533–536 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Location of Eigenvalues**  
→ PDF pp. 537–540 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Conditioning of Eigenvalue Problems**  
→ PDF pp. 541–542 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Eigenvalues of the Matrix Exponential**  
→ PDF pp. 543–556 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch15"></a>
## Unit Quaternions and Rotations in SO(3)

*PDF pp. 557–580*

Rotations via quaternions.

*Terms:* unit quaternions, SO(3), SU(2), exponential map

**The Group SU(2) and the Skew Field H of Quaternions**  
→ PDF pp. 557–558 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Representation of Rotation in SO(3) By Quaternions in SU(2)**  
→ PDF pp. 559–563 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Matrix Representation of the Rotation rq**  
→ PDF pp. 564–565 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**An Algorithm to Find a Quaternion Representing a Rotation**  
→ PDF pp. 566–568 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Exponential Map exp : su(2) → SU(2)**  
→ PDF pp. 569–571 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Quaternion Interpolation ~**  
→ PDF pp. 572–573 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Nonexistence of a “Nice” Section from SO(3) to SU(2)**  
→ PDF pp. 574–580 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch16"></a>
## Spectral Theorems

*PDF pp. 581–616*

Spectral theorems.

*Terms:* normal matrices, symmetric matrices, spectral theorem, Rayleigh quotient, Courant-Fischer

**Introduction**  
→ PDF p. 581 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Normal Linear Maps: Eigenvalues and Eigenvectors**  
→ PDF pp. 581–586 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Spectral Theorem for Normal Linear Maps**  
→ PDF pp. 587–591 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Self-Adjoint and Other Special Linear Maps**  
→ PDF pp. 592–597 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Normal and Other Special Matrices**  
→ PDF pp. 598–600 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Rayleigh–Ritz Theorems and Eigenvalue Interlacing**  
→ PDF pp. 601–605 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Courant–Fischer Theorem; Perturbation Results**  
→ PDF pp. 606–616 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch17"></a>
## Computing Eigenvalues and Eigenvectors

*PDF pp. 617–646*

Numerical eigenvalue methods.

*Terms:* QR algorithm, Hessenberg, shifts, Krylov, Arnoldi, Lanczos, power iteration

**The Basic QR Algorithm**  
→ PDF pp. 619–624 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Hessenberg Matrices**  
→ PDF pp. 625–630 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Making the QR Method More Efficient Using Shifts**  
→ PDF pp. 631–635 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Krylov Subspaces; Arnoldi Iteration**  
→ PDF pp. 636–639 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**GMRES**  
→ PDF p. 640 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Hermitian Case; Lanczos Iteration**  
→ PDF p. 641 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Power Methods**  
→ PDF pp. 642–646 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch18"></a>
## Graphs and Graph Laplacians; Basic Facts

*PDF pp. 647–670*

Graphs and Laplacians.

*Terms:* graph Laplacian, incidence matrix, normalized Laplacian

**Directed Graphs, Undirected Graphs, Weighted Graphs**  
→ PDF pp. 650–656 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Laplacian Matrices of Graphs**  
→ PDF pp. 657–660 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Normalized Laplacian Matrices of Graphs**  
→ PDF pp. 661–664 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Graph Clustering Using Normalized Cuts**  
→ PDF pp. 665–670 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch19"></a>
## Spectral Graph Drawing

*PDF pp. 671–680*

Spectral graph drawing.

*Terms:* spectral drawing, graph embedding

**Graph Drawing and Energy Minimization**  
→ PDF pp. 671–673 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Examples of Graph Drawings**  
→ PDF pp. 674–680 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch20"></a>
## Singular Value Decomposition and Polar Form

*PDF pp. 681–702*

Singular value decomposition.

*Terms:* SVD, polar decomposition

**Properties of f ◦ f**  
→ PDF pp. 681–686 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Singular Value Decomposition for Square Matrices**  
→ PDF pp. 687–690 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Polar Form for Square Matrices**  
→ PDF pp. 691–692 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Singular Value Decomposition for Rectangular Matrices**  
→ PDF pp. 693–696 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Ky Fan Norms and Schatten Norms**  
→ PDF pp. 697–702 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch21"></a>
## Applications of SVD and Pseudo-Inverses

*PDF pp. 703–736*

Applications of SVD.

*Terms:* pseudo-inverse, least squares, PCA, best low-rank approximation, data compression

**Least Squares Problems and the Pseudo-Inverse**  
→ PDF pp. 703–709 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Properties of the Pseudo-Inverse**  
→ PDF pp. 710–714 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Data Compression and SVD**  
→ PDF pp. 715–716 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Principal Components Analysis (PCA)**  
→ PDF pp. 717–727 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Best Affine Approximation**  
→ PDF pp. 728–736 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)


---

<a id="ch22"></a>
## Annihilating Polynomials; Primary Decomposition

*PDF pp. 737–770*

Polynomials of linear maps.

*Terms:* minimal polynomial, annihilating polynomial, primary decomposition, Jordan form, nilpotent

**Basic Properties of Polynomials; Ideals, GCD’s**  
→ PDF pp. 739–743 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Annihilating Polynomials and the Minimal Polynomial**  
→ PDF p. 744 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Minimal Polynomials of Diagonalizable Linear Maps**  
→ PDF pp. 745–747 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Commuting Families of Linear Maps**  
→ PDF pp. 748–750 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**The Primary Decomposition Theorem**  
→ PDF pp. 751–757 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Jordan Decomposition**  
→ PDF pp. 758–759 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

**Nilpotent Linear Maps and Jordan Form**  
→ PDF pp. 760–770 in [the PDF](https://drive.google.com/file/d/1CBEcgoiWa0IriWJzGwVwt4SDqF_3951m/view)

