class Solution:
    def totalWays(self, arr, target):
        # code here
        
        # This code implemented by Barsha Saha
        total_sum = sum(arr)
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0

        subset_sum = (total_sum + target) // 2
        
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]
        
        
