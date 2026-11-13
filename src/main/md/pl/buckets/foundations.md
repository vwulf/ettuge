# Foundations: λ-calculus and types

Where the FP forays keep returning: the untyped λ-calculus, reduction strategies, fixed points, and reading types as specifications.

## Articles

- [ॐλ — Lambda Calculus](om-lambda.md) — reduction strategies (eager/lazy × shallow/deep), the Y combinator, and the detour into parsers that terminate.

## Deep-dive gists

**Reduction is a choice, not a given.** The λ-calculus is equational, so it doesn't fix an evaluation order. The matrix of normal form, weak normal form, head normal form and weak head normal form falls out of two independent choices: whether to reduce under binders, and whether to evaluate arguments first. Most confusion in introductory texts comes from leaving that choice implicit.

**Parsing the calculus you're studying.** Rebuilding the ML PL-zoo interpreters in Scala led to parser combinators: Willis and Wu's *Design Patterns for Parser Combinators* and *Garnishing Parsec with Parsley*. Lesson learned: a natural grammar and a grammar whose parser terminates are often different grammars. Left recursion has to be engineered out.

**Fixed points recur across the site.** The Y combinator gives recursion in the untyped calculus. Traced monoidal categories (see [Algebra and Categories](bucket-algebra-categories.md)) give the abstract account of feedback. λ-RLM's planner (see [Effects and LLM Systems](bucket-effects-llm.md)) uses a bounded, terminating version of the same move to tame long contexts.

Sources: [Papers › Programming Languages and Type Theory](../Books/Papers#programming-languages-and-type-theory), [Papers › Functional Programming](../Books/Papers#functional-programming).
