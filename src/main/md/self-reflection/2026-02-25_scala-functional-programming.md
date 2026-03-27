---
title: Scala & Functional Programming
created: 2026-02-25
source: personal notes (self.md, self-1.md)
---

# Scala & Functional Programming

> Derived from personal notes · Created: 2026-02-25

Collected links, notes, and code snippets on Scala 3, ZIO, Kyo, Haskell, Rust, functional effects, type theory, and related FP topics.

---

<a id="ch1"></a>
## ZIO / Scala Effect Systems

**ZIO Actors (John De Goes tweet)**
John De Goes's tweet introducing or discussing ZIO Actors — a library for building actor-based concurrent systems on top of ZIO's fiber runtime. Actors provide location-transparent message passing as an alternative to direct functional composition.
<https://twitter.com/jdegoes/status/1600917565625270272>

**ZIO Telemetry**
OpenTelemetry integration for ZIO applications: tracing, metrics, and logging emitted via the OpenTelemetry standard. ZIO Telemetry enables distributed tracing across fiber-based services without manual instrumentation plumbing.
<https://github.com/zio/zio-telemetry>

**ZIO NIO**
Non-blocking I/O for ZIO built on Java NIO, providing purely functional wrappers for channels, selectors, and file operations. ZIO NIO allows building high-performance I/O pipelines that compose cleanly with other ZIO effects.
<https://github.com/zio/zio-nio>

**Alvin Alexander: What Are the Benefits of ZIO and FP? — ZIO Direct**
Alvin Alexander's LinkedIn post prompted by a Twitter question on ZIO/FP benefits, using ZIO Direct as the entry point. ZIO Direct enables direct-style (non-monadic) Scala code that desugars to proper ZIO effect composition, lowering the learning curve significantly.
<https://www.linkedin.com/posts/alvinalexander_github-ziozio-direct-direct-style-programming-activity-7247368581145923584-gS3l>

**ZIO 2.x Migration Guide — zio.dev**
Official migration guide for upgrading from ZIO 1.x to ZIO 2.x: API changes, renamed combinators, the new ZIO Layer model, and the removal of Has type-class wiring. Essential reference for any production ZIO 1 codebase planning a version upgrade.
<https://zio.dev/guides/migrate/zio-2.x-migration-guide/>

**ZIO Schema**
ZIO Schema enables automatic derivation of serialization, validation, migration, and diffing logic from data type definitions, without runtime reflection. It is a core component of the Kyo AI project for JSON schema derivation from Scala case classes.
<https://zio.dev/zio-schema/>

**Zymposium: ZIO 2.0 (John De Goes, Adam Fraser)**
In-depth technical presentation of ZIO 2.0 by its creators: the new fiber-based runtime, performance improvements, the Layer model replacing manual dependency injection, and API simplifications. Essential viewing for Scala engineers planning a ZIO 2 adoption.
<https://www.youtube.com/watch?v=6A1SA5Be9qw>

**John De Goes — Reimagining Functional Type Classes**
John De Goes's exploration of how to redesign functional type class hierarchies from scratch, addressing coherence, orphan instances, and deriving. A deep dive into the theoretical tensions and practical trade-offs of type class design in Scala.
<https://www.youtube.com/watch?v=oluPEFlXumw>

**Streams in ZIO (John De Goes tweet)**
Tweet discussing ZIO Streams — the ZIO library's composable streaming abstraction built on fibers. ZIO Streams unify streaming and effect composition in a way that avoids the separate streaming monad transformer stacks required in other functional ecosystems.
<https://twitter.com/jdegoes/status/1565001020918034432>

**The Effect Pattern — Michael Arnaldi (effectful.co)**
Michael Arnaldi's framework for thinking about effects in functional programming: the idea that effects represent descriptions of computations rather than executions, enabling compositional and testable programs. Arnaldi later developed the Effect TypeScript library based on these ideas.
<https://effectful.co>

**Compositional Resource Management in Scala 3 with ZIO**
Blog post by Pierre Ricadat on managing resources (database connections, file handles, HTTP clients) in a composable way using ZIO's scoped resources and ZLayer. Demonstrates how resource lifecycle integrates naturally with ZIO's effect composition.
<https://blog.pierre-ricadat.com/compositional-resource-management-in-scala-3-with-zio>

---

## Kyo Effect System

**Kyo — Scala 3 Effect System (Flavio Brasil)**
Kyo is a novel Scala 3 effect system by Flavio Brasil that encodes algebraic effects without monad transformers, using an intersection type approach for effect composition. Unlike ZIO's monadic stack, Kyo effects are composable through normal function calls, enabling direct-style code without desugaring steps.
<https://github.com/getkyo/kyo>

**kyo-chatgpt Example**
A small application demonstrating Kyo effects integrated with OpenAI's ChatGPT API, showing how AI interactions compose with other effects (IO, error, concurrency) in a Kyo application. Predecessor to the kyo-ai project.
<https://github.com/fwbrasil/kyo/tree/main/kyo-chatgpt>

**Kyo: Crafting Scala's Futuristic Effects (YouTube)**
Conference talk by Flavio Brasil introducing Kyo's intersection-type effect encoding, explaining why it avoids the monadic composition tax and how it achieves performance competitive with direct IO implementations.
<https://www.youtube.com/watch?v=cyGSLCXR4Bo>

---

## Safe Direct-Style Scala / Structured Concurrency

**Safe Direct-Style Scala: Ox 0.1.0 Released (SoftwareMill)**
Ox is a SoftwareMill library for structured concurrency in Scala 3 using direct style — no monads, no futures, just blocking fibers with structured lifetime scopes. The 0.1.0 release announcement explains the design goals and how Ox compares to ZIO and cats-effect.
<https://softwaremill.com/ox-0-1-0-released-safe-direct-style-scala/>

**Comparing Approaches to Structured Concurrency (LambdaConf 2024)**
James Ward and Adam Hearn compare structured concurrency models across Scala (ZIO, cats-effect, Ox), Kotlin coroutines, and Go, examining how each handles cancellation, error propagation, and resource safety. Provides a vendor-neutral framework for evaluating concurrency abstractions.
<https://www.youtube.com/watch?v=g6dyLhAublQ>

**EasyRacer LambdaConf 2024 (James Ward)**
EasyRacer is a benchmark comparing how different frameworks and languages implement ten concurrent racing scenarios — selecting the first successful result from parallel tasks. Used in the LambdaConf talk to objectively compare ZIO, cats-effect, Ox, Akka, and other approaches.
<https://jamesward.github.io/easyracer/>

**Coroutines and Effects (without.boats)**
Withoutboats's essay examining the relationship between coroutines (as in Rust async/await) and algebraic effects, arguing that coroutines are a restricted form of effects that compile down to state machines. Essential context for understanding why Rust chose coroutines over a more general effect system.
<https://without.boats/blog/coroutines-and-effects/>

---

## Scala 3 Language Features & Patterns

**Scala HTMX Web Apps (Igal Tabachnik, RockTheJVM)**
Igal Tabachnik's Twitter discussion and RockTheJVM content on building server-side web applications in Scala using HTMX — a hypermedia-driven approach that eliminates the need for a JavaScript frontend framework while still delivering dynamic UI interactions.
<https://twitter.com/igal_tabachnik>

**Scala 3 — End Markers, Given Instances, Sealed Traits (official docs)**
Official Scala 3 reference documentation for language features introduced in Scala 3: end markers for large blocks, given/using for type class instances, and sealed trait exhaustivity checking. Core reading for any developer migrating from Scala 2 to Scala 3.
<https://docs.scala-lang.org/scala3/reference/>

**Scala CLI**
Scala CLI is a modern command-line tool for running, compiling, testing, and packaging Scala code without a full SBT project setup. It enables single-file Scala scripts, inline dependencies, and rapid prototyping — significantly lowering the barrier for writing quick Scala utilities.
<https://scala-cli.virtuslab.org/>

**sbt-assembly**
SBT plugin for creating fat JARs (assembly JARs) by merging all dependencies into a single deployable artifact. Essential for deploying Scala applications to environments without Maven dependency resolution, including many data engineering and streaming platforms.
<https://github.com/sbt/sbt-assembly>

