class Solution:
    def subarrayXor(self, arr, k):
        # code here
        # this code implemented by barsha saha
        freq = {}
        
        prefix_xor = 0
        count = 0
        
        for num in arr:
            prefix_xor ^= num  
            
            # If prefix_xor itself equals k
            if prefix_xor == k:
                count += 1
            
            # If (prefix_xor ^ k) seen before
            if (prefix_xor ^ k) in freq:
                count += freq[prefix_xor ^ k]
            
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count
