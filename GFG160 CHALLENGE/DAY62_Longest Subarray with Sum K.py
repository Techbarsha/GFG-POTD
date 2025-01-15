class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum_map = {}
        prefix_sum = 0
        max_length = 0
        
        for i, num in enumerate(arr):
            prefix_sum += num
            
            if prefix_sum == k:
                max_length = i + 1
                
            if (prefix_sum - k) in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum - k])
                
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i
                
        return max_length  
