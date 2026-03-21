class Solution:
    def countBSTs(self, arr):
        # code here
        # This code implemented by Barsha Saha
        n = len(arr)
        
        # Store value with original index
        indexed_arr = [(val, i) for i, val in enumerate(arr)]
        
        # Sort by value
        indexed_arr.sort()
        
        # Precompute Catalan numbers
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        # Prepare result
        res = [0] * n
        
        # Compute for each root
        for i in range(n):
            val, original_index = indexed_arr[i]
            
            L = i
            R = n - i - 1
            
            res[original_index] = catalan[L] * catalan[R]
        
        return res
