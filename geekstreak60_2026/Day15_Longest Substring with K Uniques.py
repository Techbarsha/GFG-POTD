class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        # This code implemented by barsha saha
        left = 0
        max_len = -1
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            # shrink window if distinct chars > k
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            if len(freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len
        
        
