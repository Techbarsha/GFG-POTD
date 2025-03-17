class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        d = [False]*(sum+1)
        d[0] = True
        for i in arr:
            for j in range(sum,i-1,-1):
                d[j] = d[j] or d[j-i]
        return d[sum]        
        