**The Evolution of Effects (Haskell'23 Keynote, Nicolas Wu)**
Nicolas Wu's Haskell Symposium 2023 keynote tracing the evolution of effect systems from Haskell's IO monad through monad transformers, free monads, and algebraic effects — contextualizing where algebraic effect systems like Kyo fit in the intellectual history of functional programming.
<https://icfp23.sigplan.org/details/haskellsymp-2023/10/The-Evolution-of-Effects>

**What Is So Unique About Unison? (Etienne Torreborre blog)**
Torreborre — specs2 author — explains what makes the Unison programming language unusual: content-addressed code, no dependency hell, abilities (algebraic effects), and distributed computing built into the language semantics. A thoughtful comparison with Haskell and Scala.
<https://etorreborre.blog/>

**Unison Is Crack for Backend Software Engineers (neander.tech)**
A detailed personal account of why Unison's packaging and deployment model is uniquely compelling for backend engineers, eliminating dependency conflicts and enabling code to be deployed to the cloud as a first-class language operation rather than an infrastructure concern.
<https://neander.tech/2024-07-31-unison-is-crack>

**FUNARCH 2024 — Functional Architecture**
The Functional Software Architecture workshop at ICFP 2024, focused on methods for structuring large, long-lived software projects using functional programming principles. Covers DDD with FP, hexagonal architecture in FP, and effect system design for scalable codebases.
<https://functional-architecture.org/events/funarch-2024/>

**FP Meets OS: The Case of I/O — Vitaly Bragilevsky (LambdaConf 2024)**
Keynote examining how functional programming abstractions map onto operating system I/O primitives: how the IO monad, fibers, and async effects relate to kernel system calls, epoll, and OS scheduling. Bridges FP abstraction theory with systems programming reality.
<https://www.youtube.com/watch?v=ZGyIp8oalmE>

**What Does It Mean That a Language Has an "Effect System"? (langdev.stackexchange.com)**
Stack Exchange language design discussion explaining effect systems to those unfamiliar with the concept: what effects are tracked, how the type system encodes them, and how effect systems compare to monadic I/O and algebraic effects in terms of expressivity and ergonomics.
<https://langdev.stackexchange.com/questions/3726/what-does-it-mean-that-a-language-has-an-effect-system>

**Higher Order Company / HVM / Bend Language**
Higher Order Company's HVM (Higher-order Virtual Machine) is a parallel runtime based on interaction nets that can execute functional programs on many CPU cores or GPU threads without explicit parallelism annotations. Bend is the high-level language targeting HVM.
<https://higherorderco.com/>

---

<a id="ch2"></a>
## Rust

**Rust Design Patterns (rust-unofficial.github.io)**
Community-maintained book of idiomatic Rust patterns: RAII guards, type state machines, builder pattern, newtype wrappers, and anti-patterns to avoid. Essential reference for writing Rust code that leverages the borrow checker's guarantees rather than fighting them.
<https://rust-unofficial.github.io/patterns/>

**Rust Cheat Sheet**
Quick-reference guide to Rust syntax: lifetimes, trait bounds, closures, iterators, pattern matching, and common standard library APIs. Useful as a desktop companion for developers who know Rust but need to recall specific syntax during coding sessions.
<https://upsuper.github.io/rust-cheatsheet/>

**Type-Level Programming in Rust (Will Crichton)**
Will Crichton's guide to expressing invariants and constraints in Rust's type system: phantom data, zero-sized types, associated types, and const generics for encoding state machines and API contracts at compile time rather than at runtime.
<https://willcrichton.net/rust-api-type-patterns/>

**graydon2: Notes on Rust, Mutable Aliasing, and Formal Verification**
Graydon Hoare's — Rust's original creator — blog on the relationship between Rust's aliasing rules and formal verification: how the borrow checker's guarantees enable both safe concurrency and machine-checkable correctness proofs.
<https://graydon2.dreamwidth.org/>

**Rust Formal Verification (xav.io)**
Resource on formally verifying Rust programs using tools like Kani, Creusot, and Prusti — leveraging Rust's ownership model to make verification tractable. An active research area connecting Rust's type system to formal methods.
<https://xav.io/>

**100 Exercises To Learn Rust (rust-exercises.com)**
Structured curriculum of 100 progressive Rust exercises, starting from basic types and ownership through iterators, traits, and error handling. Particularly effective because it provides a compiler-driven feedback loop — exercises only pass when the Rust code is correct.
<https://rust-exercises.com/02_basic_calculator/00_intro>

**Rust Atomics and Locks — Mara Bos**
Comprehensive book on low-level concurrent programming in Rust: memory ordering, atomic operations, spinlocks, mutexes, and condition variables implemented from first principles. Required reading for systems programmers building lock-free data structures in Rust.
<https://marabos.nl/atomics/>

**Implementing Git from Scratch in Rust (Jon Gjengset, YouTube)**
Jon Gjengset's extended live-coding session implementing a significant portion of git in Rust, demonstrating how to apply Rust idioms to a real-world systems project: object storage, pack files, delta compression, and the ref system.
<https://www.youtube.com/watch?v=u0VotuGzD_w>

**Golem's Rust Transaction API (blog.vigoo.dev)**
Daniel Vigovszky's blog on building a transactional API in Rust for the Golem platform — a distributed computing runtime. Covers how Rust's ownership model interacts with distributed system guarantees and durable execution primitives.
<https://blog.vigoo.dev/>

**LogLog Games: Leaving Rust Gamedev**
LogLog Games' post-mortem on choosing to leave Rust for game development: the cognitive overhead of the borrow checker in game entity system patterns, compile times, and the ergonomic friction of dynamic dispatch in performance-critical game loops. A balanced critique from practitioners.
<https://loglog.games/blog/leaving-rust-gamedev/>

**Google Hails Move to Rust for Drop in Memory Vulnerabilities**
Google's report on the measurable security improvement from migrating Android and other components from C++ to Rust: memory safety vulnerabilities in migrated code dropped to near zero, validating Rust's ownership model as a practical security engineering tool.
<https://www.yahoo.com/tech/google-hails-move-rust-huge-180100292.html>

**Introducing Distill CLI — Rust-Powered Media Summarization (allthingsdistributed.com)**
Werner Vogels (AWS CTO) introduces Distill CLI — an efficient Rust tool for summarizing media files using LLMs — with a code review story about learning Rust from Amazon Rustaceans. A pragmatic example of Rust adoption for performance-sensitive CLI tooling.
<https://www.allthingsdistributed.com/2024/06/introducing-distill-cli.html>

**Hands-On Data Structures and Algorithms With Rust (San Mateo County Libraries)**
Library record for a book implementing classic data structures and algorithms in Rust: trees, graphs, sorting, and dynamic programming. Bridges algorithmic fundamentals with Rust-specific ownership patterns.
<https://smcl.bibliocommons.com/v2/record/S76C3254158>

**Breaking Out of the Fold (Ethan Kent's Dev Blog)**
Essay on the problem of early termination within fold/reduce operations in functional languages: the challenge of short-circuiting without exceptions, using techniques like returning early via Option, Either, or lazy evaluation. Examines how different languages handle this.
<https://ethankent.dev/posts/breaking_fold/>

---

## Rust LeetCode Solutions (Knight's Tour)

**Rust: Check Valid Grid (Knight's Tour Validation)**
Rust implementation of LeetCode's knight's tour grid validation problem, using fold for traversal and custom Move/Rc structs for position tracking. The optimized version eliminates the visited array by leveraging the grid's value sequence as implicit state.
```rust
impl Solution {
    pub fn check_valid_grid(grid: Vec<Vec<i32>>) -> bool {
        #[derive(Copy, Clone)]
        struct Move{row: isize, col: isize}
        #[derive(Copy, Clone)]
        struct Rc{row: usize, col: usize}
        fn mv(row: isize, col: isize) -> Move {
            Move{row: row, col:col}
        }

        fn check_init(grid: &Vec<Vec<i32>>) -> bool {
            (grid.len() > 0) && (grid[0].len() > 0) && (grid[0][0] == 0)
        }

        fn get_next(grid: &Vec<Vec<i32>>, curr : Rc, n: isize) -> Option<Rc> {
            let moves: Vec<Move> = vec!(mv(-2, -1), mv(-2, 1), mv(-1, -2), mv(-1, 2 ), mv(1, 2), mv(1, -2), mv(2, 1), mv(2, -1));
            let knight_step = grid[curr.row][curr.col];
            moves.iter().fold(None, |next_pos_o, m| {
                let r = m.row + curr.row as isize;
                let c = m.col + curr.col as isize;
                next_pos_o.or_else(|| {
                    if ((r >= 0) && (r < n) && (c >= 0) && (c < n) &&
                        (grid[r as usize][c as usize] == knight_step + 1)) {
                        Some(Rc{row:r as usize, col:c as usize})
                    } else {
                        None
                    }})
            })
        }

        fn check_tour(grid: &Vec<Vec<i32>>) -> bool {
            let n = grid.len() as isize;
            let mut curr = Rc{row: 0, col: 0};
            let mut next_o = get_next(grid, curr, n);
            while (next_o.is_some()) {
                curr = next_o.map_or_else(|| curr,  |n| n);
                next_o = get_next(grid, Rc{row: curr.row, col: curr.col}, n);
            }
            grid[curr.row][curr.col] == ((n*n - 1) as i32)
        }

        check_init(&grid) && check_tour(&grid)
    }
}
```
Runtime 710ms Beats 100.00%

---

## Scala LeetCode Solutions

### Knight's Tour Validation (Scala)

**Scala: Check Valid Grid — Version 1 and Version 2**
Two Scala implementations of the knight's tour grid validation problem: Version 1 uses an explicit visited buffer (774ms, 50th percentile); Version 2 eliminates the visited set by relying on monotonically increasing step values in the grid (710ms, 100th percentile). The optimization illustrates how understanding problem constraints eliminates unnecessary bookkeeping.
Submitted as "kodebale" at Sep 25, 2024

Version 1 (with visited tracking, 774ms Beats 50%):
```scala
object Solution {
    case class Rc (row:Int, col:Int)
    def checkValidGrid(grid: Array[Array[Int]]): Boolean = {
        val n = grid.size
        def checkInit():Boolean = (n > 0) && (grid(0)(0) == 0)
        val visited = scala.collection.mutable.ArrayBuffer.empty[Rc]
        def getNextRc(currRc:Rc):Option[Rc] = {
            val nrInc = Array(-2, -2, -1, -1, 1,  1, 2,  2)
            val ncInc = Array(-1,  1, -2,  2, 2, -2, 1, -1)
            val knightStep = grid(currRc.row)(currRc.col)
            visited += currRc
            val nextPoss:Array[Rc] = (0 until 8).toArray.flatMap(i => {
              val nr = currRc.row + nrInc(i)
              val nc = currRc.col + ncInc(i)
              val nrc = Rc(nr, nc)
              if ((nr >= 0) && (nr < n) && (nc >= 0) && (nc < n) && (visited.find(rc => nrc == rc).isEmpty)) {
                Array(nrc)
              }
              else {
                Array[Rc]()
              }
            })
            nextPoss.find(rc => grid(rc.row)(rc.col) == knightStep + 1)
        }
        def checkTour() : Boolean = {
           var currO:Option[Rc] = Some(Rc(0,0))
           var nextO = getNextRc(Rc(0,0))
           while(nextO.isDefined) {
             currO = nextO
             nextO = getNextRc(nextO.get)
           }
           val finalrc = currO.getOrElse(Rc(0,0))
           grid(finalrc.row)(finalrc.col) == (n*n)-1
        }
        checkInit() && checkTour()
    }
}
```

Version 2 (optimized, 710ms Beats 100%):
```scala
object Solution {
    case class Rc (row:Int, col:Int)
    def checkValidGrid(grid: Array[Array[Int]]): Boolean = {
        val n = grid.size
        def checkInit():Boolean = (n > 0) && (grid(0)(0) == 0)
        def getNextRc(currRc:Rc):Option[Rc] = {
            val nrInc = Array(-2, -2, -1, -1, 1,  1, 2,  2)
            val ncInc = Array(-1,  1, -2,  2, 2, -2, 1, -1)
            val knightStep = grid(currRc.row)(currRc.col)
            val nextPoss:Array[Rc] = (0 until 8).toArray.flatMap(i => {
              val nr = currRc.row + nrInc(i)
              val nc = currRc.col + ncInc(i)
              val nrc = Rc(nr, nc)
              if ((nr >= 0) && (nr < n) &&
                  (nc >= 0) && (nc < n) &&
                  (grid(nrc.row)(nrc.col) == knightStep + 1)) {
                Array(nrc)
              }
              else {
                Array[Rc]()
              }
            })
            nextPoss.find(rc => grid(rc.row)(rc.col) == knightStep + 1)
        }
        def checkTour() : Boolean = {
           var currO:Option[Rc] = Some(Rc(0,0))
           var nextO = getNextRc(Rc(0,0))
           while(nextO.isDefined) {
             currO = nextO
             nextO = getNextRc(nextO.get)
           }
           val finalrc = currO.getOrElse(Rc(0,0))
           grid(finalrc.row)(finalrc.col) == (n*n)-1
        }
        checkInit() && checkTour()
    }
}
```

---

<a id="ch3"></a>
## Haskell

**Euterpea — Music Composition DSL in Haskell**
Euterpea is a Haskell library for algorithmic music composition developed at Yale, built on Paul Hudak's work connecting functional programming and music theory. It provides abstractions for notes, chords, instruments, and musical transformations that compose like any other Haskell functions.
<https://www.haskell.org/euterpea/>

**Unison Programming Language (Haskell / Stack)**
Unison is a programming language designed and implemented in Haskell using the Stack build tool. Its content-addressed code model, algebraic abilities (effects), and built-in distributed computing make it a unique laboratory for exploring what programming could look like with a clean slate.
<https://github.com/unisonweb/unison>

---

## Nushell

**Writing Shell Scripts in Nushell (jpospisil.com)**
Tutorial on using Nushell's structured data model for scripting: how Nushell represents command output as tables rather than plain text, enabling pipelines that process data without awk/sed parsing. Demonstrates practical Nushell scripting patterns for common automation tasks.
<https://jpospisil.com/2023/writing-shell-scripts-in-nushell>

**Exploring Nushell (LogRocket)**
LogRocket's introduction to Nushell for developers familiar with bash: the type system, plugin architecture, and how structured pipelines simplify operations like filtering JSON or processing CSV that require jq/awk in traditional shells.
<https://blog.logrocket.com/exploring-nushell/>

**In Praise of Nushell (lars.yencken.org)**
Personal essay arguing for Nushell as a superior shell for data-oriented scripting: the comparison to PowerShell's object pipelines, how structured data eliminates fragile text parsing, and why Nushell's learning curve is worth the investment.
<https://lars.yencken.org/in-praise-of-nushell>

**Nushell ArchWiki**
Arch Linux wiki page on installing and configuring Nushell, including integration with system utilities, prompt configuration, and environment variable management. The ArchWiki is often the most concise and accurate reference for shell configuration details.
<https://wiki.archlinux.org/title/Nushell>

**Solene: Nushell Intro Article (dataswamp.org)**
Solène Rapenne's introduction to Nushell from an OpenBSD/sysadmin perspective, focusing on practical day-to-day shell replacement use cases and how Nushell handles the POSIX compatibility trade-offs that prevent it from being a drop-in bash replacement.
<https://dataswamp.org/~solene/>

**casey/just — Command Runner**
`just` is a command runner (not a build tool) that provides a cleaner Makefile alternative for project-specific commands: no implicit dependencies, better error messages, and shell-agnostic syntax. Useful for documenting and standardizing developer workflows.
<https://github.com/casey/just>

### Nushell Command: Parse alar.txt Linkchecker Output to JSON
Nushell regex pipeline for parsing linkchecker output from the alar.ink Kannada dictionary tool into structured JSON — extracting URL, Name, Parent URL, and Real URL fields. Demonstrates Nushell's `parse -r` for regex-based structured extraction and `to json` for output.
```nushell
open alar.txt | parse -r '(((URL *\x60(?P<Url>[^\x27]*)\x27)\n)|((Name *\x60(?P<Name>.*)\x27)\n)|(Parent URL *(?P<Purl>(?P<phttp>[^,]*), line (?P<pline>[^,]*), col (?P<pcol>[^\n]*))\n)|((Real URL *(?P<Rurl>.*))\n)){4}' | select Url Name Rurl phttp pline pcol| to json | save -f "alar-url.txt"
```

### Nushell Kannada Character Class Variables (for alar.ink Analysis)
Nushell environment variable setup defining Kannada character class regex patterns for analyzing the alar.ink Kannada dictionary corpus — vowel blocks, consonant blocks, conjunct consonants — and grepping for words of specific syllable structures.
```nushell
$env.vowelfull = $env.vowel + $env.vowelend
$env.consnooth = $env.cons + $env.consend
$env.consotth1 = $env.cons + $env.hal + $env.cons + $env.consend
$env.consotth2 = $env.cons + $env.hal + $env.cons + $env.hal + $env.cons + $env.consend
$env.block = $"\(\(($env.vowelfull)\)|\(($env.consnooth)\)|\(($env.consotth1)\)|\(($env.consotth2)\)\)"
egrep $"\^($env.block){5}[್]?\$" alar-212-sorted-uniq-2.txt | save -f alar-5.txt
# Result: 21416 words of 5+ syllables
```

---

## The Life and Times of an Abstract Syntax Tree

**The Life and Times of an Abstract Syntax Tree (blog.trailofbits.com)**
Trail of Bits' deep dive into how compilers and analysis tools represent and transform Abstract Syntax Trees: construction, traversal, transformation patterns, and the practical challenges of maintaining source location information through optimization passes.
<https://blog.trailofbits.com/>

---

## Logic / Formal Verification

**CPSC-298: Logic in Software Engineering (Lean), LeanDojo, and Lean Copilot**
Resources on using the Lean 4 theorem prover for formal verification in software engineering: course materials, LeanDojo's environment for training ML-based proof search, and Anima Anandkumar's Lean Copilot for LLM-assisted theorem proving.

**Terry Tao: Pilot Project in Universal Algebra with Machine Assistance**
Terry Tao's blog post on a collaborative mathematics research project exploring universal algebra theorems with machine assistance, describing how crowd-sourced human expertise combined with automated verification tools can tackle problems too large for individual mathematicians.
<https://terrytao.wordpress.com/2024/09/25/a-pilot-project-in-universal-algebra-to-explore-new-ways-to-collaborate-and-use-machine-assistance/>

---

## Concurrency / OS

**Rearchitecting Core Services at X (Mike @cambridgemike)**
Tweet thread by a senior X (Twitter) engineer on the architectural decisions involved in rebuilding core services at X: database choices, service decomposition, and the performance characteristics of their infrastructure at massive scale.
<https://x.com/cambridgemike/status/1835774409786986572>

**TinyURL + PasteBin — Systems Design Interview (YouTube)**
Classic system design interview walkthrough for two foundational distributed systems: URL shortener (TinyURL) and text/code sharing (PasteBin). Covers distributed ID generation, sharding, caching, and CDN strategies applicable across many backend service designs.
<https://youtu.be/5V6Lam8GZo4>

**GitHub: Coder-World04/Complete-System-Design**
Comprehensive system design reference repository covering distributed systems patterns: consistent hashing, CAP theorem, load balancing, sharding strategies, and case studies of how real systems (Netflix, Uber, WhatsApp) implement them.
<https://github.com/Coder-World04/Complete-System-Design>

**GitHub: Coder-World04/Tech-Interview-Important-Topics**
Repository covering the most important topics and techniques for technical interviews at top tech companies: data structures, algorithms, system design, behavioral patterns, and company-specific patterns at Google, Amazon, Meta, and similar firms.
<https://github.com/Coder-World04/Tech-Interview-Important-Topics-and-Techniques>

**Neo Kim: How Instagram Scaled to 2.5 Billion Users (@systemdesign42)**
Detailed Twitter thread from systemdesign42 covering Instagram's scaling journey: from single-server Django app to global multi-region infrastructure — database sharding, CDN, media storage, and the architectural pivots made at each order-of-magnitude growth stage.
<https://x.com/systemdesign42/status/1800491019663970354>

---

## Java

### Dining Philosophers (LeetCode, Java)

**Java: Dining Philosophers Solution**
Classic synchronization problem implementation in Java using ReentrantLocks with a resource hierarchy to prevent deadlock: philosophers always acquire the lower-numbered fork first, breaking circular wait. Demonstrates Java concurrent locking primitives in a canonical CS problem.
```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.ArrayList;

class DiningPhilosophers {
    private final ArrayList<Lock> forks = new ArrayList<Lock>();

    public DiningPhilosophers() {
        for (int i = 0; i < 5; i++) {
            forks.add(new ReentrantLock(false));
        }
    }
    // ... wantsToEat method with lock ordering
}
```
<https://leetcode.com/problems/the-dining-philosophers/>

---

<a id="ch4"></a>
## Nix

**The Determinate Nix Installer — Zero to Nix**
Zero to Nix's guide to the Determinate Systems Nix installer — a more reliable, multi-user Nix installation experience than the official installer. Zero to Nix provides the most beginner-friendly introduction to the Nix ecosystem and its reproducible build guarantees.
<https://zero-to-nix.com/concepts/nix-installer>

---

## Miscellaneous Programming

**Edward Kmett: Why B-Trees Exist and Are Provably Optimal (@kmett)**
Edward Kmett's tweet explaining the information-theoretic and cache-hierarchy reasons why B-trees are provably optimal for many applications — connecting the physical constraints of memory hierarchies to the mathematical analysis of tree branching factors.
<https://x.com/kmett/status/1811904210021286014>

**Erik Meijer: Real Life Case of Law of Excluded Middle — Hallucination (@headinthebox)**
Erik Meijer applies classical logic to the LLM hallucination debate: "Hallucination is Inevitable" vs "AI guarantees accuracy and eliminates hallucinations" — demonstrating how the law of excluded middle forces a choice between these incompatible propositions and what it implies about formal verification of AI systems.
<https://x.com/headinthebox/status/1801087634200199464>

**Satnam Singh: Erik Meijer Tames AI with Lambda Calculus and Big-Step Semantics**
Tweet referencing Erik Meijer's work applying lambda calculus and operational semantics to constrain and reason about AI model behavior. A perspective on formal methods as a framework for AI reliability rather than purely for traditional software.
<https://x.com/satnam6502/status/1817243947800129956>

**Bounties on Scala Open Source (algora.io)**
Algora's bounty console for Scala open source projects: financial incentives for fixing issues, adding features, or improving documentation in the Scala ecosystem. Useful for both finding paid contribution opportunities and incentivizing work on projects you depend on.
<https://console.algora.io/bounties/t/scala>

**Why, After 6 Years, I'm Over GraphQL (bessey.dev)**
A candid post-mortem from a long-time GraphQL practitioner explaining the accumulated frustrations: N+1 query problems at scale, authorization complexity, schema stitching nightmares, and the cases where REST and JSON:API would have been simpler. A useful counterweight to GraphQL evangelism.
<https://bessey.dev/>

**Mathematics in India (bhavana.org.in)**
Bhavana journal's series on the history of mathematics in India: zero, the decimal system, infinite series, combinatorics, and the Āryabhaṭa tradition. Bridges Indian mathematical history with modern number theory and analysis.
<https://bhavana.org.in/mathematics-in-india-6/>

---

<a id="ch5"></a>
## From self-1.md (Oct 2024 – Feb 2026)

**NammaYatri / Haskell Open Source**
NammaYatri is a Bengaluru-based open-source ride-sharing platform built by Juspay entirely in Haskell, demonstrating that Haskell is viable for large-scale production systems beyond academia. Open-sourced in Oct 2024, it is one of the largest public Haskell codebases.
nammayatri.in — <https://nammayatri.in/>

**Yoneda Perspective (YouTube Playlist)**
Video lecture series on the Yoneda lemma — one of the most profound results in category theory — and its significance for functional programming: how it explains the naturality of `fmap`, the representability of functors, and the deep connection between data types and their transformations.
<https://www.youtube.com/playlist?list=PLbgaMIhjbmEnaH_LTkxLI7FMa2HsnawM_>

**Graham Hutton Publications**
Research papers and books by Graham Hutton on functional programming: most famously "Programming in Haskell" and his work on fold/unfold as universal recursive operators. Hutton's publications are among the clearest formal treatments of functional programming principles.
cs.nott.ac.uk — <http://www.cs.nott.ac.uk/~pszgmh/>

**GitHub: openai/lean-gym**
OpenAI's Lean 4 reinforcement learning environment for training AI agents to generate and verify mathematical proofs. Lean-gym was a key infrastructure piece behind the AlphaProof and related neural theorem prover research directions.
github.com — <https://github.com/openai/lean-gym>

**LeanDojo**
LeanDojo is an open-source toolkit providing a Lean 4 proof environment, tactic state extraction, and dataset generation infrastructure for training machine learning models on formal mathematics. Used as the basis for multiple neural theorem prover research projects.
leandojo.org — <https://leandojo.org/>

**Fermat's Last Theorem in Lean**
Ongoing Lean 4 formalization project aiming to produce a machine-checkable proof of Fermat's Last Theorem — Andrew Wiles's 1994 proof — covering hundreds of pages of advanced number theory. A landmark in the computer formalization of modern mathematics.
leanprover-community.github.io — <https://leanprover-community.github.io/>

**Domain Modelling Made Functional (Scott Wlaschin)**
Scott Wlaschin's book applying Domain-Driven Design to F# functional programming, using algebraic data types (discriminated unions) to make illegal states unrepresentable. The DDD/FP synthesis applies equally to Scala, Haskell, and other strongly typed functional languages.
fsharpforfunandprofit.com — <https://fsharpforfunandprofit.com/books/>

**Finger Trees Paper (Hinze & Paterson)**
The classic 2006 paper introducing 2-3 finger trees — a purely functional sequence data structure with amortized O(1) operations at both ends and O(log n) splits and concatenations. Finger trees underlie many persistent sequence implementations in functional languages including Haskell's `Data.Sequence`.
staff.city.ac.uk — <http://staff.city.ac.uk/~ross/papers/FingerTree.html>

**RRB Trees — Relaxed Radix Balanced Trees**
Phil Bagwell and Tiark Rompf's EPFL paper on Relaxed Radix Balanced Trees — the persistent vector data structure powering Scala's immutable Vector and Clojure's PersistentVector. RRB trees provide efficient O(log₃₂ n) operations and O(log n) concatenation for functional sequences.
infoscience.epfl.ch — <https://infoscience.epfl.ch/record/169879>

**Hylomorphisms**
A hylomorphism is a recursion scheme combining an anamorphism (unfold, building up a structure) with a catamorphism (fold, consuming the structure) — a pattern that naturally expresses divide-and-conquer algorithms. Mergesort is the canonical hylomorphism example.
blog.sumtypeofway.com — <https://blog.sumtypeofway.com/posts/recursion-schemes-part-4-5.html>

**Recursion Schemes Intro (Sum Type of Way)**
Patrick Thomson's approachable introduction to recursion schemes: cata (fold over structure), ana (unfold into structure), and para (fold with access to original subtrees). Demonstrates how to eliminate explicit recursion and express structural algorithms as pattern-matched scheme applications.
blog.sumtypeofway.com — <https://blog.sumtypeofway.com/posts/introduction-to-recursion-schemes.html>

**Catamorphisms (HaskellWiki)**
HaskellWiki's reference on catamorphisms — the generalization of fold to arbitrary algebraic data types defined as initial algebras of functors. Explains the F-algebra formulation and how GHC's `Data.Fix` and libraries like `recursion-schemes` express catamorphisms in practice.
wiki.haskell.org — <https://wiki.haskell.org/Catamorphisms>

**"Oh, the Morphisms You'll See!" (Patrick Thomson)**
Patrick Thomson's survey of exotic recursion schemes beyond cata and ana: histomorphism (history), futumorphism (future), zygomorphism (co-recursion), chronomorphism, and their applications. Demonstrates that virtually any recursive algorithm corresponds to a named morphism in the scheme taxonomy.
blog.sumtypeofway.com — <https://blog.sumtypeofway.com/posts/recursion-schemes-part-6.html>

**FP Jargon Glossary**
Plain-English definitions of functional programming terminology: monad, functor, applicative, semigroup, monoid, natural transformation, free monad, and more. Useful onboarding reference for developers encountering FP abstractions for the first time in Scala or Haskell codebases.
github.com — <https://github.com/hemanth/functional-programming-jargon>

**Ralf Hinze Publications**
Academic papers by Ralf Hinze on functional data structures and generic programming: finger trees, generalized tries, and the `Data.Generics` approach to polytypic programming in Haskell. A core contributor to the theoretical foundations of functional data structures.
cs.ox.ac.uk — <https://www.cs.ox.ac.uk/ralf.hinze/>

**Constraints Liberate, Liberties Constrain (Runar Bjarnason)**
Runar Bjarnason's influential talk arguing that more constrained types lead to more polymorphic, composable, and reusable functions — a counter-intuitive thesis that is central to the Haskell and Scala functional programming philosophy. The "parametricity" argument in accessible form.
<https://www.youtube.com/watch?v=GqmsQeSzMdw>

**Simple Made Easy (Rich Hickey)**
Rich Hickey's seminal talk distinguishing "simple" (not complex, not interleaved) from "easy" (near, familiar, easy to reach): arguing that programming culture's pursuit of ease over simplicity produces incidental complexity that compounds over time. One of the most cited talks in the software engineering community.
<https://www.youtube.com/watch?v=LKtk3HCgTa8>

**Haskell Notes for Professionals**
Free Haskell reference book compiled from Stack Overflow answers: type classes, monads, concurrency, Template Haskell, and common GHC extensions. A quick-reference companion to the Haskell Report for working Haskell programmers.
goalkicker.com — <https://goalkicker.com/HaskellBook/>

**SplinterDB**
VMware Research's high-performance key-value store with a novel B-tree variant (SplinterTree) designed to reduce write amplification in SSDs. Represents active research at the intersection of functional data structures, disk I/O optimization, and storage engine design.
github.com — <https://github.com/vmware/splinterdb>

**MoonBit Language**
MoonBit is a new statically-typed, functional-style programming language targeting WebAssembly (WASM) with an emphasis on performance, small binary size, and developer experience. Designed as a practical alternative to Rust for WASM compilation.
moonbitlang.com — <https://www.moonbitlang.com/>

**Mind-Bending GPU Language — Bend**
Bend is a high-level functional language by Higher Order Company that compiles to their HVM parallel runtime, executing on many CPU/GPU cores via interaction nets without explicit parallel annotations. Represents a novel approach to massively parallel functional programming.
github.com — <https://github.com/HigherOrderCO/Bend>

**8 Months of OCaml After Haskell (chshersh)**
Dmitrii Kovanikov's retrospective on switching from Haskell to OCaml after 8 months: what OCaml does better (pragmatic tooling, type inference, effect handlers), what is worse (less expressive type classes, fewer category theory abstractions), and the culture differences between the two communities.
chshersh.com — <https://chshersh.com/blog/2023-12-16-ocaml-after-haskell.html>

**Static Search Trees — 40x Faster Than Binary Search (algorithmica.org)**
Algorithmica's explanation of the cache-oblivious Eytzinger layout for static sorted arrays: by rearranging elements in BFS order, prefetching eliminates memory latency bottlenecks, achieving 40x throughput versus naive binary search on modern CPUs. A profound example of hardware-aware algorithm design.
algorithmica.org — <https://algorithmica.org/en/eytzinger>

**Unison Docs — Abilities (Effects)**
Official Unison language documentation on "abilities" — Unison's name for algebraic effects. The abilities system is a core language feature that distinguishes Unison from Haskell/Scala effect libraries: effects are first-class types rather than library-level abstractions.
unison-lang.org — <https://www.unison-lang.org/learn/fundamentals/abilities/>

**Category Theory Catsters (YouTube — Eugenia Cheng)**
Eugenia Cheng's lecture series on category theory for mathematicians: functors, natural transformations, adjunctions, limits, colimits, and monoidal categories. One of the best video resources connecting pure category theory to the abstractions used in functional programming.
<https://www.youtube.com/user/TheCatsters>

**Comonads Are Objects (haskellforall.com)**
Gabriel Gonzalez's blog post demonstrating that comonads — the categorical dual of monads — are precisely what OOP calls "objects": they package state with behavior, offering a rigorous categorical foundation for object-oriented programming from a functional perspective.
haskellforall.com — <https://www.haskellforall.com/2013/02/you-could-have-invented-comonads.html>

**WHNF (Weak Head Normal Form) — StackOverflow**
The authoritative Stack Overflow explanation of Haskell's lazy evaluation strategy: what Weak Head Normal Form means, how GHC's runtime evaluates expressions to WHNF, and why understanding WHNF is essential for reasoning about space leaks and forcing strategies in Haskell.
stackoverflow.com — <https://stackoverflow.com/questions/6872898/>

**Nobody Gets Fired for JSON — Serialisation Comparison (mcyoung.xyz)**
Article comparing JSON with binary serialization formats (Protobuf, MessagePack, Thrift, CBOR) for production systems: parsing cost, schema evolution, human readability trade-offs, and the "nobody gets fired" cultural inertia that keeps JSON dominant despite its inefficiencies.
mcyoung.xyz — <https://mcyoung.xyz/2024/12/10/json-sucks/>

**Type Classes in Scala 3**
Official Scala 3 documentation on implementing and using type classes via the `given`/`using` mechanism: defining instances, conditional derivation, and how the new implicit system improves on Scala 2's implicit evidence pattern.
docs.scala-lang.org — <https://docs.scala-lang.org/scala3/book/ca-type-classes.html>

**Recursion Schemes in Scala**
Deep dive implementing catamorphisms and anamorphisms in Scala using the Matryoshka library: how to define Fix-point types, write algebra functions, and apply recursion schemes to JSON, AST, and custom data type traversals.
medium.com — <https://medium.com/@wiemzin/getting-started-with-recursion-schemes-using-matryoshka-f5b5ec01bb>

**Mill Scala Build Tool**
Mill is a build tool for Scala, Java, and other JVM languages that competes with SBT: faster incremental compilation, simpler build scripts using plain Scala objects, and a more intuitive task dependency model. Comparison article with SBT for choosing a build tool.
mill-build.com — <https://mill-build.com/>

**Type Class Derivation in Scala 3**
Official Scala 3 documentation on automatic type class derivation using `Mirror`: how the compiler generates `derived` instances for Show, Eq, Codec, and custom type classes using compile-time generic programming without macro libraries.
docs.scala-lang.org — <https://docs.scala-lang.org/scala3/reference/contextual/derivation.html>

**Monad is a Monoid in the Category of Endofunctors (StackOverflow)**
The famous Stack Overflow thread explaining the categorical identity "a monad is a monoid in the category of endofunctors" — what it means precisely, why it is true, and how it connects Haskell monads to mathematical category theory. One of the most read mathematical explanations on Stack Overflow.
stackoverflow.com — <https://stackoverflow.com/questions/3870088/>

**Kleisli — Typelevel Cats Docs**
Cats library documentation on the Kleisli data type: a wrapper for functions `A => F[B]` that composes monadic functions sequentially. Kleisli is foundational for building modular, composable service layers in Scala where each step may fail or perform effects.
typelevel.org — <https://typelevel.org/cats/datatypes/kleisli.html>

**Y Combinator in Lambda Calculus**
Derivation and explanation of the Y combinator — the fixed-point combinator that enables anonymous recursion in pure lambda calculus without named recursion. Essential to understanding the denotational semantics of recursive programs and their formalization.
blog.klipse.tech — <https://blog.klipse.tech/lambda/2016/08/10/pure-functional-programming.html>

**Kyo getkyo.io — Official Site and Documentation**
Official website and documentation for the Kyo effect system for Scala 3: API reference, getting started guides, and explanations of Kyo's intersection-type effect encoding. The primary reference for building applications with Kyo effects.
getkyo.io — <https://getkyo.io/>

**Algebraic Effects from Scratch — Kyo Talk (YouTube)**
Talk demonstrating how to implement algebraic effects in Scala 3 without relying on monad transformer stacks: the direct encoding via intersection types that underlies Kyo's approach. Explains why this produces better ergonomics than Free monad or MTL-style effect composition.
<https://www.youtube.com/watch?v=qPvPdRbTF-E>

**Data.Conduit.Combinators (Haskell)**
Haskell Conduit library's streaming combinators documentation: source, conduit, and sink combinators for building resource-safe streaming pipelines. Conduit's backpressure and resource safety guarantees made it a predecessor to similar ideas in ZIO Streams and fs2.
hackage.haskell.org — <https://hackage.haskell.org/package/conduit-extra>

**Bifunctors (Haskell/Scala)**
Explanation of the Bifunctor type class — types with two type parameters that can be independently mapped over. Common instances include Either and tuples; Bifunctor generalizes Functor to binary containers in a way useful for error-handling types and product types.
hackage.haskell.org — <https://hackage.haskell.org/package/base/docs/Data-Bifunctor.html>

**Turtle — Haskell Shell Scripting Library**
Turtle is a Haskell library for writing shell scripts in Haskell: file operations, process execution, and pipeline composition using Haskell's type system. An alternative to Nushell for those who prefer Haskell as their scripting language.
hackage.haskell.org — <https://hackage.haskell.org/package/turtle>

**FP with TypeScript Playlist (YouTube)**
Video series on applying functional programming patterns in TypeScript: Option, Either, Task, IO monad, and the fp-ts library. Useful for developers wanting to apply Haskell/Scala FP ideas in the TypeScript ecosystem.
youtube.com — <https://www.youtube.com/playlist?list=PLuPevXgCPUIMbCxBEnc1dNwboH6e2ImQo>

**Haskell Dijkstra (Generalized)**
Stack Overflow discussion of implementing Dijkstra's shortest path algorithm idiomatically in Haskell: priority queue selection, mutable vs immutable approaches, and the trade-offs between functional purity and the imperative efficiency of the original algorithm.
stackoverflow.com

**Haskell Tail Recursion and Deforestation**
Article on tail recursion optimization and stream fusion (deforestation) in Haskell: how GHC's `foldr`/`build` fusion eliminates intermediate list allocations in producer-consumer pipelines, and when tail recursion is and is not automatically optimized.
debasishg.blogspot.com — <http://debasishg.blogspot.com/2009/01/to-tail-recurse-or-not-part-2-follow-up.html>

**Lambda Calculus Blog (klipse)**
Introduction to untyped lambda calculus, alpha-equivalence, beta-reduction, and Church encodings for numbers and booleans, with live in-browser evaluation. A hands-on route into the theoretical foundation of all functional programming languages.
blog.klipse.tech — <https://blog.klipse.tech/lambda/>

**Haskell Arrows**
Haskell arrows are a generalization of monads for computation with static structure (arrows can be analyzed without executing them), enabling efficient compilation and static analysis. Arrows underlie Haskell's `proc` notation for arrow-style programming.
haskell.org — <https://www.haskell.org/arrows/>

**Haskell Unfold / Anamorphism (Data.List.unfoldr)**
Documentation and tutorial on `Data.List.unfoldr` — the Haskell unfold operator — and its generalization as an anamorphism: building potentially infinite data structures from a seed value using a step function. The dual of fold/catamorphism.
hackage.haskell.org — <https://hackage.haskell.org/package/base/docs/Data-List.html#v:unfoldr>

**Most Influential CS Papers — Papers We Love**
The Papers We Love repository curating landmark computer science research papers across algorithms, distributed systems, programming languages, and machine learning. A community-maintained reading list for engineers who want to understand the intellectual foundations of their field.
github.com — <https://github.com/papers-we-love/papers-we-love>

**A 2025 Scala Stack (dimitarg.github.io)**
Blog post recommending a modern Scala 3 production technology stack: http4s or tapir for HTTP, Skunk for Postgres, Doobie for JDBC, cats-effect for effects, and circe for JSON. A practical guide to the current Typelevel ecosystem best practices.
dimitarg.github.io — <https://dimitarg.github.io/scala-stack/>

**Building Robust Applications with Kyo (scala.io)**
Scala.io Paris 2024 session on error handling, resource management, and resilience patterns using Kyo: how Kyo's pending effects model leads to naturally robust application code without requiring explicit effect stacking or complex monad transformer compositions.
scala.io — <https://scala.io/sessions/paris-2024/building-robust-applications-with-kyo>

**Writing Modular Apps with Kyo (scalamatters.io)**
Blog post on designing modular, testable applications using Kyo's algebraic effects: how to define capability interfaces as Kyo effects and provide test versus production interpreters without dependency injection frameworks.
scalamatters.io — <https://www.scalamatters.io/post/writing-modular-applications-using-the-kyo-library>

**Kyo — Functional Scala 2023 Talk (YouTube)**
Conference talk introducing Kyo's design to the Functional Scala community: the intersection-type encoding, performance benchmarks against ZIO and cats-effect, and the vision for algebraic effects as the basis for a new generation of Scala libraries.
youtube.com — <https://www.youtube.com/watch?v=FXkYKQRC9LI>

**Scala 3 Extension Methods (official docs)**
Official documentation on Scala 3 extension methods: adding methods to existing types without modifying them, with better ergonomics than Scala 2 implicit classes. Extension methods are fundamental to the Scala 3 typeclass pattern and library extension conventions.
docs.scala-lang.org — <https://docs.scala-lang.org/scala3/book/ca-extension-methods.html>

**etorreborre Blog: 2024 in Review**
Year-in-review post from Étienne Torreborre — creator of specs2 and prominent Scala/Haskell contributor — reflecting on 2024 developments in the Scala ecosystem, functional programming trends, and his own open-source work.
etorreborre.blog — <https://etorreborre.blog/2024-in-review>

**Typed Tagless Final for Real (Oleg Kiselyov)**
Oleg Kiselyov's authoritative resource on the typed tagless final (TTF) approach to embedding DSLs: representing terms as functions over type class algebras rather than as algebraic data types, enabling multiple interpreters without committing to a single representation.
okmij.org — <https://okmij.org/ftp/tagless-final/>

**Unison Cloud Platform**
Unison's cloud-native distributed computing platform built on the Unison language's first-class distributed computing semantics: deploying code to the cloud is a language operation, not a deployment pipeline step. An ambitious attempt to make distributed programming as natural as local programming.
unison.cloud — <https://www.unison.cloud/>

**Profunctors, Arrows, and Static Analysis (elvishjerricco.github.io)**
Technical blog post connecting profunctors — contravariant in the input, covariant in the output — to Haskell arrows and their application in building computations that can be statically analyzed before execution. Important for understanding selective applicative functors and arrow-based analysis.
elvishjerricco.github.io — <https://elvishjerricco.github.io/2017/03/10/profunctors-arrows-and-static-analysis.html>

**Open-Sourcing Haxl (Facebook Engineering)**
Facebook's announcement of open-sourcing Haxl — a Haskell library for efficient batched and concurrent data fetching that automatically batches independent requests, deduplicates fetches, and caches results. The inspiration for GraphQL's DataLoader and similar patterns.
engineering.fb.com — <https://engineering.fb.com/2014/06/10/web/open-sourcing-haxl-a-library-for-haskell/>

**Applicative Effects and Free Monads (blog.functorial.com)**
Comparison of applicative and monadic effect strategies: how Applicative enables static analysis of effects (known before execution) while Monad enables data-dependent sequential effects. Connects to Free Applicative and Free Monad as explicit reifications of each strategy.
blog.functorial.com — <https://blog.functorial.com/posts/2017-07-01-FreeAp-Is-A-Comonad.html>

**lens (ekmett/lens) — Haskell Optics Library**
Edward Kmett's premier Haskell optics library: lenses, prisms, traversals, folds, and isos for composable, typed data access and modification. The lens library demonstrates how profunctor optics encode complex data transformation patterns with minimal boilerplate.
github.com — <https://github.com/ekmett/lens>

**PRE-SIP: Suspended Functions in Scala**
A Scala Improvement Proposal for coroutine-style suspended functions — adding language-level support for suspending computations without explicit monad wrappers. Would potentially reduce the ergonomic gap between Scala's monadic effects and Kotlin's suspend functions.
github.com — <https://github.com/scala/improvement-proposals>

**Capture Checking in Scala 3 (Experimental)**
Scala 3's experimental capture checking feature: a type system extension that tracks which capabilities (IO, network, memory) a function captures in its closure, enabling purely functional API boundaries to be enforced by the compiler without runtime overhead.
docs.scala-lang.org — <https://docs.scala-lang.org/scala3/reference/experimental/cc.html>

**Haskell Kinds and Higher-Kinded Types (Serokell)**
Serokell's tutorial on kind polymorphism and higher-kinded types in Haskell: how `* -> *` kinds express type constructors like `Maybe` and `[]`, and how kind polymorphism via `forall k` enables highly generic abstractions like `Functor`, `Monad`, and `Applicative` to work across type-level structures.
serokell.io — <https://serokell.io/blog/>

**Comonad Can Be Monad (Bartosz Milewski)**
Bartosz Milewski's mathematical exploration of comonads as the categorical dual of monads: how `extend`/`extract` correspond to `bind`/`return`, the relationship to cellular automata and context-dependent computations, and how comonads model "objects with environment."
bartoszmilewski.com — <https://bartoszmilewski.com/2017/01/02/comonads/>

**Free Monad Blog (Reasonably Polymorphic)**
Sandy Maguire's practical guide to free monads as an effect encoding strategy: building an effect algebra as a functor, lifting it into a Free monad, and providing multiple interpreters. Explains both the appeal and the performance overhead relative to tagless final.
reasonablypolymorphic.com — <https://reasonablypolymorphic.com/blog/freer-monads/>

**Haskell Fix and Recursion**
Documentation and tutorial on Haskell's `fix` combinator — the fixed-point operator for defining recursive values and functions without explicit `let rec`. `fix` is the lambda calculus Y combinator expressed in Haskell's type system.
hackage.haskell.org — <https://hackage.haskell.org/package/base/docs/Data-Function.html#v:fix>

**Recursion Schemes in Rust (inanna-malick)**
Implementation of catamorphisms and anamorphisms in Rust using trait-based F-algebra encoding, demonstrating that recursion schemes are a language-agnostic pattern applicable outside Haskell/Scala to any sufficiently expressive type system.
github.com — <https://github.com/inanna-malick/recursion>

**Understanding F-Algebras (Bartosz Milewski)**
Bartosz Milewski's category-theoretic explanation of F-algebras: the mathematical structure underlying recursion schemes, where a functor F applied to a carrier type A plus an evaluation function `F A -> A` defines the semantics of recursive computations.
bartoszmilewski.com — <https://bartoszmilewski.com/2013/06/10/understanding-f-algebras/>

**unfoldable (Hackage)**
Haskell package providing a type class for data structures that can be built from an unfold operation: a generalization of `Data.List.unfoldr` to trees, rose trees, and other branching structures. The dual of `Foldable` in the recursion scheme sense.
hackage.haskell.org — <https://hackage.haskell.org/package/unfoldable>

**Existential Types in Haskell**
HaskellWiki explanation of existential quantification in Haskell types: how `forall a. (Constraint a) => T a` enables heterogeneous containers, dynamic dispatch, and information hiding at the type level without requiring type erasure or runtime type tags.
wiki.haskell.org — <https://wiki.haskell.org/Existential_type>

**A Gentle Run-Through of CPS (matt.might.net)**
Matt Might's explanation of continuation-passing style from first principles: transforming direct-style programs to CPS, what CPS reveals about control flow, and how CPS transformation is used in compilers for tail-call optimization and first-class continuation support.
matt.might.net — <https://matt.might.net/articles/>

**Quick Overview: Haskell Streamly**
Introduction to Streamly — a high-performance Haskell streaming library that competes with Conduit and pipes, claiming better throughput through stream fusion and a simpler API. Relevant for high-throughput data processing pipelines in Haskell.
github.com — <https://github.com/composewell/streamly>

**Pavel Fatin: Design Patterns in Scala**
Pavel Fatin's guide to implementing classic Gang of Four design patterns in idiomatic Scala: how patterns like Strategy, Decorator, and Visitor map naturally to type classes, higher-order functions, and case class hierarchies — and when FP eliminates the need for the pattern entirely.
pavelfatin.com — <https://pavelfatin.com/design-patterns-in-scala/>

**Alexis King Blog**
Alexis King's deep technical blog on Haskell, algebraic effects, and type system design: posts on "Effects for Less" (the basis for the `eff` library), delimited continuations, and the theory behind efficient algebraic effect implementations.
lexi-lambda.github.io — <https://lexi-lambda.github.io/>

**Kyo Memory.scala**
The Memory management module in the Kyo effect system source code — providing Kyo-native memory allocation and management effects that integrate with Kyo's pending effect tracking. Relevant for performance-sensitive Kyo applications managing native or off-heap memory.
github.com — <https://github.com/getkyo/kyo>

**Tweag Named Routes**
Tweag's blog on named route patterns in Haskell's Servant library: using type-level symbols to refer to routes by name rather than position, enabling refactoring-safe API client generation. The pattern is influential for type-safe API design in both Haskell and Scala http4s/tapir.
tweag.io — <https://www.tweag.io/blog/2022-02-24-named-routes/>

**Noel Welsh: Tagless Final for Humans (Scalar Conference)**
Noel Welsh's pragmatic Scalar Conference talk making tagless final interpreters accessible to mainstream Scala developers: focusing on the practical benefits (testability, multiple interpreters) while de-emphasizing the category theory motivation that makes the pattern seem inaccessible.
scalar-conf.com — <https://www.scalar-conf.com/talk/tagless-final-for-humans>

**The Expression Problem**
Philip Wadler's classic extensibility challenge: how to extend a language with new data types and new operations simultaneously without modifying existing code. Functional languages solve it one way (new operations easy), OOP another (new types easy); tagless final and open unions offer general solutions.
wiki.haskell.org — <https://wiki.haskell.org/Expression_problem>

**Scala 3 REST API with ZIO (rockthejvm.com)**
RockTheJVM tutorial on building REST APIs in Scala 3 using ZIO HTTP (formerly ZIO HTTP4S): route definition, JSON encoding/decoding via ZIO JSON, dependency injection via ZLayer, and testing with ZIO Test. A practical end-to-end production REST API walkthrough.
blog.rockthejvm.com — <https://blog.rockthejvm.com/zio-http/>

**Compiler Tagless Final / Oleg Kiselyov Tagless Final**
Oleg Kiselyov's authoritative collection of tagless final papers and implementations: the initial vs final encoding comparison, the role of type classes as effect algebras, and the symantics approach to embedded DSL implementation. The theoretical bedrock of modern Scala effect systems.
okmij.org — <https://okmij.org/ftp/tagless-final/>

**Scala Distributed System from Scratch (bridgefour)**
Christian Hollinger's open-source project building a simple distributed system in Scala 3 from scratch: master/worker coordination, job distribution, failure handling, and recovery — without using Akka or ZIO, demonstrating the raw mechanics of distributed coordination.
github.com — <https://github.com/chollinger93/bridgefour>

**Whiteboxish Named Tuples in Scala 3 — Scalar 2025**
Scalar Conference 2025 talk on named tuple improvements in Scala 3: how named tuples improve API expressiveness compared to anonymous tuples or case classes, and the compiler implementation challenges around whitebox macro interactions.
scalar-conf.com — <https://scalar-conf.com/>

**Evaluating AI on Haskell Tasks — Benchmark Study**
Research benchmarking LLM performance on writing correct Haskell code: comparing GPT-4, Claude, and Gemini on type class usage, monad transformer stacks, and Haskell-specific idioms. Provides data on where AI assistance is most and least reliable for Haskell development.
github.com — <https://github.com/MercuryTechnologies/haskell_llm_benchmark>

**Parsley — Scala 3 Parser Combinator Library**
Parsley is a Scala 3 parser combinator library with a Haskell-like interface, featuring optimistic parsing, Parsec-style combinators, and automatic left-recursion handling. Provides better performance than naive recursive descent through combinator fusion.
github.com — <https://github.com/j-mie6/Parsley>

**LSUG: Parsley Talk (YouTube)**
London Scala User Group talk presenting the Parsley parser combinator library: its design goals, performance characteristics, and comparison with other Scala parsing libraries (Cats Parse, Fastparse). Practical guidance on choosing a parser combinator for production Scala projects.
youtube.com

**Hazel Live Functional Programming Environment**
Hazel is a live programming environment for a functional language with "holes" — incomplete programs that still execute and provide meaningful feedback. Designed to make the development experience of functional programming more interactive and exploratory.
hazel.org — <https://hazel.org/>

**Zig and Rust Comparison (matklad)**
Aleksey Kladov (matklad)'s thoughtful comparison of Zig and Rust: where Zig's simpler model (no borrowing, explicit allocators, comptime) makes it preferable for systems programming, and where Rust's ownership guarantees remain irreplaceable. A nuanced view from a Rust core team alum.
matklad.github.io — <https://matklad.github.io/2023/03/26/zig-and-rust.html>

**GitHub: Developer-Y/cs-video-courses**
Comprehensive curated list of computer science video courses freely available online: algorithms, programming languages theory, systems, distributed systems, compilers, and machine learning from MIT, Stanford, CMU, and other institutions.
github.com — <https://github.com/Developer-Y/cs-video-courses>

**Legalizing Comonad Composition (Bartosz Milewski)**
Bartosz Milewski's 2025 blog post on the mathematical conditions under which two comonads can be composed — a problem symmetric to monad composition but with different constraints. Relevant to understanding the categorical limits of comonad-based object composition.
bartoszmilewski.com — <https://bartoszmilewski.com/2025/01/04/legalizing-comonad-composition/>

**Hylomorphism and Refold Code Snippets (GitHub Gist)**
Code examples implementing hylomorphisms (refold) in Scala and Haskell: demonstrating how to express algorithms like merge sort, tree evaluation, and expression folding as explicit unfold-then-fold compositions using recursion scheme combinators.
gist.github.com — <https://gist.github.com/yuwki0131/db2dcc08d8b6b086d055182dc32c0300>

**PL Zoo — Programming Language Implementations Collection**
Andrej Bauer's collection of small programming language implementations for learning programming language theory: untyped lambda calculus, typed PCF, System F, and more, each implemented in OCaml with clear separation of parser, type checker, and evaluator.
plzoo.andrej.com — <https://plzoo.andrej.com/>

**De Bruijn Index (Wikipedia)**
Wikipedia article on De Bruijn indices — a name-free representation of lambda calculus terms using natural numbers to denote binding depth rather than variable names. De Bruijn indices eliminate alpha-equivalence as a concern and simplify substitution in lambda calculus implementations.
en.wikipedia.org — <https://en.wikipedia.org/wiki/De_Bruijn_index>

**tree-sitter — Incremental Parser Generator**
tree-sitter is a parser generator tool and incremental parsing library used to build syntax-aware editors and analysis tools: it produces concrete syntax trees for any language, updates them incrementally as code changes, and powers syntax highlighting in Neovim, Helix, and GitHub's Linguist.
tree-sitter.github.io — <https://tree-sitter.github.io/tree-sitter/>

**Rhombus Lang — Racket-Based Language**
Rhombus is a new language built on the Racket platform with improved syntax (non-S-expression) and a revised macro system, designed to be Racket's more approachable successor for language-oriented programming. It preserves Racket's language extensibility while removing the syntactic barrier.
github.com — <https://github.com/racket/rhombus-prototype>

**Which Programming Languages Are Most Token-Efficient? (martinalderson.com)**
Analysis of token counts across 19 programming languages on RosettaCode benchmarks: Clojure and other Lisps are most token-efficient, C/C++ least efficient, with Scala and Haskell in the middle. The 2.6x Clojure vs C difference has implications for LLM coding costs and context window usage.
martinalderson.com — <https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/>

**LLM-Generated Lean 4 Proofs — Research Paper**
Study comparing GPT-4, Gemini, and other LLMs on formal Lean 4 proof generation tasks: success rates, error types, and the strategies that improve proof generation quality. Represents the state of AI-assisted formal mathematics as of early 2025.
github.com — <https://github.com/lampless/LLM-Generated-Lean4-Proofs/blob/main/Dylan%20Miller_%20LLM-Generated%20Lean4%20Proofs.pdf>

**Rust Replaces Java/Scala at xAI (Tweet)**
Tweet noting that xAI's x-algorithm repository — where Java or Scala might be expected — uses Rust as its primary language, signaling an industry shift toward Rust even in domains traditionally dominated by JVM languages for their ecosystem and tooling advantages.
x.com — <https://x.com/ForrestPKnight/status/2018768871474315761>

**GitHub: duolingo/slack-mcp — OAuth Multi-User Slack MCP Server**
Duolingo's open-source Model Context Protocol (MCP) server for Slack, implementing OAuth-based multi-user authentication and HTTP transport to support team-wide AI assistant integrations with Slack. A reference implementation for multi-user MCP server design.
github.com — <https://github.com/duolingo/slack-mcp>

**Kyo Issue Tracker (GitHub)**
Active Kyo development discussion thread tracking a specific issue or feature request in the Kyo effect system repository. A reference for following the evolution of the Kyo API and understanding design trade-offs being actively debated by the core team.
github.com — <https://github.com/getkyo/kyo/issues/1419>

**Agentic Reasoning for Large Language Models — Survey (arxiv)**
Comprehensive survey paper organizing the landscape of agentic LLM reasoning: foundational reasoning (chain-of-thought, reflection), self-evolving reasoning (reinforcement learning, online adaptation), and multi-agent coordination patterns. A reference for building LLM-based agent systems.
arxiv.org — <https://arxiv.org/abs/2601.12538>

**Intelligent AI Delegation — Framework (arxiv)**
Research paper proposing a framework for adaptive task allocation and authority transfer in multi-agent AI systems: how to decide when to delegate to a subagent, how to transfer context, and how to aggregate results with appropriate uncertainty calibration.
arxiv.org — <https://arxiv.org/abs/2602.11865>

**Claude Code Design Decisions Talk (Tech with Mak)**
45-minute talk by the Claude Code creator on the design decisions behind Claude Code: why it uses a CLI interface, how tool use is structured, the permissions model, and the future direction of AI coding assistants. Relevant to both Claude Code users and developers building similar tools.
x.com — <https://x.com/techNmak/status/2024041443837526375>

**User Personal Note: Eke Project Plan**
Personal project priority notes: Haskell unfold implementation for Eke word structure analysis, Kyo effect system integration for the ettuge project, Wiktionary parsing for etymology data, and alar.ink dictionary corpus analysis work planned for Jan–Feb 2025.

**User Observation: Claude for Kannada DNS Bhat Analysis**
Personal note on using Claude for Kannada video transcription and DNS Bhat grammar book analysis — finding Claude superior to NotebookLM for cross-document discovery and synthesis. The generated analysis output would have required extensive hand-coding to produce otherwise.
github.com — <https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/malatibhat_dns_bhat_chat.md>

**ettuge/dnsbhat Kannada Grammar Chapters (GitHub)**
Series of markdown notes in the ettuge repository translating and summarizing chapters from DNS Bhat's Kannada grammar books: morphology, phonology, and syntax analysis of the Kannada language using the Ellara Kannada (pure Dravidian) framework.
github.com — <https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/dnsbhat/>

**mEsṭre Kannada AI App Concept**
Personal product concept: a Kannada AI assistant that code-switches intelligently between pure Dravidian Kannada, standard literary Kannada, and Kanglish depending on context — with autocomplete, agent integrations (calendar, mail), and an Eke romanization keyboard. Designed as a culturally authentic Kannada AI experience.

**Ship an MCP Server/Agent — Architectural Note**
Personal architectural insight: shipping an MCP (Model Context Protocol) server makes all downstream AI integrations compose automatically — any Claude or other MCP-compatible AI client gains access to the server's capabilities without additional integration work.

**Skill Graph for Memory — Tweet (rohit4verse)**
Tweet proposing a network of skill files connected via wikilinks as a useful pattern for AI agent memory systems: the graph structure enables semantic navigation between related skills rather than linear search, mirroring how knowledge graphs outperform flat key-value memory.
x.com — <https://x.com/rohit4verse/status/2024031053103366528>

**RAG Architecture Selection Guide (Tech with Mak)**
Practical guide to selecting the right RAG (Retrieval-Augmented Generation) variant by use case: standard vector RAG for factual Q&A, agentic RAG for multi-step reasoning, graph RAG for entity-relationship queries, modular RAG for hybrid approaches, and long-term memory RAG for persistent personalization.
x.com — <https://x.com/techNmak/status/2023978105606676821>

**Transformers Use 6D Helical Manifolds for Counting (Anthropic)**
Anthropic mechanistic interpretability research revealing that Claude 3.5 Haiku represents numerical values on six-dimensional helical manifolds in its residual stream — a geometric representation that enables robust counting and arithmetic rather than a lookup-table approach.
x.com — <https://x.com/che_shr_cat/status/2023729615055782140>

**Scala 3 'break' and 'continue' Equivalents (rockthejvm.com)**
RockTheJVM's explanation of how to express early loop termination idiomatically in Scala 3 — using boundary/break from scala.util.boundary (Scala 3.3+), tailrec with Option, or functional approaches with takeWhile/find. Scala 3 finally provides a principled break/continue via the boundary API.
blog.rockthejvm.com — <https://blog.rockthejvm.com/>

## Functional Programming Channels & Conferences

**Typelevel (YouTube)**
<https://www.youtube.com/channel/UC-CzKrmtV55SlW2eL3k1RRQ>

The Typelevel ecosystem (Cats, http4s, fs2, Circe, Doobie) for purely functional Scala programming. Conferences and talks from core contributors. **[→ scala-fp; typelevel]**

---

**Bartosz Milewski (YouTube)**
<https://www.youtube.com/channel/UC8BtBl8PNgd3vWKtm2yJ7aA>

Author of *Category Theory for Programmers* (the Haskell-based textbook that became the standard reference for programmers learning category theory). His YouTube series is the video companion to the book. **[→ scala-fp; category-theory]**

---

**TheCatsters (YouTube)**
<https://www.youtube.com/channel/UC5Y9H2KDRHZZTWZJtlH4VbA>

Eugenia Cheng and Simon Willerton's original category theory lecture series recorded at Sheffield. The Catsters videos are widely considered the best introductory category theory content available online — rigorous but accessible. **[→ scala-fp; category-theory; mathematics]**

---

**Edward Kmett (YouTube)**
<https://www.youtube.com/channel/UCE3MJbkTVLoK8dAq7Del8ww>

One of the most prolific Haskell library authors (lens, comonad, free, adjunctions, etc.). His talks at Haskell conferences cover advanced type system techniques, category theory applications in Haskell, and the theory behind his libraries. **[→ scala-fp; haskell; category-theory]**

---

**Graham Hutton (YouTube)**
<https://www.youtube.com/channel/UCBSRCuGz9laxVv0rAnn2O9Q>

Author of *Programming in Haskell* (the standard undergraduate Haskell textbook). His channel supplements the book with lecture videos covering monads, parsing, lazy evaluation, and compiler theory. **[→ scala-fp; haskell]**

---

**Bay Area Haskell (YouTube)**
<https://www.youtube.com/channel/UCCL46pxWWtfhK3TxL55ybeQ>

Bay Area Haskell user group talks and meetups — covering industrial Haskell usage, library design, and theoretical topics from practitioners in the SF Bay Area. **[→ scala-fp; haskell]**

---

**Boston Haskell (YouTube)**
<https://www.youtube.com/channel/UCUCpgCWjaniUkX88wZrK_Ig>

Boston Haskell user group meetup recordings. Covers applied Haskell, libraries, and theoretical discussions from the New England functional programming community. **[→ scala-fp; haskell]**

---

**chshersh — Dmitrii Kovanikov (YouTube)**
<https://www.youtube.com/channel/UCKmndeSJ-xKGHPtxQulG_EA>

Haskell library author and educator; creator of the `relude` Prelude alternative and `co-log` logging library. His content focuses on practical Haskell library design, algebraic design patterns, and Haskell best practices. **[→ scala-fp; haskell]**

---

**mpilquist — Michael Pilquist (YouTube)**
<https://www.youtube.com/channel/UC634L9eG-YsskyzWxnp9BJA>

Creator of fs2 (Functional Streams for Scala) and shapeless contributor. Talks on functional streaming, type-level programming, and the design of the Typelevel ecosystem. **[→ scala-fp; typelevel]**

---

**Scala for Fun & Profit (YouTube)**
<https://www.youtube.com/channel/UCJ2zsdq4-5vzySOYtgo1nHw>

Community Scala channel covering practical Scala 3 patterns, effect systems, and library usage. **[→ scala-fp]**

---

**Happy Path Programming (YouTube)**
<https://www.youtube.com/channel/UCJXWVm6uAKh_Nd1mqkKLW5A>

Scala and functional programming podcast/channel by Brian Sletten and Bruce Eckel. Focuses on the pragmatics of adopting functional programming in real projects. **[→ scala-fp]**

---

**Rock the JVM — Daniel Ciocîrlan (YouTube)**
<https://www.youtube.com/channel/UCRS4DvO9X7qaqVYUW2_dwOw>

Comprehensive Scala and JVM ecosystem tutorials; the best source for Akka, ZIO, Cats Effect, Spark, and Scala 3 tutorials online. Ciocîrlan's structured approach makes advanced topics accessible. **[→ scala-fp]**

---

**LambdaConf (YouTube)**
<https://www.youtube.com/channel/UCEtohQeDqMSebi2yvLMUItg>

Annual functional programming conference covering Haskell, PureScript, Idris, category theory, dependent types, formal verification, and applied FP. One of the more theoretically ambitious FP conferences. **[→ scala-fp; category-theory; formal-methods]**

---

**Lambda World (YouTube)**
<https://www.youtube.com/channel/UCERm5yFZ1SptUEU4wZ2vJvw>

European functional programming conference (Spain) featuring talks on Scala, Haskell, Kotlin, Clojure, and type theory. Strong theoretical content alongside practical applications. **[→ scala-fp; category-theory]**

---

**Scala World (YouTube)**
<https://www.youtube.com/channel/UCc0j7uOItUDh7vEvPb-TeCg>

UK Scala conference in the Lake District; known for high-quality, practitioner-focused content on the Scala ecosystem and functional programming. **[→ scala-fp]**

---

**ScalaCon (YouTube)**
<https://www.youtube.com/channel/UCEvZRFnLl65Dg1sMgb8yIBQ>

Online Scala conference with broad coverage of Scala 2 and 3, effect systems, and Scala's role in data engineering and distributed systems. **[→ scala-fp]**

---

**Scala Stockholm (YouTube)**
<https://www.youtube.com/channel/UCQVjiKOragIVS8jbzqUG09A>

Stockholm Scala user group talks. **[→ scala-fp]**

---

**London Scala User Group (YouTube)**
<https://www.youtube.com/channel/UCR-XcPzcRKSXxk4hcsddLtg>

London's active Scala meetup, one of the largest Scala communities in Europe. **[→ scala-fp]**

---

**ScalaUA Conference (YouTube)**
<https://www.youtube.com/channel/UC_ZJvRHot6thpgqsXvtEvFg>

Ukrainian Scala conference; historically high-quality talks on the Typelevel ecosystem, functional design, and Scala tooling. **[→ scala-fp]**

---

**Xebia Functional (formerly 47 Degrees) (YouTube)**
<https://www.youtube.com/channel/UCatg8Vf2cgX5ZV30RFZe-gg>

Consulting firm focused on functional programming; produces content on Scala, Kotlin, Swift, and arrow-kt (Kotlin functional library). Co-organizer of Scala World. **[→ scala-fp]**

---

**Jane Street (YouTube)**
<https://www.youtube.com/channel/UCDsVC_ewpcEW_AQcO-H-RDQ>

Jane Street Capital's tech talks; predominantly OCaml content from one of the world's largest functional programming shops. Their open-source contributions (Core, Async, Base) and their reasoning about type-safe financial systems are highly instructive for FP practitioners. **[→ scala-fp; ocaml]**

---

**Ziverge (YouTube)**
<https://www.youtube.com/channel/UCeIg_PnAoyd1w6y8BelLdiQ>

John De Goes's company behind ZIO; the channel covers ZIO, ZIO Schema, ZIO HTTP, and the broader ZIO ecosystem for purely functional Scala programming. **[→ scala-fp; zio]**

---

**DevInsideYou (YouTube)**
<https://www.youtube.com/channel/UCSBUwLT9zXhUalKfJrc2q2A>

Practical Scala tutorials and FP content; popular for Scala beginners and intermediate practitioners. **[→ scala-fp]**

---

**SoftwareMill (YouTube)**
<https://www.youtube.com/channel/UCDHLL2QvdpCytAfBiwUeKgg>

Polish software consultancy known for Akka, sttp, tapir, and Scala conference talks. Pragmatic functional Scala content. **[→ scala-fp]**

---

**FunctionalTV (YouTube)**
<https://www.youtube.com/channel/UCKvhw2CPR-0S4XZ1bNlihnw>

Aggregator of functional programming conference talks across languages and venues. **[→ scala-fp; haskell]**

---

**MoonBit (YouTube)**
<https://www.youtube.com/channel/UCRRiPMzGU0suqQE8PuXHIMA>

MoonBit is a new strongly-typed, functional programming language targeting WebAssembly, developed by IDEA Research. Its type system is influenced by ML/Haskell; worth tracking as a next-generation FP language. **[→ scala-fp; programming-languages]**

---

**Unison Language (YouTube)**
<https://www.youtube.com/channel/UCwNb-TXaavfoTgDu8UglXyw>

The Unison programming language from Unison Computing — a content-addressed, purely functional language that stores code by its AST hash rather than name. Its approach to distributed programming and code storage is genuinely novel; the repository in this codebase (unison/) tracks this project. **[→ scala-fp; programming-languages]**

---

**makingthematrix (YouTube)**
<https://www.youtube.com/channel/UC5lQKRHit0OPI9QbE8nJv6g>

Scala 3 tutorials and functional programming content, often with visualization. **[→ scala-fp]**

---

**Jakub Kozłowski (YouTube)**
<https://www.youtube.com/channel/UCbipI7oQJsOUXXWRvGjkYmg>

Scala and Haskell content; known for talks on effect systems, type-level programming, and Scala 3. **[→ scala-fp]**

---

**Formalizing a Proof in Lean Using Claude Code (YouTube, Watch History)**

Video demonstrating the workflow of using Claude Code to assist in formal proof development in Lean 4 — a dependent type theory–based proof assistant. Lean is increasingly the tool of choice for mechanizing mathematical proofs; this video sits at the intersection of FP, formal methods, and AI-assisted development. **[→ scala-fp; formal-methods; machine-learning-ai]**
