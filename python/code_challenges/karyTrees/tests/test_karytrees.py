from karytrees import __version__
from karytrees.kary_trees import NewNode, fizzBuzzTree


def test_version():
    assert __version__ == '0.1.0'

def test_fizz_buzz():
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

    actual = fizzBuzzTree(root)
    expected = ['Fizz', '2', 'Buzz', 'Buzz', 'Fizz',
                '11', 'Fizz', '13', '4', '7', '8', 'FizzBuzz']
    assert actual == expected
