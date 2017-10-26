"""Tests for doubly-linked list."""
import pytest


def test_dll_attr():
    """Test if Dll object is created."""
    from dll import Dll
    test_dll = Dll()
    assert test_dll._length == 0
