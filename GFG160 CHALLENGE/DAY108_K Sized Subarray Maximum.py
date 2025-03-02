class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        res = []
        n = len(arr)
        i = 0
        j = k-1
        while j != n:
            if i > 0 and res[-1] < arr[j]:
                res.append(arr[j])
                i += 1
                j += 1
            elif i > 0 and res[-1] > arr[j] and res[-1] != arr[i-1]:
                res.append(res[-1])
                i += 1
                j += 1
            else:
                res.append(max(arr[i:j+1]))
                i += 1
                j += 1
                
        return res
