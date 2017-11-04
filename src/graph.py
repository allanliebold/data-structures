"""Implement a graph of nodes and edges."""


class Graph(object):
    """Create Graph class."""

    def __init__(self):
        """Initialization of node class."""
        self.nodes = dict()

    def add_node(self, val):
        """Create node with value and all to all nodes list."""
        if val in self.nodes:
            raise ValueError('Duplicates not allowed.')
        self.nodes[val] = set()

    def add_edge(self, val1, val2):
        """Create a connection from one node to another."""
        if val1 not in self.nodes:
            self.add_node(val1)
        if val2 not in self.nodes:
            self.add_node(val2)
        if val2 in self.nodes[val1]:
            print('Edge already exists')
        self.nodes[val1].add(val2)

    def del_node(self, val):
        """Remove node if passed value that matches key in nodes."""
        if val not in self.nodes:
            raise KeyError('Node not found.')
        del self.nodes[val]
