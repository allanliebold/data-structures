"""Implementation of a Max Binary Heap."""


class Node(object):
    """Create Node class object."""

    def __init__(self, data):
        """Initialization of Node with attributes."""
        self.data = data
        self.parent = None
        self.child_left = None
        self.child_right = None


class Heap(object):
    """Create Heap class object."""

    def __init__(self, iterable=()):
        """Initialization of Heap with attributes."""
        self.root = None
        self._size = 0

        self.root = Node(iterable[0])
        current_node = self.root
        for i in range(len(iterable)):
            if iterable[(2 * i) + 1] is not None:
                current_node.left_child = Node(iterable[(2 * i) + 1])
            if iterable[(2 * i) + 2] is not None:
                current_node.right_child = Node(iterable[(2 * i) + 2])
            if current_node.left_child is not None:
                current_node.left_child.parent = current_node
            if current_node.right_child is not None:
                current_node.right_child.parent = current_node
            current_node = iterable[i + 1]

    # def push(data):
    #     """Add new node to heap with data passed."""
    #     new_node = Node(data)

    #     if not self.head:
    #         self.head = new_node
    #         return

    #     current_node = self.head

    #     while current_node.left is not None:
    #         if current_node.right is None:
    #             new_node.parent = current_node
    #             current_node.right = new_node
    #             return
    #         current_node = current_node.left
