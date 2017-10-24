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

    def search(self, target):
        """Search method."""
        current_node = self.head
        while current_node.value != target:
            if current_node.next is None:
                return None
            else:
                current_node = current_node.next
        print(current_node.value)
        return current_node

    def remove(self, target):
        """Remove method."""
        current_node = self.head
        next_node = current_node.next
        if current_node.value == target:
            self.pop()
            return current_node
        while next_node.value != target:
            if next_node.next is None:
                raise ValueError('Not found')
            else:
                current_node = next_node
                next_node = current_node.next
        current_node.next = next_node.next
        self.length -= 1
        return next_node
