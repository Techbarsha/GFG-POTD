from typing import List


class Solution:
    def countPartitions(self, n, d, arr):
        # code here
        
        MOD = 10**9 + 7
        total = sum(arr)
        
        # Check if it's possible to split the array as required
        if total < d or (total - d) % 2 == 1:
            return 0
        
        target = (total - d) // 2
        
        # Initialize dp array
        dp = [0] * (target + 1)
        dp[0] = 1  # There's one way to make the sum 0, which is using no elements
        
        # Fill the dp array
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[target]
