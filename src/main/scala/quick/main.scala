import datastructures._
import scala.math.Numeric.Implicits.infixNumericOps
import datastructures.{given typeclasses.MonoidF[List]}
import scala.math.Ordering.Implicits.infixOrderingOps
import scala.math.Numeric.Implicits.infixNumericOps
import scala.collection.mutable.ArrayBuffer

def qsort_naive_rec_imm_list[A: Ordering]
  (xs: List[A]): List[A] =
  if xs.isEmpty then Nil
  else
    val pivot = xs.head
    val (less, greater) = xs.tail.partition(_ < pivot)
    qsort_naive_rec_imm_list(less) :::
       pivot ::
         qsort_naive_rec_imm_list(greater)

def qsort_tail_rec_imm_list[A: Ordering]
  (xs: List[A]): List[A] =
  @annotation.tailrec
  def qsort_tail_rec(
    inp:List[List[A]],
    op: List[A]): List[A] =
    if inp.isEmpty then
      op.reverse
    else
      val (ninp, nop) = inp.foldLeft
        (List.empty[List[A]], op)
        ((acc, l) =>
          val (ninp, nop) = acc
          val pivot = l.head
          if (l.size == 1) then
            if (ninp.isEmpty)
              (ninp, pivot :: nop)
            else
              (List(pivot) :: ninp, nop)
          else
            val (lesser, greater) =
               l.tail.partition(_ < pivot)
            (greater ?:: List(pivot) ?:: lesser ?:: ninp,
             nop)
        )
      qsort_tail_rec(ninp.reverse, nop)
    end if
  qsort_tail_rec(List(xs), Nil)

def qsort_imperative_imm_stack[A: Ordering]
  (xs: List[A]): List[A] =
  def qsort_imp(in:IS[List[A]]): List[A] =
    var inp:IS[List[A]] = in
    val op: scala.collection.mutable.ListBuffer[A] =
       scala.collection.mutable.ListBuffer.empty[A]
    while !inp.isEmpty do
      val (ol, ninp) = inp.pop
      inp = ninp
      val l = ol.get
      val pivot = l.head
      if (l.size == 1) then
        op.prepend(pivot)
      else
        val (lesser, greater) =
          l.tail.partition(_ < pivot)
        inp = inp.
                pushNE(lesser).
                pushNE(List(pivot)).
                pushNE(greater)
    end while
    op.toList
  qsort_imp(IS[List[A]](xs))


def qsort_tail_rec_imm_q[A: Ordering]
  (xs: List[A]): List[A] =
  @annotation.tailrec
  def qsort_tail_rec(
    inp:IQ[List[A]], op: List[A]): List[A] =
    if inp.isEmpty then
      op.reverse
    else
      val (ninp, nop) = inp.foldLeft
        (IQ.empty[List[A]], op)
        ((acc, l) =>
          val (ninp, nop) = acc
          val pivot = l.head
          if (l.size == 1) then
            if (ninp.isEmpty)
              (ninp, pivot :: nop)
            else
              (ninp.enqueue(List(pivot)), nop)
          else
            val (lesser, greater) =
              l.tail.partition(_ < pivot)
            (IQ.empty[List[A]].
              enqueueNE(lesser).
              enqueueNE(List(pivot)).
              enqueueNE(greater).
              combineF(ninp),
             nop)
        )
      qsort_tail_rec(ninp, nop)
    end if
  qsort_tail_rec(IQ(xs), Nil)

def qsort_imperative_imm_q[A: Ordering]
  (xs: List[A]): List[A] =
  def qsort_imp(in:List[A]): List[A] =
    var inp:IQ[List[A]] = IQ[List[A]](in)
    val op: scala.collection.mutable.ListBuffer[A] =
       scala.collection.mutable.ListBuffer.empty[A]
    while !inp.isEmpty do
      val (ol, ninp) = inp.dequeue
      val l = ol.get
      val pivot = l.head
      inp =
        if (l.size == 1) then
          op.append(pivot)
          ninp
        else
          val (lesser, greater) =
            l.tail.partition(_ < pivot)
          IQ.empty[List[A]].
               enqueueNE(lesser).
               enqueueNE(List(pivot)).
               enqueueNE(greater).
               combineF(ninp)
    end while
    op.toList
  qsort_imp(xs)

def  qsort_imperative_mut_array[A: Ordering]
  (xs: List[A]): List[A] =
  import util.control.Breaks._
  def partition(arr: ArrayBuffer[A], l: Int, r: Int): Int =
    val pivot = arr(l)
    var i = l
    var j = r
    breakable {
      while true do
        while arr(i) < pivot do
          i = i + 1
        while arr(j) > pivot do
          j = j - 1
        println(s"l: $l, r: $r, pivot: $pivot, i: $i, j: $j")
        if i >= j then
          break()
        //swap arr(i) and arr(j)
        val t = arr(j)
        arr(j) = arr(i)
        arr(i) = t
        //continue
        i = i + 1
        j = j - 1
      end while
    }
    println(s"arr: ${arr.toList} ")
    j
  end partition

  def qsort_imp(in:List[A]): List[A] =
    var st: IS[(Int, Int)] = IS((0, in.size))
    val inp = scala.collection.mutable.ArrayBuffer[A](in*)
    breakable {
      while !st.isEmpty do
        val (ind, nst) = st.pop
        st = nst
        val (l,r) = ind.get
        val pivot = inp(l)
        val c = partition(inp, l, r-1)
        println(s"pivot: $pivot, c: $c")
        if l < c && c < r then
          st = st.push((l, c))
        if c < r && c >= l then
          st = st.push((c+1, r))
        print(s"inp: ${inp.toList} st: $st")
      end while
    }
    inp.toList
  end qsort_imp  
  qsort_imp(xs)
@main def testIQ =
  val q = IQ(1, 2, 3, 4, 5)
  println(q.dequeue)
  println(q.foldLeft("")(
    (acc, x) => acc + x.toString + " ")) // "1 2 3 4 5 "
  println(q.dequeue) // Original q is not changed
  println(q.para(List.empty[Int])
            ((acc, x) => acc :+ x))

  val q1 = IQ.empty[Int]
  println(q.dequeue) // Empty queue returns None


