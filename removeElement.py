## given an integer array nums and an integer val, remove all occurences of val in-place

class Solution:
	def removeElement(self, nums:list[int], val:int) -> int:
		k = 0

		for i in range(len(nums)):
			if nums[i] != val:
				nums[k] = nums[i]
				k += 1
		return k