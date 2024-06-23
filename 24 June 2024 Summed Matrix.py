#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        # Compute the valid range for i
        start = max(1, q - n)
        end = min(n, q - 1)
        
        # Calculate the number of valid i's
        if start > end:
            return 0
        return end - start + 1
