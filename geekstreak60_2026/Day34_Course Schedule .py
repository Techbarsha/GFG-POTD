from collections import deque
class Solution:
    def canFinish(self, n, prerequisites):
        # code here 
        # This code implemented by Barsha Saha
        # Build graph and indegree array
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for x, y in prerequisites:
            graph[y].append(x)   # y → x
            indegree[x] += 1
        
        # Initialize queue with nodes having 0 indegree
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == n
        
        
