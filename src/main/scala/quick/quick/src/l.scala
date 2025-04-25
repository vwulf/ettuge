package datastructures
import typeclasses._

given MonoidF[List] with
  def unitF[A]: List[A] = Nil
  extension [A] (l: List[A])
    def combineF(y: List[A]): List[A] = l ::: y

extension [F[_]:MonoidF, A] (l: F[A])
    infix def ?:: (inp: List[F[A]]): List[F[A]] =
      val mf = summon[MonoidF[F]]
      if l == mf.unitF[F[A]] then inp else l :: inp
 
