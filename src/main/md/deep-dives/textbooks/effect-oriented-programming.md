<a id="ch1"></a>
# Effect Oriented Programming

> Bill Frasure, Bruce Eckel and James Ward · Scala 3 and ZIO 2 · [the PDF in Drive](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

Summaries are in our own words; the text stays in the PDF.

## The book in one paragraph

An introduction to effect systems for working programmers, using Scala 3 and ZIO. An effect is any unpredictable interaction with the outside world (clocks, files, networks, randomness, mutation); wrapping effects as values that describe work instead of doing it gives back control. The book shows what that buys: retries, timeouts, fallbacks and finalizers added without changing the code they wrap; dependencies modeled as layers and wired into a graph; deterministic tests with controllable clocks and randomness; typed failures in place of thrown exceptions; composition with existing Scala types; safe shared state; and resilience patterns such as caching, rate limiting, circuit breaking and hedged requests.

**Contents**

1. [1: Preface](ch1): Why Scala 3 and ZIO, how to run the examples.
2. [2: Introduction](ch2): What effects are and why unmanaged effects make software hard to change.
3. [3: Superpowers](ch3): Behaviors you can attach to any effect once it is a value.
4. [4: Initialization](ch4): Managing dependencies as effects with ZIO layers.
5. [5: Testing](ch5): Testing effectful code with ZIO Test and its controllable services.
6. [6: Failure](ch6): Failures as typed values instead of exceptions.
7. [7: Composability](ch7): How ZIO effects compose with each other and with Future, Option, Either, Try and resources.
8. [8: Shared State](ch8): Mutable state shared safely between concurrent effects.
9. [9: Resilience](ch9): Patterns for keeping services responsive under load and failure.


---

## 1: Preface

*PDF pp. 7–10*

Why Scala 3 and ZIO, how to run the examples.

**1.1: Scala 3 & ZIO**  
The choice of Scala 3 and ZIO.  
*Terms:* Scala 3, ZIO  
→ PDF p. 7 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**1.2: Code Examples**  
How the code examples are organized and run.  
*Terms:* code examples, sbt  
→ PDF pp. 8–9 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**1.3: Acknowledgements**  
Acknowledgements.  
*Terms:* acknowledgements  
→ PDF p. 10 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch2"></a>
## 2: Introduction

*PDF pp. 11–20*

What effects are and why unmanaged effects make software hard to change.

**2.1: Types of Effects**  
Kinds of effects, from reading a clock to controlling machinery; effect systems wrap them.  
*Terms:* effect, side effect  
→ PDF p. 11 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**2.2: Motivation**  
Why software built on raw effects resists change.  
*Terms:* motivation  
→ PDF pp. 12–13 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**2.3: The Pursuit of Adaptability**  
Adaptability as the goal.  
*Terms:* adaptability  
→ PDF p. 14 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**2.4: What's Stopping Us?**  
What blocks it: hidden effects and tangled failure handling.  
*Terms:* hidden effects  
→ PDF pp. 15–16 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**2.5: Managing Effects**  
Treating effects as values that a runtime executes.  
*Terms:* effect system, effects as values  
→ PDF pp. 17–19 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**2.6: Improving Your Life**  
The practical payoff.  
*Terms:* benefits  
→ PDF p. 20 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch3"></a>
## 3: Superpowers

*PDF pp. 21–34*

Behaviors you can attach to any effect once it is a value.

**3.1: Retry**  
Retrying failed effects with schedules.  
*Terms:* retry, Schedule  
→ PDF p. 23 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.2: Modifying Failure**  
Mapping and refining error types.  
*Terms:* mapError, error refinement  
→ PDF p. 24 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.3: Timeout**  
Timeouts.  
*Terms:* timeout  
→ PDF p. 25 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.4: Fallback**  
Falling back to alternatives.  
*Terms:* orElse, fallback  
→ PDF p. 26 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.5: Finalization**  
Guaranteed cleanup.  
*Terms:* ensuring, finalization  
→ PDF p. 27 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.6: Timing**  
Measuring how long effects take.  
*Terms:* timed  
→ PDF p. 28 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.7: Filtering**  
Filtering results.  
*Terms:* filter  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.8: Effects are the Sum of Their Parts**  
Combining these behaviors freely.  
*Terms:* combinators  
→ PDF p. 29 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**3.9: Deferred Execution**  
Effects describe work and run only when executed.  
*Terms:* deferred execution, laziness  
→ PDF pp. 30–34 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch4"></a>
## 4: Initialization

*PDF pp. 35–55*

Managing dependencies as effects with ZIO layers.

**4.1: Effects and Dependencies**  
Effects can need services to run.  
*Terms:* dependencies, environment  
→ PDF p. 35 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.2: Defining Dependencies**  
Defining services as traits.  
*Terms:* services, traits  
→ PDF p. 36 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.3: Effects as Dependencies**  
Constructing services with effects.  
*Terms:* ZLayer  
→ PDF p. 37 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.4: Providing Dependencies to Effects**  
Supplying dependencies with provide.  
*Terms:* provide  
→ PDF pp. 38–39 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.5: Dependencies With Dependencies**  
Services that depend on other services.  
*Terms:* layer composition  
→ PDF pp. 40–42 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.6: Naming Dependencies**  
Distinguishing several services of the same type.  
*Terms:* named services  
→ PDF p. 43 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.7: Sharing Dependencies**  
Sharing one instance across consumers.  
*Terms:* shared layers  
→ PDF pp. 44–46 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.8: The Dependency Graph**  
ZIO builds the dependency graph and reports missing pieces at compile time.  
*Terms:* dependency graph  
→ PDF p. 47 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.9: Dependency Cleanup**  
Releasing resources when layers shut down.  
*Terms:* scoped resources, cleanup  
→ PDF p. 48 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.10: Construction Failure**  
Handling failure while constructing a service.  
*Terms:* construction failure  
→ PDF pp. 49–51 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**4.11: External Configuration**  
Loading configuration from outside.  
*Terms:* configuration  
→ PDF pp. 52–55 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch5"></a>
## 5: Testing

*PDF pp. 56–70*

Testing effectful code with ZIO Test and its controllable services.

**5.1: Basic ZIO Testing**  
Writing tests as effects with ZIO Test.  
*Terms:* ZIO Test  
→ PDF pp. 56–61 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**5.2: Test Dependencies**  
Supplying test implementations of services.  
*Terms:* test layers, mocks  
→ PDF pp. 62–63 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**5.3: Testing Built-Ins**  
TestClock, TestRandom, TestConsole and other controllable built-ins.  
*Terms:* TestClock, TestRandom, TestConsole  
→ PDF pp. 64–70 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch6"></a>
## 6: Failure

*PDF pp. 71–86*

Failures as typed values instead of exceptions.

**6.1: Throwing Exceptions**  
Problems with thrown exceptions.  
*Terms:* exceptions  
→ PDF pp. 71–72 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**6.2: The Functional Solution**  
Failures as part of the effect type.  
*Terms:* typed errors  
→ PDF p. 73 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**6.3: Failure Types**  
Designing error types with ADTs.  
*Terms:* error ADT  
→ PDF pp. 73–74 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**6.4: Short-Circuiting**  
How a failure stops the rest of a computation.  
*Terms:* short-circuiting  
→ PDF pp. 75–77 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**6.5: Handling Failures**  
Recovering with catch and fold operators.  
*Terms:* catchAll, fold  
→ PDF pp. 78–81 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**6.6: Multiple Failure Types**  
Combining effects with different error types.  
*Terms:* union types, multiple errors  
→ PDF pp. 82–83 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**6.7: Handling Thrown Exceptions**  
Wrapping legacy code that throws.  
*Terms:* ZIO.attempt  
→ PDF pp. 84–86 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch7"></a>
## 7: Composability

*PDF pp. 87–111*

How ZIO effects compose with each other and with Future, Option, Either, Try and resources.

**7.1: Composing with Effects**  
Effects compose because they are values.  
*Terms:* composition  
→ PDF p. 88 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.2: Future**  
Interop with Future.  
*Terms:* Future  
→ PDF pp. 89–91 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.3: Option**  
With Option.  
*Terms:* Option  
→ PDF pp. 92–93 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.4: Either**  
With Either.  
*Terms:* Either  
→ PDF p. 94 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.5: AutoCloseable**  
Resource safety for AutoCloseable.  
*Terms:* AutoCloseable, acquireRelease  
→ PDF pp. 95–98 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.6: Try**  
With Try.  
*Terms:* Try  
→ PDF p. 99 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.7: Exceptions**  
With exception-throwing code.  
*Terms:* exceptions interop  
→ PDF pp. 100–101 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.8: Slow Functions**  
Wrapping blocking or slow calls.  
*Terms:* blocking, attemptBlocking  
→ PDF pp. 102–103 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.9: Composing an Application**  
Assembling a full application from parts.  
*Terms:* application assembly  
→ PDF pp. 104–109 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**7.10: Effects are Values**  
Recap: effects as values.  
*Terms:* effects as values  
→ PDF pp. 110–111 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch8"></a>
## 8: Shared State

*PDF pp. 112–119*

Mutable state shared safely between concurrent effects.

**8.1: Unreliable State**  
Races with plain mutable variables.  
*Terms:* race conditions, mutable state  
→ PDF p. 112 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**8.2: Reliable State**  
Ref for atomic shared state.  
*Terms:* Ref  
→ PDF p. 113 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**8.3: Effects Are Not Allowed**  
Why effects aren’t allowed inside Ref updates.  
*Terms:* pure updates  
→ PDF p. 114 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**8.4: Sneaking in Side Effects**  
Ways side effects can sneak in anyway.  
*Terms:* side effects  
→ PDF pp. 115–116 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**8.5: Reliable Effects**  
Ref.Synchronized for effectful updates.  
*Terms:* Ref.Synchronized  
→ PDF pp. 117–119 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)


