"""Implement a graph of nodes and edges."""


class Graph(object):
    """Create Graph class."""

    def __init__(self):
        """Initialization of node class."""
        self.nodes = dict()

    def all_nodes(self):
        """Return a list of all nodes in graph."""
        return list(self.nodes.keys())

    def all_edges(self):
        """Return a list of all edges in graph."""
        edge_list = []
        for key, value in self.nodes.items():
            for item in value:
                edge_list.append('{}-{}'.format(key, item))

        return edge_list

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
        if val in self.nodes:
            del self.nodes[val]
        else:
            raise KeyError('Node not found.')
        for key in self.nodes:
            if val in self.nodes[key]:
                self.del_edge(key, val)

    def del_edge(self, val1, val2):
        """Remove edge if passed two values that edge exists. Raise error if it doesn't exist."""
        if val2 in self.nodes[val1]:
            self.nodes[val1].remove(val2)
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
