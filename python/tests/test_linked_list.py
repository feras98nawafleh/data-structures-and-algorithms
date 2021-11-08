from code_challenges.linked_list.linked_list import LinkedList
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


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert('Hello')
    ll.insert(1.67)
    return ll
