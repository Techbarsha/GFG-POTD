class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	non_zero_index = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1
