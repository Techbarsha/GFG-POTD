from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def reverseLevelOrder(root):
    # code here
    if not root:
        return []

    result = []
    queue = deque()
    stack = []

    queue.append(root)

    while queue:
        node = queue.popleft()
        stack.append(node.data)

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    while stack:
        result.append(stack.pop())

    return result
