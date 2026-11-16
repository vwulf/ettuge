<a id="ch1"></a>
# Reinforcement Learning: An Introduction (2nd edition draft)

> Richard S. Sutton and Andrew G. Barto · MIT Press; this PDF is an early “in progress” draft of the second edition · [the PDF in Drive](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

PDF page = printed page + 14. This draft predates the published 2018 edition: several chapters (off-policy approximation, psychology, neuroscience) are one-page placeholders and are left out here, and the later chapters differ from the final book. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The standard introduction to reinforcement learning: an agent learning by trial and error to maximize reward. Part I covers tabular methods: bandits and exploration, finite MDPs and the Bellman equations, dynamic programming, Monte Carlo methods, temporal-difference learning (Sarsa, Q-learning), eligibility traces and TD(λ), and planning with learned models (Dyna, prioritized sweeping, MCTS). Part II extends value prediction and control to function approximation and introduces actor–critic and average-reward methods. A case-study chapter covers TD-Gammon, Samuel’s checkers player, the acrobot, elevator dispatching, channel allocation and job-shop scheduling.

**Contents**

1. [The Reinforcement Learning Problem](ch1): What reinforcement learning is and where it came from.
2. [Multi-arm Bandits](ch2): Balancing exploration and exploitation in a single-state problem.
3. [Finite Markov Decision Processes](ch3): The formal problem: finite Markov decision processes.
4. [Dynamic Programming](ch4): Computing optimal policies when the model is known.
5. [Monte Carlo Methods](ch5): Learning values from complete sampled episodes.
6. [Temporal-Difference Learning](ch6): Bootstrapping from estimates: temporal-difference learning.
7. [Eligibility Traces](ch7): Unifying TD and Monte Carlo with eligibility traces.
8. [Planning and Learning with Tabular Methods](ch8): Integrating planning with learning in tabular methods.
9. [On-policy Approximation of Action Values](ch9): Function approximation for prediction and control.
10. [Policy Approximation](ch10): Learning policies directly.
11. [Applications and Case Studies](ch11): Case studies of RL applied to real problems.
12. [Prospects](ch12): Open directions.


---

## The Reinforcement Learning Problem

*PDF pp. 15–44*

What reinforcement learning is and where it came from.

**Reinforcement Learning**  
Learning from interaction to maximize reward.  
*Terms:* reinforcement learning  
→ PDF pp. 16–18 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Examples**  
Examples from games, robotics and biology.  
*Terms:* examples  
→ PDF pp. 19–20 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Elements of Reinforcement Learning**  
Policy, reward, value function and model.  
*Terms:* policy, reward signal, value function, model  
→ PDF pp. 21–22 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Limitations and Scope**  
What is and is not covered.  
*Terms:* scope, evolutionary methods  
→ PDF p. 23 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**An Extended Example: Tic-Tac-Toe**  
Learning tic-tac-toe with a value table.  
*Terms:* tic-tac-toe, temporal difference  
→ PDF pp. 24–28 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**History of Reinforcement Learning**  
Optimal control, trial-and-error learning and TD learning as historical threads.  
*Terms:* history, optimal control, Bellman, law of effect  
→ PDF pp. 30–38 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch2"></a>
## Multi-arm Bandits

*PDF pp. 45–66*

Balancing exploration and exploitation in a single-state problem.

**An n-Armed Bandit Problem**  
The k-armed bandit.  
*Terms:* multi-armed bandit  
→ PDF p. 46 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Action-Value Methods**  
Estimating action values; ε-greedy.  
*Terms:* action values, epsilon-greedy  
→ PDF pp. 47–49 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Incremental Implementation**  
Incremental averages.  
*Terms:* incremental update  
→ PDF pp. 50–51 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Tracking a Nonstationary Problem**  
Constant step sizes for changing problems.  
*Terms:* nonstationary, step size  
→ PDF p. 52 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Optimistic Initial Values**  
Optimistic initial values.  
*Terms:* optimistic initialization  
→ PDF pp. 53–54 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Upper-Confidence-Bound Action Selection**  
UCB action selection.  
*Terms:* upper confidence bound  
→ PDF p. 55 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Gradient Bandits**  
Gradient bandit algorithms.  
*Terms:* gradient bandit, softmax  
→ PDF pp. 56–59 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Associative Search (Contextual Bandits)**  
Contextual bandits.  
*Terms:* contextual bandits  
→ PDF p. 60 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch3"></a>
## Finite Markov Decision Processes

*PDF pp. 67–102*

The formal problem: finite Markov decision processes.

**The Agent–Environment Interface**  
Agent, environment, states, actions, rewards.  
*Terms:* agent-environment interface  
→ PDF pp. 67–70 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Goals and Rewards**  
The reward hypothesis.  
*Terms:* reward hypothesis  
→ PDF pp. 71–72 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Returns**  
Returns and discounting.  
*Terms:* return, discounting  
→ PDF pp. 73–74 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Unified Notation for Episodic and Continuing Tasks**  
Episodic vs. continuing tasks.  
*Terms:* episodic, continuing  
→ PDF p. 75 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**The Markov Property**  
The Markov property.  
*Terms:* Markov property  
→ PDF pp. 76–80 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Markov Decision Processes**  
MDP dynamics.  
*Terms:* MDP, transition probabilities  
→ PDF pp. 81–83 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Value Functions**  
State and action value functions and Bellman equations.  
*Terms:* value function, Bellman equation  
→ PDF pp. 84–88 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Optimal Value Functions**  
Optimal values and Bellman optimality.  
*Terms:* optimal value function, Bellman optimality  
→ PDF pp. 89–92 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Optimality and Approximation**  
Why exact optimality is impractical.  
*Terms:* approximation  
→ PDF p. 93 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch4"></a>
## Dynamic Programming

*PDF pp. 103–126*

Computing optimal policies when the model is known.

**Policy Evaluation**  
Iterative policy evaluation.  
*Terms:* policy evaluation  
→ PDF pp. 104–107 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Policy Improvement**  
Policy improvement theorem.  
*Terms:* policy improvement  
→ PDF pp. 108–109 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Policy Iteration**  
Policy iteration.  
*Terms:* policy iteration  
→ PDF pp. 110–111 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Value Iteration**  
Value iteration.  
*Terms:* value iteration  
→ PDF pp. 112–114 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Asynchronous Dynamic Programming**  
Asynchronous DP.  
*Terms:* asynchronous dynamic programming  
→ PDF pp. 115–117 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Generalized Policy Iteration**  
Generalized policy iteration.  
*Terms:* generalized policy iteration  
→ PDF pp. 118–119 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Efficiency of Dynamic Programming**  
Efficiency.  
*Terms:* efficiency, curse of dimensionality  
→ PDF p. 120 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch5"></a>
## Monte Carlo Methods

*PDF pp. 127–156*

Learning values from complete sampled episodes.

**Monte Carlo Prediction**  
First-visit and every-visit prediction.  
*Terms:* Monte Carlo prediction  
→ PDF pp. 128–132 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Monte Carlo Estimation of Action Values**  
Estimating action values.  
*Terms:* action values  
→ PDF p. 133 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Monte Carlo Control**  
MC control with exploring starts.  
*Terms:* exploring starts  
→ PDF pp. 134–137 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Monte Carlo Control without Exploring Starts**  
On-policy control with soft policies.  
*Terms:* epsilon-soft, on-policy  
→ PDF pp. 138–140 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Off-policy Prediction via Importance Sampling**  
Importance sampling for off-policy prediction.  
*Terms:* importance sampling, off-policy  
→ PDF pp. 141–146 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Incremental Implementation**  
Incremental implementation.  
*Terms:* weighted importance sampling  
→ PDF pp. 147–148 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Off-Policy Monte Carlo Control**  
Off-policy MC control.  
*Terms:* off-policy control  
→ PDF p. 149 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Importance Sampling on Truncated Returns**  
Truncated-return importance sampling.  
*Terms:* truncated returns  
→ PDF pp. 150–151 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch6"></a>
## Temporal-Difference Learning

*PDF pp. 157–180*

Bootstrapping from estimates: temporal-difference learning.

**TD Prediction**  
TD(0) prediction.  
*Terms:* TD(0), TD error  
→ PDF pp. 157–161 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Advantages of TD Prediction Methods**  
Why TD often beats MC.  
*Terms:* bootstrapping  
→ PDF pp. 162–164 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Optimality of TD(0)**  
Batch TD and certainty equivalence.  
*Terms:* batch updating, certainty equivalence  
→ PDF pp. 165–167 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Sarsa: On-Policy TD Control**  
Sarsa.  
*Terms:* Sarsa  
→ PDF pp. 168–170 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Q-Learning: Off-Policy TD Control**  
Q-learning.  
*Terms:* Q-learning  
→ PDF pp. 171–173 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Games, Afterstates, and Other Special Cases**  
Afterstates and special cases.  
*Terms:* afterstates  
→ PDF p. 174 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch7"></a>
## Eligibility Traces

*PDF pp. 181–208*

Unifying TD and Monte Carlo with eligibility traces.

**n-Step TD Prediction**  
n-step returns.  
*Terms:* n-step TD  
→ PDF pp. 182–185 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**The Forward View of TD(λ)**  
λ-returns (forward view).  
*Terms:* lambda-return, forward view  
→ PDF pp. 186–190 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**The Backward View of TD(λ)**  
Eligibility traces (backward view).  
*Terms:* eligibility traces, backward view  
→ PDF pp. 191–194 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Equivalences of Forward and Backward Views**  
When the views agree.  
*Terms:* equivalence  
→ PDF pp. 195–196 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Sarsa(λ)**  
Sarsa(λ).  
*Terms:* Sarsa(λ)  
→ PDF pp. 197–199 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Watkins’s Q(λ)**  
Watkins’s Q(λ).  
*Terms:* Watkins Q(λ)  
→ PDF pp. 200–201 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Off-policy Eligibility Traces using Importance Sampling**  
Off-policy traces.  
*Terms:* off-policy traces  
→ PDF p. 202 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Implementation Issues**  
Implementation.  
*Terms:* implementation  
→ PDF p. 203 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Variable λ**  
Variable λ.  
*Terms:* variable lambda  
→ PDF p. 204 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch8"></a>
## Planning and Learning with Tabular Methods

*PDF pp. 209–238*

Integrating planning with learning in tabular methods.

**Models and Planning**  
Models and planning.  
*Terms:* model-based, planning  
→ PDF pp. 209–211 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Integrating Planning, Acting, and Learning**  
Dyna architecture.  
*Terms:* Dyna-Q  
→ PDF pp. 212–216 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**When the Model Is Wrong**  
Coping with wrong models (Dyna-Q+).  
*Terms:* model error, exploration bonus  
→ PDF pp. 217–219 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Prioritized Sweeping**  
Prioritized sweeping.  
*Terms:* prioritized sweeping  
→ PDF pp. 220–223 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Full vs. Sample Backups**  
Expected vs. sample backups.  
*Terms:* full vs sample backups  
→ PDF pp. 224–226 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Trajectory Sampling**  
Trajectory sampling.  
*Terms:* trajectory sampling  
→ PDF pp. 227–230 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Heuristic Search**  
Heuristic search.  
*Terms:* heuristic search  
→ PDF pp. 231–233 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Monte Carlo Tree Search**  
Monte Carlo tree search.  
*Terms:* MCTS  
→ PDF p. 234 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch9"></a>
## On-policy Approximation of Action Values

*PDF pp. 239–268*

Function approximation for prediction and control.

**Value Prediction with Function Approximation**  
Value prediction with approximation.  
*Terms:* function approximation  
→ PDF pp. 240–242 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Gradient-Descent Methods**  
Gradient and semi-gradient methods.  
*Terms:* gradient descent, semi-gradient  
→ PDF pp. 243–245 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Linear Methods**  
Linear methods, coarse and tile coding, RBFs.  
*Terms:* linear features, tile coding, coarse coding, RBF  
→ PDF pp. 246–254 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Control with Function Approximation**  
Control with approximation (e.g. mountain car).  
*Terms:* control, mountain car  
→ PDF pp. 255–260 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Should We Bootstrap?**  
Bootstrapping versus Monte Carlo under approximation.  
*Terms:* bootstrapping  
→ PDF pp. 261–262 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch10"></a>
## Policy Approximation

*PDF pp. 271–282*

Learning policies directly.

**Actor–Critic Methods**  
Actor–critic methods.  
*Terms:* actor-critic  
→ PDF pp. 271–272 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Eligibility Traces for Actor–Critic Methods**  
Traces for actor–critic.  
*Terms:* eligibility traces  
→ PDF p. 273 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**R-Learning and the Average-Reward Setting**  
R-learning and average reward.  
*Terms:* R-learning, average reward  
→ PDF pp. 274–282 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch11"></a>
## Applications and Case Studies

*PDF pp. 287–316*

Case studies of RL applied to real problems.

**TD-Gammon**  
TD-Gammon.  
*Terms:* TD-Gammon, backgammon  
→ PDF pp. 287–292 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Samuel’s Checkers Player**  
Samuel’s checkers player.  
*Terms:* Samuel checkers  
→ PDF pp. 293–295 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**The Acrobot**  
Acrobot swing-up.  
*Terms:* acrobot  
→ PDF pp. 296–299 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Elevator Dispatching**  
Elevator dispatching.  
*Terms:* elevator dispatching  
→ PDF pp. 300–304 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Dynamic Channel Allocation**  
Channel allocation in cellular systems.  
*Terms:* dynamic channel allocation  
→ PDF pp. 305–308 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Job-Shop Scheduling**  
Job-shop scheduling.  
*Terms:* job-shop scheduling  
→ PDF pp. 309–316 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)


---

<a id="ch12"></a>
## Prospects

*PDF pp. 317–324*

Open directions.

**The Unified View**  
The unified view of RL methods.  
*Terms:* unified view  
→ PDF pp. 317–319 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**State Estimation**  
State estimation under partial observability.  
*Terms:* POMDP, state estimation  
→ PDF p. 320 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Temporal Abstraction**  
Temporal abstraction and options.  
*Terms:* options, temporal abstraction  
→ PDF p. 320 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Predictive Representations**  
Predictive state representations.  
*Terms:* predictive representations  
→ PDF p. 320 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

**Other Frontier Dimensions**  
Other frontiers.  
*Terms:* frontiers  
→ PDF pp. 320–324 in [the PDF](https://drive.google.com/file/d/15cJp-WoqoqiflM0OPxmgOYLXqhYIOL1v/view)

