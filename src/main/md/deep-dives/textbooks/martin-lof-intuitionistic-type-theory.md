<a id="ch1"></a>
# Intuitionistic Type Theory

> Per Martin-Löf · Padua lectures (1980), Bibliopolis 1984, retypeset edition · [the PDF in Drive](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

A short set of lecture notes, one continuous text with numbered topics rather than chapters. Here it is split into its two halves: what the judgements mean, then the rules for each way of forming sets. Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

Martin-Löf lays out a constructive foundation in which propositions are sets, proofs are their elements and elements are programs. The first half explains what it means to judge that something is a set, an element, or equal, starting from canonical elements and the methods that compute them, then extends this to hypothetical judgements and contexts. The second half gives each type former by the same four rules (formation, introduction, elimination, equality): dependent products, dependent sums, finite sets, disjoint union, identity types, natural numbers, lists, well-founded trees and universes. Along the way logic falls out of the types: the axiom of choice becomes provable, and consistency follows from the meaning explanations.

**Contents**

1. [Meaning explanations](ch1): The meaning of the four forms of judgement, from propositions and canonical elements to hypothetical judgements, contexts and the pattern every rule follows.
2. [The set formers](ch2): The type formers, each given by formation, introduction, elimination and equality rules, with the logic and mathematics they encode.


---

## Meaning explanations

*PDF pp. 7–19*

The meaning of the four forms of judgement, from propositions and canonical elements to hypothetical judgements, contexts and the pattern every rule follows.

**Introductory remarks**  
Logic can be symbolism, foundations, or a branch of mathematics; type theory is offered as foundations and doubles as a programming language.  
*Terms:* mathematical logic, foundations  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Propositions and judgements**  
A proposition is something that can be proved; a judgement is the act of asserting something about it. The distinction is central.  
*Terms:* proposition, judgement, assertion  
→ PDF pp. 8–9 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Explanations of the forms of judgement**  
Each judgement form reads four ways: set and element, proposition and proof, intention and fulfillment, problem and solution.  
*Terms:* forms of judgement, propositions as types, BHK interpretation  
→ PDF pp. 10–11 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Propositions**  
A set is given by how its canonical elements are formed and when they are equal; an element is a program that computes a canonical element.  
*Terms:* canonical elements, meaning explanations  
→ PDF pp. 12–13 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Rules of equality**  
Reflexivity, symmetry, transitivity and the set-equality rules, justified directly from the meanings.  
*Terms:* equality rules, transitivity, symmetry  
→ PDF p. 14 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Hypothetical judgements and substitution rules**  
Judgements under one assumption, and the substitution rules that let you plug in elements.  
*Terms:* hypothetical judgement, substitution  
→ PDF p. 15 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Judgements with more than one assumption and contexts**  
Several assumptions form a context, each depending on the earlier ones.  
*Terms:* contexts, dependent assumptions  
→ PDF p. 16 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Sets and categories**  
Families of sets, and the distinction between sets and the larger categories of types.  
*Terms:* families of sets, categories  
→ PDF pp. 17–18 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**General remarks on the rules**  
Every type former is given by four kinds of rule, and each rule is justified by the meaning explanations.  
*Terms:* formation rules, introduction rules, elimination rules, equality rules  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)


---

<a id="ch2"></a>
## The set formers

*PDF pp. 19–57*

The type formers, each given by formation, introduction, elimination and equality rules, with the logic and mathematics they encode.

**Cartesian product of a family of sets**  
The dependent function type Π: λ-abstraction introduces it, application eliminates it, β-equality connects them.  
*Terms:* Pi type, dependent function, lambda abstraction, application  
→ PDF pp. 19–21 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Definitional equality**  
Definitional equality is the equality of names that the system computes with, as opposed to proved equality.  
*Terms:* definitional equality  
→ PDF p. 22 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Applications of the cartesian product**  
Π gives universal quantification, implication and ordinary function spaces; worked derivations of combinators.  
*Terms:* universal quantifier, implication, combinators  
→ PDF pp. 22–25 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Disjoint union of a family of sets**  
The dependent pair type Σ, with pairing and a split eliminator.  
*Terms:* Sigma type, dependent pair  
→ PDF pp. 26–27 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Applications of the disjoint union**  
Σ gives existential quantification, conjunction and Cartesian products; real numbers as sequences paired with proofs.  
*Terms:* existential quantifier, conjunction, Cauchy reals  
→ PDF pp. 28–32 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**The axiom of choice**  
Under this reading of the quantifiers, the axiom of choice is a theorem with a short constructive proof.  
*Terms:* axiom of choice  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**The notion of such that**  
Subsets defined by “such that” are pairs of an element and a proof of the property.  
*Terms:* subset types, such that  
→ PDF p. 34 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Disjoint union of two sets**  
Binary sum A + B with injections and case analysis; it gives disjunction.  
*Terms:* disjoint union, sum type, disjunction  
→ PDF pp. 35–36 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Propositional equality**  
The identity type I(A, a, b) internalizes equality as a set; equality of functions and its limits.  
*Terms:* identity type, propositional equality, function extensionality  
→ PDF pp. 37–40 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Finite sets**  
Finite sets N₀, N₁, N₂ … given outright; N₀ is falsity, N₂ the Booleans with if–then–else.  
*Terms:* finite sets, empty type, Booleans  
→ PDF pp. 41–42 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Consistency**  
Consistency (⊥ is never true) follows from the meaning explanations, though any metamathematical proof leans on a weaker theory.  
*Terms:* consistency  
→ PDF p. 43 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Natural numbers**  
Natural numbers with primitive recursion, which also gives proof by induction.  
*Terms:* natural numbers, primitive recursion, induction  
→ PDF pp. 44–47 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Lists**  
Lists with a recursion operator, defined the same way.  
*Terms:* lists, list recursion  
→ PDF p. 48 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Wellorderings**  
W-types: well-founded trees that give constructive ordinals and transfinite induction.  
*Terms:* W-types, well-orderings, transfinite induction  
→ PDF pp. 49–52 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

**Universes**  
Universes: a set of (codes for) sets, closed under the type formers, so sets can be quantified over.  
*Terms:* universes  
→ PDF pp. 53–57 in [the PDF](https://drive.google.com/file/d/11p7qWzLE-0zW95B_O5sfUNVhoE4AQXXw/view)

