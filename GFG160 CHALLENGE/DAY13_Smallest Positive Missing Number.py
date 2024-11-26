class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        #Your code here
        n = len(arr)
        
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1
        
        for i in range(n):
            val = abs(arr[i])
            if val <= n:
                arr[val - 1] = -abs(arr[val - 1])
        
        for i in range(n):
            if arr[i] > 0:
                return i + 1
        
        return n + 1
