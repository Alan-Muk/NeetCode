## you are climbing stairs with n steps to reach the top, each ime you can take 1 or 2 steps

class Solution:
	def climbStairs(self, n:int) -> int:
		one, two = 1, 1

		for i in range (n - 1):
			temp = one
			one = one + two
			two = temp

		return one