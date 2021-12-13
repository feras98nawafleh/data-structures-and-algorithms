class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append (self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current_value = self.head
            while current_value.next != None:
                current_value = current_value.next
            current_value.next = node

    def __str__(self):
        output = ""
        current_value = self.head
        # print(current_value)
        while (current_value):
            output += f"{current_value.value} -> "
            current_value = current_value.next
        output += "Null"

        return output
