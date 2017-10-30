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


def test_dq_1_conftest(dq_1):
    """Test to validate dq_1 conftest is working."""
    assert dq_1._dll.head.data == 9


def test_append_left_head_is_new_node(dq_1):
    """Test to check if new node is data value associated with append_left arg."""
    dq_1.append_left('threve')
    assert dq_1._dll.head.data == 'threve'
