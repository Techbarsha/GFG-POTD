class Solution:
	def countStrings(self,n):
    	# code here
        # This code implemented by Barsha Saha
        if n == 1:
            return 2
        if n == 2:
            return 3
            
        # dp[1], dp[2]
        a, b = 2, 3 
        
        for i in range(3, n + 1):
            a, b = b, a + b
        
        return b
        
        
