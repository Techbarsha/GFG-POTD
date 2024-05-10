class Solution:
    
     def CombinationSum2(self, arr, n, k):
        # code here
         # Sort the array to handle duplicates and improve efficiency
        arr.sort()
        
        # Initialize variables to store results and current combination
        result = []
        current_combination = []
        
        # Define the backtracking function
        def backtrack(start, target):
            # If the target is reached, add the current combination to the result
            if target == 0:
                result.append(current_combination[:])
                return
            
            # Iterate through the array starting from 'start' index
            for i in range(start, n):
                # Skip duplicates to avoid duplicate combinations
                if i > start and arr[i] == arr[i - 1]:
                    continue
                
                # Check if current element can be a part of the combination
                if arr[i] <= target:
                    current_combination.append(arr[i])
                    # Recursively find combinations with remaining elements
                    backtrack(i + 1, target - arr[i])
                    # Backtrack by removing the last element to explore other possibilities
                    current_combination.pop()
        
        # Start backtracking from index 0 with the target value 'k'
        backtrack(0, k)
        return result
