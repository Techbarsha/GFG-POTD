class Solution:
    def countFreq(self, arr, target):
        #code here
        
        # Find the first occurrence of the target
        left = bisect.bisect_left(arr, target)
        
        # Find the position after the last occurrence of the target
        right = bisect.bisect_right(arr, target)
        
        return right - left
