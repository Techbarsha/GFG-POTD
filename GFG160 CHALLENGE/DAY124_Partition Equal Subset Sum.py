class Solution:
    def equalPartition(self, arr):
        # code here
        s = sum(arr)
        if s%2: return False
        target,dp = s//2,[False]*(s//2+1)
        dp[0] = True
        for num in arr:
            for j in range(target,num-1,-1):
                dp[j] |= dp[j-num]
        return dp[target]
