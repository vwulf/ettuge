<a id="ch1"></a>
# Concise Machine Learning

> Jonathan Richard Shewchuk · UC Berkeley CS 189/289A lecture notes, Spring 2024 · [the PDF in Drive](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)

Lecture notes compiled into one report, one chapter per lecture (no numbered sections); PDF page = printed page + 6. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Shewchuk’s notes for Berkeley’s undergraduate machine learning course, written with his characteristic geometric pictures and blunt asides. They move from linear classifiers (perceptron, hard- and soft-margin SVMs) through decision theory and Gaussian discriminant analysis (QDA, LDA) to regression (least squares, logistic, ridge, lasso) and the bias–variance decomposition, then decision trees and random forests, kernels, neural networks and CNNs. The unsupervised part covers PCA, the SVD, clustering and high-dimensional geometry, followed by learning theory, boosting and nearest-neighbor methods with k-d trees, and two bonus lectures on spectral graph clustering and latent factor analysis.

**Contents**

1. [Lecture 1: Introduction](ch1): Classification, validation, overfitting, and what the course covers.
2. [Lecture 2: Linear Classifiers and Perceptrons](ch2): Decision boundaries, linear classifiers, and the perceptron’s goal.
3. [Lecture 3: Perceptron Learning; Maximum Margin Classifiers](ch3): The perceptron algorithm and the hard-margin SVM.
4. [Lecture 4: Soft-Margin Support Vector Machines; Features](ch4): Slack variables for non-separable data, and adding features to get nonlinear boundaries.
5. [Lecture 5: Machine Learning Abstractions and Numerical Optimization](ch5): How ML problems decompose into model, objective and optimizer; gradient descent, Newton and convex programs.
6. [Lecture 6: Decision Theory; Generative and Discriminative Models](ch6): Bayes risk, loss functions, and generative versus discriminative models.
7. [Lecture 7: Gaussian Discriminant Analysis, including QDA and LDA](ch7): Fitting Gaussians per class: QDA and LDA decision boundaries.
8. [Lecture 8: Eigenvectors and the (Anisotropic) Multivariate Normal Distribution](ch8): Eigenvectors, quadratic forms and the anisotropic multivariate normal.
9. [Lecture 9: Anisotropic Gaussians: Maximum Likelihood Estimation, QDA, and LDA](ch9): Maximum likelihood for anisotropic Gaussians, applied to QDA and LDA.
10. [Lecture 10: Regression, including Least-Squares Linear and Logistic Regression](ch10): Least-squares linear regression and logistic regression.
11. [Lecture 11: More Regression; Newton’s Method; ROC Curves](ch11): Weighted and polynomial regression, Newton’s method for logistic regression, ROC curves.
12. [Lecture 12: Statistical Justifications; the Bias-Variance Decomposition](ch12): Regression as maximum likelihood and MAP; bias, variance and noise.
13. [Lecture 13: Shrinkage: Ridge Regression, Subset Selection, and Lasso](ch13): Ridge regression, subset selection and the lasso.
14. [Lecture 14: Decision Trees](ch14): Building decision trees by greedy splitting on information gain.
15. [Lecture 15: More Decision Trees, Ensemble Learning, and Random Forests](ch15): Pruning, multivariate splits, bagging, random forests and ensembles.
16. [Lecture 16: The Kernel Trick](ch16): Kernelized algorithms and common kernels, including the Gaussian.
17. [Lecture 17: Neural Networks](ch17): Feedforward networks and backpropagation.
18. [Lecture 18: Vanishing Gradients; ReLUs; Output Units and Losses; Neurobiology](ch18): Vanishing gradients, ReLU, output units and losses, and the neuroscience behind neural nets.
19. [Lecture 19: Better Neural Network Training; Convolutional Neural Networks](ch19): Training heuristics (initialization, momentum, normalization) and convolutional networks.
20. [Lecture 20: Unsupervised Learning and Principal Components Analysis](ch20): Unsupervised learning and principal components analysis.
21. [Lecture 21: The Singular Value Decomposition; Clustering](ch21): The SVD, and clustering with k-means and hierarchical methods.
22. [Lecture 22: High Dimensions; Random Projection; the Pseudoinverse](ch22): Behavior of high-dimensional data, random projection and the pseudoinverse.
23. [Lecture 23: Learning Theory](ch23): Generalization bounds, VC dimension and dichotomies.
24. [Lecture 24: Boosting; Nearest Neighbor Classification](ch24): AdaBoost, and nearest-neighbor classification.
25. [Lecture 25: Nearest Neighbor Algorithms: Voronoi Diagrams and k-d Trees](ch25): Exact and approximate nearest-neighbor search with Voronoi diagrams and k-d trees.
26. [A. Bonus Lecture: Spectral Graph Clustering](ch26): Graph partitioning via the Fiedler vector and normalized cuts.
27. [B. Bonus Lecture: Multiple Eigenvectors; Latent Factor Analysis](ch27): Spectral clustering with several eigenvectors, and latent factor analysis.


