### climbing a staircase with n steps, 1 or 2 steps
## Fibinacci sequence/ Bottom-Up Dynamic solution
class Solution:
	def climbStairs(self, n:int) -> int:
		one, two = 1, 1

		for i in range(n-1):

			temp = one
			one = one + two
			two = temp

		return one 