class Solution:
    def findSmallest(self, arr):
        # code here
        res = 1
        
        for num in arr:
            if num > res:
                break
            
            res += num
            
        return res
