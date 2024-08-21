from collections import deque, defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code edutech barsha
        # Create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Initialize distances
        distances = [float('inf')] * n
        distances[src] = 0
        
        # BFS queue
        queue = deque([src])
        
        # BFS traversal
        while queue:
            node = queue.popleft()
            current_distance = distances[node]
            
            for neighbor in adj[node]:
                if distances[neighbor] == float('inf'):  # not visited
                    distances[neighbor] = current_distance + 1
                    queue.append(neighbor)
        
        # Replace 'inf' with -1 to indicate unreachable nodes
        return [distance if distance != float('inf') else -1 for distance in distances]
