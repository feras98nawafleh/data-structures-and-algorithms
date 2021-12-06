def Mergesort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        # sort the left side
        Mergesort(left)
        # sort the right side
        Mergesort(right)
        # merge the sorted left and right sides together
        Merge(left, right, arr)

    return arr

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    if i == len(left):
        for element in right[j:]:
            arr[k] = element
            k = k + 1
    else:
        for element in left[i:]:
            arr[k] = element
            k = k + 1


if __name__ == "__main__":
    arr = [8, 4, 23, 42, 16, 15]
    print(Mergesort(arr))
