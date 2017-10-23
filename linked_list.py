"""Linked List."""


class Node(object):
    """Node Class."""

    def __init__(self, value, next=None):
        """Init."""
        self.next = next
        self.value = value


class LinkedList(object):
    """LinkedList Class."""

    def __init__(self, head=None, size=0):
        """Init."""
        self.head = head
        self.size = size
    def push(self, node):
        """Push method."""
        node.next = self.head
        self.head = node
        self.size += 1
        print('Node added')
        print(node)
    def pop(self):
        """Pop method."""
        deleted_node = self.head
        self.head = self.head.next
        print('Node deleted')
        print(deleted_node)
        self.size -= 1
        return deleted_node
