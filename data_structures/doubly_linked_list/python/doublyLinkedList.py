class Node:
    def __init__(self, val = None, nxt = None, prev = None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class DoublyLinkedList:
    """Doubly Linked List"""

    def __init__(self, length):
        self.length = length

    def getLength(self):
        return self.length
    
    def insertAt(self, index, val):
        print("inserting at a specific index")

    def remove(self, val):
        print("removing a specific val")

    def removeAt(self, index):
        print("removing at given index")
        
    def append(self, val):
        print("appending")

    def prepend(self, val):
        print("prepending")

    def get(self, index):
        print("getting")

if __name__ == "__main__":
    