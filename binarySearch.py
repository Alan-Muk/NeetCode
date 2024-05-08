## given an array nums which is sorted in ascending order and a target, find a function to search target in nums

class Solution:
	def search(self, nums:list[int], target:int) -> int:
		l, r = 0, len(nums) -1

		while l <= r:
			mid = (l + r) // 2
			if mid < target:
				l = mid + 1
			elif mid > target:
				r = mid - 1
			else:
				return mid
		return -1
