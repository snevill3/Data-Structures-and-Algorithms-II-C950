# Name: Shawn Neville
# Student ID: 001158357


class HashMap:

    # Big-O: O(n)
    def __init__(self, capacity=100):
        # initialize hash table with empty entries
        self.capacity = capacity
        self.map = []
        for i in range(capacity):
            self.map.append([])

    # calculates index from key and returns index
    # Big-O: O(1)
    def _get_hash(self, key):
        return key % self.capacity

    # insert new item into hash table
    # Big-O: O(1)
    def insert(self, package):
        key = package.pkg_id
        key_hash = self._get_hash(key)
        self.map[key_hash].append(package)

    # Big-O: O(n)
    def delete(self, package):
        key = package.pkg_id
        key_hash = self._get_hash(key)
        self.map[key_hash].remove(package)

    # Big-O: O(n)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for i, item in self.map[key_hash]:
                if i == key:
                    return item
        else:
            return None

