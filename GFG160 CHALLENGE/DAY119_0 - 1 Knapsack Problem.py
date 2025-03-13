class Solution:
    def knapsack(self, W, val, wt):
        # code here
        n=len(wt)
        dp = [[0]*(n+1) for _ in range(W+1)]
        for W in range(1,W+1):
            for i in range(n):
                dp[W][i+1]=dp[W][i]
                if wt[i]<=W:
                    dp[W][i+1]=max(dp[W][i+1],dp[W-wt[i]][i]+val[i])
        return dp[-1][-1]
