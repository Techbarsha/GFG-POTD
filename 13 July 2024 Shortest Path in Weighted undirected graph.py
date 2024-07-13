from typing import List
import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        # Create the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Initialize the distance array with infinity
        dist = [float('inf')] * (n + 1)
        dist[1] = 0
        
        # Min-heap to store (distance, vertex)
        heap = [(0, 1)]
        
        # To reconstruct the path
        parent = [-1] * (n + 1)

        while heap:
            current_dist, u = heapq.heappop(heap)

            # If we pop a node from the heap with a distance greater than the known shortest distance, skip it
            if current_dist > dist[u]:
                continue

            # Explore the neighbors
            for v, weight in graph[u]:
                distance = current_dist + weight

                # Only consider this new path if it's better
                if distance < dist[v]:
                    dist[v] = distance
                    parent[v] = u
                    heapq.heappush(heap, (distance, v))
        
        # No path found to vertex n
        if dist[n] == float('inf'):
            return [-1]
        
        # Reconstruct the path from n to 1
        path = []
        node = n
        while node != -1:
            path.append(node)
            node = parent[node]
        path.reverse()

        # Return the path with its total weight
        return [dist[n]] + path
