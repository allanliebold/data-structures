"""Implementation of deque, or double-ended queue."""
from dll import Dll
from linked_list import Node


class Deque(object):
    """Create deque class object."""

    def __init__(self):
        """Initialize new deque class object with a front and back."""
        self._dll = Dll()
        self.head = self._dll.head
        self.tail = self._dll.tail
        self._length = self._dll._length

    @property
    def length(self):
        """Use dll length method to return size of the deque."""
        return self._dll._length

    def append(self, data):
        """Use dll append method to add node with data at tail."""
        self._dll.append(data)

    def append_left(self, data):
        """Use dll push method to add node with data at front(head)."""
        self._dll.push(data)

    def pop(self):
        """Use dll shift method to remove node at back(tail)."""
        return self._dll.shift()

    def pop_left(self):
        """Use dll pop method to remove node from front(head)."""
        return self._dll.pop()

    def peek(self):
        """Use dll peek method to view node at back(tail)."""
        if self.length == 0:
            return None
        return self._dll.tail.data

    def peek_left(self):
        """Use dll peek method to view node at front(head)."""
        if self.length == 0:
            return None
        return self._dll.head.data
