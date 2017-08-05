"""test for graph"""
from graph_paths import Graph
import pytest


@pytest.fixture
def empty_graph():
    """ Makes a graph."""
    return(Graph())


@pytest.fixture
def greater_graph():
    """Makes a graph that is size 5"""
    graph = Graph()
    graph.add_edge('a', 'b', 1)
    graph.add_edge('b', 'c', 1)
    graph.add_edge('a', 'd', 1)
    graph.add_edge('c', 'e', 1)
    graph.add_edge('a', 'f', 1)
    return(graph)


@pytest.fixture
def path_graph():
    """Makes a graph that is size 3"""
    graph = Graph()
    graph.add_edge('a', 'b', 10)
    graph.add_edge('a', 'c', 5)
    graph.add_edge('c', 'f', 20)
    graph.add_edge('b', 'd', 5)
    graph.add_edge('b', 'e', 30)
    graph.add_edge('d', 'e', 5)
    graph.add_edge('e', 'f', 1)
    return(graph)


@pytest.fixture
def three_graph():
    """Makes a graph that is size 3"""
    graph = Graph()
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 2)
    graph.add_edge(3, 2, 3)
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
    assert three_graph.edges() == [(1, 2, 10), (1, 3, 2), (3, 2, 3)]


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


def test_add_edge_error(empty_graph):
    with pytest.raises(ValueError):
        empty_graph.add_edge(1, 2, [])


def test_add_edge(three_graph):
    """Test to see if add edge works on and makes new node."""
    assert three_graph.edges() == [(1, 2, 10), (1, 3, 2), (3, 2, 3)]


def test_add_edge_old_node(three_graph):
    """Test to see if add edge works on and makes new node."""
    three_graph.add_edge(2, 3, 20)
    assert three_graph.edges() == [(1, 2,10), (1, 3, 2) , (2, 3, 20), (3, 2, 3)]


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
        empty_graph.del_edge(1, 2, 10)


def test_del_edge(three_graph):
    """Test to see if del edge works"""
    three_graph.del_edge(1, 2, 10)
    assert three_graph.edges() == [(1, 3, 2), (3, 2, 3)]


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


def test_depth_first_error(empty_graph):
    """Test if depth first can error"""
    with pytest.raises(ValueError):
        empty_graph.depth_first_traversal(1)


def test_breadth_first_error(empty_graph):
    """Test if breadth first can error"""
    with pytest.raises(ValueError):
        empty_graph.breadth_first_traversal(1)


def test_depth_first_work(greater_graph):
    """Test if depth first can error"""
    assert greater_graph.depth_first_traversal('a') == ['a', 'b', 'c', 'e', 'd', 'f']


def test_breadth_first_work(greater_graph):
    """Test if breadth first can error"""
    assert greater_graph.breadth_first_traversal('a') == ['a', 'b', 'd', 'f', 'c', 'e']


def test_bellman_ford(path_graph):
    """Test the bellman ford fucntion"""
    assert path_graph.bellman_ford('a', 'f') == ['f', 'e', 'd', 'b', 'a']


def test_dijkstra(path_graph):
    """Test the dijkstra fucntion"""
    assert path_graph.dijkstra('a', 'f') == ['f', 'e', 'd', 'b', 'a']
