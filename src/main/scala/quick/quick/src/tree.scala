package datastructures

import scala.annotation.tailrec
import typeclasses._

// Split the code into 1 file per data structure

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
type RFBTree[+A] = RootedFullBinaryTree[A]

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
type RFFBTree[+A] = RootedFullFreeBinaryTree[A]

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

type RTree[+A] = RoseTree[A]
