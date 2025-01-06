class Solution:
    def sumClosest(self, arr, target):
        # code here
        
        if len(arr) <= 1:
            return []
            
        arr.sort()
        n = len(arr)
        i = 0
        j = n - 1
        min_diff =  float('inf')
        res = []
        
        while i < j:
            s = arr[i] + arr[j]
            diff = abs(target - s)
            
            if diff < min_diff:
                min_diff = diff
                res = [arr[i] , arr[j]]
                
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                break
            
            
        return res 
