from MergeSort import __version__
from MergeSort.merge_sort import Mergesort

def test_version():
    assert __version__ == '0.1.0'

def test_sorting():
    reversed_arr = [20, 18, 12, 8, 5, -2]
    few_uniques = [5, 12, 7, 5, 5, 7]
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    assert Mergesort(reversed_arr) == [-2, 5, 8, 12, 18, 20]
    assert Mergesort(few_uniques) == [5, 5, 5, 7, 7, 12]
    assert Mergesort(nearly_sorted) == [2, 3, 5, 7, 11, 13]
