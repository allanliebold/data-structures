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
