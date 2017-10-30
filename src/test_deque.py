"""Tests for deque creation and functionality."""
import pytest


def test_deque_creation(dq):
    """Test __init__ to ensure deque created with attrs."""
    assert dq._length == 0


def test_deque_append_one_node(dq):
    """Test that append function adds node with passed data."""
    dq.append(4)
    assert dq._dll.head.data == 4


def test_deque_append_one_head_is_tail(dq):
    """Test that the first node appended is the head and the tail."""
    dq.append(8)
    assert dq._dll.head == dq._dll.tail
