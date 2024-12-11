class Solution:
    def mergeArrays(self, a, b):
        # code here
        n, m = len(a), len(b)

        def next_gap(gap):
            if gap <= 1:
                return 0
            return (gap + 1) // 2

    
        gap = next_gap(n + m)
        while gap > 0:
            # Compare elements in the first array
            i = 0
            while i + gap < n:
                if a[i] > a[i + gap]:
                    a[i], a[i + gap] = a[i + gap], a[i]
                i += 1

            # Compare elements between the two arrays
            j = gap - n if gap > n else 0
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1

            # Compare elements in the second array
            j = 0
            while j + gap < m:
                if b[j] > b[j + gap]:
                    b[j], b[j + gap] = b[j + gap], b[j]
                j += 1

            gap = next_gap(gap)
