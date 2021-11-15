from queue.queue import Queue, Node

class AnimalShelter:
    def __init__(self):
        self.dogQueue = Queue()
        self.catQueue = Queue()

    def Enqueue(self, animal):
        if animal == 'Dog' or animal == 'dog':
            self.dogQueue.Enqueue(animal)
        elif animal == 'Cat' or animal == 'cat':
            self.catQueue.Enqueue(animal)

    def Dequeue(self, pref):
        if pref == 'Dog' or pref == 'dog':
            self.dogQueue.Dequeue()
        elif pref == 'Cat' or pref == 'cat':
            self.catQueue.Dequeue()
        else:
            return None



