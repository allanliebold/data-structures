"""Implementation of doubly-linked list."""
from linked_list import LinkedList
from linked_list import Node


class Dll(object):
    """Doubly-Linked List Class."""

    def __init__(self):
        """List initialization."""
        self._linkedlist = LinkedList()
        self.head = None
        self._length = 0
        self.tail = None

    def push(self, data):
        """Push method for Dll."""
        prev_head = self.head
        new_head = self._linkedlist.push(data)
        if self._length != 0:
            self.head.prev = new_head
        self.head = new_head
        self.head.next = prev_head
        self._length += 1
        self.head.prev = None


class Dllnode(object):
    """Doubly-Linked Node Class."""

    def __init__(self, data):
        """Dll initialization."""
        self._node = Node(data)
        self.data = self._node.data
        self.next = self._node.next
        self.prev = None
