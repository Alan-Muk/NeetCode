## given an array og n integers where nums[i] is the range [1,n], return an array of inegers that do not appear in nums

class Solution:
	def findDisapperedNumber(self, nums:list[int]) -> list[int]:

		for n in nums:
			i = abs(n) - 1
			nums[i] = -1 * abs(nums[i])

		res = []
		for i, n in enumerate(nums):
			if n > 0:
				res.append(i+1)
		return res