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
