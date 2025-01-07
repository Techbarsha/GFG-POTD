class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        
        f = {}
        c = 0
        
        for i in arr:
            s = target - i
            
            if s in f:
                c += f[s]
                
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
                
        return c   
