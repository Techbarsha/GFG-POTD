class Solution:
    def findMaxDiff(self, arr):
        # code edutech barsha
        n = len(arr)
        s1, s2 = [], []
        v1, v2 = [0] * n, [0] * n
        
        for i in range(n):
            while s1 and s1[-1] >= arr[i]:
                s1.pop()
            v1[i] = s1[-1] if s1 else 0
            s1.append(arr[i])
        
        for i in range(n-1, -1, -1):
            while s2 and s2[-1] >= arr[i]:
                s2.pop()
            v2[i] = s2[-1] if s2 else 0
            s2.append(arr[i])
        
        ans = float('-inf')
        for i in range(n):
            ans = max(ans, abs(v1[i] - v2[i]))
        
        return ans
