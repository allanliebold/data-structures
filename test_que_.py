"""Tests for queue data structure."""
import pytest


def test_queue_init():
    """Test if queue object is created."""
    from que_ import Queue
    test_q = Queue()
    assert test_q._length == 0


def test_queue_enqueue_node():
    """Test if able to enqueue a node."""
    from que_ import Queue
    test_q = Queue()
    test_q.enqueue(8)
    assert test_q._dll.head.data == 8


def test_queue_enqueue_two_nodes():
    """Test if able to enqueue two nodes."""
    from que_ import Queue
    test_q = Queue()
    test_q.enqueue(7)
    test_q.enqueue(8)
    assert test_q._dll.tail.data == 7


def test_dequeue_node():
    """Test if able to dequeue a node."""
    from que_ import Queue
    test_q = Queue()
    test_q.enqueue(9)
    test_q.enqueue(10)
    assert test_q.dequeue() == 9


def test_dequeue_node_length():
    """Test if able to dequeue a node."""
    from que_ import Queue
    test_q = Queue()
    test_q.enqueue(9)
    test_q.enqueue(10)
    test_q.dequeue()
    assert test_q.length == 1
