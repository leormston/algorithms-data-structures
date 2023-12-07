class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def depthFirstSearch(curr, val):
    """Depth First Search"""

    if (curr == None):
        return False
    if (curr.val == val):
        return True
    elif (val > curr.val):
        return depthFirstSearch(curr.right, val)
    elif (val <= curr.val):
        return depthFirstSearch(curr.left, val)

if __name__ == "__main__":
    bt_head = Node(25, 
                   left=Node(23, Node(5, Node(2), None)),
                   right=Node(27, 
                              Node(26), Node(30, left=None, right=Node(100))
                              )
                    )

    print(depthFirstSearch(bt_head, 5)) #true

    print(depthFirstSearch(bt_head, 23)) #true

    print(depthFirstSearch(bt_head, 30)) #true

    print(depthFirstSearch(bt_head, 0)) #false

    print(depthFirstSearch(bt_head, 28)) #false

    print(depthFirstSearch(bt_head, 2356)) #false