---

## Lecture 1: Introduction

*PDF pp. 7–12*

Classification, validation, overfitting, and what the course covers.

*Terms:* classification, validation, overfitting

→ PDF pp. 7–12 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch2"></a>
## Lecture 2: Linear Classifiers and Perceptrons

*PDF pp. 13–18*

Decision boundaries, linear classifiers, and the perceptron’s goal.

*Terms:* linear classifier, decision boundary, perceptron

→ PDF pp. 13–18 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch3"></a>
## Lecture 3: Perceptron Learning; Maximum Margin Classifiers

*PDF pp. 19–23*

The perceptron algorithm and the hard-margin SVM.

*Terms:* perceptron algorithm, hard-margin SVM, maximum margin

→ PDF pp. 19–23 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch4"></a>
## Lecture 4: Soft-Margin Support Vector Machines; Features

*PDF pp. 24–30*

Slack variables for non-separable data, and adding features to get nonlinear boundaries.

*Terms:* soft-margin SVM, slack variables, feature engineering

→ PDF pp. 24–30 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch5"></a>
## Lecture 5: Machine Learning Abstractions and Numerical Optimization

*PDF pp. 31–36*

How ML problems decompose into model, objective and optimizer; gradient descent, Newton and convex programs.

*Terms:* gradient descent, Newton’s method, convex optimization, linear program, quadratic program

→ PDF pp. 31–36 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch6"></a>
## Lecture 6: Decision Theory; Generative and Discriminative Models

*PDF pp. 37–41*

Bayes risk, loss functions, and generative versus discriminative models.

*Terms:* decision theory, Bayes risk, generative model, discriminative model

→ PDF pp. 37–41 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch7"></a>
## Lecture 7: Gaussian Discriminant Analysis, including QDA and LDA

*PDF pp. 42–46*

Fitting Gaussians per class: QDA and LDA decision boundaries.

*Terms:* QDA, LDA, Gaussian discriminant analysis

→ PDF pp. 42–46 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch8"></a>
## Lecture 8: Eigenvectors and the (Anisotropic) Multivariate Normal Distribution

*PDF pp. 47–52*

Eigenvectors, quadratic forms and the anisotropic multivariate normal.

*Terms:* eigenvectors, multivariate normal, covariance

→ PDF pp. 47–52 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch9"></a>
## Lecture 9: Anisotropic Gaussians: Maximum Likelihood Estimation, QDA, and LDA

*PDF pp. 53–59*

Maximum likelihood for anisotropic Gaussians, applied to QDA and LDA.

*Terms:* maximum likelihood estimation, QDA, LDA

→ PDF pp. 53–59 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch10"></a>
## Lecture 10: Regression, including Least-Squares Linear and Logistic Regression

*PDF pp. 60–64*

Least-squares linear regression and logistic regression.

*Terms:* least squares, linear regression, logistic regression

→ PDF pp. 60–64 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch11"></a>
## Lecture 11: More Regression; Newton’s Method; ROC Curves

*PDF pp. 65–70*

Weighted and polynomial regression, Newton’s method for logistic regression, ROC curves.

*Terms:* Newton’s method, ROC curve, weighted regression

→ PDF pp. 65–70 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch12"></a>
## Lecture 12: Statistical Justifications; the Bias-Variance Decomposition

*PDF pp. 71–76*

Regression as maximum likelihood and MAP; bias, variance and noise.

*Terms:* MAP, bias-variance decomposition

→ PDF pp. 71–76 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch13"></a>
## Lecture 13: Shrinkage: Ridge Regression, Subset Selection, and Lasso

