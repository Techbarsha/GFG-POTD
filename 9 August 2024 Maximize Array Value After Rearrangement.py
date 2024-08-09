class Solution:
    def Maximize(self, arr): 
        # Complete the function
        arr.sort()
        
        sum = 0
        mod = 10**9+7
        
        for i in range(len(arr)):
            sum += arr[i] * i
            sum %= mod
            
        return sum    
