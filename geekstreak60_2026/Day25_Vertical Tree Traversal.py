'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root): 
        # code here
        
         # This code implemented by Barsha Saha
        if not root:
            return []

        # Dictionary to store nodes at each horizontal distance
        hd_map = defaultdict(list)

        # Queue for BFS: (node, horizontal distance)
        q = deque()
        q.append((root, 0))

        while q:
            node, hd = q.popleft()

            # Store node value
            hd_map[hd].append(node.data)

            # Left child
            if node.left:
                q.append((node.left, hd - 1))
            # Right child
            if node.right:
                q.append((node.right, hd + 1))

        # Sort by horizontal distance
        result = []
        for key in sorted(hd_map.keys()):
            result.append(hd_map[key])

        return result
        
         
