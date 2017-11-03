"""Implement a graph of nodes and edges."""


class Node(object):
    """Create Node class."""

    def __init__(self, val):
        """Initialization of node class."""
        self.val = val


class Graph(object):
    """Create Graph class."""

    def __init__(self):
        """Initialization of node class."""
        self.all_nodes = []
        self.all_edges = []
        self.graph = {}

    def add_node(self, val):
        """Create node with value and all to all nodes list."""
        new_node = Node(val)
        self.all_nodes.append(new_node)
        if new_node in self.graph:
            raise ValueError("Duplicates are not allowed.")
        else:
            self.graph[new_node] = []
        return new_node
