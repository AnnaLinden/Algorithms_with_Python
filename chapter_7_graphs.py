class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        if v in self.graph:
            self.graph[v].append(u)

    def get_adjacent_vertices(self, u):
        return self.graph.get(u,[])

#  Kysymys 1 Implement a DFS traversal function for a graph
def DFS(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.
    """
    # Function should be called without a visited dict
    # as one will be created in the first call.
    # The starting vertex will be added in that case
    if visited is None:
        visited = {u: None}
    # Traverse all adjacents of u
    for v in graph.get_adjacent_vertices(u):
        # Check if the adjacent has been visited before
        if v not in visited:
            # If not visited, add it to the dict
            visited[v] = u
            # And make the recursive call on the vertex
            DFS(graph, v, visited)
    # When the function backtracks to the start,
    # then all nodes and edges have been visited
    # and the list can be returned
    return visited

# Kysymys 2 Implement a BFS traversal function for a graph
def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex u.
    """
    # Prepare variables.
    # The only discovered vertex is the start vertex
    discovered = {start: None}
    # The only vertex in this level is the start vertex
    level = [start]
    while level:
        # Prepare a variable for the next level
        next_level = []
        # Iterate the vertices in this level
        for u in level:
            # Iterate the adjacents of this vertex
            for v in graph.get_adjacent_vertices(u):
                # If the adjacent is not yet in discovered
                if v not in discovered:
                    # Add the adjacent and the edge between them
                    discovered[v] = u
                    # Add also the adjacent to the next level
                    next_level.append(v)
        # When current level is exhausted, advance to the next level
        level = next_level
    return discovered

# Example usage
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

# Now you can test your DFS and BFS functions
visited_dfs = DFS(g, 'A')
print("DFS Visited Order:", visited_dfs)

visited_bfs = BFS(g, 'A')
print("BFS Visited Order:", visited_bfs)