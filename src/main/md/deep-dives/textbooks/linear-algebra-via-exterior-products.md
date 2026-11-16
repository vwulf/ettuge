<a id="ch1"></a>
# Linear Algebra via Exterior Products

> Sergei Winitzki · 2010 edition (GNU FDL) · [the PDF in Drive](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

Appendices (complex numbers, permutations, matrices, license) are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A coordinate-free course in linear algebra for physicists and mathematicians that does nearly everything with the exterior (wedge) product instead of matrices. After vector spaces, duals and tensor products, it introduces exterior powers and uses them to define determinants, the trace and the characteristic polynomial as basis-independent objects, then derives Cramer’s rule, Vandermonde determinants, Cayley–Hamilton, functions of operators, the Jacobi and Liouville formulas and the Jordan form. A final chapter adds a scalar product: orthogonality, Hodge-style duality, antisymmetric operators and Pfaffians.

**Contents**

1. [0 Introduction and summary](ch1): Notation, a quiz of the kind of problems the book solves, and a list of its results.
2. [1 Linear algebra without coordinates](ch2): Vector spaces, maps, duals and tensors without choosing coordinates.
3. [2 Exterior product](ch3): The exterior product and the spaces ∧ᵏV.
4. [3 Basic applications](ch4): Determinants, trace and characteristic polynomial from exterior powers.
5. [4 Advanced applications](ch5): Further results: adjugates, Cayley–Hamilton, functions of operators and the Jordan form.
6. [5 Scalar product](ch6): Adding a scalar product: orthogonality, duality and antisymmetric operators.


---

## 0 Introduction and summary

*PDF pp. 11–20*

Notation, a quiz of the kind of problems the book solves, and a list of its results.

**0.1 Notation**  
Notation.  
*Terms:* notation  
→ PDF pp. 11–12 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**0.2 Sample quiz problems**  
Sample problems.  
*Terms:* quiz problems  
→ PDF pp. 13–14 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**0.3 A list of results**  
Summary of results.  
*Terms:* results  
→ PDF pp. 15–20 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)


---

<a id="ch2"></a>
## 1 Linear algebra without coordinates

*PDF pp. 21–82*

Vector spaces, maps, duals and tensors without choosing coordinates.

**1.1 Vector spaces**  
Abstract vector spaces.  
*Terms:* vector space  
→ PDF pp. 21–35 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.2 Linear maps in vector spaces**  
Linear maps.  
*Terms:* linear map  
→ PDF pp. 36–42 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.3 Subspaces**  
Subspaces.  
*Terms:* subspace  
→ PDF pp. 43–44 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.4 Isomorphisms of vector spaces**  
Isomorphisms.  
*Terms:* isomorphism  
→ PDF p. 45 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.5 Direct sum of vector spaces**  
Direct sums.  
*Terms:* direct sum  
→ PDF p. 46 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.6 Dual (conjugate) vector space**  
Dual spaces and covectors.  
*Terms:* dual space, covector  
→ PDF pp. 47–54 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.7 Tensor product of vector spaces**  
Tensor products.  
*Terms:* tensor product  
→ PDF pp. 55–62 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.8 Linear maps and tensors**  
Linear maps as tensors in V⊗V*.  
*Terms:* tensor, linear operator  
→ PDF pp. 63–74 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.9 Index notation for tensors**  
Index notation.  
*Terms:* index notation, Einstein summation  
→ PDF pp. 75–78 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**1.10 Dirac notation for vectors and covectors**  
Dirac bra-ket notation.  
*Terms:* Dirac notation, bra-ket  
→ PDF pp. 79–82 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)


---

<a id="ch3"></a>
## 2 Exterior product

*PDF pp. 83–116*

The exterior product and the spaces ∧ᵏV.

**2.1 Motivation**  
Why oriented areas and volumes motivate the wedge product.  
*Terms:* oriented area, volume  
→ PDF pp. 83–87 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**2.2 Exterior product**  
Definition and rules of the exterior product.  
*Terms:* exterior product, wedge product  
→ PDF pp. 88–94 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**2.3 Properties of spaces kV**  
Dimension and bases of ∧ᵏV, and linear dependence via wedges.  
*Terms:* exterior power, linear independence  
→ PDF pp. 95–116 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)


---

<a id="ch4"></a>
## 3 Basic applications

*PDF pp. 117–164*

Determinants, trace and characteristic polynomial from exterior powers.

