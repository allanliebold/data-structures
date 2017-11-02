"""Tests for singly-linked list."""
import pytest


def test_node_attributes():
    """Test that node object has expected attributes."""
    from linked_list import Node
    n = Node('test')
    assert n.data == 'test' and n.next_node is None


def test_list_push():
    """Test that linked_list has node pushed to it."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(1)
    assert linked_list.head.data == 1


def test_list_push_next():
    """Test push with second node.

    Head should be new node, next attribute should point to previous head.
    """
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push('first')
    linked_list.push('second')
    assert linked_list.head.data == 'second' and \
        linked_list.head.next_node.data == 'first'


def test_list_push_iterable():
    """Test that all data is in list when passed as an iterable."""
    from linked_list import LinkedList
    datas = [1, 2, 3, 4, 5]
    linked_list = LinkedList(datas)
    for i in datas:
        assert linked_list.search(i).data == i


def test_list_pop():
    """Test that pop returns the data of the deleted node."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(5)
    assert linked_list.pop() == 5


def test_list_pop_empty():
    """Test pop called on an empty linked list. Should raise IndexError."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    with pytest.raises(IndexError):
        linked_list.pop()


def test_list_search():
    """Test that search method returns the node with the data passed."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push('target')
    linked_list.push(3)
    assert linked_list.search('target').data == 'target'


def test_list_search_invalid():
    """Test that search for node not in list raises dataError."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    with pytest.raises(ValueError):
        linked_list.search('target')


def test_list_size():
    """Test that size method returns correct number."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    for i in range(10):
        linked_list.push(i)
    assert linked_list.size() == 10


def test_string_not_iterated_upon_init():
    """Test that strings passed on init are not split."""
    from linked_list import LinkedList
    linked_list = LinkedList('68')
    assert linked_list.head.data == '68'


def test_remove_node():
    """Test that remove returns the target node."""
    from linked_list import LinkedList
    linked_list = LinkedList([2, 3, 4])
    target = linked_list.head.next_node
    assert linked_list.remove(linked_list.head.next_node) == target


def test_remove_node_list_contents():
    """Test contents of list after removing a node."""
    from linked_list import LinkedList
    linked_list = LinkedList([2, 3, 4])
    linked_list.remove(linked_list.head.next_node)
    assert linked_list.display() == '(4, 2)'


def test_remove_nonexistent_node():
    """Test that calling remove with node not in list raises ValueError."""
    from linked_list import LinkedList, Node
    linked_list = LinkedList([2, 3, 4])
    target = Node('5')
    with pytest.raises(ValueError):
        linked_list.remove(target)


def test_remove_empty_list():
    """Test that calling remove on empty list raises IndexError."""
    from linked_list import LinkedList, Node
    linked_list = LinkedList()
    target = Node('5')
    with pytest.raises(IndexError):
        linked_list.remove(target)
