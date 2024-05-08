## given a sorted array of distinct integers and a target value, return the index if the target is found else index it can be inserted in order
class Solution:
	def searchInsert(self, nums:list[int], target:int) -> int:
		l, r = 0, len(nums) -1

		while l < r:
			mid = (l + r)//2

			if target == nums[mid]:
				return mid

			if target > nums[mid]:
				l = mid +1
			else:
				r = mid -1

		return l
