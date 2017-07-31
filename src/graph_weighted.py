"""Implementation of a graph
 that is unweighted and directed."""


class Graph(object):
    """Define attributes and methods for the graph class."""

    def __init__(self):
        """Inits the graph object."""
        self._graph = {}

    def nodes(self):
        """Return list of graph nodes."""
        return list(self._graph.keys())

    def edges(self):
        """Return list all edges in  graph edges."""
        edges = []
        for key in self.nodes():
            for item in self._graph[key]:
                edges.append((key, item[0], item[1]))
        return edges

    def add_node(self, val):
        """Add as node to graph."""
        if type(val) not in [str, int, float]:
            raise ValueError('Please use a valid value.')
        if self.has_node(val):
            message = str(val) + " is in graph"
            raise ValueError(message)
        self._graph[val] = []

    def has_node(self, val):
        """Return Ture if a val is in the graph, False if the val is not in the graph."""
        return val in self._graph

    def add_edge(self, val1, val2, weight):
        """Adds an edge between to nodes, adds nodes with the val if node is not in grpah."""
        if type(weight) not in [int, float]:
            raise ValueError('Weight must be int or float.')
        if not self.has_node(val1):
            self.add_node(val1)
        if not self.has_node(val2):
            self.add_node(val2)
        if (val1, val2, weight) not in self.edges():
            self._graph[val1].append((val2, weight))

    def del_node(self, val):
        """Removes a node and any edges that pointed to it."""
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        del self._graph[val]
        for key in self.nodes():
            for item in self._graph[key]:
                if val == item[0]:
                    self._graph[key].remove(item)

    def del_edge(self, val1, val2, weight):
        """Remove an edge."""
        if (val1, val2, weight) not in self.edges():
            raise ValueError('This edge is not in graph.')
        self._graph[val1].remove((val2, weight))

    def neighbors(self, val):
        """Returns the list of neighbors for any node in the graph."""
        if val not in self.nodes():
            raise ValueError('This node is not in the graph.')
        return [item[0] for item in self._graph[val]]

    def adjacent(self, val1, val2):
        """Returns bool of whether val1 is val2's neighbor."""
        if val1 not in self._graph or val2 not in self._graph:
            raise ValueError('One or both values are not in the graph.')
        if val2 in self.neighbors(val1) or val1 in self.neighbors(val2):
            return True
        else:
            raise AssertionError('There is no edge from val1 to val2.')
