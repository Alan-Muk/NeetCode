## given an integer array of nums containing n + 1 in range [1, n], there is at least one repeated number and return it

class Solution:
	def findDuplicates(self, nums:list[int]) -> int:
		slow, fast = 0, 0

		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break

		slow2 = 0
		while True:
			slow = nums[slow]
			slow2 = nums[slow2]
			if slow == slow2:
				break
		return slow