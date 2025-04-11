class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        from heapq import heappush,heappop
        g = [[] for _ in range(V)]
        for u,v,w in edges:
            g[u].append((v,w))
        d=[float('inf')] * V
        d[src]=0
        q=[(0,src)]
        while q:
            du,u = heappop(q)
            if du > d[u]: continue
            for v,w in g[u]:
                if du + w <d[v]:
                    d[v] =du + w
                    heappush(q, (d[v],v))
        return d
