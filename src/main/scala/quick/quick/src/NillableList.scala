package datastructures

import scala.annotation.tailrec
import typeclasses._

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


