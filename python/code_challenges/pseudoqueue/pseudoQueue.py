from code_challenges.stack.stack import Stack

class Pseudo_queue:
    def __init__(self):
        self.firstStack = Stack()
        self.secondStack = Stack()


    def Enqueue(self, value):
        self.firstStack.push(value)
        return value


    def Dequeue(self):
        if self.firstStack.isEmpty():
            raise Exception("Empty Stack")

        while self.firstStack.Top():
            temp1 = self.firstStack.pop()
            self.secondStack.push(temp1)
        temp2 = self.secondStack.pop()

        while self.secondStack.Top():
            temp1 = self.secondStack.pop()
            self.firstStack.push(temp1)
        return temp2


if __name__ == '__main__':
    pseudoQueue = Pseudo_queue()
    pseudoQueue.Enqueue(30)
    pseudoQueue.Enqueue(20)
    pseudoQueue.Enqueue(10)

    print(pseudoQueue.Dequeue())
    print(pseudoQueue.Dequeue())
    print(pseudoQueue.Dequeue())
