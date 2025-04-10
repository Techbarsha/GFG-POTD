class Solution:
    def minCost(self, a):
        # code here
        n,ans = len(a),0
        vis =[0]*n
        d = [float('inf')]*n
        d[0]=0
        for _ in range(n):
            m,u = float('inf'), -1
            for i in range(n):
                if not vis[i] and d[i] < m:
                    m,u = d[i],i
            vis[u] = 1
            ans += m
            for v in range(n):
                if not vis[v]:
                    d[v] = min(d[v], abs(a[u][0] - a[v][0]) + abs(a[u][1] - a[v][1]))
        return ans
