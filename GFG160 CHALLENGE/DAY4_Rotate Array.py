class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n
        
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # Reverse the first d elements
        reverse(arr, 0, d - 1)
        # Reverse the rest of the array
        reverse(arr, d, n - 1)
        # Reverse the entire array
        reverse(arr, 0, n - 1)
