class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        # Calculate the sums of both arrays
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Calculate the difference
        diff = sum_a - sum_b
        
        # If the difference is odd, we can't split it into two equal parts
        if diff % 2 != 0:
            return -1
        
        # Target difference to find
        target = diff // 2
        
        # Use a set for quick lookup of elements in array a
        set_a = set(a)
        
        # Iterate through elements in array b
        for b_j in b:
            if (b_j + target) in set_a:
                return 1
        
        # If no such pair is found
        return -1
