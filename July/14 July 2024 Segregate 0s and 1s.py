class Solution:
    def segregate0and1(self, arr):
        # Initialize two pointers, left starting from the beginning and right from the end of the array
        left, right = 0, len(arr) - 1

        # Loop until the two pointers meet
        while left < right:
            # Move the left pointer to the right as long as it points to 0
            while left < right and arr[left] == 0:
                left += 1
            # Move the right pointer to the left as long as it points to 1
            while left < right and arr[right] == 1:
                right -= 1
            # If left is still less than right, it means arr[left] is 1 and arr[right] is 0
            # Swap these two elements
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                # Move both pointers inward after the swap
                left += 1
                right -= 1
