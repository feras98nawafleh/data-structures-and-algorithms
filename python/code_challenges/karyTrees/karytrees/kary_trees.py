from collections import deque

class NewNode():

	def __init__(self, val):
		self.key = val
		self.child = []

def preorderTraversal(root):

	Stack = deque([])

	Preorder = []
	Preorder.append(root.key)
	Stack.append(root)
	while len(Stack) > 0:

		flag = 0

		if len((Stack[len(Stack)-1]).child) == 0:
			X = Stack.pop()

		else:
			Par = Stack[len(Stack)-1]

		for i in range(0, len(Par.child)):
			if Par.child[i].key not in Preorder:
				flag = 1
				Stack.append(Par.child[i])
				Preorder.append(Par.child[i].key)
				break
		if flag == 0:
			Stack.pop()
	return Preorder

def devisibleBy3(number):
    return number % 3 == 0

def devisibleBy5(number):
    return number % 5 == 0

def fizzBuzzTree(root):
    preOrder = preorderTraversal(root)
    for i in range(0, len(preOrder)):
        if devisibleBy3(preOrder[i]):
            if devisibleBy5(preOrder[i]):
                preOrder[i] = 'FizzBuzz'
            else:
                preOrder[i] = 'Fizz'
        elif devisibleBy5(preOrder[i]):
            preOrder[i] = 'Buzz'
        else:
            preOrder[i] = str(preOrder[i])

    return preOrder





if __name__ == '__main__':

    root = NewNode(3)
    root.child.append(NewNode(2))
    root.child.append(NewNode(3))
    root.child.append(NewNode(4))
    root.child[0].child.append(NewNode(5))
    root.child[0].child[0].child.append(NewNode(10))
    root.child[0].child.append(NewNode(6))
    root.child[0].child[1].child.append(NewNode(11))
    root.child[0].child[1].child.append(NewNode(12))
    root.child[0].child[1].child.append(NewNode(13))
    root.child[2].child.append(NewNode(7))
    root.child[2].child.append(NewNode(8))
    root.child[2].child.append(NewNode(15))

    print(preorderTraversal(root))
    print(fizzBuzzTree(root))
