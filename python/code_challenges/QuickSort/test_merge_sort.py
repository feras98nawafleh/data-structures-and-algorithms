from QuickSort.quick_sort import QuickSort


def test_sorting():
    reversed_arr = [20, 18, 12, 8, 5, -2]
    few_uniques = [5, 12, 7, 5, 5, 7]
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    n = len(reversed_arr) - 1
    assert QuickSort(reversed_arr, 0, n) == [-2, 5, 8, 12, 18, 20]
    assert QuickSort(few_uniques, 0, n) == [5, 5, 5, 7, 7, 12]
    assert QuickSort(nearly_sorted, 0, n) == [2, 3, 5, 7, 11, 13]
