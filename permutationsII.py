## given a collection of numbers that might contain duplicates, return all possible unique permutations

class Solution:
	def permutations(self, nums:list[int]) -> list[list[int]]:
		res = []
		perm = []
		count = { n:0 for n in nums}
		for n in nums:
			count[n] += 1


		def dfs():
			if len(perm) == len(nums):
				res.append(perm.copy())
				return

			for n in count:
				if count[n] > 0:
					perm.append()
					count[n] -=1

					dfs()

					count[n] += 1
					perm.pop()
		dfs()
		return res