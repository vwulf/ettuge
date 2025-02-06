package datastructures
sealed case class IS[A]
  (private val list: List[A]):
  
  def push(a: A): IS[A] =
    new IS[A](a :: list)

  def pop: (Option[A], IS[A]) =
    list match
      case Nil => (None, this) 
      case x :: xs => (Some(x), new IS(xs))
   
  def isEmpty: Boolean = list.isEmpty

  def size: Int = list.size

  override def toString(): String = 
    toList.mkString(" ")

  private def toList: List[A] = list

object IS:
  def apply[A](xs: A*): IS[A] = new IS[A](xs.toList)
  def empty[A] = new IS[A](Nil)
  import typeclasses.Foldable

  private def map_int[A, B](s: IS[A])(f:A => B): IS[B] =
    def fb(sb: IS[B], a: A): IS[B] =
      sb.push(f(a))
    val FO: Foldable[IS] = summon[Foldable[IS]]
    val isb1 = FO.foldLeft(s)(IS.empty)(fb)
    new IS(isb1.list)

  private def apply_int[A, B](s: IS[A])(f: IS[A => B]): IS[B] =
    def fb(isb: IS[B], a: A): IS[B] =
      val sb:IS[B] = f.map(g => g(a))
      sb.foldLeft(isb)((isb, b) => isb.push(b))
    val FO: Foldable[IS] = summon[Foldable[IS]]
    FO.foldLeft(s)(IS.empty[B])(fb)

  private def combineF_int[A](s:IS[A])(y: IS[A]): IS[A] = 
    new IS[A](y.list ++ s.list)

  given Foldable[IS] with
    extension [A, B](s: IS[A])
      def foldLeft(z: B)(f: (B, A) => B): B =
        s.list.foldLeft(z)(f)

  import typeclasses.SemiGroupF
  given SemiGroupF[IS] with
    extension [A] (s: IS[A])
      def combineF(y: IS[A]): IS[A] = combineF_int[A](s)(y)

  import typeclasses.MonoidF

  extension [F[_]:MonoidF, A] (inp: IS[F[A]])
    def pushNE(l: F[A]): IS[F[A]] =
      val mf = summon[MonoidF[F]]
      if l == mf.unitF[F[A]] then inp else inp.push(l)
       
  given MonoidF[IS] with
    def unitF[A]: IS[A] = IS.empty[A]
    extension [A] (s:IS[A])
      def combineF(y: IS[A]): IS[A] = combineF_int[A](s)(y) 

  import typeclasses.Functor
  given Functor[IS] with
    extension [A, B](s: IS[A])
      def map(f: A => B): IS[B] = map_int(s)(f)
  
  import typeclasses.Applicative
  given Applicative[IS] with
    extension [A, B](s: IS[A])
      def map(f: A => B): IS[B] = map_int(s)(f)
    extension [A, B](s: IS[A])
      def apply(f: IS[A => B]): IS[B] = apply_int(s)(f)

  import typeclasses.Monad
  given Monad[IS] with
    extension [A, B](s: IS[A])
      def flatMap(f: A => IS[B]): IS[B] =
        def fb(isb: IS[B], a: A): IS[B] =
          val fb:IS[B] = f(a)
          fb.foldLeft(isb)((isb, b) => isb.push(b))
        val FO: Foldable[IS] = summon[Foldable[IS]]
        FO.foldLeft(s)(IS.empty[B])(fb)
    extension [A, B](s: IS[A])
      def map(f: A => B): IS[B] = map_int(s)(f)
    extension [A, B](s: IS[A])
      def apply(f: IS[A => B]): IS[B] = apply_int(s)(f)