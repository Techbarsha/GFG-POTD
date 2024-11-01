#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        
        res = []
        n = len(arr)
        for i in range(n // 2):
            res.append(arr[-(i + 1)]) 
            res.append(arr[i])
            
        if n % 2 == 1:
            res.append(arr[n // 2])
            
        max_sum = 0
        for i in range(n):
            max_sum += abs(res[i] - res[(i + 1) % n])

        return max_sum
