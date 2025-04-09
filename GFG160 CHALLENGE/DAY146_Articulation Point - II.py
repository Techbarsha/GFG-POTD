class Solution:
    def articulationPoints(self, V, edges):
        # code here
        from collections import defaultdict
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            
        disc,low,time = [-1]*V, [-1]*V,0
        ret = set()
        
        def dfs(u, p=-1):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            children = 0
            for v in g[u]:
                if disc[v] == -1:
                    children += 1
                    dfs(v,u)
                    low[u] = min(low[u], low[v])
                    if p != -1 and low[v] >= disc[u]:
                        ret.add(u)
                elif v != p:
                        low[u] = min(low[u], disc[v])
            if p == -1 and children > 1:
                ret.add(u)
                
        for u in range(V):
            if disc[u] == -1:
                dfs(u)
        return sorted(ret) if ret else [-1] 
