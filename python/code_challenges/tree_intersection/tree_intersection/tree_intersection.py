from trees import BinaryTree, Node
from hashing import HashTable


def tree_intersection(tree1 , tree2):
    tree1 = tree1.pre_order(tree1.root)
    tree2 = tree2.pre_order(tree2.root)

    hashed = HashTable()
    repeat = []

    for node in tree1:

        hashed.add(node,node)


    for node in tree2:

        if hashed.contains(node):
            repeat.append(node)
        hashed.add(node,node)

    if len(repeat)==0:
        return "theres no repeat"

    return repeat


if __name__ == "__main__":
    tree1=BinaryTree()
    tree1.root=Node("A")
    tree1.root.left=Node("B")
    tree1.root.right=Node("C")
    tree1.root.left.left=Node("D")
    tree1.root.left.right=Node("E")
    tree1.root.right.left=Node("F")

    tree2=BinaryTree()
    tree2.root=Node("A")
    tree2.root.left=Node("B")
    tree2.root.right=Node("k")
    tree2.root.left.left=Node("r")
    tree2.root.left.right=Node("x")
    tree2.root.right.left=Node("m")

    print(tree_intersection(tree1,tree2))
