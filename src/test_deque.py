"""Tests for deque creation and functionality."""
import pytest


def test_deque_creation():
    """Test __init__ to ensure deque created with attrs."""
    from deque import Deque
    test_deque = Deque()
    assert test_deque._length == 0
