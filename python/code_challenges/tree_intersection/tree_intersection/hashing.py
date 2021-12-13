from linked_list import LinkedList


class HashTable:
    def __init__(self,size=1024):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        hashed = self.hash(key)


        if not self.map[hashed]:
            self.map[hashed] = [key ,value]

        else:
            if isinstance(self.map[hashed], LinkedList):
                self.map[hashed].append([key,value])
            else:
                chain = LinkedList()
                existing_pair = self.map[hashed]
                new_pair = [key, value]
                self.map[hashed] = chain
                chain.append(existing_pair)
                chain.append(new_pair)



    def get(self,key):
        hashed = self.hash(key)
        return self.map[hashed]

    def contains(self,key):
        hashed = self.hash(key)
        try:
            return key in self.map[hashed].__str__()
        except:
            return False


    def hash(self,key):
        ascii_sum = 0
        for i in key:
            ascii_sum += ord(i)
        temp = ascii_sum*19
        hashed_key = temp%self.size
        return hashed_key


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.add("key", 10)
    hash_table.add("yo", 20)
    hash_table.add("sos", 20)
    hash_table.add("eky", 10)
    hash_table.add("yek", 10)

    hash_table.add("oy", 30)
    # hash_table.add("sso", 40)

    # print(hash_table.get('hello'))
    # print(hash_table.contains('eky'))

    for i,item in enumerate(hash_table.map):
        if item:
            print(i , item)
