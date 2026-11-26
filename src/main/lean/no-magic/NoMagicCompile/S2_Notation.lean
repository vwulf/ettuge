import NoMagic

/-!
# Stage 2 — Notation removed

`2 * sumTo n` is shorthand. Turning off notation shows the function calls.
-/

open NoMagic

set_option pp.notation false in
#check two_mul_sumTo

/-!
Turning on explicit arguments as well shows everything the elaborator filled
in: the type `Nat` at every position, the multiplication and addition
instances, and the numerals, each an `OfNat.ofNat` around a raw literal.
-/

set_option pp.notation false in
set_option pp.explicit true in
#check two_mul_sumTo
