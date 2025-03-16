class Solution:
	def minJumps(self, arr):
	    # code here
	    a,b,c = 0, -1, 0
	    
	    while a < len(arr)-1:
	        mx = max([b+1+i+e for i,e in enumerate(arr[b+1:a+1])])
	        if mx > a:
	            a,b,c = mx,a,c+1
	        else:
	            return -1
	    return c 
