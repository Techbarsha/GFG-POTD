class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        total_sum = sum(arr)
        
        # Check if the total sum is divisible by 3
        if total_sum % 3 != 0:
            return [-1, -1]
        
        # Each part's target sum
        target_sum = total_sum // 3
        
        # Initialize variables
        current_sum = 0
        first_split = -1
        second_split = -1
        parts_found = 0
        
        # Traverse the array to find first and second split indices
        for i in range(len(arr)):
            current_sum += arr[i]
            
            # Check if we've reached the target sum for a part
            if current_sum == target_sum:
                parts_found += 1
                
                # Set the first and second split points
                if parts_found == 1:
                    first_split = i
                elif parts_found == 2:
                    second_split = i
                    break  # No need to continue once we have two splits
                
                # Reset current_sum for the next part
                current_sum = 0
        
        # If we have found two split points, return them; otherwise, return [-1, -1]
        if first_split != -1 and second_split != -1:
            return [first_split, second_split]
        else:
            return [-1, -1]
