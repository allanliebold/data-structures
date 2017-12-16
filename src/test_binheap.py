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


def test_pop_empty_heap(heap):
    """Test IndexError raises when pop called on empty heap."""
    with pytest.raises(IndexError):
        heap.pop()


def test_empty_heap_after_pop(heap):
    """Test pop on heap with one value empties heap."""
    heap.push(1)
    heap.pop()
    assert heap.contents == []


def test_pop_heap2_moves_value_to_0_index(heap_2):
    """Test pop on heap 2 moves remaining value to index 0."""
    heap_2.pop()
    assert heap_2.contents[0] == 7


def test_heap_sorted_after_pop(heap_3):
    """Test pop on heap to ensure sorted properly."""
    heap_3.pop()
    assert heap_3.contents == [74, 5]


def test_heap_of_10_nums_sorted_on_initialization():
    """Test to ensure heapify method is sorting correctly."""
    from binheap import Heap
    heap_10 = Heap([3, 22, 31, 4, 49, 47, 19, 88, 92, 2])
    assert heap_10.contents == [92, 88, 47, 49, 4, 22, 19, 3, 31, 2]
