from functools import cmp_to_key
class Solution:

	def findLargest(self, arr):
	    # code here
	    
	    # this code implemented by barsha saha
	    
	    # Convert integers to strings
        arr = list(map(str, arr))
        
        def compare(a, b):
            if a + b > b + a:
                return -1  
            elif a + b < b + a:
                return 1    
            else:
                return 0
        
        arr.sort(key=cmp_to_key(compare))
        
        if arr[0] == "0":
            return "0"
        
        return ''.join(arr)

	    
