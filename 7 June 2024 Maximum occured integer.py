class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        ##Your code here
         # Initialize frequency array
        freq = [0] * (maxx + 2)
        
        # Mark the frequency changes
        for i in range(n):
            freq[l[i]] += 1
            freq[r[i] + 1] -= 1
        
        # Apply prefix sum to get actual frequencies
        max_count = -1
        max_occurred_int = -1
        current_count = 0
        
        for i in range(maxx + 1):
            current_count += freq[i]
            if current_count > max_count:
                max_count = current_count
                max_occurred_int = i
        
        return max_occurred_int
