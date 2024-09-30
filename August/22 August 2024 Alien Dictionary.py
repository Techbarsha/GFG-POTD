from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
         # Your implementation here by edutech barsha
        # Step 1: Create an adjacency list for the graph and an array to count in-degrees
        adj = defaultdict(list)
        in_degree = [0] * k
        
        # Step 2: Build the graph
        for i in range(n - 1):
            word1, word2 = dict[i], dict[i + 1]
            min_length = min(len(word1), len(word2))
            for j in range(min_length):
                if word1[j] != word2[j]:
                    u = ord(word1[j]) - ord('a')
                    v = ord(word2[j]) - ord('a')
                    adj[u].append(v)
                    in_degree[v] += 1
                    break
        
        # Step 3: Topological sort using Kahn's Algorithm (BFS)
        queue = deque([i for i in range(k) if in_degree[i] == 0])
        topo_order = []
        
        while queue:
            u = queue.popleft()
            topo_order.append(chr(u + ord('a')))
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        # If topo_order contains all the characters
        if len(topo_order) == k:
            return ''.join(topo_order)
        else:
            return ""
