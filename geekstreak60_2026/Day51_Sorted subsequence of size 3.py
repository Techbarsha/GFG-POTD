class Solution:
    def find3Numbers(self, arr):
        # Code Here
        
        # This code implemented by Barsha Saha
        n = len(arr)
        if n < 3:
            return []
            
        smaller = [-1] * n
        greater = [-1] * n
        
        # Fill smaller[]
        min_index = 0
        for i in range(1, n):
            if arr[i] <= arr[min_index]:
                min_index = i
                smaller[i] = -1
            else:
                smaller[i] = min_index
        # Fill greater[]
        max_index = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_index]:
                max_index = i
                greater[i] = -1
            else:
                greater[i] = max_index
        # Find valid triplet
        for i in range(n):
            if smaller[i] != -1 and greater[i] != -1:
                return [arr[smaller[i]], arr[i], arr[greater[i]]]
        
        return []
        
        
        
