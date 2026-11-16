<a id="ch1"></a>
# Deep Learning and Computational Physics (lecture notes)

> Deep Ray, Orazio Pinti and Assad A. Oberai · USC course notes, 2023 · [the PDF in Drive](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

Course notes rather than a polished book; sections often end with questions for the reader. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

These notes teach deep learning to people who already know numerical methods for physics, and keep drawing the parallel between the two. Networks are introduced as function approximators with universal approximation results; ResNets are read as time-stepping schemes, which leads to neural ODEs; convolutions are compared with finite-difference stencils. The physics-specific core is solving PDEs with networks: physics-informed neural networks (PINNs) that put the PDE residual in the loss, then operator networks (DeepONet and the Fourier Neural Operator) that learn the whole map from inputs to solutions. The last chapter adds probability and generative models (GANs) for problems with uncertain or multiple answers.

**Contents**

1. [1 Introduction](ch1): Computational physics starts from laws, machine learning from data; the notes motivate combining them.
2. [2 Introduction to deep neural networks](ch2): MLPs, activation functions, approximation theorems, training and generalization, optimizers and backpropagation.
3. [3 Residual neural networks](ch3): Vanishing gradients, residual networks, and the reading of ResNets as forward-Euler steps of an ODE, leading to neural ODEs.
4. [4 Solving PDEs with MLPs](ch4): Classical PDE solvers next to physics-informed neural networks, with error analysis and data assimilation.
5. [5 Convolutional Neural Networks](ch5): Convolutions of functions and images, their link to finite differences, CNN layers and image-to-image networks.
6. [6 Operator Networks](ch6): Learning solution operators for parametrized PDEs: DeepONet and the Fourier Neural Operator.
7. [7 Probabilistic Deep Learning](ch7): Probability basics and probabilistic deep learning: generative models for uncertainty and inverse problems.


---

## 1 Introduction

*PDF pp. 5–9*

Computational physics starts from laws, machine learning from data; the notes motivate combining them.

**1.1 Computational physics**  
Physics-based models: postulate a law, discretize it, solve numerically.  
*Terms:* computational physics  
→ PDF p. 5 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**1.2 Machine learning**  
ML steps: collect data, choose a model, train it on the data.  
*Terms:* machine learning workflow  
→ PDF p. 6 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**1.3 Artificial Intelligence, Machine Learning and Deep Learning**  
Supervised, unsupervised, semi-supervised and reinforcement learning, and where deep learning fits.  
*Terms:* supervised learning, unsupervised learning, semi-supervised learning, reinforcement learning  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**1.4 Machine learning and computational physics**  
How ML and physics solvers complement each other, using a self-driving-car pipeline as illustration.  
*Terms:* physics-based ML, semantic segmentation  
→ PDF pp. 8–9 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)


---

<a id="ch2"></a>
## 2 Introduction to deep neural networks

*PDF pp. 10–27*

MLPs, activation functions, approximation theorems, training and generalization, optimizers and backpropagation.

**2.1 MLP architecture**  
Layers of neurons, weights and biases, and the network as a composed function.  
*Terms:* MLP, weights, bias  
→ PDF p. 10 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.2 Activation functions**  
ReLU, leaky ReLU, logistic, tanh and others, with their properties.  
*Terms:* ReLU, leaky ReLU, logistic, tanh  
→ PDF pp. 11–13 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.3 Expressivity of a network**  
Universal approximation theorems (Pinkus and others) and why depth helps.  
*Terms:* universal approximation theorem, expressivity  
→ PDF pp. 14–15 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.4 Training, validation and testing of neural networks**  
Loss, training/validation/test splits, and overfitting.  
*Terms:* training set, validation set, test set, overfitting  
→ PDF pp. 16–17 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.5 Generalizability**  
Generalization and sensitivity to inputs; regularization.  
*Terms:* generalization, regularization  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.6 Gradient descent**  
Gradient descent and its convergence.  
*Terms:* gradient descent  
→ PDF pp. 19–20 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.7 Some advanced optimization algorithms**  
Momentum, RMSProp, Adam; mini-batches and epochs.  
*Terms:* momentum, RMSProp, Adam, mini-batch, epoch  
→ PDF pp. 21–23 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.8 Calculating gradients using back-propagation**  
Backpropagation derived layer by layer.  
*Terms:* backpropagation  
→ PDF pp. 24–25 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**2.9 Regression versus classification**  
Losses for regression versus classification (cross-entropy, softmax).  
*Terms:* regression, classification, cross-entropy, softmax  
→ PDF pp. 26–27 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)


---

<a id="ch3"></a>
## 3 Residual neural networks

*PDF pp. 28–33*

Vanishing gradients, residual networks, and the reading of ResNets as forward-Euler steps of an ODE, leading to neural ODEs.

**3.1 Vanishing gradients in deep networks**  
Why gradients shrink in very deep networks.  
*Terms:* vanishing gradients  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**3.2 ResNets**  
Skip connections let gradients bypass layers.  
*Terms:* ResNet, skip connections  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**3.3 Connections with ODEs**  
A residual block is a forward-Euler step of an ODE.  
*Terms:* forward Euler, ODE  
→ PDF p. 30 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**3.4 Neural ODEs**  
Taking the step to zero gives neural ODEs: a network defines a vector field integrated by an ODE solver.  
*Terms:* neural ODE  
→ PDF pp. 31–33 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)


---

<a id="ch4"></a>
## 4 Solving PDEs with MLPs

*PDF pp. 34–44*

Classical PDE solvers next to physics-informed neural networks, with error analysis and data assimilation.

