"""Test file for dijkstra and bellman-ford algorithims."""
import pytest


def test_dijkstra_returns_correct_order_five_nodes(weighted_graph):
    """Test dijkstra returns correct path."""
    from shortest_path import shortest
    assert shortest(weighted_graph, 'a', 'f') == ['a', 'c', 'e', 'f']


def test_dijkstra_returns_order_for_three_nodes(weighted_graph_3_nodes):
    """Test dijkstra returns correct path for a graph with three nodes."""
    from shortest_path import shortest
    assert shortest(weighted_graph_3_nodes, 'a', 'c') == ['a', 'b', 'c']
