---
title: Algorithms & Data Structures
created: 2026-02-25
source: self.md (not in repository)
---

# Algorithms & Data Structures

> Derived from `self.md` · Created: 2026-02-25

LeetCode solutions, algorithm resources, and data structure notes from the source log.

---

## Books & Courses

Algorithms by Jeff Erickson
jeffe.cs.illinois.edu
https://jeffe.cs.illinois.edu/teaching/algorithms/

GitHub - ossu/computer-science: Path to a free self-taught education in Computer Science!
https://github.com/ossu/computer-science

GitHub - Coder-World04/Tech-Interview-Important-Topics-and-Techniques
https://github.com/Coder-World04/Tech-Interview-Important-Topics-and-Techniques

## LeetCode Patterns

Ashish Pratap Singh (@ashishps_1): LeetCode was HARD until I Learned these 15 Patterns:
1. Prefix Sum
2. Two Pointers
3. Sliding Window
4. Fast & Slow Pointers
5. LinkedList In-place Reversal
6. Monotonic Stack
7. Top 'K' Elements
8. Overlapping Intervals
9. Modified Binary Search
10. Binary Tree Traversal
11. (and more)
https://x.com/ashishps_1/status/1814884401249198569

Alex Xu: Recommended materials for technical interview

Arpit Adlakha (@arpit20adlakha): Finest roadmaps for Senior Software Interviews — Uber L5A/L5B or Google L5/L6 levels
https://x.com/arpit20adlakha/status/1805084468870521100

1: TinyURL + PasteBin — Systems Design Interview Questions With Ex-Google SWE (YouTube)
https://youtu.be/5V6Lam8GZo4

## Knight's Tour

The Knight's Tour (boraberan.wordpress.com)
https://boraberan.wordpress.com/2012/09/28/the-knights-tour/

Warnsdorff's algorithm for Knight's tour problem — GeeksforGeeks
https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/

Knight's tour — Wikipedia
https://en.wikipedia.org/wiki/Knight's_tour

Warnsdorff's rule PDF
https://raw.githubusercontent.com/douglassquirrel/warnsdorff/refs/heads/master/5_Squirrel96.pdf

Graph theory origins in Sanskrit poetry and Arabic — highly entertaining YouTube
https://youtu.be/DjZB9HvddQk
https://youtu.be/DjZB9HvddQk

### Scala Knight's Tour Validation (LeetCode)

Version 1 (774ms, Beats 50%):
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

Version 2 (optimized, 710ms Beats 100% — removes O(n) visited scan):
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
Submitted as "kodebale" at Sep 25, 2024.

### Rust Knight's Tour Validation

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
                    if (r >= 0) && (r < n) && (c >= 0) && (c < n) &&
                       (grid[r as usize][c as usize] == knight_step + 1) {
                        Some(Rc{row:r as usize, col:c as usize})
                    } else {
                        None
                    }
                })
            })
        }
        fn check_tour(grid: &Vec<Vec<i32>>) -> bool {
            let n = grid.len() as isize;
            let mut curr = Rc{row: 0, col: 0};
            let mut next_o = get_next(grid, curr, n);
            while next_o.is_some() {
                curr = next_o.map_or_else(|| curr, |n| n);
                next_o = get_next(grid, Rc{row: curr.row, col: curr.col}, n);
            }
            grid[curr.row][curr.col] == ((n*n - 1) as i32)
        }
        check_init(&grid) && check_tour(&grid)
    }
}
```
Runtime 3ms, Beats 25.00%, Memory 2.05MB Beats 66.67%

## Concurrency: Dining Philosophers (Java, LeetCode)

https://leetcode.com/problems/the-dining-philosophers/

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
    // ... wantsToEat implementation
}
```

## fold / Short-Circuiting

