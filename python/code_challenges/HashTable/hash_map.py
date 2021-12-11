from types import new_class
from linked_list import LinkedList

class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.map = [None]*size

    def custom_hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii*19
        hashed_key = temp_value % self.size
        return hashed_key

    def add(self, key, value):
        hashed_key = self.custom_hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = value
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key, value])
            else:
                chain = LinkedList()
                existing_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(existing_pair)
                chain.add(new_pair)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        return self.map[hashed_key]

    def contains(self, key):
        hashed = self.custom_hash(key)
        try:
            print(key in self.map[hashed].__str__())
            return True
        except:
            return False

    def hash(self, key):
        ascii_sum = 0
        for i in key:
            ascii_sum += ord(i)
        temp = ascii_sum*19
        hashed_key = temp % self.size
        return hashed_key

if __name__ == "__main__":

    hashtable = HashTable()
    hashtable.add("ahmad", 10)
    hashtable.add("feras", 20)
    hashtable.add("moe", 10)
    hashtable.add("salah", 10)

    for index, item in enumerate(hashtable.map):
        if item:
            print(index, item)
