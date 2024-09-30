class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        # code edutech barsha
         # Calculate the sum of first n natural numbers
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of elements in the array
        arr_sum = sum(arr)
        
        # The missing number will be the difference between total_sum and arr_sum
        return total_sum - arr_sum
