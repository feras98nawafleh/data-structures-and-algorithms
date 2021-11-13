from code_challenges.linked_list.linked_list import LinkedList, zipLists
from code_challenges.queue.queue import Queue
from code_challenges.stack.stack import Stack
import pytest

def test_empty_linked_list():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


def test_insert_3_values(ll):
    expected = '{5} -> {Hello} -> {1.67} -> NULL'
    actual = ll.__str__()
    assert expected == actual


def test_insert_to_existing_ll(ll):
    ll.insert(True)
    expected = '{5} -> {Hello} -> {1.67} -> {True} -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_includes_found(ll):
    actual = ll.includes(5)
    excepted = True
    assert excepted == actual

def test_includes_notfound(ll):
    actual = ll.includes(50)
    excepted = False
    assert excepted == actual

def test_insert_before(ll):
    ll.insertBefore('Hello', 10)
    expected = '{5} -> {10} -> {Hello} -> {1.67} -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_insert_before_head(ll):
    ll.insertBefore(5, 10)
    expected = '{10} -> {5} -> {Hello} -> {1.67} -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_insert_after(ll):
    ll.insertAfter('Hello', 10)
    expected = '{5} -> {Hello} -> {10} -> {1.67} -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_insert_after_head(ll):
    ll.insertAfter(5, 10)
    expected = '{5} -> {10} -> {Hello} -> {1.67} -> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_kth_from_end(ll):
    actual = ll.kthFromEnd(0)
    expected = 1.67
    assert expected == actual
    actual1 = ll.kthFromEnd(2)
    expected1 = 5
    assert actual1 == expected1


def test_kthFromEnd_wrong_position(ll):
    actual = ll.kthFromEnd(10)
    expected = '10.000000 is greater than the length of the linked list'
    assert expected == actual

def test_kthFromEnd_wrong_input(ll):
    actual = ll.kthFromEnd('input')
    expected = 'input must be an integer number'
    assert expected == actual

def test_zip_lists(ll, ll1):
    actual = zipLists(ll, ll1).__str__()
    expected = '{5} -> {1} -> {Hello} -> {2} -> {1.67} -> {3} -> NULL'
    assert actual == expected


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert('Hello')
    ll.insert(1.67)

    return ll

@pytest.fixture
def ll1():
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(3)

    return ll1

# #_#_#_#_#_#_#_#_END OF LINKEDLIST TESTING _#_#_#_#_#_#_#_#

def test_is_empty():
    queue = Queue()
    assert queue.isEmpty() == True

def test_not_empty():
    queue = Queue()
    queue.Enqueue(1)
    assert queue.isEmpty() == False

def test_counter():
    queue = Queue()
    assert queue.counter() == 0
    queue.Enqueue(1)
    assert queue.counter() == 1
    queue.Enqueue(2)
    assert queue.counter() == 2

def test_Enqueue_and_front():
    queue = Queue()
    assert queue.Front() == None
    queue.Enqueue(1)
    assert queue.isEmpty() == False
    assert queue.Front() == '1'


def test_Dequeue_and_front():
    queue = Queue()
    queue.Enqueue(1)
    queue.Enqueue(2)
    assert queue.Front() == '1'
    queue.Dequeue()
    assert queue.Front() == '2'
    queue.Dequeue()
    assert queue.Front() == None

def test_peek():
    queue = Queue()
    queue.Enqueue(1)
    assert queue.peek() == 'Front -> 1'
    queue.Dequeue()
    assert queue.peek() == None

def test_includes():
    queue = Queue()
    actual = queue.includes('feras')
    expected = False
    assert expected == actual
    queue.Enqueue('feras')
    actual = queue.includes('feras')
    expected = True
    assert expected == actual

def test_includes_after_Dequeue():
    queue = Queue()
    queue.Enqueue('feras')
    queue.Dequeue()
    actual = queue.includes('feras')
    expected = False
    assert expected == actual

def test_doesnt_includes():
    queue = Queue()
    actual = queue.includes('feras')
    expected = False
    assert expected == actual

# #_#_#_#_#_#_#_#_END OF QUEUE TESTING _#_#_#_#_#_#_#_#


def test_is_empty():
    stack = Stack()
    assert stack.isEmpty() == True

def test_not_empty():
    stack = Stack()
    stack.push(1)
    assert stack.isEmpty() == False

def test_length():
    stack = Stack()
    assert stack.length() == 0
    stack.push(1)
    assert stack.length() == 1
    stack.push(2)
    assert stack.length() == 2

def test_push_and_top():
    stack = Stack()
    assert stack.Top() == None
    stack.push(1)
    assert stack.isEmpty() == False
    assert stack.Top() == '1'
    stack.push('Top')
    assert stack.Top() == 'Top'

def test_pop_and_top():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.Top() == '2'
    stack.pop()
    assert stack.Top() == '1'
    stack.pop()
    assert stack.Top() == None

def test_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 'Top -> 1'
    stack.pop()
    assert stack.peek() == None

def test_includes():
    stack = Stack()
    stack.push('feras')
    actual = stack.includes('feras')
    expected = True
    assert expected == actual

def test_includes_after_pop():
    stack = Stack()
    stack.push('feras')
    stack.pop()
    actual = stack.includes('feras')
    expected = False
    assert expected == actual

def test_doesnt_includes():
    stack = Stack()
    actual = stack.includes('feras')
    expected = False
    assert expected == actual



