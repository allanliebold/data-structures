"""Test file for graph.py."""
import pytest


def test_graph_initialization():
    """Test creation of graph object."""
    from graph import Graph
    new_graph = Graph()
    assert isinstance(new_graph.nodes, set)


def test_graph_add_node():
    """Test adding a new node to empty graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(9)
    assert new_graph.nodes == {9}


def test_graph_add_dupe_node():
    """Test adding a new node to empty graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(9)
    with pytest.raises(ValueError):
        new_graph.add_node(9)


def test_graph_add_second_node(graph_1):
    """Test adding a second node to graph."""
    graph_1.add_node(2)
    assert graph_1.nodes == {2, 5}
