
def reverseList(myList):
    """
   below line is to print the passed list in reversed order
   using built in functions
    """
    print(myList[::-1])


if __name__=="__main__":
  myList = list(input())
  reverseList(myList)