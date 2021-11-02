def binary_search(myList, n):
    low = 0
    high = len(myList) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if myList[mid] < n:
            low = mid + 1

        elif myList[mid] > n:
            high = mid - 1

        else:
            return mid

    return -1

if __name__ == "__main__":
    myList = [10, 12, 14, 16, 18, 20]
    number = 20
    result = binary_search(myList, number)
    print(result)
