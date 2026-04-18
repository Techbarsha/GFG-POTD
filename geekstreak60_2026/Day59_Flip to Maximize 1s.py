class Solution:
    def maxOnes(self, arr):
        # code here
        # This code implemented by Barsha Saha
        # count initial ones
        total_ones = sum(arr)
        
        # apply Kadane
        max_gain = 0
        curr_gain = 0
        
        for num in arr:
            # convert: 0 -> +1, 1 -> -1
            val = 1 if num == 0 else -1
            
            curr_gain = max(val, curr_gain + val)
            max_gain = max(max_gain, curr_gain)
        
        return total_ones + max_gain
        
        
