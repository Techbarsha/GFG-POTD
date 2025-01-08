class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        count = 0
        
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    count += (right - left)
                    right -= 1
                    
                else:
                    left += 1
                    
        return count      
