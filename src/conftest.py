"""Fixtures for test_deque.py."""
import pytest


@pytest.fixture
def dq():
    """Create empty Deque class."""
    from deque import Deque
    return Deque()


@pytest.fixture
def dq_1():
    """Create and append with one value."""
    from deque import Deque
    dq = Deque()
    dq.append(9)
    return dq


@pytest.fixture
def dq_3():
    """Create and append with three values."""
    from deque import Deque
    dq = Deque()
    dq.append('snine')
    dq.append(4)
    dq.append('ragtime')
    return dq


@pytest.fixture
def heap():
    """Create instance of heap with empty list."""
    from binheap import Heap
    test_heap = Heap()
    return test_heap


@pytest.fixture
def heap_3():
    """Create instance of heap with empty list."""
    from binheap import Heap
    test_heap = Heap([5, 99, 74])
    return test_heap
