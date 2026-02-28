class Solution:
    def findClosestPair(self, arr1, arr2, x):
        #code here
        
        # This code implemented by Barsha Saha
        
        i = 0
        j = len(arr2) - 1
        
        min_diff = float('inf')
        closest_pair = [0, 0]
        
        while i < len(arr1) and j >= 0:
            curr_sum = arr1[i] + arr2[j]
            diff = abs(curr_sum - x)
            
            if diff < min_diff:
                min_diff = diff
                closest_pair = [arr1[i], arr2[j]]
            
            if curr_sum > x:
                j -= 1
            else:
                i += 1
        
        return closest_pair
        
        
        
        
