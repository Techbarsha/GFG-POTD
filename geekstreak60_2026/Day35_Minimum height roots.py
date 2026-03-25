from collections import defaultdict, deque
class Solution:
    def minHeightRoot(self, V, edges):
        # Code here
        # This code implemented by Barsha Saha
        # Edge case
        if V == 1:
            return [0]
            
        # Build graph
        graph = defaultdict(list)
        degree = [0] * V
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Initialize leaves
        leaves = deque()
        for i in range(V):
            if degree[i] == 1:
                leaves.append(i)
        
        # Remove leaves layer by layer
        remaining_nodes = V
        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count
            
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)
        
