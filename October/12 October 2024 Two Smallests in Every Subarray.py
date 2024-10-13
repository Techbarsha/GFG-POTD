class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        if len(arr) < 2:
            return -1
        
        max_sum = float('-inf')  
        
        for i in range(len(arr) - 1):
            current_sum = arr[i] + arr[i + 1]
            max_sum = max(max_sum, current_sum)
        
        return max_sum
