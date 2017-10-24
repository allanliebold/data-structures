"""Linked List."""


class Node(object):
    """Node Class."""

    def __init__(self, value, next=None):
        """Init."""
        self.next = next
        self.value = value


class LinkedList(object):
    """LinkedList Class."""

    def __init__(self, head=None, length=0):
        """Init."""
        self.head = head
        self.length = length

    def push(self, node):
        """Push method."""
        node.next = self.head
        self.head = node
        self.length += 1
        print('Node added')
        print(node)

    def pop(self):
        """Pop method."""
        deleted_node = self.head
        self.head = self.head.next
        print('Node deleted')
        print(deleted_node)
        self.length -= 1
        return deleted_node

    def size(self):
        """Size method."""
        return self.length
