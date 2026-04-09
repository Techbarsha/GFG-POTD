class Solution:
    def intersection(self,a, b):
        # code here
        
        # This code implemented by Barsha Saha
        i, j = 0, 0
        n, m = len(a), len(b)
        result = []

        while i < n and j < m:
            if a[i] == b[j]:
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return result
        
        
