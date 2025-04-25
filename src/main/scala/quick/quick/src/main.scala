import datastructures._
import datastructures.{given typeclasses.MonoidF[List]}

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


