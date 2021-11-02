import math

def insertShiftList(myList, number):
    position = math.ceil(len(myList) / 2)

    newList = [None]*(len(myList) + 1)
    newList[position] = number

    for index,i in enumerate(myList):

        if newList[index] == None:
           newList[index]=(i)
           index += 1

        else:
            newList[index+1]=(i)

    myList = newList
    return myList

if __name__ == "__main__":
    myList = [1, 2, 3, 5, 6, 7]
    print(insertShiftList(myList, 4))




