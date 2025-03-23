class Solution:
	def countWays(self, digits):
		# Code here
		from functools import lru_cache
		@lru_cache(None)
		def dfs(ix = len(digits)-1):
		    nonlocal digits
		    if ix < 0:
		        return 1
		    ret = 0
		    if 1 <= int(digits[ix]) <= 9:
		        ret += dfs(ix -1)
		    if ix - 1 >= 0 and 10 <= int(digits[ix-1]+digits[ix]) <= 26:
		        ret += dfs(ix-2)
		    return ret
		return dfs()
