<a id="ch1"></a>
# Linear Algebra Done Wrong

> Sergei Treil · Brown University, 2017 edition (free online) · [the PDF in Drive](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

Review exercises are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A rigorous first course in linear algebra for mathematics majors, “done wrong” in the sense that it brings in determinants early instead of avoiding them as Axler does. It moves from vector spaces and linear maps through systems of equations, rank and change of basis, to determinants, eigenvalues and diagonalization; then inner product spaces, orthogonal projection, least squares and adjoints; the spectral theorem, polar and singular value decompositions; quadratic forms and Sylvester’s law of inertia; dual spaces and tensors; and finally Cayley–Hamilton, generalized eigenspaces and the Jordan form.

**Contents**

1. [Chapter 1. Basic Notions](ch1): Vector spaces, linear maps and matrices, from first definitions to isomorphisms and subspaces.
2. [Chapter 2. Systems of linear equations](ch2): Solving linear systems by row reduction, and what the pivots reveal: dimension, rank and the fundamental subspaces.
3. [Chapter 3. Determinants](ch3): Determinants built from the properties they must have, then computed by cofactor expansion.
4. [Chapter 4. Introduction to spectral theory (eigenvalues and eigenvectors)](ch4): Eigenvalues and eigenvectors, and when a matrix can be diagonalized.
5. [Chapter 5. Inner product spaces](ch5): Inner products, orthogonality and projection, adjoints, and unitary and orthogonal maps.
6. [Chapter 6. Structure of operators in inner product spaces.](ch6): How operators look in inner product spaces: Schur form, the spectral theorem, polar decomposition and the SVD.
7. [Chapter 7. Bilinear and quadratic forms](ch7): Quadratic forms: diagonalizing them, Sylvester’s law of inertia, and positive definiteness.
8. [Chapter 8. Dual spaces and tensors](ch8): Dual spaces, the transpose as a dual map, and tensors with their transformation rules.
9. [Chapter 9. Advanced spectral theory](ch9): Cayley–Hamilton, the spectral mapping theorem, generalized eigenspaces and the Jordan decomposition.


---

## Chapter 1. Basic Notions

*PDF pp. 11–48*

Vector spaces, linear maps and matrices, from first definitions to isomorphisms and subspaces.

**1. Vector spaces**  
Axioms and examples of vector spaces.  
*Terms:* vector space, axioms  
→ PDF pp. 11–15 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Linear combinations, bases.**  
Linear combinations, spanning sets, linear independence and bases.  
*Terms:* linear combination, span, linear independence, basis  
→ PDF pp. 16–21 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Linear Transformations. Matrix–vector multiplication**  
Linear maps and how a matrix acts on a vector.  
*Terms:* linear transformation, matrix-vector product  
→ PDF pp. 22–26 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. Linear transformations as a vector space**  
The space of linear maps.  
*Terms:* space of linear maps  
→ PDF pp. 27–28 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Composition of linear transformations and matrix multiplication.**  
Composition of maps as matrix multiplication.  
*Terms:* composition, matrix multiplication  
→ PDF pp. 29–33 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**6. Invertible transformations and matrices. Isomorphisms**  
Invertible maps and matrices, and isomorphic spaces.  
*Terms:* invertible matrix, isomorphism  
→ PDF pp. 34–39 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**7. Subspaces.**  
Subspaces.  
*Terms:* subspace  
→ PDF p. 40 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**8. Application to computer graphics.**  
Rotations, scaling and projective coordinates in computer graphics.  
*Terms:* computer graphics, homogeneous coordinates  
→ PDF pp. 41–48 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch2"></a>
## Chapter 2. Systems of linear equations

*PDF pp. 49–84*

Solving linear systems by row reduction, and what the pivots reveal: dimension, rank and the fundamental subspaces.

**1. Different faces of linear systems.**  
A system as a matrix equation, a vector equation, and a linear map.  
*Terms:* linear system  
→ PDF p. 49 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Solution of a linear system. Echelon and reduced echelon forms**  
Gaussian elimination to echelon and reduced echelon form.  
*Terms:* Gaussian elimination, row echelon form, reduced row echelon form  
→ PDF pp. 50–55 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Analyzing the pivots.**  
What pivots say about existence and uniqueness of solutions.  
*Terms:* pivots  
→ PDF pp. 56–61 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. Finding the inverse of A by row reduction.**  
Computing an inverse by row reduction.  
*Terms:* inverse matrix  
→ PDF pp. 62–63 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Dimension. Finite-dimensional spaces.**  
Dimension of finite-dimensional spaces.  
*Terms:* dimension  
→ PDF pp. 64–65 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**6. General solution of a linear system.**  
General solution as particular plus homogeneous solution.  
*Terms:* general solution, homogeneous system  
→ PDF pp. 66–68 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**7. Fundamental subspaces of a matrix. Rank.**  
Column space, null space, row space and rank, and the rank theorem.  
*Terms:* rank, null space, column space, row space, rank-nullity  
→ PDF pp. 69–78 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**8. Representation of a linear transformation in arbitrary bases. Change of coordinates formula.**  
Matrices of a map in different bases and the change-of-coordinates formula.  
*Terms:* change of basis, similar matrices  
→ PDF pp. 79–84 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch3"></a>
## Chapter 3. Determinants

*PDF pp. 85–108*

Determinants built from the properties they must have, then computed by cofactor expansion.

**1. Introduction.**  
Motivation: volume and invertibility.  
*Terms:* determinant, volume  
→ PDF p. 85 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. What properties determinant should have.**  
The properties a determinant must satisfy (linearity, antisymmetry, normalization).  
*Terms:* multilinearity, alternating  
→ PDF pp. 86–87 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Constructing the determinant.**  
Building it by row operations.  
*Terms:* row operations  
→ PDF pp. 88–95 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. Formal definition. Existence and uniqueness of the determinant.**  
Existence and uniqueness via permutations.  
*Terms:* permutations, existence and uniqueness  
→ PDF pp. 96–99 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Cofactor expansion.**  
Cofactor expansion and the classical adjugate.  
*Terms:* cofactor expansion, adjugate, Cramer’s rule  
→ PDF pp. 100–105 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**6. Minors and rank.**  
Minors and their relation to rank.  
*Terms:* minors, rank  
→ PDF p. 106 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch4"></a>
## Chapter 4. Introduction to spectral theory (eigenvalues and eigenvectors)

*PDF pp. 109–126*

Eigenvalues and eigenvectors, and when a matrix can be diagonalized.

**1. Main definitions**  
Eigenvalues, eigenvectors, characteristic polynomial, spectrum.  
*Terms:* eigenvalue, eigenvector, characteristic polynomial  
→ PDF pp. 110–114 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Diagonalization.**  
Diagonalization and its criteria, with applications to powers of matrices.  
*Terms:* diagonalization, algebraic multiplicity, geometric multiplicity  
→ PDF pp. 115–126 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch5"></a>
## Chapter 5. Inner product spaces

*PDF pp. 127–172*

Inner products, orthogonality and projection, adjoints, and unitary and orthogonal maps.

**1. Inner product in R**n and C**n. Inner product spaces.**  
Inner products on real and complex spaces, norms and Cauchy–Schwarz.  
*Terms:* inner product, norm, Cauchy-Schwarz  
→ PDF pp. 127–134 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Orthogonality. Orthogonal and orthonormal bases.**  
Orthogonal and orthonormal bases.  
*Terms:* orthogonality, orthonormal basis  
→ PDF pp. 135–138 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Orthogonal projection and Gram-Schmidt orthogonalization**  
Orthogonal projection and Gram–Schmidt.  
*Terms:* orthogonal projection, Gram-Schmidt  
→ PDF pp. 139–145 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. Least square solution. Formula for the orthogonal projection**  
Least-squares solutions and the projection formula.  
*Terms:* least squares, normal equations  
→ PDF pp. 146–151 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Adjoint of a linear transformation. Fundamental subspaces revisited.**  
The adjoint and the fundamental subspaces revisited.  
*Terms:* adjoint, fundamental subspaces  
→ PDF pp. 152–155 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**6. Isometries and unitary operators. Unitary and orthogonal matrices.**  
Isometries, unitary and orthogonal matrices.  
*Terms:* isometry, unitary matrix, orthogonal matrix  
→ PDF pp. 156–160 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**7. Rigid motions in R**n**  
Rigid motions of Euclidean space.  
*Terms:* rigid motion  
→ PDF pp. 161–163 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**8. Complexification and decomplexification**  
Moving between real and complex spaces.  
*Terms:* complexification  
→ PDF pp. 164–172 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch6"></a>
## Chapter 6. Structure of operators in inner product spaces.

*PDF pp. 173–206*

How operators look in inner product spaces: Schur form, the spectral theorem, polar decomposition and the SVD.

**1. Upper triangular (Schur) representation of an operator.**  
Every operator is upper triangular in some orthonormal basis (Schur).  
*Terms:* Schur decomposition  
→ PDF pp. 173–174 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Spectral theorem for self-adjoint and normal operators.**  
Self-adjoint and normal operators are unitarily diagonalizable.  
*Terms:* spectral theorem, self-adjoint, normal operator  
→ PDF pp. 175–180 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Polar and singular value decompositions.**  
Polar decomposition and the singular value decomposition.  
*Terms:* polar decomposition, SVD, singular values  
→ PDF pp. 181–188 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. Applications of the singular value decomposition.**  
Uses of the SVD: operator norm, condition number, low-rank approximation.  
*Terms:* operator norm, condition number, low-rank approximation  
→ PDF pp. 189–196 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Structure of orthogonal matrices**  
Orthogonal matrices as products of rotations and reflections.  
*Terms:* orthogonal matrix, rotation, reflection  
→ PDF pp. 197–202 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**6. Orientation**  
Orientation of bases.  
*Terms:* orientation  
→ PDF pp. 203–206 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch7"></a>
## Chapter 7. Bilinear and quadratic forms

*PDF pp. 207–226*

Quadratic forms: diagonalizing them, Sylvester’s law of inertia, and positive definiteness.

**1. Main definition**  
Bilinear and quadratic forms.  
*Terms:* bilinear form, quadratic form  
→ PDF pp. 207–209 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Diagonalization of quadratic forms**  
Diagonalizing forms by orthogonal change of coordinates or by completing squares.  
*Terms:* diagonalization of quadratic forms  
→ PDF pp. 210–215 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Silvester's Law of Inertia**  
Sylvester’s law of inertia: the signature is invariant.  
*Terms:* Sylvester law of inertia, signature  
→ PDF pp. 216–217 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. Positive definite forms. Minimax characterization of eigenvalues and the Silvester's criterion of positivity**  
Positive definite forms, the minimax characterization of eigenvalues, and Sylvester’s criterion.  
*Terms:* positive definite, minimax, Courant-Fischer, Sylvester criterion  
→ PDF pp. 218–223 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Positive definite forms and inner products**  
Positive definite forms as inner products.  
*Terms:* inner product  
→ PDF pp. 224–226 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch8"></a>
## Chapter 8. Dual spaces and tensors

*PDF pp. 227–262*

Dual spaces, the transpose as a dual map, and tensors with their transformation rules.

**1. Dual spaces**  
Linear functionals and dual bases.  
*Terms:* dual space, linear functional, dual basis  
→ PDF pp. 227–233 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Dual of an inner product space**  
Riesz representation in inner product spaces.  
*Terms:* Riesz representation  
→ PDF pp. 234–236 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Adjoint (dual) transformations and transpose. Fundamental subspace revisited (once more)**  
Dual maps and the transpose; fundamental subspaces once more.  
*Terms:* dual map, transpose  
→ PDF pp. 237–241 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. What is the difference between a space and its dual?**  
Why a space and its dual differ: covariant and contravariant behavior.  
*Terms:* covariant, contravariant  
→ PDF pp. 242–248 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Multilinear functions. Tensors**  
Multilinear functions and tensors.  
*Terms:* multilinear map, tensor  
→ PDF pp. 249–256 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**6. Change of coordinates formula for tensors.**  
How tensor coordinates change with the basis.  
*Terms:* tensor transformation law  
→ PDF pp. 257–262 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)