Breaking out of the fold (Ethan Kent's dev blog)
Namely, we sometimes want to break out of the iteration within fold, but it is not easy to do in many languages.
https://ethankent.dev/posts/breaking_fold/

## Graph Theory

Massimo (@Rainmaker1973): Henri Poincaré proved the non-existence of the uniform first integral of the three-body problem and the sensitive dependence to initial conditions of its trajectories.
https://x.com/Rainmaker1973/status/1830309619966554272

Edward Kmett: Ask yourself why B-trees exist and are provably optimal for so many applications
https://x.com/kmett/status/1811904210021286014

## Probability

Applied Problems In Probability Theory — E. Wentzel
https://archive.org/details/wentzel-ovcharov-applied-problems-in-probability-theory

Exercises in Probability (Grimmett-Stirzaker, Oxford)
https://people.sabanciuniv.edu/atilgan/FE507_Fall2014/ProblemsProblems/Grimmett-Stirzaker_Oxford01_ExercisesInProbability.pdf

Probability Theory — Jaynes
http://www.med.mcgill.ca/epidemiology/hanley/bios601/GaussianModel/JaynesProbabilityTheory.pdf

Birthday problem — Wikipedia
https://en.wikipedia.org/wiki/Birthday_problem

Coin flip sequences notation:
```
(HT)HH(HT) => AAA, B
(HT)HT(HT) => A, BB
(HT)TH(HT) => A, BB
(HT)TT(HT) => B
```

## Topology / Category Theory

If the Universe Is a Hologram, This Long-Forgotten Math Could Decode It | Quanta Magazine
A 1930s-era breakthrough is helping physicists understand holographic space-time.
https://www.quantamagazine.org/if-the-universe-is-a-hologram-this-long-forgotten-math-could-decode-it-20240925/

"Conceptual Mathematics: A First Introduction to Categories" (Lawvere, Schanuel)
https://www.amazon.com/Conceptual-Mathematics-First-Introduction-Categories/dp/052171916X

Category theory without categories (johndcook.com)
https://www.johndcook.com/blog/2023/05/22/category-theory-without-categories/

## From self-1.md (Oct 2024 – Feb 2026)

**Competitive Programming Patterns — Advanced LeetCode**
Collection of advanced patterns for competitive programming: segment trees, tries, Dijkstra, union-find.
youtube.com — https://www.youtube.com/watch?v=...

**System Design: Instagram Scale — 2.5 Billion Users**
Deep dive into how Instagram architected their systems to support 2.5 billion users; sharding, caching, CDNs.
x.com — https://x.com/systemdesign42/status/1800491019663970354

**Rearchitecting Core Services at X (Twitter)**
Engineering overview of X's infrastructure rearchitecture: monolith-to-microservices, cost reduction.
x.com — https://x.com/cambridgemike/status/1835774409786986572

**B-Trees — Why They Are Provably Optimal**
Edward Kmett thread on the mathematical optimality of B-trees for many practical applications.
x.com — https://x.com/kmett/status/1811904210021286014

**Breaking Out of a Fold — Short-Circuiting Functional Iteration**
Blog post on techniques for early termination inside fold/reduce operations in functional programming.
ethankent.dev — https://ethankent.dev/posts/breaking_fold/

**Graph Neural Networks for Exact Scheduling (2022 Paper)**
Research using GNNs to accelerate exact solving of scheduling problems in industrial settings.
arxiv.org — file:///Users/vishwas/Downloads/2022Exactsolvingschedulingproblemsacceleratedbygraphneuralnetworks_RG.pdf

**AI for Production Scheduling — Systematic Literature Review**
Survey of AI techniques (PSO, neural nets, RL) for production scheduling; real industrial results.
mdpi.com — https://www.mdpi.com/2079-9292/12/23/4732

**Topological Data Analysis — Book Recommendation**
Frank Nielsen's recommendation for an introductory TDA textbook covering persistent homology and simplicial complexes.
x.com — https://x.com/FrnkNlsn/status/1814972379187093563

**Divergence as Adjoint of Gradient — PDE Primer**
Gabriel Peyré's explanation of divergence/gradient adjoint relationship via integration by parts; Laplacian workhorses.
x.com — https://x.com/gabrielpeyre/status/1816699972789628992

**Warnsdorff's Rule — Knight's Tour Heuristic**
Warnsdorff's 1823 heuristic for constructing knight's tours: always move to the square with fewest onward moves.
github.com — https://raw.githubusercontent.com/douglassquirrel/warnsdorff/refs/heads/master/5_Squirrel96.pdf

**Universal Algebra Pilot Project — Terry Tao**
Terry Tao's blog post on exploring new human-machine collaboration methods in universal algebra.
terrytao.wordpress.com — https://terrytao.wordpress.com/2024/09/25/a-pilot-project-in-universal-algebra-to-explore-new-ways-to-collaborate-and-use-machine-assistance/

**Grad Students Find Inevitable Patterns in Number Sets — Quanta**
New proof marking first progress in decades on arithmetic Ramsey theory: order emerging from disorder in large sets.
quantamagazine.org — https://www.quantamagazine.org/grad-students-find-inevitable-patterns-in-big-sets-of-numbers-20240805/

**Complexity Theory's 50-Year Journey to Knowledge Limits — Quanta**
History and current state of meta-complexity theory: how hard is it to prove hardness?
quantamagazine.org — https://www.quantamagazine.org/complexity-theorys-50-year-journey-to-the-limits-of-knowledge-20230817/

**Elliptic Curve Murmurations Discovered With AI — Quanta**
AI-discovered statistical patterns in elliptic curve families; mathematicians working to explain the phenomenon.
quantamagazine.org — https://www.quantamagazine.org/elliptic-curve-murmurations-found-with-ai-take-flight-20240305/

**How Base 3 Computing Beats Binary — Quanta**
Ternary (base-3) computing's theoretical advantages and potential applications in cryptography and computing.
quantamagazine.org — https://www.quantamagazine.org/how-base-3-computing-beats-binary-20240809/

**Geometric Langlands Conjecture — Monumental Proof — Quanta**
30-year effort culminating in proof of the geometric Langlands conjecture; connecting geometry, algebra, and number theory.
quantamagazine.org — https://www.quantamagazine.org/monumental-proof-settles-geometric-langlands-conjecture-20240719/

**Scientists Find a Fast Way to Describe Quantum Systems — Quanta**
New algorithm enabling efficient classical description of quantum system states, bypassing exponential blowup.
quantamagazine.org — https://www.quantamagazine.org/...

**OpenClaw Workflows — AI Agent Orchestration (Feb 2026)**
Framework for orchestrating multi-step AI agent workflows with dependency management and parallelism.
github.com — https://github.com/...

**Intelligent AI Delegation — Arxiv (Feb 2026)**
Research on automatic delegation strategies in multi-agent AI systems: when and how to hand off tasks.
arxiv.org — https://arxiv.org/abs/...
