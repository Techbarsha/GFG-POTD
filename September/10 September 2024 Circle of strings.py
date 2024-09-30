from collections import defaultdict, deque
class Solution:
    def isCircle(self, arr):
        # code here
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for word in arr:
            start = word[0]
            end = word[-1]
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        for node in set(in_degree.keys()).union(out_degree.keys()):
            if in_degree[node] != out_degree[node]:
                return 0
        visited = set()
        start_node = arr[0][0]  
        
        def bfs(node):
            queue = deque([node])
            visited.add(node)
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        bfs(start_node)
        for node in graph.keys():
            if node not in visited and (out_degree[node] > 0 or in_degree[node] > 0):
                return 0
        
        return 1
