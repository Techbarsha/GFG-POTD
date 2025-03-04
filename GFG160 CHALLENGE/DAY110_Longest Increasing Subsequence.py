import bisect

class Solution:
    def lis(self, arr):
        # code here
        sub = []  
        for x in arr:
            pos = bisect.bisect_left(sub, x)
            if pos == len(sub):
                sub.append(x)
            else:
                sub[pos] = x
        
        return len(sub)
