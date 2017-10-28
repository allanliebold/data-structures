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


def test_append():
    """Test append function to add to tail."""
    from dll import Dll
    test_dll = Dll()
    test_dll.append(9)
    assert test_dll.tail.data == 9


def test_append_two_nodes():
    """Test append function to add to tail."""
    from dll import Dll
    test_dll = Dll()
    test_dll.append(9)
    test_dll.append('goat')
    assert test_dll.tail.data == 'goat'


def test_shift():
    """Test shift function.

    Should remove last node and return value.
    """
    from dll import Dll
    test_dll = Dll()
    test_dll.append(8)
    assert test_dll.shift() == 8


def test_remove_returns_node():
    """Test that correct node returned from search."""
    from dll import Dll
    test_dll = Dll()
    test_dll.push(11)
    test_dll.push('target')
    check = test_dll.head
    test_dll.push(34)
    assert test_dll.remove('target') == check


def test_remove_to_ensure_node_no_longer_exists():
    """Test remove method to ensure node is gone once remove is called."""
    from dll import Dll
    test_dll = Dll()
    test_dll.push(11)
    test_dll.push('target')
    test_dll.push(34)
    test_dll.remove('target')
    with pytest.raises(ValueError):
        test_dll._linkedlist.search('target')


def test_remove_with_empty_list():
    """Test to ensure error raised if remove called on empty list."""
    from dll import Dll
    test_dll = Dll()
    with pytest.raises(IndexError):
        test_dll.remove('a thing')


def test_remove_head_of_list_with_multiple_nodes():
    """Test for remove method on list with multiple nodes."""
    from dll import Dll
    test_dll = Dll()
    test_dll.push(11)
    test_dll.push('target')
    check = test_dll.head
    assert test_dll.remove('target') == check


def test_remove_with_one_node():
    """Test remove if only one node."""
    from dll import Dll
    test_dll = Dll()
    test_dll.push('target')
    test_dll.remove('target')
    assert test_dll.head is None
