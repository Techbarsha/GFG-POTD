class Solution:
    def noOfWays(self, m,n,x):
        # code here
        
        # This code implemented by barsha saha
        dp = [[0]*(x+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, x+1):
                for k in range(1, m+1):
                    if j-k >= 0:
                        dp[i][j] += dp[i-1][j-k]
        
        return dp[n][x]
        
