from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        # code here
        # Initialize dp array with infinity
        dp = [float('inf')] * (w + 1)
        # Base case: 0 kg oranges cost 0
        dp[0] = 0
        
        # Fill the dp array
        for i in range(1, w + 1):
            for j in range(1, n + 1):
                if j <= i and cost[j - 1] != -1:
                    dp[i] = min(dp[i], dp[i - j] + cost[j - 1])
        
        # If dp[w] is still infinity, we cannot form w kg of oranges
        return dp[w] if dp[w] != float('inf') else -1
