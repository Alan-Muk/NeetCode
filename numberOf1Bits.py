## write a function that takes in an unsigned integer and returns the number of '1' bits

class Solution:
	def hammingWeight(self, n:int) -> int:
		res = 0

		while n:
			# res += n % 2
			# n = n >> 1

			n &= (n - 1)
			res += 1


		return res