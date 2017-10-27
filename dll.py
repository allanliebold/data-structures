"""Implementation of Doubly-Linked list."""
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

    def push(self, data):
        """Push method for Dll."""
        prev_head = self.head
        new_head = self._linkedlist.push(data)
        if self._length == 0:
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

    def append(self, data):
        """Append method for Dll to add to tail."""
        prev_tail = self.tail
        new_tail = Node(data)
        if self._length == 0:
            self.tail = new_tail
            self.head = new_tail
            self.tail.prev = None
        self.tail = new_tail
        if self._length > 0:
            prev_tail.next = new_tail
            self.tail.prev = prev_tail
        self._length += 1

    def shift(self):
        """Shift method for Dll to remove from tail end."""
        if not self.tail:
            raise IndexError('List empty')
        deleted_node = self.tail.data
        self._length -= 1
        if not self.tail.prev:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return deleted_node

    def remove(self, val):
        """Remove method for Dll to remove specified node."""
        if self._length < 1:
            raise IndexError('Value not present. List empty.')
        if self._length == 1:
            self.head = None
            self.tail = None
        target = self._linkedlist.search(val)
        if target.prev:
            target.prev.next = target.next
        if target.next:
            target.next.prev = target.prev
        return target
