"""Test of priority queue and associated methods."""
import pytest


def test_initialization_empty_dict():
    """Test if empty dict created on init."""
    from priorityq import PriQ
    new_priq = PriQ()
    assert new_priq.pri_dict == {}


def test_inserts_value_no_priority():
    """Test if insert method adds a value with no priority to PriQ."""
    from priorityq import PriQ
    new_priq = PriQ()
    new_priq.insert(88)
    assert new_priq.pri_dict == {0: [88]}


def test_inserts_value_with_priority(priq):
    """Test if insert method adds a value with a priority to PriQ."""
    priq.insert(88, 1)
    assert priq.pri_dict == {1: [88]}


def test_inserts_two_diff_priorities(priq):
    """Test inserting two values with different priorities."""
    priq.insert(6, 1)
    priq.insert(44, 2)
    assert priq.pri_dict == {1: [6], 2: [44]}


def test_inserts_two_val_same_pri(priq):
    """Test inserting two values with same priorities."""
    priq.insert(6, 1)
    priq.insert(44, 1)
    assert priq.pri_dict == {1: [6, 44]}
