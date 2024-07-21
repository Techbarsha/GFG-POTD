class Solution:
    def findMaxProduct(self, arr):
        # code edutechbarsha
         MOD = 10**9 + 7
        prod = 1
        maxi = float('-inf')
        zero_count = 0
        negative_count = 0
        
        for num in arr:
            if num != 0:
                prod = (prod * num) % MOD
                if num < 0:
                    negative_count += 1
                    maxi = max(maxi, num)
            else:
                zero_count += 1
        
        if zero_count == len(arr):
            return 0
        
        if negative_count % 2 != 0:
            if negative_count == 1 and zero_count > 0 and negative_count + zero_count == len(arr):
                return 0
            prod = (prod * pow(maxi, MOD-2, MOD)) % MOD
        
        return prod % MOD
