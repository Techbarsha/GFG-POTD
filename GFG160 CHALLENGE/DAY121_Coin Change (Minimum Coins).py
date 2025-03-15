class Solution:
	def minCoins(self, coins, sum):
		# code here
		dp = [float('inf')] * (sum + 1)
		dp[0] = 0
		
		for c in coins:
		    for j in range(c, sum+1):
		        dp[j] = min(dp[j], dp[j-c] + 1)
		return -1 if dp[sum] == float('inf') else dp[sum] 
