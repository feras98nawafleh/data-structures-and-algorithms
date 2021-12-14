from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import left_join
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_left_join(dict1, dict2):
    expected = [['hi', 'hello', 'good by'], ['dad', 'father', 'mother'], ['block', 'prevent', 'NULL']]
    actual = left_join(dict1, dict2)
    assert expected == actual

def test_left_join_no_match(dict1, dict3):
    expected = [['hi', 'hello', 'NULL'], ['dad', 'father', 'NULL'], ['block', 'prevent', 'NULL']]
    actual = left_join(dict1, dict3)
    assert expected == actual

def test_left_join_full_match(dict1, dict4):
    expected = [['hi', 'hello', 'good by'], ['dad', 'father', 'mother'], ['block', 'prevent', 'allow']]
    actual = left_join(dict1, dict4)
    assert expected == actual

def test_left_join_empty_hashmap2(dict1):
    dict = {}
    expected = [['hi', 'hello', 'NULL'], ['dad', 'father', 'NULL'], ['block', 'prevent', 'NULL']]
    actual = left_join(dict1, dict)
    assert expected == actual

def test_left_join_empty_hashmap1(dict1):
    dict = {}
    expected = []
    actual = left_join(dict, dict1)
    assert expected == actual

@pytest.fixture
def dict1():
    dict1 = {
    'hi':'hello',
    'dad': 'father',
    'block': 'prevent'
    }
    return dict1

@pytest.fixture
def dict2():
    dict2 = {
    'hi':'good by',
    'dad': 'mother'
    }
    return dict2

@pytest.fixture
def dict3():
    dict3 = {
    'welcome':'go away',
    'true': 'false'
    }
    return dict3

@pytest.fixture
def dict4():
    dict4 = {
    'hi':'good by',
    'dad': 'mother',
    'block': 'allow'
    }
    return dict4
