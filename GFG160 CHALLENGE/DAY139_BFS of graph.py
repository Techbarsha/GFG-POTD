from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        q = deque()
        v = set()
        res=[]
        v.add(0)
        q.append(0)
        while q:
            node=q.popleft()
            res.append(node)
            for i in adj[node]:
                if i not in v:
                    q.append(i)
                    v.add(i)
        return res
