class Solution:
    def maxChocolate(self, grid):
        # code here
        # This code implemented by Barsha Saha
        n = len(grid)
        m = len(grid[0])
        
        # dp[j1][j2] = max chocolates from current row
        dp = [[0] * m for _ in range(m)]
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[j1][j2] = grid[n-1][j1]
                else:
                    dp[j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        # Fill from bottom to top
        for i in range(n-2, -1, -1):
            temp = [[0] * m for _ in range(m)]
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float('-inf')
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            nj1 = j1 + dj1
                            nj2 = j2 + dj2
                            if 0 <= nj1 < m and 0 <= nj2 < m:
                                if j1 == j2:
                                    value = grid[i][j1]
                                else:
                                    value = grid[i][j1] + grid[i][j2]
                                
                                value += dp[nj1][nj2]
                                maxi = max(maxi, value)
                    
                    temp[j1][j2] = maxi
            
            dp = temp
        
        return dp[0][m-1]
        
        
        
