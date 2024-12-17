class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        
        if k > len(arr):
            return -1
        
        def isFeasible(mid):
            students = 1
            pages_sum = 0
            for pages in arr:
                if pages_sum + pages > mid:
                    students += 1
                    pages_sum = pages
                    if students > k:
                        return False
                else:
                    pages_sum += pages
            return True
        
        low, high = max(arr), sum(arr)
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            if isFeasible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
