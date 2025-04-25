package datastructures

import scala.annotation.tailrec
import typeclasses._

// Split the code into 1 file per data structure

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

