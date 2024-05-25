class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        #code here
        count = 0
        ans = 0
        for i in range(n):
            if arr[i] <= k:
                count += arr[i]
            else:
                count = 0
            ans = max(count, ans)
        return ans
