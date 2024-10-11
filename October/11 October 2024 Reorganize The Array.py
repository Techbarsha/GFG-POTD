class Solution:
    def rearrange(self, arr):
        #Code here
        n = len(arr)
        
        for i in range(n):
            while arr[i] != -1 and arr[i] != i:
                correct_idx = arr[i]
                if arr[correct_idx] == correct_idx:
                    break
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        
        for i in range(n):
            if arr[i] != i:
                arr[i] = -1
        
        return arr
