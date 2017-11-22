"""Binary Search Tree."""


class Node(object):
    """Create Node class for BST."""

    def __init__(self, data):
        """Initialization of node class object."""
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0


class BST(object):
    """Create Binary Search Tree."""

    def __init__(self, iterable=()):
        """Initialization of BST class object."""
        self.root = None
        self._size = 0
        self.layers = 0
        self.right_layers = 0
        self.left_layers = 0

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
                    new_node.depth = curr.depth + 1
                    curr.left = new_node
                    self._size += 1
                    break
                curr = curr.left
            elif new_node.data > curr.data:
                if not curr.right:
                    new_node.depth = curr.depth + 1
                    curr.right = new_node
                    self._size += 1
                    break
                curr = curr.right

        if new_node.depth > self.layers:
            self.layers = new_node.depth

        if (
                new_node.data > self.root.data and
                new_node.depth > self.right_layers
        ):
            self.right_layers += 1
        elif (
                new_node.data < self.root.data and
                new_node.depth > self.left_layers
        ):
            self.left_layers += 1

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
        return

    def size(self):
        """Return number of nodes in tree."""
        return self._size

    def contains(self, data):
        """Return True if value in tree, else False."""
        return bool(self.search(data))

    def depth(self):
        """Return the number of layers deep in the tree."""
        return self.layers

    def balance(self):
        """Return 0 if balanced, 1 or -1 if unbalanced."""
        return self.left_layers - self.right_layers


if __name__ == '__main__':
    """Document best and worst cast search with timeit."""
    import timeit as ti
    best_tree = BST((10, 5, 15, 4, 13, 7, 20))
    worst_tree = BST((1, 2, 3, 4, 5, 6, 7))

    time_best1 = ti.timeit("best_tree.search(7)",
                           setup="from __main__ import best_tree")
    time_best2 = ti.timeit("best_tree.search(12)",
                           setup="from __main__ import best_tree")
    time_worst1 = ti.timeit("worst_tree.search(7)",
                            setup="from __main__ import worst_tree")
    time_worst2 = ti.timeit("worst_tree.search(8)",
                            setup="from __main__ import worst_tree")

    print(time_best1)
    print(time_best2)
    print(time_worst1)
    print(time_worst2)
