class Solution:
    def floorSqrt(self, n): 
    # code edutechbarsha
        if n == 0 or n == 1:
            return n
        low, high = 0, n
        result = 0  
        while low <= high:
            mid = (low + high) // 2  
            
            
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                low = mid + 1
                result = mid
            else:
                high = mid - 1
        return result
