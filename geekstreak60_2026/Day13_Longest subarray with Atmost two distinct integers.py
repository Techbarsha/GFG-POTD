class Solution:
    def totalElements(self, arr):
        # Code here
        
        # This code implemented by Barsha Saha
        left = 0
        max_len = 0
        freq = {}
        for right in range(len(arr)):
            freq[arr[right]] = freq.get(arr[right], 0) + 1

            # If more than 2 distinct integers shrink window
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
                
            max_len = max(max_len, right - left + 1)
        return max_len
        
        
        
        
