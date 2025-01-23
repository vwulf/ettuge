my-simple-project/
├── app/
│   └── Main.hs        # Entry point for the executable
├── src/
│   └── Lib.hs         # Library source code
├── test/
│   └── Spec.hs        # Test source code
├── package.yaml       # Project configuration
├── stack.yaml         # Stack configuration
└── README.md          # Optional README

cd ~/code/ettuge/src/main/haskell/quick/

Build and Run

Build the project:
stack build

Run the executable:
stack exec quick-exe

Run tests:
stack test

For doc, see:
<https://github.com/vwulf/ettuge/blob/master/src/main/md/haskell/qsortof.md>

Qsortof:

This Haskell file, qsortof.hs, contains several functions and data types focused on sorting and selection algorithms. Here's a summary of its contents:

    Imports and Pragmas:
        The file begins with language pragmas and imports necessary modules for its functionality.

    Sorting Algorithms:
        qsort: An implementation of the QuickSort algorithm.
        qsort1: A modified version of QuickSort that takes an additional parameter k and incorporates tracing for debugging.

    Utility Function:
        unless: A utility function using unfoldr to generate a list based on a condition and step function.

    Data Type H:
        Defines a data type H with fields for a list, count, min, max, weighted median, and sum.
        Instances for Semigroup, Monoid, Functor, Bifunctor, and Biapplicative are provided for H.

    Helper Functions:
        maybeOp, maybeOp', fromMaybeOp: Functions to operate on Maybe values.
        calcWmid: Calculates a weighted median.
        calcH: Updates an H value with a new element.
        pivotnk: Determines a pivot element based on a provided function.

    Selection Algorithm:
        qsel: A function to select the k-th smallest element from a list.
        accf: An accumulator function for selection.
        qsel': A helper function for qsel with debugging traces.

This file provides comprehensive implementations for sorting and selection along with utility functions and data structures to support these operations.

