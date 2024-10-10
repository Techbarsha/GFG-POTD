class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        first_occurrence = {}
        max_dist = 0
        
        for i in range(len(arr)):
            if arr[i] not in first_occurrence:
                first_occurrence[arr[i]] = i
            else:
                max_dist = max(max_dist, i - first_occurrence[arr[i]])
        
        return max_dist
