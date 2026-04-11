class Solution:
    def countIncreasing(self, arr):
        # code here.
        # This code implemented by Barsha Saha
        n = len(arr)
        count = 0
        length = 1   
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
                count += (length - 1)
            else:
                length = 1
        
        return count
