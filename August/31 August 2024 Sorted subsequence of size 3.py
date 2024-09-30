class Solution:
    def find3Numbers(self, arr):
        # Code edutech barsha
        n = len(arr)
        if n < 3:
            return []
        
        # Initialize left_min array
        left_min = [0] * n
        left_min[0] = arr[0]
        
        # Fill left_min array
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])
        
        # Initialize right_max array
        right_max = [0] * n
        right_max[-1] = arr[-1]
        
        # Fill right_max array
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        
        # Find the triplet
        for j in range(1, n - 1):
            if left_min[j - 1] < arr[j] < right_max[j + 1]:
                return [left_min[j - 1], arr[j], right_max[j + 1]]
        
        return []
