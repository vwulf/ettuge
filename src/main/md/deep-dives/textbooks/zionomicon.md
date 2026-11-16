<a id="ch1"></a>
# Zionomicon: Master the Dark Art of Creating Scalable, Type-Safe, Concurrent Apps with ZIO

> John A. De Goes, Adam Fraser and Milad Khajavi · Ziverge, edition of 20 November 2024 · [the PDF in Drive](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

This book is very granular (about 40 chapters and 250 sections), so summaries and terms are given per chapter; each section is still listed with its own PDF page range. Conclusion and exercise sections are not broken out. An older 2021 draft of Zionomicon is also in your Drive and is superseded by this edition. Chapters link to the matching pages of the official ZIO 2 reference at zio.dev, which covers the same APIs (it is separate documentation, not the book’s text). Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

The comprehensive guide to ZIO 2 for Scala, by its creator and core contributors. After a history of ZIO, it teaches effects as blueprints, testing, the typed error model and interop; then fibers and structured concurrency, concurrency operators, supervision and interruption; concurrent structures (Ref, Promise, Queue, Hub, Semaphore); resource safety with acquire/release and Scope; dependency injection with ZLayer and ZEnvironment; software transactional memory; retries with Schedule, debugging and error-handling practice; ZStream, channels, pipelines and sinks; ZIO Test in depth (assertions, test environment, aspects, resources, property-based testing, annotations, reporting); a parallel web crawler application; and appendices on Scala’s type system and variance.

**Contents**

1. [Foreword by John A. De Goes](ch1): How ZIO evolved from 1.0 to 2.0 and why.
2. [Essentials: First Steps With ZIO](ch2): Effects as values and the ZIO type.
3. [Essentials: Testing ZIO Programs](ch3): A first look at ZIO Test.
4. [Essentials: The ZIO Error Model](ch4): Typed errors, defects and Cause.
5. [Essentials: Integrating with ZIO](ch5): Interop with Java, JS, Cats Effect and libraries.
6. [Parallelism and Concurrency: The Fiber Model](ch6): Fibers.
7. [Parallelism and Concurrency: Concurrency Operators](ch7): Racing and parallel composition.
8. [Parallelism and Concurrency: Fiber Supervision in Depth](ch8): Supervision and structured concurrency.
9. [Parallelism and Concurrency: Interruption in Depth](ch9): Interruption semantics.
10. [Concurrent Structures: Ref - Shared State](ch10): Ref and FiberRef.
11. [Concurrent Structures: Promise - Work Synchronization](ch11): Promise for synchronization.
12. [Concurrent Structures: Queue - Work Distribution](ch12): Queues for work distribution.
13. [Concurrent Structures: Hub - Broadcasting](ch13): Hub for broadcasting.
14. [Concurrent Structures: Semaphore - Work Limiting](ch14): Semaphores for limiting concurrency.
15. [Resource Handling: Acquire Release - Safe Resource Handling](ch15): acquireRelease and ensuring.
16. [Resource Handling: Scope - Composable Resources](ch16): Scope as a composable resource abstraction.
17. [Resource Handling: Advanced Scopes](ch17): Advanced scopes and resources.
18. [Dependency Injection: Essentials](ch18): ZIO environment and layers.
19. [Dependency Injection: Advanced Dependency Injection](ch19): Advanced dependency injection.
20. [Software Transactional Memory: Composing Atomicity](ch20): STM basics.
21. [Software Transactional Memory: STM Data Structures](ch21): Transactional data structures.
22. [Software Transactional Memory: Advanced STM](ch22): STM internals and tuning.
23. [Advanced Error Management: Retries](ch23): Retrying and repeating with Schedule.
24. [Advanced Error Management: Debugging](ch24): Debugging ZIO programs.
25. [Advanced Error Management: Best Practices](ch25): Error-handling best practices.
26. [Streaming: First Steps with ZStream](ch26): ZStream basics.
27. [Streaming: Next Steps With ZStream](ch27): Sinks and pipelines introduced.
28. [Channels: Unifying Streams, Sinks, and Pipelines](ch28): ZChannel as the unifying abstraction.
29. [Streaming: Transforming Streams](ch29): Transforming streams.
30. [Streaming: Combining Streams](ch30): Combining streams.
31. [Streaming: Pipelines](ch31): Pipelines.
32. [Streaming: Sinks](ch32): Sinks.
33. [Testing: Basic Testing](ch33): ZIO Test fundamentals.
34. [Testing: Assertions](ch34): Assertions.
35. [Testing: The Test Environment](ch35): Test environment.
36. [Testing: Test Aspects](ch36): Test aspects.
37. [Testing: Using Resources in Tests](ch37): Resources in tests.
38. [Testing: Property-Based Testing](ch38): Property-based testing.
39. [Testing: Test Annotations](ch39): Test annotations.
40. [Testing: Reporting](ch40): Test reporting.
41. [Applications: Parallel Web Crawler](ch41): A parallel web crawler application.
42. [Appendix 1: The Scala Type System](ch42): Scala type system essentials.
43. [Appendix 2: Mastering Variance](ch43): Variance.


---

## Foreword by John A. De Goes

*PDF pp. 17–36*

How ZIO evolved from 1.0 to 2.0 and why.

zio.dev reference: [Introduction](https://zio.dev/reference/)

*Terms:* ZIO history, ZIO 2.0, structured concurrency, ZLayer, ZIO Test, alternatives, Cats Effect

**A Brief History of ZIO**  
→ PDF p. 17 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**The Birth of ZIO**  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Contentious Concurrency**  
→ PDF p. 18 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Typed Errors & Other Evolution**  
→ PDF p. 19 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Contributor Growth**  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Improved Type-Inference**  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Batteries Included**  
→ PDF p. 21 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO Stream**  
→ PDF p. 22 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO Environment**  
→ PDF p. 22 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Software Transactional Memory**  
→ PDF p. 23 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Execution Traces**  
→ PDF p. 24 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Summer 2019**  
→ PDF p. 25 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO Test**  
→ PDF p. 25 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZLayer**  
→ PDF p. 26 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Structured Concurrency**  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Preparation for ZIO 2.0**  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Simplification of ZIO Environment and Dependency Injection**  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO Becomes Composable Resourceful Effect**  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Service Pattern**  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Smart Assertions**  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**More Concrete Types**  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Unified Streaming**  
→ PDF p. 30 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Regional Settings and Contextual Scopes**  
→ PDF p. 30 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Observability**  
→ PDF p. 30 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Performance**  
→ PDF p. 31 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO 2.0**  
→ PDF p. 32 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**What is Next?**  
→ PDF p. 32 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Why ZIO**  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO Alternatives**  
→ PDF p. 33 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Zionomicon**  
→ PDF pp. 34–36 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch2"></a>
## Essentials: First Steps With ZIO

*PDF pp. 37–68*

Effects as values and the ZIO type.

zio.dev reference: [ZIO](https://zio.dev/reference/core/zio/)

*Terms:* functional effects, blueprints, flatMap, zip, ZIO[R, E, A], type aliases, Future, ZIO.attempt, default services, recursion

**Functional Effects as Blueprints**  
→ PDF pp. 37–40 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Sequential Composition**  
→ PDF pp. 41–42 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Other Sequential Operators**  
→ PDF pp. 43–44 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO Type Parameters**  
→ PDF pp. 45–48 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**ZIO Type Aliases**  
→ PDF p. 49 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Comparison to Future**  
→ PDF pp. 49–51 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**More Effect Constructors**  
→ PDF pp. 52–57 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Default ZIO Services**  
→ PDF pp. 58–60 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Recursion and ZIO**  
→ PDF p. 61 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch3"></a>
## Essentials: Testing ZIO Programs

*PDF pp. 69–82*

A first look at ZIO Test.

zio.dev reference: [Writing our first test](https://zio.dev/reference/test/writing-our-first-test/)

*Terms:* ZIO Test, assertions, TestClock, test aspects, property-based testing

**Writing Simple Programs with ZIO Test**  
→ PDF pp. 72–73 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Assertions**  
→ PDF pp. 74–75 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Test Implementations of Standard ZIO Services**  
→ PDF pp. 76–77 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Common Test Aspects**  
→ PDF p. 78 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Basic Property-based Testing**  
→ PDF pp. 79–80 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch4"></a>
## Essentials: The ZIO Error Model

*PDF pp. 83–98*

Typed errors, defects and Cause.

zio.dev reference: [Error management](https://zio.dev/reference/error-management/), [Cause](https://zio.dev/reference/core/cause/), [Exit](https://zio.dev/reference/core/exit/)

*Terms:* errors vs defects, Cause, Exit, catchAll, orDie, multiple failures, error composition, execution tracing, typed errors

**Exceptions Versus Defects**  
→ PDF pp. 83–84 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Cause**  
→ PDF p. 85 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Exit**  
→ PDF p. 85 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Handling Defects**  
→ PDF p. 86 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Converting Errors to Defects**  
→ PDF p. 87 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Multiple Failures**  
→ PDF pp. 88–89 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Other Useful Error Operators**  
→ PDF p. 90 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Combining Effects with Different Errors**  
→ PDF pp. 90–91 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Execution Tracing**  
→ PDF p. 92 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Dealing With Stacked Errors**  
→ PDF p. 93 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Leveraging Typed Errors**  
→ PDF p. 94 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch5"></a>
## Essentials: Integrating with ZIO

*PDF pp. 99–116*

Interop with Java, JS, Cats Effect and libraries.

zio.dev reference: [Java](https://zio.dev/guides/interop/with-java/), [JavaScript](https://zio.dev/guides/interop/with-javascript/), [Cats Effect](https://zio.dev/guides/interop/with-cats-effect/), [Future](https://zio.dev/guides/interop/with-future/)

*Terms:* Java interop, CompletableFuture, Scala.js, Cats Effect interop, library integration

**Integrating with Java**  
→ PDF pp. 102–104 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Integrating with Javascript**  
→ PDF p. 105 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Integrating with Cats Effect**  
→ PDF pp. 106–107 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Integrating with Specific Libraries**  
→ PDF pp. 108–113 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch6"></a>
## Parallelism and Concurrency: The Fiber Model

*PDF pp. 117–128*

Fibers.

zio.dev reference: [Fibers](https://zio.dev/reference/fiber/)

*Terms:* fibers, fork, join, interrupt, supervision, locking to executors

**Fibers Distinguished from Operating System Threads**  
→ PDF p. 117 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Forking Fibers**  
→ PDF p. 118 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Joining Fibers**  
→ PDF pp. 119–120 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Interrupting Fibers**  
→ PDF pp. 121–122 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Fiber Supervision**  
→ PDF pp. 123–124 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Locking Effects**  
→ PDF pp. 125–126 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch7"></a>
## Parallelism and Concurrency: Concurrency Operators

*PDF pp. 129–136*

Racing and parallel composition.

zio.dev reference: [Concurrency](https://zio.dev/reference/concurrency/)

*Terms:* race, zipPar, foreachPar, collectAllPar, validatePar

**The Importance of Concurrency Operators**  
→ PDF p. 129 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Race and ZipPar**  
→ PDF p. 129 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Variants of ZipPar**  
→ PDF pp. 130–131 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Variants of Race**  
→ PDF p. 132 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Validation Errors**  
→ PDF p. 133 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch8"></a>
## Parallelism and Concurrency: Fiber Supervision in Depth

*PDF pp. 137–148*

Supervision and structured concurrency.

zio.dev reference: [Fibers](https://zio.dev/reference/fiber/), [Supervisor](https://zio.dev/reference/observability/supervisor/)

*Terms:* structured concurrency, fork/join, forkDaemon, custom supervision, fire-and-forget

**Fork/Join Identity Law**  
→ PDF p. 137 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Structured Concurrency**  
→ PDF pp. 138–140 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Custom Supervision Strategies**  
→ PDF pp. 141–145 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Fire-and-Forget**  
→ PDF p. 146 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch9"></a>
## Parallelism and Concurrency: Interruption in Depth

*PDF pp. 149–164*

Interruption semantics.

zio.dev reference: [Interruption](https://zio.dev/reference/interruption/)

*Terms:* interruption, uninterruptible regions, interruptibility composition, await interruption

**Timing of Interruption**  
→ PDF pp. 149–153 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Interruptible and Uninterruptible Regions**  
→ PDF pp. 154–155 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Composing Interruptibility**  
→ PDF pp. 156–158 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Waiting for Interruption**  
→ PDF pp. 159–161 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch10"></a>
## Concurrent Structures: Ref - Shared State

*PDF pp. 165–180*

Ref and FiberRef.

zio.dev reference: [Ref](https://zio.dev/reference/concurrency/ref/), [Ref.Synchronized](https://zio.dev/reference/concurrency/refsynchronized/), [FiberRef](https://zio.dev/reference/state-management/fiberref/)

*Terms:* Ref, atomic updates, Ref.Synchronized, FiberRef, shared state

**Purely Functional Mutable State**  
→ PDF pp. 165–167 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Purely Functional Equivalent of an Atomic Reference**  
→ PDF pp. 168–170 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Operations are Atomic but do not Compose Atomically**  
→ PDF p. 171 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Ref.Synchronized for Evaluating Effects while Updating**  
→ PDF pp. 172–173 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**FiberRef for References Specific to each Fiber**  
→ PDF pp. 174–176 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch11"></a>
## Concurrent Structures: Promise - Work Synchronization

*PDF pp. 181–190*

Promise for synchronization.

zio.dev reference: [Promise](https://zio.dev/reference/concurrency/promise/)

*Terms:* Promise, await, completion, interruption

**Various Ways of Completing Promises**  
→ PDF pp. 182–183 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Waiting on a Promise**  
→ PDF p. 184 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Promises and Interruption**  
→ PDF p. 185 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Combining Ref and Promise for More Complicated Concurrency Scenarios**  
→ PDF pp. 186–187 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch12"></a>
## Concurrent Structures: Queue - Work Distribution

*PDF pp. 191–200*

Queues for work distribution.

zio.dev reference: [Queue](https://zio.dev/reference/concurrency/queue/)

*Terms:* Queue, bounded, dropping, sliding, offer, take

**Queues as Generalizations of Promises**  
→ PDF p. 191 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Offering and Taking Values from a Queue**  
→ PDF p. 192 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Varieties of Queues**  
→ PDF pp. 193–195 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Other Combinators on Queues**  
→ PDF pp. 196–197 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch13"></a>
## Concurrent Structures: Hub - Broadcasting

*PDF pp. 201–212*

Hub for broadcasting.

zio.dev reference: [Hub](https://zio.dev/reference/concurrency/hub/)

*Terms:* Hub, broadcast, publish, subscribe

**Hub: An Optimal Solution to the Broadcasting Problem**  
→ PDF pp. 202–203 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Creating Hubs**  
→ PDF pp. 204–207 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Operators on Hubs**  
→ PDF p. 208 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch14"></a>
## Concurrent Structures: Semaphore - Work Limiting

*PDF pp. 213–218*

Semaphores for limiting concurrency.

zio.dev reference: [Semaphore](https://zio.dev/reference/concurrency/semaphore/)

*Terms:* Semaphore, withPermits, limiting parallelism

**Semaphore Interface**  
→ PDF p. 213 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Semaphores to Limit Parallelism**  
→ PDF p. 214 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Semaphore to Implement Operators**  
→ PDF p. 215 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Making a Data Structure Safe for Concurrent Access**  
→ PDF pp. 216–217 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch15"></a>
## Resource Handling: Acquire Release - Safe Resource Handling

*PDF pp. 219–226*

acquireRelease and ensuring.

zio.dev reference: [Resource management](https://zio.dev/reference/resource/)

*Terms:* acquireRelease, bracket, ensuring, finalizers

**The Limitation of try-finally in Asynchronous Programming**  
→ PDF pp. 219–220 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Acquire Release as a Generalization of Try and Finally**  
→ PDF pp. 221–222 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**The Ensuring Operator**  
→ PDF p. 223 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch16"></a>
## Resource Handling: Scope - Composable Resources

*PDF pp. 227–242*

Scope as a composable resource abstraction.

zio.dev reference: [Scope](https://zio.dev/reference/resource/scope/)

*Terms:* Scope, ZIO.scoped, scoped resources, finalizers

**Reification of Acquire Release**  
→ PDF pp. 228–230 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Scope as a Dynamic Scope**  
→ PDF p. 231 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Constructing Scoped Resources**  
→ PDF pp. 232–235 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Transforming Scoped Resources**  
→ PDF p. 236 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Scoped Resources**  
→ PDF pp. 236–237 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Varieties of Scoped Resources**  
→ PDF p. 238 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch17"></a>
## Resource Handling: Advanced Scopes

*PDF pp. 243–256*

Advanced scopes and resources.

zio.dev reference: [Scope](https://zio.dev/reference/resource/scope/), [ScopedRef](https://zio.dev/reference/resource/scopedref/)

*Terms:* scopes, child scopes, resource management

**Scopes Revisited**  
→ PDF pp. 243–244 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**From Scopes to Resources**  
→ PDF pp. 245–246 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Resources**  
→ PDF pp. 247–248 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Child Scopes**  
→ PDF pp. 249–251 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Putting it All Together**  
→ PDF pp. 252–253 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch18"></a>
## Dependency Injection: Essentials

*PDF pp. 257–276*

ZIO environment and layers.

zio.dev reference: [Dependency injection](https://zio.dev/reference/di/), [ZLayer](https://zio.dev/reference/contextual/zlayer/), [Service pattern](https://zio.dev/reference/service-pattern/)

*Terms:* ZEnvironment, ZLayer, service pattern, onion architecture, accessors

**The Environment Type**  
→ PDF pp. 257–258 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Fundamental Operators for Working with the Environment**  
→ PDF pp. 259–260 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Typical Uses for the Environment**  
→ PDF p. 261 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**The Onion Architecture**  
→ PDF pp. 262–266 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Layers**  
→ PDF pp. 267–271 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Accessors**  
→ PDF pp. 272–273 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Service Pattern**  
→ PDF p. 274 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Declaring Dependencies via ZIO Environment or Constructor Arguments?**  
→ PDF p. 275 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch19"></a>
## Dependency Injection: Advanced Dependency Injection

*PDF pp. 277–288*

Advanced dependency injection.

zio.dev reference: [ZEnvironment](https://zio.dev/reference/contextual/zenvironment/), [Layer memoization](https://zio.dev/reference/di/dependency-memoization/), [Automatic ZLayer derivation](https://zio.dev/reference/contextual/automatic-zlayer-derivation/)

*Terms:* ZEnvironment, multiple services, layer errors, memoization, automatic layer derivation

**What is ZEnvironment?**  
→ PDF pp. 277–278 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Providing Multiple Services of the Same Type**  
→ PDF p. 279 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Handling Errors in Layer Construction**  
→ PDF pp. 279–280 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Memoization of Dependencies**  
→ PDF pp. 281–283 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Automatic ZLayer Derivation**  
→ PDF pp. 284–285 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch20"></a>
## Software Transactional Memory: Composing Atomicity

*PDF pp. 289–304*

STM basics.

zio.dev reference: [STM](https://zio.dev/reference/stm/), [TRef](https://zio.dev/reference/stm/tref/)

*Terms:* STM, TRef, atomically, retry, composable transactions

**Inability to Compose Atomic Actions with other Concurrency Primitives**  
→ PDF pp. 289–291 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Conceptual Description of STM**  
→ PDF pp. 292–293 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using STM**  
→ PDF pp. 294–298 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Retrying and Repeating Transactions**  
→ PDF p. 299 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Limitations of STM**  
→ PDF pp. 299–301 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch21"></a>
## Software Transactional Memory: STM Data Structures

*PDF pp. 305–326*

Transactional data structures.

zio.dev reference: [TMap](https://zio.dev/reference/stm/tmap/), [TQueue](https://zio.dev/reference/stm/tqueue/), [TPriorityQueue](https://zio.dev/reference/stm/tpriorityqueue/), [TSet](https://zio.dev/reference/stm/tset/), [TArray](https://zio.dev/reference/stm/tarray/)

*Terms:* TMap, TQueue, TPriorityQueue, TSet, custom STM structures

**Description of STM Data Structures**  
→ PDF pp. 306–318 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Creating Your Own STM Data Structures**  
→ PDF pp. 319–323 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch22"></a>
## Software Transactional Memory: Advanced STM

*PDF pp. 327–344*

STM internals and tuning.

zio.dev reference: [STM](https://zio.dev/reference/stm/)

*Terms:* STM implementation, debugging, optimization, control flow

**How STM Works Under the Hood**  
→ PDF pp. 327–332 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Troubleshooting and Debugging**  
→ PDF pp. 333–334 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Optimization**  
→ PDF pp. 335–340 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Transaction Control Flows**  
→ PDF p. 341 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch23"></a>
## Advanced Error Management: Retries

*PDF pp. 345–378*

Retrying and repeating with Schedule.

zio.dev reference: [Schedule](https://zio.dev/reference/schedule/), [Retrying](https://zio.dev/reference/error-management/recovering/retrying/)

*Terms:* Schedule, retry, repeat, exponential backoff, schedule composition

**Limitations of Traditional Retry Operators**  
→ PDF pp. 345–346 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Retrying and Repeating with ZIO**  
→ PDF pp. 347–348 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Common Schedules**  
→ PDF pp. 349–357 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Transforming Schedules**  
→ PDF pp. 358–366 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Composing Schedules**  
→ PDF pp. 367–374 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Implementation of Schedule**  
→ PDF pp. 375–376 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch24"></a>
## Advanced Error Management: Debugging

*PDF pp. 379–390*

Debugging ZIO programs.

zio.dev reference: [Supervisor](https://zio.dev/reference/observability/supervisor/), [Logging](https://zio.dev/reference/observability/logging/), [Tracing](https://zio.dev/reference/observability/tracing/)

*Terms:* debug, logging, stack traces, fiber dumps, supervisor

**Understanding Execution Flows**  
→ PDF p. 379 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Printing Debug Information**  
→ PDF p. 380 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Enabling Diagnostic and Debug Logging**  
→ PDF p. 381 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Reading Stack Traces**  
→ PDF p. 382 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Fiber Dumps**  
→ PDF pp. 383–384 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Supervising Fibers**  
→ PDF pp. 385–388 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch25"></a>
## Advanced Error Management: Best Practices

*PDF pp. 391–404*

Error-handling best practices.

zio.dev reference: [Error-management best practices](https://zio.dev/reference/error-management/best-practices/)

*Terms:* recoverable errors, non-recoverable errors, error modeling

**Recoverable Errors**  
→ PDF p. 391 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Non-recoverable Errors**  
→ PDF pp. 392–401 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch26"></a>
## Streaming: First Steps with ZStream

*PDF pp. 405–420*

ZStream basics.

zio.dev reference: [ZStream](https://zio.dev/reference/stream/zstream/), [Creating streams](https://zio.dev/reference/stream/zstream/creating-zio-streams/)

*Terms:* ZStream, effectful iterator, constructors, run

**Streams as Effectful Iterators**  
→ PDF pp. 405–406 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Streams as Collections**  
→ PDF pp. 407–409 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Constructing Basic Streams**  
→ PDF pp. 410–412 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Running Streams**  
→ PDF pp. 413–417 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Type Parameters**  
→ PDF p. 418 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch27"></a>
## Streaming: Next Steps With ZStream

*PDF pp. 421–432*

Sinks and pipelines introduced.

zio.dev reference: [ZSink](https://zio.dev/reference/stream/zsink/), [ZPipeline](https://zio.dev/reference/stream/zpipeline/)

*Terms:* ZSink, ZPipeline

**Sinks**  
→ PDF pp. 425–428 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Pipelines**  
→ PDF pp. 429–430 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch28"></a>
## Channels: Unifying Streams, Sinks, and Pipelines

*PDF pp. 433–448*

ZChannel as the unifying abstraction.

zio.dev reference: [ZChannel](https://zio.dev/reference/stream/zchannel/)

*Terms:* ZChannel, channel constructors, operators, scopes

**Channels**  
→ PDF pp. 433–437 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Channel Constructors**  
→ PDF pp. 438–439 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Channel Operators**  
→ PDF pp. 440–445 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Channel Scopes**  
→ PDF p. 446 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch29"></a>
## Streaming: Transforming Streams

*PDF pp. 449–468*

Transforming streams.

zio.dev reference: [ZStream operations](https://zio.dev/reference/stream/zstream/operations/)

*Terms:* map, mapZIO, flatMap, filter, collect, grouping, partition, broadcast, throttle

**Mapping**  
→ PDF pp. 449–451 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Transform and Combine**  
→ PDF p. 452 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Flattening**  
→ PDF p. 453 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Filtering Operators**  
→ PDF p. 454 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Collecting (Filter-map)**  
→ PDF p. 454 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Grouping**  
→ PDF pp. 455–459 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Partitioning**  
→ PDF p. 460 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Broadcasting and Distributing**  
→ PDF pp. 460–461 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Flow Control and Rate Limiting**  
→ PDF pp. 462–465 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch30"></a>
## Streaming: Combining Streams

*PDF pp. 469–480*

Combining streams.

zio.dev reference: [ZStream operations](https://zio.dev/reference/stream/zstream/operations/)

*Terms:* concat, merge, zip, cross, orElse, interleave

**Stream Concatenation**  
→ PDF p. 469 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Merging Streams**  
→ PDF p. 470 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Zipping Streams**  
→ PDF pp. 470–472 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Cartesian Product**  
→ PDF p. 473 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Fallback Streams**  
→ PDF p. 474 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Stateful Stream Combination**  
→ PDF pp. 475–477 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Interleaving**  
→ PDF p. 478 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch31"></a>
## Streaming: Pipelines

*PDF pp. 481–494*

Pipelines.

zio.dev reference: [ZPipeline](https://zio.dev/reference/stream/zpipeline/)

*Terms:* ZPipeline, transformations

**Pipelines as Stream Transformations**  
→ PDF pp. 481–482 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Pipelines**  
→ PDF pp. 483–485 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Constructing Pipelines**  
→ PDF pp. 486–492 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch32"></a>
## Streaming: Sinks

*PDF pp. 495–510*

Sinks.

zio.dev reference: [ZSink](https://zio.dev/reference/stream/zsink/), [Sink operations](https://zio.dev/reference/stream/zsink/operations/)

*Terms:* ZSink, aggregation, combining sinks

**Sinks as Composable Aggregation Strategies**  
→ PDF pp. 495–496 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Sinks**  
→ PDF pp. 497–502 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Combining Sinks**  
→ PDF pp. 503–506 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Constructing Sinks**  
→ PDF pp. 507–508 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch33"></a>
## Testing: Basic Testing

*PDF pp. 511–518*

ZIO Test fundamentals.

zio.dev reference: [Spec](https://zio.dev/reference/test/spec/), [Running tests](https://zio.dev/reference/test/running-tests/)

*Terms:* tests as effects, specs, suites

**Tests as Effects**  
→ PDF pp. 511–516 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Specs as Recursively Nested Collections of Tests**  
→ PDF p. 517 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch34"></a>
## Testing: Assertions

*PDF pp. 519–534*

Assertions.

zio.dev reference: [Assertions](https://zio.dev/reference/test/assertions/), [Smart assertions](https://zio.dev/reference/test/assertions/smart-assertions/)

*Terms:* Assertion, smart assertions, assertTrue

**Assertions as Predicates**  
→ PDF pp. 519–524 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Common ZIO Assertions**  
→ PDF pp. 525–528 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Smart Assertions**  
→ PDF pp. 529–532 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch35"></a>
## Testing: The Test Environment

*PDF pp. 535–554*

Test environment.

zio.dev reference: [Test services](https://zio.dev/reference/test/services/), [Live](https://zio.dev/reference/test/services/live/)

*Terms:* TestClock, TestConsole, TestRandom, live environment

**Test Implementation of Standard Services**  
→ PDF pp. 535–546 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Accessing the Live Environment**  
→ PDF pp. 547–548 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Creating Custom Test Implementations**  
→ PDF pp. 549–553 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch36"></a>
## Testing: Test Aspects

*PDF pp. 555–572*

Test aspects.

zio.dev reference: [Test aspects](https://zio.dev/reference/test/aspects/)

*Terms:* TestAspect, repeats, retries, timeouts, platform-specific

**Test Aspects as Polymorphic Functions**  
→ PDF p. 558 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Ability to Constrain Types**  
→ PDF pp. 559–561 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Common Test Aspects**  
→ PDF pp. 562–563 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Repeating and Retrying Tests**  
→ PDF pp. 564–570 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch37"></a>
## Testing: Using Resources in Tests

*PDF pp. 573–578*

Resources in tests.

zio.dev reference: [Sharing layers across files](https://zio.dev/reference/test/sharing-layers-between-multiple-files/), [within a file](https://zio.dev/reference/test/sharing-layers-within-the-same-file/)

*Terms:* provideLayer, shared layers, test resources

**Providing Resources to Tests**  
→ PDF p. 574 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Sharing Resources Between Test Iterations**  
→ PDF p. 575 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Providing Resources to Test Suites**  
→ PDF p. 576 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Sharing Resources Between Tests**  
→ PDF pp. 576–577 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch38"></a>
## Testing: Property-Based Testing

*PDF pp. 579–604*

Property-based testing.

zio.dev reference: [Property testing](https://zio.dev/reference/test/property-testing/), [Shrinking](https://zio.dev/reference/test/property-testing/shrinking/)

*Terms:* Gen, generators, shrinking, check

**Generators as Streams of Samples**  
→ PDF pp. 583–584 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Constructing Generators**  
→ PDF pp. 585–586 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Operators on Generators**  
→ PDF pp. 587–593 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Random and Deterministic Generators**  
→ PDF pp. 594–597 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Samples and Shrinking**  
→ PDF pp. 598–601 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch39"></a>
## Testing: Test Annotations

*PDF pp. 605–612*

Test annotations.

zio.dev reference: [Annotating tests](https://zio.dev/reference/test/aspects/annotating-tests/)

*Terms:* tagging, annotations, reporters

**Tagging Tests**  
→ PDF p. 605 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**How Test Annotations Works**  
→ PDF pp. 606–607 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Test Annotations in Tests**  
→ PDF p. 608 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Using Test Annotations in Test Aspects**  
→ PDF pp. 609–610 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Implementing Test Annotation Reporter**  
→ PDF p. 611 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch40"></a>
## Testing: Reporting

*PDF pp. 613–616*

Test reporting.

zio.dev reference: [Running tests](https://zio.dev/reference/test/running-tests/)

*Terms:* reporting, test results

**Gathering Data**  
→ PDF pp. 613–614 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Analyzing Data**  
→ PDF p. 615 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch41"></a>
## Applications: Parallel Web Crawler

*PDF pp. 617–634*

A parallel web crawler application.

*Terms:* web crawler, parallelism, testability, Queue, Ref

**Definition of a Parallel Web Crawler**  
→ PDF pp. 618–619 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Interacting with Web Data**  
→ PDF pp. 620–623 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**First Sketch of a Parallel Web Crawler**  
→ PDF pp. 624–626 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Making It Testable**  
→ PDF pp. 627–628 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Scaling It Up**  
→ PDF pp. 629–633 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch42"></a>
## Appendix 1: The Scala Type System

*PDF pp. 635–648*

Scala type system essentials.

*Terms:* subtyping, Any, Nothing, union and intersection types, type constructors

**Types And Values**  
→ PDF p. 635 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Subtyping**  
→ PDF p. 636 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Any and Nothing**  
→ PDF pp. 637–639 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Product and Sum Types**  
→ PDF pp. 640–642 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Intersection and Union Types**  
→ PDF pp. 643–645 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Type Constructors**  
→ PDF pp. 646–647 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)


---

<a id="ch43"></a>
## Appendix 2: Mastering Variance

*PDF pp. 649–681*

Variance.

*Terms:* covariance, contravariance, invariance, variance positions

**Definition of Variance**  
→ PDF pp. 649–650 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Covariance**  
→ PDF pp. 651–654 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Contravariance**  
→ PDF pp. 655–658 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Invariance**  
→ PDF pp. 659–660 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

**Advanced Variance**  
→ PDF pp. 661–664 in [the PDF](https://drive.google.com/file/d/1Mm9QlnS38BmXS47ZiY6Ne1Aw18malK6c/view)

