from collections import deque, defaultdict

class Solution:
    def minTime(self, root, target):
        # code edutech barsha
        if not root:
            return 0
        
        # To store parent pointers
        parent_map = {}
        target_node = None
        
        # DFS to populate the parent map and find the target node
        def populate_parent_map_and_find_target(node, parent=None):
            nonlocal target_node
            if not node:
                return
            if node.data == target:
                target_node = node
            if parent:
                parent_map[node] = parent
            populate_parent_map_and_find_target(node.left, node)
            populate_parent_map_and_find_target(node.right, node)
        
        populate_parent_map_and_find_target(root)
        
        # BFS to burn the tree
        queue = deque([target_node])
        visited = set([target_node])
        time_to_burn = 0
        
        while queue:
            # Number of nodes in the current level
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                
                # Visit the left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                
                # Visit the right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                
                # Visit the parent node
                if node in parent_map and parent_map[node] not in visited:
                    visited.add(parent_map[node])
                    queue.append(parent_map[node])
            
            # If there are more nodes to process, increment the time
            if queue:
                time_to_burn += 1
        
        return time_to_burn
