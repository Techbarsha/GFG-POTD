class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        diff_map = {0: 1}  # Base case: the difference is 0 before starting the array
        diff = 0  # Initialize the difference between count(x) and count(y)
        result = 0  # To store the count of sub-arrays
        
        # Traverse the array
        for num in arr:
            # Update the difference based on whether the current number is x or y
            if num == x:
                diff += 1
            elif num == y:
                diff -= 1
            
            # If this diff has been seen before, it means there are sub-arrays that have 
            # equal counts of x and y ending at the current position.
            if diff in diff_map:
                result += diff_map[diff]
            
            # Increment the count of this diff in the map
            diff_map[diff] = diff_map.get(diff, 0) + 1
        
        return result
