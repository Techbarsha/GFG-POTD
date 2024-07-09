class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # code here
        if not mat or not mat[0]:
            return 0
        
        # Create a DP table with the same dimensions as the matrix
        dp = [[0] * m for _ in range(n)]
        max_side = 0
        
        # Fill the DP table
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:  # If we're on the first row or first column
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # Update the maximum side length
                    max_side = max(max_side, dp[i][j])
        
        return max_side
