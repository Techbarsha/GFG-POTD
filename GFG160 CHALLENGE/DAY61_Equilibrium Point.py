class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        
        n = len(arr)
        right_sum = sum(arr)
        left_sum = 0
        
        for i in range(n):
            right_sum -= arr[i]
            if (left_sum == right_sum):
                return i
                
            left_sum += arr[i]
            
        return -1  
