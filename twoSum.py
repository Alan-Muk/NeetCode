### given an array return indices of the two numbers that add up to target
class Solution:
	def twoSum(self, nums:list[int], target:int) -> list[int]:
		prevMap = {}  # vlaue:index

		for i, n in enumerate(nums):
			diff = target - n 
			if diff in  prevMap:
				return[prevMap[diff], i] 
			prevMap[n] = i 