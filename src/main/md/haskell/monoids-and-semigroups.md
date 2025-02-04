# Monoids are everywhere

Semigroups are those structures that have an associative "combine" operation.

The simplest example to understand are numbers (integers) wrt addition.

1 + 2 + 3 = (1 + 2) + 3 = 1 + (2 + 3)

Note that this definition does not require the definition of a 0 element.

If we add the requirement that there must be some 0 element.

i.e. a + 0 = 0 + a = a

then such a structure is called a monoiod.

Semigroups are everywhere and so are monoids.

1. ℕ \ {0} i.e. ℕ₁ is a semigroup under +, but not a monoid
1. ℕ with 0 i.e. ℕ₀ is a semigroup and a monoid under +
1. The set of positive integers ℤ⁺ is a semigroup under +, but not a monoid
1. ℤ = ℤ⁺ ⋃ {0} is a monoid and a semigroup under +
1. ℕ₁ is a monoid and a semigroup under ×
1. ℕ₁ - {1} is a semigroup but not a monoid under ×

All this jargon seems meaningless in the context of imperative programming but is relevant in the world of functional programming.

The monoid and semigroup abstractions are actually useful to provide as a constraint for the input. In haskell and scala its usually
done using typeclasses and constraints supplied in the type parameter.

// Scala
def combine[A: Monoid]
def sort[A: Ordering]

// haskell
qsort :: (Ord a) => [a] -> [a]

This might still seem arcane but these are other common monoids
1. Strings with concatenation, where "" is the 0 element.
2. text files with concatenation, where /dev/null can be considered the 0 element.
3. Lists of anything, where the empty list is the 0 element and list concat is the operation.
4. markdown files.

Segueing into markdown, I had a file in wikimedia format which needed to be moved into github markdown format, 
due to which I discovered this tool called pandoc - courtesy some llm chatting. Coincidentally pandoc is written
in haskell and there's a running joke that this is the only piece of useful software written in haskell.

pandoc helped me convert some really intricate sections into github markdown (although some tables gave it trouble
and it was likely that I did not supply the formats correctly).

The .md file in question [^2] was easier to edit and correct if it was in smaller chunks. So refactored the original
wikimedia file into a bunch of .md file into sections [^3] and added links to the section in [^2]. However I noticed
that browsing these files in github was a pain - you lose context when you navigate back and forth between links.
What was easy to write and edit was not easy to edit. So I decided to regenerate the original monolithic content
using pandoc. I created a list of files [^4] and then supplied the list of files as input to pandoc:

```
let files = cat list-of-files.txt | grep -v "#" | xargs // In nushell 
pandoc $files -o Eke.md
```

However I ran into a limit on the number of inputs on mac.

```
pandoc: .. openBinaryFile: invalid argument (File name too long)
```

One of the fixes for this:

```
cat list-of-files | xargs pandoc -o Eke.md
```

just works since the act of joining md files is an associative operation.

At the end, I have the single .md file which contains all the sections instead of having to navigate back and forth.
To see the differences, see [^2] and [^6] on your browser and scroll down.

References:

1. https://en.wikipedia.org/wiki/Natural_number
1. https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/Eke.md
1. https://github.com/vwulf/ettuge/tree/master/src/main/md/kannada/sections
1. https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/list_of_files.txt
1. https://github.com/vwulf/ettuge/blob/master/src/main/md/kannada/sections/pandoc_cmd.nu
1. https://github.com/vwulf/ettuge/blob/e2d17c832b90c29e076d3a56fc0626a82497b286/src/main/md/kannada/Eke.md   
