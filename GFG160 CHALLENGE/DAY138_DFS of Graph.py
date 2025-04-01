class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        visited = set()
        result = []
        
        def dfs_util(node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            for neighbor in adj[node]:
                dfs_util(neighbor)
                
        dfs_util(0)
        return result
