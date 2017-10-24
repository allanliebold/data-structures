"""Tests for Data Structures."""
import pytest
from linked_list import Node, LinkedList
n = Node('test')
n2 = Node(2)
n3 = Node(4)
linked_list = LinkedList()


def test_node_attributes():
    """Test that node object has expected attributes."""
    assert n.value == 'test' and n.next is None


def test_list_push():
    """Test that linked_list has node pushed to it."""
    linked_list.push(n)
    assert linked_list.head.value == n.value


def test_list_push_next():
    """Test that pushing a second node changes head and creates link to next node."""
    linked_list.push(n)
    linked_list.push(n2)
    assert linked_list.head.value == 2 and linked_list.head.next.value == 'test'


def test_list_pop():
    """Test that pop returns the value of the deleted node."""
    linked_list.push(n)
    assert linked_list.pop() == n.value
