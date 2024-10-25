class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        
        # Initialize pointers for largest and smallest element
        left, right = 0, len(arr) - 1
        result = []
        
        # Alternate between the largest and smallest elements
        while left <= right:
            if right >= left:
                result.append(arr[right])
                right -= 1
            if left <= right:
                result.append(arr[left])
                left += 1
                
        return result
