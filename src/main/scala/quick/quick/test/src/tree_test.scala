// Add test cases for tree
import datastructures._
import org.scalatest.funsuite.AnyFunSuite
import org.scalatest.matchers.should.Matchers
import org.scalatest.prop.TableDrivenPropertyChecks


class TreeTest extends AnyFunSuite with Matchers {

  test("Tree creation and traversal") {
    val tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
    tree.preOrder shouldEqual List(1, 2, 3, 4, 5)
    tree.inOrder shouldEqual List(2, 1, 4, 3, 5)
    tree.postOrder shouldEqual List(2, 4, 5, 3, 1)
  }

  test("Tree height") {
    val tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
    tree.height shouldEqual 3
  }

}
