## given an array, calculate the pivot index( index where the sum of the left is equal to sum of right)

class Solution:
	def pivotIndex(self, nums:list[int]) -> int:
		total = sum(nums)

		leftSum = 0
		for i in range(len(nums)):
			rightSum = total - nims[i] - leftSum
			if leftSum == rightSum:
				return i
			leftSum += nums[i]
		return -1