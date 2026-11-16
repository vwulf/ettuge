<a id="ch1"></a>
# Geometric Algebra Applications, Vol. I: Computer Vision, Graphics and Neurocomputing

> Eduardo Bayro-Corrochano · Springer, 2019 · [the PDF in Drive](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

Long and finely sectioned, so summaries and terms are given per chapter; each section is listed with its PDF page range. Exercise and conclusion sections and the front-matter guide are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A large reference on Clifford/geometric algebra as a unified language for geometric computing in robotics, vision and neural networks. Part I develops the mathematics: multivector products and operations, differentiation and multilinear functions, geometric calculus (including Maxwell and Dirac equations), Lie algebras and groups via rotors, 2D–4D algebras, kinematics with motors, conformal geometric algebra and higher algebras, plus implementation issues. Later parts cover quaternion and Clifford Fourier and wavelet transforms, geometric algebra for multi-view and stereo computer vision, geometric neural networks and Clifford SVMs, and applications: Lie filters, speech recognition, projective invariants and omnidirectional vision, tensor voting and Hough transforms in conformal algebra, medical data registration and surface reconstruction.

**Contents**

1. [1 Geometric Algebra for the Twenty-First Century Cybernetics](ch1): Why geometric algebra for perception–action systems.
2. [2 Introduction to Geometric Algebra](ch2): Foundations of geometric algebra.
3. [3 Differentiation, Linear, and Multilinear Functions in Geometric Algebra](ch3): Calculus and multilinear functions.
4. [4 Geometric Calculus](ch4): Geometric calculus.
5. [5 Lie Algebras, Lie Groups, and Algebra of Incidence](ch5): Lie theory in geometric algebra.
6. [6 2D, 3D, and 4D Geometric Algebras](ch6): Low-dimensional geometric algebras.
7. [7 Kinematics of the 2D and 3D Spaces](ch7): Kinematics with geometric algebra.
8. [8 Conformal Geometric Algebra](ch8): Conformal geometric algebra.
9. [9 The Geometric Algebras G6,0,2+, G6,3, G9,3+, G6,0,6+](ch9): Higher-dimensional algebras for lines and quadrics.
10. [10 Programming Issues](ch10): Implementing geometric algebra efficiently.
11. [11 Quaternion–Clifford Fourier and Wavelet Transforms](ch11): Hypercomplex signal transforms.
12. [12 Geometric Algebra of Computer Vision](ch12): Geometric algebra for computer vision.
13. [13 Geometric Neurocomputing](ch13): Geometric neural networks.
14. [14 Applications of Lie Filters, Quaternion Fourier, and Wavelet Transforms](ch14): Signal-processing applications.
15. [15 Invariants Theory in Computer Vision and Omnidirectional Vision](ch15): Invariants and omnidirectional vision.
16. [16 Geometric Algebra Tensor Voting, Hough Transform, Voting and Perception Using Conformal Geometric Algebra](ch16): Voting and perception in conformal GA.
17. [17 Modeling and Registration of Medical Data](ch17): Medical data modeling and registration.
18. [18 Applications in Neurocomputing](ch18): Experiments with geometric neural networks.
19. [19 Neurocomputing for 2D Contour and 3D Surface Reconstruction](ch19): Neural shape reconstruction.
20. [20 Clifford Algebras and Related Algebras](ch20): Clifford algebras and relatives.


---

## 1 Geometric Algebra for the Twenty-First Century Cybernetics

*PDF pp. 32–49*

Why geometric algebra for perception–action systems.

*Terms:* cybernetics, geometric algebra, unified language, geometric computing

**1.1 Cybernetics**  
→ PDF pp. 32–33 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**1.2 The Roots of Geometry and Algebra**  
→ PDF pp. 34–35 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**1.3 Geometric Algebra a Unified Mathematical Language**  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**1.4 What does Geometric Algebra Offer for Geometric Computing?**  
→ PDF pp. 37–42 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**1.5 Solving Problems in Perception and Action Systems**  
→ PDF pp. 43–49 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch2"></a>
## 2 Introduction to Geometric Algebra

*PDF pp. 50–82*

Foundations of geometric algebra.

*Terms:* history, multivectors, geometric product, inner and outer product, duality, reversion, simplexes

**2.1 History of Geometric Algebra**  
→ PDF pp. 50–51 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**2.2 What is Geometric Algebra?**  
→ PDF pp. 52–56 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**2.3 Multivector Products**  
→ PDF pp. 57–68 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**2.4 Multivector Operations**  
→ PDF pp. 69–74 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**2.5 Linear Algebra**  
→ PDF p. 75 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**2.6 Simplexes**  
→ PDF pp. 76–77 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch3"></a>
## 3 Differentiation, Linear, and Multilinear Functions in Geometric Algebra

*PDF pp. 83–116*

Calculus and multilinear functions.

*Terms:* multivector derivative, linear functions, determinant, adjoint, eigenblades, tensors

**3.1 Differentiation**  
→ PDF pp. 84–93 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**3.2 Linear Multivector Functions**  
→ PDF p. 94 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**3.3 The Determinant**  
→ PDF p. 95 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**3.4 Adjoints and Inverses**  
→ PDF pp. 96–97 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**3.5 Eigenvectors and Eigenblades**  
→ PDF pp. 98–100 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**3.6 Symmetric and Skew-Symmetric Transformations**  
→ PDF p. 101 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**3.7 Traction Operators: Contraction and Protraction**  
→ PDF pp. 102–103 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**3.8 Tensors in Geometric Algebra**  
→ PDF pp. 104–113 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch4"></a>
## 4 Geometric Calculus

*PDF pp. 117–140*

Geometric calculus.

*Terms:* vector manifolds, vector derivative, monogenic functions, Laplace-Beltrami, Maxwell equations, Dirac equation, spinors

**4.1 Vector Manifolds and Tangent Space**  
→ PDF pp. 117–120 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.2 Vector Derivative**  
→ PDF p. 121 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.3 Vector Fields, Grad, Div, Curl, and Monogenic Functions**  
→ PDF p. 122 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.4 Multivector Fields**  
→ PDF pp. 123–124 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.5 The Generalized Gaussian Map**  
→ PDF p. 125 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.6 Second Derivative and the Laplace–Beltrami Operator**  
→ PDF p. 126 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.7 Projection, Shape, Curl, and Spur**  
→ PDF pp. 127–130 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.8 Blade–Laplace Operator**  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.9 Geometric Calculus in 2D**  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.10 Electromagnetism: The Maxwell Equations**  
→ PDF pp. 132–134 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**4.11 Spinors, Shrödinger–Pauli, and Dirac Equations**  
→ PDF pp. 135–138 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch5"></a>
## 5 Lie Algebras, Lie Groups, and Algebra of Incidence

*PDF pp. 141–209*

Lie theory in geometric algebra.

*Terms:* Lie algebras, bivector algebra, rotors, unitary groups, spin groups, null cones, projective geometry

**5.1 Introduction**  
→ PDF p. 141 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.2 Lie Algebras and Bivector Algebras**  
→ PDF p. 142 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.3 Lie Groups and Lie Algebras of Rotors**  
→ PDF pp. 142–144 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.4 Complex Structures and Unitary Groups**  
→ PDF pp. 145–148 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.5 Geometric Algebra of Reciprocal Null Cones**  
→ PDF pp. 149–161 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.6 The General Linear Group as Spin Group**  
→ PDF pp. 162–166 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.7 The Pinsp(3,3)**  
→ PDF pp. 167–179 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.8 2D Projective Geometry in ℝ3,3**  
→ PDF p. 180 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.9 Horosphere and n-Dimensional Affine Plane**  
→ PDF pp. 181–182 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.10 The General Linear Algebra gl(calN) of the General Linear Lie Group GL(calN)**  
→ PDF pp. 183–194 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**5.11 The Algebra of Incidence**  
→ PDF pp. 195–200 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch6"></a>
## 6 2D, 3D, and 4D Geometric Algebras

*PDF pp. 210–234*

Low-dimensional geometric algebras.

*Terms:* complex and dual numbers, 2D and 3D GA, quaternions, motor algebra, projective 4D

**6.1 Complex, Double, and Dual Numbers**  
→ PDF p. 210 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**6.2 2D Geometric Algebras of the Plane**  
→ PDF pp. 211–212 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**6.3 3D Geometric Algebra for the Euclidean 3D Space**  
→ PDF pp. 213–218 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**6.4 Quaternion Algebra**  
→ PDF pp. 219–221 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**6.5 4D Geometric Algebra for 3D Kinematics**  
→ PDF pp. 222–228 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**6.6 4D Geometric Algebra for Projective 3D Space**  
→ PDF p. 229 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch7"></a>
## 7 Kinematics of the 2D and 3D Spaces

*PDF pp. 235–257*

Kinematics with geometric algebra.

*Terms:* points lines planes, motors, screw motion, rigid motion

**7.1 Introduction**  
→ PDF p. 235 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.2 Representation of Points, Lines, and Planes Using 3D Geometric Algebra**  
→ PDF pp. 235–236 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.3 Representation of Points, Lines, and Planes Using Motor Algebra**  
→ PDF p. 237 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.4 Representation of Points, Lines, and Planes Using 4D Geometric Algebra**  
→ PDF p. 238 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.5 Motion of Points, Lines, and Planes in 3D Geometric Algebra**  
→ PDF p. 239 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.6 Motion of Points, Lines, and Planes Using Motor Algebra**  
→ PDF pp. 240–241 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.7 Motion of Points, Lines, and Planes Using 4D Geometric Algebra**  
→ PDF p. 242 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.8 Spatial Velocity of Points, Lines, and Planes**  
→ PDF pp. 243–251 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**7.9 Incidence Relations Between Points, Lines, and Planes**  
→ PDF pp. 252–253 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch8"></a>
## 8 Conformal Geometric Algebra

*PDF pp. 258–292*

Conformal geometric algebra.

*Terms:* conformal GA, spheres, circles, conformal transformations, ruled surfaces

**8.1 Introduction**  
→ PDF pp. 258–273 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**8.2 The 3D Affine Plane**  
→ PDF pp. 274–276 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**8.3 The Lie Algebra**  
→ PDF p. 277 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**8.4 Conformal Transformations**  
→ PDF pp. 278–285 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**8.5 Ruled Surfaces**  
→ PDF pp. 286–288 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch9"></a>
## 9 The Geometric Algebras G6,0,2+, G6,3, G9,3+, G6,0,6+

*PDF pp. 293–316*

Higher-dimensional algebras for lines and quadrics.

*Terms:* double motor algebra, G6, 3, G9, 3, quadrics

**9.1 Introduction**  
→ PDF p. 293 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**9.2 The Double Motor Algebra G6,0,2+**  
→ PDF pp. 294–301 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**9.3 The Geometric Algebra G6,3**  
→ PDF pp. 302–309 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**9.4 The Geometric Subalgebras G9,3+ and G6,0,6+**  
→ PDF pp. 310–313 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch10"></a>
## 10 Programming Issues

*PDF pp. 317–326*

Implementing geometric algebra efficiently.

*Terms:* implementation, performance, software

**10.1 Main Issues for an Efficient Implementation**  
→ PDF pp. 317–318 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**10.2 Implementation Practicalities**  
→ PDF pp. 319–326 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch11"></a>
## 11 Quaternion–Clifford Fourier and Wavelet Transforms

*PDF pp. 327–380*

Hypercomplex signal transforms.

*Terms:* quaternion Fourier transform, Clifford Fourier transform, Gabor filters, monogenic signal, Riesz transform, Clifford wavelets

**11.1 Introduction**  
→ PDF pp. 327–340 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**11.2 Gabor Filters and Atomic Functions**  
→ PDF pp. 341–349 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**11.3 Quaternionic Analytic Signal, Monogenic Signal, Hilbert Transform, and Riesz Transform**  
→ PDF pp. 350–356 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**11.4 Radon Transform of Functionals**  
→ PDF pp. 357–358 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**11.5 Clifford Fourier Transforms**  
→ PDF pp. 359–361 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**11.6 From Real to Clifford Wavelet Transforms for Multiresolution Analysis**  
→ PDF pp. 362–378 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch12"></a>
## 12 Geometric Algebra of Computer Vision

*PDF pp. 381–436*

Geometric algebra for computer vision.

*Terms:* incidence algebra, projective space, projective invariants, multi-view geometry, camera calibration, stereo

**12.1 Introduction**  
→ PDF p. 381 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.2 The Geometric Algebras of 3D and 4D Spaces**  
→ PDF pp. 382–388 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.3 The Algebra of Incidence**  
→ PDF pp. 389–391 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.4 Algebra in Projective Space**  
→ PDF pp. 392–394 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.5 Projective Invariants**  
→ PDF pp. 395–399 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.6 Visual Geometry of n-Uncalibrated Cameras**  
→ PDF pp. 400–408 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.7 Calibrated Camera Model and Stereo Vision Using the Conformal Geometric Algebra Framework**  
→ PDF pp. 409–413 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.8 Omnidirectional Vision**  
→ PDF pp. 414–417 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.9 Invariants in the Conformal Space**  
→ PDF pp. 418–422 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.10 Conformal Geometric Algebra Voting Scheme**  
→ PDF pp. 423–425 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**12.11 Conformal Model for Stereoscopic Perception Systems**  
→ PDF pp. 426–431 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch13"></a>
## 13 Geometric Neurocomputing

*PDF pp. 437–507*

Geometric neural networks.

*Terms:* quaternion MLP, Clifford neural networks, geometric RBF networks, Clifford SVM

**13.1 Introduction**  
→ PDF pp. 437–438 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.2 Real-Valued Neural Networks**  
→ PDF p. 439 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.3 Complex MLP and Quaternionic MLP**  
→ PDF p. 440 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.4 Geometric Algebra Neural Networks**  
→ PDF pp. 440–447 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.5 Geometric Radial Basis Function Networks**  
→ PDF pp. 448–450 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.6 Spherical Radial Basis Function Network**  
→ PDF pp. 451–452 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.7 Quaternion Wavelet Function Network**  
→ PDF pp. 453–455 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.8 Support Vector Machines in Geometric Algebra**  
→ PDF p. 456 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.9 Linear Clifford Support Vector Machines for Classification**  
→ PDF pp. 457–460 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.10 Nonlinear Clifford Support Vector Machines for Classification**  
→ PDF p. 461 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.11 Clifford SVM for Regression**  
→ PDF pp. 462–464 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.12 Real- and Quaternion-Valued Spike Neural Networks**  
→ PDF pp. 465–474 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.13 Rotor or Quaternion Quantum Neural Networks**  
→ PDF pp. 475–498 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**13.14 Deep Learning Using Geometric Algebra**  
→ PDF pp. 499–504 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch14"></a>
## 14 Applications of Lie Filters, Quaternion Fourier, and Wavelet Transforms

*PDF pp. 508–536*

Signal-processing applications.

*Terms:* Lie filters, speech as 2D signals, phoneme recognition, quaternion wavelets, Riesz transform

**14.1 Lie Filters in the Affine Plane**  
→ PDF pp. 508–511 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**14.2 Representation of Speech as 2D Signals**  
→ PDF p. 512 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**14.3 Preprocessing of Speech 2D Representations**  
→ PDF pp. 513–516 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**14.4 Recognition of French Phonemes Using Neurocomputing**  
→ PDF pp. 517–518 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**14.5 Application of QWT**  
→ PDF pp. 519–526 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**14.6 Riesz Transform and Multiresolution Processing**  
→ PDF pp. 527–535 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch15"></a>
## 15 Invariants Theory in Computer Vision and Omnidirectional Vision

*PDF pp. 537–575*

Invariants and omnidirectional vision.

*Terms:* conics, Pascal theorem, intrinsic calibration, projective depth, visually guided grasping, omnidirectional vision

**15.1 Introduction**  
→ PDF p. 537 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.2 Conics and Pascal's Theorem**  
→ PDF pp. 538–540 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.3 Computing Intrinsic Camera Parameters**  
→ PDF pp. 541–542 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.4 Projective Invariants**  
→ PDF pp. 543–551 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.5 3D Projective Invariants from Multiple Views**  
→ PDF pp. 552–557 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.6 Visually Guided Grasping**  
→ PDF pp. 558–560 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.7 Camera Self-localization**  
→ PDF p. 561 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.8 Projective Depth**  
→ PDF pp. 562–563 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.9 Shape and Motion**  
→ PDF pp. 564–568 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.10 Omnidirectional Vision Landmark Identification Using Projective Invariants**  
→ PDF pp. 569–574 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**15.11 Conclusions**  
→ PDF p. 575 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch16"></a>
## 16 Geometric Algebra Tensor Voting, Hough Transform, Voting and Perception Using Conformal Geometric Algebra

*PDF pp. 576–628*

Voting and perception in conformal GA.

*Terms:* tensor voting, Hough transform, egomotion, 3D reconstruction, pose estimation

**16.1 Problem Formulation**  
→ PDF pp. 576–579 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**16.2 Tensor Voting**  
→ PDF pp. 580–587 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**16.3 Experimental Analysis of Tensor Votings Using Geometric Algebra**  
→ PDF pp. 588–593 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**16.4 Hough Transform in Conformal Geometric Algebra**  
→ PDF pp. 594–600 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**16.5 Conformal Geometric Algebra Voting Scheme**  
→ PDF pp. 601–612 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**16.6 Egomotion, 3D Reconstruction, and Relocalization**  
→ PDF pp. 613–620 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**16.7 3D Pose Estimation Using Conformal Geometric Algebra**  
→ PDF pp. 621–626 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**16.8 Conclusions**  
→ PDF pp. 627–628 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch17"></a>
## 17 Modeling and Registration of Medical Data

*PDF pp. 629–645*

Medical data modeling and registration.

*Terms:* segmentation, marching spheres, registration

**17.1 Background**  
→ PDF pp. 629–630 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**17.2 Segmentation**  
→ PDF pp. 631–635 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**17.3 Marching Spheres**  
→ PDF pp. 636–638 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**17.4 Registration of Two Models**  
→ PDF pp. 639–643 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**17.5 Conclusions**  
→ PDF pp. 644–645 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch18"></a>
## 18 Applications in Neurocomputing

*PDF pp. 646–672*

Experiments with geometric neural networks.

*Terms:* feedforward geometric networks, low-level structure recognition, Clifford SVM experiments

**18.1 Experiments Using Geometric Feedforward Neural Networks**  
→ PDF pp. 646–649 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**18.2 Recognition of 2D and 3D Low-Level Structures**  
→ PDF pp. 650–658 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**18.3 Experiments Using Clifford Support Vector Machines**  
→ PDF pp. 659–671 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch19"></a>
## 19 Neurocomputing for 2D Contour and 3D Surface Reconstruction

*PDF pp. 673–689*

Neural shape reconstruction.

*Terms:* contour reconstruction, surface reconstruction, neural gas

**19.1 Determining the Shape of an Object**  
→ PDF pp. 673–677 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**19.2 Experiments**  
→ PDF pp. 678–688 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)


---

<a id="ch20"></a>
## 20 Clifford Algebras and Related Algebras

*PDF pp. 690–730*

Clifford algebras and relatives.

*Terms:* Clifford algebras, classification, related algebras

**20.1 Clifford Algebras**  
→ PDF pp. 690–699 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

**20.2 Related Algebras**  
→ PDF pp. 700–730 in [the PDF](https://drive.google.com/file/d/1LkkEBd4A_GofGPSbejoN_74d9JNduT9l/view)

