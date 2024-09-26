class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        
        max_steps = 0
        current_steps = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                current_steps += 1
                max_steps = max(max_steps, current_steps)
            else:
                current_steps = 0
        
        return max_steps
