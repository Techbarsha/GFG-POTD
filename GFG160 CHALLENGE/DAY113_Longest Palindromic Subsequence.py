class Solution:

    def longestPalinSubseq(self, s):
        # code here
        n=len(s)
        dp=[[0]*n for i in range(n)]
        
        for i in range(n):
            dp[i][i]=1
            
        for j in range(2,n+1):
            for i in range(n-j+1):
                x=i+j-1
                if s[i] == s[x]:
                    dp[i][x]=dp[i+1][x-1]+2
                else:
                    dp[i][x]=max(dp[i+1][x], dp[i][x-1])
                        
        return dp[0][n-1] 
