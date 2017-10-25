"""Implementation of doubly-linked list."""
from linked_list import LinkedList
from linked_list import Node


class Dll(object):
    """Doubly-Linked List Class."""

    def __init__(self):
        """List initialization."""
        self._linkedlist = LinkedList()
        self.head = self._linkedlist.head
        self._length = self._linkedlist._length
        self.tail = None


class Dll_Node(object):
    """Doubly-Linked Node Class."""

    def __init__(self, data):
        self._node = Node(data)
        self.data = self._node.data
        self.next = self._node.next
        self.prev = None

