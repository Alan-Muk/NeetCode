class Solution:
	def minCostTicket(self, days:list[int], cost:list[int]) -> int:
		dp = {}

		# for i in range(len(days) -1, -1, -1):
		# 	dp[i] = float("inf")
		# 	for d, c in zip([1, 7,30], cost):
		# 		j = i
		# 		while j < len(days) and days[j] < days[i] + d:
		# 			j += 1
		# 		dp[i] = min(dp[i], c + dp.get(j, 0))
		# return dp[0]

		def dfs(i):
			if i == len(days):
				return 0
			if i in dp:
				return dp[i]

			dp[i] = float("inf")
			for d, c in zip([1, 7, 30], cost):
				j = i
				while j < len(days) and days[j] < days[i] + d:
					j += 1
				dp[i] = min(dp[i], c + dfs(j))
			return dp[i]

		return dfs(0)