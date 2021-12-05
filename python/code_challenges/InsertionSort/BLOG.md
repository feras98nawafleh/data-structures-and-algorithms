# Tracing of insertion sorting

Normal Array [8,4,23,42,16,15]


 | arr[i]      | arr[y] | temp | arr |
| ----------- | ----------- |  ----------- |----------- |
|  4           | 8           | 4            | [4, 8, 23, 42, 16, 15]            |
| 23          | 8           | 23           | [4, 8, 23, 42, 16, 15]            |
| 42          | 23          | 42           | [4, 8, 23, 42, 16, 15]            |
| 16          | 42          | 16           | [4, 8, 16, 23, 42, 15]            |
| 15          | 42          | 15           | [4, 8, 15, 16, 23, 42]            |


### In the first pass through of the insertion sort, we will swap between index 0 and 1

### In the second pass through of the insertion sort, we will not swap any indexes

### In the third pass through of the insertion sort, we will  not swap any indexes


### In the fourth pass through of the insertion sort, we will swap any indexes


### In the fifth pass through of the insertion sort, we will swap two times between index 4 and 3 then 3 and 2


### In the sixth pass through of the insertion sort, we will swap three times between index 5 and 4 then 4 and 3 then 3 and 2

![WhiteBoard](https://github.com/feras98nawafleh/data-structures-and-algorithms/blob/main/python/code_challenges/InsertionSort/WhiteBoard.PNG)
