---
title: Scala & Functional Programming
created: 2026-02-25
source: ../self.md
---

# Scala & Functional Programming

> Derived from [`self.md`](../self.md) · Created: 2026-02-25

Collected links, notes, and code snippets on Scala 3, ZIO, Kyo, Haskell, Rust, functional effects, type theory, and related FP topics.

---

## ZIO / Scala Effect Systems

ZIO Actors
https://twitter.com/jdegoes/status/1600917565625270272

ZIO Telemetry
https://github.com/zio/zio-telemetry

ZIO NIO
https://github.com/zio/zio-nio

Alvin Alexander on LinkedIn: GitHub - zio/zio-direct: Direct-Style Programming for ZIO
On Twitter I was asked a great question: What are the benefits of ZIO and FP?
https://www.linkedin.com/posts/alvinalexander_github-ziozio-direct-direct-style-programming-activity-7247368581145923584-gS3l

ZIO 2.x migration guide — zio.dev
https://zio.dev/guides/migrate/zio-2.x-migration-guide/

ZIO Schema
https://zio.dev/zio-schema/

Zymposium: ZIO 2.0 (John De Goes, Adam Fraser)
https://www.youtube.com/watch?v=6A1SA5Be9qw

John De Goes — Reimagining Functional Type Classes
https://www.youtube.com/watch?v=oluPEFlXumw

Scala + ZIO = Functional Scala (multiple playlist links)

Streams in ZIO
https://twitter.com/jdegoes/status/1565001020918034432

The Effect Pattern — Michael Arnaldi
https://effectful.co

Compositional resource management in Scala 3 with ZIO
https://blog.pierre-ricadat.com/compositional-resource-management-in-scala-3-with-zio

## Kyo Effect System

Kyo — Scala 3 effect system (Flavio Brasil)
https://github.com/getkyo/kyo

kyo-chatgpt example
https://github.com/fwbrasil/kyo/tree/main/kyo-chatgpt

Kyo: Crafting Scala's Futuristic Effects
https://www.youtube.com/watch?v=cyGSLCXR4Bo

## Safe Direct-Style Scala / Structured Concurrency

Safe direct-style Scala: Ox 0.1.0 released (SoftwareMill)
https://softwaremill.com/ox-0-1-0-released-safe-direct-style-scala/

Comparing Approaches to Structured Concurrency by James Ward and Adam Hearn (LambdaConf 2024)
https://www.youtube.com/watch?v=g6dyLhAublQ

EasyRacer LambdaConf 2024 (James Ward)
https://jamesward.github.io/easyracer/

Coroutines and effects (without.boats)
https://without.boats/blog/coroutines-and-effects/

## Scala 3 Language Features & Patterns

Scala HTMX web apps (Igal Tabachnik tweet, RockTheJVM)
https://twitter.com/igal_tabachnik

Scala 3 — end markers, given instances, sealed traits
https://docs.scala-lang.org/scala3/reference/

Scala CLI
https://scala-cli.virtuslab.org/

sbt-assembly
https://github.com/sbt/sbt-assembly

