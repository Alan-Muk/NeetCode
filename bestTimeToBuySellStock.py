### array with elements are the price
class Solution:
	def maxProfit(self, proces:list[int]) -> int:
		l, r = 0, 1  #left = buy, right = sell
		maxP = 0

		while r < len(prices):
			#profit
			if prices[l] < prices[r]:
				profit = prices[r] - prices[l]
				maxP = max(profit, maxP)
			else:
				l = r
			r += 1
		return maxP

