## given an integer array nums and a target, build an expression that can evaluate to target

class Solution:
	def findTargetSum(self, nums:list[int], target:int) -> int:
		dp = {}

		def backtrack(i, total):
			if i == len(nums):
				return 1 if total == target else 0
			if (i, total) in dp:
				return dp[(i, total)]

			dp[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])

			return dp[(i, total)]

		return backtrack(0, 0)
