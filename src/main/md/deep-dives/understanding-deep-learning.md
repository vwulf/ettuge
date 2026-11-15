<a id="ch1"></a>
# Textbook: Understanding Deep Learning

> Simon J. D. Prince · draft of January 23, 2023 (MIT Press) · [the PDF in Drive](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

This page breaks one textbook down from the top. The book summary comes first, then one chapter per page. Each chapter page lists its sections, and each section points to its pages in the PDF. The summaries are written in our own words from a read of this draft. The text itself stays in the PDF, so the last step down is opening it at the pages given. Book page numbers are the printed ones; PDF page numbers count from the cover (book page = PDF page − 13). This draft predates the published edition, so its numbering differs from the edition on the author's site.

**Related pages on this site**
- [Technical › Deep Learning](https://vwulf.github.io/ettuge/Books/Technical#deep-learning): the catalog entry.
- [AI Deep Dives](https://vwulf.github.io/ettuge/Deep-Dives/ai): papers on the same topics, read in depth.

## The book in one paragraph

Prince builds deep learning from one idea outward: a network is a parameterized family of functions, and training picks one member of that family. With ReLU activations every network is piecewise linear, so the early chapters can draw exactly what shallow and deep networks compute: linear regions, joints and folds of input space. Losses then come from maximum likelihood, fitting from gradient methods, and generalization from bias, variance and double descent. The middle of the book adds the architectures that share parameters or route information: convolutions, residual connections, transformers and graph networks. The last part covers four families of generative models (GANs, normalizing flows, VAEs, diffusion), each framed by what it can and cannot do: sample, evaluate likelihood, or both.

**Contents**

1. [Introduction](ch1): What deep learning is, the three settings it is used in, and how the book is organized. It closes with an unusually direct section on the ethics of AI.
2. [Supervised learning](ch2): The whole supervised pipeline on the smallest possible example: a straight line fitted to points.
3. [Shallow neural networks](ch3): Networks with one hidden layer, analyzed geometrically. With ReLU they produce piecewise-linear functions, and enough hidden units can approximate anything.
4. [Deep neural networks](ch4): Why depth helps: composing networks folds input space, so deep networks create far more linear regions per parameter than shallow ones.
5. [Loss functions](ch5): Where loss functions come from: the network predicts the parameters of a probability distribution over outputs, and training maximizes the likelihood of the data.
6. [Fitting models](ch6): How parameters are actually found: gradient descent and the stochastic, momentum-based and adaptive refinements used in practice.
7. [Gradients and initialization](ch7): Two problems specific to neural networks: computing gradients for every parameter efficiently, and initializing so that signals neither explode nor vanish.
8. [Measuring performance](ch8): How to measure and explain test error, from the classical bias-variance trade-off to double descent in over-parameterized models.
9. [Regularization](ch9): Techniques that shrink the gap between training and test performance, from explicit penalty terms to the implicit biases of SGD and a long list of heuristics.
10. [Convolutional networks](ch10): Convolutional layers for grid data: weight sharing builds in translation equivariance, which cuts parameters and improves generalization.
11. [Residual networks](ch11): Residual connections make very deep networks trainable; batch normalization keeps their activations in check.
12. [Transformers](ch12): Transformers: self-attention lets every token weigh every other, with parameters shared across positions. Covers the architecture and its main uses in language and vision.
13. [Graph neural networks](ch13): Graph neural networks: layers that must be equivariant to node order, and the extra problems of huge or single graphs.
14. [Unsupervised learning](ch14): A short map of unsupervised learning that frames the next four chapters.
15. [Generative Adversarial Networks](ch15): GANs generate samples by fooling a discriminator. Much of the chapter is about why training is unstable and how to fix it.
16. [Normalizing flows](ch16): Normalizing flows transform a simple distribution through invertible layers, so they can both sample and compute exact likelihoods.
17. [Variational autoencoders](ch17): VAEs train a nonlinear latent-variable model by maximizing a lower bound on likelihood, using an encoder to approximate the posterior.
18. [Diffusion models](ch18): Diffusion models add noise in many small steps and learn to undo them. The ELBO reduces to a simple noise-prediction loss.

The remaining parts of this draft:

- **19. Reinforcement learning**: A placeholder in this draft; the chapter was not yet written.
- **20. Why does deep learning work?**: A placeholder in this draft; the chapter was not yet written.
- **Appendices**: Notation, probability (expectations and common distributions) and a short maths reference, mostly section headings in this draft.


---

## 1. Introduction

*PDF pp. 14–29 (book pp. 1–16)*

What deep learning is, the three settings it is used in, and how the book is organized. It closes with an unusually direct section on the ethics of AI.

**1.1 Supervised learning**  
Supervised learning maps inputs to outputs: regression predicts numbers, classification predicts categories, and structured outputs (text, images, segmentations) are the hard case. Deep networks are introduced as one very flexible family of such mappings.  
→ PDF pp. 14–20 (book pp. 1–7) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**1.2 Unsupervised learning**  
Unsupervised learning works without labels. Generative models learn to produce new examples like the data, and latent variables give a compact explanation of what varies between examples.  
→ PDF pp. 20–24 (book pp. 7–11) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**1.3 Reinforcement learning**  
Shows how latent variables also help supervised problems with structured outputs, then introduces reinforcement learning: an agent acts, the world changes, rewards arrive late. Temporal credit assignment and the explore/exploit trade-off are the core difficulties.  
→ PDF pp. 24–25 (book pp. 11–12) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**1.4 Structure of book**  
Two worked RL examples (robot locomotion, chess), then the book's roadmap: supervised pipeline first, then specialized architectures, then generative models.  
→ PDF pp. 25–26 (book pp. 12–13) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**1.5 Ethics**  
Five concerns are named: bias and fairness, explainability, weaponization, concentration of power, and existential risk. The author argues researchers carry real responsibility for how the technology is used.  
→ PDF pp. 26–28 (book pp. 13–15) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**1.6 Other books**  
Continues the ethics discussion (accountability, who funds AI, whether harm can be controlled) and lists complementary books.  
→ PDF pp. 28–29 (book pp. 15–16) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**1.7 How to read this book**  
How each chapter is laid out (main text, notes, problems) and where the background maths lives.  
→ PDF p. 29 (book p. 16) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch2"></a>
## 2. Supervised learning

*PDF pp. 30–37 (book pp. 17–24)*

The whole supervised pipeline on the smallest possible example: a straight line fitted to points.

**2.1 Supervised learning overview**  
A model is an equation with parameters; inference runs it, training searches for parameter values that make predictions match a training set.  
→ PDF pp. 30–32 (book pp. 17–19) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**2.2 Linear regression example**  
One input, one output, two parameters. A least-squares loss scores each line, and the loss over all parameter values forms a surface that training walks down.  
→ PDF pp. 32–35 (book pp. 19–22) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**2.3 Summary**  
Training descends the loss surface by gradient; testing on held-out data shows whether the fit generalizes. Too simple a model underfits, too flexible a model overfits.  
→ PDF pp. 35–37 (book pp. 22–24) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch3"></a>
## 3. Shallow neural networks

*PDF pp. 38–53 (book pp. 25–40)*

Networks with one hidden layer, analyzed geometrically. With ReLU they produce piecewise-linear functions, and enough hidden units can approximate anything.

**3.1 Neural network example**  
A 1D network with three hidden units: three linear functions, each clipped by a ReLU, then summed with weights. The result is piecewise linear with joints where units switch on or off.  
→ PDF pp. 38–42 (book pp. 25–29) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**3.2 Universal approximation theorem**  
With D hidden units a 1D network has at most D+1 linear regions, and with enough units it can approximate any continuous function on a bounded interval.  
→ PDF pp. 42–43 (book pp. 29–30) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**3.3 Multivariate inputs and outputs**  
More outputs share the same joints; more inputs turn the joints into lines or hyperplanes that divide input space into convex polygonal regions.  
→ PDF pp. 43–46 (book pp. 30–33) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**3.4 Shallow neural networks: general case**  
The general equation for a shallow network with any number of inputs, hidden units and outputs. The count of linear regions grows fast with input dimension.  
→ PDF pp. 46–49 (book pp. 33–36) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**3.5 Terminology**  
Vocabulary: layers, hidden units (neurons), pre-activations and activations, MLP, fully connected.  
→ PDF p. 49 (book p. 36) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**3.6 Summary**  
Recap, then notes on the history and on other activation functions (sigmoid, tanh, leaky ReLU, GELU, Swish and others).  
→ PDF pp. 49–53 (book pp. 36–40) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch4"></a>
## 4. Deep neural networks

*PDF pp. 54–68 (book pp. 41–55)*

Why depth helps: composing networks folds input space, so deep networks create far more linear regions per parameter than shallow ones.

**4.1 Composing neural networks**  
Feeding one shallow network into another repeats the second network's function on each piece of the first's output.  
→ PDF pp. 54–56 (book pp. 41–43) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**4.2 From composing networks to deep networks**  
Composition can be read as folding: the first network maps several input ranges onto the same output range, and the second network's function is applied to all of them at once. The composed network is a special case of a two-layer network.  
→ PDF pp. 56–58 (book pp. 43–45) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**4.3 Deep neural networks**  
The general two-hidden-layer network, and hyperparameters (depth and width) as choices about model capacity.  
→ PDF pp. 58–61 (book pp. 45–48) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**4.4 Matrix notation**  
Writing a deep network as alternating weight matrices, bias vectors and activations, layer by layer.  
→ PDF pp. 61–62 (book pp. 48–49) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**4.5 Shallow vs. deep neural networks**  
Shallow and deep networks can both approximate anything, but deep ones get many more regions per parameter, some functions need exponentially many shallow units, and deep networks handle large structured inputs better. Why they also train and generalize well is left open.  
→ PDF pp. 62–65 (book pp. 49–52) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**4.6 Summary**  
Recap of folding, depth efficiency and the open questions.  
→ PDF pp. 65–68 (book pp. 52–55) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch5"></a>
## 5. Loss functions

*PDF pp. 69–89 (book pp. 56–76)*

Where loss functions come from: the network predicts the parameters of a probability distribution over outputs, and training maximizes the likelihood of the data.

**5.1 Maximum likelihood**  
The model outputs distribution parameters; maximum likelihood picks parameters that make the observed outputs probable, and taking logs turns the product over examples into a sum.  
→ PDF pp. 69–72 (book pp. 56–59) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**5.2 Recipe for constructing loss functions**  
The recipe: choose a distribution suited to the output domain, have the network predict its parameters, minimize negative log-likelihood. Inference returns the most probable output.  
→ PDF pp. 72–73 (book pp. 59–60) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**5.3 Example 1: univariate regression**  
Assuming normally distributed outputs and predicting only the mean gives least squares. Predicting the variance too gives uncertainty estimates, and making the variance depend on the input gives heteroscedastic regression.  
→ PDF pp. 73–77 (book pp. 60–64) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**5.4 Example 2: binary classification**  
A Bernoulli output passed through a logistic sigmoid gives the binary cross-entropy loss.  
→ PDF pp. 77–79 (book pp. 64–66) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**5.5 Example 3: multiclass classification**  
A categorical distribution with a softmax gives the multiclass cross-entropy loss.  
→ PDF pp. 79–81 (book pp. 66–68) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**5.6 Multiple outputs**  
Several outputs are usually treated as independent, so their losses add. A table maps output types (circular, counts, rankings and others) to suitable distributions.  
→ PDF pp. 81–83 (book pp. 68–70) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**5.7 Cross-entropy loss**  
Cross-entropy is the KL divergence between the empirical data distribution and the model, minus a constant, so it is the same objective as negative log-likelihood.  
→ PDF pp. 83–85 (book pp. 70–72) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**5.8 Summary**  
Recap, then notes on robust losses, mixtures of Gaussians for multimodal outputs, and other distributions.  
→ PDF pp. 85–89 (book pp. 72–76) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch6"></a>
## 6. Fitting models

*PDF pp. 90–108 (book pp. 77–95)*

How parameters are actually found: gradient descent and the stochastic, momentum-based and adaptive refinements used in practice.

**6.1 Gradient descent**  
Gradient descent steps against the gradient. Linear regression has a convex loss with one minimum; the nonlinear Gabor model shows a loss surface with many.  
→ PDF pp. 90–95 (book pp. 77–82) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**6.2 Stochastic gradient descent**  
Local minima and saddle points trap plain gradient descent. Stochastic gradient descent uses random batches and epochs, so each step sees a slightly different loss surface.  
→ PDF pp. 95–98 (book pp. 82–85) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**6.3 Momentum**  
SGD's noise helps escape bad regions and is cheap per step. Momentum averages past gradients to smooth the path; Nesterov momentum measures the gradient after the momentum step.  
→ PDF pp. 98–101 (book pp. 85–88) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**6.4 Adam**  
Adam normalizes each parameter's step by a running estimate of its gradient magnitude, so steep and shallow directions move at similar rates. Bias corrections fix the early estimates.  
→ PDF pp. 101–104 (book pp. 88–91) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**6.5 Training algorithm hyperparameters**  
Learning rate, batch size, schedule and momentum are hyperparameters of training, usually tuned by trial.  
→ PDF p. 104 (book p. 91) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**6.6 Summary**  
Recap, then notes on convexity, line search, learning-rate schedules and other optimizers.  
→ PDF pp. 104–108 (book pp. 91–95) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch7"></a>
## 7. Gradients and initialization

*PDF pp. 109–127 (book pp. 96–114)*

Two problems specific to neural networks: computing gradients for every parameter efficiently, and initializing so that signals neither explode nor vanish.

**7.1 Problem definitions**  
The setup: total loss is a sum over examples, and training needs its derivative for every weight and bias at every step.  
→ PDF pp. 109–110 (book pp. 96–97) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**7.2 Computing derivatives**  
Backpropagation runs a forward pass storing activations, then a backward pass applying the chain rule layer by layer. It is a special case of reverse-mode algorithmic differentiation, which frameworks automate.  
→ PDF pp. 110–117 (book pp. 97–104) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**7.3 Parameter initialization**  
Backprop extends to any computational graph and works on batches as tensors. For initialization, the variance of activations and gradients should stay constant across layers; for ReLU this gives He initialization.  
→ PDF pp. 117–121 (book pp. 104–108) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**7.4 Example training code**  
When adjacent layers differ in width, averaging the two sizes is a compromise. A short PyTorch listing shows the whole training loop so far.  
→ PDF p. 121 (book p. 108) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**7.5 Summary**  
Recap, then notes on the history of backprop and on initialization schemes.  
→ PDF pp. 121–127 (book pp. 108–114) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch8"></a>
## 8. Measuring performance

*PDF pp. 128–147 (book pp. 115–134)*

How to measure and explain test error, from the classical bias-variance trade-off to double descent in over-parameterized models.

**8.1 Training a simple model**  
A network trained on the MNIST-1D toy dataset reaches zero training error but much higher test error.  
→ PDF pp. 128–130 (book pp. 115–117) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**8.2 Sources of error**  
Test error splits into noise (irreducible), bias (the model family can't represent the truth) and variance (the fit depends on which training sample you drew).  
→ PDF pp. 130–134 (book pp. 117–121) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**8.3 Reducing error**  
More data reduces variance; more capacity reduces bias but raises variance. Classically the best model sits at a trade-off point.  
→ PDF pp. 134–137 (book pp. 121–124) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**8.4 Double descent**  
Past the point where the model can memorize the training data, test error falls again: double descent. In this regime the question becomes why training picks smooth solutions among many that fit.  
→ PDF pp. 137–142 (book pp. 124–129) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**8.5 Choosing hyperparameters**  
Hyperparameters are tuned on a separate validation set, never the test set, usually by random or Bayesian search.  
→ PDF pp. 142–143 (book pp. 129–130) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**8.6 Summary**  
Recap, then notes including why high-dimensional spaces behave counterintuitively.  
→ PDF pp. 143–147 (book pp. 130–134) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch9"></a>
## 9. Regularization

*PDF pp. 148–171 (book pp. 135–158)*

Techniques that shrink the gap between training and test performance, from explicit penalty terms to the implicit biases of SGD and a long list of heuristics.

**9.1 Explicit regularization**  
Adding a penalty term to the loss, read as a prior over parameters; L2 regularization (weight decay) favors small weights and smoother functions.  
→ PDF pp. 148–151 (book pp. 135–138) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**9.2 Implicit regularization**  
Finite-step gradient descent behaves like continuous descent on a modified loss that penalizes steep gradients. SGD adds a term favoring places where batches agree, one reason larger learning rates and smaller batches can generalize better.  
→ PDF pp. 151–154 (book pp. 138–141) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**9.3 Heuristics to improve performance**  
Early stopping, ensembling and bagging, dropout, adding noise, Bayesian inference, transfer and multi-task learning, self-supervised pretraining and data augmentation, each explained by how it improves generalization.  
→ PDF pp. 154–164 (book pp. 141–151) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**9.4 Summary**  
The methods sorted by mechanism: smoother functions, more data, better initialization, or averaging. Notes on sharp versus flat minima.  
→ PDF pp. 164–171 (book pp. 151–158) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch10"></a>
## 10. Convolutional networks

*PDF pp. 172–197 (book pp. 159–184)*

Convolutional layers for grid data: weight sharing builds in translation equivariance, which cuts parameters and improves generalization.

**10.1 Invariance and equivariance**  
Images are high-dimensional, nearby pixels are related, and meaning shouldn't change under translation. Equivariance and invariance make the last point precise.  
→ PDF pp. 172–174 (book pp. 159–161) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**10.2 Convolutional networks for 1D inputs**  
1D convolution, padding, stride, kernel size and dilation; channels and growing receptive fields; on MNIST-1D a convolutional network beats a fully connected one with far fewer parameters.  
→ PDF pp. 174–181 (book pp. 161–168) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**10.3 Convolutional networks for 2D inputs**  
The same machinery in two dimensions, with kernels spanning all input channels.  
→ PDF pp. 181–183 (book pp. 168–170) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**10.4 Downsampling and upsampling**  
Downsampling (subsampling, max and mean pooling, strided convolution), upsampling (duplication, max-unpooling, transposed convolution) and 1×1 convolutions to change channel counts.  
→ PDF pp. 183–186 (book pp. 170–173) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**10.5 Applications**  
Image classification (AlexNet, VGG on ImageNet), object detection (YOLO) and semantic segmentation with an encoder–decoder network.  
→ PDF pp. 186–191 (book pp. 173–178) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**10.6 Summary**  
Recap, then notes on the history of CNNs and the steady ImageNet gains.  
→ PDF pp. 191–197 (book pp. 178–184) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch11"></a>
## 11. Residual networks

*PDF pp. 198–220 (book pp. 185–207)*

Residual connections make very deep networks trainable; batch normalization keeps their activations in check.

**11.1 Sequential processing**  
Simply stacking more layers made results worse. Shattered gradients, where small parameter changes alter the output unpredictably, are one explanation.  
→ PDF pp. 198–201 (book pp. 185–188) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**11.2 Residual connections and residual blocks**  
Each block adds a change to its input rather than replacing it, so the network unrolls into many paths of different lengths. Order of operations inside a block matters.  
→ PDF pp. 201–204 (book pp. 188–191) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**11.3 Exploding gradients in residual networks**  
In residual networks the variance of activations grows with each block at initialization, even with He initialization.  
→ PDF pp. 204–205 (book pp. 191–192) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**11.4 Batch normalization**  
Batch normalization rescales each activation using batch statistics, with learned offset and scale. It stabilizes forward signals, allows higher learning rates and adds a little regularizing noise.  
→ PDF pp. 205–207 (book pp. 192–194) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**11.5 Common residual architectures**  
ResNet blocks and bottlenecks, DenseNet's concatenation of earlier layers, and U-Nets and stacked hourglass networks for dense prediction.  
→ PDF pp. 207–210 (book pp. 194–197) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**11.6 Why do nets with residual connections perform so well?**  
Residual nets behave partly like ensembles of shallower paths, and their loss surfaces are smoother around minima.  
→ PDF pp. 210–213 (book pp. 197–200) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**11.7 Summary**  
Recap, then notes on other normalization schemes (layer, instance, group norm) and on why residual connections work.  
→ PDF pp. 213–220 (book pp. 200–207) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch12"></a>
## 12. Transformers

*PDF pp. 221–254 (book pp. 208–241)*

Transformers: self-attention lets every token weigh every other, with parameters shared across positions. Covers the architecture and its main uses in language and vision.

**12.1 Processing text data**  
Text is long, variable in length and ambiguous, so a network needs shared parameters and connections whose strength depends on the content.  
→ PDF pp. 221–222 (book pp. 208–209) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.2 Dot-product self-attention**  
Each output is a weighted sum of value vectors; the weights come from softmaxed dot products between queries and keys, all computed by shared linear maps. In matrix form this is one compact expression.  
→ PDF pp. 222–227 (book pp. 209–214) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.3 Extensions to dot-product self-attention**  
Position encodings break the permutation symmetry, scaling the dot products keeps softmax well behaved, and multiple heads attend in parallel.  
→ PDF pp. 227–230 (book pp. 214–217) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.4 Transformer layers**  
A transformer layer: multi-head attention and a per-token MLP, each wrapped in a residual connection, with LayerNorm.  
→ PDF pp. 230–232 (book pp. 217–219) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.5 Transformers for natural language processing**  
The NLP pipeline: sub-word tokenization (byte-pair encoding), learned embeddings, then a stack of layers in one of three forms: encoder, decoder or encoder-decoder.  
→ PDF pp. 232–233 (book pp. 219–220) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.6 Encoder model example: BERT**  
BERT as the encoder example: pretraining by predicting masked tokens, then fine-tuning for classification or tagging.  
→ PDF pp. 233–236 (book pp. 220–223) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.7 Decoder model example: GPT3**  
GPT-3 as the decoder example: next-token prediction with masked attention, autoregressive generation, and few-shot learning from prompts.  
→ PDF pp. 236–240 (book pp. 223–227) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.8 Encoder-decoder model example: machine translation**  
Machine translation as the encoder-decoder example, with cross-attention from target to source.  
→ PDF p. 240 (book p. 227) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.9 Transformers for long sequences**  
Attention cost grows quadratically with length; sparse and local interaction patterns cut the cost.  
→ PDF pp. 240–242 (book pp. 227–229) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.10 Transformers for images**  
ImageGPT models pixels autoregressively; ViT treats image patches as tokens; multi-scale transformers like SWIN reintroduce hierarchy.  
→ PDF pp. 242–246 (book pp. 229–233) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**12.11 Summary**  
Recap, then notes on RNNs as the predecessor and on efficient-attention variants.  
→ PDF pp. 246–254 (book pp. 233–241) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch13"></a>
## 13. Graph neural networks

*PDF pp. 255–283 (book pp. 242–270)*

Graph neural networks: layers that must be equivariant to node order, and the extra problems of huge or single graphs.

**13.1 What is a graph?**  
Graphs model roads, molecules, circuits and social networks; they can be directed, weighted, hierarchical and more.  
→ PDF pp. 255–258 (book pp. 242–245) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.2 Graph representation**  
A graph is stored as an adjacency matrix plus node and edge embeddings. Powers of the adjacency matrix count walks.  
→ PDF pp. 258–260 (book pp. 245–247) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.3 Graph neural networks, tasks, and loss functions**  
Node numbering is arbitrary, so a layer must give the same answer under any permutation of the nodes.  
→ PDF pp. 260–261 (book pp. 247–248) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.4 Tasks and loss functions**  
Graph-level, node-level and edge-prediction tasks, each with its loss.  
→ PDF pp. 261–263 (book pp. 248–250) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.5 Graph convolutional networks**  
A graph convolutional layer aggregates neighbors' embeddings (multiplying by the adjacency matrix plus identity) and shares weights across the graph.  
→ PDF pp. 263–266 (book pp. 250–253) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.6 Example: graph classification**  
Classifying molecules as toxic or not; batches are built by treating many graphs as one disconnected graph.  
→ PDF pp. 266–267 (book pp. 253–254) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.7 Inductive vs. transductive models**  
Inductive models learn a rule for new graphs; transductive models label the unlabeled nodes of one graph seen during training.  
→ PDF p. 267 (book p. 254) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.8 Transductive learning example: node classification**  
Node classification on one huge graph needs batching via neighborhood sampling or graph partitioning, because receptive fields grow with depth.  
→ PDF pp. 267–271 (book pp. 254–258) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.9 Layers for graph convolutional networks**  
Design choices inside a layer: treating the node differently from its neighbors, residual connections, mean or Kipf-normalized aggregation, max pooling, and graph attention.  
→ PDF pp. 271–275 (book pp. 258–262) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.10 Edge graphs**  
Turning edges into nodes lets the same machinery work on edge embeddings.  
→ PDF pp. 275–276 (book pp. 262–263) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**13.11 Summary**  
Recap, then notes on spectral methods, expressiveness and the Weisfeiler–Lehman test.  
→ PDF pp. 276–283 (book pp. 263–270) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch14"></a>
## 14. Unsupervised learning

*PDF pp. 284–289 (book pp. 271–276)*

A short map of unsupervised learning that frames the next four chapters.

**14.1 Taxonomy of unsupervised learning models**  
Models learned without labels; generative models can sample, probabilistic ones also assign likelihoods, latent-variable models map a simple latent space to data.  
→ PDF pp. 284–285 (book pp. 271–272) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**14.2 What makes a good generative model?**  
Desired properties: efficient sampling, high quality, coverage of the data, a well-behaved latent space and the ability to evaluate probability. No family has all of them.  
→ PDF pp. 285–287 (book pp. 272–274) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**14.3 Quantifying performance**  
Ways to score generative models: test likelihood, Inception score, FID, and manifold-based precision and recall.  
→ PDF pp. 287–289 (book pp. 274–276) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**14.4 Summary**  
Recap of the taxonomy and what each later chapter's model can do.  
→ PDF p. 289 (book p. 276) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch15"></a>
## 15. Generative Adversarial Networks

*PDF pp. 290–318 (book pp. 277–305)*

GANs generate samples by fooling a discriminator. Much of the chapter is about why training is unstable and how to fix it.

**15.1 Discrimination as a signal**  
A generator maps noise to samples and a discriminator learns to tell them from real data; the two play a minimax game. DCGAN made it work for images, but training is hard.  
→ PDF pp. 290–295 (book pp. 277–282) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**15.2 Improving stability**  
Mode dropping and collapse; the original loss gives vanishing gradients when the discriminator wins. The Wasserstein distance, from optimal transport, gives a smoother signal and a more stable loss.  
→ PDF pp. 295–301 (book pp. 282–288) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**15.3 Improving quality**  
Progressive growing, minibatch discrimination and truncation of the latent distribution improve image quality and diversity.  
→ PDF pp. 301–303 (book pp. 288–290) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**15.4 Conditional generation**  
Conditional GANs and auxiliary-classifier GANs generate samples with chosen attributes.  
→ PDF pp. 303–305 (book pp. 290–292) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**15.5 Image translation**  
InfoGAN discovers interpretable attributes on its own; Pix2Pix and CycleGAN translate images between styles, with and without paired examples.  
→ PDF pp. 305–310 (book pp. 292–297) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**15.6 StyleGAN**  
StyleGAN injects style vectors and noise at several scales, separating coarse and fine variation.  
→ PDF pp. 310–312 (book pp. 297–299) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**15.7 Summary**  
Recap, then notes on the large GAN literature and evaluation.  
→ PDF pp. 312–318 (book pp. 299–305) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch16"></a>
## 16. Normalizing flows

*PDF pp. 319–342 (book pp. 306–329)*

Normalizing flows transform a simple distribution through invertible layers, so they can both sample and compute exact likelihoods.

**16.1 1D Normalizing flows example**  
A 1D example: probability changes by the slope of the mapping, so an invertible function gives a density you can evaluate in either direction.  
→ PDF pp. 319–322 (book pp. 306–309) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**16.2 General case**  
In many dimensions the scaling factor is the Jacobian determinant. A deep flow is a stack of invertible layers trained by maximum likelihood.  
→ PDF pp. 322–324 (book pp. 309–311) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**16.3 Invertible network layers**  
Layers must be expressive, invertible and have cheap Jacobians. Linear, elementwise, coupling, autoregressive and inverse-autoregressive flows, then residual flows (iRevNet, iResNet).  
→ PDF pp. 324–332 (book pp. 311–319) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**16.4 Multi-scale flows**  
Multi-scale flows set some latent dimensions aside early to save computation.  
→ PDF pp. 332–333 (book pp. 319–320) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**16.5 Applications**  
Density modeling and image synthesis (GLOW), and using a flow to approximate another density model.  
→ PDF pp. 333–336 (book pp. 320–323) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**16.6 Summary**  
Recap, then notes and the open question of why flow samples trail GANs and diffusion.  
→ PDF pp. 336–342 (book pp. 323–329) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch17"></a>
## 17. Variational autoencoders

*PDF pp. 343–364 (book pp. 330–351)*

VAEs train a nonlinear latent-variable model by maximizing a lower bound on likelihood, using an encoder to approximate the posterior.

**17.1 Latent variable models**  
The data distribution is modeled by marginalizing over a hidden variable.  
→ PDF pp. 343–344 (book pp. 330–331) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.2 Nonlinear latent variable model**  
A mixture of Gaussians as the simple case; then a deep network maps a continuous latent to the data mean, and new samples come from ancestral sampling.  
→ PDF pp. 344–347 (book pp. 331–334) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.3 Training**  
The likelihood integral is intractable, so Jensen's inequality gives the evidence lower bound (ELBO).  
→ PDF pp. 347–350 (book pp. 334–337) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.4 ELBO properties**  
The bound is tight when the auxiliary distribution equals the posterior; it can be read as reconstruction quality minus distance to the prior.  
→ PDF pp. 350–352 (book pp. 337–339) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.5 Variational approximation**  
Choose a simple (Gaussian) auxiliary distribution and fit it to the true posterior.  
→ PDF p. 352 (book p. 339) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.6 The variational autoencoder**  
The VAE: an encoder predicts the approximate posterior for each example, and a decoder reconstructs the data from samples.  
→ PDF pp. 352–355 (book pp. 339–342) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.7 The reparameterization trick**  
The reparameterization trick moves randomness into an input so gradients flow through the sampling step.  
→ PDF pp. 355–356 (book pp. 342–343) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.8 Applications**  
Estimating sample probability by importance sampling, generation, resynthesis and disentangled latent spaces.  
→ PDF pp. 356–359 (book pp. 343–346) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**17.9 Summary**  
Recap, then notes on β-VAE, other variants and the link to expectation maximization.  
→ PDF pp. 359–364 (book pp. 346–351) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)


---

<a id="ch18"></a>
## 18. Diffusion models

*PDF pp. 365–388 (book pp. 352–375)*

Diffusion models add noise in many small steps and learn to undo them. The ELBO reduces to a simple noise-prediction loss.

**18.1 Overview**  
Like flows the latent has the data's size; like VAEs training uses a lower bound. The encoder is fixed noise addition.  
→ PDF pp. 365–366 (book pp. 352–353) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**18.2 Encoder (forward process)**  
The forward process blends data with Gaussian noise under a schedule. Closed-form diffusion kernels and conditional distributions make every step's distribution computable.  
→ PDF pp. 366–372 (book pp. 353–359) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**18.3 Decoder model (reverse process)**  
The decoder approximates each reverse step with a Gaussian whose mean a network predicts.  
→ PDF pp. 372–373 (book pp. 359–360) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**18.4 Training**  
The ELBO simplifies to a sum of KL terms between Gaussians, giving a least-squares loss and a simple training procedure.  
→ PDF pp. 373–377 (book pp. 360–364) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**18.5 Reparameterization of loss function**  
Reparameterizing so the network predicts the added noise gives the simplest, best-performing loss.  
→ PDF pp. 377–379 (book pp. 364–366) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**18.6 Implementation**  
Image diffusion with U-Nets, faster sampling (DDIM and others), classifier and classifier-free guidance, and cascaded text-to-image generation.  
→ PDF pp. 379–384 (book pp. 366–371) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

**18.7 Summary**  
Recap, then notes on score matching and related views.  
→ PDF pp. 384–388 (book pp. 371–375) in [the PDF](https://drive.google.com/file/d/1QAJf3zjp95eBhmwZb3UAlQKPG0iYWgw6/view)

