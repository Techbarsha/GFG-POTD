from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        
        #code here
        n = len(arr)
        if n == 0 or k == 0:
            return []
        result = []
        dq = deque()
        for i in range(n):
            
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result
