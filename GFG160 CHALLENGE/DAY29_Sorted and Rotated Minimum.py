class Solution:
    def findMin(self, arr):
        #complete the function here
        
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
    # If mid element is less than the last element, the minimum is on the left side
            if arr[mid] < arr[high]:
                high = mid
                
    # If mid element is greater than the last element, the minimum is on the right side
            elif arr[mid] > arr[high]:
                low = mid + 1
            else:  
                high -= 1
        
        return arr[low]
