import math
class Solution:
    def rectanglesInCircle(self,r):
        #code here
        count = 0
        max_len = 2 * r
        
        for w in range(1, max_len + 1):
            for h in range(1, max_len + 1):
                if w**2 + h**2 <= 4 * r * r:
                    count += 1
        
        return count
