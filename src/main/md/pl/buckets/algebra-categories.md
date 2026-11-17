# Algebra and Categories

The algebraic structures used every day in Scala and Haskell (semigroups, monoids, functors, applicatives, monads), and the category theory behind them, followed into machine learning.

## Articles

- [Monoids and Semigroups](monoids-and-semigroups.md) — associativity explains why joining markdown files with pandoc works one file at a time or all at once.

## Deep-dive gists

**Applicatives vs monads: when is the shape of the effect known?** McBride and Paterson's *Applicative programming with effects* defines an applicative as an effectful computation whose structure is fixed before it runs. A monad lets later effects depend on earlier results. That explains an old struggle with `ValidationNel`: accumulating every error is applicative, because all the checks are independent. Short-circuiting on the first failure is monadic. Partial successes fit neither out of the box. The same distinction drives `ApplicativeDo` and lets Funcformer (below) swap in an applicative where a transformer uses vectors.

**Two ways into category theory.** Milewski's *Category Theory for Programmers* starts from code: types as objects, functions as arrows, monads as composition of effectful functions. Riehl's *Category Theory in Context* starts from mathematics: universal properties, Yoneda, limits and adjunctions, with examples from algebra and topology. They work best read together. Milewski supplies the intuition, and Riehl explains why the definitions are the right ones.

**A representable functor is one with a generic example. Every other example is that one specialized along a map.**
`F : C → Set` is representable when `F ≅ Hom(a, −)` for some object `a`. Yoneda (next gist) says the isomorphism is fixed by one universal element `u ∈ F(a)`, the image of `id_a`, and every element of every `F(X)` is `F(f)(u)` for exactly one `f : a → X`.

*In programming,* representable functors are containers of fixed shape: `f x ≅ (Rep -> x)`, where `Rep` is the type of positions.
- `Pair a ≅ Bool -> a`, `Stream a ≅ Nat -> a`, `Vec n a ≅ Fin n -> a`, and infinite binary trees are indexed by paths. `Maybe` and `List` are not representable, because their shape varies and `Nothing` has no position.
- `tabulate` and `index` make the functor secretly `Reader Rep`, so `zip`, `Applicative` and `Monad` come for free.
- Turning `Rep -> x` into a data structure is memoization (Hinze's *Memo functions, polytypically!*, Elliott's memo tries). Gibbons' *APLicative Programming with Naperian Functors* builds typed multidimensional arrays this way, with transpose as a swap of indices.
- `f x ≅ x^Rep`, so `Rep` behaves like a logarithm of `f`, which is why McBride calls these functors Naperian.

*In mathematics,* the representing object is a classifier:
- The elements of a group are maps `ℤ → G`, and the elements of a ring are maps `ℤ[x] → R`. The generic element is `x`, and every element of every ring is `x` specialized by a map.
- Subsets are maps to `2`, so the powerset functor is `Hom(−, 2)`. In a topos, `2` becomes the subobject classifier.
- Rank-n vector bundles on `X` are maps into a Grassmannian, and cohomology classes are maps into `K(G, n)`. The representing space carries the universal bundle or class, and everything else is pulled back from it.
- Universal properties are representability: `A × B` represents pairs of maps, the tensor product represents bilinear maps, and the free group on `S` represents functions out of `S`.

*Recursive datatypes* connect through polynomial functors, or containers. A datatype is a fixpoint of `P(x) = Σ_{s ∈ S} x^{E(s)}`, with shapes `s` and positions `E(s)`, and a representable functor is the case with one shape. Finite lists and trees vary in shape, so they are sums of representables, one per shape (Abbott, Altenkirch and Ghani, *Containers*). Infinite codata with fixed branching is representable, and its positions form an inductive type: the final coalgebra of `X ↦ a × F X`, with `F` represented by `R`, is represented by `List R`, the paths into it.
- `Stream a = νX. a × X ≅ Nat -> a`, and `Nat = μX. 1 + X` is the fold side.
- `νX. a × X × X ≅ [Bool] -> a` for infinite binary trees.
- Rose trees whose children form a stream give `νX. a × Stream X ≅ [Nat] -> a`. Finite rose trees `μX. a × List X` are not representable.

