class Vertex:
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return f'<Vertex: {self._value}>'

    def __hash__(self):
        return hash(id(self))

class Edge:
    def __init__(self, u, v, x):
        self._first = u
        self._second = v
        self._value = x

    def __repr__(self):
        return f'<Edge ({self._value}): {self._first} --> {self._second}>'

    def endpoints(self):
        return (self._first, self._second)

    def opposite(self, v):
        return self._second if v is self._first else self._first

    def value(self):
        return self._value

    def __hash__(self):
        return hash((self._first, self._second))

class Graph:
    def __init__(self, adj_map=None):
        if adj_map:
            self._adj_map = adj_map
        else:
            self._adj_map = {}

    def get_vertices(self):
        return self._adj_map.keys()

    def get_edges(self):
        """Return a set of all edges of the graph."""
        result = set()
        for secondary_map in self._adj_map.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Returns the edge from u to v, or None if not adjacent."""
        return self._adj_map[u].get(v)

    def degree(self, u):
        """Returns the number of edges incident to vertex u."""
        return len(self._adj_map[u])

    def get_adjacent_vertices(self, u):
        """Return a list of the adjacent vertices of a given vertex."""
        return list(self._adj_map[u].keys())

    def get_incident_edges(self, u):
        """Returns edges incident to vertex u."""
        return list(self._adj_map[u].values())

    def add_vertex(self, value):
        vertex = Vertex(value)
        self._adj_map[vertex] = {}
        return vertex

    def add_edge(self, u, v, x=None):
        edge = Edge(u, v, x)
        self._adj_map[u][v] = edge
        self._adj_map[v][u] = edge

    def get_adj_map(self):
        return self._adj_map

    def get_adj_matrix(self):
        all_vertices = list(self._adj_map.keys())
        return [[int(bool(self._adj_map[u].get(v))) for v in all_vertices] for u in all_vertices]

# kysymys 3. Implement a Dijkstra's shortest path function
def dijkstra_shortest_path(source_vertex, destination_vertex, graph):
    """
    Calculate the shortest path (in distance value) between given vertices
    
    Parameters:
    - source_vertex: The source vertex
    - destination_vertex: The destination vertex
    - graph: The graph in question
    
    Returns: a tuple containing the minimum distance between vertices and a list of
             vertices that form the minimum path from one vertex to the other.
    """
    # Ensure unvisited_vertices is a list so it supports removal.
    unvisited_vertices = list(graph.get_vertices())
    shortest_path_table = {vertex: {'shortest': float('inf'), 'previous': None} for vertex in unvisited_vertices}
    shortest_path_table[source_vertex]['shortest'] = 0

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_path_table[vertex]['shortest'])
        if shortest_path_table[current_vertex]['shortest'] == float('inf'):
            break  # If the smallest distance is infinite, stop the loop.
        unvisited_vertices.remove(current_vertex)
        for adjacent_vertex in graph.get_adjacent_vertices(current_vertex):
            if adjacent_vertex in unvisited_vertices:
                edge = graph.get_edge(current_vertex, adjacent_vertex)
                if edge:  # Ensure there is an edge
                    tentative_distance = shortest_path_table[current_vertex]['shortest'] + edge.value()
                    if tentative_distance < shortest_path_table[adjacent_vertex]['shortest']:
                        shortest_path_table[adjacent_vertex]['shortest'] = tentative_distance
                        shortest_path_table[adjacent_vertex]['previous'] = current_vertex

    path = []
    current = destination_vertex
    while current:
        path.append(current)
        current = shortest_path_table[current]['previous']
    path.reverse()

    return shortest_path_table[destination_vertex]['shortest'], path



#TESTING

# Prepare the vertices and edges
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')

AB = Edge(A, B, 2)
AC = Edge(A, C, 4)
BD = Edge(B, D, 5)
CD = Edge(C, D, 9)
CE = Edge(C, E, 3)
DF = Edge(D, F, 2)
EF = Edge(E, F, 2)

# Setup adjacency map for the graph
adj_map = {
    A: { B: AB, C: AC },
    B: { A: AB, D: BD },
    C: { A: AC, D: CD, E: CE },
    D: { B: BD, C: CD, F: DF },
    E: { C: CE, F: EF },
    F: { D: DF, E: EF }
}

# Initialize the graph
g = Graph(adj_map)

# Convert vertices to a list before calling Dijkstra's
unvisited_vertices = list(g.get_vertices())  # Convert dict_keys to a list
result_af = dijkstra_shortest_path(A, F, g)
print("Shortest path from A to F:", result_af)

result_cd = dijkstra_shortest_path(C, D, g)
print("Shortest path from C to D:", result_cd)


