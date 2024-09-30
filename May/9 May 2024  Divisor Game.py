class Solution:
    def divisorGame(self, n):
        #Code here
        # Alice wins if n is even, loses if n is odd
        return n % 2 == 0
