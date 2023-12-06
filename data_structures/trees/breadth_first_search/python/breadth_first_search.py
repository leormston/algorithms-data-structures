class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(curr, val):
    """breadth first search for a val and returns true if it exists"""
    queue = [curr]

    while(len(queue) > 0):
        curr = queue.pop(0)

        if(curr.val == val):
            return True
        
        #see if the left node exists
        if curr.left:
            queue.append(curr.left)
        
        #see if the right node exists
        if curr.right:
            queue.append(curr.right)

    return False

if __name__ == "__main__":
    left_node = Node(1)
    right_node = Node(5)
    bt_head = Node(4, left_node, right_node)
    left_node.left = Node(0)
    left_node.right = Node(2)
    right_node.left = Node(6)
    right_node.right = Node(7)

    print(bfs(bt_head, 7))