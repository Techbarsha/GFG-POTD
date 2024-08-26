class Solution:
    def wildCard(self,pattern, string):
        # Code edutech barsha
        n = len(pattern)
        m = len(string)
        
        # Initialize DP table
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # Empty pattern can match with empty string
        dp[0][0] = True
        
        # Only '*' can match with an empty string
        for i in range(1, n + 1):
            if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return 1 if dp[n][m] else 0
