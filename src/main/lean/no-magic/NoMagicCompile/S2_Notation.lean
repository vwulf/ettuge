import NoMagic

/-!
# Stage 2 — Notation removed

`2 * sumTo n` is shorthand. Turning off notation shows the function calls;
turning on explicit arguments shows what the elaborator filled in: the
types, the multiplication instance, and the numeral instance.
-/

open NoMagic

/-- info: NoMagic.two_mul_sumTo (n : Nat) : Eq (HMul.hMul 2 (sumTo n)) (HMul.hMul n (HAdd.hAdd n 1)) -/
#guard_msgs in
set_option pp.notation false in
#check two_mul_sumTo

/--
info: NoMagic.two_mul_sumTo (n : Nat) :
  @Eq Nat
    (@HMul.hMul Nat Nat Nat (@instHMul Nat instMulNat) (@OfNat.ofNat Nat (nat_lit 2) (instOfNatNat (nat_lit 2)))
      (sumTo n))
    (@HMul.hMul Nat Nat Nat (@instHMul Nat instMulNat) n
      (@HAdd.hAdd Nat Nat Nat (@instHAdd Nat instAddNat) n (@OfNat.ofNat Nat (nat_lit 1) (instOfNatNat (nat_lit 1)))))
-/
#guard_msgs in
set_option pp.notation false in
set_option pp.explicit true in
#check two_mul_sumTo
