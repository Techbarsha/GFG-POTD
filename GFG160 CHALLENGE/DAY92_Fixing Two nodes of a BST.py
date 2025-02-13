'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def correctBST(self, root):
    # your code here
        def inOrder(node):
            nonlocal prev,first,second
            if node is None:
               return
            inOrder(node.left)
            if prev and prev.data > node.data:
                if not first:
                  first = prev
                second = node
            prev = node
            inOrder(node.right)
        
        prev = None
        first = None
        second = None
        inOrder(root)
        first.data, second.data = second.data, first.data