Hinze's *Generalizing Generalized Tries* turns this around: every inductive key type `K` has a trie functor `T_K` with `T_K v ≅ K -> v`, computed by the laws of exponents (`1 -> v ≅ v`, `(K₁ + K₂) -> v ≅ (K₁ -> v) × (K₂ -> v)`, `(K₁ × K₂) -> v ≅ K₁ -> K₂ -> v`). Data built by folds are the representing objects, and their memo tables are the representable functors. `Traversable` fits the same picture: finitary containers are traversable (Jaskelioff and Rypacek), and O'Connor and Jaskelioff showed the converse, so traversing works shape by shape on each shape's representable piece.

Where to read it:
- Milewski, *CTFP*, [ch. 14 Representable Functors](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch14), pp. 273–279
- Smith, *Introducing Category Theory*, [ch. 37 Representables and universal elements](../Deep-Dives/textbooks/smith-introducing-category-theory/ch37), pp. 336–341
- McBride, *Perhaps Not the Answer*, [ch. 6](../Deep-Dives/textbooks/mcbride-perhaps-not-the-answer/ch6): *Representable (or Naperian) Functors*, pp. 140–142, and *Tries as Naperian Functors; Matching via their Derivatives*, pp. 143–148; [ch. 8](../Deep-Dives/textbooks/mcbride-perhaps-not-the-answer/ch8): *Why do we need containers?*, pp. 200–203
- Winitzki, *SOFP*, [ch. 3 › 3.3 Lists and trees as recursive disjunctive types](../Deep-Dives/textbooks/winitzki-science-of-functional-programming/ch3), pp. 130–141, and [ch. 12 Traversable functors](../Deep-Dives/textbooks/winitzki-science-of-functional-programming/ch13), pp. 738–765

