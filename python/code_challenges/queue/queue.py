class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.__front = None
    self.__rear = None
    self.__counter = 0

  def isEmpty(self):
    return self.__counter == 0

  def counter(self):
      return self.__counter

  def Front(self):
      if not self.isEmpty():
        return str(self.__front.value)
        self.Dequeue()

  def peek(self):
      if not self.isEmpty():
        return 'Front -> ' + str(self.__front.value)
  
  def Enqueue(self, value):
    node = Node(value)
    if self.isEmpty():
      self.__front = node
      self.__rear = node
      self.__counter += 1
    else:
      self.__rear.next = node
      self.__rear = node
      self.__counter += 1

  def Dequeue(self):
    self.__front = self.__front.next
    self.__counter -= 1

  def includes(self, element):

    if self.isEmpty():
        return False

    pointer = self.__front
    flag = False
    while pointer is not None:
        if str(pointer.value) == str(element):
            flag = True
            break
        pointer = pointer.next
    return flag

  def __str__(self):
    if self.isEmpty():
        return "this stack is empty"

    response = "front -> "
    pointer = self.__front
    for i in range(0, self.__counter):
        response += str(pointer.value)
        response += " -> "
        pointer = pointer.next
    response += "rear"
    return response

if __name__ == "__main__":
  queue = Queue()
  queue.Enqueue(1)
  queue.Enqueue(2)
  queue.Enqueue(3)
  print(queue) # front -> 1 -> 2 -> 3 -> rear
  queue.Dequeue()
  queue.Dequeue()
  queue.Dequeue()
  print(queue) # this stack is empty
  queue.Enqueue('feras')
  print(queue.includes('feras')) # True
  