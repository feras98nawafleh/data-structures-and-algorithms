class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

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
            else:
                current = self.head
                previous = None
                while current.value != number:
                    previous = current
                    current = current.next
                node = Node(value)
                previous.next = node
                node.next = current
        else:
            print(f"{number} not found")

    def insertAfter(self, number, value):
        if self.includes(number):
            if self.head.value == number:
                node = Node(value)
                node.next = self.head.next
                self.head.next = node
            else:
                current = self.head
                next = None
                while current.value != number:
                    current = current.next
                next = current.next
                node = Node(value)
                current.next = node
                node.next = next

        else:
            print(f"{number} not found")


    def __str__(self):
        output = ""
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
    print(newList)
    newList.insertBefore('Hello', 55)
    print(newList)
    newList.insertAfter('Hello', 55)
    print(newList)





