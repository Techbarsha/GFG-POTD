class Solution:
    def isBridge(self, V, edges, c, d):
        adj = [[] for _ in range(V)]
        for u,v in edges:
            if (u==c and v==d) or (u==d and v==c): # this remove the edges between c to d
                continue
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False]*V
        
        def dfs(start):
            visit[start]=True
            for neigh in adj[start]:
                if not visit[neigh]:
                    dfs(neigh)
        dfs(c) # dfs start from c
        return not visit[d]  # checking d is visited or not
