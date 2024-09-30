class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        # Initialize a counter to keep track of numbers containing the digit '4'
        count = 0
        
        # Loop through each number from 1 to n
        for i in range(1, n + 1):
            # Convert the current number to a string and check if '4' is a substring
            if '4' in str(i):
                # If '4' is found in the string representation, increment the counter
                count += 1
                
        # Return the total count of numbers containing the digit '4'
        return count
