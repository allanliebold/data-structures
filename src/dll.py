"""Implementation of Doubly-Linked list with a head and tail."""
from linked_list import LinkedList
from linked_list import Node


class Dll(object):
    """Doubly-Linked List class object."""

    def __init__(self):
        """Doubly-linked list initialization.

        Composed of some attributes from linked-list, and also has a tail.
        """
        self._linkedlist = LinkedList()
        self.head = self._linkedlist.head
        self._length = self._linkedlist._length
        self.tail = None

    def push(self, data):
        """Push node to head of list."""
        prev_head = self.head
        new_head = self._linkedlist.push(data)
        if self.tail is None:
            self.tail = new_head
        if self.head:
            prev_head.prev = new_head
        self.head = new_head
        self.head.next_node = prev_head
        self._length += 1
        self.head.prev = None

    def pop(self):
        """Remove node at head of list."""
        if not self.head:
            raise IndexError('List empty')
        deleted_node = self.head.data
        self._length -= 1
        if not self.head.next_node:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
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
            prev_tail.next_node = new_tail
            self.tail.prev = prev_tail
        self._length += 1

    def shift(self):
        """Shift method for Dll to remove from tail end."""
        if self._length == 0:
            raise IndexError('List empty')
        deleted_node = self.tail.data
        self._length -= 1
        if not self.tail.prev:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next_node = None
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
            target.prev.next_node = target.next_node
        if target.next_node:
            target.next_node.prev = target.prev
        return target

    def __len__(self):
        """Function uses built-in len function to show length."""
        return self._length
