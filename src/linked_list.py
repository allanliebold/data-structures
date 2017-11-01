"""Singly-linked list.

Links together nodes in one direction, beginning at the head node.
"""


class Node(object):
    """Create Node class object used in list."""

    def __init__(self, data):
        """Initialization of node with next and data attributes."""
        self.next_node = None
        self.data = data


class LinkedList(object):
    """Linked list class object that contains nodes."""

    def __init__(self, iterable=()):
        """Initialization of list.

        Has a head, length, and can accept iterable.
        """
        self.head = None
        self._length = 0
        if isinstance(iterable, (tuple, list)):
            for i in iterable:
                self.push(i)
        else:
            self.push(iterable)

    def push(self, data):
        """Add new node with data to the head of the list."""
        new = Node(data)
        new.next_node = self.head
        self.head = new
        self._length += 1
        return new

    def pop(self):
        """Remove node from head of list."""
        if not self.head:
            raise IndexError('List is empty.')
        else:
            deleted_node = self.head.data
            self.head = self.head.next_node
            self._length -= 1
            return deleted_node

    def size(self):
        """Return number of nodes in linked list."""
        return self._length

    def search(self, target):
        """Find and return node that contains value passed as argument."""
        current_node = self.head
        while current_node.data != target:
            if current_node.next_node is None:
                raise ValueError('not found')
            else:
                current_node = current_node.next_node
        print(current_node.data)
        return current_node

    def remove(self, target):
        """Find node with target value.

        Returns node and removes references to it, or raises ValueError if not
        found.
        """
        current_node = self.head
        search_node = current_node.next_node
        if current_node.data == target:
            self.pop()
            return current_node
        while search_node.data != target:
            if search_node.next_node is None:
                raise ValueError('Not found')
            else:
                current_node = search_node
                search_node = current_node.next_node
        current_node.next_node = search_node.next_node
        self._length -= 1
        return search_node

    def display(self):
        """Display list as a tuple-like string."""
        list_contents = '('
        current_node = self.head
        list_contents += str(current_node.data)
        while current_node.next_node is not None:
            list_contents += ', ' + str(current_node.next_node.data)
            current_node = current_node.next_node
        list_contents += ')'
        return list_contents

    def __len__(self):
        """Function uses built-in len function to show length."""
        return self._length

    def __str__(self):
        """Function uses built-in print function to display list as string."""
        return self.display()
