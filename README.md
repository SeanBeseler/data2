# data-structures

## Authors: Sean Beseler and Carlos Cadena

### Linked List with tests.
- push(val) will insert the value ‘val’ at the head of the list
- pop() will pop the first value off the head of the list and return it.
- size() will return the length of the list
- search(val) will return the node containing ‘val’ in the list, if present
- remove(node) will remove the given node from the list
- display() will return a unicode string representing the list as if it were a Python tuple literal
- len(the_list) returns the size of the list
- print(the_list) returns what the display() method returns

### Doubly Linked List with tests.
- push(val) will insert the value val at the head of the list
- append(val) will append the value val at the tail of the list
- pop() will pop the first value off the head of the list and return it
- shift() will remove the last value from the tail of the list and return it.
- remove(val) will remove the first instance of val found in the list, starting from the head
- len(the_list) returns the size of the list

### Stack with tests
- push(value) - Adds a value to the stack. The parameter is the value to be added to the stack.
- pop() - Removes a value from the stack and returns that value.

### Queue
- enqueue(value): adds value to the queue
- dequeue(): removes the correct item from the queue and returns its value
- peek(): returns the next value in the queue without dequeueing it
- size(): return the size of the queue

### Double Ended Queue with tests (deque)
- append(val): adds value to the end of the deque
- appendleft(val): adds a value to the front of the deque
- pop(): removes a value from the end of the deque and returns it
- popleft(): removes a value from the front of the deque and returns it
- peek(): returns the next value that would be returned by pop but leaves the value in the deque
- peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque
- size(): returns the count of items in the queue

### Binary Heap functions with tests.
- push(val): puts a new value into the heap, maintaining the heap property.
- pop(): removes the “top” value in the heap, maintaining the heap property.

### Priority Queue functions with tests.
- insert(value): inserts a value into the queue. Takes an optional argument for that value’s priority, set by default to whatever your lowest priority is (i.e. 0, -99, whatever).
- pop(): removes the most important item from the queue and returns its value.
- peek(): returns the most important item without removing it from the queue.


### Graph with tests. (weighted, traversals, and shortest path)
- g.nodes(): return a list of all nodes in the graph
- g.edges(): return a list of all edges in the graph
- g.add_node(val): adds a new node with value ‘n’ to the graph
- g.add_edge(val1, val2): adds a new edge to the graph connecting the node containing ‘val1’ and the node containing ‘val2’. If either val1 or val2 are not already present in the graph, they should be added. If an edge already exists, overwrite it.
- g.del_node(val): deletes the node containing ‘val’ from the graph; raises an error if no such node exists
- g.del_edge(val1, val2): deletes the edge connecting ‘val1’ and ‘val2’ from the graph; raises an error if no such edge exists
- g.has_node(val): True if node containing ‘val’ is contained in the graph, False if not.
- g.neighbors(val): returns the list of all nodes connected to the node containing ‘val’ by edges; raises an error if val is not in g
- g.adjacent(val1, val2): returns True if there is an edge connecting val1 and val2, False if not; raises an error if either of the supplied values are not in g
- g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
- g.breadth_first_traversal(start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.


## To run tests:
python3 -m venv ENV
source ENV/bin/activate
tox
