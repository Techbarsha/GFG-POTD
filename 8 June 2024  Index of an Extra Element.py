class Solution:
    def findExtra(self,n,a,b):
        #add code here
        left, right = 0, n - 2
        
        while left <= right:
            mid = (left + right) // 2
            
            if a[mid] == b[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
