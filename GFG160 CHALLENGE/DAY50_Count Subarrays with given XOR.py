class Solution:
    def subarrayXor(self, arr, k):
        # code here
        
        xor_count = {}
        prefix_xor = 0
        count = 0
        
        for num in arr:
            prefix_xor ^= num
            
            if prefix_xor == k:
                count += 1
                
            target = prefix_xor ^ k
            
            if target in xor_count:
                count += xor_count[target]
                
            xor_count[prefix_xor] = xor_count.get(prefix_xor, 0) + 1
            
        return count  
