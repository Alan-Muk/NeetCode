## given a signed 32-bit integer x, return x with its digits reversed if it goes outside range return 0
class Solution:
 	def reverse(self, x:int) -> int:
 		# Max value = 2147483647
 		#Max minValue = -2147483648

 		MIN = -2147483648
 		MAX = 2147483647

 		res = 0
 		while x:
 			digit = int(math.fmod(x, 10))
 			x = int(x/10)

 			if (res > MAX // 10 or
 				(res == MAX //10 and digit >= MAX % 10)):
 				return 0
 			if (res < MIN //10 or
 				(res == MIN //10 and digit <= MIN %10)):
 				return 0
 			res = (res * 10) + digit
 		return res