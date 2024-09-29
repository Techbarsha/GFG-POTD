class Solution:
    def totalCount(self, k, arr):
        # code here
        
        total_parts = 0
        
        for num in arr:
            total_parts += (num + k - 1) // k
            
        return total_parts
