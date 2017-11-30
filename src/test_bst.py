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


def test_insert_duplicate_data(bst_three):
    """Test return when trying to insert data already in tree."""
    assert bst_three.insert(5) == "Duplicate data"


def test_insert_node_in_bst_three(bst_three):
    """Test node is inserted in the correct place."""
    bst_three.insert(13)
    assert bst_three.root.right.left.data == 13


def test_size_bst_three(bst_three):
    """Test size is corrent on bst with three nodes."""
    assert bst_three.size() == 3


def test_size_bst_three_insert_one(bst_three):
    """Test size is corrent on bst with three nodes after insert."""
    bst_three.insert(8)
    assert bst_three.size() == 4


def test_search_valid_data(bst_three):
    """Test search for data in tree returns correct node data."""
    assert bst_three.search(15).data == 15


def test_search_valid_data_return_node(bst_three):
    """Test search for data in tree returns correct node."""
    assert bst_three.search(5) == bst_three.root.left


def test_search_invalid_data(bst_three):
    """Test search for data not in tree returns None."""
    assert bst_three.search(22) is None


def test_search_data_in_root(bst_three):
    """Test search for data in root returns root node."""
    assert bst_three.search(10) == bst_three.root


def test_contains_data_in_tree(bst_three):
    """Test contains method on data in tree returns True."""
    assert bst_three.contains(5) is True


def test_contains_data_not_in_tree(bst_three):
    """Test contains method on data in tree returns True."""
    assert bst_three.contains(8) is False


def test_depth_of_zero_empty_tree(bst_empty):
    """Depth on empty tree is 0."""
    assert bst_empty.depth() == 0


def test_depth_of_zero_tree_with_root(bst_empty):
    """Depth on tree with one node is 0."""
    bst_empty.insert(30)
    assert bst_empty.depth() == 0


def test_depth_of_one(bst_three):
    """Test that tree returns depth of 1."""
    assert bst_three.depth() == 1


def test_depth_of_two(bst_three):
    """Test tree with depth of 2."""
    bst_three.insert(8)
    assert bst_three.depth() == 2


def test_balance_equal(bst_three):
    """Test balanced tree returns 0."""
    assert bst_three.balance() == 0


def test_balance_negative_one(bst_three):
    """Test left balanced tree returns 1."""
    bst_three.insert(6)
    assert bst_three.balance() == 1


def test_balance_plus_one(bst_three):
    """Test left balanced tree returns -1."""
    bst_three.insert(20)
    assert bst_three.balance() == -1


def test_in_order_gen(bst_three):
    """Test in order generator on tree with three nodes."""
    gen = bst_three.in_order()
    output = []
    for i in range(3):
        output.append(next(gen))
    assert output == [5, 10, 15]


def test_pre_order_gen(bst_three):
    """Test pre order generator on tree with three nodes."""
    gen = bst_three.pre_order()
    output = []
    for i in range(3):
        output.append(next(gen))
    assert output == [10, 5, 15]


def test_post_order_gen(bst_three):
    """Test post order generator on tree with three nodes."""
    gen = bst_three.post_order()
    output = []
    for i in range(3):
        output.append(next(gen))
    assert output == [5, 15, 10]


def test_breadth_first_gen(bst_three):
    """Test breadth first generator on tree with three nodes."""
    gen = bst_three.breadth_first()
    output = []
    for i in range(3):
        output.append(next(gen))
    assert output == [10, 5, 15]


def test_in_order_gen_big(bst_big):
    """Test in order generator on tree with many nodes."""
    gen = bst_big.in_order()
    output = []
    for i in range(15):
        output.append(next(gen))
    assert output == [1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 15, 19, 20, 22]


def test_pre_order_gen_big(bst_big):
    """Test pre order generator on tree with many nodes."""
    gen = bst_big.pre_order()
    output = []
    for i in range(15):
        output.append(next(gen))
    assert output == [10, 5, 2, 1, 3, 8, 7, 9, 15, 12, 11, 13, 20, 19, 22]


def test_post_order_gen_big(bst_big):
    """Test post order generator on tree with many nodes."""
    gen = bst_big.post_order()
    output = []
    for i in range(15):
        output.append(next(gen))
    assert output == [1, 3, 2, 7, 9, 8, 5, 11, 13, 12, 19, 22, 20, 15, 10]


def test_breadth_first_gen_big(bst_big):
    """Test breadth first generator on tree with many nodes."""
    gen = bst_big.breadth_first()
    output = []
    for i in range(15):
        output.append(next(gen))
    assert output == [10, 5, 15, 2, 8, 12, 20, 1, 3, 7, 9, 11, 13, 19, 22]


def test_traversal_empty(bst_empty):
    """Test traversal on empty tree."""
    assert bst_empty.in_order() == 'Tree empty'


def test_traversal_one_node(bst_empty):
    """Test traversal on tree with one node."""
    bst_empty.insert(1)
    gen = bst_empty.in_order()
    assert next(gen) == 1


def test_orphan_node(bst_empty):
    """Test that the first node in a tree has no parents."""
    bst_empty.insert(1)
    assert bst_empty.root.parent is None


def test_parentage_of_second_node(bst_three):
    """Test that child node has correct parent."""
    assert bst_three.root.left.parent.data == 10


def test_parentage_of_edge_node(bst_big):
    """Test that a specific child in a big tree has correct parent."""
    child = bst_big.root.left.right.left
    assert child.parent.parent.data == 5


def test_delete_from_empty_tree(bst_empty):
    """Test delete called on empty tree returns None."""
    assert bst_empty.delete(1) is None


def test_delete_invalid_value(bst_big):
    """Test calling delete with a value not in the tree."""
    assert bst_big.delete(44) is None


def test_delete_root_only_node(bst_empty):
    """Test deleting root from one node tree."""
    bst_empty.insert(1)
    bst_empty.delete(1)
    assert bst_empty.root is None


def test_delete_root_and_replace(bst_three):
    """Test deleting root puts expected node in its place."""
    bst_three.delete(10)
    assert bst_three.root.data == 15
    assert bst_three.root.parent is None
    assert bst_three.root.right is None
    assert bst_three.root.left.data == 5


def test_delete_root_and_replace_big_tree(bst_big):
    """Test deleting root with a larger tree."""
    bst_big.delete(10)
    assert bst_big.root.data == 11
    assert bst_big.root.parent is None


def test_delete_leaf(bst_three):
    """Test deleting a non-root node without children."""
    assert bst_three.delete(5) == 5
    assert bst_three.root.left is None
    assert bst_three._size == 2


def test_delete_node_children(bst_big):
    """Test deleting a node with two children."""
    bst_big.delete(15)
    assert bst_big.root.right.data == 19
    assert bst_big.root.right.left.data == 12


def test_delete_node_only_child(bst_long_branch_right):
    """Test deleting a node with one child."""
    bst_long_branch_right.delete(2)
    assert bst_long_branch_right.root.right.data == 3


def test_delete_node_only_child_left(bst_long_branch_left):
    """Test deleting a node with one child on the left side."""
    bst_long_branch_left.delete(9)
    assert bst_long_branch_left.root.left.data == 8
