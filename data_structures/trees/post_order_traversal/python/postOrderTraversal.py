class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def walk(curr, path):
    if curr == None:
        return path

    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.val)

    return path

def postOrderTraversal(head):
    return walk(head, [])

if __name__ == "__main__": 
    left_node = Node(1)
    right_node = Node(5)
    bt_head = Node(4, left_node, right_node)
    left_node.left = Node(0)
    left_node.right = Node(2)
    right_node.left = Node(6)
    right_node.right = Node(7)

    print(postOrderTraversal(bt_head))