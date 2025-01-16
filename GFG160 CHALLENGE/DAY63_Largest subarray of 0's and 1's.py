class Solution:
    def maxLen(self, arr):
        # code here
        prefix_sum = 0
        hash_map = {}
        res = 0
        
        for i in range(len(arr)):
            prefix_sum += -1 if arr[i] == 0 else 1
            
            if prefix_sum == 0:
               res = i + 1
               
            if prefix_sum in hash_map:
                res = max(res, i - hash_map[prefix_sum])
            else:
                hash_map[prefix_sum] = i
                
        return res
