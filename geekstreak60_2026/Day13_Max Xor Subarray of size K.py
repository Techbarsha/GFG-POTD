class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        
        # This code implemented by barsha saha
        n = len(arr)
        
        # Calculate XOR of first window
        current_xor = 0
        for i in range(k):
            current_xor ^= arr[i]
        max_xor = current_xor
        
        # Slide the window
        for i in range(k, n):
            current_xor ^= arr[i - k]
            current_xor ^= arr[i]
            max_xor = max(max_xor, current_xor)
        
        return max_xor
        
        
       
