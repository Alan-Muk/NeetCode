## given an integer array cost where cost i is the ith step and once you pay you can climb one or two, starting at 0 or 1

class Solution:
	def minCostClimbingStairs(self, cost:list[int]) -> int:

		cost.append(0)

		for i in range(len(cost) -3, -1, -1):
			cost[i] += min(cost[i + 1],cost[i + 2])

		return min(cost[0], cost[1])