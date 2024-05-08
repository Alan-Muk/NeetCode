## given an integer array of nums sorted in ascending order, return an array of tha squares of each number

class solution:
	def sortedSquares(self, nums:list[int]) -> list[int]:
		res = []

		l, r = 0; len(nums) -1

		while l <= r:
			if nums[l]*nums[l] > nums[r]*nums[r]:
				res.append(nums[l]*nums[l])
				l +=1
			else:
				res.append(nums[r]*nums[r])
				r -=1

		return res[::-1]