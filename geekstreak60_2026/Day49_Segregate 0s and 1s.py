class Solution:
    def segregate0and1(self, arr):
        # code here
        
        # This code implemented by Barsha Saha
        left = 0
        right = len(arr) - 1
        
        while left < right:
            
            # Move left pointer if element is 0
            if arr[left] == 0:
                left += 1
            # Move right pointer if element is 1
            elif arr[right] == 1:
                right -= 1
            # Swap when left is 1 and right is 0
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        return arr
        
        
