class Solution:
    def countSquare(self, mat, x):
        # code here
        # This code implemented by Barsha Saha
        n = len(mat)
        m = len(mat[0])
        
        # Step 1: Build prefix sum matrix
        prefix = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                prefix[i][j] = (mat[i-1][j-1] 
                                + prefix[i-1][j] 
                                + prefix[i][j-1] 
                                - prefix[i-1][j-1])
        
        count = 0
        
        # Step 2: Try all square sizes
        for size in range(1, min(n, m) + 1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    
                    r1, c1 = i, j
                    r2, c2 = i + size, j + size
                    
                    total = (prefix[r2][c2]
                             - prefix[r1][c2]
                             - prefix[r2][c1]
                             + prefix[r1][c1])
                    
                    if total == x:
                        count += 1
        
        return count
        
