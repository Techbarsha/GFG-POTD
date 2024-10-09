class Node:
    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None

class Solution:
    def constructLinkedMatrix(self, mat):
        if not mat:  
            return None
        
        n = len(mat)  
        nodes = [[None for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                nodes[i][j] = Node(mat[i][j])
        
        for i in range(n):
            for j in range(n):
                if j < n - 1:  
                    nodes[i][j].right = nodes[i][j + 1]
                if i < n - 1:  
                    nodes[i][j].down = nodes[i + 1][j]
        
        return nodes[0][0]
        
def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            Rp = Rp.right
        print()  
        Dp = Dp.down