---

<a id="ch9"></a>
## 9: Resilience

*PDF pp. 120–147*

Patterns for keeping services responsive under load and failure.

**9.1: Caching**  
Caching results.  
*Terms:* caching  
→ PDF pp. 120–124 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**9.2: Rate Limits**  
Respecting rate limits.  
*Terms:* rate limiting  
→ PDF pp. 125–128 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**9.3: Constraining Concurrent Requests**  
Bounding concurrent requests.  
*Terms:* concurrency limits, semaphore  
→ PDF pp. 129–131 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**9.4: Circuit Breaking**  
Circuit breakers to stop calling failing services.  
*Terms:* circuit breaker  
→ PDF pp. 132–135 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**9.5: Reducing Worst-Case Latency**  
Hedging requests to cut tail latency.  
*Terms:* hedged requests, tail latency  
→ PDF pp. 136–139 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**9.6: Test Resilience**  
Testing resilience behavior.  
*Terms:* resilience testing  
→ PDF pp. 140–142 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

**9.7: The Ecosystem of Effects**  
The wider ZIO ecosystem of effect libraries.  
*Terms:* ZIO ecosystem  
→ PDF pp. 143–147 in [the PDF](https://drive.google.com/file/d/1YWYWwxMHolLIN-YJ6qgDgDy2L2x0XKkx/view)

