## unfolding min k elements lazily

### Problem

Finding the min k or max k elements: [^1] in contrast to finding the min kth or max kth element: [^19] are slightly different problems.

We'll focus on the former.

For a list of size n, where the minimum k elements need to be obtained: 
The naive approach is to sort it first using an efficient n log n algorithm (say quick sort) and then picking the first k elements. So it's O(k + n log n) => O(n log n).

It can be improved to n log k using one of the following methods:
1. Use a heap of size k. Scan the n elements and add each element to the heap of size k. If the heap is full, and a new element needs to be inserted,  toss the largest element in favor of the new smaller element. Each insertion is order log k and there are n such insertions to consider.
1. Use a variation of quick sort.
quick sort sorts in some m steps by dividing the list into a lesser and larger sublist around a pivot element (which can be the first element in the sub list if there's no random access).
For finding the k minimum numbers we don't need a total sort. If the smallest sublist that contains the k elements are sorted, we don't really need to sort the rest.

Variation 2 above can be retrofitted to provide a linear time solution, if you are interested only in the min kth element using QuickSelect. A subsequent filtering of all elements <=k can be done to achieve it in linear time but that's a different topic.

This is mostly about an exploration of folds and unfolds in the context of the stated problem.

### Motivation
This write-up started on a 1-liner in "Real World Haskell" that "take" composed with "sort" is idiomatic in haskell unlike strict languages.

### History
I played around a qsort that I had written earlier and cleaned it up to use a fold and went down a rabbit hole of foldl v/s foldl' v/s foldr.
[^20]

Earlier I had done it using list comprehension. s, m, l are lists that represent less, equal and more than the pivot element - which is
nominally picked as the head.

```
qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort ns = (qsort s) ++ m ++ (qsort l) where
  x = head ns
  s = [n | n <- ns, n < x]
  l = [n | n <- ns, n > x]
  m = [n | n <- ns, n == x]
```

The cool part is that qsort can be done so simply and elegantly with some differences:
1. This is not in-place unlike the classic imperative one. It might negate the reason why quick sort is preferred in the imperative version over other sorts
because it is in-place.
1. It is not tail-recursive and won't work well for larger numbers on eagerly evaluated languages. This is due to work being done after the recursive step. In eagerly evaluated languages this won't fly. [^21] discusses that gradation from naive -> tail recursive -> immutable stack/queue -> imperative.
1. There are 3 passes to get s,m and l which seems excessive.
Rewriting to tail recursive or switch to trampolining to put the intermediates on the heap rather than the stack are rabbit holes [^4][^5][^6]. See the rabbit holes section in the end. All I'll note is that in Haskell, it's not as critical to make it tail recursive. In scala, you pretty much have to. Addressing Point 2 gets into classic writeups on tail recursion. Addressing point 1 gets into classic imperative quick sort implementations where there may be nothing new. See [^21].

Let's say I try to address just Point 3. I tried to reduce it to 2 passes as is before realizing that recursive steps are needed only for s and l.
1 pass would seem sufficient with a loop, or a slightly contorted comprehension. I decided to use fold instead.

```
qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort elems = qsort lt ++ eq ++ qsort gt where
  pivot = head elems
  emptysml = (mempty, mempty, mempty)
  (lt, eq, gt) = foldl' (\(lt, eq, gt) elem ->
                  if elem < pivot
                    then (elem:lt, eq, gt)
                  else if elem == pivot
                    then (lt, elem:eq, gt)
                  else
                    (lt, eq, elem:gt)
                  ) emptysml elems
```

### Notes on Fold

See  discussion on folds and recursion schemes for more details: [^22].

Here I just tried foldr, foldl and foldl'. foldr is idiomatic in haskell and is amenable for infinite lists but not tail-recursive. foldl is tail-recursive but can't handle infinite lists. foldl' is the same as foldl but avoids the space leaks of foldl - due to Haskell being a lazy language - it builds up code thunks for each element in the list - that are more expensive than the primitive number itself. foldl' uses "seq" to forces the eager evaluation of the constructor to Weak Head Normal Form. See [^7][^8][^9][^15][^16] for details.

In short, use foldr in general in Haskell. foldl' in special cases. foldl never.
In scala, use foldl most of the time unless you want to rewrite in imperative loop style for performance and remember to add the @tailrecursive tag to have the compiler check that it is indeed tail recursive. 
foldr - almost never - unless you are dealing with streams or infinite lists. More on that as I dig more in to comonads.

### Notes on Unfold

Basically "unfold" takes a terminating condition and can keep generating a recursive structure till that condition is met. It is an anamorphism. It is the dual to "fold" which can take a recursive structure and reduce it to a simple or complex value. The datastructure generated can be infinite if there is no terminating condition for the generating function.

List - like many other structures provides an unfoldr.

```
unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
```

If Nothing is returned, the list generation terminates. Otherwise it recursively adds whatever value of type 'a' is returned by the function i.e. 'a' in Maybe(a, b).

The convention of using 'b' for this type and 'a' for the returned type is also the reverse of what you would see in a fold.

### unless and until
A short wrapper around unfold (generating functions) helped me do some interesting things. Here it seemed interesting that classic programming language control path-like things like "until" (called "unless" to avoid clashing with the standard library) can be created.

Here the parameters for "unless" are pun intended.
So that you can read the subsequent calls in the same style.

```
unless counter reaches end step init f =
  unfoldr (tillcount reaches end step init f) counter where
  tillcount reaches end step init f counter =
    if counter `reaches` end
    then Nothing
    else Just(f counter, counter `step` init)
```

So that you can use it like:

```
ghci> unless 0 (==) 10 (+) 1 id
[0,1,2,3,4,5,6,7,8,9]
-- "id" does nothing, i.e a -> a
-- unless 0 equals 10 add 1 until we get 10

ghci> unless 0 (==) 10 (+) 1 (*2)
[0,2,4,6,8,10,12,14,16,18]
-- unless 0 equals 10 add 1 until we get 10, multiply the result by 2
```

Let's see the type signatures a bit

```
unless :: (Ord b) =>       -- Precondition: Input type b must be ordinal
      b ->                 -- counter, LHS of Comparison,    10
      (b -> b -> Bool) ->  -- reaches, Comparison operator, (==)
      b ->                 -- end, RHS of comparison,         0
      (b -> b -> b) ->     -- step, func appl at each step,  (+) 
      b ->                 -- init, value for step            1
      (b -> a) ->          -- f(o/p) prior to ins in [a], id, (*2) etc
      [a]                  -- returned list of type a

tillcount ::               -- A lambda func to be supplied to unfoldr 
      (b -> b -> Bool) ->  -- reaches
      b ->                 -- end
      (b -> b -> b) ->     -- step 
      b ->                 -- init
      (b -> a) ->          -- f
      b -> Maybe (a, b)    -- returns a func which can be fed to unfoldr
                           -- i.e. takes counter of type b
                           -- and returns Maybe (a,b)
 
unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
```

Great for generating test cases - declaratively.

```
ghci> unless 10 (<) 0 (-) 1 id 
[10,9,8,7,6,5,4,3,2,1,0]
ghci> unless 10 (>=) 0 (-) 1 (*2)
[]
ghci> unless 10 (<) 0 (-) 1 (*2)
[20,18,16,14,12,10,8,6,4,2,0]
```

\ in haskell is shorthand for λ as in λ functions. Just replace the parameter in the function body.
Here, I am ignoring init parameter of step, since sqrt takes only 1 input.

```
ghci> unless (10.0^^20) (<) (sqrtFloat 2.0) (\x _ -> sqrtFloat x) 1 id
[1.0e20,1.0e10,100000.0,316.22775,17.782793,4.2169647,2.053525,1.4330126]
```

This can be cleaned up to have more specific function signatures where id, step are skipped and 1 param function is taken. However the λ helps shoehorn it for now.

### Continuing
Coming back to the original problem, qsort is not tail recursive and lazily evaluated, it does give some interesting side effects (punintended).

When this function is composed with another one that takes a subset like "take 3", the function returns when the 3 least elements are known instead of waiting
for the full sort. This is interesting indeed.

Below, you can read $ as ( with closing bracket ) at end of the line. Just more readable than ().

```
ghci> take 3 $ qsort $ unless 1000000 (<) 0 (-) 1 id
[1,2,3]
still works at reasonable pace compared to full sort
ghci> qsort $ unless 1000000 (<) 0 (-) 1 id
which takes far longer.
```

This means "take 3" works on the partially sorted values due to laziness - unlike strict languages which would have fully sorted and then taken the first few values.

### but not too much or Not extending to Infinite Lists:

I thought this interesting property can be extended to infinite lists but algorithmically it can't since sort ends up looking at every element.
If I restrict the problem to min k only:
With integers and reals that's not guaranteed looking at the types. With natural numbers, you could theoretically do it, if there are no repeats. Even then E.g. 0 could wait forever before coming in. You need to guarantee that minimum k elements are in a finite sublist of the list, preceded by finite number of elements.

E.g. An arbitrary list of natural numbers with no repeats, with the 0, 1 and the prime numbers in ascending order - [0, 1, 2, 3, 5, 4, 7, 6, ...]. However this guarantee needs to be encoded in the type before a min K can be made to work on infinite lists. Otherwise, the program won't terminate in the general case. Since this seems very restrictive, I'll not go in the infinite list case any more other than noting that when you deal with streams do not peek too far into it [^15]

### Summary
The naive approach being idiomatic in haskell was still surprising to me even though I knew haskell was lazy. In a sense laziness in calculating the sort is buying the ability to compose/chain it with take and aborting when the list is partially sorted enough.

### A continuation to recursion schemes
As noted in [^22] there's more to recursion schemes than fold and unfold. 

You can look at them as an alternate control flow theory where you may want to write immutable code
- Imperative constructs like loops are not feasible
- Unstructured constructs like goto are best avoided
- Hand coding recursion can be error-prone
- Writing tail recursion to avoid the stack overflow pitfalls is good, but seems less elegant than the simple recursive idea.

It turns out there's an excellent library to get you started beyond the theory in [^22] - the recursion-schemes library: [^23]

An excellent flowchart from there provides a handy guide on when to use what:


![alt text](https://github.com/recursion-schemes/recursion-schemes/blob/master/docs/flowchart.svg?raw=true "A guide to recursion schemes")

Let's take a simpler problem. Let's say we want to find the sum of digits of a natural number [^24] in a functional style.

The naive approach would be recursive. You could make it tail recursive. With some thought, it looks like a variation of a fold or unfold.

Using unfoldr:

```
sumd1 :: Natural -> Natural
sumd1 = sum . unfoldr \case
    0 -> Nothing
    x -> Just (x `mod` 10, x `div` 10) 
```

However one would still need to think whether the terms that are expanded by unfold are collapsed by sum (which is defined as a fold with (+)). Instead of manually combining an unfold (anamorphism) and a fold (catamorphism), one can directly use a refold (hylomorphism). The intermediate structures are then guaranteed not to be created and then collapsed. The definitions for hylo(refold), cata(unfold) and ana(fold) from recursion-schemes are provided here for clarity. See [^27] for details.

```
cata :: (Base t a -> a) -> t -> a
cata f = c where c = f . fmap c . project

-- | An alias for 'unfold'.
ana
  :: (a -> Base t a) -- ^ a (Base t)-coalgebra
  -> a               -- ^ seed
  -> t               -- ^ resulting fixed point
ana g = a where a = embed . fmap a . g

-- | An alias for 'refold'.
hylo :: Functor f => (f b -> b) -> (a -> f a) -> a -> b
hylo f g = h where h = f . fmap h . g

```

To understand recursion schemes from a theoretical perspective F* algebras are helpful. A category theoretic explanation is provided here: [^29]. However this is not necessarily a design overview of the recurion-schemes library itself.

Unlike the prelude, recursion-schemes uses a slightly different structure for defining the base cases. Note the "(Base t a -> a)". Instead of using a Maybe to construct/destruct a list, it uses a Cons structure that is more amenable to handle recursion schemes. E.g. See [^28]

```
data ListF a b = Nil | Cons a b
```
Here b is the recursive structure. a is the thing that goes in to the list - the base case. This structure helps extract/create the base case for folding/unfolding/refolding.

Using this the sum of digits can be written as: [^26]

```
sumd :: Natural -> Natural
sumd = refold (\case Nil -> 0; Cons x y -> x + y)
              (\case 0 -> Nil; x -> Cons (x `mod` 10) (x `div` 10))

ghci> sumd 102348
18
```

This can be more nicely explained by plugging into chat GPT.

```
That’s a nice use of refold! It looks like you’re defining sumd to compute the sum of digits of a natural number using a refold, which essentially mirrors an unfold-followed-by-a-fold pattern.

Your unfold (\case 0 -> Nil; x -> Cons (x mod 10) (x div 10)) breaks the number into its digits, and the fold (\case Nil -> 0; Cons x y -> x + y) sums them up. Very elegant!
```

And voila - recursion without hand coding. And further, using hylomorphism guarantees no extraneous temporary structures. It's a bit magical!

There is a quick sort example in [^27] which uses a hylomorphism to transform the sublists on a pivot into Trees that notionally exist only for the sake of merging. It does not do an in-place imperative quick sort but avoids creating a full-fledged tree and then collapsing it. Instead it builds one step of a Tree at a time and collapses into a list, sorting along the way.

Given that a solution for avoiding direct recursion altogether was in sight - Things that recurse multiple times are usually harder to
make tail recursive - I decided to just complete the quick sort using recursion-schemes. The solutions in [^21] make use of an explicit auxiliary data structure like an immutable list, stack or queue to ensure that it can be made tail recursive. However with recursion-schemes, we can just use the library appropriately and get the results we need.

This code is mostly the version in the example with minor modifications using the internal methods developed earlier.

```
data BinTreeF a b = Tip | Branch b a b deriving (Functor)

qsort' :: (Ord a) => [a] -> [a]
qsort' = refold merge split where
  merge :: (Ord a) => BinTreeF [a] [a] -> [a]
  merge Tip = []
  merge (Branch lt xs gt) = lt ++ xs ++ gt

  split :: (Ord a) => [a] -> BinTreeF [a] [a]
  split [] = Tip
  split (x:xs) = Branch lt xs' gt where
    (lt, xs', gt) = foldl'
                  (\(lt, xs', gt) elem ->
                     if elem < x then
                         (elem:lt, xs', gt)
                       else
                        if elem > x then
                          (lt, xs', elem:gt)
                        else
                          (lt, elem:xs', gt)) 
                  ([], [], []) xs```

```
ghci>:set +t
ghci> import System.Random
ghci> pureGen = mkStdGen 137
ghci> rs = take 10000000 randomRs (10, 10000) pureGen
ghci> qsort rs
(169.63 secs, 100,863,083,848 bytes)
ghci> qsort' rs
(169.55 secs, 99,502,972,936 bytes)
```
The naive and the recursion-schemes perfomrm almost identically once similar logic is used in both. Its good to know that neither version overflows the stack (primarily due to haskell's graph reduction scheme unlike strict languages) even though the laptop - a first generation mac m1 gets quite warm churning all those numbers.

More general morphisms are discussed in [^30]

### References
[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22]

[^1]: https://stackoverflow.com/questions/5380568/algorithm-to-find-k-smallest-numbers-in-array-of-n-items
[^2]: https://learnyouahaskell.com/
[^3]: https://stackoverflow.com/questions/2394684/in-haskell-how-can-you-sort-a-list-of-infinite-lists-of-strings#2395508
[^4]: https://eed3si9n.com/herding-cats/stackless-scala-with-free-monads.html
[^5]: https://stackoverflow.com/questions/76182328/how-to-do-tail-call-optimisation-in-scala3
[^6]: https://www.reddit.com/r/haskell/comments/f97qok/enforcing_tail_recursion_in_haskell/
[^7]: http://debasishg.blogspot.com/2009/01/to-tail-recurse-or-not-part-2-follow-up.html
[^8]: https://paul.bone.id.au/blog/2017/03/16/tail-recursion/
[^9]: https://free.cofree.io/2017/11/13/recursion/
[^10]: https://stackoverflow.com/questions/28652452/what-is-the-correct-definition-of-unfold-for-an-untagged-tree
[^11]: https://stackoverflow.com/questions/46716122/haskell-length-runtime-o1-or-on
[^12]: https://ris.utwente.nl/ws/portalfiles/portal/6142049/meijer91functional.pdf
[^13]: https://stackoverflow.com/questions/6119225/overloading-function-signatures-haskell
[^14]: https://medium.com/p/1b7a709fb71f#efe2
[^15]: https://en.m.wikibooks.org/wiki/Haskell/Graph_reduction
[^16]: https://hmac.dev/posts/2019-03-09-graph-reduction.html
[^17]: https://www.microsoft.com/en-us/research/wp-content/uploads/1992/01/student.pdf
[^18]: https://www.microsoft.com/en-us/research/wp-content/uploads/1987/01/slpj-book-1987-small.pdf
[^19]: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
[^20]: https://github.com/vwulf/ettuge/blob/master/src/main/haskell/quick/src/qsortof.hs
[^21]: https://github.com/vwulf/ettuge/blob/master/src/main/scala/quick/main.scala
[^22]: https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/%E0%B2%95%E0%B2%B3%E0%B3%8D%E0%B2%B3.md
[^23]: https://github.com/recursion-schemes/recursion-schemes/tree/master
[^24]: https://x.com/chshersh/status/1895135789727526920?s=61
[^25]: https://x.com/sampocino/status/1895168609262915682?s=61
[^26]: https://x.com/vishwasms/status/1897230479088296057?s=61
[^27]: https://github.com/recursion-schemes/recursion-schemes/blob/master/src/Data/Functor/Foldable.hs
[^28]: https://github.com/recursion-schemes/recursion-schemes/blob/master/src/Data/Functor/Base.hs
[^29]: https://bartoszmilewski.com/2017/02/28/f-algebras/
[^30]: https://blog.sumtypeofway.com/posts/recursion-schemes-part-5.html
