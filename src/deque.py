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
