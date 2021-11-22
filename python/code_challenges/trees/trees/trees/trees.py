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

def BreadthFirst(tree):
    output = []
    current = tree.root
    def _traverse(root = current):
        nonlocal current
        output.append(current.value)
        output.append(current.left.value)
        output.append(current.right.value)
        _traverse(current.left)
        _traverse(current.right)
    _traverse()
    return output




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


def BreadthFirst(tree):
    if tree.root is None:
        return

    queue = []
    output = []
    queue.append(tree.root)

    while(len(queue) > 0):

        output.append(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
            
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
