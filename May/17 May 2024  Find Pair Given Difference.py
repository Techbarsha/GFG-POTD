from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        arr.sort()  # Sort the array first
        left = 0
        right = 1
        
        while right < n:
            if left == right:  # Ensure that left and right are not pointing to the same element
                right += 1
                continue
            
            diff = arr[right] - arr[left]
            
            if diff == x:
                return 1
            elif diff < x:
                right += 1
            else:
                left += 1
        
        return -1
