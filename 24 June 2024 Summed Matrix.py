#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
      low = max(1, q - n)
      high = min(n, q - 1)
    
    # If the range is valid, calculate the count
      if low > high:
         return 0
      else:
         return high - low + 1
