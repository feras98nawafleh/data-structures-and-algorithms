import math
class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.length += 1
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            self.length += 1


    def includes(self, number):
        flag = False
        current = self.head
        while(current):
            if current.value == number:
                flag = True
                break
            else:
                current = current.next
        return flag

    def insertBefore(self, number, value):
        if self.includes(number):
            if self.head.value == number:
                node = Node(value)
                node.next = self.head
                self.head = node
                self.length += 1
            else:
                current = self.head
                previous = None
                while current.value != number:
                    previous = current
                    current = current.next
                node = Node(value)
                previous.next = node
                node.next = current
                self.length += 1
        else:
            print(f"{number} not found")

    def insertAfter(self, number, value):
        if self.includes(number):
            if self.head.value == number:
                node = Node(value)
                node.next = self.head.next
                self.head.next = node
                self.length += 1
            else:
                current = self.head
                next = None
                while current.value != number:
                    current = current.next
                next = current.next
                node = Node(value)
                current.next = node
                node.next = next
                self.length += 1
        else:
            print(f"{number} not found")

    def kthFromEnd(self, k):
        if type(k) == int:
            if  self.length > k:
                current = self.head
                for i in range(1, self.length - k):
                    current = current.next
                return current.value
            else:
                return ("%f is greater than the length of the linked list" % k)
        else:
            return ("%s must be an integer number" % k)

    # STRETCH GOAL
    def middleNode(self):
        if self.head != None:
            current = self.head
            for i in range(1, math.ceil(self.length / 2)):
                current = current.next
            return current.value

    def __str__(self):
        output = "";
        current = self.head
        while current:
            output += "{"
            output += f"{current.value}"
            output += "} -> "
            current = current.next
        output += "NULL"
        return output

if __name__ == "__main__":

    newList = LinkedList()
    newList.insert(5)
    newList.insert('Hello')
    newList.insert(1.67)
    print(newList) # {5} -> {Hello} -> {1.67} -> NULL
    newList.insertBefore('Hello', 55)
    print(newList) # {5} -> {55} -> {Hello} -> {1.67} -> NULL
    newList.insertAfter('Hello', 55)
    print(newList) # {5} -> {55} -> {Hello} -> {55} -> {1.67} -> NULL
    print(newList.kthFromEnd(4)) # 5
    print(newList.middleNode()) # Hello




