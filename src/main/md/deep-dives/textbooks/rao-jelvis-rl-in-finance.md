<a id="ch1"></a>
# Foundations of Reinforcement Learning with Applications in Finance

> Ashwin Rao and Tikhon Jelvis · CRC Press / Chapman & Hall, 2022 (authors’ free PDF) · [the PDF in Drive](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

Short appendix chapters (moment generating functions, portfolio theory, stochastic calculus, HJB, Black–Scholes, affine spaces, conjugate priors) and per-chapter key-takeaway sections are not broken out. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

A Stanford-course textbook that teaches reinforcement learning from Markov processes up, with Python implementations built on careful abstractions and with finance as the running application area. After an overview and a chapter on code design, Module I covers Markov processes, MRPs and MDPs, dynamic programming, and function approximation with approximate DP. Module II casts financial problems as MDPs: utility theory, Merton-style asset allocation, derivatives pricing and hedging (including American options and incomplete markets), and order-book execution and market-making. Module III presents RL algorithms: MC and TD prediction and control, batch methods (experience replay, DQN, LSPI, gradient TD) and policy gradients. Module IV covers bandits, blending learning with planning (MCTS) and real-world considerations.

**Contents**

1. [1. Overview](ch1): What the book covers and the MDP framework.
2. [2. Programming and Design](ch2): Python code design for the book’s library.
3. [3. Markov Processes](ch3): Markov processes and reward processes.
4. [4. Markov Decision Processes](ch4): Markov decision processes.
5. [5. Dynamic Programming Algorithms](ch5): Dynamic programming.
6. [6. Function Approximation and Approximate Dynamic Programming](ch6): Function approximation and approximate DP.
7. [7. Utility Theory](ch7): Utility and risk aversion.
8. [8. Dynamic Asset-Allocation and Consumption](ch8): Asset allocation and consumption over time.
9. [9. Derivatives Pricing and Hedging](ch9): Pricing and hedging derivatives.
10. [10. Order-Book Trading Algorithms](ch10): Trading with limit order books.
11. [11. Monte-Carlo and Temporal-Difference for Prediction](ch11): Model-free prediction.
12. [12. Monte-Carlo and Temporal-Difference for Control](ch12): Model-free control.
13. [13. Batch RL, Experience-Replay, DQN, LSPI, Gradient TD](ch13): Batch and stable RL methods.
14. [14. Policy Gradient Algorithms](ch14): Policy gradient methods.
15. [15. Multi-Armed Bandits: Exploration versus Exploitation](ch15): Bandits.
16. [16. Blending Learning and Planning](ch16): Combining models and learning.
17. [17. Summary and Real-World Considerations](ch17): Lessons and practice.


---

## 1. Overview

*PDF pp. 17–34*

What the book covers and the MDP framework.

**Learning Reinforcement Learning**  
Approach to learning RL.  
*Terms:* learning RL  
→ PDF p. 17 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**What You Will Learn from This Book**  
Topics.  
*Terms:* contents  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Expected Background to Read This Book**  
Prerequisites.  
*Terms:* prerequisites  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Decluttering the Jargon Linked to Reinforcement Learning**  
Sorting out RL/DP/ML jargon.  
*Terms:* terminology  
→ PDF pp. 20–21 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Introduction to the Markov Decision Process (MDP) Framework**  
MDP framework.  
*Terms:* MDP framework  
→ PDF pp. 22–24 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Real-World Problems That Fit the MDP Framework**  
Real-world MDPs.  
*Terms:* applications  
→ PDF p. 25 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**The Inherent Difficulty in Solving MDPs**  
Why MDPs are hard.  
*Terms:* curse of dimensionality  
→ PDF pp. 25–26 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Value Function, Bellman Equations, Dynamic Programming and RL**  
Value functions, Bellman equations, DP and RL.  
*Terms:* Bellman equations  
→ PDF pp. 27–28 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Outline of Chapters**  
Chapter outline.  
*Terms:* outline  
→ PDF pp. 29–34 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch2"></a>
## 2. Programming and Design

*PDF pp. 35–58*

Python code design for the book’s library.

**Code Design**  
Design principles.  
*Terms:* code design  
→ PDF p. 35 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Environment Setup**  
Setup.  
*Terms:* environment  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Classes and Interfaces**  
Distribution interfaces, dataclasses, type checking, generics.  
*Terms:* Distribution, abstract classes, type hints  
→ PDF pp. 37–47 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Abstracting over Computation**  
First-class functions and iterative algorithms.  
*Terms:* higher-order functions, iterate, converge  
→ PDF pp. 48–53 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch3"></a>
## 3. Markov Processes

*PDF pp. 59–92*

Markov processes and reward processes.

**The Concept of State in a Process**  
State.  
*Terms:* state  
→ PDF p. 59 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Understanding Markov Property from Stock Price Examples**  
Markov property via stock prices.  
*Terms:* Markov property  
→ PDF pp. 59–65 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Formal Definitions for Markov Processes**  
Definitions.  
*Terms:* Markov process  
→ PDF pp. 66–69 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Stock Price Examples Modeled as Markov Processes**  
Stock price models.  
*Terms:* random walk, mean reversion  
→ PDF p. 70 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Finite Markov Processes**  
Finite MPs.  
*Terms:* finite Markov process  
→ PDF pp. 71–72 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Simple Inventory Example**  
Inventory example.  
*Terms:* inventory example  
→ PDF pp. 73–75 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Stationary Distribution of a Markov Process**  
Stationary distributions.  
*Terms:* stationary distribution  
→ PDF pp. 76–78 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Formalism of Markov Reward Processes**  
MRPs.  
*Terms:* Markov reward process  
→ PDF pp. 79–81 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Simple Inventory Example as a Markov Reward Process**  
Inventory as MRP.  
*Terms:* inventory MRP  
→ PDF pp. 82–83 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Finite Markov Reward Processes**  
Finite MRPs.  
*Terms:* finite MRP  
→ PDF p. 84 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Simple Inventory Example as a Finite Markov Reward Process**  
Inventory as finite MRP.  
*Terms:* inventory  
→ PDF pp. 85–87 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Value Function of a Markov Reward Process**  
MRP value functions.  
*Terms:* value function, Bellman equation  
→ PDF pp. 88–89 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch4"></a>
## 4. Markov Decision Processes

*PDF pp. 93–122*

Markov decision processes.

**Simple Inventory Example: How Much to Order?**  
Inventory ordering decision.  
*Terms:* inventory  
→ PDF p. 93 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**The Difficulty of Sequential Decisioning Under Uncertainty**  
Difficulty of sequential decisions.  
*Terms:* sequential decisions  
→ PDF p. 94 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Formal Definition of a Markov Decision Process**  
MDP definition.  
*Terms:* MDP  
→ PDF pp. 95–96 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Policy**  
Policies.  
*Terms:* policy  
→ PDF pp. 97–99 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**[Markov Decision Process, Policy] := Markov Reward Process**  
MDP plus policy gives an MRP.  
*Terms:* MRP from MDP  
→ PDF pp. 100–101 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Simple Inventory Example with Unlimited Capacity (Infinite State/Action Space)**  
Infinite inventory example.  
*Terms:* infinite state space  
→ PDF p. 102 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Finite Markov Decision Processes**  
Finite MDPs.  
*Terms:* finite MDP  
→ PDF pp. 103–105 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Simple Inventory Example as a Finite Markov Decision Process**  
Inventory as finite MDP.  
*Terms:* inventory MDP  
→ PDF pp. 106–108 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**MDP Value Function for a Fixed Policy**  
Policy value functions.  
*Terms:* Bellman expectation equation  
→ PDF pp. 109–111 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Optimal Value Function and Optimal Policies**  
Optimal values and policies.  
*Terms:* optimal policy, Bellman optimality  
→ PDF pp. 112–115 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Variants and Extensions of MDPs**  
Variants.  
*Terms:* POMDP, variants  
→ PDF pp. 116–121 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch5"></a>
## 5. Dynamic Programming Algorithms

*PDF pp. 123–160*

Dynamic programming.

**Planning versus Learning**  
Planning vs. learning.  
*Terms:* planning  
→ PDF p. 123 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Usage of the Term Dynamic Programming**  
Meaning of DP.  
*Terms:* DP  
→ PDF pp. 123–124 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Fixed-Point Theory**  
Fixed-point theory and contractions.  
*Terms:* Banach fixed point  
→ PDF pp. 125–128 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Bellman Policy Operator and Policy Evaluation Algorithm**  
Policy evaluation.  
*Terms:* policy evaluation  
→ PDF pp. 129–131 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Greedy Policy**  
Greedy policy.  
*Terms:* greedy policy  
→ PDF p. 132 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Policy Improvement**  
Policy improvement.  
*Terms:* policy improvement theorem  
→ PDF pp. 133–135 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Policy Iteration Algorithm**  
Policy iteration.  
*Terms:* policy iteration  
→ PDF pp. 136–137 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Bellman Optimality Operator and Value Iteration Algorithm**  
Value iteration.  
*Terms:* value iteration  
→ PDF pp. 138–140 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Optimal Policy from Optimal Value Function**  
Extracting policies.  
*Terms:* optimal policy  
→ PDF pp. 141–142 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Revisiting the Simple Inventory Example**  
Inventory revisited.  
*Terms:* example  
→ PDF p. 143 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Generalized Policy Iteration**  
GPI.  
*Terms:* GPI  
→ PDF pp. 144–146 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Asynchronous Dynamic Programming**  
Asynchronous DP.  
*Terms:* asynchronous DP  
→ PDF pp. 147–148 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Finite-Horizon Dynamic Programming: Backward Induction**  
Backward induction.  
*Terms:* backward induction  
→ PDF pp. 149–153 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Dynamic Pricing for End-of-Life/End-of-Season of a Product**  
Dynamic pricing example.  
*Terms:* dynamic pricing  
→ PDF pp. 154–157 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Generalization to Non-Tabular Algorithms**  
Toward non-tabular.  
*Terms:* generalization  
→ PDF p. 158 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch6"></a>
## 6. Function Approximation and Approximate Dynamic Programming

*PDF pp. 161–196*

Function approximation and approximate DP.

**Function Approximation**  
FunctionApprox interface.  
*Terms:* function approximation  
→ PDF pp. 162–165 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Linear Function Approximation**  
Linear approximation.  
*Terms:* linear regression  
→ PDF pp. 166–171 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Neural Network Function Approximation**  
Neural networks.  
*Terms:* deep neural network  
→ PDF pp. 172–182 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Tabular as a Form of FunctionApprox**  
Tabular as a special case.  
*Terms:* tabular  
→ PDF pp. 183–185 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Approximate Policy Evaluation**  
Approximate policy evaluation.  
*Terms:* approximate policy evaluation  
→ PDF pp. 186–187 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Approximate Value Iteration**  
Approximate value iteration.  
*Terms:* approximate value iteration  
→ PDF p. 188 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Finite-Horizon Approximate Policy Evaluation**  
Finite-horizon evaluation.  
*Terms:* finite horizon  
→ PDF pp. 188–189 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Finite-Horizon Approximate Value Iteration**  
Finite-horizon VI.  
*Terms:* backward induction  
→ PDF p. 190 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Finite-Horizon Approximate Q-Value Iteration**  
Finite-horizon Q-VI.  
*Terms:* Q-value iteration  
→ PDF pp. 190–191 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**How to Construct the Non-Terminal States Distribution**  
Sampling non-terminal states.  
*Terms:* state distribution  
→ PDF p. 192 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch7"></a>
## 7. Utility Theory

*PDF pp. 197–208*

Utility and risk aversion.

**Introduction to the Concept of Utility**  
Utility concept.  
*Terms:* utility  
→ PDF p. 197 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**A Simple Financial Example**  
Example.  
*Terms:* example  
→ PDF p. 198 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**The Shape of the Utility function**  
Concavity and risk aversion.  
*Terms:* concave utility  
→ PDF pp. 199–200 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Calculating the Risk-Premium**  
Risk premium.  
*Terms:* risk premium, certainty equivalent  
→ PDF pp. 201–202 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Constant Absolute Risk-Aversion (CARA)**  
CARA.  
*Terms:* CARA, exponential utility  
→ PDF p. 203 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**A Portfolio Application of CARA**  
CARA portfolio.  
*Terms:* portfolio  
→ PDF p. 204 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Constant Relative Risk-Aversion (CRRA)**  
CRRA.  
*Terms:* CRRA, power utility  
→ PDF p. 205 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**A Portfolio Application of CRRA**  
CRRA portfolio.  
*Terms:* portfolio  
→ PDF pp. 206–207 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch8"></a>
## 8. Dynamic Asset-Allocation and Consumption

*PDF pp. 209–232*

Asset allocation and consumption over time.

**Optimization of Personal Finance**  
Personal finance as optimization.  
*Terms:* consumption-investment  
→ PDF pp. 209–210 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Merton's Portfolio Problem and Solution**  
Merton’s problem and solution.  
*Terms:* Merton portfolio problem, HJB  
→ PDF pp. 211–215 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Developing Intuition for the Solution to Merton's Portfolio Problem**  
Intuition.  
*Terms:* intuition  
→ PDF pp. 216–218 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**A Discrete-Time Asset-Allocation Example**  
Discrete-time example as MDP.  
*Terms:* discrete-time asset allocation, ADP  
→ PDF pp. 219–222 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Porting to Real-World**  
Real-world porting.  
*Terms:* real-world  
→ PDF pp. 223–229 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch9"></a>
## 9. Derivatives Pricing and Hedging

*PDF pp. 233–268*

Pricing and hedging derivatives.

**A Brief Introduction to Derivatives**  
Derivatives basics.  
*Terms:* derivatives  
→ PDF pp. 233–235 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Notation for the Single-Period Simple Setting**  
Single-period notation.  
*Terms:* notation  
→ PDF p. 236 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Portfolios, Arbitrage and Risk-Neutral Probability Measure**  
Arbitrage and risk-neutral measure.  
*Terms:* arbitrage, risk-neutral probability  
→ PDF pp. 237–238 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**First Fundamental Theorem of Asset Pricing (1st FTAP)**  
1st FTAP.  
*Terms:* first fundamental theorem  
→ PDF p. 239 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Second Fundamental Theorem of Asset Pricing (2nd FTAP)**  
2nd FTAP.  
*Terms:* second fundamental theorem, completeness  
→ PDF pp. 240–241 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Derivatives Pricing in Single-Period Setting**  
Single-period pricing.  
*Terms:* pricing  
→ PDF pp. 242–253 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Derivatives Pricing in Multi-Period/Continuous-Time**  
Multi-period and continuous time.  
*Terms:* binomial tree, Black-Scholes  
→ PDF pp. 254–255 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Optimal Exercise of American Options Cast as a Finite MDP**  
American options as finite MDPs.  
*Terms:* American options  
→ PDF pp. 256–262 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Generalizing to Optimal-Stopping Problems**  
Optimal stopping.  
*Terms:* optimal stopping  
→ PDF pp. 263–264 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Pricing/Hedging in an Incomplete Market Cast as an MDP**  
Incomplete-market pricing as an MDP.  
*Terms:* incomplete markets, utility indifference  
→ PDF pp. 265–267 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch10"></a>
## 10. Order-Book Trading Algorithms

*PDF pp. 269–304*

Trading with limit order books.

**Basics of Order Book and Price Impact**  
Order books and price impact.  
*Terms:* order book, price impact  
→ PDF pp. 270–277 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Optimal Execution of a Market Order**  
Optimal execution (Bertsimas–Lo).  
*Terms:* optimal execution  
→ PDF pp. 278–290 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Optimal Market-Making**  
Optimal market-making (Avellaneda–Stoikov).  
*Terms:* market making  
→ PDF pp. 291–301 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch11"></a>
## 11. Monte-Carlo and Temporal-Difference for Prediction

*PDF pp. 305–342*

Model-free prediction.

**Overview of the Reinforcement Learning Approach**  
RL approach.  
*Terms:* RL  
→ PDF pp. 305–306 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**RL for Prediction**  
Prediction problem.  
*Terms:* prediction  
→ PDF p. 307 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Monte-Carlo (MC) Prediction**  
MC prediction.  
*Terms:* Monte Carlo  
→ PDF pp. 308–314 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Temporal-Difference (TD) Prediction**  
TD prediction.  
*Terms:* TD(0)  
→ PDF pp. 315–318 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**TD versus MC**  
TD vs. MC.  
*Terms:* bias-variance  
→ PDF pp. 319–330 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**TD(λ) Prediction**  
TD(λ).  
*Terms:* TD(λ), eligibility traces  
→ PDF pp. 331–340 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch12"></a>
## 12. Monte-Carlo and Temporal-Difference for Control

*PDF pp. 343–378*

Model-free control.

**Refresher on Generalized Policy Iteration (GPI)**  
GPI refresher.  
*Terms:* GPI  
→ PDF p. 343 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**GPI with Evaluation as Monte-Carlo**  
MC evaluation in GPI.  
*Terms:* MC control  
→ PDF pp. 344–346 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**GLIE Monte-Carlo Control**  
GLIE MC control.  
*Terms:* GLIE  
→ PDF pp. 347–352 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**SARSA**  
SARSA.  
*Terms:* SARSA  
→ PDF pp. 353–358 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**SARSA(λ)**  
SARSA(λ).  
*Terms:* SARSA(λ)  
→ PDF p. 359 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Off-Policy Control**  
Off-policy control and Q-learning.  
*Terms:* Q-learning, importance sampling  
→ PDF pp. 360–372 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Conceptual Linkage between DP and TD Algorithms**  
DP–TD links.  
*Terms:* DP and TD  
→ PDF pp. 373–374 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Convergence of RL Algorithms**  
Convergence.  
*Terms:* convergence  
→ PDF pp. 375–376 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch13"></a>
## 13. Batch RL, Experience-Replay, DQN, LSPI, Gradient TD

*PDF pp. 379–412*

Batch and stable RL methods.

**Batch RL and Experience-Replay**  
Batch RL and experience replay.  
*Terms:* batch RL, experience replay  
→ PDF pp. 380–382 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**A Generic Implementation of Experience-Replay**  
Generic replay.  
*Terms:* replay buffer  
→ PDF p. 383 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Least-Squares RL Prediction**  
Least-squares prediction (LSTD).  
*Terms:* LSTD  
→ PDF pp. 384–389 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Q-Learning with Experience-Replay**  
Q-learning with replay and DQN.  
*Terms:* DQN  
→ PDF pp. 390–392 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Least-Squares Policy Iteration (LSPI)**  
LSPI.  
*Terms:* LSPI  
→ PDF pp. 393–399 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**RL for Optimal Exercise of American Options**  
Optimal exercise of American options.  
*Terms:* American options  
→ PDF pp. 400–402 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Value Function Geometry**  
Value function geometry.  
*Terms:* Bellman error, projected Bellman error  
→ PDF pp. 403–408 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Gradient Temporal-Difference (Gradient TD)**  
Gradient TD.  
*Terms:* gradient TD  
→ PDF p. 409 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch14"></a>
## 14. Policy Gradient Algorithms

*PDF pp. 413–444*

Policy gradient methods.

**Advantages and Disadvantages of Policy Gradient Algorithms**  
Pros and cons.  
*Terms:* policy gradient  
→ PDF p. 414 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Policy Gradient Theorem**  
Policy gradient theorem.  
*Terms:* policy gradient theorem  
→ PDF pp. 415–418 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Score Function for Canonical Policy Functions**  
Score functions for softmax and Gaussian policies.  
*Terms:* score function  
→ PDF p. 419 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**REINFORCE Algorithm (Monte-Carlo Policy Gradient)**  
REINFORCE.  
*Terms:* REINFORCE  
→ PDF pp. 420–422 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Optimal Asset Allocation (Revisited)**  
Asset allocation revisited.  
*Terms:* asset allocation  
→ PDF pp. 423–427 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Actor-Critic and Variance Reduction**  
Actor–critic and variance reduction.  
*Terms:* actor-critic, baseline  
→ PDF pp. 428–432 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Overcoming Bias with Compatible Function Approximation**  
Compatible function approximation.  
*Terms:* compatible function approximation  
→ PDF pp. 433–435 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Policy Gradient Methods in Practice**  
Practical methods.  
*Terms:* natural gradient, PPO  
→ PDF pp. 436–438 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Evolutionary Strategies**  
Evolutionary strategies.  
*Terms:* evolution strategies  
→ PDF pp. 439–440 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch15"></a>
## 15. Multi-Armed Bandits: Exploration versus Exploitation

*PDF pp. 445–472*

Bandits.

**Introduction to the Multi-Armed Bandit Problem**  
Problem statement.  
*Terms:* multi-armed bandit  
→ PDF pp. 445–448 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Simple Algorithms**  
Simple algorithms (ε-greedy).  
*Terms:* epsilon-greedy  
→ PDF pp. 449–451 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Lower Bound**  
Lai–Robbins lower bound.  
*Terms:* regret lower bound  
→ PDF p. 452 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Upper Confidence Bound Algorithms**  
UCB.  
*Terms:* UCB  
→ PDF pp. 453–457 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Probability Matching**  
Thompson sampling.  
*Terms:* Thompson sampling  
→ PDF pp. 458–461 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Gradient Bandits**  
Gradient bandits.  
*Terms:* gradient bandit  
→ PDF pp. 462–464 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Horse Race**  
Comparing algorithms.  
*Terms:* comparison  
→ PDF pp. 465–467 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Information State Space MDP**  
Information-state MDP.  
*Terms:* Gittins, information state  
→ PDF pp. 468–469 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Extending to Contextual Bandits and RL Control**  
Contextual bandits.  
*Terms:* contextual bandits  
→ PDF pp. 470–471 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch16"></a>
## 16. Blending Learning and Planning

*PDF pp. 473–484*

Combining models and learning.

**Planning versus Learning**  
Planning vs. learning.  
*Terms:* model-based RL  
→ PDF pp. 473–476 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Decision-Time Planning**  
Decision-time planning.  
*Terms:* decision-time planning  
→ PDF p. 477 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Monte-Carlo Tree-Search (MCTS)**  
MCTS.  
*Terms:* MCTS  
→ PDF p. 478 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

**Adaptive Multi-Stage Sampling**  
Adaptive multi-stage sampling.  
*Terms:* AMS  
→ PDF pp. 479–482 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)


---

<a id="ch17"></a>
## 17. Summary and Real-World Considerations

*PDF pp. 485–494*

Lessons and practice.

**RL in the Real-World**  
RL in the real world.  
*Terms:* real-world RL, practical considerations  
→ PDF pp. 489–494 in [the PDF](https://drive.google.com/file/d/1nUB9DgHDI5pAGhUdNHuvAWWpsykO53BV/view)

