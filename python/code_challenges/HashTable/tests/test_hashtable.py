from hash_map import HashTable
from linked_list import LinkedList
import pytest


def test_add(hashed):
    actual = hashed[0]
    expected = [10, 10, 20, 10]
    assert actual == expected

def test_contains(hashed):
    assert hashed[1].contains("feras") == True


def test_get(hashed):
    assert hashed[1].get_value("feras") == 20


@pytest.fixture
def hashed():
    hash_table = HashTable()
    hash_table.add("ahmad", 10)
    hash_table.add("feras", 20)
    hash_table.add("moe", 10)
    hash_table.add("salah", 10)
    arr = []
    for i, item in enumerate(hash_table.map):
        if item:
            if isinstance(item, LinkedList):
                arr.append(item.__str__())
            else:
                arr.append(item)

    return arr, hash_table
