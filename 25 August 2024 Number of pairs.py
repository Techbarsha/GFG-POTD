import math
class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        #code edutech barsha
        n = len(arr)
        m = len(brr)
        a = []*n
        b = []*m
        count = 0
        for y in arr:
            a.append(math.log(y)/y)
        for x in brr:
            b.append(math.log(x)/x)
        
        a.sort()
        b.sort()
        
        for i in range(m):
            idx = bisect.bisect_right(a, b[i])
            count += n-idx
        
        return count
