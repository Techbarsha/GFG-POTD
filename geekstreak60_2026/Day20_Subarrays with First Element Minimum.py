class Solution:
    def countSubarrays(self, arr):
        # code here
        
        # This code implemented by Barsha Saha
        n = len(arr)
        stack = []
        next_smaller = [n] * n
        
        # Find next smaller element to the right
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans += next_smaller[i] - i
        
        return ans
        
