class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr = sorted(arr)
        res = 0
        l = 0
        r = len(arr)-1
        
        while(l<r):
            if arr[l] + arr[r] >= target:
                r -= 1
            else:
                res += r - l
                l += 1
                
                
        return res
