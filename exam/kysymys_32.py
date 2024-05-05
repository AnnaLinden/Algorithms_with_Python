# dijkstra algorithm
import heapq

class Vertex:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label

class Edge:
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost

class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

def get_best_city(graph):
    def dijkstra(start_vertex):
        distances = {vertex: float('infinity') for vertex in graph.adj_matrix}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex.label)]
        
        while priority_queue:
            current_distance, current_label = heapq.heappop(priority_queue)
            
            # Get the vertex object from its label
            current_vertex = next(v for v in graph.adj_matrix if v.label == current_label)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, edge in graph.adj_matrix[current_vertex].items():
                distance = current_distance + edge.cost
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor.label))
        
        return sum(distances.values())
    
    min_cost = float('infinity')
    best_city = None
    
    for city in graph.adj_matrix:
        total_cost = dijkstra(city)
        if total_cost < min_cost:
            min_cost = total_cost
            best_city = city
    
    return (best_city.label, min_cost)

# Example setup
A, B, C, D, E, F, G, H, I, J = [Vertex(x) for x in 'ABCDEFGHIJ']
AB = Edge(A, B, 25)
AD = Edge(A, D, 3)
AG = Edge(A, G, 17)
BC = Edge(B, C, 2)
BD = Edge(B, D, 73)
BE = Edge(B, E, 84)
CF = Edge(C, F, 79)
DE = Edge(D, E, 47)
DH = Edge(D, H, 10)
EF = Edge(E, F, 73)
EH = Edge(E, H, 15)
FJ = Edge(F, J, 48)
GH = Edge(G, H, 38)
HJ = Edge(H, J, 72)

am = {
    A: {B: AB, D: AD, G: AG},
    B: {A: AB, C: BC, D: BD, E: BE},
    C: {B: BC, F: CF},
    D: {A: AD, B: BD, E: DE, H: DH},
    E: {B: BE, D: DE, F: EF, H: EH},
    F: {C: CF, E: EF, J: FJ},
    G: {A: AG, H: GH},
    H: {D: DH, E: EH, G: GH, J: HJ},
    J: {F: FJ, H: HJ}
}
g = Graph(am)
print(get_best_city(g))