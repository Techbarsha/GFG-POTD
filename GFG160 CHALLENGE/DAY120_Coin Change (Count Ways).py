class Solution:
    def count(self, coins, sum):
        # code here 
        dp = [0] * (sum+1)
        dp[0] =1
        for coin in coins:
            for i in range(coin,sum+1):
                dp[i] += dp[i-coin]
        return dp[-1]   
