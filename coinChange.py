## you are given  coins of fifferent denominations and a total amount. Write a function to compute the fewest number of coins you need

class Solution:
	def coinChange(self, coins:list[int], amount:int) -> int :
		dp = [amount + 1] * (amount + 1)
		dp[0] = 0 

		for a in range(1, amount+1):
			for c in coins:
				if a - c >= 0:
					dp[a] = min(dp[a], 1 + dp[a - c])

		return dp[amount] if dp[amount] != amount + 1 else -1


