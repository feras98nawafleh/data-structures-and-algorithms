def sumOfMatrix(matrix):
    sumArray = []
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        sumArray.append(sum)
    return sumArray


if __name__ == "__main__":
    print(sumOfMatrix([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]))

