# Proof and Formalization

Dependent types as a working tool: Lean, mathlib, and the 2026 wave of AI-produced, machine-checked mathematics and software proofs.

## Articles

- [Lean and AI Formalization](lean-ai-formalization.md) — Lean's foundations, the HoTT question, how much math is formalized, consolidation into mathlib, and case studies.

## Deep-dive gists

**The pattern behind the 2026 headlines.** The Unique Games proof, the claimed refutation of the Exponential Time Hypothesis, the Quasi-Riemann zero-free region, Aaronson–Ambainis, and deterministic n^O(log n) graph isomorphism each showed some of the same features:
- a Lean-checked version alongside a shorter unchecked one
- disputes over what exactly was proved (the forced Navier–Stokes claim against the Millennium problem)
- disputes over credit

The statement by 25 Fields medalists on the "severe misalignment" of AI in mathematics argues that announcing famous problems as solved swamps referees and rewards headlines over understanding. Machine checking settles correctness. It doesn't settle significance, readability or attribution.

**Autoformalization at scale moves the bottleneck.** Meta's ATLAS turned 26 open textbooks into 45,000+ verified declarations. Tao's *Analysis I* now has a Lean companion, and his measure-theory text is a formalization target. Proving is no longer the scarce step. Curating is: mathlib stays human-reviewed while staging libraries absorb unreviewed AI output.

**What formalizing category theory teaches.** Carneiro and Riehl's colimits in Cat and the ∞-cosmos blueprint both show that definitions which are routine on paper (size issues, coherence, "the obvious isomorphism") need real design work in a kernel. This is where [Algebra and Categories](bucket-algebra-categories.md) meets the proof assistant.

**Beyond mathematics.** Claude produced machine-checked Rocq proofs for 239 OSS-Fuzz entry points across 123 libraries, reasoning over compiled RISC-V binaries. Verification is reaching deployed code. Statement fidelity, meaning whether the theorem says what you meant, remains the human step.

Sources: [Papers › Foundations and Logic](../Books/Papers#foundations-and-logic), [Papers › Theory of Computation](../Books/Papers#theory-of-computation), [Papers › History of Mathematics](../Books/Papers#history-of-mathematics), [Technical › Analysis and Linear Algebra](../Books/Technical#analysis-and-linear-algebra).
