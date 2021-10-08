# Name: Shawn Neville
# Student ID: 001158357

from hashmap import *
from package import *
import csv


class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.package_list = HashMap()
        self.truck_departure_time = 0
        self.travel = 0
        self.total_cost = 0

    # Gets the package for each truck. Set the package departure time based on the departure time of the truck that
    # will deliver the package.
    # Big-O: O(1) O(n^2)
    def get_package(self, id):
        with open('WGUPS Package File.csv', 'r') as csv_packages:
            csv_reader = csv.reader(csv_packages, delimiter=',')

            for row in csv_reader:
                pkg = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if id == pkg.pkg_id:
                    self.package_list.insert(pkg)

            for i in self.package_list.map:
                for j in i:
                    if self.truck_id == 1:
                        j.package_departure_time = self.truck_departure_time
                    elif self.truck_id == 2:
                        j.package_departure_time = self.truck_departure_time
                    elif self.truck_id == 3:
                        j.package_departure_time = self.truck_departure_time

            return self.package_list

    # Set the travel time for the truck
    # Big-O: O(1)
    def set_travel_time(self, distance):
        self.travel = round(3.33 * distance) + self.truck_departure_time

