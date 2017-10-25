"""Tests for Stack Class."""
import pytest


def test_stack_init_empty():
    """Tests initialization of Stack with no values passed."""
    from stack import Stack
    test_stack = Stack()
    assert test_stack._length == 0


def test_stack_init_with_value():
    """."""
    from stack import Stack
    test_stack = Stack(1)
    assert test_stack.head.value == 1