*PDF pp. 77–81*

Ridge regression, subset selection and the lasso.

*Terms:* ridge regression, lasso, subset selection

→ PDF pp. 77–81 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch14"></a>
## Lecture 14: Decision Trees

*PDF pp. 82–86*

Building decision trees by greedy splitting on information gain.

*Terms:* decision tree, entropy, information gain

→ PDF pp. 82–86 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch15"></a>
## Lecture 15: More Decision Trees, Ensemble Learning, and Random Forests

*PDF pp. 87–94*

Pruning, multivariate splits, bagging, random forests and ensembles.

*Terms:* random forest, bagging, ensemble learning, pruning

→ PDF pp. 87–94 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch16"></a>
## Lecture 16: The Kernel Trick

*PDF pp. 95–99*

Kernelized algorithms and common kernels, including the Gaussian.

*Terms:* kernel trick, Gaussian kernel, kernel perceptron

→ PDF pp. 95–99 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch17"></a>
## Lecture 17: Neural Networks

*PDF pp. 100–106*

Feedforward networks and backpropagation.

*Terms:* neural network, backpropagation

→ PDF pp. 100–106 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch18"></a>
## Lecture 18: Vanishing Gradients; ReLUs; Output Units and Losses; Neurobiology

*PDF pp. 107–113*

Vanishing gradients, ReLU, output units and losses, and the neuroscience behind neural nets.

*Terms:* vanishing gradients, ReLU, softmax, cross-entropy

→ PDF pp. 107–113 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch19"></a>
## Lecture 19: Better Neural Network Training; Convolutional Neural Networks

*PDF pp. 114–121*

Training heuristics (initialization, momentum, normalization) and convolutional networks.

*Terms:* CNN, momentum, batch normalization, initialization

→ PDF pp. 114–121 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch20"></a>
## Lecture 20: Unsupervised Learning and Principal Components Analysis

*PDF pp. 122–130*

Unsupervised learning and principal components analysis.

*Terms:* unsupervised learning, PCA

→ PDF pp. 122–130 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch21"></a>
## Lecture 21: The Singular Value Decomposition; Clustering

*PDF pp. 131–138*

The SVD, and clustering with k-means and hierarchical methods.

*Terms:* SVD, k-means, hierarchical clustering

→ PDF pp. 131–138 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch22"></a>
## Lecture 22: High Dimensions; Random Projection; the Pseudoinverse

*PDF pp. 139–143*

Behavior of high-dimensional data, random projection and the pseudoinverse.

*Terms:* high dimensions, random projection, Johnson-Lindenstrauss, pseudoinverse

→ PDF pp. 139–143 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch23"></a>
## Lecture 23: Learning Theory

*PDF pp. 144–149*

Generalization bounds, VC dimension and dichotomies.

*Terms:* learning theory, VC dimension, generalization bound

→ PDF pp. 144–149 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch24"></a>
## Lecture 24: Boosting; Nearest Neighbor Classification

*PDF pp. 150–154*

AdaBoost, and nearest-neighbor classification.

*Terms:* AdaBoost, boosting, k-nearest neighbors

→ PDF pp. 150–154 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch25"></a>
## Lecture 25: Nearest Neighbor Algorithms: Voronoi Diagrams and k-d Trees

*PDF pp. 155–159*

Exact and approximate nearest-neighbor search with Voronoi diagrams and k-d trees.

*Terms:* Voronoi diagram, k-d tree, nearest neighbor search

→ PDF pp. 155–159 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch26"></a>
## A. Bonus Lecture: Spectral Graph Clustering

*PDF pp. 160–167*

Graph partitioning via the Fiedler vector and normalized cuts.

*Terms:* spectral clustering, Fiedler vector, normalized cut, graph Laplacian

→ PDF pp. 160–167 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)


---

<a id="ch27"></a>
## B. Bonus Lecture: Multiple Eigenvectors; Latent Factor Analysis

*PDF pp. 168–174*

Spectral clustering with several eigenvectors, and latent factor analysis.

*Terms:* latent factor analysis, spectral clustering

→ PDF pp. 168–174 in [the PDF](https://drive.google.com/file/d/1-0ritizBiXATR96iC8Dri0vjPaYchvZ9/view)

