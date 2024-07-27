class Solution:
	def removeDups(self, str):
		# code here edutechbarsha
		ans = ""
        for char in str:
            if char not in ans:
                ans += char
        return ans
