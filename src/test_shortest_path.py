"""Test file for dijkstra and bellman-ford algorithims."""
import pytest


def test_dijkstra_returns_correct_order(weighted_graph):
    """Test dijkstra returns correct path."""
    from shortest_path import dijkstra
    assert dijkstra(weighted_graph, 'a', 'f') == ['a', 'c', 'e', 'f']
