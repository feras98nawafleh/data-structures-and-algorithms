from hashmaprepeated.linked_list import LinkedList
from hashmaprepeated.hashing import HashTable
import re


def repeated(para):

    para = para.lower()
    hashed = HashTable()

    para = re.sub('[^A-Za-z ]+', '', para)
    print(para)
    para = para.split(" ")

    for word in para:

        if word and hashed.contains(word):
            return word

        hashed.add(word, word)

    return "No Repetition"


if __name__ == "__main__":
    print(repeated("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
