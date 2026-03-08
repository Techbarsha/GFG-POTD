class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	# This code implemented by barsha saha
    	s = set(arr)
        n = len(arr)
        
        for i in range(n):
            for j in range(i+1, n):
                val = arr[i]*arr[i] + arr[j]*arr[j]
                c = int(val ** 0.5)
                
                if c*c == val and c in s:
                    return True
        
        return False
        
