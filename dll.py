"""Implementation of doubly-linked list."""
from linked_list import LinkedList


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
        if self._length == 1:
            self.tail == new_head

        if self.head:
            self.head.prev = new_head
        self.head = new_head
        self.head.next = prev_head
        self._length += 1
        self.head.prev = None

    def pop(self):
        """Pop method for Dll."""
        if not self.head:
            raise IndexError('List empty')
        deleted_node = self._linkedlist.pop()
        self._length -= 1
        if not self.head.next:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return deleted_node
