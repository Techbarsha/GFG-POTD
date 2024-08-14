class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code edutech barsha
        n = len(str1)
        m = len(str2)
        
        # Initialize the DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        max_length = 0
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return max_length
