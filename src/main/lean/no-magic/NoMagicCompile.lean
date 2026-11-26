-- Companion to "No Magic": the article's proof taken apart, one stage per file,
-- from surface syntax down to the kernel. Every stage pins Lean's actual output
-- with `#guard_msgs`, so `lake build` fails if any of it changes.
import NoMagicCompile.S1_Surface
import NoMagicCompile.S2_Notation
import NoMagicCompile.S3_Tactics
import NoMagicCompile.S4_Recursion
import NoMagicCompile.S5_Primitives
import NoMagicCompile.S6_CurryHoward
import NoMagicCompile.S7_Computation
import NoMagicCompile.S8_Kernel
import NoMagicCompile.S9_Checkers
