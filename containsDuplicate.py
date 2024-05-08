### given an integer array, return true if any value appears at least twice 

class Solution:
	def containsDuplicates(self, nums: list[int]) -> bool:
		hashset = set()

		for n in nums:
			if n in hashset:
				return True
			hashset.add(n)
		return False