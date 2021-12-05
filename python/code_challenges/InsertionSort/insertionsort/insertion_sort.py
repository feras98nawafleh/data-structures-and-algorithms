def InsertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


if __name__ == "__main__":
    arr = [2, 3, 5, 7, 13, 11]
    print(InsertionSort(arr))
