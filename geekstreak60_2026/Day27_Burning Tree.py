'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def minTime(self, root, target):
        # code here
        # This code implemented by Barsha Saha
        # Create parent mapping and find target node
        parent = {}
        target_node = None
        
        q = deque([root])
        
        while q:
            node = q.popleft()
            
            if node.data == target:
                target_node = node
            
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        
        # BFS to simulate burning
        visited = set()
        q = deque([target_node])
        visited.add(target_node)
        
        time = 0
        
        while q:
            size = len(q)
            burned = False
            
            for _ in range(size):
                node = q.popleft()
                
                # Left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                    burned = True
                
                # Right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                    burned = True
                
                # Parent
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])
                    burned = True
            
            if burned:
                time += 1
        
        return time
        
        
