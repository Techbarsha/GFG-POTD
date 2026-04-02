class Solution:
    def countWays(self,n,k):
        #code here.
        
        # This code implemented by Barsha Saha
        if n == 1:
            return k
        
        # For n = 2
        same = k * 1          
        diff = k * (k - 1)    
        
        # For n >= 3
        for i in range(3, n + 1):
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            same = new_same
            diff = new_diff
        
        return same + diff
        
