"""Test for graph_2.py."""
import pytest


def test_dfs_output(graph_5_w_edges):
    """Test output of dfs function."""
    from graph_2 import dfs
    assert dfs(graph_5_w_edges, 3) == [3, 8, 16, 59, 77]
