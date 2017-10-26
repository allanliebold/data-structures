"""Tests for doubly-linked list."""
import pytest


def test_dll_attr():
    """Test if Dll object is created."""
    from dll import Dll
    test_dll = Dll()
    assert test_dll._length == 0


def test_dll_push_one():
    """Test pushing to an empty list."""
    from dll import Dll
    test_dll = Dll()
    test_dll.push(1)
    assert test_dll.head.data == 1


def test_dll_head_push_two():
    """Test list with two nodes.

    Head should point to next node.
    """
    from dll import Dll
    test_dll = Dll()
    test_dll.push(1)
    test_dll.push(2)
    assert test_dll.head.next.data == 1


def test_dll_next_push_two():
    """Test list with two nodes.

    Second node should point back to head.
    """
    from dll import Dll
    test_dll = Dll()
    test_dll.push(1)
    test_dll.push(2)
    assert test_dll.head.next.prev.data == 2


def test_pop():
    """Test pop function.

    Should remove first node and return value.
    """
    from dll import Dll
    test_dll = Dll()
    test_dll.push(1)
    assert test_dll.pop() == 1
