"""Tests for Data Structures."""
from linked_list import Node, LinkedList
n = Node('test')
linked_list = LinkedList()


def test_node_attributes():
    """Test that node object has expected attributes."""
    assert n.value == 'test' and n.next is None


def test_list_push():
    """Test that linked_list has node pushed to it."""
    linked_list.push(1)
    assert linked_list.head.value == 1


def test_list_push_next():
    """Test push with second node.

    Head should be new node, next attribute should point to previous head.
    """
    linked_list.push('first')
    linked_list.push('second')
    assert linked_list.head.value == 'second' and linked_list.head.next.value == 'first'


def test_list_pop():
    """Test that pop returns the value of the deleted node."""
    linked_list.push('target')
    assert linked_list.pop() == 'target'


def test_list_search():
    """Test that search method returns the node with the value passed."""
    linked_list.push(1)
    linked_list.push('target')
    linked_list.push(3)
    assert linked_list.search('target').value == 'target'
