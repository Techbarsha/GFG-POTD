'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    def topView(self, root):
        # code here
        
        # This code implemented by Barsha Saha
        
        if not root:
            return []
        
        q = deque()
        q.append((root, 0))  
        hd_map = {}
        
        while q:
            node, hd = q.popleft()
            
            # store first node at this HD
            if hd not in hd_map:
                hd_map[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        result = []
        
        for key in sorted(hd_map):
            result.append(hd_map[key])
        
        return result
        
        
        
        
