"""Implement a graph with weighted edges."""


class Graph(object):
    """Create Graph class."""

    def __init__(self):
        """Initialization of node class."""
        self.nodes = dict()

    def add_node(self, val):
        """Create node with value and all to all nodes list."""
        if val in self.nodes:
            raise ValueError('Duplicates not allowed.')
        self.nodes[val] = dict()

    def add_edge(self, val1, val2, dist):
        """Create a connection from one node to another."""
        if val1 not in self.nodes:
            self.add_node(val1)
        if val2 not in self.nodes:
            self.add_node(val2)
        if val2 in self.nodes[val1]:
            print('Edge already exists')
        self.nodes[val1][val2] = dist

    def del_node(self, val):
        """Remove node if passed value that matches key in nodes."""
        if val in self.nodes:
            del self.nodes[val]
        else:
            raise KeyError('Node not found.')

    def del_edge(self, val1, val2):
        """Remove edge if passed two values that edge exists. Raise error if it doesn't exist."""
        if val2 in self.nodes[val1]:
            del self.nodes[val1][val2]
        else:
            raise KeyError('Edge not found.')

    def has_node(self, val):
        """If graph includes node with value passed, return True."""
        return True if val in self.nodes else False

    def neighbors(self, val):
        """Return list of nodes connected to node with value passed."""
        if val in self.nodes:
            return list(self.nodes[val])
        else:
            raise KeyError('Node not found.')

    def adjacent(self, val1, val2):
        """Return True if nodes passed are connected."""
        if val1 not in self.nodes or val2 not in self.nodes:
            raise KeyError('Node not found')
        elif val2 in self.nodes[val1]:
            return True
        else:
            return False
