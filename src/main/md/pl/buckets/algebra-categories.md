# Algebra and Categories

The algebraic structures used every day in Scala and Haskell (semigroups, monoids, functors, applicatives, monads), and the category theory behind them, followed into machine learning.

## Articles

- [Monoids and Semigroups](monoids-and-semigroups.md) — associativity explains why joining markdown files with pandoc works one file at a time or all at once.

## Deep-dive gists

**Applicatives vs monads: when is the shape of the effect known?** McBride and Paterson's *Applicative programming with effects* defines an applicative as an effectful computation whose structure is fixed before it runs. A monad lets later effects depend on earlier results. That explains an old struggle with `ValidationNel`: accumulating every error is applicative, because all the checks are independent. Short-circuiting on the first failure is monadic. Partial successes fit neither out of the box. The same distinction drives `ApplicativeDo` and lets Funcformer (below) swap in an applicative where a transformer uses vectors.

**Two ways into category theory.** Milewski's *Category Theory for Programmers* starts from code: types as objects, functions as arrows, monads as composition of effectful functions. Riehl's *Category Theory in Context* starts from mathematics: universal properties, Yoneda, limits and adjunctions, with examples from algebra and topology. They work best read together. Milewski supplies the intuition, and Riehl explains why the definitions are the right ones.

**Poly: one language for interacting systems.** Niu and Spivak treat polynomial functors as interfaces: positions are what a system can show, and directions are what it can receive at each position. Dynamical systems, wiring diagrams and databases are then all morphisms in one category. The interface changes with the mode a system is in, which is what makes Poly look like a natural home for effect handlers and agent protocols.

**Feedback, probability and higher structure.**
- *Traced monoidal categories* (Joyal, Street and Verity) axiomatize loops and feedback. The Int construction embeds them in compact closed categories. This is the categorical counterpart of the Y combinator.
- *Markov categories* (Fritz) do probability synthetically. Conditional independence and sufficient statistics become properties of string diagrams, with no measure theory up front.
- *∞-categories*: Riehl and Verity's *Elements of ∞-Category Theory* develops the theory model-independently through ∞-cosmoi. The ∞-cosmos Lean blueprint and Carneiro and Riehl's *Formalizing Colimits in Cat* show what changes when that mathematics has to be machine-checked (more in [Proof and Formalization](bucket-proof-formalization.md)).

**Categories meet machine learning.**
- *Funcformer* (Laakkonen) rebuilds the transformer from applicative functors, so attention can run over functions, graphs or distributions as well as vectors.
- *On the Anatomy of Attention* breaks attention variants into shared diagrammatic building blocks. Its companion *pattern language for ML tasks* specifies tasks independently of architecture.
- *Defining and Generating Compositional Structure* (Elmoznino, Bengio et al.) gives compositionality a complexity-based definition and a way to generate data with controlled compositional structure. It was read together with a rose-tree follow-up.

The common thread: when an LLM system is described compositionally, its parts can be reasoned about separately. That is the premise of the Kyo work in [Effects and LLM Systems](bucket-effects-llm.md).

Sources: [Papers › Category Theory](../Books/Papers#category-theory), [Papers › Deep Learning](../Books/Papers#deep-learning), [Papers › Foundations](../Books/Papers#foundations), [Technical › Category Theory](../Books/Technical#category-theory).
