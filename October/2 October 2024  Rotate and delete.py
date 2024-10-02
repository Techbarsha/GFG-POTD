class Solution:
    def rotateDelete(self,  arr):
        # code here
        sz = len(arr)
        n = sz
        for k in range(1, sz // 2 + 1):
            arr = [arr[-1]] + arr[:-1]  
            delete_index = n - k  
            del arr[delete_index]
            
            n -= 1
        return arr[0]
