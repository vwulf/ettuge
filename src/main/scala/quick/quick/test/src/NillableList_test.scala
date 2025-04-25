package datastructures
import org.scalatest.funsuite.AnyFunSuite
import scala.annotation.tailrec
import typeclasses._

class NillableList_test extends AnyFunSuite {
  test("map") {
    val q = NillableList(1, 2, 3, 4, 5)
    val r = q.map(_ + 1)
    assertEquals(r, NillableList(2, 3, 4, 5, 6))
  }

  test("foldLeft") {
    val q = NillableList(1, 2, 3, 4, 5)
    val r = q.foldLeft(0)(_ + _)
    assertEquals(r, 15)
  }
}
  test("unfold") {
    val q = NillableList.unfold(0)(i => if (i < 5) S((i, i + 1)) else N)
    assertEquals(q, NillableList(0, 1, 2, 3, 4))
  }

  test("toList") {
    val q = NillableList(1, 2, 3, 4, 5)
    assertEquals(q.toList, List(1, 2, 3, 4, 5))
  }
}