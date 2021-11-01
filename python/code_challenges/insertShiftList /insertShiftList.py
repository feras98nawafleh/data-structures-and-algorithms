import math

def insertShiftlist(myList, number):
    position = math.ceil(len(myList) / 2)
    myList.insert(position, number)

    return myList

if __name__ == "__main__":

    myList = [1, 2, 3, 4, 6]
    print(insertShiftlist(myList, 5))




