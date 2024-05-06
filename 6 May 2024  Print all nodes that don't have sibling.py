def noSiblingUtil(root, siblings):
    if root is None:
        return
    
    # Check if the current node has exactly one child
    if root.left is None and root.right is not None:
        siblings.add(root.right.data)
    elif root.left is not None and root.right is None:
        siblings.add(root.left.data)
    
    # Recur for left and right subtrees
    noSiblingUtil(root.left, siblings)
    noSiblingUtil(root.right, siblings)
    
    
def noSibling(root):
    # code here
    siblings = set()
    noSiblingUtil(root, siblings)
    
    # Convert the set to a sorted list
    result = sorted(list(siblings))
    
    if len(result) == 0:
        return [-1]  # If all nodes have siblings
    else:
        return result
