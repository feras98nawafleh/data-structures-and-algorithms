class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.__top = None
        self.__length = 0

    def isEmpty(self):
        return self.__length == 0

    def length(self):
        return self.__length

    def Top(self):
        if not self.isEmpty():
            return str(self.__top.value)
        self.pop()

    def peek(self):
        if not self.isEmpty():
            return "Top -> " + str(self.__top.value)

    def push(self, value):

        node = Node(value)

        if self.isEmpty():
            self.__top = node
            self.__length += 1

        else:
            pointer = self.__top
            self.__top = node
            node.next = pointer
            self.__length += 1

    def pop(self):

        if not self.isEmpty():
            self.__top = self.__top.next
            self.__length -= 1

    def includes(self, element):

        if self.isEmpty():
            return False

        pointer = self.__top
        flag = False
        while pointer is not None:
            if str(pointer.value) == str(element):
                flag = True
                break
            pointer = pointer.next
        return flag


    def __str__(self):

        if self.isEmpty():
            return "this stack is empty"

        response = ""
        pointer = self.__top
        for i in range(0, self.__length):
            response += "\n-----------------\n"
            response += str(pointer.value)
            response += "\n-----------------"
            pointer = pointer.next
        return response


if __name__ == "__main__":
    stack = Stack()
    stack.push("feras")
    stack.push("adel")
    stack.push("nawafleh")
    print(stack)
    print(stack.Top())
    stack.pop()
    stack.pop()
    print(stack)
    print(stack.Top())
