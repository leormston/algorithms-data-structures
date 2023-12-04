class Node:
    def __init__(self, val=None, nextNode=None):
        self.val = val
        self.next = nextNode

class Queue:
    def __init__(self, length = 0, head = None, tail = None):
        self.length = length
        self.head = head
        self.tail = tail 
    
    def enqueue(self, node):
        """enqueue"""
        self.length += 1
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        """dequeue"""
        if self.head == None:
            return None
        else:
            self.length -= 1
            head = self.head
            self.head = self.head.next
            head.next = None
            return head.val

    def peek(self):
        """peek at the first element in the queue"""
        return self.head
    
if __name__ == "__main__":
    q = Queue()
    print(q.peek())
    q.enqueue(Node(4, None))
    print(q.peek().val)
    q.enqueue(Node(5, None))
    print(q.peek().val)
    q.dequeue()
    print(q.peek().val)

    