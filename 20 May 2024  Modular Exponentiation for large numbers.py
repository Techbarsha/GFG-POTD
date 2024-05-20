#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		# Code here
		result = 1  # Initialize result
        x = x % m  # Update x if it is more than or equal to m

        while n > 0:
            # If n is odd, multiply x with the result
            if (n % 2) == 1:
                result = (result * x) % m

            # n must be even now
            n = n >> 1  # Divide n by 2
            x = (x * x) % m  # Change x to x^2

        return result
