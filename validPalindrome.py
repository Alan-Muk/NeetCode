## given a string s, determine it is a palindrome

# class Solution:
# 	def validPalindrome(self, s:str) -> bool:
# 		newStr = ""

# 		for c in s:
# 			if c.isalnum():
# 				newStr += c.lower()
# 		return newStr == newStr[::-1]

class Solution:
	def validPalindrome(self, s:str) -> bool:
		l, r = o, len(s) -1

		while l < r:
			while l < r and not self.alphaNum(s[l]):
				l += 1
			while r < l and not self.alphaNum(s[r]):
				r -= 1
			if s[l].lower() != s[r].lower():
				return False
			l, r = l +1, r -1

		return True


	def alphaNum(self, c):
		return (ord('A') <= ord(c) <= ord('Z') or 
			rd('a') <= ord(c) <= ord('z') or 
			ord('0') <= ord(c) <= ord('9'))