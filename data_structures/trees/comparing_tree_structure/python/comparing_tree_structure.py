class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def compare(a, b):
    if a is None and b is None:
        return True
    
    if a is None or b is None:
        return False
    
    if a.val != b.val:
        return False
    
    return compare(a.left, b.left) and compare(a.right, b.right)


if __name__ == "__main__":
    """Comparing one tree to another ensuring structure and contents are identical"""
    tree_one = Node(4, Node(2, None, None), Node(5, None, None))
    tree_two = Node(4, Node(2, None, None), Node(5, None, None))
    tree_three = Node(4, Node(2, Node(5, None, None)))

    print(compare(tree_one, tree_two))

    print(compare(tree_one, tree_three))
