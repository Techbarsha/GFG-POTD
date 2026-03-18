'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandy(self, root):
        # code here
         # This code implemented by Barsha Saha
        self.moves = 0
        def dfs(node):
            if not node:
                return 0
            # Postorder traversal
            left = dfs(node.left)
            right = dfs(node.right)
            # Count moves required
            self.moves += abs(left) + abs(right)
            # Return excess candies
            return node.data + left + right - 1
        
        dfs(root)
        return self.moves
        
        
