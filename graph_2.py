"""Implement a graph traversal using composition from the original Graph class."""
from graph import Graph

visited = []


def dfs(graph, start):
    """Depth-first traversal method for Graph class."""
    visited.append(start)
    start = graph.nodes[start]
    for val in start:
        print(val)
        if val in visited:
            return
        dfs(graph, val)
    return
