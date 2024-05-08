class Solution:
	def convert(self, s:str, numRows:int) -> str:
		if numRows == 1: return s

		res = ""
		for r in range(numRows):
			increament = 2 * (numRows - 1)
			for i in rangr(r,len(s), increament):
				res += s[i]
				if (r > 0 and r < numRows -1 and i + increament - 2*r < len(s)):
					res += s[i + increament - 2*r]
		return res