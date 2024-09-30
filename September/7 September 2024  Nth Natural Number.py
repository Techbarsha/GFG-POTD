class Solution:
    def findNth(self,n):
        #code here
        # Initialize the result variable to store the base-9 equivalent
        result = 0
        # Initialize base to 1, which represents the position in the new number system (units, tens, etc.)
        base = 1
        
        # Loop until n becomes 0
        while n > 0:
            # Get the least significant digit in base-9 (by taking n % 9)
            result += (n % 9) * base
            # Move to the next digit by dividing n by 9
            n //= 9
            # Increase the base (move to the next position: units -> tens -> hundreds, etc.)
            base *= 10
        
        # Return the final result, which is the nth natural number after removing numbers with digit '9'
        return result
