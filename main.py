# Name: Shawn Neville
# Student ID: 001158357

import delivery
import re
from truck import *

# Initialize Trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)


# Starts the delivery program. Sets delivery for truck 1 and 2 at certain times based on the assumptions of the project.
# Truck 3 departure time is based on the complete travel time of truck 1.
# Big-O: O(1)
def run(time):
    truck2.truck_departure_time = 545
    truck1.truck_departure_time = 480
    delivery.delivery(truck1, time)
    truck3.truck_departure_time = truck1.travel
    delivery.delivery(truck2, time)
    delivery.delivery(truck3, time)


# View package status at user input times.
# Big-O: O(n)
def package_statuses(time):
    print('\n================================================================================\n\t\t\t\t\t '
          'PACKAGE STATUSES AT', time, '\n================================================================='
                                       '===============')
    for i in delivery.delivered:
            i.lookup(time)


# Function to view the complete delivery and prints total miles traveled to console.
# Big-O: O(n)
def lookup_all():
    print('\n============================================================\n\t\t\t COMPLETE PACKAGE DELIVERY LIST\n',
          '============================================================')
    for i in delivery.delivered:
        print('PACKAGE:', i.pkg_id, '|', i.address, '|', i.deadline, '|', i.city, '|', i.zip, '|', i.state, '|',
              i.pkg_weight, '|', i.status_update)
    print('\n--------------------- PACKAGES HAVE BEEN DELIVERED WITH A TOTAL DISTANCE OF', round(delivery.total_distance),
          'MILES ---------------------')
    # print distance each truck traveled.
    print('Truck:', truck1.truck_id, 'has returned to the hub with', truck1.total_cost, 'miles traveled.')
    print('Truck:', truck2.truck_id, 'has returned to the hub with', truck2.total_cost, 'miles traveled.')
    print('Truck:', truck3.truck_id, 'has returned to the hub with', truck3.total_cost, 'miles traveled.')


# Function to view each package after a simulation.
# Big-O: O(n)
def lookup_package(option, package_id, time):
    for i in delivery.delivered:
        if option == '1' and i.pkg_id == int(package_id):
            print('Address for package {}: {}'.format(package_id, i.address))
        if option == '2' and i.pkg_id == int(package_id):
            print('City for package {}: {}'.format(package_id, i.city))
        if option == '3' and i.pkg_id == int(package_id):
            print('Zipcode for package {}: {}'.format(package_id, i.zip))
        if option == '4' and i.pkg_id == int(package_id):
            print('State for package {}: {}'.format(package_id, i.state))
        if option == '5' and i.pkg_id == int(package_id):
            print('Deadline for package {}: {}'.format(package_id, i.deadline))
        if option == '6' and i.pkg_id == int(package_id):
            print('Weight of package {}: {}'.format(package_id, i.pkg_weight))
        if option == '7' and i.pkg_id == int(package_id):
            i.lookup(time)

    # Call submenu to give user more options before exiting program
    sub_menu(time)


# function that begins delivery program. user is prompted to enter a time to run the delivery simulation.
# package progress can be viewed based on input time. After time is inputted, the user has option to view complete
# delivery list that displays delivery times for all packages.
# Big-O: O(1)
def user_interface():
    print('==============================\n\t\t MAIN MENU \n==============================')
    print('It is currently 8:00am.')

    time = input('To start deliveries, enter time after 8:00am in a "24-Hour" format, (ex. "13:00" for 1:00pm): ')

    # Loop until user input matches a time of 8:00am or later in 24hr format.
    while not re.match("([1]{1}[0-9]|[0]?[8-9]|2[0-3]):[0-5][0-9]", time):
        time = input('PLEASE enter a time after 8:00am in a valid "24-Hour" format to start the deliveries '
                     '(ex. "13:00" for 1:00PM): ')

    run(time)
    package_statuses(time)
    sub_menu(time)


# Big-O: O(1)
def sub_menu(time):
    print('\n==============================\n\t\t\t MENU \n==============================')
    choice = input('Enter [1] to view complete delivery list\n'
                   'Enter [2] to search for a package\n'
                   'Enter [3] to exit\n: ')

    while choice not in ('1', '2', '3'):
        print('\n==============================\n\t\t\t MENU \n==============================')
        print('PLEASE ENTER A VALID OPTION FROM FOLLOWING LIST')
        choice = input('Enter [1] to view complete delivery list\n'
                       'Enter [2] to search for a package\n'
                       'Enter [3] to exit program\n: ')

    if choice == '1':
        lookup_all()

    elif choice == '2':
        print('\n=========================================\n\t\t Searching package at', time,
              '\n=========================================')
        option = input('Choose one of the following:\n'
                       'Address [1]\n'
                       'City [2]\n'
                       'Zipcode [3]\n'
                       'State [4]\n'
                       'Deadline [5]\n'
                       'Weight [6]\n'
                       'Status [7]\n: ')
        id = input('Enter Package ID: ')

        lookup_package(option, id, time)

    else:
        SystemExit


# Call the interface function to start the program
user_interface()
