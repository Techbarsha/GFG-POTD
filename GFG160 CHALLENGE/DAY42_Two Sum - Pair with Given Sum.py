class Solution:
	def twoSum(self, arr, target):
		# code here
		
		seen = {}
		
        for i, num in enumerate(arr):
            complement = target - num
            
            if complement in seen:
                return True
            seen[num] = i
            
        return False
