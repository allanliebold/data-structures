"""Implementation of Queue. First in, first out data structure."""
from dll import Dll


class Queue(object):
    """Create Queue Class object."""

    def __init__(self):
        """Queue initiliazation.

        Composed of Doubly-Linked List attributes and methods.
        """
        self._dll = Dll()
        self._length = self._dll._length
        self.head = self._dll.head
        self.tail = self._dll.tail

    @property
    def length(self):
        """Use dll length method to return size of list."""
        return self._dll._length

    def enqueue(self, data):
        """Add node to queue at head."""
        self._dll.push(data)

    def dequeue(self):
        """Remove node from queue at tail."""
        if self._dll._length == 0:
            raise IndexError('Queue empty')
        return self._dll.shift()

    def peek(self):
        """Display next value that will be removed if dequeued is called."""
        if self._dll._length == 0:
            return None
        return self._dll.tail.data

    def __len__(self):
        """Function overwrites built-in len function to show length."""
        return self.length

    def __str__(self):
        """Function uses built-in print function to display list as string."""
        return self.display()
