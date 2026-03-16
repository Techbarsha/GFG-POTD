'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def countAllPaths(self, root, k):
        # code here
        # This code implemented by Barsha Saha
        prefix = {0: 1}
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.data
            
            count = prefix.get(curr_sum - k, 0)
            
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)
