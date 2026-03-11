class Solution:
    def sumSubMins(self, arr):
        # code here
        # This code implemented by Barsha Saha
        n = len(arr)
        ple = [0]*n
        nle = [0]*n
        stack = []
        
        # Previous Less Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                ple[i] = i - stack[-1]
            else:
                ple[i] = i + 1
            
            stack.append(i)
        
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nle[i] = stack[-1] - i
            else:
                nle[i] = n - i
            
            stack.append(i)
        
        ans = 0
        
        for i in range(n):
            ans += arr[i] * ple[i] * nle[i]
        
        return ans
        
