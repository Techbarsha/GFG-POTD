class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(1, min(k, i) + 1):
                dp[i] = min(dp[i], dp[i-j] + abs(arr[i] - arr[i-j]))
        return dp[-1]
