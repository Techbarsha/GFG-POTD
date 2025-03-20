class Solution:
    def maxProfit(self, prices):
        # code here
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        if n <= 1:
            return 0
        for i in range(1,3):
            dif =- prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], prices[j] + dif)
                dif = max(dif,dp[i-1][j]- prices[j])
                
        return dp[2][n-1] 
