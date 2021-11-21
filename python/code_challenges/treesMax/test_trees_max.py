from trees_max import Node, BinaryTree

def test_tree():
    tree  =  BinaryTree()
    assert tree.root == None

def test_pre_order():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    actual  =  tree.pre_order()
    expected  =  ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual(tree.root) == expected

def test_find_max_character():
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")

    actual = tree.find_max()
    expected = "F"
    assert actual == expected

def test_find_max_number():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(12)
    tree.root.right = Node(20)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(55)
    tree.root.right.left = Node(30)

    actual = tree.find_max()
    expected = 55
    assert actual == expected

