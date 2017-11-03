"""Test file for graph.py."""
import pytest


def test_node_class_instantiation():
    """Test if Node class is created with value attribute."""
    from graph import Node
    some_node = Node(4)
    assert some_node.val == 4


def test_graph_class_instantiation():
    """Test if Graph class is created with all attributes."""
    from graph import Graph
    some_graph = Graph()
    assert some_graph.all_nodes == []
    assert some_graph.all_edges == []
    assert some_graph.graph == {}


def test_add_node():
    """Test if node added to graph and list of nodes."""
    from graph import Graph
    some_graph = Graph()
    new_node = some_graph.add_node(83)
    assert new_node in some_graph.graph
