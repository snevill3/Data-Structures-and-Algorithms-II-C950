# Name: Shawn Neville
# Student ID: 001158357

from algorithm import *
from graph import *
import csv

# Trucks are loaded based on project constraints. Each truck can hold up 16 packages
# Truck 1 loaded with packages 13, 15, and 19 that can only be shipped together.
# Truck 2 loaded with packages that arrive at 9:05, and packages that can only be delivered by Truck 2
# Truck 3 loaded with the remaining packages that have no constraints.
truck1_load = [4, 11, 13, 14, 15, 16, 19, 20, 21, 23, 24, 34, 35, 39, 40]
truck2_load = [3, 5, 6, 12, 17, 18, 28, 30, 31, 32, 36, 37, 38]
truck3_load = [1, 2, 7, 8, 9, 10, 22, 25, 26, 27, 29, 33]
total_distance = 0
list_statuses = []
delivered = []


# Read in distance data from csv file and return the data in list.
# Big-O: O(n)
def get_distance_data():
    distance_data = []
    with open('WGUPS Distance Table.csv') as csv_distances:
        csv_dist_reader = csv.reader(csv_distances, delimiter=',')
        for row in csv_dist_reader:
            distance_data.append(row)
    return distance_data


# Uses csv data returned from get_distance_data to add edges to "edges" list that is then used when adding edge weights
# Big-O: O(n^2)
def get_graph(graph):
    edges = []
    global vertex1
    global vertex2
    data = get_distance_data()
    for row in data:
        graph.add_vertex(Vertex(row[1]))  # adds vertex/address to adjacency list in Graph object
    for row in data:
        for i in range(3, len(row)):  # start at index 3 to get only distances
            if row[i] != '':
                edges.append((row[1], data[i - 3][1],
                              float(row[i - 1])))  # data[i-3][1] gets each each pair of address that are connected

    for j in edges:
        for i in graph.adjacency_list:
            if i.address == j[0]:
                vertex1 = i
            if i.address == j[1]:
                vertex2 = i
        graph.add_edge(vertex1, vertex2, j[2])
        graph.add_edge(vertex2, vertex1, j[2])

    return graph


# Finds and returns a vertex in adjacency list.
# Big-O: O(n)
def find_vertex(graph, address):
    for i in graph.adjacency_list:
        if i.address == address:
            return i


# Delivers the packages. Sets the starting vertex to the hub
# Big-O: O(n^3)
def delivery(truck, time):
    undelivered = []
    start_vertex = (None, '4001 South 700 East')
    _smallest = None
    cost = 0
    _package = None

    # Iterates through truck load lists and loads trucks.
    if truck.truck_id == 1:
        for i in truck1_load:
            truck.get_package(i)
    if truck.truck_id == 2:
        for i in truck2_load:
            truck.get_package(i)
    if truck.truck_id == 3:
        for i in truck3_load:
            truck.get_package(i)

    # Iterates through Truck's hash table. Packages are appended to undelivered list.
    for i in truck.package_list.map:
        for j in i:
            undelivered.append((j, j.address))
    undelivered.append(start_vertex)

    # While the list is not empty, function will continue.
    while len(undelivered) != 0:
        # removes the new start_vertex
        undelivered.remove(start_vertex)

        # Creates a new graph after each run through.
        graph = get_graph(Graph())

        # finds and returns a vertex with a matching package address.
        current = find_vertex(graph, start_vertex[1])

        # Shortest path's algorithm object construct takes the new graph and a vertex.
        algorithm = ShortestPath(graph, current)

        for i in undelivered:
            # In each loop iteration the package address is run through shortest_path function.
            # Loops until a smallest weight is determined
            a = algorithm.get_shortest_path(find_vertex(graph, i[1]))

            # If smallest has not been determined, assigns the first vertex as smallest along with its package
            # this is the first step after a package delivery.
            if _smallest is None:
                _smallest = a
                cost = _smallest.min_distance
                _package = i[0]

            # If the new vertex is less than the smallest, new vertex becomes smallest and along with its package
            elif a.min_distance < _smallest.min_distance and a.address != _smallest.address:
                _smallest = a
                cost = _smallest.min_distance
                _package = i[0]

            # If the current vertex is a match for package 9 and time user inputs is greater than or equal to 10:20,
            # the vertex is deleted from undelivered list and package is modified.
            # Corrected vertex is added to undelivered list.
            elif i[0].pkg_id == 9 and a.address == '300 State St' and i[0].to_minutes(time) >= 620:
                print('AT 10:20AM ADDRESS FOR PACKAGE', i[0].pkg_id, 'WAS CORRECTED FROM:', a.address)
                undelivered.remove((i[0], a.address))
                _package = i[0]
                _package.address = '410 S State St'
                _smallest = find_vertex(graph, '410 S State St')
                print('TO CORRECT ADDRESS:', _smallest.address)
                undelivered.append((_package, _smallest.address))

        # After all packages are delivered, the shortest distance to the hub from the last vertex will be found.
        # Calculate final mileage by adding miles from each truck to total miles.
        if len(undelivered) == 0:
            hub = algorithm.get_shortest_path(find_vertex(graph, '4001 South 700 East'))
            truck.total_cost += hub.min_distance
            global total_distance
            total_distance += truck.total_cost
            return

        # After smallest weight is found, distance traveled is added to the total. Updates the package
        # delivery timestamp. Package status is set to delivered. Adds the package to delivered list
        # and assigns the new start vertex. Smallest is set to None.
        truck.total_cost += cost
        truck.set_travel_time(truck.total_cost)
        _package.set_timestamp(truck.total_cost)
        delivered.append(_package)
        _package.set_delivered()
        start_vertex = (_package, _smallest.address)
        _smallest = None

