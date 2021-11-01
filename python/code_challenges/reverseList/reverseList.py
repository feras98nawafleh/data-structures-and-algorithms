
def reverseList(myList):
    """
   below line is to print the passed list in reversed order
   using built in functions
    """
    reversedList = myList[::-1]
    return reversedList


if __name__=="__main__":
  myList = list(input())
  print(reverseList(myList))
