class Solution:
    def canSplit(self, arr):
        #code edutech barsha
        total_sum = sum(arr)
        
        # If total sum is odd, can't split into two equal parts
        if total_sum % 2 != 0:
            return False
        
        left_sum = 0
        target = total_sum // 2
        
        for num in arr:
            left_sum += num
            if left_sum == target:
                return True
        
        return False
