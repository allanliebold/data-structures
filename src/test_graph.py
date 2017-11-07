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


def test_del_edge_removes_val(graph_w_edge):
    """Test del_edge to ensure val removed from associated key."""
    graph_w_edge.del_edge(84, 2)
    assert graph_w_edge.nodes[84] == set()


def test_del_edge_raise_error_no_edge(graph_w_edge):
    """Test to raise edge not found KeyError."""
    with pytest.raises(KeyError):
        graph_w_edge.del_edge(84, 9)


def test_has_node_true(graph_3):
    """Test has_node called with existing node returns True."""
    assert graph_3.has_node(20) is True


def test_has_node_false(graph_3):
    """Test has_node called with invalid node returns False."""
    assert graph_3.has_node(1000) is False


def test_has_node_false_after_del(graph_3):
    """Test has_node returns false after a node is deleted."""
    graph_3.del_node(17)
    assert graph_3.has_node(17) is False


def test_has_node_true_after_del_edge(graph_w_edge):
    """Test that has_node is True after edge deleted."""
    graph_w_edge.del_edge(84, 2)
    assert graph_w_edge.has_node(2) is True


def test_neighbors(graph_w_edge):
    """Test neighbors returns list of connected nodes."""
    graph_w_edge.add_edge(84, 17)
    assert 17 in graph_w_edge.neighbors(84)
    assert 2 in graph_w_edge.neighbors(84)


def test_neighbors_key_error(graph_w_edge):
    """Test KeyError raises calling neighbor with invalid node."""
    with pytest.raises(KeyError):
        graph_w_edge.neighbors(112)


def test_adjacent_node_not_found(graph_3):
    """Test KeyError raised if node not in dictionary."""
    with pytest.raises(KeyError):
        graph_3.adjacent(38, 999)


def test_adjacent_val_connected(graph_w_edge):
    """Test True if values are connected."""
    assert graph_w_edge.adjacent(2, 84) is True


def test_adjacent_val_not_connected(graph_3):
    """Test False for values not connected."""
    assert graph_3.adjacent(20, 17) is False
