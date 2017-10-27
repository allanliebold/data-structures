"""Implementation of Queue."""
from dll import Dll


class Queue(object):
    """Queue Class."""

    def __init__(self):
        """Queue initiliazation."""
        self._dll = Dll()
        self._length = self._dll._length
        self.head = self._dll.head
        self.tail = self._dll.tail

    @property
    def length(self):
        """."""
        return self._dll._length

    def enqueue(self, data):
        """Add node to queue."""
        self._dll.push(data)

    def dequeue(self):
        """Remove node from queue."""
        return self._dll.shift()
