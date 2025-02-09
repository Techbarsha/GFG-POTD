class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        def dfs(node):
            if not node:return 0
            l = max(0,dfs(node.left))
            r = max(0,dfs(node.right))
            self.res = max(self.res,l+r+node.data)
            return max(l,r) + node.data
            
        self.res = float('-inf')
        dfs(root)
        
        return self.res
