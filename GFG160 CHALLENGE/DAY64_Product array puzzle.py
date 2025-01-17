class Solution:
    def productExceptSelf(self, arr):
        #code here
        
        n = len(arr)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * arr[i - 1]
            
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * arr[i + 1]
            
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
            
        return result  
