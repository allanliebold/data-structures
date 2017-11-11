"""Implementation of Dijkstra's Shortest Path Algorithm."""
from graph_3 import Graph


def dijkstra(graph, start, end, visited=[], distances={}, routes={}):
    """Function utilizing Dijkstra's algorithm.

    Find the shortest path from a starting node to and end node.
    """
    if start == end:
        path = []
        pred = end
        while pred is not None:
            path.append(pred)
            pred = routes.get(pred, None)
        return path
    else:
        if not visited:
            distances[start] = 0
        for edge in graph.nodes[start]:
            if edge not in visited:
                new_distance = distances[start] + graph.nodes[start][edge]
                if new_distance < distances.get(edge, float('inf')):
                    distances[edge] = new_distance
                    routes[edge] = start
        visited.append(start)
        unvisited = {}
        for node in graph.nodes:
            if node not in visited:
                unvisited[node] = distances.get(node, float('inf'))
            new_start = min(unvisited, key=unvisited.get)
            dijkstra(graph, new_start, visited, distances, routes)
