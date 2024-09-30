class Solution:
    def kPalindrome(self, str, n, k):
        # code here
        reverse_str = str[::-1]
        
        # Create a dp array to store the lengths of LCS
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if str[i - 1] == reverse_str[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The minimum deletions required to make the string a palindrome
        min_deletions = n - dp[n][n]
        
        # Check if the minimum deletions required is less than or equal to k
        if min_deletions <= k:
            return 1
        else:
            return 0
