"""Test for graph_2.py."""
import pytest


def test_dfs_output(graph_5_w_edges):
    """Test output of dfs function."""
    from graph_2 import dfs
    assert dfs(graph_5_w_edges, 3) == [3, 8, 16, 59, 77]


def test_hundo(graph_5_w_edges):
    """Our 100th test.

    Test output of bfs function.
    """
    from graph_2 import bfs
    assert bfs(graph_5_w_edges, 3) == [3, 8, 59, 16, 77]


def test_dfs_on_looping_graph(graph_loop):
    """Test dfs on looping graph doesn't get stuck."""
    from graph_2 import dfs
    assert dfs(graph_loop, 2) == [2]


def test_bfs_on_looping_graph(graph_loop):
    """Test bfs on looping graph doesn't get stuck."""
    from graph_2 import dfs
    assert dfs(graph_loop, 2) == [2]
