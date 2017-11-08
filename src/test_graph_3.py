"""Test file for graph.py."""
import pytest


def test_graph_initialization():
    """Test creation of graph object."""
    from graph_3 import Graph
    new_graph = Graph()
    assert isinstance(new_graph.nodes, dict)


def test_graph_add_node():
    """Test adding a new node to empty graph."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_node(9)
    assert 9 in new_graph.nodes


def test_graph_add_dupe_node():
    """Test adding a new node to empty graph."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_node(9)
    with pytest.raises(ValueError):
        new_graph.add_node(9)


def test_graph_add_edge():
    """Test adding an edge with a distance."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_edge('A', 'B', 6)
    assert new_graph.nodes == {'A': {'B': 6}, 'B': {}}


def test_delete_edge():
    """Test if deleting edge removes edge and distance associated wit it."""
    from graph_3 import Graph
    new_graph = Graph()
    new_graph.add_edge(19, 73, 2)
    new_graph.del_edge(19, 73)
    assert new_graph.nodes == {19: {}, 73: {}}
