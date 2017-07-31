"""Implementation of a graph
 that is weighted and directed."""


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

    def depth_first_traversal(self, val):
        """Return a path starting from val using the depth first  traversal."""
        from stack import Stack
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        path = []
        to_visit = Stack()
        current_val = val
        while True:
            if current_val not in path:
                path.append(current_val)
                for neighbor in self._graph[current_val][::-1]:
                    to_visit.push(neighbor[0])
            if len(to_visit) == 0:
                break
            current_val = to_visit.pop().val
        return path

    def breadth_first_traversal(self, val):
        """Returns a path starting from val using the depth- frist traversal."""
        from que import que
        if not self.has_node(val):
            raise ValueError('This node is not in the graph.')
        path = []
        current_val = val
        to_visit = que()
        while True:
            if current_val not in path:
                path.append(current_val)
                for neighbor in self._graph[current_val]:
                    to_visit.enqueue(neighbor[0])
            if len(to_visit) == 0:
                break
            current_val = to_visit.dequeue()
        return path

     def get_short_path(self, start, end, li):
        """Retrieves shortest path between nodes."""
        path = []
        while True:
            path.append(end)
            if end is start:
                break
            end = li[end][1]
        return path

    def bellman_ford_helper(self, li, start):
        """Bellman-Ford helper, iterates through graph."""
        for key in li:
            for key2 in self.graph[key]:
                # import pdb; pdb.set_trace()
                if li[key2[0]][0] > li[key][0] + key2[1] and key2[0] != start:
                    new_value = li[key][0] + key2[1]
                    li[key2[0]] = (new_value, key)
        return li

    def bellman_ford(self, start, end):
        """Implementation of Bellman-Ford algorithm."""
        nodes = self.nodes()
        li = {}
        for x in nodes:
            if x == start:
                li[x] = (0, x)
            else:
                li[x] = (float('inf'), 'nan')
        temp_li = self.bellman_ford_helper(li, start)
        while True:
            if temp_li == li:
                return self.get_short_path(start, end, li)
            li = temp_li
            temp_li = self.bellman_ford_helper(li, start)
        return self.get_short_path(start, end, li)

    def dijkstra(self, start, end):
        """Implentation of Dijkstra's algorithm."""
        nodes = self.nodes()
        nodes.remove(start)
        potential_nodes = {}
        for x in nodes:
            potential_nodes[x] = (float('inf'), 'nan')
        li = {}
        li[start] = (0, start)
        for x in self.graph[start]:
            potential_nodes[x[0]] = (x[1], start)
        while True:
            if len(potential_nodes) == 0:
                return self.get_short_path(start, end, li)
            min_node = float('inf')
            min_node_name = ''
            for x in potential_nodes:
                if potential_nodes[x][0] < min_node:
                    min_node = potential_nodes[x][0]
                    min_node_name = x
            for x in self.graph[min_node_name]:
                if potential_nodes[x[0]][0] > x[1] + min_node:
                    potential_nodes[x[0]] = (x[1] + min_node, potential_nodes[x[0]][0])
            li[min_node_name] = (min_node, start)
            potential_nodes.remove(min_node_name)
            start = min_node_name


if __name__ == '__main__':  # pragma: no cover
    graph = Graph()
    graph.add_edge('a', 'b', 1)
    graph.add_edge('b', 'c', 1)
    graph.add_edge('a', 'd', 1)
    graph.add_edge('c', 'e', 1)
    graph.add_edge('a', 'f', 1)
    print('Out put for breadth -first:')
    print(graph.breadth_first_traversal('a'))
    print()
    print('Out put for Depth-frist:')
    print(graph.depth_first_traversal('a'))
