class Solution:
    def smallestNumber(self, s, d):
        # code here
         # If the sum is greater than the maximum possible sum with d digits, return -1
        if s > 9 * d:
            return "-1"
        
        # Initialize an array to store digits of the result number
        result = [0] * d
        
        # Start from the most significant digit and work our way to the least significant
        for i in range(d - 1, -1, -1):
            if s > 9:
                result[i] = 9
                s -= 9
            else:
                result[i] = s
                s = 0
        
        # Ensure the first digit is not zero by adjusting the first non-zero digit if needed
        for i in range(d):
            if result[i] > 0:
                if i > 0:
                    result[i] -= 1
                    result[0] = 1
                break
        
        # Convert list of digits to string
        result_str = ''.join(map(str, result))
        
        # Return the smallest number as a string
        return result_str
