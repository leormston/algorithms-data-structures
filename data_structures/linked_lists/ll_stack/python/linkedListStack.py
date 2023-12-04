class Node:
    def __init__(self, val = None, nextNode = None):
        self.val = val
        self.nextNode = nextNode


class LinkedListStack:
    head = None
    length = 0

    def push(self, val):
        self.length += 1
        new_node = Node(val=val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nextNode=self.head
            self.head = new_node
        
    def pop(self):
        if self.length == 0:
            print("Stack is empty")
        else:
            self.length -= 1
            print(self.head.val)
            if self.length ==1:
                self.head = None
            else:
                self.head=self.head.nextNode

    def peek(self):
        if self.head == None:
            print("Queue is empty")
        else:
            print(self.head.val)

if __name__ == "__main__":
    stack = LinkedListStack()
    stack.peek()
    stack.push(5)
    stack.peek()
    stack.push(4)
    stack.push(3)
    stack.peek()
    stack.pop()
    stack.peek()