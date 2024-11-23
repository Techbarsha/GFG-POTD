class Solution:
    def getMinDiff(self,k, arr):
        # code here
        arr.sort()
        n = len(arr)
        
        ans = arr[-1] - arr[0]
        
        for i in range(1, n):
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[i - 1] + k, arr[-1] - k)
            ans = min(ans, max_height - min_height)
        
        return ans
