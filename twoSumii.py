### given an array in sorted array in ascending order find two numbers that add up to target
class Solution:
	def twoSum(self, numbers:list[int], target:int) -> list[int]:
		l,r = 0, len(numbers) - 1

		while l < r:
			curSum = numbers[l] + numbers[r]

			if curSum > target:
				r -= 1
			elif curSum < target:
				l += 1
			else:
				return[l+1, r+1]