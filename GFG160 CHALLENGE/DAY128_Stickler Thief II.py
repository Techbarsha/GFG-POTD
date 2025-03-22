class Solution:
    def maxValue(self, arr):
        # code here
        
        if len(arr) == 1:
            return arr[0]
            
        def rob(l,r):
            prev2=prev1=0
            
            for i in range(l,r+1):
                prev2,prev1=prev1,max(prev1,prev2+arr[i])
                
            return prev1
            
        return max(rob(0,len(arr)-2),rob(1,len(arr)-1))
