class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ## code edutech barsha
        
        # Initialize variables
        max_so_far = arr[0]
        current_max = arr[0]

        # Traverse through the array starting from the second element
        for i in range(1, len(arr)):
            
            # Update the current maximum
            current_max = max(arr[i], current_max + arr[i])
            
            # Update the maximum so far
            max_so_far = max(max_so_far, current_max)

        return max_so_far
