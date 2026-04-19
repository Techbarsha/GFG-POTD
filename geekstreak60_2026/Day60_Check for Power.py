class Solution:
    def isPower(self, x, y):
        # code here
        # This code implemented by Barsha Saha
        if x == 1:
            return y == 1
    
        while y % x == 0:
            y //= x
        return y == 1
