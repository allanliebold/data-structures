"""File implements a stack with push and pop methods."""
from linked_list import LinkedList


class Stack(object):
    """Stack class."""

    def __init__(self, iterable=()):
        """Init method for Stack."""
        self._linkedlist = LinkedList(iterable)
        self.head = self._linkedlist.head
        self._length = self._linkedlist._length
        print('stack created')

    def push(self, value):
        """Push method for Stack."""
        self._linkedlist.push(value)
        print('pushed')

    def pop(self):
        """Pop method for Stack."""
        self._linkedlist.pop()
