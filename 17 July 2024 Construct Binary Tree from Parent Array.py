class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # your code here
        n = len(parent)
        nodes = [None] * n
        
        # Initialize all nodes
        for i in range(n):
            nodes[i] = Node(i)
        
        root = None
        
        # Establish the parent-child relationship
        for i in range(n):
            if parent[i] == -1:
                root = nodes[i]
            else:
                p = nodes[parent[i]]
                if p.left is None:
                    p.left = nodes[i]
                else:
                    p.right = nodes[i]
        
        return root
