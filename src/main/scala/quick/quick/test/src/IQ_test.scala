import datastructures._

import org.scalatest.funsuite.AnyFunSuite

class IQ_test extends AnyFunSuite {
    test("iq creation") {
        val q = IQ(1, 2, 3, 4, 5)
        assert(q.toList == List(1, 2, 3, 4, 5))
    }

    test("iq enqueue") {
        val q = IQ(1, 2, 3)
        val updatedQ = q.enqueue(4)
        assert(updatedQ.toList == List(1, 2, 3, 4))
    }

    test("iq dequeue") {
        val q = IQ(1, 2, 3, 4)
        val (dequeued, updatedQ) = q.dequeue
        assert(dequeued == 1)
        assert(updatedQ.toList == List(2, 3, 4))
    }

    test("iq isEmpty") {
        val emptyQ = IQ.empty[Int]
        assert(emptyQ.isEmpty)

        val nonEmptyQ = IQ(1)
        assert(!nonEmptyQ.isEmpty)
    }

    test("iq size") {
        val q = IQ(1, 2, 3, 4, 5)
        assert(q.size == 5)

        val emptyQ = IQ.empty[Int]
        assert(emptyQ.size == 0)
    }

    test("iq front") {
        val q = IQ(10, 20, 30)
        assert(q.front == 10)
    }

    test("iq back") {
        val q = IQ(10, 20, 30)
        assert(q.back == 30)
    }
}
