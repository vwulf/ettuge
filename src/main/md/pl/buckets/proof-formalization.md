# Proof and Formalization

Dependent types as a working tool: Lean, mathlib, and the 2026 wave of AI-produced, machine-checked mathematics and software proofs.

## Articles

- [Lean and AI Formalization](lean-ai-formalization.md) — Lean's foundations, the HoTT question, how much math is formalized, consolidation into mathlib, and case studies.

## Deep-dive gists

**The pattern behind the 2026 headlines.** Several of the year's AI-produced results arrived as a Lean-checked version alongside a shorter unchecked one. Each also came with disputes over what exactly was proved and over credit, and 25 Fields medalists warned that headline races are distorting the field. Machine checking settles correctness. It doesn't settle significance, readability or attribution. The individual results are covered in [Math Deep Dives](../Reflection/math-deep-dives.md).

**Autoformalization at scale moves the bottleneck.** Meta's ATLAS turned 26 open textbooks into 45,000+ verified declarations. Tao's *Analysis I* now has a Lean companion, and his measure-theory text is a formalization target. Proving is no longer the scarce step. Curating is: mathlib stays human-reviewed while staging libraries absorb unreviewed AI output.

**What formalizing category theory teaches.** Carneiro and Riehl's colimits in Cat and the ∞-cosmos blueprint both show that definitions which are routine on paper (size issues, coherence, "the obvious isomorphism") need real design work in a kernel. This is where [Algebra and Categories](bucket-algebra-categories.md) meets the proof assistant.

**Beyond mathematics.** Claude produced machine-checked Rocq proofs for 239 OSS-Fuzz entry points across 123 libraries, reasoning over compiled RISC-V binaries. Verification is reaching deployed code. Statement fidelity, meaning whether the theorem says what you meant, remains the human step.

Sources: [Papers › Foundations and Logic](../Books/Papers#foundations-and-logic), [Papers › Theory of Computation](../Books/Papers#theory-of-computation), [Papers › History of Mathematics](../Books/Papers#history-of-mathematics), [Technical › Analysis and Linear Algebra](../Books/Technical#analysis-and-linear-algebra).
