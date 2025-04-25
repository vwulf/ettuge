package datastructures
sealed case class IQ[A]
  (private val front: List[A],
   private val back: List[A]):
  
  def enqueue(b: A): IQ[A] = new IQ[A](front, b::back)
  
  def dequeue: (Option[A], IQ[A]) =
    front match
      case Nil => back.reverse match
        case x::xs => (Some(x), new IQ[A](xs, Nil)) 
        case Nil => (None, IQ.empty[A])
      case x::xs => (Some(x), new IQ[A](xs, back))
   
  def isEmpty: Boolean = front.isEmpty && back.isEmpty

  def para[B](z: B)
             (f: (B, A) => B) : (B, List[IQ[A]]) =
    def loop(acc: B, q1: IQ[A],
             lq: List[IQ[A]]): (B, List[IQ[A]]) =
      if q1.isEmpty then (acc, lq)
      else
        val (x, q2) = q1.dequeue
        loop(f(acc, x.get), q2, lq :+ q1)
    loop(z, this, List())

  override def toString(): String = 
    toList.mkString(" ")

  private def toList: List[A] = front ::: back.reverse

object IQ:
  def apply[A](xs: A*): IQ[A] = new IQ[A](xs.toList, Nil)
  def empty[A] = new IQ[A](Nil, Nil)
  import typeclasses.Foldable
  
  private def map_int[A, B](q: IQ[A])(f:A => B): IQ[B] =
    def fb(iqb: IQ[B], a: A): IQ[B] =
      iqb.enqueue(f(a))
    val FO: Foldable[IQ] = summon[Foldable[IQ]]
    FO.foldLeft(q)(IQ.empty)(fb)

  private def apply_int[A, B](q: IQ[A])(f: IQ[A => B]): IQ[B] =
    def fb(iqb: IQ[B], a: A): IQ[B] =
      val ib:IQ[B] = f.map(g => g(a))
      ib.foldLeft(iqb)((iqb, b) => iqb.enqueue(b))
    val FO: Foldable[IQ] = summon[Foldable[IQ]]
    FO.foldLeft(q)(IQ.empty[B])(fb)

  private def combineF_int[A](q:IQ[A])(y: IQ[A]): IQ[A] = 
    val FO: Foldable[IQ] = summon[Foldable[IQ]]
    FO.foldLeft(y)(q)((iq, i) => iq.enqueue(i))
  given Foldable[IQ] with
    extension [A, B](q: IQ[A])
      def foldLeft(z: B)(f: (B, A) => B): B = 
        @annotation.tailrec
        def loop(acc: B, q: IQ[A]): B = 
          if q.isEmpty then acc
          else
            val (x, q1) = q.dequeue
            loop(f(acc, x.get), q1)
        loop(z, q)

  import typeclasses.SemiGroupF
  given SemiGroupF[IQ] with
    extension [A] (q: IQ[A])
      def combineF(y: IQ[A]): IQ[A] = combineF_int[A](q)(y)
      
  import typeclasses.MonoidF


  extension [F[_]:MonoidF, A] (inp: IQ[F[A]])
    def enqueueNE(l: F[A]): IQ[F[A]] =
      val mf = summon[MonoidF[F]]
      if l == mf.unitF[F[A]] then inp else inp.enqueue(l)
  given MonoidF[IQ] with
    def unitF[A]: IQ[A] = IQ.empty[A]
    extension [A] (q:IQ[A])
      def combineF(y: IQ[A]): IQ[A] = combineF_int[A](q)(y) 

  import typeclasses.Functor
  given Functor[IQ] with
    extension [A, B](q: IQ[A])
      def map(f: A => B): IQ[B] = map_int(q)(f)
  
  import typeclasses.Applicative
  given Applicative[IQ] with
    extension [A, B](q: IQ[A])
      def map(f: A => B): IQ[B] = map_int(q)(f)
    extension [A, B](q: IQ[A])
      def apply(f: IQ[A => B]): IQ[B] = apply_int(q)(f)

  import typeclasses.Monad
  given Monad[IQ] with
    extension [A, B](q: IQ[A])
      def flatMap(f: A => IQ[B]): IQ[B] =
        def fb(iqb: IQ[B], a: A): IQ[B] =
          val fb:IQ[B] = f(a)
          fb.foldLeft(iqb)((iqb, b) => iqb.enqueue(b))
        val FO: Foldable[IQ] = summon[Foldable[IQ]]
        FO.foldLeft(q)(IQ.empty[B])(fb)
    extension [A, B](q: IQ[A])
      def map(f: A => B): IQ[B] = map_int(q)(f)
    extension [A, B](q: IQ[A])
      def apply(f: IQ[A => B]): IQ[B] = apply_int(q)(f)
  
/*  
  import typeclasses.Paramorphism

  given Paramorphism[IQ] with
    def para[A, B](fa: IQ[A], b: B, f: (=> A, => IQ[A], B) => B): B =
      fa.para(b)(f)._1
      */