---

<a id="ch9"></a>
## Chapter 9. Advanced spectral theory

*PDF pp. 263–286*

Cayley–Hamilton, the spectral mapping theorem, generalized eigenspaces and the Jordan decomposition.

**1. Cayley–Hamilton Theorem**  
Every matrix satisfies its characteristic polynomial.  
*Terms:* Cayley-Hamilton theorem  
→ PDF pp. 263–266 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**2. Spectral Mapping Theorem**  
Eigenvalues of p(A) are p of eigenvalues of A.  
*Terms:* spectral mapping theorem  
→ PDF pp. 267–268 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**3. Generalized eigenspaces. Geometric meaning of algebraic multiplicity**  
Generalized eigenspaces and the meaning of algebraic multiplicity.  
*Terms:* generalized eigenspace, algebraic multiplicity  
→ PDF pp. 269–275 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**4. Structure of nilpotent operators**  
Nilpotent operators and their cyclic structure.  
*Terms:* nilpotent operator  
→ PDF pp. 276–281 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

**5. Jordan decomposition theorem**  
The Jordan canonical form.  
*Terms:* Jordan canonical form  
→ PDF pp. 282–286 in [the PDF](https://drive.google.com/file/d/1BSOH6pFVYgeTvms1OUkhgo8L8BuEiiqK/view)

