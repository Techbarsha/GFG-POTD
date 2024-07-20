class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7
        
        if len(arr) == 1:
            return arr[0] % MOD
        
        negatives = []
        positives = []
        zero_count = 0
        
        for num in arr:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zero_count += 1
        
        if len(negatives) == 0 and len(positives) == 0:
            return 0
        
        negatives.sort()
        
        if len(negatives) % 2 != 0:
            if len(negatives) == 1 and len(positives) == 0:
                return 0 if zero_count > 0 else negatives[0] % MOD
            negatives.pop()
        
        product = 1
        for num in positives + negatives:
            product = (product * num) % MOD
        
        return product % MOD
