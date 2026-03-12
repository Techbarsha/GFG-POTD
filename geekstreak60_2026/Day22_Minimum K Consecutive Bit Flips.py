class Solution:
    def kBitFlips(self, arr, k):
        # code here
        
        # This code implemented by Barsha Saha
        n = len(arr)
        is_flipped = [0] * n
        
        flip = 0
        ans = 0
        
        for i in range(n):
            
            if i >= k:
                flip ^= is_flipped[i - k]
            
            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1
                
                is_flipped[i] = 1
                flip ^= 1
                ans += 1
        
        return ans
        
