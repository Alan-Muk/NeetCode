## write a function that reverses a string

class Solution:
	def reversString(self, s:list[str]) -> None:
		l, r = 0, len(s) -1

		while l <= r:
			s[l], s[r] = s[r], s[l]
			l, r = l+1, r-1

class Solution:
	def reversString(self, s:list[str]) -> None:
		stack = []
		for c in s:
			stack.append(c)
		i = 0
		while stack:
			s[i] = stack.pop()
			i += 1

class Solution:
	def reversString(self, s:list[str]) -> None:
		
		def reverse(l,r):
			if l <= r:
				s[l], s[r] = s[r], s[l]
				reverse(l+1, r-1)
		reverse(0, len(s) _1)