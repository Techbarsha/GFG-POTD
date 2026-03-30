class Solution:
    def minCost(self, houses):
        # code here
        # This code implemented by Barsha Saha
        n = len(houses)
        visited = [False] * n
        minDist = [float('inf')] * n
        minDist[0] = 0  
        total_cost = 0
        
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or minDist[i] < minDist[u]):
                    u = i
            
            visited[u] = True
            total_cost += minDist[u]
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if dist < minDist[v]:
                        minDist[v] = dist
        
        return total_cost
        
        
