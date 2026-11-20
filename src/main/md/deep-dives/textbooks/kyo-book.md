<a id="ch1"></a>
# Kyo: a book-style guide to the documentation

> Kyo maintainers (Flavio Brasil and contributors) · getkyo.io, documentation for v1.0.0-RC7 (September 2026), Apache 2.0 · [the online book](https://getkyo.io/latest/)

Kyo has no book; its documentation is the set of per-module READMEs published at getkyo.io. This page arranges that documentation like a book, in a suggested reading order: the introduction, the core modules, writing styles, concurrency, testing, then applications. Every section links straight to its heading on getkyo.io (the latest release). Terms under each section are its sub-headings in the docs. Summaries are in our own words.

## The book in one paragraph

Kyo is a Scala 3 toolkit built on algebraic effects. A computation has type A < S: it produces an A once every effect in the row S has been handled, and S is an intersection type, so effects combine in any order and each handler removes one. Pure effects (Abort, Env, Var, Choice, Emit, Stream) live in kyo-prelude; kyo-core adds Sync, Async, fibers, Scope and concurrency primitives; kyo-kernel exposes the machinery (ArrowEffect, ContextEffect, handlers with continuations) for writing new effects. Around that core sit direct-style and combinator dialects, STM and actors, a work-stealing scheduler, a test framework, derived schemas, HTTP, typed LLM programs (kyo-ai) and bridges to ZIO and other runtimes.

**Contents**

1. [Introduction: the pending type](ch1): How Kyo programs are shaped: the type A < S (a result A still owing the effects in S), the single import, composing with map/flatMap/for, sequential versus parallel collection operations, what an effect and its handler look like, and why the order you handle effects in changes the result.
2. [kyo-data: low-allocation values](ch2): The value types everything else returns: Maybe instead of Option, Result instead of Either/Try, Chunk and Span for sequences, Dict, durations, instants and schedules, typed records, type tags and rendering.
3. [kyo-prelude: pure effects and handlers](ch3): The pure, handler-based effects: Abort for typed failure, Env and Local for dependencies and context, Var for state, Choice for non-determinism, Emit/Poll and Stream for streaming, Memo, validation, batching and aspects.
4. [kyo-core: Sync, Async and the fiber runtime](ch4): The runtime layer: Sync for suspended side effects, Async for fibers, races and structured cancellation, KyoApp as the entry point; Scope for resources; channels, queues and hubs between fibers; latches, gates, meters, admission control and signals for coordination; atomics and caches; clocks, retries, timeouts and schedules; files and processes; console, random and logging; metrics and stream bridges.
5. [kyo-kernel: how effects are built](ch5): For effect authors: the pending type itself, declaring effects with ArrowEffect (an operation takes an input and is answered with an output) and ContextEffect (a value bound around the computation), answering them with handlers that hold the continuation (and may resume it more than once), failure and brackets at the kernel level, loops, Isolate for carrying effect state across execution boundaries, and Mask for hiding an effect from inner handlers.
6. [kyo-direct: direct style](ch6): Write effectful code as straight-line Scala inside direct { … }, marking each effect with .now (or .later); a macro rewrites it into flatMap chains.
7. [kyo-combinators: fluent operators](ch7): ZIO-style postfix operators over the existing effects: constructing computations, sequencing and zipping, repetition, error handling and narrowing with forAbort, optional values, forking, Choice, streaming conversions, resources and Env.
8. [kyo-stm: software transactional memory](ch8): Transactional references and collections (TRef, TMap, TChunk, TTable), running and retrying transactions, what effects are allowed inside one, low-level escape hatches, and what happens when a transaction gives up.
9. [kyo-actor: typed actors](ch9): Actors as receive loops over a private mailbox: defining behaviour, starting and messaging them, ask, Subjects as any message sink, supervision by composition, publish/subscribe, request/reply, a worker-pool dispatcher, and a worked bank example.
10. [kyo-scheduler: the work-stealing scheduler](ch10): The standalone scheduler under Kyo’s fibers: time-sliced cooperative tasks, admission control under overload, blocking detection that grows the pool, tuning, Loom and virtual threads, monitoring, and extension points.
11. [kyo-test: testing](ch11): Kyo’s own test framework: suites as trees of groups and leaves whose bodies are Kyo computations, assertions, decorators, setup, property-based and snapshot testing, mandatory assertions, and build wiring.
12. [kyo-schema: derived schemas](ch12): One derives Schema gives serialization (JSON, YAML, Protobuf, MessagePack and more), validation, lenses, reshaping, structural conversion, diffs, builders, ordering and introspection; usable standalone on top of kyo-data.
13. [kyo-http: HTTP client and server](ch13): A cross-platform HTTP client and server with typed routes, error handling, WebSockets, OpenAPI generated from and into routes, feature flags over HTTP, and migration from kyo-sttp and kyo-tapir.
14. [kyo-ai: typed LLM programs](ch14): LLM calls as typed values: the LLM/AI/Agent trio, one-shot and typed generation, instances that keep a conversation, tools with an automatic call loop, prompts, thoughts and modes, long-lived agents, streaming, decisions, parallel generation, usage tracking, conversation state, providers, and how it works inside.
15. [kyo-zio: ZIO interop](ch15): Moving between Kyo and ZIO: lifting and running effects in both directions, ZStream interop, ZLayer interop, and how failures and interruption translate.
16. [More modules](ch16): The rest of the ecosystem, one page each on getkyo.io: system access, SQL drivers, schema codecs, config and feature flags, durable workflows, UI, i18n, GraphQL, parsing, containers, chat bots, browser automation, JSON-RPC, MCP and LSP, networking, FFI, TASTy, observability, compatibility bridges, and scheduler drop-ins for ZIO, Pekko and Finagle.


---

## Introduction: the pending type

How Kyo programs are shaped: the type A < S (a result A still owing the effects in S), the single import, composing with map/flatMap/for, sequential versus parallel collection operations, what an effect and its handler look like, and why the order you handle effects in changes the result. Also platforms, the translation table for ZIO and Cats Effect users, and using Kyo’s scheduler under other runtimes.

getkyo.io: [Overview](https://getkyo.io/latest/)

**Getting Started**  
→ [read online](https://getkyo.io/latest/#getting-started)

**The pending type**  
→ [read online](https://getkyo.io/latest/#the-pending-type)

**Imports: all you need is import kyo.***  
→ [read online](https://getkyo.io/latest/#imports-all-you-need-is-import-kyo)

**Composing computations: map, flatMap, and for**  
→ [read online](https://getkyo.io/latest/#composing-computations-map-flatmap-and-for)

**Composing many computations: sequential vs parallel**  
→ [read online](https://getkyo.io/latest/#composing-many-computations-sequential-vs-parallel)

**The shape of an effect**  
→ [read online](https://getkyo.io/latest/#the-shape-of-an-effect)

**Effect ordering**  
→ [read online](https://getkyo.io/latest/#effect-ordering)

**Idiomatic style: monadic by default**  
→ [read online](https://getkyo.io/latest/#idiomatic-style-monadic-by-default)

**Platforms**  
→ [read online](https://getkyo.io/latest/#platforms)

**Coming from ZIO or Cats Effect**  
→ [read online](https://getkyo.io/latest/#coming-from-zio-or-cats-effect)

**Drop-in scheduler for ZIO, Pekko, Finagle**  
→ [read online](https://getkyo.io/latest/#drop-in-scheduler-for-zio-pekko-finagle)


---

<a id="ch2"></a>
## kyo-data: low-allocation values

The value types everything else returns: Maybe instead of Option, Result instead of Either/Try, Chunk and Span for sequences, Dict, durations, instants and schedules, typed records, type tags and rendering. Opaque types keep them allocation-free; usable without the effect system.

getkyo.io: [kyo-data](https://getkyo.io/latest/kyo-data/)

**Portable path matching**  
→ [read online](https://getkyo.io/latest/kyo-data/#portable-path-matching)

**Optional and fallible values**  
  
*Terms:* Working with optional values, Modeling success and failure, Pattern matching on the result, Recovering from specific errors, Narrowing to expected failures only  
→ [read online](https://getkyo.io/latest/kyo-data/#optional-and-fallible-values)

**Sequences, maps, and identifiers**  
  
*Terms:* Slicing without copying, Storing primitives without boxing, Chunk vs Span: when to use which, Mapping keys to values, Building incrementally, Binary-to-text encoding, Identifiers and UUIDs  
→ [read online](https://getkyo.io/latest/kyo-data/#sequences-maps-and-identifiers)

**Time and scheduling**  
  
*Terms:* Time spans, Points in time, Retry and periodic policies  
→ [read online](https://getkyo.io/latest/kyo-data/#time-and-scheduling)

**Storage sizes**  
→ [read online](https://getkyo.io/latest/kyo-data/#storage-sizes)

**Records and named fields**  
  
*Terms:* Building a record, Records from case classes, Updating, mapping, and zipping, Reified field descriptors, Compile-time staging per field, Library-author tooling  
→ [read online](https://getkyo.io/latest/kyo-data/#records-and-named-fields)

**Type identity at runtime**  
  
*Terms:* Compile-time-derived tags, Union- and intersection-aware tags, Array element tags, Choosing a tag, Heterogeneous maps, Compile-time literals as runtime values, Rejecting intersection types in evidence  
→ [read online](https://getkyo.io/latest/kyo-data/#type-identity-at-runtime)

**Rendering and formatting**  
  
*Terms:* Customizable rendering, Terminal color and formatting  
→ [read online](https://getkyo.io/latest/kyo-data/#rendering-and-formatting)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-data/#putting-it-together)

**Reading values from configuration**  
→ [read online](https://getkyo.io/latest/kyo-data/#reading-values-from-configuration)

**Call-site context and exceptions**  
  
*Terms:* Compile-time-captured source position, Exceptions with frame context  
→ [read online](https://getkyo.io/latest/kyo-data/#call-site-context-and-exceptions)


---

<a id="ch3"></a>
## kyo-prelude: pure effects and handlers

The pure, handler-based effects: Abort for typed failure, Env and Local for dependencies and context, Var for state, Choice for non-determinism, Emit/Poll and Stream for streaming, Memo, validation, batching and aspects. Each handler (Abort.run, Env.run, Var.run …) removes its effect from the row, which is the algebraic-effects picture in practice.

getkyo.io: [kyo-prelude](https://getkyo.io/latest/kyo-prelude/)

**Failure and recovery**  
  
*Terms:* Declaring a failure, Lifting standard types, Handling failure: run, recover, fold, Run variants that drop panic, Recover-only-failure vs fold-and-rethrow, Observing a failure without consuming it, Singleton-typed errors  
→ [read online](https://getkyo.io/latest/kyo-prelude/#failure-and-recovery)

**Dependencies**  
  
*Terms:* Reading the environment, Providing values directly, Wiring with layers  
→ [read online](https://getkyo.io/latest/kyo-prelude/#dependencies)

**Contextual values**  
  
*Terms:* Inheritable vs non-inheritable, Scoped override and update  
→ [read online](https://getkyo.io/latest/kyo-prelude/#contextual-values)

**Mutable state**  
  
*Terms:* Discharging state: run vs runTuple, Isolation strategies  
→ [read online](https://getkyo.io/latest/kyo-prelude/#mutable-state)

**Branching computations**  
  
*Terms:* Introducing branches, Killing a branch, Collect all vs stream  
→ [read online](https://getkyo.io/latest/kyo-prelude/#branching-computations)

**Streaming**  
  
*Terms:* Building a stream, Transforming, Composing streams: zip, concat, into, Consuming: run, fold, foreach, Threading effects through a stream: handle, Reusable transducers: Pipe, Reusable consumers: Sink, Low-level: Emit and Poll, Isolation strategies for streaming effects  
→ [read online](https://getkyo.io/latest/kyo-prelude/#streaming)

**Memoization**  
→ [read online](https://getkyo.io/latest/kyo-prelude/#memoization)

**Validation**  
→ [read online](https://getkyo.io/latest/kyo-prelude/#validation)

**Batching**  
→ [read online](https://getkyo.io/latest/kyo-prelude/#batching)

**Aspect-oriented interception**  
→ [read online](https://getkyo.io/latest/kyo-prelude/#aspect-oriented-interception)

**Sequencing collections over any effect: Kyo.***  
→ [read online](https://getkyo.io/latest/kyo-prelude/#sequencing-collections-over-any-effect-kyo)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-prelude/#putting-it-together)


---

<a id="ch4"></a>
## kyo-core: Sync, Async and the fiber runtime

The runtime layer: Sync for suspended side effects, Async for fibers, races and structured cancellation, KyoApp as the entry point; Scope for resources; channels, queues and hubs between fibers; latches, gates, meters, admission control and signals for coordination; atomics and caches; clocks, retries, timeouts and schedules; files and processes; console, random and logging; metrics and stream bridges.

getkyo.io: [kyo-core](https://getkyo.io/latest/kyo-core/)

**From values to programs: Sync, Async, and KyoApp**  
  
*Terms:* Suspending side effects with Sync, Adding fibers with Async, Running an application  
→ [read online](https://getkyo.io/latest/kyo-core/#from-values-to-programs-sync-async-and-kyoapp)

**Structured concurrency**  
  
*Terms:* First success vs first finish, Gathering bounded successful results, Bounded-concurrency collection ops, Parallel n-way join, Explicit fibers (advanced)  
→ [read online](https://getkyo.io/latest/kyo-core/#structured-concurrency)

**Resource safety**  
  
*Terms:* Choosing the tool, acquireRelease, acquire, and ensure, Closing a scope, Fibers and scopes, Where the guarantee starts and stops  
→ [read online](https://getkyo.io/latest/kyo-core/#resource-safety)

**Talking between fibers**  
  
*Terms:* Bounded MPMC buffers, Lock-free queues with overflow policies, Broadcast fan-out, ID-multiplexed request/response (advanced)  
→ [read online](https://getkyo.io/latest/kyo-core/#talking-between-fibers)

**Coordinating work**  
  
*Terms:* Latch: asymmetric countdown, Gate: symmetric multi-party barrier, Meter: mutex, semaphore, rate limiter, Admission: load shedding at the boundary, Signal: reactive value with change streams  
→ [read online](https://getkyo.io/latest/kyo-core/#coordinating-work)

**Shared mutable state**  
  
*Terms:* Atomic primitives, Contention-optimized counters, Bounded caches and memoization  
→ [read online](https://getkyo.io/latest/kyo-core/#shared-mutable-state)

**Time, deadlines, retries**  
  
*Terms:* Clock.now vs Clock.nowMonotonic, Measuring elapsed time and tracking deadlines, Scheduling recurring work, Deterministic time for tests, Retry, Timeout  
→ [read online](https://getkyo.io/latest/kyo-core/#time-deadlines-retries)

**Files, processes, and the OS**  
→ [read online](https://getkyo.io/latest/kyo-core/#files-processes-and-the-os)

**Ambient services**  
  
*Terms:* Console, UUID generation, Random, Log  
→ [read online](https://getkyo.io/latest/kyo-core/#ambient-services)

**Cross-cutting errors**  
→ [read online](https://getkyo.io/latest/kyo-core/#cross-cutting-errors)

**Metrics and stream bridges**  
  
*Terms:* Stat: metrics registry, StreamCoreExtensions, StreamCompression (JVM only)  
→ [read online](https://getkyo.io/latest/kyo-core/#metrics-and-stream-bridges)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-core/#putting-it-together)

**Low-level extension points**  
→ [read online](https://getkyo.io/latest/kyo-core/#low-level-extension-points)


---

<a id="ch5"></a>
## kyo-kernel: how effects are built

For effect authors: the pending type itself, declaring effects with ArrowEffect (an operation takes an input and is answered with an output) and ContextEffect (a value bound around the computation), answering them with handlers that hold the continuation (and may resume it more than once), failure and brackets at the kernel level, loops, Isolate for carrying effect state across execution boundaries, and Mask for hiding an effect from inner handlers. Read alongside Plotkin–Pretnar and Leijen in this library.

getkyo.io: [kyo-kernel](https://getkyo.io/latest/kyo-kernel/)

**A < S: the pending type**  
  
*Terms:* Composing computations, Plain values are computations already, Nesting, and flatten, Running, Printing  
→ [read online](https://getkyo.io/latest/kyo-kernel/#a-s-the-pending-type)

**Declaring an effect**  
  
*Terms:* ArrowEffect: operations with an input and an answer, An effect whose operations answer at different types, ContextEffect: a value bound around the computation  
→ [read online](https://getkyo.io/latest/kyo-kernel/#declaring-an-effect)

**Answering an effect**  
  
*Terms:* handleCont: the continuation in hand, handleContRepeated: applying the continuation more than once, handleLoop: one answer per occurrence, handleLoopState: carrying state between occurrences, Performing effects while handling, The *With variants: fusing the region's continuation, ContextEffect.handle: binding a value for a scope, handle: reading a stack of handlers left to right, Arrow: a transformation you can hold, head and tail: why an arrow exposes its own composition, Region.NoEscape: the continuation cannot leave its region  
→ [read online](https://getkyo.io/latest/kyo-kernel/#answering-an-effect)

**Failure and resources**  
  
*Terms:* Recovery is a clause, not a wrapper, ensureMap: no gap between a value and what it owes, Bracket: acquire, use, release, A released scope, entered again, EffectTrace: what a failure carries out  
→ [read online](https://getkyo.io/latest/kyo-kernel/#failure-and-resources)

**Iteration**  
  
*Terms:* Loop: the general loops, Loop.Outcome: what a round answers with, The shapes that need no state  
→ [read online](https://getkyo.io/latest/kyo-kernel/#iteration)

**Sequential collection operations**  
  
*Terms:* Mapping over a collection, Selecting and folding, Splitting and branching, The collection types, and where the concurrent variants live  
→ [read online](https://getkyo.io/latest/kyo-kernel/#sequential-collection-operations)

**Isolate: crossing an execution boundary**  
  
*Terms:* The three type parameters, The three phases, run: the three phases composed, nest: holding the restore back, Composing and obtaining instances, What the bindings themselves decide  
→ [read online](https://getkyo.io/latest/kyo-kernel/#isolate-crossing-an-execution-boundary)

**Mask: hiding an effect from inner handlers**  
→ [read online](https://getkyo.io/latest/kyo-kernel/#mask-hiding-an-effect-from-inner-handlers)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-kernel/#putting-it-together)


---

<a id="ch6"></a>
## kyo-direct: direct style

Write effectful code as straight-line Scala inside direct { … }, marking each effect with .now (or .later); a macro rewrites it into flatMap chains. Covers what the macro rejects and why, higher-order calls, and its error messages.

getkyo.io: [kyo-direct](https://getkyo.io/latest/kyo-direct/)

**Writing effects in direct style**  
  
*Terms:* direct, .now, .later  
→ [read online](https://getkyo.io/latest/kyo-direct/#writing-effects-in-direct-style)

**What direct rejects, and what to use instead**  
  
*Terms:* Bare T < S as a statement, Shared mutable state, One-shot caching and memoization, def containing .now, Catching and raising failures, Thread coordination, Nested class / trait / object  
→ [read online](https://getkyo.io/latest/kyo-direct/#what-direct-rejects-and-what-to-use-instead)

**Higher-order calls and lazy structures**  
  
*Terms:* Shift-aware methods, Lazy structures: Stream  
→ [read online](https://getkyo.io/latest/kyo-direct/#higher-order-calls-and-lazy-structures)

**Error diagnostics**  
→ [read online](https://getkyo.io/latest/kyo-direct/#error-diagnostics)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-direct/#putting-it-together)

**Cross-platform**  
→ [read online](https://getkyo.io/latest/kyo-direct/#cross-platform)


---

<a id="ch7"></a>
## kyo-combinators: fluent operators

ZIO-style postfix operators over the existing effects: constructing computations, sequencing and zipping, repetition, error handling and narrowing with forAbort, optional values, forking, Choice, streaming conversions, resources and Env.

getkyo.io: [kyo-combinators](https://getkyo.io/latest/kyo-combinators/)

**Construction**  
  
*Terms:* Lifting plain values and side-effects, Async primitives, Lifting standard-library types, Resource lifecycle (constructing the resource), Env constructors (reading dependencies), Parallel fan-out, Emit and Poll, Logging  
→ [read online](https://getkyo.io/latest/kyo-combinators/#construction)

**Sequencing and combining**  
  
*Terms:* Sequential zip: *>, <*, <*>, tap: side-effect on the success value, when / unless: conditional execution  
→ [read online](https://getkyo.io/latest/kyo-combinators/#sequencing-and-combining)

**Repetition**  
  
*Terms:* repeat: by count or schedule, repeatWhile / repeatUntil: predicate-driven, forever: infinite repetition, delay: postpone before running  
→ [read online](https://getkyo.io/latest/kyo-combinators/#repetition)

**Error handling**  
  
*Terms:* result: handle to a Result, recover and recoverSome: replace failures, foldAbort / foldAbortOrThrow: fold over outcome, mapAbort and swapAbort: transform the error type, orPanic / orThrow / unpanic: collapse to panic or back, abortToChoiceDrop, abortToAbsent, abortToThrowable: route to other effects, retry: re-run on failure, forAbort[E1]: handle one branch of a union, PanicException: the panic wrapper  
→ [read online](https://getkyo.io/latest/kyo-combinators/#error-handling)

**Optionality (Absent)**  
  
*Terms:* maybe: handle to Maybe[A], Routing absence to other effects  
→ [read online](https://getkyo.io/latest/kyo-combinators/#optionality-absent)

**Concurrency and forking**  
  
*Terms:* fork, forkUnscoped, forkUsing, Parallel zip: &>, <&, <&>, Fiber#join and Fiber#await  
→ [read online](https://getkyo.io/latest/kyo-combinators/#concurrency-and-forking)

**Non-determinism (Choice)**  
  
*Terms:* handleChoice: handle to Seq[A], filterChoice: drop branches by predicate, choiceDropToAbsent, choiceDropToThrowable, choiceDropToFailure  
→ [read online](https://getkyo.io/latest/kyo-combinators/#non-determinism-choice)

**Emit, streaming, and conversion**  
  
*Terms:* handleEmit, handleEmitDiscarding, foreachEmit, emitToChannel: pipe to a Channel[A], emitChunked: re-emit as chunks, Convert to Stream, unwrapStream: flatten an effectful stream  
→ [read online](https://getkyo.io/latest/kyo-combinators/#emit-streaming-and-conversion)

**Resource lifecycle**  
  
*Terms:* ensuring and ensuringError  
→ [read online](https://getkyo.io/latest/kyo-combinators/#resource-lifecycle)

**Dependency injection (Env)**  
  
*Terms:* provideValue and Kyo.provideFor: supply a single dependency, provideLayer: supply via a Layer, provide: supply all required Env with multiple layers  
→ [read online](https://getkyo.io/latest/kyo-combinators/#dependency-injection-env)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-combinators/#putting-it-together)


---

<a id="ch8"></a>
## kyo-stm: software transactional memory

Transactional references and collections (TRef, TMap, TChunk, TTable), running and retrying transactions, what effects are allowed inside one, low-level escape hatches, and what happens when a transaction gives up.

getkyo.io: [kyo-stm](https://getkyo.io/latest/kyo-stm/)

**Transactional references**  
  
*Terms:* TRef: single-cell state, TRef.initWith: allocate and use in one shot, TMap: keyed state with per-value concurrency, TChunk: transactional sequence, TTable: record store with auto IDs, TTable.Indexed: compile-time-checked queries  
→ [read online](https://getkyo.io/latest/kyo-stm/#transactional-references)

**Running a transaction**  
  
*Terms:* STM.run: commit a transaction, STM.run: custom retry schedule, STM.retry and STM.retryIf: abort and reschedule, Nested STM.run  
→ [read online](https://getkyo.io/latest/kyo-stm/#running-a-transaction)

**What may run inside a transaction**  
  
*Terms:* Side effects: after commit, not inside, Isolate requirement, Anti-starvation: barging  
→ [read online](https://getkyo.io/latest/kyo-stm/#what-may-run-inside-a-transaction)

**Low-level escape hatches**  
  
*Terms:* TRef.Unsafe.init: allocate outside any orchestration  
→ [read online](https://getkyo.io/latest/kyo-stm/#low-level-escape-hatches)

**When a transaction gives up**  
  
*Terms:* FailedTransaction  
→ [read online](https://getkyo.io/latest/kyo-stm/#when-a-transaction-gives-up)


---

<a id="ch9"></a>
## kyo-actor: typed actors

Actors as receive loops over a private mailbox: defining behaviour, starting and messaging them, ask, Subjects as any message sink, supervision by composition, publish/subscribe, request/reply, a worker-pool dispatcher, and a worked bank example.

getkyo.io: [kyo-actor](https://getkyo.io/latest/kyo-actor/)

**Defining an actor's behavior**  
  
*Terms:* Actor.receiveAll: run until the mailbox closes, Actor.receiveMax: process a fixed count, then return, Actor.receiveLoop (no state), Actor.receiveLoop with state, Actor.Context[A]  
→ [read online](https://getkyo.io/latest/kyo-actor/#defining-an-actor-s-behavior)

**Starting and driving an actor**  
  
*Terms:* Actor.run, Actor.defaultCapacity: the bounded mailbox (default 128), The Actor[E, A, B] handle, send, trySend, ask  
→ [read online](https://getkyo.io/latest/kyo-actor/#starting-and-driving-an-actor)

**Talking to other actors and to yourself**  
  
*Terms:* Actor.self and Actor.selfWith, Actor.reenqueue, Subject#ask: a one-shot reply channel per request  
→ [read online](https://getkyo.io/latest/kyo-actor/#talking-to-other-actors-and-to-yourself)

**Subjects: anything that receives messages**  
  
*Terms:* Actor.Subject.noop, Actor.Subject.init(promise), Actor.Subject.init(channel), Actor.Subject.init(queue), Actor.Subject.init(send, trySend)  
→ [read online](https://getkyo.io/latest/kyo-actor/#subjects-anything-that-receives-messages)

**Supervision and lifecycle**  
  
*Terms:* Parent-child scope inheritance, Closing an actor, Supervision is handler composition, not a strategy API  
→ [read online](https://getkyo.io/latest/kyo-actor/#supervision-and-lifecycle)

**Publish/Subscribe**  
→ [read online](https://getkyo.io/latest/kyo-actor/#publish-subscribe)

**PubSub: push-based publish/subscribe**  
  
*Terms:* PubSub.init: plain concurrent fan-out, PubSub.linearized: total order across subscribers, Subject.contramap: subscribing an actor with a sum message type, PubSub API summary  
→ [read online](https://getkyo.io/latest/kyo-actor/#pubsub-push-based-publish-subscribe)

**Request/Reply**  
→ [read online](https://getkyo.io/latest/kyo-actor/#request-reply)

**Job dispatcher with a worker pool**  
→ [read online](https://getkyo.io/latest/kyo-actor/#job-dispatcher-with-a-worker-pool)

**Worked example: a bank, step by step**  
  
*Terms:* Stage 0: a single account actor, Stage 1: concurrent ATM clients, Stage 2: observe transactions with a PubSub, Stage 3: a second observer via contramap, Stage 4: consistent order across observers with PubSub.linearized  
→ [read online](https://getkyo.io/latest/kyo-actor/#worked-example-a-bank-step-by-step)


---

<a id="ch10"></a>
## kyo-scheduler: the work-stealing scheduler

The standalone scheduler under Kyo’s fibers: time-sliced cooperative tasks, admission control under overload, blocking detection that grows the pool, tuning, Loom and virtual threads, monitoring, and extension points.

getkyo.io: [kyo-scheduler](https://getkyo.io/latest/kyo-scheduler/)

**Getting started**  
  
*Terms:* Submitting a task, Bridging to standard executors  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#getting-started)

**Cooperative tasks and time slicing**  
  
*Terms:* A custom Task, Yield hooks, Opting in to interruption  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#cooperative-tasks-and-time-slicing)

**Admission control**  
  
*Terms:* Random rejection, Keyed rejection (sticky within a rotation window), Random vs keyed: when to use which, Reading the current admission percentage  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#admission-control)

**Adaptive concurrency and blocking compensation**  
  
*Terms:* Triggering an immediate scan  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#adaptive-concurrency-and-blocking-compensation)

**Configuration and tuning**  
  
*Terms:* Scheduler-wide config, Constructing a non-singleton scheduler  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#configuration-and-tuning)

**Loom and virtual threads**  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#loom-and-virtual-threads)

**Monitoring (kyo-scheduler top)**  
  
*Terms:* Rendering as a table, Exposing the status via JMX, Periodic console dump in-process  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#monitoring-kyo-scheduler-top)

**Lifecycle and ops**  
  
*Terms:* flush(), shutdown(), flush() vs shutdown(), Cross-classloader singletons  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#lifecycle-and-ops)

**Cross-platform notes**  
  
*Terms:* Scala.js, Scala Native  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#cross-platform-notes)

**Extending the scheduler**  
  
*Terms:* Thread factories, Self-check harness  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#extending-the-scheduler)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-scheduler/#putting-it-together)


---

<a id="ch11"></a>
## kyo-test: testing

Kyo’s own test framework: suites as trees of groups and leaves whose bodies are Kyo computations, assertions, decorators, setup, property-based and snapshot testing, mandatory assertions, and build wiring.

getkyo.io: [kyo-test](https://getkyo.io/latest/kyo-test/)

**Writing a suite**  
  
*Terms:* Test[S] and the baseline, Groups (-) and leaves (in): two operators, no inference  
→ [read online](https://getkyo.io/latest/kyo-test/#writing-a-suite)

**Assertions**  
  
*Terms:* assert: the power-assert, fail, cancel, and assume: steering the outcome, intercept: expected exceptions, assertEventually: eventual consistency, typeCheck: compile-time assertions, Asserting inside a helper: AssertScope  
→ [read online](https://getkyo.io/latest/kyo-test/#assertions)

**Decorating tests**  
  
*Terms:* Selection: focus, ignore, only, tagged, slow, Lifecycle: pendingUntilFixed, Resilience and timing: timeout, retry, flaky, times, Platform: jvm/js/native/wasm, notX, onlyX  
→ [read online](https://getkyo.io/latest/kyo-test/#decorating-tests)

**Per-test and per-suite setup**  
  
*Terms:* .handle: discharge an extra effect, aroundLeaf and the suite hooks  
→ [read online](https://getkyo.io/latest/kyo-test/#per-test-and-per-suite-setup)

**Property-based testing**  
  
*Terms:* Gen: generators with shrinking, Shrink: custom generators  
→ [read online](https://getkyo.io/latest/kyo-test/#property-based-testing)

**Write meaningful tests: no-assertion enforcement**  
→ [read online](https://getkyo.io/latest/kyo-test/#write-meaningful-tests-no-assertion-enforcement)

**Snapshot testing**  
  
*Terms:* assertSchemaSnapshot: schema-based snapshots, assertGoldenSnapshot: golden snapshots over a generated spread  
→ [read online](https://getkyo.io/latest/kyo-test/#snapshot-testing)

**Running and selecting tests**  
  
*Terms:* CLI flags, RunConfig, TestFilter, Verbosity: the programmatic equivalents, Outcomes and counters, Reporters  
→ [read online](https://getkyo.io/latest/kyo-test/#running-and-selecting-tests)

**Build wiring**  
→ [read online](https://getkyo.io/latest/kyo-test/#build-wiring)


---

<a id="ch12"></a>
## kyo-schema: derived schemas

One derives Schema gives serialization (JSON, YAML, Protobuf, MessagePack and more), validation, lenses, reshaping, structural conversion, diffs, builders, ordering and introspection; usable standalone on top of kyo-data. Also what kyo-ai uses to derive JSON schemas for typed LLM results.

getkyo.io: [kyo-schema](https://getkyo.io/latest/kyo-schema/)

**Module layout**  
→ [read online](https://getkyo.io/latest/kyo-schema/#module-layout)

**Installation**  
→ [read online](https://getkyo.io/latest/kyo-schema/#installation)

**Schemas: the single source of truth**  
→ [read online](https://getkyo.io/latest/kyo-schema/#schemas-the-single-source-of-truth)

**Serialization**  
  
*Terms:* JSON, Ion, BSON, YAML, Protobuf, MsgPack, Built-in Types, Custom Types, Validating smart constructors  
→ [read online](https://getkyo.io/latest/kyo-schema/#serialization)

**Annotations**  
  
*Terms:* Renaming and aliases, Omitting fields, Sum representations, Custom field codecs, Protobuf field numbers, Reading annotations back  
→ [read online](https://getkyo.io/latest/kyo-schema/#annotations)

**Validation**  
  
*Terms:* Constraints, Custom Checks, Running Validation, JSON Schema, Ion Schema  
→ [read online](https://getkyo.io/latest/kyo-schema/#validation)

**Navigation and lenses**  
  
*Terms:* Reading and writing one field, Navigating into collections, Walking every field, Metadata Accessors  
→ [read online](https://getkyo.io/latest/kyo-schema/#navigation-and-lenses)

**Reshaping schemas**  
  
*Terms:* drop / rename / add / select / flatten, Serializing transformed schemas, Per-field wire transforms  
→ [read online](https://getkyo.io/latest/kyo-schema/#reshaping-schemas)

**Type Conversion**  
  
*Terms:* Transform-aware Conversion  
→ [read online](https://getkyo.io/latest/kyo-schema/#type-conversion)

**Comparison and Mutation**  
  
*Terms:* Comparing two values, Batching mutations, Diffs as data  
→ [read online](https://getkyo.io/latest/kyo-schema/#comparison-and-mutation)

**Constructing values with Builder**  
→ [read online](https://getkyo.io/latest/kyo-schema/#constructing-values-with-builder)

**Ordering and Equality**  
→ [read online](https://getkyo.io/latest/kyo-schema/#ordering-and-equality)

**Structural Introspection**  
  
*Terms:* Docs, examples, deprecation, The runtime type and value trees  
→ [read online](https://getkyo.io/latest/kyo-schema/#structural-introspection)

**Custom Formats**  
  
*Terms:* The Codec trait, The event model, A minimal codec, Safety limits  
→ [read online](https://getkyo.io/latest/kyo-schema/#custom-formats)

**Exceptions**  
→ [read online](https://getkyo.io/latest/kyo-schema/#exceptions)

**Putting it together**  
→ [read online](https://getkyo.io/latest/kyo-schema/#putting-it-together)

**Cross-platform behavior**  
→ [read online](https://getkyo.io/latest/kyo-schema/#cross-platform-behavior)


---

<a id="ch13"></a>
## kyo-http: HTTP client and server

A cross-platform HTTP client and server with typed routes, error handling, WebSockets, OpenAPI generated from and into routes, feature flags over HTTP, and migration from kyo-sttp and kyo-tapir.

getkyo.io: [kyo-http](https://getkyo.io/latest/kyo-http/)

**Getting Started**  
→ [read online](https://getkyo.io/latest/kyo-http/#getting-started)

**Making Requests (the client)**  
  
*Terms:* Making Requests, Side-Effect Operations, Error Handling, Streaming, Multipart Uploads, Configuration, Retries, Custom Instances  
→ [read online](https://getkyo.io/latest/kyo-http/#making-requests-the-client)

**Serving Requests (the server)**  
  
*Terms:* Handling Requests, Streaming, Configuration, TLS, Transport Tuning  
→ [read online](https://getkyo.io/latest/kyo-http/#serving-requests-the-server)

**Describing Endpoints with Routes**  
  
*Terms:* Paths, Typed Fields, Request and Response Fields, Route Handlers, Domain Errors, Filters, Custom Codecs, Primitive Types  
→ [read online](https://getkyo.io/latest/kyo-http/#describing-endpoints-with-routes)

**Error Handling**  
  
*Terms:* Short-Circuit Responses, Client Errors, Response Helpers  
→ [read online](https://getkyo.io/latest/kyo-http/#error-handling-2)

**WebSockets and Raw Connections**  
  
*Terms:* WebSockets, Raw Connections  
→ [read online](https://getkyo.io/latest/kyo-http/#websockets-and-raw-connections)

**OpenAPI in Both Directions**  
  
*Terms:* Routes to Spec, Spec to Routes  
→ [read online](https://getkyo.io/latest/kyo-http/#openapi-in-both-directions)

**Feature Flags over HTTP**  
→ [read online](https://getkyo.io/latest/kyo-http/#feature-flags-over-http)

**Cross-Platform**  
→ [read online](https://getkyo.io/latest/kyo-http/#cross-platform)

**Migrating from kyo-sttp and kyo-tapir**  
  
*Terms:* Client: kyo-sttp → HttpClient, Server: tapir endpoint → HttpRoute, Server: NettyKyoServer → HttpServer, Errors: StatusCode → HttpResponse.halt / .error, JSON: zio-json → Schema, Cheat sheet  
→ [read online](https://getkyo.io/latest/kyo-http/#migrating-from-kyo-sttp-and-kyo-tapir)

**Demos**  
→ [read online](https://getkyo.io/latest/kyo-http/#demos)


---

<a id="ch14"></a>
## kyo-ai: typed LLM programs

LLM calls as typed values: the LLM/AI/Agent trio, one-shot and typed generation, instances that keep a conversation, tools with an automatic call loop, prompts, thoughts and modes, long-lived agents, streaming, decisions, parallel generation, usage tracking, conversation state, providers, and how it works inside. The module the kyo-lambda-rlm work builds on.

getkyo.io: [kyo-ai](https://getkyo.io/latest/kyo-ai/)

**The trio: LLM, AI, Agent**  
→ [read online](https://getkyo.io/latest/kyo-ai/#the-trio-llm-ai-agent)

**One-shot generation**  
→ [read online](https://getkyo.io/latest/kyo-ai/#one-shot-generation)

**Typed results**  
→ [read online](https://getkyo.io/latest/kyo-ai/#typed-results)

**Instances that remember**  
→ [read online](https://getkyo.io/latest/kyo-ai/#instances-that-remember)

**Tools and the automatic loop**  
  
*Terms:* Tools from an MCP server  
→ [read online](https://getkyo.io/latest/kyo-ai/#tools-and-the-automatic-loop)

**Shaping generation: prompts, thoughts, modes**  
  
*Terms:* Prompts, Thoughts, Modes, Composing binders  
→ [read online](https://getkyo.io/latest/kyo-ai/#shaping-generation-prompts-thoughts-modes)

**Long-lived agents**  
→ [read online](https://getkyo.io/latest/kyo-ai/#long-lived-agents)

**Streaming**  
  
*Terms:* Not every backend streams incrementally  
→ [read online](https://getkyo.io/latest/kyo-ai/#streaming)

**Decisions**  
  
*Terms:* Which model decides  
→ [read online](https://getkyo.io/latest/kyo-ai/#decisions)

**Parallel generation**  
→ [read online](https://getkyo.io/latest/kyo-ai/#parallel-generation)

**Tracking usage**  
→ [read online](https://getkyo.io/latest/kyo-ai/#tracking-usage)

**Controlling conversation state**  
→ [read online](https://getkyo.io/latest/kyo-ai/#controlling-conversation-state)

**Configuration and providers**  
  
*Terms:* Reasoning, Output ceilings, Declaring a model, The providers  
→ [read online](https://getkyo.io/latest/kyo-ai/#configuration-and-providers)

**Conversation data types**  
→ [read online](https://getkyo.io/latest/kyo-ai/#conversation-data-types)

**What this removes**  
→ [read online](https://getkyo.io/latest/kyo-ai/#what-this-removes)

**How it works**  
→ [read online](https://getkyo.io/latest/kyo-ai/#how-it-works)

**Demos**  
→ [read online](https://getkyo.io/latest/kyo-ai/#demos)


---

<a id="ch15"></a>
## kyo-zio: ZIO interop

Moving between Kyo and ZIO: lifting and running effects in both directions, ZStream interop, ZLayer interop, and how failures and interruption translate.

getkyo.io: [kyo-zio](https://getkyo.io/latest/kyo-zio/)

**Lifting and running effects**  
  
*Terms:* Lifting a ZIO into Kyo, Running a Kyo as ZIO, ZIO environments are rejected at compile time, Failure ordering at the boundary, Cancellation semantics on ZIOs.run  
→ [read online](https://getkyo.io/latest/kyo-zio/#lifting-and-running-effects)

**Streaming interop (ZStream)**  
  
*Terms:* Lifting a ZStream into Kyo, Scoping and finalizers, Running a Kyo Stream as ZStream, Round-tripping  
→ [read online](https://getkyo.io/latest/kyo-zio/#streaming-interop-zstream)

**Dependency layers (ZLayer)**  
  
*Terms:* Lifting a ZLayer into Kyo, Running a Kyo Layer as ZLayer, When to use which  
→ [read online](https://getkyo.io/latest/kyo-zio/#dependency-layers-zlayer)

**Failure and interruption translation**  
  
*Terms:* Exit.toResult and Result.toExit, Cause.toError and Result.Error.toCause, Interruption as panic  
→ [read online](https://getkyo.io/latest/kyo-zio/#failure-and-interruption-translation)


---

<a id="ch16"></a>
## More modules

The rest of the ecosystem, one page each on getkyo.io: system access, SQL drivers, schema codecs, config and feature flags, durable workflows, UI, i18n, GraphQL, parsing, containers, chat bots, browser automation, JSON-RPC, MCP and LSP, networking, FFI, TASTy, observability, compatibility bridges, and scheduler drop-ins for ZIO, Pekko and Finagle.

**kyo-system**  
  
*Terms:* Command, FileSystemException, Path, Process, System  
→ [read online](https://getkyo.io/latest/kyo-system/)

**kyo-system-doltfs**  
  
*Terms:* FileSystem  
→ [read online](https://getkyo.io/latest/kyo-system-doltfs/)

**kyo-sql**  
  
*Terms:* DB  
→ [read online](https://getkyo.io/latest/kyo-sql/)

**kyo-sql-postgres**  
  
*Terms:* COPY, LISTEN, NOTIFY  
→ [read online](https://getkyo.io/latest/kyo-sql-postgres/)

**kyo-sql-mysql**  
  
*Terms:* LOAD DATA LOCAL INFILE  
→ [read online](https://getkyo.io/latest/kyo-sql-mysql/)

**kyo-sql-sqlite**  
→ [read online](https://getkyo.io/latest/kyo-sql-sqlite/)

**kyo-sql-dolt**  
→ [read online](https://getkyo.io/latest/kyo-sql-dolt/)

**kyo-sql-doltlite**  
→ [read online](https://getkyo.io/latest/kyo-sql-doltlite/)

**kyo-schema-json**  
  
*Terms:* Json.Lines, Jsonl  
→ [read online](https://getkyo.io/latest/kyo-schema-json/)

**kyo-schema-protobuf**  
  
*Terms:* .proto, Protobuf.encode, decode  
→ [read online](https://getkyo.io/latest/kyo-schema-protobuf/)

**kyo-schema-msgpack**  
  
*Terms:* MsgPack.encode, decode  
→ [read online](https://getkyo.io/latest/kyo-schema-msgpack/)

**kyo-schema-bson**  
  
*Terms:* Bson.encode, decode  
→ [read online](https://getkyo.io/latest/kyo-schema-bson/)

**kyo-schema-ion**  
  
*Terms:* Ion, IonBinary  
→ [read online](https://getkyo.io/latest/kyo-schema-ion/)

**kyo-schema-yaml**  
  
*Terms:* Yaml.encode, decode  
→ [read online](https://getkyo.io/latest/kyo-schema-yaml/)

**kyo-config**  
→ [read online](https://getkyo.io/latest/kyo-config/)

**kyo-flow**  
→ [read online](https://getkyo.io/latest/kyo-flow/)

**kyo-ui**  
→ [read online](https://getkyo.io/latest/kyo-ui/)

**kyo-markdown**  
→ [read online](https://getkyo.io/latest/kyo-markdown/)

**kyo-i18n**  
  
*Terms:* .ftl, Signal, t  
→ [read online](https://getkyo.io/latest/kyo-i18n/)

**kyo-caliban**  
→ [read online](https://getkyo.io/latest/kyo-caliban/)

**kyo-zio-test**  
  
*Terms:* KyoSpecAbstract, KyoSpecDefault, Spec, zio-test  
→ [read online](https://getkyo.io/latest/kyo-zio-test/)

**kyo-offheap**  
  
*Terms:* calloc, free  
→ [read online](https://getkyo.io/latest/kyo-offheap/)

**kyo-parse**  
  
*Terms:* Parse[Char] & Parse[Int]  
→ [read online](https://getkyo.io/latest/kyo-parse/)

**kyo-pod**  
→ [read online](https://getkyo.io/latest/kyo-pod/)

**kyo-slack**  
  
*Terms:* dsl  
→ [read online](https://getkyo.io/latest/kyo-slack/)

**kyo-browser**  
  
*Terms:* readableContent  
→ [read online](https://getkyo.io/latest/kyo-browser/)

**kyo-jsonrpc**  
→ [read online](https://getkyo.io/latest/kyo-jsonrpc/)

**kyo-mcp**  
→ [read online](https://getkyo.io/latest/kyo-mcp/)

**kyo-lsp**  
→ [read online](https://getkyo.io/latest/kyo-lsp/)

**kyo-compiler**  
→ [read online](https://getkyo.io/latest/kyo-compiler/)

**kyo-aeron**  
  
*Terms:* Topic  
→ [read online](https://getkyo.io/latest/kyo-aeron/)

**kyo-net**  
→ [read online](https://getkyo.io/latest/kyo-net/)

**kyo-ffi**  
→ [read online](https://getkyo.io/latest/kyo-ffi/)

**kyo-tasty**  
→ [read online](https://getkyo.io/latest/kyo-tasty/)

**kyo-stats-registry**  
  
*Terms:* TraceExporter  
→ [read online](https://getkyo.io/latest/kyo-stats-registry/)

**kyo-stats-otlp**  
  
*Terms:* traceparent  
→ [read online](https://getkyo.io/latest/kyo-stats-otlp/)

**kyo-stats-machine**  
  
*Terms:* kyo.Stat  
→ [read online](https://getkyo.io/latest/kyo-stats-machine/)

**kyo-logging-jpl**  
  
*Terms:* java.lang.System.Logger, kyo.Log  
→ [read online](https://getkyo.io/latest/kyo-logging-jpl/)

**kyo-logging-slf4j**  
  
*Terms:* kyo.Log  
→ [read online](https://getkyo.io/latest/kyo-logging-slf4j/)

**kyo-compat**  
  
*Terms:* kyo.compat.*  
→ [read online](https://getkyo.io/latest/kyo-compat/)

**kyo-reactive-streams**  
  
*Terms:* Publisher, Stream, Subscriber  
→ [read online](https://getkyo.io/latest/kyo-reactive-streams/)

**kyo-case-app**  
  
*Terms:* run { options => ... }  
→ [read online](https://getkyo.io/latest/kyo-case-app/)

**kyo-doctest**  
  
*Terms:* sbt doctest  
→ [read online](https://getkyo.io/latest/kyo-doctest/)

**kyo-scheduler-zio**  
  
*Terms:* KyoSchedulerZIORuntime.default, extends KyoSchedulerZIOAppDefault  
→ [read online](https://getkyo.io/latest/kyo-scheduler-zio/)

**kyo-scheduler-pekko**  
→ [read online](https://getkyo.io/latest/kyo-scheduler-pekko/)

**kyo-scheduler-finagle**  
  
*Terms:* -Dcom.twitter.finagle.exp.scheduler=kyo  
→ [read online](https://getkyo.io/latest/kyo-scheduler-finagle/)

