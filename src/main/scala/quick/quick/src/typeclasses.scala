package typeclasses
trait SemiGroup[A]:
  extension (x: A)
    def combine(y: A): A
trait Monoid[A] extends SemiGroup[A]:
  def unit: A
trait Functor[F[_]]:
  extension [A, B] (fa: F[A])
    def map(f: A => B): F[B]
trait SemiGroupF[F[_]]:
  extension [A] (x: F[A])
    def combineF(y: F[A]): F[A]
trait MonoidF[F[_]] extends SemiGroupF[F]:
  def unitF[A]: F[A]

trait Applicative[F[_]] extends Functor[F]:
  extension [A, B] (fa: F[A])
    def apply(f: F[A => B]): F[B]

trait Monad[F[_]] extends Applicative[F]:
  extension [A, B] (fa: F[A])
    def flatMap(f: A => F[B]): F[B]

trait Foldable[F[_]]:
  extension [A, B] (fa: F[A])
    def foldLeft(z: B)(f: (B, A) => B): B

trait Unfoldable[F[_]]:
  extension [A, B] (b: B)
    def unfold(f: B => Option[(A, B)]): F[A]

trait Paramorphism[P[_]]:
  def para[A, B](fa: P[A], b: B, f: (=> A, => P[A], B) => B): B

trait Traverse[F[_]] extends Functor[F] with Foldable[F]:
  extension [A, B] (fa: F[A])
    def traverse[G[_]: Applicative](f: A => G[B]): G[F[B]]  