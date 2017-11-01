"""Test file for binheap implementation."""
import pytest


def test_heap_initialized_with_list(heap):
    """Check if Heap object has empty list."""
    assert heap.contents == []


def test_heap_initialized_with_multiple_values(heap_3):
    """Check if Heap object can accept iterable of three values."""
    assert heap_3.contents == [99, 5, 74]


def test_push_empty_heap(heap):
    """Check if Heap object can accept push of single value."""
    heap.push(9)
    assert heap.contents == [9]


def test_push_to_heap_with_values(heap_3):
    """Check if heap of three values adds additional value on push."""
    heap_3.push(18)
    assert heap_3.contents == [99, 18, 74, 5]


def test_king_num_goes_to_root_throne(heap_3):
    """Check num greater than current root sorts to root."""
    heap_3.push(196)
    assert heap_3.contents == [196, 99, 74, 5]


def test_if_error_raised_for_dupe_nums(heap_3):
    """Check if ValueError raised if num already in list passed in as arg."""
    with pytest.raises(ValueError):
        heap_3.push(99)


def test_size_after_pushing(heap_3):
    """Test to see if size is 4 after pushing single value to existing heap of 3."""
    heap_3.push(91)
    heap_3._size == 4
