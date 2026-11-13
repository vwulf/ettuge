# Effects and LLM Systems

Treating model calls as effects: what an algebraic-effects runtime (Kyo, in Scala 3) buys when the program around an LLM has to be bounded, inspectable and cheap.

## Articles

- [Decision Points as Effects](decision-points-as-effects.md) — a cascade for fuzzy decisions (rules, then a small decision model, then a reasoning model), with a cost model in "lines of code" units.

## Deep-dive gists

**λ-RLM turns long-context reasoning into terminating recursion over pre-verified combinators.**
A planner fixes the split factor and leaf size up front. Pure operators (split, map, filter, reduce) then recurse over the prompt, and the model is called only on chunks that fit its window. That gives a strictly decreasing rank, a cost linear in n/τ, power-law rather than exponential accuracy decay, and an optimal split of k = 2. In an effect-typed host, the symbolic/neural separation becomes a compile-time property: a combinator that tries to call the model fails to type-check. Still open: reducing over structured (non-string) results without a second model call, and metering cost across the k^d leaves.
[Papers › Large Language Models](../Books/Papers#large-language-models)

**Recursive Language Models are the open-ended baseline λ-RLM restricts.**
The model loads the prompt into a REPL as a variable and writes its own code to slice it and recurse. That is flexible, but nothing forces each call to shrink its input, so there is no rank function and no termination or cost guarantee. The open question is how much of RLM's flexibility is lost under λ-RLM's fixed operator set, and on which task types that matters.
[Papers › Large Language Models](../Books/Papers#large-language-models)

**Context Language Models win by letting the model rewrite its own context, the opposite bet to λ-RLM.**
Instead of only appending to context, the model edits it in place like a file. Without being told to, it wrote reusable compaction functions, created a private notes role, and kept in-place scoreboards across many subagents. Most of the Suffix Cache Reuse gain comes from stripping reasoning tokens, so it helps ordinary chat serving too. The two approaches can compose, with λ-RLM recursion outside and CLM-style context inside each leaf. Still open: an editable context lets injected or self-written instructions persist across turns.
[Papers › Large Language Models](../Books/Papers#large-language-models)

**DSPy maps onto algebraic effects: signatures become types, modules handlers, optimizers handler rewrites.**
Make `Predict` an effect, and a program's effect row lists statically which model calls it can make, which an optimizer can inspect. Chain-of-thought and ReAct become handlers that rewrite `Predict` into raw completion calls. Optimizers become meta-functions that swap handlers or demonstrations. BootstrapFewShot and MIPROv2 are the first optimizers worth porting. Still open: whether a typed trace can stand in for DSPy's runtime trace collection.
[Papers › Large Language Models](../Books/Papers#large-language-models)

**Learning from use: OpenClaw-RL.** Next-state signals (a user's reply, a tool's output) carry two kinds of information: *evaluative* (did it work, scored by a process-reward judge) and *directive* (how it should have gone, recoverable as token-level hints by on-policy distillation). The idea is sound. Two caveats: the headline 0.17 → 0.81 result is from a simulation, and the reference setup needs eight GPUs.

**Small models as judges: use one judge per failure mode and calibrate each model.** Husain and Saha argue for trained decision models over LLM-as-judge in evals. This is the middle tier of the cascade in [Decision Points as Effects](decision-points-as-effects.md). The guide recommends a separate judge for each failure mode, with a held-out test set kept apart from the folds used to tune thresholds. Platt scaling gave mixed results: it helped some models, slightly hurt OpenAI Decisions and barely changed Jev. Clef Flash was badly miscalibrated: in one bucket it predicted about 8% failures where 60% actually failed. Still open: the evidence comes from one dataset of 98 traces, and Laya was not tested. [Papers › AI and Machine Learning › Applied ML](../Books/Papers#applied-ml)

**A typed decision model gives you marginals, not joints, and that trade is what makes it fast.**
One shared prefill is forked per question, and each answer is scored as a single label token, so every field decodes in parallel. The cost is that there is no chain rule: no `bind`, no `observe`, only independent marginals. So the common "Kleisli arrow" framing does not hold, and whether those marginals fit one joint distribution is the classical compatibility problem (Besag; Arnold & Press). A practical engine uses three tiers: parallel fan-out for independent closed fields (closed sets can be derived from `enum`/`oneOf` schemas), staged binding for discriminated unions, and constrained generation for open types.
[Papers › Large Language Models](../Books/Papers#large-language-models)

**Which language should agents write?** Content-addressed code (Unison) skips rebuilds and re-tests, but it doesn't reduce inference tokens, and a hash says nothing about correctness unless it comes with a strong specification. Token-cost studies put languages with thin training corpora at a measurable disadvantage. Rust benefits from the training-data flywheel, and Lean from being an RL verifier. A plausible split is a control plane (Python, TypeScript, Rust, Go) and a compute plane of embedded array DSLs (JAX, Triton). There JAX turns out to be functional programming's quiet success.

Sources: [Papers › Large Language Models](../Books/Papers#large-language-models), [Papers › Applied ML](../Books/Papers#applied-ml), [Papers › Functional Programming](../Books/Papers#functional-programming).
