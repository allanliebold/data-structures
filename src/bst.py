"""Binary Search Tree."""


class Node(object):
    """Create Node class for BST."""

    def __init__(self, data):
        """Initialization of node class object."""
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    """Create Binary Search Tree."""

    def __init__(self, iterable=()):
        """Initialization of BST class object."""
        self.root = None
        self.size = 0

        if isinstance(iterable, (tuple, list)):
            for i in iterable:
                self.insert(i)
        else:
            self.push(iterable)

    def insert(self, data):
        """Add node to tree."""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            self.size += 1
            return

        curr = self.root
        while curr:
            if new_node.data < curr.data:
                if not curr.left:
                    curr.left = new_node
                    self.size += 1
                    return
                curr = curr.left
            if new_node.data > curr.data:
                if not curr.right:
                    curr.right = new_node
                    self.size += 1
                    return
                curr = curr.right
