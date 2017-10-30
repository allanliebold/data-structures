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
    """Test if new node is data value associated with append_left arg."""
    dq_1.append_left('threve')
    assert dq_1._dll.head.data == 'threve'


def test_append_left_adds_to_length(dq_3):
    """Test length is correct after append left to list with three nodes."""
    dq_3.append_left('trex')
    assert dq_3.length == 4


def test_pop_returns_value_of_tail(dq_3):
    """Test that the correct value is returned with pop function."""
    assert dq_3.pop() == 'ragtime'


def test_pop_empty_list():
    """Test that pop on empty list raises IndexError."""
    from deque import Deque
    dq = Deque()
    with pytest.raises(IndexError):
        dq.pop()


def test_deque_length_after_pop(dq_3):
    """Test that length is correct after pop function."""
    dq_3.pop()
    assert dq_3.length == 2
