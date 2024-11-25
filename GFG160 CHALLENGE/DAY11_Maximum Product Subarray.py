#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	 def maxProduct(self, arr):
		# code here
		n = len(arr)
        if n == 0:
            return 0
        
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        
        for i in range(1, n):
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])
            result = max(result, max_product)
        
        return result
