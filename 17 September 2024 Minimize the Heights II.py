class Solution:
    def getMinDiff(self, arr, k):
        # code edutech barsha
        arr.sort()
        n = len(arr)
        result = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] >= k:
                max_element = max(arr[i-1] + k, arr[-1] - k)
                min_element = min(arr[0] + k, arr[i] - k)
                result = min(result, max_element - min_element)
        
        return result
