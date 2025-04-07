class Solution:
    def isCycle(self, V, edges):
        # code here
        g = [[] for _ in range(V)]
        in_d = [0]*V
        for u,v in edges: g[u].append(v); in_d[v] += 1
        q = [i for i in range(V) if in_d[i] == 0]
        c = 0
        while q:
            u=q.pop(0); c+=1
            for v in g[u]:
                in_d[v] -= 1
                if in_d[v] == 0: q.append(v)
        return c!= V
