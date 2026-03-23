class Solution:
    def longestCycle(self, V, edges):
        # code here
        # This code implemented by Barsha Saha
        adj = [-1] * V
        for u, v in edges:
            adj[u] = v
        
        visited = [False] * V
        ans = -1
        
        for i in range(V):
            if not visited[i]:
                curr = i
                step_map = {}
                step = 0
                
                while curr != -1 and not visited[curr]:
                    visited[curr] = True
                    step_map[curr] = step
                    step += 1
                    curr = adj[curr]
                
                if curr != -1 and curr in step_map:
                    ans = max(ans, step - step_map[curr])
        
        return ans
        
        
        
