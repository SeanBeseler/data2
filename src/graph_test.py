"""test for graph"""
from graph import Graph
import pytest


@pytest.fixture
def empty_graph():
    """ Makes a graph."""
    return(Graph())


@pytest.fixture
def three_graph():
    """Makes a graph that is size 3"""
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 2)
    return(graph)


def test_init(empty_graph):
    """Test that the init works"""
    assert empty_graph._graph == {}


def test_nodes(empty_graph):
    """Test the nodes function returns"""
    assert empty_graph.nodes() == []


def test_nodes_not_empty(three_graph):
    """Test the nodes function returns that is populated"""
    assert three_graph.nodes() == [1, 2, 3]


def test_edges(empty_graph):
    """Test the edges function returns"""
    assert empty_graph.edges() == []


def test_edges_not_empty(three_graph):
    """Test the edges function returns that is populated"""
    assert three_graph.edges() == [(1, 2), (1, 3), (3, 2)]


def test_add_node_error_not_proper_type(empty_graph):
    """Test to see if add_node can error"""
    with pytest.raises(ValueError):
        empty_graph.add_node([])


def test_add_node_error_has_node(three_graph):
    """Test to see if add_node can error"""
    with pytest.raises(ValueError):
        three_graph.add_node(1)


def test_add_node_works(three_graph):
    """Test to see if add node works"""
    assert three_graph.has_node(1)


def test_has_node_false(empty_graph):
    """Test to see if has node works on empyt graph"""
    assert empty_graph.has_node(1) is False


def test_has_node_true(three_graph):
    """Test to see if has node works on populated graph"""
    assert three_graph.has_node(1)


def test_add_edge(three_graph):
    """Test to see if add edge works on and makes new node."""
    assert three_graph.edges() == [(1, 2), (1, 3), (3, 2)]


def test_add_edge_old_node(three_graph):
    """Test to see if add edge works on and makes new node."""
    three_graph.add_edge(2, 3)
    assert three_graph.edges() == [(1, 2), (1, 3), (2, 3), (3, 2)]


def test_del_node_error(empty_graph):
    """Test to see if del_node can error"""
    with pytest.raises(ValueError):
        empty_graph.del_node(1)


def test_del_node(three_graph):
    """Test to see if del node works"""
    three_graph.del_node(2)
    assert three_graph.has_node(2) is False


def test_del_edge_error(empty_graph):
    """Test to see if del_edge can error"""
    with pytest.raises(ValueError):
        empty_graph.del_edge(1, 2)


def test_del_edge(three_graph):
    """Test to see if del edge works"""
    three_graph.del_edge(1, 2)
    assert three_graph.edges() == [(1, 3), (3, 2)]


def test_neighbors_error(empty_graph):
    """Test to see if neighbors can error"""
    with pytest.raises(ValueError):
        empty_graph.neighbors(1)


def test_neighbors(three_graph):
    """Test to see if neighbors works"""
    assert three_graph.neighbors(1) == [2, 3]


def test_adjacent_node_not_in_graph(empty_graph):
    """Test to see if adjancet can error"""
    with pytest.raises(ValueError):
        empty_graph.adjacent(1, 2)


def test_adjacent_edge_not_in_graph(empty_graph):
    """Test to see if adjancet can error"""
    with pytest.raises(ValueError):
        empty_graph.adjacent(2, 1)


def test_adjacent_works(three_graph):
    """Test to see if adjancet works"""
    assert three_graph.adjacent(2, 1)
