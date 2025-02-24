class Solution:
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        ans = [0]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if not stack:
                ans[i] = i + 1
            else:
                ans[i] = i-stack[-1]
            stack.append(i)
        return ans
