"""Test file for graph.py."""
import pytest


def test_graph_initialization():
    """Test creation of graph object."""
    from graph import Graph
    new_graph = Graph()
    assert isinstance(new_graph.nodes, dict)


def test_graph_add_node():
    """Test adding a new node to empty graph."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(9)
    assert 9 in new_graph.nodes


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
    assert isinstance(graph_1.nodes[2], set)


def test_add_edge_existing_nodes(graph_3):
    """Test adding an edge between existing nodes."""
    graph_3.add_edge(20, 17)
    assert graph_3.nodes[20] == {17}


def test_add_edge_one_existing_node(graph_1):
    """Test adding an edge between one existing node, and one that hasn't been created yet."""
    graph_1.add_edge(5, 9)
    assert graph_1.nodes[5] == {9}


def test_add_two_edges_to_node(graph_3):
    """Test adding two edges to one existing node."""
    graph_3.add_edge(5, 20)
    graph_3.add_edge(5, 17)
    assert graph_3.nodes[5] == {20, 17}


def test_del_node_removes_node(graph_3):
    """Test del_node function removes node."""
    graph_3.del_node(20)
    assert graph_3.nodes == {5: set(), 17: set()}
