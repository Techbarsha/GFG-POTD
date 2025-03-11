class Solution:
    def countWays(self, n):
        # code here
        if n == 0 or n==1:
            return 1
        arr=[0]*(n+1)
        arr[0]=1
        arr[1]=1
        for i in range(2,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[-1]