**3.1 Determinants through permutations: the hard way**  
The classical permutation formula, for comparison.  
*Terms:* permutations, Leibniz formula  
→ PDF pp. 117–118 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.2 The space NV and oriented volume**  
The top power ∧ᴺV and oriented volume.  
*Terms:* top exterior power, oriented volume  
→ PDF pp. 119–123 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.3 Determinants of operators**  
The determinant of an operator as its action on ∧ᴺV.  
*Terms:* determinant  
→ PDF pp. 124–129 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.4 Determinants of square tables**  
Determinants of matrices.  
*Terms:* matrix determinant  
→ PDF pp. 130–135 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.5 Solving linear equations**  
Cramer’s rule and solving systems.  
*Terms:* Cramer’s rule  
→ PDF pp. 136–142 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.6 Vandermonde matrix**  
The Vandermonde determinant.  
*Terms:* Vandermonde matrix  
→ PDF pp. 143–146 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.7 Multilinear actions in exterior powers**  
How operators act on exterior powers.  
*Terms:* exterior power of operator  
→ PDF pp. 147–150 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.8 Trace**  
The trace as a derivation on ∧ᴺV.  
*Terms:* trace  
→ PDF pp. 151–154 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**3.9 Characteristic polynomial**  
The characteristic polynomial and its coefficients.  
*Terms:* characteristic polynomial  
→ PDF pp. 155–164 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)


---

<a id="ch5"></a>
## 4 Advanced applications

*PDF pp. 165–222*

Further results: adjugates, Cayley–Hamilton, functions of operators and the Jordan form.

**4.1 The space N-1V**  
The space ∧ᴺ⁻¹V.  
*Terms:* N-1 exterior power  
→ PDF pp. 165–169 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**4.2 Algebraic complement (adjoint) and beyond**  
The algebraic complement (adjugate) and generalizations.  
*Terms:* adjugate, algebraic complement  
→ PDF pp. 170–179 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**4.3 Cayley-Hamilton theorem and beyond**  
Cayley–Hamilton and its extensions.  
*Terms:* Cayley-Hamilton theorem  
→ PDF pp. 180–182 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**4.4 Functions of operators**  
Functions of operators via polynomials and power series.  
*Terms:* functions of operators, matrix exponential  
→ PDF pp. 183–195 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**4.5 Formulas of Jacobi and Liouville**  
Jacobi’s formula and Liouville’s formula for determinants of exponentials.  
*Terms:* Jacobi formula, Liouville formula  
→ PDF pp. 196–203 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**4.6 Jordan canonical form**  
The Jordan canonical form.  
*Terms:* Jordan canonical form  
→ PDF pp. 204–213 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**4.7 * Construction of projectors onto Jordan cells**  
Projectors onto Jordan cells (optional).  
*Terms:* projectors  
→ PDF pp. 214–222 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)


---

<a id="ch6"></a>
## 5 Scalar product

*PDF pp. 223–270*

Adding a scalar product: orthogonality, duality and antisymmetric operators.

**5.1 Vector spaces with scalar product**  
Scalar products and orthonormal bases.  
*Terms:* scalar product, orthonormal basis  
→ PDF pp. 223–231 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**5.2 Orthogonal subspaces**  
Orthogonal complements.  
*Terms:* orthogonal complement  
→ PDF pp. 232–236 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**5.3 Orthogonal transformations**  
Orthogonal transformations.  
*Terms:* orthogonal transformation  
→ PDF pp. 237–239 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**5.4 Applications of exterior product**  
Volumes, cross products and distances via wedges.  
*Terms:* cross product, Hodge star  
→ PDF pp. 240–249 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**5.5 Scalar product in kV**  
The induced scalar product on ∧ᵏV.  
*Terms:* scalar product on exterior powers  
→ PDF pp. 250–255 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**5.6 Scalar product for complex spaces**  
Hermitian products on complex spaces.  
*Terms:* Hermitian product  
→ PDF pp. 256–260 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**5.7 Antisymmetric operators**  
Antisymmetric operators.  
*Terms:* antisymmetric operator  
→ PDF pp. 261–263 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

**5.8 * Pfaffians**  
Pfaffians (optional).  
*Terms:* Pfaffian  
→ PDF pp. 264–270 in [the PDF](https://drive.google.com/file/d/10gYZxIrH4CT-B8qRWfh34aHL-JWDksFM/view)

