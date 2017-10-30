import pytest


@pytest.fixture
def dq():
    from deque import Deque
    return Deque()
