#User function Template for python3
class Solution:
    def countgroup(self, a): 
        xs = 0
        n = len(arr)
        for i in range(n):
            xs = xs ^ a[i]
         
        # We can split only if XOR is 0. 
        # Since XOR of all is 0, we can 
        # consider all subsets as one group.
        if xs == 0:
            return (1 << (n-1)) - 1
         
        return 0

