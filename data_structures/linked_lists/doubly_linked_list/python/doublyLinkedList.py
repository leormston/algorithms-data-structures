class Node:
    def __init__(self, val = None, nxt = None, prev = None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class DoublyLinkedList:
    """Doubly Linked List"""

    def __init__(self, length = 0, head = None, tail=None):
        self.length = length
        self.head = head
        self.tail = tail

    def getLength(self):
        #returns the lenght of the linked list
        return self.length
    
    def insertAt(self, index, val):
        #insert a value at a given index
        if index > self.length or index < 0:
            return "Index out of bounds"
        else:
            self.length += 1
            if index == 0:
                self.prepend(val)
            elif index == self.length:
                self.append(val)
            else:
                curr = self.head
                for i in range(index-1):
                    print(curr.val)
                    curr = curr.nxt
                new_node = Node(val, curr.nxt, curr)
                if curr.nxt:
                    curr.nxt.prev = new_node
                curr.nxt = new_node
                

    def remove(self, val):
        # removing the first occurence of a node with a given value
        curr = self.head
        found = False
        for i in range(self.length):
            curr=curr.nxt
            if curr.val == val:
                found = True
                break
        if found:
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            else:
                if curr.prev:
                    curr.prev.nxt = curr.nxt
                if curr.nxt:
                    curr.nxt.prev = curr.prev
        else:
            return "Value not found in array"


    def removeAt(self, index):
        #removing an element at a given index
        if (index > self.length):
            return "Index is out of range"
        else:
            curr = self.head
            for i in range(index):
                curr = curr.nxt
            
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            else:
                if curr.prev:
                    curr.prev.nxt = curr.nxt
                if curr.nxt:
                    curr.nxt.prev = curr.prev
        
    def append(self, val):
        #Using the tail to add an element to the end of the linked list
        node = Node(val, None, self.tail)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node
        self.length += 1


    def prepend(self, val):
        #insert at the start of the list
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head = node
        self.length += 1
    
    def get(self, index):
        #return the value of a given index in the linked list
        if index > self.length:
            return "Index is out of bounds"
        else:
            curr = self.head
            for i in range(index):
                curr = curr.nxt
            return curr.val

if __name__ == "__main__":
    dll = DoublyLinkedList()


    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.remove(4)
    print(dll.get(3))
    dll.prepend(0)
    print(dll.get(0))
    dll.append(6)
    dll.insertAt(1, 5)
    print(dll.get(1))
    print(dll.removeAt(1))
    print(dll.get(1))







