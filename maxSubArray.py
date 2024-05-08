### given an array find cotiguous subarray with largest sum
class Solution:
	def maxSubArray(self, nums:list[int]) -> int:
		maxSub = nums[0]
		curSum = 0

		for n in mums:
			if curSum < 0:
				cursum = 0
			curSum += n
			maxSub = max(maxSub, curSum)
		return maxSub