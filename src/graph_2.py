"""Implement a graph traversal using composition from the original Graph class."""
from graph import Graph



def dfs(graph, start):
    """Depth-first traversal method for Graph class."""
    visited = []
    visited.append(start)
    start = graph.nodes[start]
    for val in start:
        print(val)
        if val in visited:
            return
        visited.extend(dfs(graph, val))
    return visited
