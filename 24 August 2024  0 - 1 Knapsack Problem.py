def knapSack(self,W, wt, val):
       
        # code edutech barsha
        N = len(val)
        # Initializing the dp table with zeros
        dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
        
        # Fill the dp table
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if wt[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w - wt[i-1]])
                else:
                    dp[i][w] = dp[i-1][w]
        
        # The last cell contains the maximum value we can obtain
        return dp[N][W]
