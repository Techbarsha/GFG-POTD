class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        MOD = 10**9 + 7
        n = len(s1)
        m = len(s2)
        
        if m == 0:
            return 1
        if n == 0:
            return 0
        
        # Initialize dp arrays for the current and previous rows
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        
        # Base case: An empty s2 can always be formed by any prefix of s1
        for i in range(n + 1):
            prev[0] = 1
        
        # Fill the dp table using optimized space
        for i in range(1, n + 1):
            curr[0] = 1  # An empty string s2 can always be formed by any prefix of s1
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = (prev[j - 1] + prev[j]) % MOD
                else:
                    curr[j] = prev[j] % MOD
            prev, curr = curr, prev  # Move to the next row
        
        return prev[m]
