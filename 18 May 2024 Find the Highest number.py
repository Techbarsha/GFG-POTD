from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
		left, right = 0, len(a) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the next element, move the search to the left half
            if a[mid] > a[mid + 1]:
                right = mid
            else:
                # Move the search to the right half
                left = mid + 1
        
        # When left == right, we have found the peak element
        return a[left]
