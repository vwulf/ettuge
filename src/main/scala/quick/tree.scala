package datastructures

import scala.annotation.tailrec
import typeclasses._

enum O[+A]:
  case N extends O[Nothing]
  case S(a: A) extends O[A]

object O:
  def map[A, B](f: A => B)(oa: O[A]): O[B] = oa match
    case O.N => O.N
    case O.S(a) => O.S(f(a))

  def foldLeft[A, B](oa: O[A])(z: B)(f: (B, A) => B): B = oa match
    case O.N => z
    case O.S(a) => f(z, a)
given Functor[O] with
  extension [A, B] (fa: O[A])
    def map(f: A => B): O[B] = O.map(f)(fa)

given Foldable[O] with
  extension [A, B] (fa: O[A])
    def foldLeft(z: B)(f: (B, A) => B): B = O.foldLeft(fa)(z)(f)

enum E[+A, +B]:
  case L(a: A) extends E[A, Nothing]
  case R(b: B) extends E[Nothing, B]

infix type \/[+A, +B] = E[A, B]

object E:
  def bimap[A, B, C, D](f: A => C, g: B => D)(e: A \/ B): C \/ D = e match
    case L(a) => L(f(a))
    case R(b) => R(g(b))

  def foldLeft[A, B, C](e: A \/ B)(z: C)(f: (C, A) => C, g: (C, B) => C): C = e match
    case L(a) => f(z, a)
    case R(b) => g(z, b)
  
  def unfold[A, B](a: A)(f: A => O[B]): A \/ B =
    import O.{N, S}
    f(a) match
      case N => L(a)
      case S(b) => R(b)

type LE[+A] = E[A, Any]
given Functor[LE] with
  extension [A, C] (fa: LE[A])
    def map(f: A => C): LE[C] = fa match
      case E.L(a) => E.L(f(a))
      case E.R(b) => E.R(b)

type RE[+B] = E[Any, B]
given Functor[RE] with
  extension [B, D] (fa: RE[B])
    def map(f: B => D): RE[D] = fa match
      case E.L(a) => E.L(a)
      case E.R(b) => E.R(f(b))

enum NillableList[+A]:
  case Nil extends NillableList[Nothing]
  case Cons(head: A, tail: NillableList[A]) extends NillableList[A]
  def unfold[A, B](b: B)(f: B => O[(A, B)]): NillableList[A] =
    import O.{N, S}
    f(b) match
      case N => Nil
      case S((a, b)) => Cons(a, unfold(b)(f))
type NList[+A] = NillableList[A]

given Functor[NillableList] with
  extension [A, B] (fa: NillableList[A])
    def map(f: A => B): NillableList[B] = fa match
      case NillableList.Nil => NillableList.Nil
      case NillableList.Cons(a, as) => NillableList.Cons(f(a), as.map(f))

enum NonEmptyList[+A]:
  case Single(a: A) extends NonEmptyList[A]
  case Concat(head: A, tail: NonEmptyList[A]) extends NonEmptyList[A]
type NEList[+A] = NonEmptyList[A]

object NonEmptyList:
  def unfold[A, B](b: B)(f: B => A \/ (A, B)): NonEmptyList[A] =
    import E.{L, R}
    f(b) match
      case L(a) => Single(a)
      case R((a, b)) => Concat(a, unfold(b)(f))
  
  def map[A, B](f: A => B)(fa: NonEmptyList[A]): NonEmptyList[B] =
    @tailrec
    def map_int[A, B](f: A => B)(fa: NonEmptyList[A], fb: NonEmptyList[B]): NonEmptyList[B] =
      fa match
        case NonEmptyList.Single(a) => NonEmptyList.Concat(f(a), fb)
        case NonEmptyList.Concat(a, as) =>
          val b = f(a)
          val nelb = NonEmptyList.Concat(b, fb)
          map_int(f)(as, nelb)
    fa match
      case NonEmptyList.Single(a) => NonEmptyList.Single(f(a))
      case NonEmptyList.Concat(a, as) =>
        val b = f(a)
        val nelb = NonEmptyList.Single(b)
        map_int(f)(as, nelb)
  
given Functor[NonEmptyList] with
 extension [A, B] (fa: NonEmptyList[A])
  def map(f: A => B): NonEmptyList[B] = NonEmptyList.map(f)(fa)

enum RootedFullBinaryTree [+A]:
  case Leaf(a: A) extends RootedFullBinaryTree [A]
  case Branch(left : RootedFullBinaryTree[A],
              a: A,
              right : RootedFullBinaryTree[A]) extends RootedFullBinaryTree[A]
  def unfold[A, B](b: B)(f: B => A \/ (B, A, B)): RootedFullBinaryTree[A] =
    import E.{L, R}
    f(b) match
      case L(a) => Leaf(a)
      case R((b1, a, b2)) => Branch(unfold(b1)(f), a, unfold(b2)(f))
type RFBTree = RootedFullBinaryTree

given Functor[RootedFullBinaryTree] with
  extension [A, B] (fa: RootedFullBinaryTree[A])
    def map(f: A => B): RootedFullBinaryTree[B] = fa match
      case RootedFullBinaryTree.Leaf(a) => RootedFullBinaryTree.Leaf(f(a))
      case RootedFullBinaryTree.Branch(left, a, right) =>
        RootedFullBinaryTree.Branch(left.map(f), f(a), right.map(f))

enum RootedFullFreeBinaryTree [+A]:
  case Leaf(a: A) extends RootedFullFreeBinaryTree [A]
  case Branch(left : RootedFullFreeBinaryTree[A],
              right : RootedFullFreeBinaryTree[A]) extends RootedFullFreeBinaryTree[A]
  def unfold[A, B](b: B)(f: B => A \/ (B, B)): RootedFullFreeBinaryTree[A] =
    import E.{L, R}
    f(b) match
      case L(a) => Leaf(a)
      case R((b1, b2)) => Branch(unfold(b1)(f), unfold(b2)(f))
type RFFBTree = RootedFullFreeBinaryTree

given Functor[RootedFullFreeBinaryTree] with
  extension [A, B] (fa: RootedFullFreeBinaryTree[A])
    def map(f: A => B): RootedFullFreeBinaryTree[B] = fa match
      case RootedFullFreeBinaryTree.Leaf(a) => RootedFullFreeBinaryTree.Leaf(f(a))
      case RootedFullFreeBinaryTree.Branch(left, right) =>
        RootedFullFreeBinaryTree.Branch(left.map(f), right.map(f))

enum RoseTree[+A]:
  case Leaf(a: A) extends RoseTree[A]
  case Branch(a: A, children: NonEmptyList[RoseTree[A]]) extends RoseTree[A]

  def unfold[A, B](b: B)(f: B => A \/ (A, NEList[B])): RoseTree[A] =
    import E.{L, R}
    f(b) match
      case L(a) => Leaf(a)
      case R((a, bs)) => Branch(a, bs.map(b => unfold(b)(f)))

type RTree = RoseTree
