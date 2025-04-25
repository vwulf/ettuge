package datastructures

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