The Evolution of Effects (Haskell'23 keynote, Nicolas Wu)
https://icfp23.sigplan.org/details/haskellsymp-2023/10/The-Evolution-of-Effects

What is so unique about Unison? (Etienne Torreborre blog)
https://etorreborre.blog/

Unison is crack for backend software engineers
An laborious attempt at describing the value I see in Unison, specifically around packaging/deployment
https://neander.tech/2024-07-31-unison-is-crack

FUNARCH 2024 — Functional Architecture
"Functional Software Architecture" refers to methods of construction and structure of large and long-lived software projects
https://functional-architecture.org/events/funarch-2024/

KEYNOTE: FP Meets OS: The Case Of I/O by Vitaly Bragilevsky (LambdaConf 2024)
https://www.youtube.com/watch?v=ZGyIp8oalmE

What does it mean that a language has an "effect system"?
https://langdev.stackexchange.com/questions/3726/what-does-it-mean-that-a-language-has-an-effect-system

Higher Order Company / HVM / Bend language
https://higherorderco.com/

## Rust

Rust design patterns (rust-unofficial.github.io)
https://rust-unofficial.github.io/patterns/

Rust cheat sheet
https://upsuper.github.io/rust-cheatsheet/

Type-level Programming in Rust (Will Crichton)
https://willcrichton.net/rust-api-type-patterns/

graydon2: Notes on Rust, mutable aliasing and formal verification
https://graydon2.dreamwidth.org/

Rust formal verification (xav.io)
https://xav.io/

100 Exercises To Learn Rust
https://rust-exercises.com/02_basic_calculator/00_intro

A Basic Calculator - 100 Exercises To Learn Rust
rust-exercises.com
https://rust-exercises.com/02_basic_calculator/00_intro

Learning Rust (quinedot.github.io)
https://quinedot.github.io/rust-learning/

Rust Design Patterns PDF
https://rust-unofficial.github.io/patterns/

Rust Atomics and Locks by Mara Bos
Low-level Concurrency in Practice
https://marabos.nl/atomics/

Implementing (parts of) git from scratch in Rust (Jon Gjengset, YouTube)
https://www.youtube.com/watch?v=u0VotuGzD_w

Golem's Rust transaction API (blog.vigoo.dev)
https://blog.vigoo.dev/

LogLog Games: Leaving Rust Gamedev
https://loglog.games/blog/leaving-rust-gamedev/

Google hails move to Rust for huge drop in memory vulnerabilities
https://www.yahoo.com/tech/google-hails-move-rust-huge-180100292.html

Introducing Distill CLI: An efficient, Rust-powered tool for media summarization
After a few code reviews from Rustaceans at Amazon and a bit of polishing, I'm ready to share the Distill CLI
https://www.allthingsdistributed.com/2024/06/introducing-distill-cli.html

Hands-on Data Structures and Algorithms With Rust — San Mateo County Libraries
https://smcl.bibliocommons.com/v2/record/S76C3254158

Breaking out of the fold (Ethan Kent's dev blog)
Addresses the problem: we sometimes want to break out of the iteration within fold, but it is not easy to do in many languages
https://ethankent.dev/posts/breaking_fold/

## Rust LeetCode Solutions (Knight's Tour)

Rust implementation of Check Valid Grid (Knight's Tour validation)
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

## Scala LeetCode Solutions

### Knight's Tour Validation (Scala)

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

Submitted as "kodebale" at Sep 25, 2024

## Haskell

Euterpea — Music composition DSL in Haskell
https://www.haskell.org/euterpea/

Unison programming language (Haskell / Stack)
https://github.com/unisonweb/unison

What is so unique about Unison? (etorreborre.blog)
https://etorreborre.blog/

## Nushell

Writing shell scripts in Nushell (jpospisil.com)
https://jpospisil.com/2023/writing-shell-scripts-in-nushell

Exploring Nushell (LogRocket)
https://blog.logrocket.com/exploring-nushell/

In praise of Nushell (lars.yencken.org)
https://lars.yencken.org/in-praise-of-nushell

nushell ArchWiki
https://wiki.archlinux.org/title/Nushell

Solene Nushell intro article (dataswamp.org)
https://dataswamp.org/~solene/

Unleashing the Power of NuShell: Mastering CSV

GitHub - casey/just: command runner
https://github.com/casey/just

### Nushell command: parse alar.txt linkchecker output to JSON
```nushell
open alar.txt | parse -r '(((URL *\x60(?P<Url>[^\x27]*)\x27)\n)|((Name *\x60(?P<Name>.*)\x27)\n)|(Parent URL *(?P<Purl>(?P<phttp>[^,]*), line (?P<pline>[^,]*), col (?P<pcol>[^\n]*))\n)|((Real URL *(?P<Rurl>.*))\n)){4}' | select Url Name Rurl phttp pline pcol| to json | save -f "alar-url.txt"
```

### Nushell Kannada character class variables (for alar.ink analysis)
```nushell
$env.vowelfull = $env.vowel + $env.vowelend
$env.consnooth = $env.cons + $env.consend
$env.consotth1 = $env.cons + $env.hal + $env.cons + $env.consend
$env.consotth2 = $env.cons + $env.hal + $env.cons + $env.hal + $env.cons + $env.consend
$env.block = $"\(\(($env.vowelfull)\)|\(($env.consnooth)\)|\(($env.consotth1)\)|\(($env.consotth2)\)\)"
egrep $"\^($env.block){5}[್]?\$" alar-212-sorted-uniq-2.txt | save -f alar-5.txt
# Result: 21416 words of 5+ syllables
```

## The life and times of an Abstract Syntax Tree

The life and times of an Abstract Syntax Tree (blog.trailofbits.com)
https://blog.trailofbits.com/

## Logic / Formal Verification

CPSC-298 Logic in Software Engineering (Lean) — HackMD
Lean Co-pilot (Anima Anandkumar tweets)
LeanDojo oral presentation NeurIPS 2023

A pilot project in universal algebra to explore new ways to collaborate and use machine assistance? (Terry Tao blog)
Traditionally, mathematics research projects are conducted by a small number of expert mathematicians. New approaches using machine assistance.
https://terrytao.wordpress.com/2024/09/25/a-pilot-project-in-universal-algebra-to-explore-new-ways-to-collaborate-and-use-machine-assistance/

## Concurrency / OS

Rearchitecting core services at X (Mike, @cambridgemike)
https://x.com/cambridgemike/status/1835774409786986572

1: TinyURL + PasteBin — Systems Design Interview Questions With Ex-Google SWE
https://youtu.be/5V6Lam8GZo4

GitHub - Coder-World04/Complete-System-Design
https://github.com/Coder-World04/Complete-System-Design

GitHub - Coder-World04/Tech-Interview-Important-Topics-and-Techniques
This repository contains everything you need to become tech interview ready with most important tips and techniques
https://github.com/Coder-World04/Tech-Interview-Important-Topics-and-Techniques

Neo Kim (@systemdesign42): I spent 5+ hours studying how Instagram scaled to 2.5 billion users
https://x.com/systemdesign42/status/1800491019663970354

## Java

### Dining Philosophers (LeetCode, Java)
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
https://leetcode.com/problems/the-dining-philosophers/

## Algorithms & Interview Prep

Algorithms by Jeff Erickson
https://jeffe.cs.illinois.edu/teaching/algorithms/

GitHub - ossu/computer-science: Path to a free self-taught education in Computer Science
https://github.com/ossu/computer-science

Arpit Adlakha (@arpit20adlakha): One of the finest roadmaps for Senior Software Interviews (Uber L5A/L5B or Google L5/L6 levels)
https://x.com/arpit20adlakha/status/1805084468870521100

Ashish Pratap Singh (@ashishps_1): LeetCode was HARD until I Learned these 15 Patterns:
1. Prefix Sum 2. Two Pointers 3. Sliding Window 4. Fast & Slow Pointers 5. LinkedList In-place Reversal 6. Monotonic Stack 7. Top 'K' Elements 8. Overlapping Intervals 9. Modified Binary Search 10. Binary Tree Traversal 11. ...
https://x.com/ashishps_1/status/1814884401249198569

Alex Xu tweet: Recommended materials for technical interview

## Nix

The Determinate Nix Installer · Zero to Nix
https://zero-to-nix.com/concepts/nix-installer

## Miscellaneous Programming

Edward Kmett: Ask yourself why B-trees exist and are provably optimal for so many applications
https://x.com/kmett/status/1811904210021286014

Erik Meijer (@headinthebox): Real life case of law of excluded middle
A: Hallucination is Inevitable / Not-A: guarantees accuracy and eliminates hallucinations
https://x.com/headinthebox/status/1801087634200199464

Satnam Singh (@satnam6502): Erik Meijer tames AI with lambda calculus and big step semantics
https://x.com/satnam6502/status/1817243947800129956

Bounties | Algora — open source bounties on Scala
https://console.algora.io/bounties/t/scala

Why, after 6 years, I'm over GraphQL (bessey.dev)
https://bessey.dev/

Mathematics in India (bhavana.org.in)
https://bhavana.org.in/mathematics-in-india-6/

---

## From self-1.md (Oct 2024 – Feb 2026)

**NammaYatri / Haskell open source**
Haskell-based ride-sharing platform open sourced by Juspay, Oct 2024.
juspay.io — https://nammayatri.in/

**Yoneda Perspective (YouTube)**
Video lecture on the Yoneda lemma and its deep significance in category theory and functional programming.
youtu.be — https://youtu.be/

**Graham Hutton publications**
Research papers and books by Graham Hutton on functional programming.
cs.nott.ac.uk — http://www.cs.nott.ac.uk/~pszgmh/

**GitHub openai/lean-gym**
OpenAI's Lean 4 environment for training theorem-proving agents.
github.com — https://github.com/openai/lean-gym

**leandojo.org**
LeanDojo: open-source toolkit for machine learning on Lean proofs.
leandojo.org — https://leandojo.org/

**Fermat's Last Theorem in Lean**
Formalisation project for Fermat's Last Theorem using Lean 4.
leanprover-community.github.io — https://leanprover-community.github.io/

**Domain Modelling Made Functional (Scott Wlaschin)**
Book on applying DDD and F# functional patterns; referenced Dec 2024.
fsharpforfunandprofit.com — https://fsharpforfunandprofit.com/books/

**Finger Trees paper (Hinze & Paterson)**
Classic functional data structure paper — 2-3 finger trees for sequences.
staff.city.ac.uk — http://staff.city.ac.uk/~ross/papers/FingerTree.html

**RRB Trees**
Relaxed Radix Balanced Trees — efficient persistent vector implementation.
infoscience.epfl.ch — https://infoscience.epfl.ch/record/169879

**Hylomorphisms**
Recursion schemes combining anamorphisms and catamorphisms.
blog.sumtypeofway.com — https://blog.sumtypeofway.com/posts/recursion-schemes-part-4-5.html

**Recursion schemes intro (Sum Type of Way)**
Practical introduction to recursion schemes in functional programming.
blog.sumtypeofway.com — https://blog.sumtypeofway.com/posts/introduction-to-recursion-schemes.html

**Catamorphisms (HaskellWiki)**
Wiki page on catamorphisms and folds in Haskell.
wiki.haskell.org — https://wiki.haskell.org/Catamorphisms

**"Oh, the morphisms you'll see!" (Patrick Thomson)**
Survey of recursion schemes: hylo, chrono, zygo, histo, and more.
blog.sumtypeofway.com — https://blog.sumtypeofway.com/posts/recursion-schemes-part-6.html

**FP jargon**
Plain-English definitions of functional programming terminology (monad, functor, etc.).
github.com — https://github.com/hemanth/functional-programming-jargon

**Ralf Hinze publications**
Academic papers on functional data structures and generic programming.
cs.ox.ac.uk — https://www.cs.ox.ac.uk/ralf.hinze/

**Constraints Liberate, Liberties Constrain (Runar Bjarnason)**
Talk on how type constraints lead to composable, reusable code.
youtube.com — https://www.youtube.com/watch?v=GqmsQeSzMdw

**Simple Made Easy (Rich Hickey)**
Classic talk distinguishing simplicity from ease in software design.
youtube.com — https://www.youtube.com/watch?v=LKtk3HCgTa8

**Haskell Notes for Professionals**
Free Haskell reference book compiled from Stack Overflow.
goalkicker.com — https://goalkicker.com/HaskellBook/

**SplinterDB**
VMware's key-value store research project with novel B-tree design.
github.com — https://github.com/vmware/splinterdb

**MoonBit language**
New compiled functional language targeting WASM from MoonBit team.
moonbitlang.com — https://www.moonbitlang.com/

**Mind-bending GPU language Bend**
Bend: a high-level language that runs on GPUs using interaction nets.
github.com — https://github.com/HigherOrderCO/Bend

**8 months of OCaml after Haskell (chshersh)**
Personal retrospective on switching from Haskell to OCaml; Jan 2025.
chshersh.com — https://chshersh.com/blog/2023-12-16-ocaml-after-haskell.html

**Static search trees — 40x faster than binary search**
Blog post on cache-oblivious Eytzinger layout for search trees.
algorithmica.org — https://algorithmica.org/en/eytzinger

**Unison docs — abilities (effects)**
Unison language documentation on its algebraic effects system.
unison-lang.org — https://www.unison-lang.org/learn/fundamentals/abilities/

**Category Theory Catsters (YouTube)**
Eugenia Cheng's category theory lecture series.
youtube.com — https://www.youtube.com/user/TheCatsters

**Comonads are objects (Haskell)**
Blog post connecting comonads to OOP-style objects.
haskellforall.com — https://www.haskellforall.com/

**WHNF (Weak Head Normal Form) — StackOverflow**
Explanation of lazy evaluation and WHNF in Haskell.
stackoverflow.com — https://stackoverflow.com/questions/6872898/

**Nobody Gets Fired for JSON (serialisation comparison)**
Article comparing JSON vs Thrift/Protobuf/MessagePack for production systems.
steveklabnik.com — https://steveklabnik.com/

**Type Classes in Scala 3**
Tutorial on Scala 3's given/using typeclass mechanism.
docs.scala-lang.org — https://docs.scala-lang.org/scala3/book/ca-type-classes.html

**Recursion Schemes in Scala**
Deep dive into catamorphisms and anamorphisms using Scala.
medium.com — https://medium.com/

**Mill Scala build tool**
Comparison of Mill vs SBT for Scala projects.
mill-build.com — https://mill-build.com/

**Type Class Derivation Scala 3**
Scala 3 docs on automatic typeclass derivation with Mirror.
docs.scala-lang.org — https://docs.scala-lang.org/scala3/reference/contextual/derivation.html

**Monad is Monoid in Category of Endofunctors**
Explanation of the famous categorical characterisation of monads.
stackoverflow.com — https://stackoverflow.com/questions/3870088/

**Kleisli — Typelevel docs**
Cats library documentation on the Kleisli data type.
typelevel.org — https://typelevel.org/cats/datatypes/kleisli.html

**Y Combinator in Lambda Calculus**
Derivation and explanation of the Y combinator for anonymous recursion.
blog.klipse.tech — https://blog.klipse.tech/lambda/2016/08/10/pure-functional-programming.html

**Kyo getkyo.io**
Kyo effect system for Scala 3 — official site and documentation.
getkyo.io — https://getkyo.io/

**Algebraic Effects from Scratch — Kyo talk**
Talk on implementing algebraic effects in Scala without monadic stacks.
youtube.com — https://www.youtube.com/

**Data.Conduit.Combinators (Haskell)**
Haskell streaming library Conduit combinators documentation.
hackage.haskell.org — https://hackage.haskell.org/package/conduit-extra

**Bifunctors (Haskell/Scala)**
Explanation of the Bifunctor typeclass and its uses.
hackage.haskell.org — https://hackage.haskell.org/package/base/docs/Data-Bifunctor.html

**Turtle Haskell shell scripting**
Haskell library for shell-script-style programming.
hackage.haskell.org — https://hackage.haskell.org/package/turtle

**FP with TypeScript playlist**
Video series on functional programming patterns using TypeScript.
youtube.com — https://www.youtube.com/

**Haskell Dijkstra (generalized)**
Implementing Dijkstra's shortest path in Haskell idiomatically.
stackoverflow.com — https://stackoverflow.com/questions/

**Haskell tail recursion and deforestation**
Article on tail recursion optimization and stream fusion in Haskell.
debasishg.blogspot.com — https://debasishg.blogspot.com/

**Lambda calculus blog (klipse)**
Introduction to untyped lambda calculus and reduction rules.
blog.klipse.tech — https://blog.klipse.tech/lambda/

**Haskell arrows**
Introduction to Haskell arrows as a generalisation of monads.
haskell.org — https://www.haskell.org/arrows/

**Haskell unfold / anamorphism**
Building lists and trees from seeds using unfold / ana.
hackage.haskell.org — https://hackage.haskell.org/package/base/docs/Data-List.html#v:unfoldr

**Most Influential CS Papers**
Curated list of landmark computer science research papers.
github.com — https://github.com/papers-we-love/papers-we-love

**A 2025 Scala stack**
Blog post recommending a modern Scala 3 technology stack for production.
blog.rockthejvm.com — https://blog.rockthejvm.com/

**Building Robust Applications with Kyo**
Guide to error handling and resource management using the Kyo effect system.
getkyo.io — https://getkyo.io/

**Writing Modular Apps with Kyo**
Blog on modular application design using Kyo's algebraic effects.
getkyo.io — https://getkyo.io/

**Kyo — Functional Scala 2023 talk**
Conference talk introducing Kyo's effect system design.
youtube.com — https://www.youtube.com/

**Scala 3 extension methods**
Official docs on extension methods in Scala 3.
docs.scala-lang.org — https://docs.scala-lang.org/scala3/book/ca-extension-methods.html

**etorreborre blog: 2024 in review**
Year-in-review from a prominent Scala/specs2 contributor.
etorreborre.blogspot.com — https://etorreborre.blogspot.com/

**Typed Tagless Final for Real (Oleg Kiselyov)**
Oleg Kiselyov's typed tagless final interpreter approach.
okmij.org — https://okmij.org/ftp/tagless-final/

**What is so unique about Unison**
Blog on Unison's content-addressed code and abilities system.
unison-lang.org — https://www.unison-lang.org/

**Unison cloud platform**
Unison's cloud-native distributed computing platform.
unison.cloud — https://www.unison.cloud/

**Profunctors, Arrows, and Static Analysis**
Connecting profunctors to arrow-based static analysis in Haskell.
ocharles.org.uk — https://ocharles.org.uk/

**Open-sourcing Haxl (Facebook)**
Facebook's Haskell library for efficient batched data fetching.
engineering.fb.com — https://engineering.fb.com/

**Applicative Effects and Free Monads**
Comparison of applicative and monadic effect handling strategies.
blog.functorial.com — https://blog.functorial.com/

**lens (ekmett/lens)**
Haskell's premier optics library.
github.com — https://github.com/ekmett/lens

**PRE-SIP: suspended functions in Scala**
Proposal for coroutine-style suspended functions in Scala.
github.com — https://github.com/scala/improvement-proposals

**Capture Checking in Scala 3**
Scala 3 experimental feature for tracking object capabilities via capture sets.
docs.scala-lang.org — https://docs.scala-lang.org/scala3/reference/experimental/cc.html

**Haskell kinds and HKTs (Serokell)**
Tutorial on kind polymorphism and higher-kinded types in Haskell.
serokell.io — https://serokell.io/blog/

**Comonad can be monad**
Mathematical exploration of comonads as dual structures to monads.
bartoszmilewski.com — https://bartoszmilewski.com/

**Free monad blog (Reasonably Polymorphic)**
Practical guide to free monads as an effect encoding strategy.
reasonablypolymorphic.com — https://reasonablypolymorphic.com/

**Haskell Fix and recursion**
Using `fix` for recursive definitions in Haskell without `let rec`.
hackage.haskell.org — https://hackage.haskell.org/package/base/docs/Data-Function.html#v:fix

**Recursion schemes in Rust**
Applying catamorphisms and anamorphisms in Rust.
github.com — https://github.com/

**Understanding F-Algebras (Bartosz Milewski)**
Category-theoretic explanation of F-algebras and recursion.
bartoszmilewski.com — https://bartoszmilewski.com/2013/06/10/understanding-f-algebras/

**unfoldable (Hackage)**
Haskell package for unfoldable data structures.
hackage.haskell.org — https://hackage.haskell.org/package/unfoldable

**Existential types in Haskell**
Explanation of existential quantification in Haskell type system.
wiki.haskell.org — https://wiki.haskell.org/Existential_type

**A gentle run-through of CPS**
Continuation-passing style explained from first principles.
matt.might.net — https://matt.might.net/articles/

**Haskell book recommendations (Reddit)**
Community curated list of Haskell learning resources.
reddit.com — https://www.reddit.com/r/haskell/

**Quick Overview Haskell Streamly**
Introduction to Streamly, a high-performance Haskell streaming library.
github.com — https://github.com/composewell/streamly

**Pavel Fatin: Design Patterns in Scala**
Applying Gang of Four patterns in idiomatic Scala.
pavelfatin.com — https://pavelfatin.com/

**Alexis King blog**
Deep technical posts on Haskell, effects, and type system topics.
lexi-lambda.github.io — https://lexi-lambda.github.io/

**Kyo Memory.scala**
Memory management abstraction in the Kyo effect system source.
github.com — https://github.com/getkyo/kyo

**Tweag named routes**
Named route pattern for type-safe web APIs in Haskell/Servant.
tweag.io — https://www.tweag.io/

**Noel welsh tagless final talk**
Conference talk on tagless final interpreters in Scala.
youtube.com — https://www.youtube.com/

**Expression problem**
Classic extensibility problem in programming language design.
wiki.haskell.org — https://wiki.haskell.org/Expression_problem

**Scala 3 REST API with ZIO**
Tutorial on building REST APIs using ZIO and http4s.
blog.rockthejvm.com — https://blog.rockthejvm.com/

**Compiler tagless final / okmij tagless final**
Oleg Kiselyov's authoritative reference on tagless final interpreters.
okmij.org — https://okmij.org/ftp/tagless-final/

**Scala distributed system from scratch**
Building a simple distributed system in Scala 3.
github.com — https://github.com/

**GitHub capture checking (experimental)**
Tracking the experimental capture checking feature in Scala 3 compiler.
github.com — https://github.com/scala/scala3

**Whiteboxish Named Tuples (Scala 3) — Scalar 2025**
Conference talk on named tuple improvements in Scala 3.
scalar-conf.com — https://scalar-conf.com/

**Evaluating AI on Haskell tasks**
Benchmark study on LLM performance writing correct Haskell code.
github.com — https://github.com/

**Parsley Scala parser combinator library**
Scala 3 parser combinator library with Haskell-like interface.
github.com — https://github.com/j-mie6/Parsley

**LSUG Parsley talk**
London Scala User Group talk on the Parsley library.
youtube.com — https://www.youtube.com/

**Hazel live functional programming**
Live programming environment for Hazel, a functional language with holes.
hazel.org — https://hazel.org/

**Zig and Rust comparison (matklad)**
Matklad's thoughtful comparison of Zig and Rust design choices.
matklad.github.io — https://matklad.github.io/

**GitHub: Developer-Y/cs-video-courses**
Comprehensive list of CS courses with freely available video lectures.
github.com — https://github.com/Developer-Y/cs-video-courses

**Legalizing Comonad Composition**
Mathematical treatment of composing comonads correctly.
blog.functorial.com — https://blog.functorial.com/

**Hylomorphism and refold code snippets**
Code examples exploring hylomorphisms implemented in Scala/Haskell.
github.com — https://github.com/

**PL Zoo**
Programming language implementations collection for learning PL theory.
plzoo.andrej.com — https://plzoo.andrej.com/

**De Bruijn index**
Wikipedia article on De Bruijn indices for name-free lambda calculus.
en.wikipedia.org — https://en.wikipedia.org/wiki/De_Bruijn_index

**tree-sitter**
Parser generator tool for building syntax trees for any language.
tree-sitter.github.io — https://tree-sitter.github.io/tree-sitter/

**Rhombus lang**
New Racket-based language with improved syntax from the Racket team.
github.com — https://github.com/racket/rhombus-prototype

**Which programming languages are most token-efficient?**
Analysis of token counts across 19 languages on RosettaCode — Clojure vs C shows 2.6x difference.
martinalderson.com — https://martinalderson.com/posts/which-programming-languages-are-most-token-efficient/

**LLM-Generated Lean 4 Proofs (research paper)**
Study comparing GPT-5, Gemini, and other LLMs on formal Lean 4 proof generation.
github.com — https://github.com/lampless/LLM-Generated-Lean4-Proofs/blob/main/Dylan%20Miller_%20LLM-Generated%20Lean4%20Proofs.pdf

**Rust replaces Java/Scala at xAI (tweet)**
xAI's x-algorithm repo uses Rust where Java/Scala were expected.
x.com — https://x.com/ForrestPKnight/status/2018768871474315761

**GitHub: duolingo/slack-mcp**
Duolingo's OAuth-based multi-user Slack MCP server with HTTP transport.
github.com — https://github.com/duolingo/slack-mcp

**Kyo issue tracker**
Active Kyo issues and feature discussions on GitHub.
github.com — https://github.com/getkyo/kyo/issues/1419

**Agentic Reasoning for Large Language Models (survey)**
Comprehensive arxiv survey organizing agentic reasoning — foundational, self-evolving, multi-agent.
arxiv.org — https://arxiv.org/abs/2601.12538

**Intelligent AI Delegation (arxiv)**
Framework for adaptive task allocation and authority transfer in multi-agent AI systems.
arxiv.org — https://arxiv.org/abs/2602.11865

**Claude Code design decisions talk (Tech with Mak)**
45-minute talk by the Claude Code creator on design decisions and future direction.
x.com — https://x.com/techNmak/status/2024041443837526375

**User personal note: Eke project plan**
Project priorities: Haskell unfold, Kyo integration, Wiktionary parsing, Alar dictionary; referenced Jan–Feb 2025.

**User observation: Claude for Kannada DNS Bhat analysis**
Claude used for Kannada video transcription and DNS Bhat book analysis — better than NotebookLM for discovery. Generated output that would have required extensive hand-coding.
github.com — https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/malatibhat_dns_bhat_chat.md

**ettuge/dnsbhat Kannada grammar chapters (GitHub)**
Series of markdown notes translating DNS Bhat's Kannada grammar chapters.
github.com — https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/dnsbhat/

**mEStre Kannada AI app concept**
Personal product idea: Kannada AI assistant that code-switches between pure Kannada and Kanglish, with autocomplete, agent integrations, and ad platform; Feb 2026.

**Ship an MCP server/agent**
Personal architectural note: shipping an MCP server makes downstream integrations compose automatically.

**Skill graph for memory (tweet)**
A network of skill files connected with wikilinks — useful pattern for AI agent memory systems.
x.com — https://x.com/rohit4verse/status/2024031053103366528

**RAG architecture selection guide (Tech with Mak)**
Which RAG variant to pick by use case: standard, agentic, graph, modular, or long-term memory.
x.com — https://x.com/techNmak/status/2023978105606676821

**Transformers use 6D helical manifolds for counting (Anthropic)**
Reverse-engineering Claude 3.5 Haiku reveals it tracks numbers via geometric manifolds, not registers.
x.com — https://x.com/che_shr_cat/status/2023729615055782140

**Scala 3 'break' and 'continue' equivalents**
How to express early exit patterns idiomatically in Scala 3.
blog.rockthejvm.com — https://blog.rockthejvm.com/
