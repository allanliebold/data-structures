"""Implement graph traversal with composition from the original Graph class."""
from graph import Graph


def dfs(graph, node):
    """Depth-first traversal method for Graph class."""
    visited = []

    def traverse(graph, node):
        layer = []
        visited.append(node)
        layer.append(node)
        node = graph.nodes[node]
        for val in node:
            if val not in visited:
                layer.extend(traverse(graph, val))
        return layer
    return traverse(graph, node)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 1)
    g.add_edge(4, 5)
    print(g.nodes)
    print(dfs(g, 1))
