## given an integer aray, find the contiguous subarray within an array containing at least one number with the greatest product

class Solution:
	def maxProduct(self, nums:list[int]) -> int:
		res = max(nums)
		curMin, curMax = 1, 1

		for n in nums:
			if n == 0: continue

			tmp = curMax*n
			curMax = max(n, n*curMax, n*curMin)
			curMin = min(n, n*tmp, n*curMin)
			res = max(res, curMin, curMax)
		return res