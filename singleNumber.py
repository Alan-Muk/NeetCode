## given a non-emoty array of integers, every element appears twice except for one. find it

class Solution:
	def singleNumber(self, nums:list[int]) -> int:
		res = 0
		for n in nums:
			res = n ^ res
		return res