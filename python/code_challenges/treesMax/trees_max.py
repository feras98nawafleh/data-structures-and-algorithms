class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
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

    def find_max(self):
        _max = self.root.value
        def _traverse(root = self.root):
            nonlocal _max
            _max = root.value if root.value > _max else _max
            if root.left:
                _traverse(root.left)
            if root.right:
                _traverse(root.right)
        _traverse()
        return _max

def create_tree():
    tree = BinaryTree()
    tree.root=Node(10)
    tree.root.left=Node(5)
    tree.root.right=Node(11)
    tree.root.left.left=Node(20)
    tree.root.left.right=Node(50)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(30)
    return tree

if __name__ == "__main__":
    tree = create_tree()
    traverse= tree.pre_order()
    print(traverse(tree.root))

    print('max = ', tree.find_max())