Papers: [Hinze, *Generalizing Generalized Tries* (JFP 2000)](https://www.cs.ox.ac.uk/people/ralf.hinze/publications/GGTries/index.html) · [Gibbons, *APLicative Programming with Naperian Functors* (ESOP 2017)](https://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/aplicative.pdf) · [Abbott, Altenkirch and Ghani, *Containers: Constructing Strictly Positive Types* (TCS 2005)](https://people.cs.nott.ac.uk/psztxa/publ/cont-tcs.pdf) · [Jaskelioff and Rypacek, *An Investigation of the Laws of Traversals* (MSFP 2012)](https://arxiv.org/abs/1202.2919) · [O'Connor, *On the Static Nature of Traversals*](https://r6.ca/blog/20121209T182914Z.html)

**The Yoneda lemma says that a polymorphic function out of `a -> x` is determined by a single value, the one it produces from `id`.**
Milewski's version is the simplest one. Take a functor `F` and a natural transformation `α : C(a, −) → F`, which in Haskell is a polymorphic function `forall x. (a -> x) -> f x`. Feed it `id :: a -> a` and you get one value of type `f a`. Naturality then fixes everything else: for any `h :: a -> x`, `α h = fmap h (α id)`. So the function has no freedom beyond the choice of that one value, and `[C, Set](C(a, −), F) ≅ F a`. Read in code, `forall x. (a -> x) -> f x` is the same as `f a`. You can only produce an `f x` by `fmap`-ing `h` over a value you already had.
- **Objects are known by their relationships.** Taking `F = C(b, −)` gives the Yoneda embedding: maps `C(a, −) → C(b, −)` are exactly arrows `b → a`. An object is determined up to isomorphism by the arrows out of it, the way a type is determined by what you can do with it.
- **CPS.** With `F = Identity`, `forall r. (a -> r) -> r` is the same as `a`. This is the continuation-passing transform, and the codensity monad of the Kan extensions gist below is the same trick applied to a whole monad.
- **Co-Yoneda.** The dual says `exists x. (x -> a, f x)` is the same as `f a`. Storing the function next to the value turns any type constructor into a functor for free and fuses chains of `fmap` into one, which is the free functor `FreeF`.
- **As an end.** The Ninja Yoneda lemma writes the same fact as `∫_x Set(C(a, x), F x) ≅ F a`. This formula is what turns a Kan extension's universal property into an explicit end.

The payoff for programmers is Boisseau and Gibbons' *What You Needa Know about Yoneda*, which derives profunctor optics from plain getter/setter lenses by applying the lemma twice.
Reading in CTFP: [ch. 15 The Yoneda Lemma](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch15) → [ch. 16 Yoneda Embedding](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch16) → [ch. 26 Ends (Ninja Yoneda)](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch26).
[Papers › Functional Programming](../Books/Papers#functional-programming)

**CPS is the Yoneda lemma at the identity functor, and effect systems use it for encodings rather than semantics.**
No single paper is the source. CPS predates the categorical reading: Reynolds' *Definitional Interpreters* (1972) and Plotkin's *Call-by-name, call-by-value and the λ-calculus* (1975) never mention Yoneda. Mike Stay's 2008 n-Category Café post is the earliest explicit statement that the CPS transform and the Yoneda embedding are the same thing. Dan Piponi's blog post then gave the Haskell `Yoneda` newtype, and Hinze's MPC 2012 paper is the peer-reviewed version. In a programming language the isomorphism `forall r. (a -> r) -> r ≅ a` is usually proved by parametricity (Wadler, *Theorems for Free!*, 1989). Max New's PRL post pairs it with closure conversion, which is co-Yoneda. One caveat: the isomorphism needs a pure, parametric language. With first-class control such as `call/cc` the answer type cannot always stay polymorphic, and Thielecke's *Answer Type Polymorphism in Call-by-Name Continuation Passing* (2004) maps where it survives.

Effect systems are defined without Yoneda, through monads or algebraic effects. Their encodings use it in three places:
- **Codensity for speed.** Wrapping a free monad in `Codensity` re-associates binds and removes the quadratic slowdown (Voigtländer, *Asymptotic Improvement of Computations over Free Monads*, 2008). Over the state functor, Codensity is the Church encoding of state.
- **Co-Yoneda for freer monads.** Kiselyov and Ishii, *Freer Monads, More Extensible Effects* (2015), use co-Yoneda to drop the `Functor` requirement on effect signatures. Freer-simple and polysemy are built on it, and Kyo's suspended effects with their continuations have the same shape.
- **Monadic reflection for direct style.** Filinski, *Representing Monads* (1994), shows that any definable monad embeds into continuations plus state, which justifies writing effectful code in direct style. Algebraic effect handlers (Plotkin and Pretnar) make the continuation explicit: a handler receives the resumption `k`. OCaml 5 and Koka implement handlers with delimited continuations.

So Yoneda explains why these representations are faithful and why they are fast. The effect theory itself does not depend on it. More in [Effects and LLM Systems](bucket-effects-llm.md).
[n-Category Café: CPS and the Yoneda embedding](https://classes.golem.ph.utexas.edu/category/2008/01/the_continuation_passing_trans.html) · [Kmett: Free Monads for Less 2](https://ekmett.github.io/reader/2011/free-monads-for-less-2) · [Kmett: Unnatural Transformations and Quantifiers](https://ekmett.github.io/reader/2012/unnatural-transformations-and-quantifiers/index.html) · [PRL: Closure Conversion as CoYoneda](https://prl.khoury.northeastern.edu/blog/2017/08/28/closure-conversion-as-coyoneda) · [Thielecke 2004](https://link.springer.com/content/pdf/10.1007/978-3-540-24725-8_20.pdf)

**In programming Yoneda is a change of representation. In mathematics it is what lets a universal property define an object.**
Code rarely needs that guarantee, because a type comes with a concrete definition. Mathematics builds objects from universal properties all the time, and Yoneda is the guarantee that such a description fixes the object, and that maps between descriptions are maps between objects. It does four kinds of work:
- **A proof technique.** To show `A ≅ B`, show `Hom(A, X) ≅ Hom(B, X)` naturally in `X`. For example, `(A × B) × C ≅ A × (B × C)` because a map into either side is a triple of maps. The same move shows that adjoints are unique, that right adjoints preserve limits and that currying is an isomorphism.
- **Defining an object by the functor it represents.** In Grothendieck's functor of points, a space `X` is identified with `Hom(−, X)`, its points with coordinates in every ring at once, and Yoneda says nothing is lost. A moduli space such as "the space of elliptic curves" is defined as whatever represents the functor of families of elliptic curves. Structure transfers too: if `Hom(−, X)` is naturally a group, `X` is a group object, which is how `GLₙ` and elliptic curves get their group laws.
- **Classifying invariants.** Cohomology `Hⁿ(−; G)` is represented by the Eilenberg–MacLane space `K(G, n)`, so every natural cohomology operation is a map between such spaces. The Steenrod operations are computed by studying `K(G, n)` instead of every space separately.
- **Presheaves as generalized spaces.** Every presheaf is a colimit of representables (the density theorem), which is where sheaves and toposes start. In a simplicial set `X`, the n-simplices are exactly the maps `Δⁿ → X`, which is the machinery behind UMAP's fuzzy simplicial sets.

Where to read it:
- Smith, *Introducing Category Theory*, [ch. 35](../Deep-Dives/textbooks/smith-introducing-category-theory/ch35): *The Yoneda Embedding, the Yoneda Principle*, pp. 322–324, and *Putting the Yoneda Principle to work*, p. 326 (the proof technique); [ch. 37](../Deep-Dives/textbooks/smith-introducing-category-theory/ch37): *Representable functors* and *More examples of representables*, pp. 336–341; [ch. 41](../Deep-Dives/textbooks/smith-introducing-category-theory/ch41): *Adjunctions and representables*, p. 385; [ch. 42](../Deep-Dives/textbooks/smith-introducing-category-theory/ch42): toposes and their first examples, pp. 397–398
- Riehl, [*Category Theory in Context*](https://math.jhu.edu/~eriehl/context.pdf), ch. 2 (representable functors, the Yoneda lemma, universal properties, the category of elements), with examples from algebra and topology; not yet in the Textbooks library
- Milewski, *CTFP*, [ch. 14 Representable Functors](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch14), pp. 273–279, for the programmer's side of representability
- HoTT book, [ch. 9 › 9.5 The Yoneda lemma](../Deep-Dives/textbooks/hott-book/ch10), pp. 333–336, for the univalent version

**An adjunction says that a function out of what `F` builds is the same as a function into what `G` observes. It is the best approximation to an inverse when no inverse exists.**
`F ⊣ G` means `Hom(F a, b) ≅ Hom(a, G b)`, natural in `a` and `b`. Seven idioms that programmers already use are this one isomorphism:
- **Currying.** `(−, s) ⊣ (s -> −)` gives `((a, s) -> b) ≅ (a -> s -> b)`. The unit `a -> s -> (a, s)` pairs a value with the state, and the counit `(s -> b, s) -> b` is `eval`. Every adjunction yields a monad `G ∘ F` and a comonad `F ∘ G`, and here they are `s -> (a, s)`, the State monad, and `(s -> a, s)`, the Store comonad behind lenses.
- **Free ⊣ forgetful.** A monoid homomorphism `[a] -> m` is the same as a function `a -> m`, which is `foldMap`. One level up, `f ~> m` into a monad extends uniquely to `Free f ~> m`, which is `foldFree`. Free-monad and free-applicative interpreters only need cases for the primitive operations because of this.
- **Products, sums and case analysis.** Products are right adjoint to duplication, `(c -> a, c -> b) ≅ c -> (a, b)`, which is `&&&`. Sums are left adjoint, `(Either a b -> c) ≅ (a -> c, b -> c)`, which is `either`. Pattern matching uses a left adjoint.
- **Quantifiers.** `(exists x. f x) -> r ≅ forall x. (f x -> r)`, which is why consuming an existential means writing a polymorphic function.
- **Laws for free.** Left adjoints preserve sums and right adjoints preserve products, so `(a, Either b c) ≅ Either (a, b) (a, c)` and `s -> (a, b) ≅ (s -> a, s -> b)` need no proof.
- **Galois connections.** Between orders, `x * n ≤ y ⇔ x ≤ y div n` specifies `div` without an algorithm. Mu and Oliveira's *Programming from Galois Connections* calculates programs this way, splitting a specification into an easy adjoint and an optimal one. Abstract interpretation rests on the same idea.
- **Recursion schemes.** Hinze's adjoint folds insert a left adjoint into the recursive equation, which covers accumulating folds, mutumorphisms (and so zygomorphisms) and generalised folds. Adjoint unfolds use a right adjoint.

*Which side carries more information?* Neither, as a rule. "Free" means least information: `[a]` holds nothing but `a` and formal sequences with no equations imposed, so it assumes the least, while `U` keeps the elements and drops the operation. What is lost is measured by the unit `η : a → G(F a)` and the counit `ε : F(G b) → b`. For lists, `a → [a]` adds formal words and `[m] → m` forgets which word produced the element, so a round trip loses something both ways. `G` is fully faithful exactly when the counit is an isomorphism (a reflection), `F` is fully faithful exactly when the unit is (a coreflection), and both together make an equivalence. The free side is not always the richer one:
- The inclusion `ℤ ↪ ℝ` has left adjoint `ceiling` and right adjoint `floor`. The inclusion is lossless and both adjoints lose information.
- The forgetful functor `Top → Set` is right adjoint to discrete spaces and left adjoint to indiscrete ones, so it sits in the middle.
- The direct image `∃f` is left adjoint to preimage and forgets which points mapped where.
- In currying, nothing is forgotten and neither side is free.

The better reading: the left adjoint gives the most general, least constrained solution and preserves colimits (sums, unions, gluing). The right adjoint gives the most complete compatible solution and preserves limits (products, intersections, constraints).

*Fourier and Laplace* are not adjunctions in the interesting sense, but they sit close to three of them.
- **Operator adjoints, where the name comes from.** On `L²(ℝ)`, Plancherel makes Fourier unitary, so `⟨Ff, g⟩ = ⟨f, F⁻¹g⟩`: the inverse transform is the Hilbert-space adjoint. Kan named adjoint functors after `⟨Fx, y⟩ = ⟨x, Gy⟩`. As functors between time-domain and frequency-domain signals, `F` and `F⁻¹` form an adjoint equivalence in both directions, with identity unit and counit. It is a genuine adjunction, but there is nothing to approximate. The Laplace transform on `L²(0, ∞)` is a bounded self-adjoint operator (its kernel `e^{−st}` is symmetric, and its norm is `√π`) with no bounded inverse.
- **A representable duality.** For a locally compact abelian group, `Ĝ = Hom(G, U(1))` is a contravariant representable functor, with the circle in the role `2` plays for powersets. Pontryagin duality makes it an equivalence, and the Fourier transform is its linearization. The convolution theorem says the transform is monoidal, taking convolution to pointwise product. Laplace is the same construction on the monoid `(ℝ≥0, +)`, whose characters `e^{−st}` form a half-plane. Monoids have no Pontryagin duality, so Laplace is injective but not an equivalence, and inverting it takes a contour integral. Mellin is Fourier on the multiplicative group `ℝ>0`.
- **Integral transforms as kernels.** `(Tf)(y) = ∫ K(x, y) f(x) dx` has the transposed kernel as its adjoint. Categorified, the kernel is a span or profunctor, and in algebraic geometry the Fourier–Mukai transform between derived categories has left and right adjoints given by the dual kernel. Mukai's original, for an abelian variety and its dual, is an equivalence.

*In signal processing* the non-trivial adjunctions are the lossy pairs around Fourier:
- Upsampling by inserting zeros is the operator adjoint of downsampling, `⟨↓x, y⟩ = ⟨x, ↑y⟩`, and filter banks and wavelets are built on that pair.
- Inclusion of band-limited signals has the low-pass projection as its adjoint, the least-squares best approximation.
- Sinc reconstruction `R` and sampling `S` satisfy `S ∘ R = id`, and `R ∘ S` is the projection onto band-limited signals. That is a reflection, and Nyquist–Shannon says when nothing is lost.
- The synthesis operators of the short-time Fourier and wavelet transforms are the adjoints of analysis. They are inverses only for tight frames, and a dual frame repairs the gap otherwise.

So Fourier is an adjunction with nothing to gain, and the adjunctions that matter in practice are the lossy ones, which carry the best-approximation guarantees.

Where to read it:
- Milewski, *CTFP*, [ch. 18 Adjunctions](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch18), pp. 313–332 (unit and counit, hom-sets, product and exponential from adjunctions); [ch. 19 Free/Forgetful Adjunctions](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch19), pp. 333–340; [ch. 22 › Monads from Adjunctions](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch22), pp. 398–402
- Smith, *Introducing Category Theory*, [ch. 38 Galois connections](../Deep-Dives/textbooks/smith-introducing-category-theory/ch38), pp. 347–358; [ch. 39 Adjunctions introduced](../Deep-Dives/textbooks/smith-introducing-category-theory/ch39), pp. 359–371, including *Isomorphism, equivalence, adjointness*; [ch. 41 Adjunctions explored](../Deep-Dives/textbooks/smith-introducing-category-theory/ch41), pp. 380–394, including *Adjunctions and fully faithful functors* and *Right adjoints preserve limits*
- Pierce, *Basic Category Theory for Computer Scientists*, [ch. 2 › 2.4 Adjoints](../Deep-Dives/textbooks/pierce-basic-category-theory/ch2), pp. 57–64
- Spivak, *Category Theory for Scientists*, [ch. 5 › 5.1 Adjoint functors](../Deep-Dives/textbooks/spivak-category-theory-for-scientists/ch5), pp. 201–217

Papers: [Hinze, *Adjoint Folds and Unfolds—An Extended Study* (SCP 2013)](https://www.cs.ox.ac.uk/ralf.hinze/publications/SCP-78-11.pdf) · [Hinze and Wu, *Unifying Structured Recursion Schemes: An Extended Study* (JFP 2016)](https://core.ac.uk/download/73982371.pdf) · [Mu and Oliveira, *Programming from Galois Connections* (JLAP 2012)](https://scm.iis.sinica.edu.tw/home/2012/programming-from-galois-connections-2/)

**Kan extensions are the adjoints of precomposition, which is why so many other concepts turn out to be special cases of them.**
Given `D : I → C` and `K : I → A`, the right Kan extension `Ran_K D` is the best functor `F : A → C` with a natural transformation `F ∘ K → D`. The left extension `Lan_K D` has its transformation pointing the other way. The universal property makes `Ran_K` right adjoint to precomposition `− ∘ K`, and `Lan_K` left adjoint. Every universal construction is an adjoint to some kind of restriction, so the named concepts come out of special choices of the inputs:
- `A = 1`: precomposition is then the diagonal `Δ`, so `Ran` is the limit and `Lan` the colimit.
- `D = Id`: `Ran_K Id` is the left adjoint of `K`, provided `K` preserves it.
- `D = K`: `Ran_K K` is the codensity monad. It is a monad for the same reason `x/x` composes with itself.
- `C = Set`: Yoneda gives the end formula `Ran_K D a ≅ ∫_i Set(A(a, K i), D i)`, and a coend for `Lan`. These are Haskell's `Ran` and `Lan`, and the free functor `FreeF` is a `Lan`.

The reverse also holds: Kan extensions are computed by ends, which are limits, so they add no expressive power. What they give is the general statement of the problem. Mac Lane's slogan "all concepts are Kan extensions" gets a rigorous treatment in Riehl's *Category Theory in Context*, ch. 6. The programming payoff is Hinze's *Kan Extensions for Program Optimisation*, which shows that rewriting a program in continuation-passing style is moving it into the codensity monad.
Reading path through CTFP: [limits](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch12) → [Yoneda](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch15) → [adjunctions](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch18) → [ends](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch26) → [Kan extensions](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch27).
[Papers › Category Theory](../Books/Papers#category-theory) · [Math Deep Dives › Books and formalization](../Deep-Dives/math/ch5)

**In a one-object category, Yoneda is Cayley's theorem and Kan extensions are induced representations.**
A group `G` is a category with one object, whose arrows are the group elements. A functor from it to `Set` is a `G`-set, and the hom-functor is `G` acting on itself by left multiplication (the regular action). The two gists above then read as group theory:
- **Yoneda:** a `G`-equivariant map `G → X` is fixed by where it sends `e`. If `e ↦ x`, then `g ↦ g·x`, the orbit map, so `Hom_G(G, X) ≅ X`.
- **Yoneda embedding:** with `X = G`, the equivariant maps `G → G` are the right multiplications, so `G` embeds in the permutations of its own elements. That is Cayley's theorem.
- **Representations:** with vector spaces in place of sets, Yoneda says `Hom_G(k[G], V) ≅ V`, so the group algebra is the free representation on one generator.
- **Kan extensions:** for a subgroup `H ⊆ G`, restricting a representation from `G` to `H` is precomposition. Its left adjoint, the left Kan extension, is induction, and its right adjoint is coinduction. Frobenius reciprocity, `Hom_G(Ind V, W) ≅ Hom_H(V, Res W)`, is that adjunction.

Riehl's preface makes the point directly: Frobenius reciprocity, transitivity of induction and the explicit formula for an induced representation hold for any left Kan extension. Character tables, by contrast, are not formal consequences. Orbit–stabilizer drops out of the same picture: the orbit map factors through `G/Stab(x)`.
References:
- Smith, *Introducing Category Theory*, [ch. 35 The Yoneda Embedding › Yoneda meets Cayley](../Deep-Dives/textbooks/smith-introducing-category-theory/ch35), p. 325
- Spivak, *Category Theory for Scientists*, [ch. 3 › 3.2 Groups](../Deep-Dives/textbooks/spivak-category-theory-for-scientists/ch3), pp. 82–85 (groups and group actions)
- Milewski, *CTFP*, [ch. 3 › Monoid as Category](../Deep-Dives/textbooks/milewski-category-theory-for-programmers/ch3), pp. 56–58
- Riehl, [*Category Theory in Context*](https://math.jhu.edu/~eriehl/context.pdf), ch. 2 (Yoneda) and ch. 6 (Kan extensions), with the preface note on induced representations
- [Wikipedia, Yoneda lemma](https://en.wikipedia.org/wiki/Yoneda_lemma), which calls the lemma a vast generalisation of Cayley's theorem

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
