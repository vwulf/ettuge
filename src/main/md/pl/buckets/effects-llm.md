# Effects and LLM Systems

Treating model calls as effects: what an algebraic-effects runtime (Kyo, in Scala 3) buys when the program around an LLM has to be bounded, inspectable and cheap.

## Articles

- [Decision Points as Effects](decision-points-as-effects.md) — a cascade for fuzzy decisions (rules, then a small decision model, then a reasoning model), with a cost model in "lines of code" units.

## Deep-dive gists

**λ-RLM: let the planner recurse, not the model.** Roy et al.'s *Y-Combinator for LLMs* attacks long-context rot without letting the model write control code. A deterministic planner applies a fixed set of pre-verified operators (split, map, filter, reduce) over the prompt, and the LM sees only small leaf chunks. These operators map directly onto effect boundaries. `Predict` is the only neural leaf, recursion becomes a terminating handler, and the number of LM calls can be counted statically before anything runs. The paper's cost-optimal split factor (k\* = 2) is a natural seed for optimizer search.

**RLM and Context LMs: two other answers to long context.**
- *Recursive Language Models* (Zhang, Kraska and Khattab) do the opposite of λ-RLM. The prompt is a variable in a Python REPL, and the model writes the code that slices it and calls itself. The approach is more flexible but carries no termination guarantee.
- *Context Language Models* have the model edit its own live context as a file. Suffix Cache Reuse is reported to save about 35% of server compute. Compared with λ-RLM, CLMs move the bookkeeping into the serving stack, not the program.

**DSPy, re-read as effects.** Signatures become typed `Predict` effects, modules become handlers, and teleprompters become meta-programs that swap handlers. BootstrapFewShot and MIPROv2 are the first optimizers worth porting, and Effect.ts's `@effect/ai` is a useful reference design.

**Learning from use: OpenClaw-RL.** Next-state signals (a user's reply, a tool's output) carry two kinds of information: *evaluative* (did it work, scored by a process-reward judge) and *directive* (how it should have gone, recoverable as token-level hints by on-policy distillation). The idea is sound. Two caveats: the headline 0.17 → 0.81 result is from a simulation, and the reference setup needs eight GPUs.

**Small models as judges: use one judge per failure mode and calibrate each model.** Husain and Saha argue for trained decision models over LLM-as-judge in evals. This is the middle tier of the cascade in [Decision Points as Effects](decision-points-as-effects.md). The guide recommends a separate judge for each failure mode, with a held-out test set kept apart from the folds used to tune thresholds. Platt scaling gave mixed results: it helped some models, slightly hurt OpenAI Decisions and barely changed Jev. Clef Flash was badly miscalibrated: in one bucket it predicted about 8% failures where 60% actually failed. Still open: the evidence comes from one dataset of 98 traces, and Laya was not tested. [Papers › AI and Machine Learning › Applied ML](../Books/Papers#applied-ml)

**Which language should agents write?** Content-addressed code (Unison) skips rebuilds and re-tests, but it doesn't reduce inference tokens, and a hash says nothing about correctness unless it comes with a strong specification. Token-cost studies put languages with thin training corpora at a measurable disadvantage. Rust benefits from the training-data flywheel, and Lean from being an RL verifier. A plausible split is a control plane (Python, TypeScript, Rust, Go) and a compute plane of embedded array DSLs (JAX, Triton). There JAX turns out to be functional programming's quiet success.

Sources: [Papers › Large Language Models](../Books/Papers#large-language-models), [Papers › Applied ML](../Books/Papers#applied-ml), [Papers › Functional Programming](../Books/Papers#functional-programming).
