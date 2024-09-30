from collections import deque
from typing import List

class Solution:
    def bfs(self, adj, start, vis):
        num, edges = 0, 0  # Initialize counters for nodes and edges
        q = deque()  # Initialize a deque for BFS traversal
        q.append(start)  # Add the starting node to the queue
        vis[start] = 1  # Mark the starting node as visited
        
        while q:
            node = q.popleft()  # Dequeue a node for processing
            
            num += 1  # Increment the node count for the component
            edges += len(adj[node])  # Increment the edge count for the component
            
            # Explore neighbors of the current node
            for neighbor in adj[node]:
                if not vis[neighbor]:  # If neighbor is not visited
                    q.append(neighbor)  # Add neighbor to the queue for processing
                    vis[neighbor] = 1  # Mark neighbor as visited
        
        # Check if the component is fully connected (every pair of nodes has an edge between them)
        return num * (num - 1) == edges

    def findNumberOfGoodComponent(self, e: int, v: int, edges: List[List[int]]) -> int:
        # code here
        adj = [[] for _ in range(v+1)]  # Initialize adjacency list
        for edge in edges:
            adj[edge[0]].append(edge[1])  # Add edge from u to v
            adj[edge[1]].append(edge[0])  # Add edge from v to u
        
        vis = [0] * (v+1)  # Initialize visited array
        ans = 0  # Initialize count of good components
        
        # Iterate through each node to check if it forms a fully connected component
        for i in range(1, v+1):
            if self.bfs(adj, i, vis):
                ans += 1  # Increment count if the component is fully connected
        
        return ans  # Return the count of good components
