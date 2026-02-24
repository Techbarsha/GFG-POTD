class Solution:
    def equalSumSpan(self, a1, a2):
        # code here
        
        # This Code Implemented by Barsha Saha
        
        n = len(a1)
        
        prefix_sum = 0
        max_len = 0
        first_occurrence = {}
        
        for i in range(n):
            prefix_sum += (a1[i] - a2[i])
            
            # Case 1: prefix sum becomes 0
            if prefix_sum == 0:
                max_len = i + 1
            
            # Case 2: prefix sum seen before
            if prefix_sum in first_occurrence:
                length = i - first_occurrence[prefix_sum]
                max_len = max(max_len, length)
            else:
                first_occurrence[prefix_sum] = i
        
        return max_len
        
        
