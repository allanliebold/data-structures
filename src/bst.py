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
        self._size = 0

        if isinstance(iterable, (tuple, list)):
            for i in iterable:
                self.insert(i)
        else:
            self.insert(iterable)

    def insert(self, data):
        """Add node to tree."""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            self._size += 1
            return

        curr = self.root
        while curr:
            if new_node.data == curr.data:
                return "Duplicate data"

            if new_node.data < curr.data:
                if not curr.left:
                    curr.left = new_node
                    self._size += 1
                    return
                curr = curr.left
            if new_node.data > curr.data:
                if not curr.right:
                    curr.right = new_node
                    self._size += 1
                    return
                curr = curr.right

    def search(self, data):
        """Return node with specified data, or None."""
        curr = self.root
        while curr:
            if curr.data == data:
                return curr
            elif data < curr.data:
                curr = curr.left
            elif data > curr.data:
                curr = curr.right
        return None

    def size(self):
        """Return number of nodes in tree."""
        return self._size
