class Solution:
    def findMinCost(self, x, y, costX, costY):
        n = len(x)
        m = len(y)
        
        # Create a DP table with (n+1) x (m+1) dimensions
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Initialize the base cases
        for i in range(1, n + 1):
            dp[i][0] = i * costX  # Cost of deleting all characters from x[0:i] to match an empty y
        for j in range(1, m + 1):
            dp[0][j] = j * costY  # Cost of deleting all characters from y[0:j] to match an empty x
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)
        
        # The answer is in dp[n][m]
        return dp[n][m]
