##  given an array, move all zeros to the end while maintaining the relative order

class Solution:
	def moveZeros(self, nums:list[int]) -> None:
		l = 0
		for r in range(len(nums)):
			if nums[r]:
				nums[l], nums[r] = nums[r], nums[l]
				l += 1
		return nums