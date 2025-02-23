# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        n=len(arr)
        result=[-1]*n
        stack = []
        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                index = stack.pop()
                result[index] = arr[i]
            stack.append(i)
        return result  
