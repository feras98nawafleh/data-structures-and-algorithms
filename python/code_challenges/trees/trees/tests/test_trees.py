from trees.trees import Tree, Node, BreadthFirst
import pytest



def test_tree():
    tree = Tree()
    assert tree.root == None

def test_pre_order():
    tree = Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    actual = tree.pre_order()
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual(tree.root) == expected

def test_in_order():
    tree = Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    actual = tree.in_order()
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual(tree.root) == expected

def test_post_order():
    tree = Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    actual = tree.post_order()
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual(tree.root) == expected

def test_includes():
    tree = Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")
    
    actual = tree.includes("A")
    assert actual(tree.root) == True

def test_breadth_first():
    tree = Tree()
    tree.root=Node("A")
    tree.root.left=Node("B")
    tree.root.right=Node("C")
    tree.root.left.left=Node("D")
    tree.root.left.right=Node("E")
    tree.root.right.left=Node("F")

    actual = BreadthFirst(tree)
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    assert actual == expected
