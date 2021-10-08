# Name: Shawn Neville
# Student ID: 001158357


class Package:

    def __init__(self, pkg_id, address, city, state, zip, delivery_deadline, pkg_weight, notes):
        self.pkg_id = pkg_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = delivery_deadline
        self.pkg_weight = pkg_weight
        self.notes = notes
        self.delivery_status = 'AT HUB'
        self.package_departure_time = 0
        self.delivery_time = 0
        self.time = 0
        self.status_update = None

    # Print statement for package that is still at hub and not loaded on a truck.
    # Big-O: O(1)
    def not_loaded(self):
        return print('PACKAGE:', self.pkg_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.zip,
                     '|', self.state, '|', self.pkg_weight,  '|', self.delivery_status)

    # Print statement for package that has been loaded onto a truck
    # Big-O: O(1)
    def loaded(self):
        return print('PACKAGE:', self.pkg_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.zip, '|',
                     self.state, '|', self.pkg_weight, '|', 'has been loaded')

    # Print statement for package that is out for delivery
    # Big-O: O(1)
    def on_route(self):
        return print('PACKAGE:', self.pkg_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.zip, '|',
                     self.state, '|', self.pkg_weight, '|', 'on route')

    # Converts time into total minutes.
    # Big-O: O(1)
    def to_minutes(self, time):
        t = time.split(':')
        minutes = (int(t[0]) * 60) + int(t[1])
        return minutes

    # Converts time back into hours and minutes for timestamp.
    # Updates status to delivered with timestamp.
    # Big-O: O(1)
    def set_delivered(self):
        hr = int(self.delivery_time / 60)
        minutes = int(self.delivery_time % 60)
        self.time = str(hr) + ":" + str(minutes).zfill(2)
        self.status_update = 'DELIVERED AT ' + self.time

    # Calculates and updates total delivery time for package in minutes. This is done by taking in miles traveled,
    # multiplying by truck speed in rate of minutes and adding it to departure time.
    # Big-O: O(1)
    def set_timestamp(self, distance):
        self.delivery_time = round(3.33 * distance) + self.package_departure_time

    # Determines the status of each package based on time.
    # Big-O: O(1)
    def lookup(self, minutes):
        minutes = self.to_minutes(minutes)

        if minutes < 480:
            self.not_loaded()

        elif minutes >= 480 and minutes < self.package_departure_time:
            self.loaded()

        elif minutes >= self.package_departure_time and minutes < self.delivery_time:
            self.on_route()

        elif minutes >= self.delivery_time:
            print('PACKAGE:', self.pkg_id, '|', self.address, '|', self.deadline, '|', self.city, '|', self.zip, '|',
                  self.state, '|', self.pkg_weight, '|', self.status_update)

