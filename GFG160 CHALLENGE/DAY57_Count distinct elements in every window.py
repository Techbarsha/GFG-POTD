class Solution:
    def countDistinct(self, arr, k):
        # Code here
        result = []
        
        for i in range(len(arr)-(k-1)):
            result.append(len(set(arr[i:i+k])))
            
        return result    
