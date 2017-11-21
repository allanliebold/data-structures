"""Tests for Binary Search Tree."""
import pytest


def test_node_initialized():
    """Test that node object is initialized."""
    from bst import Node
    n = Node(1)
    assert n.data == 1


def test_bst_initialized(bst_empty):
    """Test new bst has no root."""
    assert bst_empty.root is None


def test_bst_three_root(bst_three):
    """Test root attributes of bst with three nodes."""
    assert bst_three.root.data == 10
    assert bst_three.root.left.data == 5
    assert bst_three.root.right.data == 15


def test_insert_node_in_bst_three(bst_three):
    """Test node is inserted in the correct place."""
    bst_three.insert(13)
    assert bst_three.root.right.left.data == 13


def test_size_bst_three(bst_three):
    """Test size is corrent on bst with three nodes."""
    assert bst_three.size == 3
