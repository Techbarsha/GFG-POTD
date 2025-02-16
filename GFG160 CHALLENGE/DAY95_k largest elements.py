class Solution:
	def kLargest(self, arr, k):
		# Your code here
		arr.sort(reverse=True)
		return arr[:k]
