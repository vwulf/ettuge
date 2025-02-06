package datastructures

enum Tree [+A]:
  case Leaf(a: A) extends Tree [A]
  case Branch(left : Tree[A], a: A, right : Tree[A]) extends Tree [A]

  def bfs =
    println("")

