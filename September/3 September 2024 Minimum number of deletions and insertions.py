class Solution:
	def minOperations(self, str1, str2):
		# code edutech barsha
		n, m = len(str1), len(str2)
        
        # Create a DP table to store the length of LCS
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Length of the longest common subsequence
        lcs_length = dp[n][m]
        
        # Calculate the minimum operations
        deletions = n - lcs_length
        insertions = m - lcs_length
        
        return deletions + insertions
