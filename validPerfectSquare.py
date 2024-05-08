## given a positive integer, write a function which returns True if nums is a perfect square

# class Solution:
# 	def isPerfectSquare(self, num:int) -> bool:
# 		for i in range(1, num +1):
# 			if i*i == num:
# 				return True
# 			if i*i > num:
# 				return False

class Solution:
	def isPerfectSquare(self, num:int) -> bool:
		l, r = 1, num
		while l <= r:
			mid = (l + r) //2
			if mid * mid > num:
				r = mid -1
			elif mid * mid < num:
				l = mid +1
			else:
				return True
		return False