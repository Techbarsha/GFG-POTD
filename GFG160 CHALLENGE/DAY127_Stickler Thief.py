class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        dp = [0]*(n+2)
        
        for i in range(n-1,-1,-1):
            dp[i]=max(dp[i+1],arr[i]+dp[i+2])
            
        return dp[0]
