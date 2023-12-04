class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

def walk(curr, path):
    """the step case"""
    if(curr == None):
        return path

    #pre
    path.append(curr.val)

    #recurse
    walk(curr.left, path)
    walk(curr.right, path)

    #post
    return path

def preOrderTraversal(head):
    """Given the head, return an array containing the binary trees elements"""
    return walk(head, [])

if __name__ == "__main__": 
    left_node = Node(1)
    right_node = Node(5)
    bt_head = Node(4, left_node, right_node)
    left_node.left = Node(0)
    left_node.right = Node(2)
    right_node.left = Node(6)
    right_node.right = Node(7)

    preOrderSearchArr = preOrderTraversal(bt_head)
    print(preOrderSearchArr)