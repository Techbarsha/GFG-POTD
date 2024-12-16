class Solution:

    def kthElement(self, a, b, k):
        # code here
        if len(a) > len(b):
            a, b = b, a

        m, n = len(a), len(b)
        
        low, high = max(0, k - n), min(k, m)
        
        while low <= high:
            i = (low + high) // 2
            j = k - i
            a_left_max = a[i - 1] if i > 0 else float('-inf')
            a_right_min = a[i] if i < m else float('inf')
            b_left_max = b[j - 1] if j > 0 else float('-inf')
            b_right_min = b[j] if j < n else float('inf')
            
            if a_left_max <= b_right_min and b_left_max <= a_right_min:
                return max(a_left_max, b_left_max)
            
            elif a_left_max > b_right_min:
                high = i - 1
            else:
                low = i + 1

        return -1
