'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        def inorder(root):
            nonlocal c,ans
            if not root or ans is not None:
                return
            
            inorder(root.left)
            c += 1
            if c == k:
                ans = root.data
                return
            
            inorder(root.right)
            
        c = 0
        ans = None
        inorder(root)
        
        return ans if ans is not None else -1
