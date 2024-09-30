from typing import List


class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        # code here
         # Create a list to store the length of the longest subsequence ending at each index
        dp = [0] * n

        ans = 0
        # Traverse the array from the end to the beginning
        for i in range(n - 1, -1, -1):
            maxi = 0
            # Check for elements that differ by 1 in the remaining part of the array
            for j in range(i + 1, n):
                if abs(a[i] - a[j]) == 1:
                    maxi = max(maxi, dp[j])
            # Update the dp array with the length of the longest subsequence ending at index i
            dp[i] = 1 + maxi
            # Update the answer with the maximum value in dp array
            ans = max(ans, dp[i])

        return ans
