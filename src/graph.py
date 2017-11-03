"""Implement a graph of nodes and edges."""


class Graph(object):
    """Create Graph class."""

    def __init__(self):
        """Initialization of node class."""
        self.nodes = set()

    def add_node(self, val):
        """Create node with value and all to all nodes list."""
        if val in self.nodes:
            raise ValueError('Duplicates not allowed.')
        self.nodes.add(val)

    def add_edge(self, val1, val2):
        """Create a connection from one node to another."""
