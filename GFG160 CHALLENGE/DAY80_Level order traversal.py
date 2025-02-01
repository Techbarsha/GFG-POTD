"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        res = []
        q = deque([root])
        
        if root == None:
            return[]
            
        while q:
            level = []
            size = len(q)
            
            for _ in range(size):
                curr = q.popleft()
                level.append(curr.data)
                
                if(curr.left)  : q.append(curr.left)
                if(curr.right) : q.append(curr.right)
                
            res.append(level)
            
            
        return res  
