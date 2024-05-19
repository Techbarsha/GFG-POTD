from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
       # Edge case: if the array has only one element, return that element
        if n == 1:
            return arr[0]

        # Binary search to find the closest position
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == k:
                return arr[mid]
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        # left is now the insertion point
        # We need to compare arr[left - 1] and arr[left] if they exist
        closest_value = None
        if left < n:
            closest_value = arr[left]
        if left > 0:
            if closest_value is None or abs(arr[left - 1] - k) < abs(closest_value - k) or \
               (abs(arr[left - 1] - k) == abs(closest_value - k) and arr[left - 1] > closest_value):
                closest_value = arr[left - 1]
        
        return closest_value 
