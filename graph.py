# Name: Shawn Neville
# Student ID: 001158357


# Vertex class for each address.
# Big-O: O(n)
class Vertex:
    def __init__(self, address):
        self.address = address
        self.visited = False
        self.predecessor = None
        self.min_distance = float('inf')
        #self.min_distance = sys.maxsize

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority


# Graph is used for shortest path algorithm.
# Big-O: O(n)
class Graph:
    def __init__(self):
        # Each vertex in adjacency list has list of connected vertices
        self.adjacency_list = {}
        # key in dict. is two vertices. The value is their edge weight
        self.edge_weights = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex_a, vertex_b, weight):
        if weight != '':
            self.edge_weights[vertex_a, vertex_a] = weight
            self.edge_weights[(vertex_b, vertex_a)] = weight
            self.adjacency_list[vertex_a].append(vertex_b)

    # Function returns edge weight between two vertices
    # Space-time complexity: O(n)
    def get_weight(self, vertex_a, vertex_b):
        if self.edge_weights[vertex_a, vertex_b]:
            weight = self.edge_weights[vertex_a, vertex_b]
            return weight
        elif self.edge_weights[vertex_b, vertex_a]:
            weight = self.edge_weights[vertex_b, vertex_a]
            return weight

