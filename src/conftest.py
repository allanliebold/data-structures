"""Fixtures for test_deque.py."""
import pytest


@pytest.fixture
def dq():
    """Create empty Deque class."""
    from deque import Deque
    return Deque()


@pytest.fixture
def dq_1():
    """Create and append with one value."""
    from deque import Deque
    dq = Deque()
    dq.append(9)
    return dq


@pytest.fixture
def dq_3():
    """Create and append with three values."""
    from deque import Deque
    dq = Deque()
    dq.append('snine')
    dq.append(4)
    dq.append('ragtime')
    return dq


@pytest.fixture
def heap():
    """Create instance of heap with empty list."""
    from binheap import Heap
    test_heap = Heap()
    return test_heap


@pytest.fixture
def heap_2():
    """Create instance of heap with two values."""
    from binheap import Heap
    test_heap = Heap([7, 49])
    return test_heap


@pytest.fixture
def heap_3():
    """Create instance of heap with empty list."""
    from binheap import Heap
    test_heap = Heap([5, 99, 74])
    return test_heap


@pytest.fixture
def priq():
    """Create empty priq."""
    from priorityq import PriQ
    new_priq = PriQ()
    return new_priq


@pytest.fixture
def priq_1():
    """Create priq with one value and no priority."""
    from priorityq import PriQ
    new_priq = PriQ()
    new_priq.insert(7)
    return new_priq


@pytest.fixture
def priq_pri_1():
    """Create priq with one value and a priority of one."""
    from priorityq import PriQ
    new_priq = PriQ()
    new_priq.insert(7, 1)
    return new_priq


@pytest.fixture
def priq_3_diff():
    """Create priq with 3 different priorities and values."""
    from priorityq import PriQ
    new_priq = PriQ()
    new_priq.insert(7, 1)
    new_priq.insert(10, 2)
    new_priq.insert(14, 3)
    return new_priq


@pytest.fixture
def priq_2_same():
    """Create priq with 2 priorities. One has two values."""
    from priorityq import PriQ
    new_priq = PriQ()
    new_priq.insert(7, 1)
    new_priq.insert(10, 2)
    new_priq.insert(14, 2)
    return new_priq


@pytest.fixture
def graph():
    """Create an empty graph."""
    from graph import Graph
    new_graph = Graph()
    return new_graph


@pytest.fixture
def graph_1():
    """Create graph with one node."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(5)
    return new_graph


@pytest.fixture
def graph_3():
    """Create graph with three nodes."""
    from graph import Graph
    new_graph = Graph()
    new_graph.add_node(5)
    new_graph.add_node(20)
    new_graph.add_node(17)
    return new_graph
