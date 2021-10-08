# Name: Shawn Neville
# Student ID: 001158357


# Greedy Algorithm to determine the shortest path from a start vertex to each vertex in the graph.
# Algorithm takes the graph and the starting vertex. Sets the starting vertex to 0 distance.
# Since each vertex has a minimum distance of MAX. 0 distance for the starting will determine each edge weight to its
# adjacent Vertices.
# Big-O: O(E log V)
class ShortestPath:

    def __init__(self, graph, start_vertex):
        unvisited = []
        # Add all vertices to unvisited list
        for current_vertex in graph.adjacency_list:
            unvisited.append(current_vertex)

        # start_vertex has a distance of 0 from itself
        start_vertex.min_distance = 0

        # one vertex is removed with each iteration
        # Loops until unvisited list is empty
        while len(unvisited) > 0:
            # visit vertex with minimum distance.
            smallest_index = 0
            for i in range(1, len(unvisited)):
                if unvisited[i].min_distance < unvisited[smallest_index].min_distance:
                    smallest_index = i
            current_vertex = unvisited.pop(smallest_index)
            current_vertex.visited = True

            # Check potential path lengths from the current vertex to all neighbors
            for adj_vertex in graph.adjacency_list[current_vertex]:
                edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.min_distance + edge_weight

                # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
                if alternative_path_distance < adj_vertex.min_distance:
                    adj_vertex.min_distance = alternative_path_distance
                    adj_vertex.predecessor = current_vertex

    # function to find the shortest path to a vertex. Returns the target vertex with an assigned distance.
    # Big-O: O(n)
    def get_shortest_path(self, target_vertex):
        vertex = target_vertex
        while vertex is not None:
            vertex = vertex.predecessor
        return target_vertex


