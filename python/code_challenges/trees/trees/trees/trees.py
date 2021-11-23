class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []

        def _traverse(root = self.root):
            output.append(root.value)
            if root.left is not None:
                _traverse(root.left)
            if root.right is not None:
                _traverse(root.right)
            return output

        return _traverse

    def in_order(self):
        output = []
        def _traverse(root = self.root):

            if root.left is not None:
                _traverse(root.left)

            output.append(root.value)

            if root.right is not None:
                _traverse(root.right)

            return output

        return _traverse

    def post_order(self):
        output = []
        def _traverse(root = self.root):

            if root.left is not None:
                _traverse(root.left)

            if root.right is not None:
                _traverse(root.right)

            output.append(root.value)
            return output
        return _traverse

    def includes(self, value):
        def _traverse(root = self.root):
            flagFound = False
            if root.value == value:
                flagFound = True
            elif root.left is not None:
                _traverse(root.left)
            elif root.right is not None:
                _traverse(root.right)

            return flagFound
        return _traverse


class BinarySearchTree(Tree):
    def __init__(self, tree):
        self.root = tree.root

    def add(self, tree, value):
        node = Node(value)
        def _traverse(root = tree.root):
            if root is None:
                root = node
            if root.left is None:
                _traverse(tree.root.left)
            elif root.right is None:
                _traverse(root.right)
            else:
                _traverse(tree.root.left)
class qNode:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__counter = 0

    def isEmpty(self):
        return self.__counter == 0

    def counter(self):
        return self.__counter

    def Front(self):
        if not self.isEmpty():
            toReturn = self.__front.value
            self.Dequeue()
            return toReturn

    def peek(self):
        if not self.isEmpty():
            return self.__front.value

    def Enqueue(self, value):
        node = qNode(value)
        if self.isEmpty():
            self.__front = node
            self.__rear = node
            self.__counter += 1
        else:
            self.__rear.next = node
            self.__rear = node
            self.__counter += 1

    def Dequeue(self):
        self.__front = self.__front.next
        self.__counter -= 1

    def __str__(self):
        if self.isEmpty():
            return "this stack is empty"

        response = "front -> "
        pointer = self.__front
        for i in range(0, self.__counter):
            response += str(pointer.value)
            response += " -> "
            pointer = pointer.next
        response += "rear"
        return response

def BreadthFirst(tree):
    if tree.root is None:
        return

    queue = Queue()
    output = Queue()
    queue.Enqueue(tree.root)

    while(queue.counter() > 0):

        node = queue.Front()
        output.Enqueue(node.value)
        if node.left is not None:
            queue.Enqueue(node.left)

        if node.right is not None:
            queue.Enqueue(node.right)

    return output



def create_tree():
    tree=Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    return tree

if __name__ == "__main__":
    tree = create_tree()
    traverse= tree.pre_order()
    print(traverse(tree.root))
    traverse = tree.in_order()
    print(traverse(tree.root))
    traverse = tree.post_order()
    print(traverse(tree.root))

    bst = BinarySearchTree(tree)
    found = bst.includes("A")
    print(found(bst.root))

    print(BreadthFirst(tree))
