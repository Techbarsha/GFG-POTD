class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        
        # This code implemented by Barsha Saha
        prefix_sum = 0
        max_len = 0
        first_occurrence = {}
        
        for i in range(len(arr)):
            
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            # Case 1: whole subarray from 0 to i is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # Case 2: check if (prefix_sum - 1) existed before
                if (prefix_sum - 1) in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[prefix_sum - 1])
            
           
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i
        
        return max_len
        
        
