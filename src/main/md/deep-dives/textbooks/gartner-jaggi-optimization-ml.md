<a id="ch1"></a>
# Optimization for Machine Learning (lecture notes)

> Bernd Gärtner (ETH) and Martin Jaggi (EPFL) · CS-439, Spring 2023 · [the PDF in Drive](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

Course notes; PDF page = printed page + 1. Exercises at the end of each chapter are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A proof-oriented course on the first-order and second-order methods behind machine-learning training. After a self-contained chapter on convex sets and functions, each chapter takes one algorithm and proves how many steps it needs under which assumptions: gradient descent for Lipschitz, smooth and strongly convex objectives (with Nesterov acceleration), projected and proximal variants for constraints and nonsmooth regularizers, subgradient and stochastic gradient descent, what can still be said for nonconvex functions, Newton and quasi-Newton (BFGS) methods, coordinate descent, and the projection-free Frank–Wolfe algorithm. The recurring pattern is a short “vanilla analysis” sharpened by each extra assumption into a better rate.

**Contents**

1. [1. Theory of Convex Functions](ch1): Calculus and linear-algebra background, convex sets and functions, their characterizations, and when minimizers exist.
2. [2. Gradient Descent](ch2): The basic method and its convergence rates under increasingly strong assumptions, plus acceleration.
3. [3. Projected and Proximal Gradient Descent](ch3): Handling constraints by projection and nonsmooth terms by proximal steps.
4. [4. Subgradient Descent](ch4): Gradient descent for nondifferentiable convex functions, and lower bounds for first-order methods.
5. [5. Stochastic Gradient Descent](ch5): Noisy gradient estimates from samples: rates and mini-batching.
6. [6. Nonconvex functions](ch6): What gradient descent guarantees without convexity, and trajectory analyses.
7. [7. Newton’s Method](ch7): Second-order steps and local quadratic convergence.
8. [8. Quasi-Newton Methods](ch8): Approximating the Hessian from gradient differences: secant methods and BFGS.
9. [9. Coordinate Descent](ch9): Updating one coordinate at a time, with coordinate-wise smoothness.
10. [10. The Frank-Wolfe Algorithm](ch10): Projection-free optimization over constraint sets via linear minimization.


---

## 1. Theory of Convex Functions

*PDF pp. 3–39*

Calculus and linear-algebra background, convex sets and functions, their characterizations, and when minimizers exist.

**1.1 Mathematical Background**  
Notation, Cauchy–Schwarz, spectral norm, mean value theorem, differentiability.  
*Terms:* Cauchy-Schwarz, spectral norm, mean value theorem, Jacobian  
→ PDF pp. 5–10 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**1.2 Convex sets**  
Convex sets and the mean value inequality.  
*Terms:* convex set  
→ PDF pp. 11–13 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**1.3 Convex functions**  
Convex functions and first- and second-order characterizations.  
*Terms:* convex function, first-order condition, second-order condition, Hessian  
→ PDF pp. 14–21 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**1.4 Minimizing convex functions**  
Global minima of convex functions, strict convexity, least squares, constraints.  
*Terms:* global minimum, strict convexity, least squares, constrained minimization  
→ PDF pp. 22–26 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**1.5 Existence of a minimizer**  
Sublevel sets and the Weierstrass theorem.  
*Terms:* sublevel set, Weierstrass theorem  
→ PDF pp. 27–28 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**1.6 Examples**  
Worked examples: digit recognition and an admissions model.  
*Terms:* examples  
→ PDF pp. 29–39 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch2"></a>
## 2. Gradient Descent

*PDF pp. 39–62*

The basic method and its convergence rates under increasingly strong assumptions, plus acceleration.

**2.1 Overview**  
Why gradient descent, and its setting.  
*Terms:* gradient descent  
→ PDF pp. 40–41 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**2.2 The algorithm**  
The update rule.  
*Terms:* step size  
→ PDF p. 42 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**2.3 Vanilla analysis**  
A one-page analysis that the later results refine.  
*Terms:* vanilla analysis  
→ PDF pp. 43–44 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**2.4 Lipschitz convex functions: O(1/ε2) steps**  
O(1/ε²) steps for Lipschitz convex functions.  
*Terms:* Lipschitz convex, O(1/ε²)  
→ PDF pp. 45–46 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**2.5 Smooth convex functions: O(1/ε) steps**  
O(1/ε) steps for smooth convex functions.  
*Terms:* smooth convex, L-smooth, O(1/ε)  
→ PDF pp. 47–54 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**2.7 Interlude**  
An interlude, then Nesterov acceleration and linear rates under strong convexity.  
*Terms:* Nesterov acceleration, strong convexity, linear convergence  
→ PDF pp. 55–62 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch3"></a>
## 3. Projected and Proximal Gradient Descent

*PDF pp. 62–78*

Handling constraints by projection and nonsmooth terms by proximal steps.

**3.1 The Algorithm**  
Projected gradient descent.  
*Terms:* projected gradient descent  
→ PDF p. 63 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**3.2 Bounded gradients: O(1/ε2) steps**  
Rate with bounded gradients.  
*Terms:* bounded gradients  
→ PDF p. 64 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**3.3 Smooth convex functions: O(1/ε) steps**  
Rate for smooth functions.  
*Terms:* smoothness  
→ PDF pp. 65–67 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**3.4 Smooth and strongly convex functions: O(log(1/ε))**  
Linear rate for smooth strongly convex functions.  
*Terms:* strong convexity  
→ PDF pp. 68–69 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**3.5 Projecting onto ℓ1-balls**  
Fast projection onto ℓ1 balls.  
*Terms:* l1-ball projection  
→ PDF pp. 70–73 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**3.6 Proximal gradient descent**  
Proximal gradient descent for composite objectives such as the lasso.  
*Terms:* proximal gradient descent, proximal operator, lasso, ISTA  
→ PDF pp. 74–78 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch4"></a>
## 4. Subgradient Descent

*PDF pp. 78–89*

Gradient descent for nondifferentiable convex functions, and lower bounds for first-order methods.

**4.1 Subgradients**  
Subgradients of convex functions.  
*Terms:* subgradient, subdifferential  
→ PDF pp. 79–80 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**4.2 Differentiability of convex functions**  
Convex functions are differentiable almost everywhere.  
*Terms:* differentiability almost everywhere  
→ PDF p. 81 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**4.3 The algorithm**  
The subgradient method.  
*Terms:* subgradient method  
→ PDF p. 82 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**4.4 Lipschitz convex functions: O(1/ε2) steps**  
O(1/ε²) for Lipschitz functions.  
*Terms:* Lipschitz functions  
→ PDF p. 82 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**4.5 Tame strong convexity: O(1/ε) steps**  
Better rates with strong convexity.  
*Terms:* strong convexity  
→ PDF pp. 83–85 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**4.6 Optimality of first-order methods**  
Lower bounds showing these rates are optimal for first-order methods.  
*Terms:* lower bounds, first-order oracle  
→ PDF pp. 86–89 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch5"></a>
## 5. Stochastic Gradient Descent

*PDF pp. 89–97*

Noisy gradient estimates from samples: rates and mini-batching.

**5.1 The algorithm**  
SGD with one sampled gradient per step.  
*Terms:* stochastic gradient descent, SGD  
→ PDF p. 90 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**5.2 Unbiasedness**  
Unbiased gradient estimates.  
*Terms:* unbiased estimator  
→ PDF p. 91 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**5.3 Bounded stochastic gradients: O(1/ε2) steps**  
Rate with bounded stochastic gradients.  
*Terms:* bounded variance  
→ PDF p. 92 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**5.4 Tame strong convexity: O(1/ε) steps**  
Rate with strong convexity.  
*Terms:* strong convexity  
→ PDF p. 93 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**5.5 Stochastic Subgradient Descent**  
Stochastic subgradient descent.  
*Terms:* stochastic subgradient  
→ PDF p. 94 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**5.6 Mini-batch variants**  
Mini-batches to reduce variance.  
*Terms:* mini-batch  
→ PDF pp. 94–97 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch6"></a>
## 6. Nonconvex functions

*PDF pp. 97–116*

What gradient descent guarantees without convexity, and trajectory analyses.

**6.1 Smooth functions**  
Convergence to stationary points for smooth nonconvex functions.  
*Terms:* nonconvex optimization, stationary point  
→ PDF pp. 99–103 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**6.2 Trajectory analysis**  
Trajectory-based analyses of specific nonconvex problems.  
*Terms:* trajectory analysis  
→ PDF pp. 104–116 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch7"></a>
## 7. Newton’s Method

*PDF pp. 116–128*

Second-order steps and local quadratic convergence.

**7.2 Newton’s method for optimization**  
Newton’s method as minimizing a local quadratic model.  
*Terms:* Newton’s method  
→ PDF pp. 119–120 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**7.3 Once you’re close, you’re there. . .**  
Quadratic convergence once close to the optimum.  
*Terms:* quadratic convergence  
→ PDF pp. 121–128 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch8"></a>
## 8. Quasi-Newton Methods

*PDF pp. 128–146*

Approximating the Hessian from gradient differences: secant methods and BFGS.

**8.1 The secant method**  
The secant method in one dimension.  
*Terms:* secant method  
→ PDF pp. 129–130 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**8.2 The secant condition**  
The secant condition for Hessian approximations.  
*Terms:* secant condition  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**8.3 Quasi-Newton methods**  
Quasi-Newton updates including BFGS.  
*Terms:* quasi-Newton, BFGS  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**8.4 Greenstadt’s approach (Optional Material)**  
Greenstadt’s derivation (optional).  
*Terms:* Greenstadt  
→ PDF pp. 132–146 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch9"></a>
## 9. Coordinate Descent

*PDF pp. 146–161*

Updating one coordinate at a time, with coordinate-wise smoothness.

**9.1 Overview**  
Motivation for coordinate methods.  
*Terms:* coordinate descent  
→ PDF p. 147 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**9.2 Alternative analysis of gradient descent**  
Re-deriving gradient-descent rates in a new way.  
*Terms:* gradient descent analysis  
→ PDF pp. 147–148 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**9.3 Coordinate-wise smoothness**  
Smoothness per coordinate.  
*Terms:* coordinate-wise smoothness  
→ PDF p. 149 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**9.4 Coordinate descent algorithms**  
Random, greedy and cyclic coordinate rules and their rates.  
*Terms:* randomized coordinate descent, greedy coordinate descent  
→ PDF pp. 150–158 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**9.5 Summary**  
Summary of rates.  
*Terms:* rates summary  
→ PDF pp. 159–161 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)


---

<a id="ch10"></a>
## 10. The Frank-Wolfe Algorithm

*PDF pp. 161–181*

Projection-free optimization over constraint sets via linear minimization.

**10.1 Overview**  
Why avoid projections.  
*Terms:* Frank-Wolfe, conditional gradient  
→ PDF p. 162 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**10.2 The Algorithm**  
The Frank–Wolfe step via a linear minimization oracle.  
*Terms:* linear minimization oracle  
→ PDF pp. 163–164 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**10.3 On linear minimization oracles**  
Oracles for common constraint sets.  
*Terms:* LMO  
→ PDF pp. 165–166 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**10.4 Duality gap — A certificate for optimization**  
The duality gap as a stopping certificate.  
*Terms:* duality gap  
→ PDF p. 167 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**10.5 Convergence in O(1/ε) steps**  
O(1/ε) convergence.  
*Terms:* convergence rate  
→ PDF pp. 168–174 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

**10.6 Sparsity, extensions and use cases**  
Sparse iterates and applications.  
*Terms:* sparsity  
→ PDF pp. 175–181 in [the PDF](https://drive.google.com/file/d/129pKy5xEIoYN036tVqiGPKff23K1lDqr/view)

