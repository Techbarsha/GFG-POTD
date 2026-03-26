import heapq
class Solution:
    def countPaths(self, V, edges):
        # code here
        # This code implemented by Barsha Saha
        MOD = 10**9 + 7
        
        # Build graph
        adj = [[] for _ in range(V)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        
        dist = [float('inf')] * V
        ways = [0] * V
        dist[0] = 0
        ways[0] = 1
        pq = [(0, 0)]  # (distance, node)
        
        # Dijkstra
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nei, time in adj[node]:
                new_dist = d + time
                
                # Found shorter path
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))
                
                # Found another shortest path
                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[V - 1] % MOD
        
        
        
