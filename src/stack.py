"""File implements a stack with push and pop methods."""
from linked_list import LinkedList


class Stack(object):
    """Create Stack class object."""

    def __init__(self, iterable=()):
        """Init method for Stack.

        Stack is composed of LinkedList methods and attributes.
        """
        self._linkedlist = LinkedList(iterable)
        self.head = self._linkedlist.head
        self._length = self._linkedlist._length

    def push(self, data):
        """Push method for Stack. Adds node at head."""
        self._linkedlist.push(data)

    def pop(self):
        """Pop method for Stack. Removes node at head."""
        return self._linkedlist.pop()

    def __len__(self):
        """Function uses built-in len function to show length."""
        return self._length

    def __str__(self):
        """Function uses built-in print function to display list as string."""
        return self.display()
