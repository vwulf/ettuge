<a id="ch1"></a>
# Reinforcement Learning: An Introduction (2nd edition)

> Richard S. Sutton and Andrew G. Barto · MIT Press, 2018 (authors’ free PDF, 2020 printing) · [the PDF in Drive](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

PDF page = printed page + 22. Chapter summaries and bibliographical remarks are not broken out; the references and index are not broken down. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The standard introduction to reinforcement learning: an agent learning by trial and error to maximize reward. Part I treats the tabular case exactly: bandits and exploration, finite MDPs and Bellman equations, dynamic programming, Monte Carlo methods, TD learning (Sarsa, Q-learning, Expected Sarsa, double learning), n-step bootstrapping and planning with learned models (Dyna, prioritized sweeping, rollouts, MCTS). Part II brings in function approximation: on-policy prediction and control (including neural networks, LSTD and average reward), the difficulties of off-policy learning and the deadly triad, eligibility traces with true online TD(λ), and policy-gradient and actor–critic methods. Part III connects RL to animal learning psychology and to dopamine and neuroscience, presents case studies from TD-Gammon to AlphaGo, and closes with open frontiers.

**Contents**

1. [1 Introduction](ch1): What reinforcement learning is and where it came from.
2. [2 Multi-armed Bandits](ch2): Exploration versus exploitation in the single-state setting.
3. [3 Finite Markov Decision Processes](ch3): The formal problem: finite Markov decision processes.
4. [4 Dynamic Programming](ch4): Computing optimal policies when the model is known.
5. [5 Monte Carlo Methods](ch5): Learning from complete sampled episodes.
6. [6 Temporal-Difference Learning](ch6): Bootstrapping from estimates: temporal-difference learning.
7. [7 n-step Bootstrapping](ch7): Methods between one-step TD and Monte Carlo.
8. [8 Planning and Learning with Tabular Methods](ch8): Integrating planning with learning in tabular methods.
9. [9 On-policy Prediction with Approximation](ch9): Function approximation for value prediction.
10. [10 On-policy Control with Approximation](ch10): Control with function approximation.
11. [11 Off-policy Methods with Approximation](ch11): Why off-policy learning with approximation is hard.
12. [12 Eligibility Traces](ch12): Eligibility traces and their modern forms.
13. [13 Policy Gradient Methods](ch13): Learning parameterized policies directly.
14. [14 Psychology](ch14): Links between RL and animal learning psychology.
15. [15 Neuroscience](ch15): Links between RL and neuroscience, especially dopamine.
16. [16 Applications and Case Studies](ch16): Landmark applications.
17. [17 Frontiers](ch17): Open problems and the future.


---

## 1 Introduction

*PDF pp. 23–43*

What reinforcement learning is and where it came from.

**Reinforcement Learning**  
Learning from interaction to maximize a reward signal.  
*Terms:* reinforcement learning  
→ PDF pp. 23–25 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Examples**  
Examples from games, control and biology.  
*Terms:* examples  
→ PDF pp. 26–27 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Elements of Reinforcement Learning**  
Policy, reward, value function and model.  
*Terms:* policy, reward signal, value function, model  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Limitations and Scope**  
Scope, and RL vs. evolutionary methods.  
*Terms:* scope, evolutionary methods  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**An Extended Example: Tic-Tac-Toe**  
Learning tic-tac-toe with a value table.  
*Terms:* tic-tac-toe, temporal difference  
→ PDF pp. 30–34 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Early History of Reinforcement Learning**  
The optimal-control, trial-and-error and temporal-difference threads of history.  
*Terms:* history, optimal control, Bellman, law of effect  
→ PDF pp. 35–43 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch2"></a>
## 2 Multi-armed Bandits

*PDF pp. 47–68*

Exploration versus exploitation in the single-state setting.

**A k-armed Bandit Problem**  
The k-armed bandit.  
*Terms:* k-armed bandit  
→ PDF pp. 47–48 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Action-value Methods**  
Sample-average action values and ε-greedy.  
*Terms:* action values, epsilon-greedy  
→ PDF p. 49 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**The 10-armed Testbed**  
The 10-armed testbed.  
*Terms:* 10-armed testbed  
→ PDF pp. 50–51 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Incremental Implementation**  
Incremental updates.  
*Terms:* incremental update  
→ PDF pp. 52–53 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Tracking a Nonstationary Problem**  
Constant step sizes for nonstationary problems.  
*Terms:* nonstationary, step size  
→ PDF pp. 54–55 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Optimistic Initial Values**  
Optimistic initial values.  
*Terms:* optimistic initialization  
→ PDF p. 56 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Upper-Confidence-Bound Action Selection**  
UCB action selection.  
*Terms:* upper confidence bound  
→ PDF pp. 57–58 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Gradient Bandit Algorithms**  
Gradient bandits with a baseline.  
*Terms:* gradient bandit, softmax, baseline  
→ PDF pp. 59–62 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Associative Search (Contextual Bandits)**  
Contextual bandits.  
*Terms:* contextual bandits  
→ PDF p. 63 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch3"></a>
## 3 Finite Markov Decision Processes

*PDF pp. 69–94*

The formal problem: finite Markov decision processes.

**The Agent–Environment Interface**  
Agent, environment, states, actions, rewards and dynamics.  
*Terms:* agent-environment interface, MDP dynamics  
→ PDF pp. 69–74 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Goals and Rewards**  
The reward hypothesis.  
*Terms:* reward hypothesis  
→ PDF p. 75 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Returns and Episodes**  
Returns, discounting and episodes.  
*Terms:* return, discounting, episodes  
→ PDF pp. 76–78 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Unified Notation for Episodic and Continuing Tasks**  
One notation for episodic and continuing tasks.  
*Terms:* episodic, continuing, absorbing state  
→ PDF p. 79 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Policies and Value Functions**  
Policies, value functions and Bellman equations.  
*Terms:* policy, value function, Bellman equation, backup diagram  
→ PDF pp. 80–83 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Optimal Policies and Optimal Value Functions**  
Optimal policies and Bellman optimality.  
*Terms:* optimal value function, Bellman optimality equation  
→ PDF pp. 84–88 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Optimality and Approximation**  
Why exact optimality is out of reach.  
*Terms:* approximation  
→ PDF p. 89 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch4"></a>
## 4 Dynamic Programming

*PDF pp. 95–112*

Computing optimal policies when the model is known.

**Policy Evaluation (Prediction)**  
Iterative policy evaluation.  
*Terms:* policy evaluation  
→ PDF pp. 96–97 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Policy Improvement**  
The policy improvement theorem.  
*Terms:* policy improvement theorem  
→ PDF pp. 98–101 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Policy Iteration**  
Policy iteration.  
*Terms:* policy iteration  
→ PDF pp. 102–103 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Value Iteration**  
Value iteration.  
*Terms:* value iteration  
→ PDF pp. 104–106 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Asynchronous Dynamic Programming**  
Asynchronous DP.  
*Terms:* asynchronous DP  
→ PDF p. 107 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Generalized Policy Iteration**  
Generalized policy iteration.  
*Terms:* generalized policy iteration  
→ PDF p. 108 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Efficiency of Dynamic Programming**  
Efficiency of DP.  
*Terms:* efficiency, curse of dimensionality  
→ PDF p. 109 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch5"></a>
## 5 Monte Carlo Methods

*PDF pp. 113–140*

Learning from complete sampled episodes.

**Monte Carlo Prediction**  
First-visit and every-visit prediction.  
*Terms:* Monte Carlo prediction  
→ PDF pp. 114–117 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Monte Carlo Estimation of Action Values**  
Estimating action values.  
*Terms:* action values  
→ PDF p. 118 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Monte Carlo Control**  
Control with exploring starts.  
*Terms:* exploring starts  
→ PDF pp. 119–121 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Monte Carlo Control without Exploring Starts**  
ε-soft on-policy control.  
*Terms:* epsilon-soft, on-policy  
→ PDF pp. 122–124 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Off-policy Prediction via Importance Sampling**  
Off-policy prediction with ordinary and weighted importance sampling.  
*Terms:* importance sampling, weighted importance sampling  
→ PDF pp. 125–130 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Incremental Implementation**  
Incremental implementation.  
*Terms:* incremental  
→ PDF p. 131 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Off-policy Monte Carlo Control**  
Off-policy MC control.  
*Terms:* off-policy control  
→ PDF pp. 132–133 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Discounting-aware Importance Sampling**  
Discounting-aware importance sampling.  
*Terms:* discounting-aware  
→ PDF pp. 134–135 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Per-decision Importance Sampling**  
Per-decision importance sampling.  
*Terms:* per-decision importance sampling  
→ PDF p. 136 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch6"></a>
## 6 Temporal-Difference Learning

*PDF pp. 141–162*

Bootstrapping from estimates: temporal-difference learning.

**TD Prediction**  
TD(0) prediction and the TD error.  
*Terms:* TD(0), TD error  
→ PDF pp. 141–145 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Advantages of TD Prediction Methods**  
Why TD often beats MC.  
*Terms:* bootstrapping  
→ PDF pp. 146–147 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Optimality of TD(0)**  
Batch TD and certainty equivalence.  
*Terms:* batch updating, certainty equivalence  
→ PDF pp. 148–150 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Sarsa: On-policy TD Control**  
Sarsa.  
*Terms:* Sarsa  
→ PDF pp. 151–152 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Q-learning: Off-policy TD Control**  
Q-learning.  
*Terms:* Q-learning  
→ PDF pp. 153–154 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Expected Sarsa**  
Expected Sarsa.  
*Terms:* Expected Sarsa  
→ PDF p. 155 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Maximization Bias and Double Learning**  
Maximization bias and double Q-learning.  
*Terms:* maximization bias, double learning  
→ PDF pp. 156–157 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Games, Afterstates, and Other Special Cases**  
Afterstates.  
*Terms:* afterstates  
→ PDF pp. 158–159 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch7"></a>
## 7 n-step Bootstrapping

*PDF pp. 163–180*

Methods between one-step TD and Monte Carlo.

**n-step TD Prediction**  
n-step TD prediction.  
*Terms:* n-step TD  
→ PDF pp. 164–166 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**n-step Sarsa**  
n-step Sarsa.  
*Terms:* n-step Sarsa  
→ PDF pp. 167–169 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**n-step Off-policy Learning**  
Off-policy n-step learning with importance sampling.  
*Terms:* off-policy n-step  
→ PDF pp. 170–171 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Per-decision Methods with Control Variates**  
Control variates.  
*Terms:* control variates  
→ PDF pp. 172–173 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Off-policy Learning Without Importance Sampling: The n-step Tree Backup Algorithm**  
Tree backup without importance sampling.  
*Terms:* tree backup  
→ PDF pp. 174–175 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**A Unifying Algorithm: n-step Q(σ)**  
n-step Q(σ) unifying sampling and expectation.  
*Terms:* Q(sigma)  
→ PDF pp. 176–178 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch8"></a>
## 8 Planning and Learning with Tabular Methods

*PDF pp. 181–213*

Integrating planning with learning in tabular methods.

**Models and Planning**  
Models and planning.  
*Terms:* model-based, planning  
→ PDF pp. 181–182 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Dyna: Integrated Planning, Acting, and Learning**  
Dyna-Q.  
*Terms:* Dyna-Q  
→ PDF pp. 183–187 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**When the Model Is Wrong**  
Coping with wrong models (Dyna-Q+).  
*Terms:* model error, exploration bonus  
→ PDF pp. 188–189 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Prioritized Sweeping**  
Prioritized sweeping.  
*Terms:* prioritized sweeping  
→ PDF pp. 190–193 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Expected vs. Sample Updates**  
Expected vs. sample updates.  
*Terms:* expected vs sample updates  
→ PDF pp. 194–195 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Trajectory Sampling**  
Trajectory sampling.  
*Terms:* trajectory sampling  
→ PDF pp. 196–198 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Real-time Dynamic Programming**  
Real-time DP.  
*Terms:* real-time dynamic programming  
→ PDF pp. 199–201 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Planning at Decision Time**  
Planning at decision time.  
*Terms:* decision-time planning  
→ PDF p. 202 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Heuristic Search**  
Heuristic search.  
*Terms:* heuristic search  
→ PDF pp. 203–204 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Rollout Algorithms**  
Rollout algorithms.  
*Terms:* rollout  
→ PDF pp. 205–206 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Monte Carlo Tree Search**  
Monte Carlo tree search.  
*Terms:* MCTS  
→ PDF pp. 207–209 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch9"></a>
## 9 On-policy Prediction with Approximation

*PDF pp. 219–264*

Function approximation for value prediction.

**Value-function Approximation**  
Value prediction as supervised learning.  
*Terms:* function approximation  
→ PDF p. 220 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**The Prediction Objective (VE)**  
The mean squared value error objective.  
*Terms:* value error objective  
→ PDF p. 221 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Stochastic-gradient and Semi-gradient Methods**  
Gradient and semi-gradient methods.  
*Terms:* semi-gradient TD  
→ PDF pp. 222–225 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Linear Methods**  
Linear methods and TD fixed points.  
*Terms:* linear methods, TD fixed point  
→ PDF pp. 226–231 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Feature Construction for Linear Methods**  
Polynomials, Fourier basis, coarse coding, tile coding, RBFs.  
*Terms:* Fourier basis, tile coding, coarse coding, RBF  
→ PDF pp. 232–243 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Selecting Step-Size Parameters Manually**  
Choosing step sizes.  
*Terms:* step size  
→ PDF p. 244 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Nonlinear Function Approximation: Artificial Neural Networks**  
Neural networks and deep RL.  
*Terms:* neural networks, deep RL  
→ PDF pp. 245–249 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Least-Squares TD**  
Least-squares TD.  
*Terms:* LSTD  
→ PDF pp. 250–251 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Memory-based Function Approximation**  
Memory-based approximation.  
*Terms:* memory-based, nearest neighbor  
→ PDF pp. 252–253 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Kernel-based Function Approximation**  
Kernel methods.  
*Terms:* kernel methods  
→ PDF pp. 254–255 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Looking Deeper at On-policy Learning: Interest and Emphasis**  
Interest and emphasis.  
*Terms:* interest, emphasis  
→ PDF pp. 256–257 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch10"></a>
## 10 On-policy Control with Approximation

*PDF pp. 265–278*

Control with function approximation.

**Episodic Semi-gradient Control**  
Episodic semi-gradient Sarsa (mountain car).  
*Terms:* semi-gradient Sarsa, mountain car  
→ PDF pp. 265–268 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Semi-gradient n-step Sarsa**  
n-step semi-gradient Sarsa.  
*Terms:* n-step Sarsa  
→ PDF pp. 269–270 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Average Reward: A New Problem Setting for Continuing Tasks**  
The average-reward setting for continuing tasks.  
*Terms:* average reward, differential return  
→ PDF pp. 271–274 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Deprecating the Discounted Setting**  
Why discounting is problematic with approximation.  
*Terms:* discounting  
→ PDF pp. 275–276 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Differential Semi-gradient n-step Sarsa**  
Differential semi-gradient Sarsa.  
*Terms:* differential Sarsa  
→ PDF p. 277 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch11"></a>
## 11 Off-policy Methods with Approximation

*PDF pp. 279–308*

Why off-policy learning with approximation is hard.

**Semi-gradient Methods**  
Semi-gradient off-policy TD.  
*Terms:* off-policy semi-gradient  
→ PDF pp. 280–281 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Examples of Off-policy Divergence**  
Baird’s counterexample and divergence.  
*Terms:* Baird counterexample, divergence  
→ PDF pp. 282–285 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**The Deadly Triad**  
The deadly triad.  
*Terms:* deadly triad  
→ PDF pp. 286–287 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Linear Value-function Geometry**  
Geometry of linear value functions and the projected Bellman error.  
*Terms:* projected Bellman error  
→ PDF pp. 288–290 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Gradient Descent in the Bellman Error**  
Gradient descent on the Bellman error.  
*Terms:* residual gradient  
→ PDF pp. 291–295 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**The Bellman Error is Not Learnable**  
The Bellman error is not learnable.  
*Terms:* learnability  
→ PDF pp. 296–299 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Gradient-TD Methods**  
Gradient-TD methods (GTD2, TDC).  
*Terms:* gradient-TD, GTD2, TDC  
→ PDF pp. 300–302 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Emphatic-TD Methods**  
Emphatic-TD.  
*Terms:* emphatic TD  
→ PDF pp. 303–304 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Reducing Variance**  
Reducing variance.  
*Terms:* variance reduction  
→ PDF p. 305 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch12"></a>
## 12 Eligibility Traces

*PDF pp. 309–342*

Eligibility traces and their modern forms.

**The λ-return**  
The λ-return.  
*Terms:* lambda-return  
→ PDF pp. 310–313 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**TD(λ)**  
TD(λ) with accumulating traces.  
*Terms:* TD(λ), eligibility trace  
→ PDF pp. 314–316 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**n-step Truncated λ-return Methods**  
Truncated λ-return methods.  
*Terms:* truncated lambda-return  
→ PDF pp. 317–318 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Redoing Updates: Online λ-return Algorithm**  
Online λ-return by redoing updates.  
*Terms:* online lambda-return  
→ PDF pp. 319–320 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**True Online TD(λ)**  
True online TD(λ) and dutch traces.  
*Terms:* true online TD(λ), dutch traces  
→ PDF pp. 321–322 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Dutch Traces in Monte Carlo Learning**  
Dutch traces in Monte Carlo learning.  
*Terms:* Monte Carlo, dutch traces  
→ PDF pp. 323–324 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Sarsa(λ)**  
Sarsa(λ).  
*Terms:* Sarsa(λ)  
→ PDF pp. 325–328 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Variable λ and γ**  
State-dependent λ and γ.  
*Terms:* variable lambda, termination  
→ PDF pp. 329–330 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Off-policy Traces with Control Variates**  
Off-policy traces with control variates.  
*Terms:* control variates  
→ PDF pp. 331–333 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Watkins's Q(λ) to Tree-Backup(λ)**  
From Watkins’s Q(λ) to tree-backup(λ).  
*Terms:* Watkins Q(λ), tree backup  
→ PDF pp. 334–335 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Stable Off-policy Methods with Traces**  
Stable off-policy trace methods.  
*Terms:* GTD(λ), HTD(λ), emphatic TD(λ)  
→ PDF pp. 336–337 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Implementation Issues**  
Implementation.  
*Terms:* implementation  
→ PDF p. 338 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch13"></a>
## 13 Policy Gradient Methods

*PDF pp. 343–358*

Learning parameterized policies directly.

**Policy Approximation and its Advantages**  
Advantages of policy approximation.  
*Terms:* policy parameterization, softmax  
→ PDF pp. 344–345 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**The Policy Gradient Theorem**  
The policy gradient theorem.  
*Terms:* policy gradient theorem  
→ PDF pp. 346–347 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**REINFORCE: Monte Carlo Policy Gradient**  
REINFORCE.  
*Terms:* REINFORCE  
→ PDF pp. 348–350 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**REINFORCE with Baseline**  
REINFORCE with a baseline.  
*Terms:* baseline  
→ PDF pp. 351–352 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Actor–Critic Methods**  
Actor–critic methods.  
*Terms:* actor-critic  
→ PDF pp. 353–354 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Policy Gradient for Continuing Problems**  
Policy gradients for continuing problems.  
*Terms:* average reward policy gradient  
→ PDF pp. 355–356 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Policy Parameterization for Continuous Actions**  
Gaussian policies for continuous actions.  
*Terms:* continuous actions, Gaussian policy  
→ PDF pp. 357–358 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch14"></a>
## 14 Psychology

*PDF pp. 363–398*

Links between RL and animal learning psychology.

**Prediction and Control**  
Prediction vs. control in psychology.  
*Terms:* prediction, control  
→ PDF p. 364 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Classical Conditioning**  
Classical conditioning, blocking, Rescorla–Wagner and the TD model.  
*Terms:* classical conditioning, Rescorla-Wagner, TD model, blocking  
→ PDF pp. 365–378 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Instrumental Conditioning**  
Instrumental conditioning and the law of effect.  
*Terms:* instrumental conditioning, law of effect  
→ PDF pp. 379–382 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Delayed Reinforcement**  
Delayed reinforcement.  
*Terms:* delayed reinforcement, eligibility  
→ PDF pp. 383–384 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Cognitive Maps**  
Cognitive maps.  
*Terms:* cognitive maps, latent learning  
→ PDF p. 385 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Habitual and Goal-directed Behavior**  
Habitual vs. goal-directed behavior.  
*Terms:* habits, goal-directed, model-free, model-based  
→ PDF pp. 386–389 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch15"></a>
## 15 Neuroscience

*PDF pp. 399–442*

Links between RL and neuroscience, especially dopamine.

**Neuroscience Basics**  
Neuroscience basics.  
*Terms:* neurons, synaptic plasticity  
→ PDF pp. 400–401 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Reward Signals, Reinforcement Signals, Values, and Prediction Errors**  
Reward and reinforcement signals, values, prediction errors.  
*Terms:* reward signal, prediction error  
→ PDF p. 402 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**The Reward Prediction Error Hypothesis**  
The reward prediction error hypothesis.  
*Terms:* reward prediction error hypothesis  
→ PDF pp. 403–404 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Dopamine**  
Dopamine neurons.  
*Terms:* dopamine  
→ PDF pp. 405–408 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Experimental Support for the Reward Prediction Error Hypothesis**  
Experimental support.  
*Terms:* experimental evidence, Schultz  
→ PDF pp. 409–411 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**TD Error/Dopamine Correspondence**  
Correspondence between TD error and dopamine.  
*Terms:* TD error, dopamine  
→ PDF pp. 412–416 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Neural Actor–Critic**  
A neural actor–critic.  
*Terms:* neural actor-critic, striatum  
→ PDF pp. 417–419 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Actor and Critic Learning Rules**  
Learning rules for actor and critic.  
*Terms:* three-factor learning rules  
→ PDF pp. 420–423 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Hedonistic Neurons**  
Hedonistic neurons.  
*Terms:* hedonistic neurons  
→ PDF pp. 424–425 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Collective Reinforcement Learning**  
Collective RL.  
*Terms:* collective learning  
→ PDF pp. 426–428 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Model-based Methods in the Brain**  
Model-based methods in the brain.  
*Terms:* model-based, brain  
→ PDF pp. 429–430 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Addiction**  
Addiction.  
*Terms:* addiction  
→ PDF p. 431 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch16"></a>
## 16 Applications and Case Studies

*PDF pp. 443–480*

Landmark applications.

**TD-Gammon**  
TD-Gammon.  
*Terms:* TD-Gammon  
→ PDF pp. 443–447 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Samuel's Checkers Player**  
Samuel’s checkers player.  
*Terms:* Samuel checkers  
→ PDF pp. 448–450 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Watson's Daily-Double Wagering**  
Watson’s Daily-Double wagering.  
*Terms:* Watson, Jeopardy  
→ PDF pp. 451–453 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Optimizing Memory Control**  
Learning DRAM memory controllers.  
*Terms:* memory controller  
→ PDF pp. 454–457 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Human-level Video Game Play**  
DQN on Atari games.  
*Terms:* DQN, Atari  
→ PDF pp. 458–462 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Mastering the Game of Go**  
AlphaGo and AlphaGo Zero.  
*Terms:* AlphaGo, AlphaGo Zero, MCTS  
→ PDF pp. 463–471 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Personalized Web Services**  
Personalized web recommendations.  
*Terms:* personalized web services, contextual bandits  
→ PDF pp. 472–474 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Thermal Soaring**  
Learning to soar in thermals.  
*Terms:* thermal soaring  
→ PDF pp. 475–480 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)


---

<a id="ch17"></a>
## 17 Frontiers

*PDF pp. 481–501*

Open problems and the future.

**General Value Functions and Auxiliary Tasks**  
General value functions and auxiliary tasks.  
*Terms:* general value functions, auxiliary tasks  
→ PDF pp. 481–482 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Temporal Abstraction via Options**  
Options and temporal abstraction.  
*Terms:* options, temporal abstraction  
→ PDF pp. 483–485 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Observations and State**  
Partial observability and state construction.  
*Terms:* partial observability, state construction  
→ PDF pp. 486–490 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Designing Reward Signals**  
Designing reward signals.  
*Terms:* reward design, shaping  
→ PDF pp. 491–493 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Remaining Issues**  
Remaining issues.  
*Terms:* open issues  
→ PDF pp. 494–496 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

**Reinforcement Learning and the Future of Artificial Intelligence**  
RL and the future of AI, including safety.  
*Terms:* AI safety, future  
→ PDF pp. 497–501 in [the PDF](https://drive.google.com/file/d/1khDj3STP0M9-litTZfZfigTQTaJ9LzUb/view)

