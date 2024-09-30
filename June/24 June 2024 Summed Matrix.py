#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
       # Calculate the start of the valid range for i
        start = max(1, q - n)
        
        # Calculate the end of the valid range for i
        end = min(n, q - 1)
        
        # If the start value is greater than the end value, there are no valid cells
        if start > end:
            return 0
        
        # The number of valid i values is the range from start to end, inclusive
        return end - start + 1
