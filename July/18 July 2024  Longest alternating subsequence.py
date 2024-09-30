class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
        if not arr:
            return 0
        up = 1
        down = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up = down + 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
        
        return max(up, down)
