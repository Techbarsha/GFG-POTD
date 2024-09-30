from typing import List


class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        # code here
        # Loop through the array till the second last element
        for i in range(n - 1):
            if i % 2 == 0:
                # If the index is even, ensure arr[i] <= arr[i + 1]
                if arr[i] > arr[i + 1]:
                    # Swap elements to satisfy the zigzag condition
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                # If the index is odd, ensure arr[i] >= arr[i + 1]
                if arr[i] < arr[i + 1]:
                     # Swap elements to satisfy the zigzag condition
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
