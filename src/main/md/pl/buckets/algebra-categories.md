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

**Transformers need only applicative structure, which gives them a partial denotational semantics.**
Funcformer rewrites attention and the MLP using only `pair` (the monoidal laxator) and a `counit` that generalises summation, so any applicative can replace `Vector N`. Using the Reader functor `Float -> a` turns dot products into L² inner products and matrix products into integral operators. That places the construction in neural-operator territory, and the post tests it on Poisson's equation. The companion papers on the anatomy of attention and a pattern language for ML tasks give the diagrammatic calculus. Still open: the semantics covers a single forward pass, not the sampling loop built on top of it.
[Papers › Deep Learning](../Books/Papers#deep-learning) · [Papers › Functional Programming](../Books/Papers#functional-programming)

**A chat loop has the shape of a category, but the proofs stop where the model starts.**
Take context states as objects and exchanges as morphisms. Skills then act like functors, memory like a coalgebra (Spivak's polynomial functors), the feedback loop like a trace (Joyal–Street–Verity), and sampling like a Markov category (Fritz). That structure is descriptive until the model step has a denotation. Restricting morphisms to size-decreasing transformations, as λ-RLM does, is the piece that makes it provable. Still open: the top layer, the full interpreter with memory and skills.
[Papers › Category Theory](../Books/Papers#category-theory)

**Categories meet machine learning.**
- *On the Anatomy of Attention* breaks attention variants into shared diagrammatic building blocks. Its companion *pattern language for ML tasks* specifies tasks independently of architecture.

**Compositional structure can be defined as the extra description length a whole's model needs beyond its parts' models.**
The paper takes the MDL-optimal model of each part and of the whole, and counts compositional novelty as K(m_x | m_parts). Scored at every node of a decomposition tree, that gives a profile across scales. The tree is a rose tree whose labels concatenate. The profile is a plain fold over it, and the maximal decomposition reduces it to an interval DP over binary splits. Turned into a reward, the measure evolves deeper but smaller string grammars and more unified CPPN images. Still open: the scores depend on the chosen compressor, and nobody knows which decomposition tree is canonical. [Papers › AI and Machine Learning › Foundations](../Books/Papers#foundations)

The common thread: when an LLM system is described compositionally, its parts can be reasoned about separately. That is the premise of the Kyo work in [Effects and LLM Systems](bucket-effects-llm.md).

Sources: [Papers › Category Theory](../Books/Papers#category-theory), [Papers › Deep Learning](../Books/Papers#deep-learning), [Papers › Foundations](../Books/Papers#foundations), [Technical › Category Theory](../Books/Technical#category-theory).