**4.1 Finite difference method**  
Discretize derivatives on a grid and solve a linear system.  
*Terms:* finite difference method, central difference  
→ PDF p. 35 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**4.2 Spectral collocation method**  
Approximate the solution with global basis functions and enforce the PDE at collocation points.  
*Terms:* spectral collocation  
→ PDF pp. 36–38 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**4.3 Physics-informed neural networks (PINNs)**  
Represent the solution with a network and minimize the PDE residual at collocation points via automatic differentiation.  
*Terms:* PINN, physics-informed neural network, collocation points  
→ PDF pp. 39–40 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**4.4 Extending PINNs to a more general PDE**  
Adding boundary conditions as penalty terms and handling general PDEs.  
*Terms:* boundary conditions, penalty  
→ PDF p. 41 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**4.5 Error analysis for PINNs**  
Sources of error: optimization, collocation sampling and network capacity, with a stability bound.  
*Terms:* PINN error analysis  
→ PDF p. 42 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**4.6 Data assimilation using PINNs**  
Combining PDE residuals with measured data to infer unknown fields or parameters.  
*Terms:* data assimilation, inverse problems  
→ PDF pp. 43–44 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)


---

<a id="ch5"></a>
## 5 Convolutional Neural Networks

*PDF pp. 45–57*

Convolutions of functions and images, their link to finite differences, CNN layers and image-to-image networks.

**5.1 Functions and images**  
Images as sampled functions.  
*Terms:* images as functions  
→ PDF p. 45 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**5.2 Convolutions of functions**  
Convolution as a smoothing or differentiating kernel acting on a function.  
*Terms:* convolution, kernel  
→ PDF pp. 45–46 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**5.3 Discrete convolutions**  
Discrete convolutions on grids.  
*Terms:* discrete convolution  
→ PDF pp. 47–48 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**5.4 Connection to finite differences**  
A convolution kernel is a finite-difference stencil.  
*Terms:* finite difference stencil  
→ PDF p. 49 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**5.5 Convolution layers**  
Kernel size, stride, padding and channels in a convolution layer.  
*Terms:* convolution layer, stride, padding, channels  
→ PDF pp. 49–51 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**5.6 Convolution Neural Network (CNN)**  
Stacking convolutions and pooling into a CNN.  
*Terms:* CNN, pooling  
→ PDF pp. 52–53 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**5.7 Transpose convolution layers**  
Upsampling with transposed convolutions.  
*Terms:* transpose convolution, upsampling  
→ PDF pp. 54–56 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**5.8 Image-to-image transformations**  
Encoder–decoder networks mapping one field to another, like source to solution.  
*Terms:* image-to-image, encoder-decoder  
→ PDF p. 57 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)


---

<a id="ch6"></a>
## 6 Operator Networks

*PDF pp. 58–70*

Learning solution operators for parametrized PDEs: DeepONet and the Fourier Neural Operator.

**6.1 The problem with PINNs**  
A PINN must be retrained for each new parameter or input.  
*Terms:* PINN limitations  
→ PDF p. 58 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.2 Parametrized PDEs**  
Including the PDE parameters as network inputs.  
*Terms:* parametrized PDE  
→ PDF p. 58 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.3 Operators**  
Operators map functions to functions; examples from PDEs.  
*Terms:* operator learning  
→ PDF p. 59 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.4 Deep Operator Network (DeepONet) Architecture**  
DeepONet: a branch net for the input function and a trunk net for coordinates, combined like basis expansions.  
*Terms:* DeepONet, branch net, trunk net  
→ PDF pp. 60–61 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.5 Training DeepONets**  
Training DeepONets on input–output function pairs.  
*Terms:* DeepONet training  
→ PDF p. 62 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.6 Error Analysis for DeepONets**  
Universal approximation for operators and error bounds.  
*Terms:* operator approximation theorem  
→ PDF p. 63 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.7 Physics-Informed DeepONets**  
Adding the PDE residual to DeepONet training.  
*Terms:* physics-informed DeepONet  
→ PDF p. 64 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.8 Fourier Neural Operators - Architecture**  
FNO: layers that act by convolution in Fourier space, motivated by Green’s functions.  
*Terms:* Fourier Neural Operator, FNO, Green’s function  
→ PDF pp. 65–66 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.9 Discretization of the Fourier Neural Operator**  
Discretizing FNO layers on grids.  
*Terms:* FNO discretization  
→ PDF p. 67 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**6.10 The Use of Fourier Transforms**  
Why FFTs make FNO efficient and resolution-independent.  
*Terms:* FFT, resolution independence  
→ PDF pp. 68–70 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)


---

<a id="ch7"></a>
## 7 Probabilistic Deep Learning

*PDF pp. 71–88*

Probability basics and probabilistic deep learning: generative models for uncertainty and inverse problems.

**7.1 Key elements of Probability Theory**  
Sample spaces, probability axioms and conditional probability.  
*Terms:* probability axioms, conditional probability  
→ PDF pp. 71–72 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**7.2 Random Variables**  
Random variables, densities, expectation, covariance and conditional densities.  
*Terms:* random variables, pdf, expectation, covariance  
→ PDF pp. 73–79 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**7.3 Unsupervised probabilistic deep learning algorithms**  
Generative models learned without labels: GANs and their training algorithm.  
*Terms:* GAN, generative models  
→ PDF pp. 80–82 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

**7.4 Supervised probabilistic deep learning algorithms**  
Conditional generative models for supervised problems such as inverse problems with many solutions.  
*Terms:* conditional GAN, inverse problems, uncertainty quantification  
→ PDF pp. 83–88 in [the PDF](https://drive.google.com/file/d/1XAxuWhLy4mMAFmTVJlfGEQFiyI2MP3Go/view)

