<a id="ch1"></a>
# High-Dimensional Probability

> Roman Vershynin · Cambridge University Press, 2018 (author’s version) · [the PDF in Drive](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

End-of-chapter notes are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An introduction to probability in high dimensions aimed at data science. Vershynin builds the toolkit of concentration inequalities (Hoeffding, Chernoff, Bernstein, sub-gaussian and sub-exponential variables), extends it to random vectors and random matrices via nets and covering numbers, and then to dependence (Lipschitz concentration, matrix Bernstein, Hanson–Wright, symmetrization). The second half covers random processes and chaining (Slepian, Sudakov, Dudley, generic chaining, VC dimension), matrix deviation inequalities and their geometry, sparse recovery and the lasso, and Dvoretzky–Milman. Every tool is paired with an application: community detection, covariance estimation, Grothendieck’s inequality and max-cut, Johnson–Lindenstrauss, matrix completion and learning theory.

**Contents**

1. [Appetizer: using probability to cover a geometric set](ch1): A warm-up showing how random sampling covers a convex set (Maurey’s empirical method).
2. [Preliminaries on random variables](ch2): Basic probability needed later.
3. [Concentration of sums of independent random variables](ch3): Concentration for sums of independent variables.
4. [Random vectors in high dimensions](ch4): Random vectors in high dimensions and two applications to optimization.
5. [Random matrices](ch5): Norms of random matrices via nets, with applications.
6. [Concentration without independence](ch6): Concentration for dependent quantities.
7. [Quadratic forms, symmetrization and contraction](ch7): Quadratic forms and techniques for removing dependence.
8. [Random processes](ch8): Gaussian processes and comparison inequalities.
9. [Chaining](ch9): Chaining arguments for suprema of processes.
10. [Deviations of random matrices and geometric consequences](ch10): A matrix deviation inequality and its geometric consequences.
11. [Sparse Recovery](ch11): Recovering structured signals from few measurements.
12. [Dvoretzky-Milman's Theorem](ch12): Random sections of convex bodies.


---

## Appetizer: using probability to cover a geometric set

*PDF pp. 9–13*

A warm-up showing how random sampling covers a convex set (Maurey’s empirical method).

*Terms:* Maurey empirical method, covering, convex hull

→ PDF pp. 9–13 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch2"></a>
## Preliminaries on random variables

*PDF pp. 14–20*

Basic probability needed later.

**Basic quantities associated with random variables**  
Expectation, variance, moments, L^p norms.  
*Terms:* expectation, variance, moments  
→ PDF p. 14 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Some classical inequalities**  
Jensen, Markov, Chebyshev and other classical inequalities.  
*Terms:* Markov inequality, Chebyshev, Jensen  
→ PDF pp. 15–16 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Limit theorems**  
Law of large numbers and central limit theorem.  
*Terms:* law of large numbers, central limit theorem  
→ PDF pp. 17–19 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch3"></a>
## Concentration of sums of independent random variables

*PDF pp. 21–49*

Concentration for sums of independent variables.

**Why concentration inequalities?**  
Why tail bounds beyond the CLT are needed.  
*Terms:* concentration inequalities  
→ PDF pp. 21–23 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Hoeffding's inequality**  
Hoeffding’s inequality for bounded variables.  
*Terms:* Hoeffding inequality  
→ PDF pp. 24–26 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Chernoff's inequality**  
Chernoff’s inequality for Bernoulli sums.  
*Terms:* Chernoff bound  
→ PDF pp. 27–28 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: degrees of random graphs**  
Degrees in Erdős–Rényi graphs.  
*Terms:* random graphs, degrees  
→ PDF pp. 29–31 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Sub-gaussian distributions**  
Sub-gaussian random variables and the ψ₂ norm.  
*Terms:* sub-gaussian, psi2 norm  
→ PDF pp. 32–36 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**General Hoeffding's and Khintchine's inequalities**  
General Hoeffding and Khintchine inequalities.  
*Terms:* Khintchine inequality  
→ PDF pp. 37–39 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Sub-exponential distributions**  
Sub-exponential variables and the ψ₁ norm.  
*Terms:* sub-exponential, psi1 norm  
→ PDF pp. 40–44 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Bernstein's inequality**  
Bernstein’s inequality.  
*Terms:* Bernstein inequality  
→ PDF pp. 45–47 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch4"></a>
## Random vectors in high dimensions

*PDF pp. 50–83*

Random vectors in high dimensions and two applications to optimization.

**Concentration of the norm**  
The norm of a random vector concentrates near √n.  
*Terms:* norm concentration  
→ PDF pp. 51–52 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Covariance matrices and principal component analysis**  
Covariance and PCA.  
*Terms:* covariance matrix, PCA  
→ PDF pp. 53–57 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Examples of high-dimensional distributions**  
Gaussian, spherical and frame examples.  
*Terms:* high-dimensional distributions  
→ PDF pp. 58–63 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Sub-gaussian distributions in higher dimensions**  
Sub-gaussian random vectors.  
*Terms:* sub-gaussian vectors  
→ PDF pp. 64–67 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: Grothendieck's inequality and semidefinite programming**  
Grothendieck’s inequality and SDP relaxations.  
*Terms:* Grothendieck inequality, semidefinite programming  
→ PDF pp. 68–73 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: Maximum cut for graphs**  
Goemans–Williamson max-cut.  
*Terms:* max-cut, Goemans-Williamson  
→ PDF pp. 74–77 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Kernel trick, and tightening of Grothendieck's inequality**  
The kernel trick and a sharper Grothendieck constant.  
*Terms:* kernel trick  
→ PDF pp. 78–81 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch5"></a>
## Random matrices

*PDF pp. 84–112*

Norms of random matrices via nets, with applications.

**Preliminaries on matrices**  
Singular values, operator norm and approximation.  
*Terms:* singular values, operator norm  
→ PDF pp. 84–88 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Nets, covering numbers and packing numbers**  
ε-nets, covering and packing numbers.  
*Terms:* epsilon-net, covering number, packing number  
→ PDF pp. 89–93 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: error correcting codes**  
Bounds for error-correcting codes.  
*Terms:* error-correcting codes  
→ PDF pp. 94–96 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Upper bounds on random sub-gaussian matrices**  
Upper bounds on sub-gaussian random matrices.  
*Terms:* random matrix norm  
→ PDF pp. 97–100 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: community detection in networks**  
Community detection in the stochastic block model.  
*Terms:* stochastic block model, community detection  
→ PDF pp. 101–104 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Two-sided bounds on sub-gaussian matrices**  
Two-sided bounds on singular values.  
*Terms:* singular value bounds  
→ PDF pp. 105–107 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: covariance estimation and clustering**  
Covariance estimation and clustering.  
*Terms:* covariance estimation, clustering  
→ PDF pp. 108–110 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch6"></a>
## Concentration without independence

*PDF pp. 113–142*

Concentration for dependent quantities.

**Concentration of Lipschitz functions on the sphere**  
Lipschitz functions on the sphere concentrate.  
*Terms:* Lipschitz concentration, sphere  
→ PDF pp. 113–119 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Concentration on other metric measure spaces**  
Concentration on other spaces (Gaussian, cube, groups).  
*Terms:* Gaussian concentration, isoperimetry  
→ PDF pp. 120–125 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: Johnson-Lindenstrauss Lemma**  
The Johnson–Lindenstrauss lemma.  
*Terms:* Johnson-Lindenstrauss lemma  
→ PDF pp. 126–128 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Matrix Bernstein's inequality**  
Matrix Bernstein for sums of random matrices.  
*Terms:* matrix Bernstein inequality  
→ PDF pp. 129–136 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: community detection in sparse networks**  
Community detection in sparse networks.  
*Terms:* sparse networks  
→ PDF p. 137 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: covariance estimation for general distributions**  
Covariance estimation for general distributions.  
*Terms:* covariance estimation  
→ PDF pp. 138–140 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch7"></a>
## Quadratic forms, symmetrization and contraction

*PDF pp. 143–163*

Quadratic forms and techniques for removing dependence.

**Decoupling**  
Decoupling quadratic forms.  
*Terms:* decoupling  
→ PDF pp. 143–146 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Hanson-Wright Inequality**  
Hanson–Wright inequality.  
*Terms:* Hanson-Wright inequality  
→ PDF pp. 147–150 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Concentration of anisotropic random vectors**  
Anisotropic random vectors.  
*Terms:* anisotropic vectors  
→ PDF pp. 151–152 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Symmetrization**  
Symmetrization with Rademacher signs.  
*Terms:* symmetrization, Rademacher  
→ PDF pp. 153–154 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Random matrices with non-i.i.d. entries**  
Random matrices with non-i.i.d. entries.  
*Terms:* non-iid random matrices  
→ PDF pp. 155–156 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: matrix completion**  
Matrix completion.  
*Terms:* matrix completion  
→ PDF pp. 157–158 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Contraction Principle**  
The contraction principle.  
*Terms:* contraction principle  
→ PDF pp. 159–161 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch8"></a>
## Random processes

*PDF pp. 164–194*

Gaussian processes and comparison inequalities.

**Basic concepts and examples**  
Random processes and examples.  
*Terms:* random process, Gaussian process  
→ PDF pp. 164–167 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Slepian's inequality**  
Slepian’s comparison inequality.  
*Terms:* Slepian inequality, Gordon  
→ PDF pp. 168–174 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Sharp bounds on Gaussian matrices**  
Sharp bounds on Gaussian matrices.  
*Terms:* Gaussian matrices  
→ PDF pp. 175–177 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Sudakov's minoration inequality**  
Sudakov’s minoration.  
*Terms:* Sudakov minoration  
→ PDF pp. 178–179 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Gaussian width**  
Gaussian width.  
*Terms:* Gaussian width  
→ PDF pp. 180–185 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Stable dimension, stable rank, and Gaussian complexity**  
Stable dimension and stable rank.  
*Terms:* stable rank, Gaussian complexity  
→ PDF pp. 186–188 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Random projections of sets**  
Random projections of sets.  
*Terms:* random projections  
→ PDF pp. 189–192 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch9"></a>
## Chaining

*PDF pp. 195–236*

Chaining arguments for suprema of processes.

**Dudley's inequality**  
Dudley’s entropy integral.  
*Terms:* Dudley inequality, entropy integral  
→ PDF pp. 195–202 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: empirical processes**  
Empirical processes.  
*Terms:* empirical processes  
→ PDF pp. 203–207 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**VC dimension**  
VC dimension.  
*Terms:* VC dimension  
→ PDF pp. 208–219 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Application: statistical learning theory**  
Statistical learning theory and generalization.  
*Terms:* statistical learning theory, generalization bound  
→ PDF pp. 220–226 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Generic chaining**  
Generic chaining.  
*Terms:* generic chaining  
→ PDF pp. 227–230 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Talagrand's majorizing measure and comparison theorems**  
Talagrand’s majorizing measures.  
*Terms:* majorizing measure, Talagrand  
→ PDF pp. 231–232 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Chevet's inequality**  
Chevet’s inequality.  
*Terms:* Chevet inequality  
→ PDF pp. 233–234 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch10"></a>
## Deviations of random matrices and geometric consequences

*PDF pp. 237–253*

A matrix deviation inequality and its geometric consequences.

**Matrix deviation inequality**  
The matrix deviation inequality.  
*Terms:* matrix deviation inequality  
→ PDF pp. 237–242 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Random matrices, random projections and covariance estimation**  
Random projections and covariance estimation.  
*Terms:* random projection  
→ PDF pp. 243–245 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Johnson-Lindenstrauss Lemma for infinite sets**  
Johnson–Lindenstrauss for infinite sets.  
*Terms:* Johnson-Lindenstrauss infinite sets  
→ PDF pp. 246–247 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Random sections: M* bound and Escape Theorem**  
The M* bound and escape through the mesh.  
*Terms:* M* bound, escape theorem  
→ PDF pp. 248–251 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch11"></a>
## Sparse Recovery

*PDF pp. 254–276*

Recovering structured signals from few measurements.

**High-dimensional signal recovery problems**  
The recovery problem.  
*Terms:* compressed sensing  
→ PDF pp. 254–255 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Signal recovery based on M* bound**  
Recovery from the M* bound.  
*Terms:* M* bound  
→ PDF pp. 256–257 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Recovery of sparse signals**  
Sparse signals.  
*Terms:* sparse recovery  
→ PDF pp. 258–261 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Low-rank matrix recovery**  
Low-rank matrices.  
*Terms:* low-rank matrix recovery  
→ PDF pp. 262–264 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Exact recovery and the restricted isometry property**  
Exact recovery and the restricted isometry property.  
*Terms:* restricted isometry property, RIP  
→ PDF pp. 265–270 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Lasso algorithm for sparse regression**  
The lasso.  
*Terms:* lasso  
→ PDF pp. 271–274 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)


---

<a id="ch12"></a>
## Dvoretzky-Milman's Theorem

*PDF pp. 277–287*

Random sections of convex bodies.

**Deviations of random matrices with respect to general norms**  
Deviation for general norms.  
*Terms:* general norms  
→ PDF pp. 277–279 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Johnson-Lindenstrauss embeddings and sharper Chevet inequality**  
Sharper Chevet and JL embeddings.  
*Terms:* Johnson-Lindenstrauss embeddings  
→ PDF pp. 280–281 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

**Dvoretzky-Milman's Theorem**  
Dvoretzky–Milman theorem: almost Euclidean sections.  
*Terms:* Dvoretzky-Milman theorem  
→ PDF pp. 282–286 in [the PDF](https://drive.google.com/file/d/1zMSjmausR3YMnY23ZPD6b0kEaqe8kAo8/view)

